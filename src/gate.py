# -*- coding: utf-8 -*-
"""EL GATE DE INTEGRIDAD (manual seccion 2).

Se corre en cada commit. Comprueba, sobre el dataset entero:
  1. esquema completo y sin huecos
  2. reglas de id (docs/REGLAS_DE_ID.md)
  3. fuentes contra la tabla canonica, y sin claves repetidas en un nodo
  4. cero auto-aristas TRAS RESOLVER
  5. cero aristas duplicadas TRAS RESOLVER
  6. cero vueltas en los pares bidireccionales, SALVO el par que traiga su
     CITA COMPLETA en el registro de enlaces mutuos tras resolver, y la cita
     se verifica entera: un par sin cita es rojo (adjudicaciones A.1 y A.4)
  7. cero guiones largos o medios en los textos de los nodos
  8. aristas solo hacia ids existentes o alias resolubles, y ningun nodo
     VIVO nombra a un DEPRECADO: el archivo no es superficie (D.17)
  9. en un nodo con mas de una fuente, el orden respeta la fecha: la fuente
     añadida va en SEGUNDO lugar (manual principio 8, automatizado por la
     adjudicacion A.2)

Salida: verde, o la lista exacta de fallos. Toda guarda de aqui tiene su
caso positivo en tests/test_aceptacion.py: una prueba que no puede fallar
no guarda nada.
"""

from . import comun
from . import config as modulo_config
from . import esquema as modulo_esquema
from . import guiones
from . import reglas_id
from .resolutor import Resolutor


class Fallo(object):

    def __init__(self, guarda, nodo, detalle):
        self.guarda = guarda
        self.nodo = nodo
        self.detalle = detalle

    def __str__(self):
        return "[%s] %s: %s" % (self.guarda, self.nodo or "dataset", self.detalle)


def _claves_de_fuente(tabla):
    return set(k for k in tabla.keys() if not k.startswith("_"))


CAMPOS_DE_CITA = ("fecha", "declarado_por", "paso_ida", "razon_ida",
                  "paso_vuelta", "razon_vuelta")


def _citas_mutuas(pares_mutuos, resolutor):
    """Indexa el REGISTRO DE CITAS por par resuelto (D.14).

    Manual principio 3: todo id pasa por el resolutor, tambien los de un
    registro. Un par cuyos dos extremos ya no resuelven no cubre nada: el
    enlace mutuo se perdio con el nodo.

    CONVENIO DEL REGISTRO, y lo escribe la aduana por construccion:
    `paso_ida` es un paso de `par[0]` (quien declaro) y `paso_vuelta` es un
    paso de `par[1]`.
    """
    citas = {}
    for entrada in pares_mutuos or []:
        par = (entrada or {}).get("par") or []
        if len(par) != 2:
            continue
        a = resolutor.resolver(par[0])
        b = resolutor.resolver(par[1])
        if a and b and a != b:
            citas[frozenset((a, b))] = {"entrada": entrada, "ida": a, "vuelta": b}
    return citas


