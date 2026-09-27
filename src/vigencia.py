# -*- coding: utf-8 -*-
"""EL BLOQUE DE VIGENCIA: los veredictos RANCIOS (D.15).

    python forja.py rancios

REGLA MADRE, y tiene fecha y muertos: los cinco pares rancios de `OP-D-03`
en My-idea (parada del 15 ago 2026, decision del fundador del mismo dia).
Medido alli: **de los seis pares A de un acto, CINCO se leyeron contra texto
que ya no existe**, porque las cirugias de una fase anterior habian reescrito
los nodos. Fundir el acto con cinco de sus seis lecturas emitidas contra texto
muerto es exactamente lo que la regla del acto leido entero existe para
impedir.

Y la precision que se pago con una vuelta entera: **LA VARA QUE MANDA ES LA DE
TEXTO, NO LA DE FECHA.** La vuelta anterior habia mirado solo las fechas y
conto DOS; contando por texto eran CINCO. Los tres que faltaban no
envejecieron por el destejido que se estaba mirando, sino por otros dos de una
fase anterior.

QUE HACE ESTE INSTRUMENTO. Recomputa la huella del texto de hoy y la compara
con la que el veredicto guardo el dia que se emitio. No juzga: CITA. Un
veredicto rancio no es un veredicto malo, es un veredicto que **no se puede
citar como vigente** hasta que alguien lo relea o lo declare.

LO QUE NO HACE, y va dicho: no toca el gate. Un rancio no pone el dataset en
rojo, porque la salida no es mecanica: se relee o se declara, y las dos cosas
las hace una persona. El gate vigila lo que es cierto o falso hoy; esto vigila
lo que fue cierto ayer y nadie ha vuelto a mirar.
"""

from . import comun
from . import config as modulo_config
from .resolutor import Resolutor

VIGENTE = "VIGENTE"
RANCIO = "RANCIO"
SIN_HUELLA = "SIN HUELLA"
NODO_IDO = "NODO IDO"

# LA HUELLA DE UN NODO VACIO. Se calcula, no se teclea, para que siga siendo la
# misma el dia que `huella_de_nodo` cambie de algoritmo.
HUELLA_DE_NADA = comun.huella_de_nodo({})


class Hallazgo(object):

    def __init__(self, clase, sede, sujeto, detalle):
        self.clase = clase
        self.sede = sede
        self.sujeto = sujeto
        self.detalle = detalle

    def __str__(self):
        return "[%s] %s %s: %s" % (self.clase, self.sede, self.sujeto, self.detalle)


def _revisar_lado(resolutor, identificador, huella_guardada, sede, sujeto, lado):
    """Compara la huella guardada con la del texto de hoy. Devuelve Hallazgo o None."""
    resuelto = resolutor.resolver(identificador)
    if resuelto is None:
        return Hallazgo(NODO_IDO, sede, sujeto,
                        "su %s '%s' ya no existe ni resuelve por alias: la lectura "
                        "se emitio sobre un nodo que se fue" % (lado, identificador))
    # LA HUELLA DE NADA NO ES UNA HUELLA, y decir que lo es era darla por buena.
    # La aduana guardaba `huella_de_nodo({})` cuando el vecino esperaba en la
    # bandeja (`D.38.5` a medio cablear). `D.15` ya tiene la casilla para esto y
    # se llama SIN HUELLA: *incomprobable, y eso se declara en vez de darse por
    # bueno.* Lo que NO se hace es llamarlo VIGENTE.
    if huella_guardada == HUELLA_DE_NADA:
        return Hallazgo(SIN_HUELLA, sede, sujeto,
                        "la huella que guarda de su %s '%s' es la de un nodo VACIO, "
                        "asi que NO SE PUEDE COMPROBAR contra que texto se emitio"
                        % (lado, resuelto))
    if not huella_guardada:
        return Hallazgo(SIN_HUELLA, sede, sujeto,
                        "no guarda la huella de su %s '%s', asi que NO SE PUEDE "
                        "COMPROBAR si sigue emitida contra el texto que leyo"
                        % (lado, resuelto))
    ahora = comun.huella_de_nodo(resolutor.canonicos[resuelto])
    if ahora != huella_guardada:
        return Hallazgo(RANCIO, sede, sujeto,
                        "el texto de su %s '%s' cambio desde que se emitio "
                        "(huella %s, hoy %s)" % (lado, resuelto, huella_guardada, ahora))
    return None


