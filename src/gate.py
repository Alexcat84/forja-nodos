# -*- coding: utf-8 -*-
"""EL GATE DE INTEGRIDAD (manual seccion 2).

Se corre en cada commit. Comprueba, sobre el dataset entero:
  1. esquema completo y sin huecos
  2. reglas de id (docs/REGLAS_DE_ID.md)
  3. fuentes contra la tabla canonica
  4. cero auto-aristas TRAS RESOLVER
  5. cero aristas duplicadas TRAS RESOLVER
  6. cero vueltas en los pares madre-hijo declarados
  7. cero guiones largos o medios en los textos de los nodos
  8. aristas solo hacia ids existentes o alias resolubles

Salida: verde, o la lista exacta de fallos. Toda guarda de aqui tiene su
caso positivo en tests/test_aceptacion.py: una prueba que no puede fallar
no guarda nada.
"""

from . import comun
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


def verificar(nodos=None, tabla_fuentes=None, esquema_nodo=None):
    """Devuelve la lista de Fallo. Lista vacia es verde."""
    if nodos is None:
        nodos = comun.leer_jsonl(comun.RUTA_DATASET)
    if tabla_fuentes is None:
        tabla_fuentes = comun.leer_json(comun.RUTA_FUENTES)
    if esquema_nodo is None:
        esquema_nodo = modulo_esquema.cargar()

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

        # 3. fuentes contra la tabla canonica
        for fuente in nodo.get("fuentes") or []:
            if fuente not in claves_fuente:
                fallos.append(Fallo(
                    "fuentes", identificador,
                    "fuente '%s' fuera de fuentes/FUENTES_CANONICAS.json" % fuente))
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
    aristas_dirigidas = set()
    for nodo in nodos:
        identificador = nodo.get("id")
        propio = resolutor.resolver(identificador)
        if propio is None:
            continue
        for campo, sentido in (("nodos_siguientes", "hacia"), ("nodos_previos", "desde")):
            vistas = []
            for destino in nodo.get(campo) or []:
                resuelto = resolutor.resolver(destino)

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

                if sentido == "hacia":
                    aristas_dirigidas.add((propio, resuelto))
                else:
                    aristas_dirigidas.add((resuelto, propio))

    # 6. cero vueltas en los pares madre-hijo declarados
    for madre, hijo in sorted(aristas_dirigidas):
        if (hijo, madre) in aristas_dirigidas:
            if madre < hijo:
                fallos.append(Fallo(
                    "vuelta", madre,
                    "el par madre-hijo con %s esta declarado en los dos sentidos. "
                    "La secuencia es dirigida: la vuelta no es redundante, es falsa "
                    "(manual seccion 2)" % hijo))

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
                "  guardas: esquema, reglas_id, fuentes, auto_arista, arista_duplicada, "
                "vuelta, arista_rota, arista_incompleta, guiones" % cuantos_nodos)
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