def _fallos_de_cita(cita, resolutor):
    """Comprueba que la cita esta COMPLETA y que sigue siendo cierta hoy.

    Regla madre: la parada de My-idea del 2 sep 2026, LA LISTA BLANCA ES UN
    REGISTRO DE CITAS. Encender la guarda contra una lista de pertenencia
    obligaba a escribir 151 entradas sin una sola lectura detras, que es
    justo lo que la lista blanca vino a impedir. La salida fue exigir la
    cita: UN PAR SIN CITA ES ROJO.
    """
    entrada = cita["entrada"]
    problemas = []
    ausentes = set()

    for campo in CAMPOS_DE_CITA:
        valor = entrada.get(campo)
        if valor is None or (isinstance(valor, str) and not valor.strip()):
            problemas.append("le falta el campo '%s'" % campo)
            ausentes.add(campo)

    textos = {}
    for campo, extremo in (("paso_ida", "ida"), ("paso_vuelta", "vuelta")):
        if campo in ausentes:
            continue
        indice = entrada.get(campo)
        nodo = resolutor.canonicos.get(cita[extremo]) or {}
        pasos = nodo.get("pasos_accionables") or []
        if not isinstance(indice, int) or isinstance(indice, bool):
            problemas.append("su '%s' no es un numero de paso: %r" % (campo, indice))
        elif 1 <= indice <= len(pasos):
            textos[extremo] = pasos[indice - 1]
        else:
            problemas.append("cita el paso %d de '%s', que hoy tiene %d paso(s)"
                             % (indice, cita[extremo], len(pasos)))

    texto_ida = textos.get("ida")
    texto_vuelta = textos.get("vuelta")
    if texto_ida is not None and texto_vuelta is not None:
        if comun.normalizar_texto(texto_ida) == comun.normalizar_texto(texto_vuelta):
            problemas.append(
                "sus dos sentidos apuntan HOY a la misma linea (%r): eso es un solape, "
                "no un enlace mutuo (banco de textos 9.22)" % texto_ida)
    return problemas


