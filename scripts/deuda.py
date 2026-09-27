# -*- coding: utf-8 -*-
"""LA DEUDA NO BLOQUEA LA PRODUCCION (D.55, 18 sep 2026).

    python scripts/deuda.py                      lo pendiente, y que toca la vuelta que viene
    python scripts/deuda.py --anotar --que "..." --cita "..." --vuelta 41 [--especie ...]
    python scripts/deuda.py --pagar <id> --vuelta 43 --como "..."
    python scripts/deuda.py --saneamiento --vuelta 46      declara una vuelta de saneamiento
    python scripts/deuda.py --clase                        INSERCION o SANEAMIENTO

POR QUE EXISTE, Y ESTA MEDIDO. La linea serial metio **`14` nodos en la vuelta 36**, en una
sola vuelta. En las **cinco siguientes metio `8` en total**, y una de ellas metio **cero**.
El grafo no se freno por falta de candidatos ni por una guarda: se freno porque **cada
vuelta abria con una tarea bloqueante de reparacion** y lo que quedaba de turno ya no daba
para insertar:

    V.38  TAREA 1.A: la arista en cola de la linea 469 cableada
    V.39  TAREAS 1 y 2, todas ANTES de la primera insercion
    V.40  TAREA 1.A CERRADA: los dos U+0008 corregidos        (0 nodos)
    V.41  TAREA 1.A CERRADA: la 498 releida contra el grafo   (0 nodos)

**LA DEUDA HAY QUE PAGARLA, Y ALGUNA ES DE HACE DIECISEIS VUELTAS.** Lo que `D.55` cambia
no es si se paga: es **cuando**. Se paga junta, en una vuelta que no inserta, **una de cada
cinco**.

LAS DOS CLASES DE VUELTA:

  VUELTA DE INSERCION   abre SIN tareas de reparacion. Su unico trabajo es meter
                        candidatos por la aduana, con las guardas de DATO intactas:
                        fidelidad `D.30`, cerrojo, censo, tallado.

  VUELTA DE SANEAMIENTO corre UNA de cada CINCO y **no inserta nada**. Paga lo que este
                        en este registro.

LA UNICA EXCEPCION, Y ES ESTRECHA: **una guarda de DATO en rojo** (`gate`, cerrojo, censo
no decreciente, fidelidad con puente) **bloquea en el acto**, porque **eso no es deuda: es
averia**. Una averia se arregla antes de seguir; una deuda se agenda.
"""

import json
import os
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)

from src import comun  # noqa: E402
from src import credito  # noqa: E402

RUTA = os.path.join(RAIZ, "docs", "loop", "DEUDA.jsonl")
CADENCIA = 5          # una vuelta de saneamiento de cada cinco

TIPOS = ("deuda", "pago", "saneamiento")

# Las guardas cuyo rojo NO es deuda: es averia, y bloquea en el acto.
GUARDAS_DE_DATO = ("gate", "cerrojo", "censo_no_decrece", "fidelidad")


class DeudaMalEscrita(Exception):
    """Una linea del registro que no se puede leer. Nunca se salta en silencio."""


def leer(ruta=None):
    destino = ruta or RUTA
    if not os.path.exists(destino):
        return []
    sucesos = []
    for numero, cruda in enumerate(
            comun.leer_texto(destino).splitlines(), 1):
        if not cruda.strip():
            continue
        try:
            suceso = json.loads(cruda)
        except ValueError as roto:
            raise DeudaMalEscrita("%s linea %d: %s"
                                  % (comun.relativa(destino), numero, roto))
        if suceso.get("tipo") not in TIPOS:
            raise DeudaMalEscrita(
                "%s linea %d: tipo %r, y los tipos son %s"
                % (comun.relativa(destino), numero, suceso.get("tipo"),
                   ", ".join(TIPOS)))
        suceso["_linea"] = numero
        sucesos.append(suceso)
    return sucesos


def pendientes(sucesos=None):
    """Lo que falta por pagar, en el orden en que se contrajo."""
    sucesos = leer() if sucesos is None else sucesos
    pagadas = set(s.get("id") for s in sucesos if s.get("tipo") == "pago")
    return [s for s in sucesos
            if s.get("tipo") == "deuda" and s.get("id") not in pagadas]


def _numero(valor):
    """`vuelta` llega como entero del arnes y como cadena de la linea de ordenes."""
    try:
        return int(str(valor).strip())
    except (TypeError, ValueError):
        return None


