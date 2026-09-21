# -*- coding: utf-8 -*-
"""El estado AL CIERRE de la vuelta 38, recomputado al cierre y no copiado de la apertura.

EXTRACTOR.md 4: toda cifra que describa el estado al cerrar se RECOMPUTA si algo de la
propia vuelta pudo haberla movido. Esta vuelta movio nodos, veredictos, aristas, bandeja
e insertados, asi que se recomputan los seis.
"""
import glob
import json
import os
import subprocess


def sh(c):
    return subprocess.run(c, shell=True, capture_output=True, text=True).stdout.strip()


RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
nodos = [json.loads(l) for l in open(os.path.join(RAIZ, "dataset", "nodos.jsonl"),
                                     encoding="utf-8") if l.strip()]
ver = [json.loads(l) for l in open(os.path.join(RAIZ, "bitacora", "VEREDICTOS.jsonl"),
                                   encoding="utf-8") if l.strip()]
sig = sum(len(n.get("nodos_siguientes", [])) for n in nodos)
prev = sum(len(n.get("nodos_previos", [])) for n in nodos)
noc = 0
for v in ver:
    anot = v.get("anotaciones")
    if isinstance(anot, list) and any(a.get("no_consumada") is True for a in anot):
        noc += 1
band = len(glob.glob(os.path.join(RAIZ, "cuarentena", "scott_radical_candor", "*.json")))
ins = len(glob.glob(os.path.join(RAIZ, "cuarentena", "_insertados",
                                 "scott_radical_candor", "*.json")))
band5 = len(glob.glob(os.path.join(RAIZ, "cuarentena", "marquet_turn_the_ship", "*.json")))
tot = band + ins

# LA APERTURA, TECLEADA AQUI A PROPOSITO PARA QUE LA COLUMNA DE MOVIMIENTO SE PUEDA
# RECONSTRUIR. Sale de .v38/apertura_tabla.txt, que es su sede y viaja en el commit.
APERTURA = {
    "nodos": 318, "veredictos": 475, "no_consumada": 14, "siguientes": 122,
    "previos": 122, "bandeja4": 27, "insertados4": 115, "bandeja5": 3,
}

filas = [
    ("rama", sh("git rev-parse --abbrev-ref HEAD"), "", "`git rev-parse --abbrev-ref HEAD`"),
    ("commit al cerrar", "`%s`" % sh("git rev-parse --short HEAD"), "",
     "`git rev-parse --short HEAD`"),
    ("nodos en `dataset/nodos.jsonl`", len(nodos), APERTURA["nodos"], "`dataset/nodos.jsonl`"),
    ("veredictos en `bitacora/VEREDICTOS.jsonl`", len(ver), APERTURA["veredictos"],
     "`bitacora/VEREDICTOS.jsonl`"),
    ("de ellos, con anotacion `no_consumada: true`", noc, APERTURA["no_consumada"],
     "`bitacora/VEREDICTOS.jsonl`"),
    ("aristas por `nodos_siguientes`", sig, APERTURA["siguientes"], "`dataset/nodos.jsonl`"),
    ("aristas por `nodos_previos`", prev, APERTURA["previos"], "`dataset/nodos.jsonl`"),
    ("candidatos en bandeja, lote 4", band, APERTURA["bandeja4"],
     "PATRON: `cuarentena/scott_radical_candor/*.json`"),
    ("insertados y archivados, lote 4", ins, APERTURA["insertados4"],
     "PATRON: `cuarentena/_insertados/scott_radical_candor/*.json`"),
    ("candidatos en bandeja, lote 5", band5, APERTURA["bandeja5"],
     "PATRON: `cuarentena/marquet_turn_the_ship/*.json`"),
]

print("| pieza | al abrir | al cerrar | movimiento | de donde sale |")
print("|---|---:|---:|---:|---|")
for nombre, valor, abre, sede in filas:
    if abre == "":
        print("| %s | %s | %s | . | %s |" % (nombre, valor, valor, sede))
    else:
        d = valor - abre
        print("| %s | %d | **%d** | %s | %s |"
              % (nombre, abre, valor, ("+%d" % d) if d > 0 else str(d), sede))
pct = ("%.1f" % (100.0 * ins / tot)).replace(".", ",")
print("| lote 4 insertado sobre `%d`, por ciento | 81,0 | **%s** | +%s | "
      "`cuarentena/_insertados/scott_radical_candor/` |"
      % (tot, pct, ("%.1f" % (100.0 * ins / tot - 81.0)).replace(".", ",")))