def verificar(nodos=None, tabla_fuentes=None, esquema_nodo=None, pares_mutuos=None):
    """Devuelve la lista de Fallo. Lista vacia es verde."""
    if nodos is None:
        nodos = comun.leer_jsonl(comun.RUTA_DATASET)
    if tabla_fuentes is None:
        tabla_fuentes = comun.leer_json(comun.RUTA_FUENTES)
    if esquema_nodo is None:
        esquema_nodo = modulo_esquema.cargar()
    if pares_mutuos is None:
        pares_mutuos = modulo_config.cargar_pares_mutuos()

    fallos = []
    resolutor = Resolutor(nodos)
    claves_fuente = _claves_de_fuente(tabla_fuentes)

    for error in resolutor.errores:
        fallos.append(Fallo("resolutor", None, error))

    familias = {}

    for nodo in nodos:
        identificador = nodo.get("id") or "(sin id)"

        # 1. esquema
        for detalle in modulo_esquema.validar(nodo, esquema_nodo):
            fallos.append(Fallo("esquema", identificador, detalle))

        # 2. reglas de id
        for detalle in reglas_id.validar(nodo.get("id"), "id"):
            fallos.append(Fallo("reglas_id", identificador, detalle))
        for alias in nodo.get("ids_alias") or []:
            for detalle in reglas_id.validar(alias, "ids_alias '%s'" % alias, es_alias=True):
                fallos.append(Fallo("reglas_id", identificador, detalle))
        if isinstance(nodo.get("id"), str):
            clave_familia = reglas_id.familia(nodo["id"])
            if clave_familia:
                if clave_familia in familias and familias[clave_familia] != nodo["id"]:
                    fallos.append(Fallo(
                        "reglas_id", identificador,
                        "misma familia de id que '%s': dos cosas que merecen ids parecidos "
                        "merecen revision antes de existir (manual seccion 2)"
                        % familias[clave_familia]))
                familias[clave_familia] = nodo["id"]

        # 3. fuentes contra la tabla canonica, sin claves repetidas, y
        # 9. su orden respeta la fecha (la añadida va en SEGUNDO lugar)
        entradas_fuente = nodo.get("fuentes") or []
        claves_de_este_nodo = set()
        piezas_ordenadas = []
        for indice, entrada in enumerate(entradas_fuente):
            clave = entrada.get("clave") if isinstance(entrada, dict) else entrada
            fecha_entrada = entrada.get("fecha") if isinstance(entrada, dict) else None
            if clave not in claves_fuente:
                fallos.append(Fallo(
                    "fuentes", identificador,
                    "fuentes[%d] '%s' fuera de fuentes/FUENTES_CANONICAS.json"
                    % (indice, clave)))
            if clave in claves_de_este_nodo:
                fallos.append(Fallo(
                    "fuentes", identificador,
                    "fuente '%s' repetida en la lista de fuentes del nodo" % clave))
            else:
                claves_de_este_nodo.add(clave)
            piezas_ordenadas.append((indice, clave, fecha_entrada))
        for anterior, siguiente in zip(piezas_ordenadas, piezas_ordenadas[1:]):
            (indice_a, clave_a, fecha_a), (indice_b, clave_b, fecha_b) = anterior, siguiente
            if not fecha_a or not fecha_b or fecha_a > fecha_b:
                fallos.append(Fallo(
                    "orden_fuentes", identificador,
                    "fuentes[%d] '%s' (fecha %s) va antes que fuentes[%d] '%s' (fecha %s), "
                    "pero su fecha no es anterior o igual: la fuente añadida va en SEGUNDO "
                    "lugar (manual principio 8, adjudicacion A.2)"
                    % (indice_a, clave_a, fecha_a or "(sin fecha)",
                       indice_b, clave_b, fecha_b or "(sin fecha)")))
        for atribucion in nodo.get("atribuciones") or []:
            fuente = (atribucion or {}).get("fuente")
            if fuente and fuente not in claves_fuente:
                fallos.append(Fallo(
                    "fuentes", identificador,
                    "atribucion con fuente '%s' fuera de la tabla canonica" % fuente))

        # 7. guiones en los textos del nodo
        for campo, texto in comun.textos_de_nodo(nodo):
            for hallazgo in comun.buscar_guiones(texto):
                fallos.append(Fallo(
                    "guiones", identificador,
                    "%s contiene %s (%s)" % (campo, hallazgo[3], repr(hallazgo[2]))))

    # Aristas: todo se compara TRAS RESOLVER (manual principio 3)
    #
    # EL DEPRECADO ES ARCHIVO, NO SUPERFICIE (D.17): las aristas que NACEN en
    # un nodo deprecado conservan su ficha para que la fusion sea auditable,
    # pero NO entran al grafo. No se reciprocan, no forman vuelta y no se
    # cuentan como duplicadas. En My-idea, reciprocar aristas nacidas en
    # deprecados fue lo que refabricaba las 33 auto-aristas cada vez que se
    # limpiaban: la sombra vuelve mientras viva lo que la proyecta.
    aristas_dirigidas = set()
    for nodo in nodos:
        identificador = nodo.get("id")
        es_archivo = identificador in resolutor.deprecados
        propio = identificador if es_archivo else resolutor.resolver(identificador)
        if propio is None:
            continue
        for campo, sentido in (("nodos_siguientes", "hacia"), ("nodos_previos", "desde")):
            vistas = []
            for destino in nodo.get(campo) or []:
                resuelto = resolutor.resolver(destino)

                # 10. ningun VIVO nombra a un DEPRECADO: el archivo no es
                # superficie, y una arista viva hacia el absorbido tenia que
                # haberse redirigido al superviviente al fundir.
                if (not es_archivo and resuelto is not None
                        and destino in resolutor.deprecados):
                    fallos.append(Fallo(
                        "deprecado_en_superficie", identificador,
                        "%s nombra a '%s', que esta DEPRECADO. El deprecado es archivo, "
                        "no participante: la arista tenia que apuntar a su superviviente "
                        "'%s' (D.17)" % (campo, destino, resuelto)))
                    continue

                # 8. arista hacia id inexistente
                if resuelto is None:
                    fallos.append(Fallo(
                        "arista_rota", identificador,
                        "%s apunta a '%s', que no existe ni resuelve por alias "
                        "(cadena probada: %s)"
                        % (campo, destino, " > ".join(resolutor.cadena(destino)))))
                    continue

                # 4. auto-arista TRAS RESOLVER
                if resuelto == propio:
                    detalle = "%s contiene '%s'" % (campo, destino)
                    if destino != identificador:
                        detalle += (" que resuelve por alias al propio nodo (%s). "
                                    "Una comparacion literal no lo veria" % propio)
                    else:
                        detalle += " apuntando a si mismo"
                    fallos.append(Fallo("auto_arista", identificador, detalle))
                    continue

                # 5. arista duplicada TRAS RESOLVER
                if resuelto in vistas:
                    fallos.append(Fallo(
                        "arista_duplicada", identificador,
                        "%s repite el destino %s tras resolver (entradas '%s')"
                        % (campo, resuelto, destino)))
                    continue
                vistas.append(resuelto)

                # Las aristas del archivo no entran al grafo: se conservan
                # como registro y no se reciprocan (D.17).
                if es_archivo:
                    continue
                if sentido == "hacia":
                    aristas_dirigidas.add((propio, resuelto))
                else:
                    aristas_dirigidas.add((resuelto, propio))

    # 6. cero vueltas en los pares madre-hijo declarados, salvo el enlace
    # mutuo declarado (adjudicacion A.1): la UNICA vuelta legitima es la que
    # cubre la lista blanca, y solo tras resolver sus dos extremos.
    citas = _citas_mutuas(pares_mutuos, resolutor)
    for madre, hijo in sorted(aristas_dirigidas):
        if (hijo, madre) in aristas_dirigidas:
            if madre < hijo:
                cita = citas.get(frozenset((madre, hijo)))
                if cita is None:
                    fallos.append(Fallo(
                        "vuelta", madre,
                        "el par bidireccional con %s NO TIENE CITA en el registro de "
                        "enlaces mutuos (config/pares_mutuos.jsonl). La secuencia es "
                        "dirigida: la vuelta no es redundante, es falsa, salvo un MUTUO "
                        "declarado que cite sus dos lineas. UN PAR SIN CITA ES ROJO "
                        "(manual seccion 2, adjudicaciones A.1 y A.4)" % hijo))
                    continue
                for problema in _fallos_de_cita(cita, resolutor):
                    fallos.append(Fallo(
                        "cita_incompleta", madre,
                        "la cita del enlace mutuo con %s no se sostiene: %s" % (hijo, problema)))

    # Coherencia del par: la arista se escribe en los dos extremos, sin huecos
    for madre, hijo in sorted(aristas_dirigidas):
        nodo_madre = resolutor.canonicos.get(madre)
        nodo_hijo = resolutor.canonicos.get(hijo)
        if nodo_madre is not None:
            siguientes = resolutor.resolver_lista(nodo_madre.get("nodos_siguientes"))
            if hijo not in siguientes:
                fallos.append(Fallo(
                    "arista_incompleta", madre,
                    "%s declara a %s como previo, pero %s no lo declara en "
                    "nodos_siguientes" % (hijo, madre, madre)))
        if nodo_hijo is not None:
            previos = resolutor.resolver_lista(nodo_hijo.get("nodos_previos"))
            if madre not in previos:
                fallos.append(Fallo(
                    "arista_incompleta", hijo,
                    "%s declara a %s como siguiente, pero %s no lo declara en "
                    "nodos_previos" % (madre, hijo, hijo)))

    return fallos


def texto_informe(fallos, cuantos_nodos):
    if not fallos:
        return ("GATE VERDE.\n"
                "  nodos verificados: %d\n"
                "  guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, "
                "arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, "
                "arista_rota, arista_incompleta, guiones"
                % cuantos_nodos)
    lineas = ["GATE EN ROJO: %d fallo(s) sobre %d nodo(s)." % (len(fallos), cuantos_nodos)]
    for fallo in fallos:
        lineas.append("  " + str(fallo))
    return "\n".join(lineas)


def main(argumentos=None):
    comun.salida_utf8()
    nodos = comun.leer_jsonl(comun.RUTA_DATASET)
    fallos = verificar(nodos)
    hallazgos = guiones.barrer_repo(rutas=[comun.RUTA_DATASET])
    for hallazgo in hallazgos:
        fallos.append(Fallo("guiones", "dataset/nodos.jsonl", hallazgo))
    print(texto_informe(fallos, len(nodos)))
    return 1 if fallos else 0