def poblacion(nodos=None):
    """GRAFO MAS BANDEJAS, que es la poblacion de esta casa (D.38.4, D.38.5).

    LA VIGENCIA ERA EL ULTIMO SITIO QUE MEDIA SOLO EL GRAFO, y por eso contaba
    como `NODO IDO` a un vecino que **no se fue: todavia no ha llegado.** Su
    texto vive en `cuarentena/` y su huella se comprueba ahi. Ocho hallazgos asi
    en la vuelta 27, lineas `252` a `264` (`ACTA 27` `5.3.b`).

    Descarta `_insertados` y `_derivadas`, como manda `D.38.4`: lo archivado ya
    vive en el grafo y contarlo dos veces seria medir un nodo contra si mismo.
    """
    if nodos is None:
        nodos = comun.leer_jsonl(comun.RUTA_DATASET)
    # La importacion va aqui y no arriba: `aduana` importa mucho mas que este
    # modulo, y `rancios` corre en cada cierre.
    from .aduana import poblacion_de_bandejas
    return list(nodos) + list(poblacion_de_bandejas())


def revisar(nodos=None, veredictos=None, citas=None):
    """Devuelve la lista de Hallazgo. Lista vacia es verde."""
    if nodos is None:
        nodos = poblacion()
    if veredictos is None:
        veredictos = comun.leer_jsonl(comun.RUTA_VEREDICTOS)
    if citas is None:
        citas = modulo_config.cargar_pares_mutuos()

    resolutor = Resolutor(nodos)
    hallazgos = []

    for numero, veredicto in enumerate(veredictos, 1):
        # UNA LINEA DECLARADA NO CONSUMADA NO SE MIDE (ACTA 27 5.2 y 5.3.b). No
        # es una lectura que envejecio: es una lectura que NUNCA OCURRIO, escrita
        # por una corrida que imprimio RECHAZADO y no inserto nada. Pedirle la
        # huella de un nodo que no entro es preguntarle a un acto que no hubo.
        # La marca no se pone a mano: la pone `forja.py anotar --no-consumada`,
        # con su razon escrita dentro de la propia linea.
        if veredicto.get("consumada") is False:
            continue
        sujeto = "%s contra %s (linea %d, %s)" % (
            veredicto.get("candidato"), veredicto.get("vecino"), numero,
            veredicto.get("fecha", "sin fecha"))
        for lado, campo_id, campo_huella in (
                ("candidato", "candidato", "huella_candidato"),
                ("vecino", "vecino", "huella_vecino")):
            hallazgo = _revisar_lado(
                resolutor, veredicto.get(campo_id), veredicto.get(campo_huella),
                "veredicto", sujeto, lado)
            if hallazgo is not None:
                hallazgos.append(hallazgo)

    for numero, cita in enumerate(citas, 1):
        par = cita.get("par") or []
        sujeto = "%s (linea %d, %s)" % (" <> ".join(str(p) for p in par), numero,
                                        cita.get("fecha", "sin fecha"))
        if len(par) != 2:
            hallazgos.append(Hallazgo(SIN_HUELLA, "cita", sujeto,
                                      "su campo 'par' no nombra dos nodos"))
            continue
        for extremo, campo_paso, campo_huella, lado in (
                (0, "paso_ida", "huella_ida", "linea de ida"),
                (1, "paso_vuelta", "huella_vuelta", "linea de vuelta")):
            resuelto = resolutor.resolver(par[extremo])
            if resuelto is None:
                hallazgos.append(Hallazgo(
                    NODO_IDO, "cita", sujeto,
                    "su nodo '%s' ya no existe ni resuelve por alias" % par[extremo]))
                continue
            guardada = cita.get(campo_huella)
            if not guardada:
                hallazgos.append(Hallazgo(
                    SIN_HUELLA, "cita", sujeto,
                    "no guarda la huella de su %s, asi que no se puede comprobar" % lado))
                continue
            pasos = resolutor.canonicos[resuelto].get("pasos_accionables") or []
            indice = cita.get(campo_paso)
            if not isinstance(indice, int) or not 1 <= indice <= len(pasos):
                hallazgos.append(Hallazgo(
                    RANCIO, "cita", sujeto,
                    "su %s citaba el paso %r de '%s', que hoy tiene %d paso(s)"
                    % (lado, indice, resuelto, len(pasos))))
                continue
            ahora = comun.huella_de_texto(pasos[indice - 1])
            if ahora != guardada:
                hallazgos.append(Hallazgo(
                    RANCIO, "cita", sujeto,
                    "su %s (paso %d de '%s') cambio de texto desde que se cito "
                    "(huella %s, hoy %s)" % (lado, indice, resuelto, guardada, ahora)))
    return hallazgos


