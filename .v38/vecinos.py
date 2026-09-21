# -*- coding: utf-8 -*-
"""Los vecinos que la aduana levanta, leidos donde vivan (grafo o bandeja)."""
import glob
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fichas = {}
with open(os.path.join(RAIZ, "dataset", "nodos.jsonl"), encoding="utf-8") as f:
    for l in f:
        l = l.strip()
        if l:
            d = json.loads(l)
            fichas[d["id"]] = ("GRAFO", d)
for ruta in glob.glob(os.path.join(RAIZ, "cuarentena", "*", "*.json")):
    if "_insertados" in ruta:
        continue
    d = json.load(open(ruta, encoding="utf-8"))
    if not isinstance(d, dict) or "id" not in d:
        continue
    fichas.setdefault(d["id"], ("BANDEJA", d))

for cid in sys.argv[1:]:
    if cid not in fichas:
        print("=== %s : NO EXISTE ni en grafo ni en bandeja ===" % cid)
        continue
    sede, d = fichas[cid]
    print("=== %s  [%s] ===" % (cid, sede))
    print("  titulo    : %s" % d["titulo"])
    print("  activacion: %s" % d["condiciones_activacion"])
    print("  entregable: %s" % d["entregable_esperado"])
    print("  pasos     : %d" % len(d["pasos_accionables"]))
    for i, p in enumerate(d["pasos_accionables"], 1):
        print("     P%02d %s" % (i, p[:190]))
    print()
