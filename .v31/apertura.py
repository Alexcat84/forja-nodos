# -*- coding: utf-8 -*-
"""LA APERTURA DE LA VUELTA 31, MEDIDA ANTES DE LA PRIMERA OPERACION."""
import json, os, subprocess, glob

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def lineas(ruta):
    with open(os.path.join(RAIZ, ruta), encoding="utf-8") as f:
        return sum(1 for _ in f)

def git(*args):
    return subprocess.check_output(("git",) + args, cwd=RAIZ).decode().strip()

sig = prev = 0
for l in open(os.path.join(RAIZ, "dataset/nodos.jsonl"), encoding="utf-8"):
    d = json.loads(l)
    sig += len(d.get("nodos_siguientes") or [])
    prev += len(d.get("nodos_previos") or [])

nocons = 0
for l in open(os.path.join(RAIZ, "bitacora/VEREDICTOS.jsonl"), encoding="utf-8"):
    d = json.loads(l)
    if any(a.get("no_consumada") is True for a in (d.get("anotaciones") or [])):
        nocons += 1

bandeja4 = len(glob.glob(os.path.join(RAIZ, "cuarentena/scott_radical_candor/*.json")))
insert4 = len(glob.glob(os.path.join(RAIZ, "cuarentena/_insertados/scott_radical_candor/*.json")))
bandeja5 = len(glob.glob(os.path.join(RAIZ, "cuarentena/marquet_turn_the_ship/*.json")))

filas = [
    ("rama", "`" + git("rev-parse", "--abbrev-ref", "HEAD") + "`", "`git rev-parse --abbrev-ref HEAD`"),
    ("commit al abrir mi turno", "`" + git("rev-parse", "--short", "HEAD") + "`", "`git rev-parse --short HEAD`"),
    ("nodos en `dataset/nodos.jsonl`", "**%d**" % lineas("dataset/nodos.jsonl"), "`dataset/nodos.jsonl`"),
    ("veredictos en `bitacora/VEREDICTOS.jsonl`", "**%d**" % lineas("bitacora/VEREDICTOS.jsonl"), "`bitacora/VEREDICTOS.jsonl`"),
    ("de ellos, con `no_consumada: true`", "**%d**" % nocons, "`bitacora/VEREDICTOS.jsonl`"),
    ("aristas por `nodos_siguientes`", "**%d**" % sig, "`dataset/nodos.jsonl`"),
    ("aristas por `nodos_previos`", "**%d**" % prev, "`dataset/nodos.jsonl`"),
    ("candidatos en bandeja, lote 4", "**%d**" % bandeja4, "PATRON: `cuarentena/scott_radical_candor/*.json`"),
    ("insertados y archivados, lote 4", "**%d**" % insert4, "PATRON: `cuarentena/_insertados/scott_radical_candor/*.json`"),
    ("candidatos en bandeja, lote 5", "**%d**" % bandeja5, "PATRON: `cuarentena/marquet_turn_the_ship/*.json`"),
    ("lote 4 insertado sobre `142`, por ciento", ("**%.1f**" % (100.0 * insert4 / 142)).replace(".", ","), "`cuarentena/_insertados/scott_radical_candor/`"),
]

print("LA APERTURA DE LA VUELTA 31, medida antes de la primera operacion")
print()
print("| pieza | valor | de donde sale |")
print("|---|---:|---|")
for a, b, c in filas:
    print("| %s | %s | %s |" % (a, b, c))
