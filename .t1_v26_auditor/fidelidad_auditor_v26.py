# -*- coding: utf-8 -*-
"""Relectura ancha D.30 del AUDITOR: cada paso pegado a la linea del libro que
lo tiene que sostener. Imprime, no juzga: el veredicto lo pone el auditor."""
import json, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
cand, ruta_cap = sys.argv[1], sys.argv[2]
mapa = {}            # paso -> [lineas]
for a in sys.argv[3:]:
    p, ls = a.split(":")
    mapa[int(p)] = [int(x) for x in ls.split(",")]
d = json.load(open(cand, encoding='utf-8'))
lin = io.open(ruta_cap, encoding='utf-8').read().split("\n")
print("CANDIDATO :", d["id"])
print("CAPITULO  :", ruta_cap)
print("PASOS     :", len(d.get("pasos_accionables") or []))
for i, p in enumerate(d.get("pasos_accionables") or [], 1):
    print("="*100)
    print("PASO %d> %s" % (i, p))
    for L in mapa.get(i, []):
        t = lin[L-1].strip()
        print("  --- L%d del libro ---" % L)
        for j in range(0, len(t), 96):
            print("      " + t[j:j+96])
    if i not in mapa:
        print("  --- SIN LINEA DECLARADA POR MI ---")
