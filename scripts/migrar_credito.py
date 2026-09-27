# -*- coding: utf-8 -*-
"""MIGRA LA HISTORIA DE LAS RACHAS DE `ACTA_AUDITOR.md` AL REGISTRO POR LINEA (D.48).

    python scripts/migrar_credito.py --ver       imprime lo que sacaria, sin escribir
    python scripts/migrar_credito.py --escribir  escribe docs/loop/CREDITO_serial.jsonl

POR QUE SE MIGRA Y NO SE EMPIEZA DE CERO. La decision del fundador del 17 sep 2026 dice
*migra el estado actual a ese formato **sin perder historia***. Las `31` actas de esta
linea llevan su racha publicada en una tabla, vuelta a vuelta, y esa es la historia: si
el registro nuevo arrancara vacio, la linea serial quedaria indistinguible de un frente
recien nacido, **que es justo la confusion que `D.48` viene a cerrar.**

DE DONDE SACA CADA CIFRA. De la tabla de rachas de cada acta, que es la unica sede donde
esta casa publica ese numero. Se reconoce por su cabecera: lleva `especie` **y** una
columna de cierre (`queda en`, `al cerrarla`, `racha`). **La columna de cierre es la que
manda**, no la de apertura: lo que el acta adjudica es como sale la tanda.

LO QUE NO INVENTA. `cae` solo se escribe **cuando el acta publica las dos columnas** y se
puede restar; cuando el acta publica una sola cifra, la fila va **sin `cae`**, y el replay
de `credito.py` la declara como no replayable en vez de suponerla. Un migrador que rellena
huecos con su criterio no migra: dicta.
"""

import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)

from src import comun, credito  # noqa: E402

RUTA_ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")

MARCA_ACTA = re.compile(r"^#\s+ACTA\s+(\d+)")
VUELTA = re.compile(r"VUELTA\s+(\d+)", re.I)
SEPARADOR = re.compile(r"^\|[\s:|-]+\|$")
RACHA = re.compile(r"(\d+)\s*(?:de\s*(\d+))?")

# Lo que la primera celda dice, y la especie que es. El orden importa: `DATO MOVIDO`
# se busca antes que `CLASE` porque la ACTA 31 escribe las dos en la misma celda.
NOMBRES = (
    ("CIFRA PUBLICADA PROPIA", "AUDITOR"),
    ("REMEDIO ROTO", "AUDITOR"),
    ("LA MIA", "AUDITOR"),
    ("PROPIA DEL AUDITOR", "AUDITOR"),
    ("DEL AUDITOR", "AUDITOR"),
    ("CIFRA PUBLICADA", "CIFRA PUBLICADA"),
    ("REPORTE", "REPORTE"),
    ("DATO MOVIDO", "DATO MOVIDO"),
    ("CLASE", "CLASE"),
)

# Las cabeceras que nombran la columna de la cifra de CIERRE, y las de APERTURA.
CIERRE = ("queda en", "al cerrarla", "al cerrar", "racha viva", "racha")
APERTURA = ("venia en", "racha al abrir", "al abrir")


def _limpiar(celda):
    texto = re.sub(r"[`*#>]", " ", celda or "")
    return " ".join(texto.split())


def _celdas(linea):
    trozo = linea.strip()
    if trozo.startswith("|"):
        trozo = trozo[1:]
    if trozo.endswith("|"):
        trozo = trozo[:-1]
    return [c.strip() for c in trozo.split("|")]


def _especies_de(celda):
    """Las especies que nombra la primera celda de una fila. Puede nombrar DOS."""
    plano = _limpiar(celda).upper()
    encontradas = []
    for aguja, especie in NOMBRES:
        if aguja in plano and especie not in encontradas:
            encontradas.append(especie)
            plano = plano.replace(aguja, " ")
    return encontradas


def _columna(cabecera, agujas):
    for n, celda in enumerate(cabecera):
        plano = _limpiar(celda).lower()
        for aguja in agujas:
            if aguja in plano:
                return n
    return None


def _racha_de(celda):
    """La cifra de una celda de racha. `**3 de 3**. TOPE` da `"3 de 3"`."""
    plano = _limpiar(celda)
    encaje = RACHA.search(plano)
    if not encaje:
        return None
    if encaje.group(2):
        return "%s de %s" % (encaje.group(1), encaje.group(2))
    return encaje.group(1)


