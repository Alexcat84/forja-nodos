# -*- coding: utf-8 -*-
"""Cobertura de linea de cap_07: que lineas reclama algun nodo (grafo o bandeja) y
que lineas no las reclama nadie. Poblacion D.38.4. Solo cuenta lineas NO vacias."""
import json, io, glob, re
CAP = "cap_07"; LIBRO = "scott_radical_candor"
RUTA = "fuentes/%s/%s.md" % (LIBRO, CAP)
RE_CAP = re.compile(r"fuentes/([a-z0-9_]+)/(cap_\d+)\.md")
RE_LIN = re.compile(r"l[ií]neas?\s+(\d+)\s+a\s+(\d+)")

def tramos(d):
    r = d.get("resumen_teorico","") or ""
    mc = RE_CAP.search(r)
    if not mc or mc.group(2) != CAP: return None
    return [(int(a),int(b)) for a,b in RE_LIN.findall(r)]

reclamada = {}
def cargar(it, donde):
    for d in it:
        t = tramos(d)
        if t is None: continue
        for a,b in t:
            for n in range(a,b+1):
                reclamada.setdefault(n, []).append((donde, d["id"]))

cargar((json.loads(l) for l in io.open("dataset/nodos.jsonl",encoding="utf-8")), "GRAFO")
cargar((json.load(io.open(f,encoding="utf-8")) for f in sorted(glob.glob("cuarentena/%s/*.json"%LIBRO))), "BANDEJA")

lineas = io.open(RUTA, encoding="utf-8").read().split("\n")
total = len(lineas)
novacias = [i+1 for i,t in enumerate(lineas) if t.strip()]
huerfanas = [n for n in novacias if n not in reclamada]
print("fichero            : %s" % RUTA)
print("lineas totales     : %d" % total)
print("lineas NO vacias   : %d" % len(novacias))
print("lineas reclamadas  : %d" % len([n for n in novacias if n in reclamada]))
print("lineas HUERFANAS   : %d" % len(huerfanas))
print("lineas reclamadas por MAS DE UN nodo: %d" % len([n for n in reclamada if len(reclamada[n])>1]))
print()
print("--- LAS HUERFANAS, con su primer tramo de texto ---")
for n in huerfanas:
    print("%4d: %s" % (n, lineas[n-1][:150]))
print()
print("--- LAS SOLAPADAS ---")
for n in sorted(reclamada):
    if len(reclamada[n])>1:
        print("%4d: %s" % (n, " | ".join("%s %s"%x for x in reclamada[n])))
