# -*- coding: utf-8 -*-
"""Censo de rotulos de cap_07 y de que nodo recoge cada uno.
ROTULO = linea no vacia de menos de 90 caracteres que no termina en punto.
Poblacion de nodos: grafo mas bandejas (D.38.4)."""
import json, io, glob, re
RE_CAP = re.compile(r"fuentes/([a-z0-9_]+)/(cap_\d+)\.md")
RE_LIN = re.compile(r"l[ií]neas?\s+(\d+)\s+a\s+(\d+)")
lineas = io.open("fuentes/scott_radical_candor/cap_07.md", encoding="utf-8").read().split("\n")

dueno = {}
def cargar(it, donde):
    for d in it:
        r = d.get("resumen_teorico","") or ""
        mc = RE_CAP.search(r)
        if not mc or mc.group(2) != "cap_07": continue
        for a,b in RE_LIN.findall(r):
            for n in range(int(a), int(b)+1):
                dueno.setdefault(n, (donde, d["id"]))
cargar((json.loads(l) for l in io.open("dataset/nodos.jsonl",encoding="utf-8")), "GRAFO")
cargar((json.load(io.open(f,encoding="utf-8")) for f in sorted(glob.glob("cuarentena/scott_radical_candor/*.json"))), "BANDEJA")

rotulos=[]
for i,t in enumerate(lineas, 1):
    s=t.strip()
    if not s or i<=7: continue
    if len(s)<90 and not s.endswith(".") and not s.startswith("\u2014") and not s.startswith("\u2014"):
        rotulos.append((i,s))
print("ROTULOS DETECTADOS: %d" % len(rotulos))
print()
print("%-6s %-8s %-46s %s" % ("linea","donde","nodo que lo recoge","rotulo"))
sin=0
for i,s in rotulos:
    d = dueno.get(i)
    if d is None: sin+=1
    print("%-6d %-8s %-46s %s" % (i, d[0] if d else "NADIE", d[1] if d else "-", s[:60]))
print()
print("ROTULOS SIN NODO QUE LOS RECLAME: %d de %d" % (sin, len(rotulos)))
