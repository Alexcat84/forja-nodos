# -*- coding: utf-8 -*-
"""EL CIERRE DE LA VUELTA 33, RECOMPUTADO AL CERRAR (EXTRACTOR.md 4).

Es el mismo fichero que la apertura (`.v33/apertura.py`) con la columna de contraste:
toda cifra que esta vuelta pudo mover se vuelve a medir aqui, y al lado va la de la
apertura leida de `.v33/apertura_tabla.txt`, que es el fichero que el hook talla.
CERO cifras tecleadas: la columna de apertura se PARSEA de ese fichero.
"""
import glob
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
from src import comun  # noqa: E402


def git(*args):
    return subprocess.check_output(["git"] + list(args), cwd=RAIZ).decode().strip()


apertura = {}
for linea in open(os.path.join(RAIZ, ".v33/apertura_tabla.txt"), encoding="utf-8"):
    celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
    if len(celdas) == 3 and not celdas[0].startswith("-") and celdas[0] != "pieza":
        apertura[celdas[0]] = celdas[1]

nodos = comun.leer_jsonl(comun.RUTA_DATASET)
veredictos = comun.leer_jsonl(comun.RUTA_VEREDICTOS)
no_consumadas = [v for v in veredictos
                 if any(a.get("no_consumada") for a in (v.get("anotaciones") or []))]
sig = sum(len(n.get("nodos_siguientes") or []) for n in nodos)
prev = sum(len(n.get("nodos_previos") or []) for n in nodos)
bandeja4 = glob.glob(os.path.join(RAIZ, "cuarentena/scott_radical_candor/*.json"))
arch4 = glob.glob(os.path.join(RAIZ, "cuarentena/_insertados/scott_radical_candor/*.json"))
bandeja5 = glob.glob(os.path.join(RAIZ, "cuarentena/marquet_turn_the_ship/*.json"))
total4 = len(bandeja4) + len(arch4)

filas = [
    ("rama", git("rev-parse", "--abbrev-ref", "HEAD")),
    ("commit al abrir mi turno", "`%s`" % git("rev-parse", "--short", "HEAD")),
    ("nodos en `dataset/nodos.jsonl`", "**%d**" % len(nodos)),
    ("veredictos en `bitacora/VEREDICTOS.jsonl`", "**%d**" % len(veredictos)),
    ("de ellos, con alguna anotacion `no_consumada: true`", "**%d**" % len(no_consumadas)),
    ("aristas por `nodos_siguientes`", "**%d**" % sig),
    ("aristas por `nodos_previos`", "**%d**" % prev),
    ("candidatos en bandeja, lote 4", "**%d**" % len(bandeja4)),
    ("insertados y archivados, lote 4", "**%d**" % len(arch4)),
    ("candidatos en bandeja, lote 5", "**%d**" % len(bandeja5)),
    ("lote 4 insertado sobre `%d`, por ciento" % total4,
     "**%s**" % ("%.1f" % (100.0 * len(arch4) / total4)).replace(".", ",")),
]

print("| pieza | al abrir | **al cerrar** | movida por esta vuelta |")
print("|---|---:|---:|---|")
for nombre, ahora in filas:
    antes = apertura.get(nombre, "*no medida al abrir*")
    if nombre == "commit al abrir mi turno":
        nombre, movida = "commit", "si, es el de ahora"
    else:
        movida = "**si**" if antes != ahora else "no"
    print("| %s | %s | %s | %s |" % (nombre, antes, ahora, movida))