def ultima_saneamiento(sucesos=None, linea=None):
    """La vuelta de la ultima de saneamiento **DE ESA LINEA**, o `None`.

    **EL REGISTRO ES UNO Y LAS LINEAS SON VARIAS** (`d097`). Hasta el 22 sep esta
    funcion devolvia la ultima de CUALQUIER linea, y como el fichero viaja a los
    frentes en la fusion, un frente que numera sus vueltas `1, 2, 3` recibia la
    `59` de la serial. **Un suceso sin `linea` es de la serial**, que es la unica
    que declaro saneamientos antes de que este campo existiera: las cuatro que hay
    (`44`, `49`, `54`, `59`) son suyas.
    """
    sucesos = leer() if sucesos is None else sucesos
    linea = linea or credito.linea_actual()
    vueltas = [_numero(s.get("vuelta")) for s in sucesos
               if s.get("tipo") == "saneamiento"
               and (s.get("linea") or credito.LINEA_SERIAL) == linea]
    vueltas = [v for v in vueltas if v is not None]
    return max(vueltas) if vueltas else None


def primera_vuelta(linea=None):
    """Desde donde cuenta una linea que todavia no ha saneado nunca (`d097`).

    **UN FRENTE NACE CON SU CONTADOR EN CERO** (decision del fundador del 22 sep
    2026, punto 3). La sede que sabe de lineas es el registro de credito (`D.48`),
    asi que la primera vuelta de la linea sale de ahi; **si la linea no ha escrito
    ninguna tanda todavia, empieza en `1`**, que es por donde empieza a numerar el
    arnes.
    """
    linea = linea or credito.linea_actual()
    try:
        sucesos = credito.leer(linea)
    except Exception:
        return 1
    vueltas = [_numero(s.get("vuelta")) for s in sucesos]
    vueltas = [v for v in vueltas if v is not None]
    return min(vueltas) if vueltas else 1


def clase_de_vuelta(vuelta, sucesos=None, linea=None):
    """`(clase, motivo)`: `SANEAMIENTO`, o `LIBRE` si la cadencia no la reclama.

    **`LIBRE` NO ES UNA CLASE DE VUELTA: ES LA AUSENCIA DE OBLIGACION.** Desde `D.58`
    hay tres clases (`EXTRACCION`, `INSERCION`, `SANEAMIENTO`) y **esta funcion solo
    sabe de una**: la que la cadencia impone. Las otras dos las elige el encargo segun
    el libro, y decirlas aqui seria publicar un rotulo que este instrumento no mide.
    Hasta el 19 sep devolvia `INSERCION`, que era falso en toda vuelta de extraccion.

    **Se cuenta desde la ultima de saneamiento**, no por el resto de la division: si la
    cadencia se cuenta contra un calendario fijo, **una vuelta perdida corre el turno de
    todas las demas** y el registro deja de poder explicar por que le toco a esa.
    """
    sucesos = leer() if sucesos is None else sucesos
    linea = linea or credito.linea_actual()
    vuelta = _numero(vuelta)
    ultima = ultima_saneamiento(sucesos, linea)
    faltan = len(pendientes(sucesos))
    if not faltan:
        return "LIBRE", ("no hay deuda pendiente: no hay nada que sanear")

    # LA CUENTA ES DE LA LINEA, Y CUANDO NO HA SANEADO NUNCA CUENTA DESDE SU PRIMERA
    # VUELTA (d097, decision del fundador del 22 sep 2026 punto 3). Antes devolvia
    # LIBRE aqui sin mirar nada, y eso dejaba a un frente SIN PODER RECIBIR NUNCA una
    # vuelta de saneamiento: la unica de la casa era la 59 de la serial, y 3 menos 59
    # da -56, que no alcanza la cadencia jamas. El LIBRE salia bueno por casualidad.
    if ultima is None:
        origen = primera_vuelta(linea)
        desde = vuelta - origen
        cuenta = ("la primera vuelta de la linea '%s' (la %d), que todavia no ha "
                  "saneado nunca" % (linea, origen))
    else:
        desde = vuelta - ultima
        cuenta = "la ultima de saneamiento (la %d)" % ultima

    if desde >= CADENCIA:
        return "SANEAMIENTO", ("han pasado %d vuelta(s) desde %s y la cadencia es %d, "
                               "con %d deuda(s) pendientes"
                               % (desde, cuenta, CADENCIA, faltan))
    return "LIBRE", ("van %d de %d desde %s, con %d deuda(s) esperando"
                     % (desde, CADENCIA, cuenta, faltan))


