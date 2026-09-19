# -*- coding: utf-8 -*-
"""LOS PASOS DE cap_04 CONTADOS POR MI, Y LA DIFERENCIA CONTRA HEAD~1."""
import json, io, os, subprocess, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BAND = os.path.join(RAIZ, "cuarentena", "grove_high_output")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def cap_de(f):
    r = f.get("resumen_teorico") or ""
    for c in ("cap_01","cap_02","cap_03","cap_04","cap_05"):
        if c in r:
            return c
    return "?"

total = 0
porcap = {}
fichas04 = []
for nombre in sorted(os.listdir(BAND)):
    if not nombre.endswith(".json"):
        continue
    f = json.loads(io.open(os.path.join(BAND, nombre), encoding="utf-8").read())
    c = cap_de(f)
    n = len(f.get("pasos_accionables") or [])
    porcap.setdefault(c, [0, 0])
    porcap[c][0] += 1
    porcap[c][1] += n
    if c == "cap_04":
        fichas04.append((nombre, n))
for c in sorted(porcap):
    print("   %-8s %2d fichas  %4d pasos" % (c, porcap[c][0], porcap[c][1]))
print()
print("   LAS FICHAS DE cap_04, UNA A UNA:")
for nombre, n in fichas04:
    print("      %-62s %2d" % (nombre[:-5], n))
print("   cap_04: %d fichas, %d pasos" % (len(fichas04), sum(n for _, n in fichas04)))
