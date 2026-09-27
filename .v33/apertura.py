# -*- coding: utf-8 -*-
"""LA APERTURA DE LA VUELTA 33, MEDIDA DEL DATO Y NO TECLEADA (EXTRACTOR.md 4 y 5).

Cero constantes de conteo tecleadas: todo lo que imprime sale de contar el fichero.
"""
import glob
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
from src import comun  # noqa: E402


def git(*args):
    return subprocess.check_output(["git"] + list(args), cwd=RAIZ).decode().strip()


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
    ("rama", git("rev-parse", "--abbrev-ref", "HEAD"), "`git rev-parse --abbrev-ref HEAD`"),
    ("commit al abrir mi turno", "`%s`" % git("rev-parse", "--short", "HEAD"),
     "`git rev-parse --short HEAD`"),
    ("nodos en `dataset/nodos.jsonl`", "**%d**" % len(nodos), "`dataset/nodos.jsonl`"),
    ("veredictos en `bitacora/VEREDICTOS.jsonl`", "**%d**" % len(veredictos),
     "`bitacora/VEREDICTOS.jsonl`"),
    ("de ellos, con alguna anotacion `no_consumada: true`", "**%d**" % len(no_consumadas),
     "`bitacora/VEREDICTOS.jsonl`"),
    ("aristas por `nodos_siguientes`", "**%d**" % sig, "`dataset/nodos.jsonl`"),
    ("aristas por `nodos_previos`", "**%d**" % prev, "`dataset/nodos.jsonl`"),
    ("candidatos en bandeja, lote 4", "**%d**" % len(bandeja4),
     "PATRON: `cuarentena/scott_radical_candor/*.json`"),
    ("insertados y archivados, lote 4", "**%d**" % len(arch4),
     "PATRON: `cuarentena/_insertados/scott_radical_candor/*.json`"),
    ("candidatos en bandeja, lote 5", "**%d**" % len(bandeja5),
     "PATRON: `cuarentena/marquet_turn_the_ship/*.json`"),
    ("lote 4 insertado sobre `%d`, por ciento" % total4,
     "**%s**" % ("%.1f" % (100.0 * len(arch4) / total4)).replace(".", ","),
     "`cuarentena/_insertados/scott_radical_candor/`"),
]
print("| pieza | valor | de donde sale |")
print("|---|---:|---|")
for a, b, c in filas:
    print("| %s | %s | %s |" % (a, b, c))