def contar_no_consumadas(veredictos):
    """Las lineas declaradas NO CONSUMADAS, que se cuentan aunque no se midan.

    Se publican SIEMPRE, verde o rojo. Una linea que sale de la medida sin dejar
    su cuenta es una guarda que se afloja a escondidas.
    """
    return sum(1 for v in veredictos if v.get("consumada") is False)


def texto_informe(hallazgos, cuantos_veredictos, cuantas_citas, no_consumadas=0):
    cola = ""
    if no_consumadas:
        cola = ("\n  lineas declaradas NO CONSUMADAS y por eso no medidas: %d\n"
                "    (las escribio una corrida que no inserto nada; ver su razon "
                "en la propia linea)" % no_consumadas)
    if not hallazgos:
        return ("BLOQUE DE VIGENCIA VERDE.\n"
                "  veredictos comprobados: %d\n"
                "  citas de enlace mutuo comprobadas: %d\n"
                "  todos siguen emitidos contra el texto que leyeron%s"
                % (cuantos_veredictos - no_consumadas, cuantas_citas, cola))
    por_clase = {}
    for hallazgo in hallazgos:
        por_clase[hallazgo.clase] = por_clase.get(hallazgo.clase, 0) + 1
    lineas = ["BLOQUE DE VIGENCIA: %d hallazgo(s) sobre %d veredicto(s) y %d cita(s)."
              % (len(hallazgos), cuantos_veredictos - no_consumadas, cuantas_citas),
              "  " + ", ".join("%s %d" % (c, n) for c, n in sorted(por_clase.items()))]
    if cola:
        lineas.append(cola.strip("\n"))
    for hallazgo in hallazgos:
        lineas.append("  " + str(hallazgo))
    lineas.append("")
    lineas.append("Un rancio NO SE CITA COMO VIGENTE: se relee con el texto de hoy, o se")
    lineas.append("declara por que sigue valiendo. Las dos cosas las hace una persona, y")
    lineas.append("por eso esto no pone el gate en rojo (D.15).")
    return "\n".join(lineas)


def main(argumentos=None):
    comun.salida_utf8()
    nodos = poblacion()
    veredictos = comun.leer_jsonl(comun.RUTA_VEREDICTOS)
    citas = modulo_config.cargar_pares_mutuos()
    hallazgos = revisar(nodos, veredictos, citas)
    print(texto_informe(hallazgos, len(veredictos), len(citas),
                        contar_no_consumadas(veredictos)))
    return 1 if hallazgos else 0
