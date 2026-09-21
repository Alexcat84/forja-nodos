# -*- coding: utf-8 -*-
"""D.58 dice que en MODO_INSERCION=cuarentena NO hay fase ciega, NO hay sello y
NO hay testigo. Esta corrida arranco en cuarentena y las tres ocurrieron."""
import re, json
ARR = "2026-09-20 12:08:04"
log = open("docs/loop/loop.log", encoding="utf-8", errors="replace").read().splitlines()
print("$ grep -nE 'arranque|APERTURA CIEGA|apertura ciega sellada' docs/loop/loop.log | tail")
for i, l in enumerate(log, 1):
    if re.search(r"arranque:|APERTURA CIEGA|apertura ciega sellada", l) and l[1:20] >= ARR:
        print("  %d:%s" % (i, l))
print()
print("$ tail -1 docs/loop/SELLOS_APERTURA.jsonl")
print("  " + open("docs/loop/SELLOS_APERTURA.jsonl", encoding="utf-8").read().strip().splitlines()[-1])
print()
t = json.load(open("docs/loop/TESTIGO_GUARDAS.json", encoding="utf-8"))
print("$ docs/loop/TESTIGO_GUARDAS.json")
print("  fecha del testigo : %s   commit : %s   guardas: %s" % (t["fecha"], t["commit"], ", ".join(t["guardas"])))
print()
print("LAS TRES QUE D.58 QUITA DEL REGIMEN LIGERO, CONTADAS EN ESTA CORRIDA:")
print("  fase ciega abierta : %d" % sum(1 for l in log if "APERTURA CIEGA" in l and l[1:20] >= ARR))
print("  sello escrito      : %d" % sum(1 for l in log if "apertura ciega sellada" in l and l[1:20] >= ARR))
print("  testigo escrito    : %d  (su fecha, %s, cae dentro de esta corrida)" % (1 if t["fecha"] >= ARR else 0, t["fecha"]))
print()
print("Y LO QUE COSTO, leido del log y no estimado:")
for l in log:
    if "auditor ciego listo" in l and l[1:20] >= ARR: print("  " + l)