def anotar(suceso, ruta=None):
    suceso = dict((k, v) for k, v in suceso.items() if not k.startswith("_"))
    if suceso.get("tipo") not in TIPOS:
        raise DeudaMalEscrita("tipo %r, y los tipos son %s"
                              % (suceso.get("tipo"), ", ".join(TIPOS)))
    # CADA SUCESO DICE DE QUE LINEA ES (d097). Sin esto el registro no se puede
    # repartir, y el fichero viaja a los frentes en cada fusion.
    suceso.setdefault("linea", credito.linea_actual())
    if suceso["tipo"] == "deuda":
        for campo in ("que", "cita", "vuelta"):
            if not str(suceso.get(campo) or "").strip():
                raise DeudaMalEscrita(
                    "una deuda sin '%s'. Una deuda sin su cita y su vuelta de origen no "
                    "se puede releer, y la que no se puede releer no se paga." % campo)
        suceso.setdefault("id", "d%03d" % (len(leer(ruta)) + 1))
        suceso.setdefault("anotada", time.strftime("%Y-%m-%d %H:%M:%S"))
    comun.agregar_jsonl(ruta or RUTA, suceso)
    return suceso


def texto(vuelta=None):
    sucesos = leer()
    falta = pendientes(sucesos)
    partes = ["DEUDA DE LA LINEA (D.55): la deuda no bloquea la produccion",
              "  registro: %s" % comun.relativa(RUTA),
              "  pendientes: %d    pagadas: %d"
              % (len(falta), len([s for s in sucesos if s.get("tipo") == "pago"])),
              ""]
    if falta:
        partes.append("  %-6s %-7s %-18s %s" % ("id", "vuelta", "especie", "que"))
        partes.append("  " + "-" * 92)
        for deuda in falta:
            partes.append("  %-6s %-7s %-18s %s"
                          % (deuda.get("id", "?"), deuda.get("vuelta", "?"),
                             (deuda.get("especie") or "")[:18],
                             (deuda.get("que") or "")[:52]))
    else:
        partes.append("  SIN DEUDA PENDIENTE.")
    ultima = ultima_saneamiento(sucesos)
    partes.append("")
    partes.append("  ultima vuelta de saneamiento: %s"
                  % (ultima if ultima is not None else "ninguna todavia"))
    if vuelta is not None:
        clase, motivo = clase_de_vuelta(int(vuelta), sucesos)
        partes.append("  la vuelta %s es de %s" % (vuelta, clase))
        partes.append("    %s" % motivo)
    return "\n".join(partes)


def main(argumentos=None):
    comun.salida_utf8()
    argumentos = list(argumentos if argumentos is not None else sys.argv[1:])

    def valor(bandera):
        return (argumentos[argumentos.index(bandera) + 1]
                if bandera in argumentos else None)

    try:
        if "--anotar" in argumentos:
            suceso = anotar({"tipo": "deuda", "que": valor("--que"),
                             "cita": valor("--cita"), "vuelta": valor("--vuelta"),
                             "especie": valor("--especie") or "deuda"})
            print("ANOTADA %s: %s" % (suceso["id"], suceso["que"][:70]))
            return 0
        if "--pagar" in argumentos:
            identificador = valor("--pagar")
            if identificador not in [d.get("id") for d in pendientes()]:
                print("NO HAY DEUDA PENDIENTE CON ID %r." % identificador)
                return 1
            anotar({"tipo": "pago", "id": identificador, "vuelta": valor("--vuelta"),
                    "como": valor("--como") or ""})
            print("PAGADA %s en la vuelta %s" % (identificador, valor("--vuelta")))
            return 0
        if "--saneamiento" in argumentos:
            anotar({"tipo": "saneamiento", "vuelta": int(valor("--vuelta") or 0),
                    "cita": valor("--cita") or "D.55, cadencia de una de cada cinco"})
            print("DECLARADA vuelta de SANEAMIENTO: %s" % valor("--vuelta"))
            return 0
        if "--clase" in argumentos:
            vuelta = int(valor("--clase") or valor("--vuelta") or 0)
            clase, motivo = clase_de_vuelta(vuelta)
            print("%s" % clase)
            print("  %s" % motivo)
            return 0
        print(texto(valor("--vuelta")))
        return 0
    except DeudaMalEscrita as roto:
        print("DEUDA MAL ESCRITA: %s" % roto)
        return 1


if __name__ == "__main__":
    sys.exit(main())