def tabla_de_rachas(lineas, desde, hasta):
    """La cabecera y las filas de la tabla de rachas de un acta, o `(None, [])`."""
    for n in range(desde, hasta):
        if not lineas[n].strip().startswith("|"):
            continue
        cabecera = _celdas(lineas[n])
        plano = " ".join(_limpiar(c).lower() for c in cabecera)
        if "especie" not in plano:
            continue
        if _columna(cabecera, CIERRE) is None:
            continue
        if n + 1 >= hasta or not SEPARADOR.match(lineas[n + 1].strip()):
            continue
        filas = []
        for m in range(n + 2, hasta):
            if not lineas[m].strip().startswith("|"):
                break
            filas.append(_celdas(lineas[m]))
        if filas:
            return cabecera, filas
    return None, []


def cosechar():
    """Un suceso por especie y por acta, en el orden en que las actas se escribieron."""
    lineas = io.open(RUTA_ACTA, encoding="utf-8").read().splitlines()
    marcas = [n for n, l in enumerate(lineas) if MARCA_ACTA.match(l)]
    sucesos, mudas = [], []
    for k, n in enumerate(marcas):
        fin = marcas[k + 1] if k + 1 < len(marcas) else len(lineas)
        numero = int(MARCA_ACTA.match(lineas[n]).group(1))
        vuelta = VUELTA.search(lineas[n])
        vuelta = int(vuelta.group(1)) if vuelta else None
        cabecera, filas = tabla_de_rachas(lineas, n, fin)
        if not filas:
            mudas.append(numero)
            continue
        col_cierre = _columna(cabecera, CIERRE)
        col_apertura = _columna(cabecera, APERTURA)
        if col_apertura == col_cierre:
            col_apertura = None
        for fila in filas:
            if len(fila) <= col_cierre:
                continue
            especies = _especies_de(fila[0])
            if not especies:
                continue
            cierre = _racha_de(fila[col_cierre])
            if cierre is None:
                continue
            for especie in especies:
                suceso = {
                    "tipo": "tanda",
                    "linea": credito.LINEA_SERIAL,
                    "vuelta": vuelta,
                    "tanda": "ACTA %d" % numero,
                    "especie": especie,
                    "racha": cierre,
                    "cita": "ACTA %d, su tabla de rachas" % numero,
                    "migrado": True,
                    # EL LITERAL DE LA CELDA VIAJA CON LA CIFRA, que es la regla de
                    # la casa (D.38.3). Las actas 1 a 7 escribian la fila del auditor
                    # como "N actas seguidas", que es OTRA unidad, anterior a que
                    # D.38 le diera una racha sola con tope: sin el literal al lado,
                    # ese `7` se leeria como siete de tres.
                    "celda": _limpiar(fila[col_cierre]),
                }
                if col_apertura is not None and len(fila) > col_apertura:
                    antes = _racha_de(fila[col_apertura])
                    if antes is not None:
                        suceso["cae"] = (credito._partir_racha(cierre)[0]
                                         > credito._partir_racha(antes)[0])
                        suceso["venia"] = antes
                sucesos.append(suceso)
    return sucesos, mudas


def main(argumentos):
    comun.salida_utf8()
    escribir = "--escribir" in argumentos
    sucesos, mudas = cosechar()
    destino = credito.ruta(credito.LINEA_SERIAL)

    print("MIGRACION DEL CREDITO DE LA LINEA SERIAL (D.48)")
    print("  fuente : %s" % comun.relativa(RUTA_ACTA))
    print("  destino: %s" % comun.relativa(destino))
    print("  sucesos: %d, de %d acta(s)"
          % (len(sucesos), len(set(s["tanda"] for s in sucesos))))
    con_cae = len([s for s in sucesos if "cae" in s])
    print("  con `cae` deducible de sus dos columnas : %d" % con_cae)
    print("  sin `cae`, que el replay declara y no supone: %d" % (len(sucesos) - con_cae))
    if mudas:
        print("  actas SIN tabla de rachas reconocible: %s"
              % ", ".join("ACTA %d" % m for m in mudas))
    print("")
    print("  %-6s %-8s %-18s %-9s %s" % ("acta", "vuelta", "especie", "queda", "cae"))
    print("  " + "-" * 62)
    for s in sucesos:
        print("  %-6s %-8s %-18s %-9s %s"
              % (s["tanda"].replace("ACTA ", ""), s["vuelta"], s["especie"],
                 s["racha"], s.get("cae", "sin dato")))

    if not escribir:
        print("")
        print("NADA ESCRITO: esto fue `--ver`. Con `--escribir` se vuelca el registro.")
        return 0
    if os.path.exists(destino):
        print("")
        print("NO ESCRIBO: %s ya existe. La migracion es de una sola vez."
              % comun.relativa(destino))
        return 1
    comun.escribir_jsonl(destino, sucesos)
    print("")
    print("ESCRITO: %d sucesos en %s" % (len(sucesos), comun.relativa(destino)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
