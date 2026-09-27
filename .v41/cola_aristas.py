# -*- coding: utf-8 -*-
"""La cola de aristas entera, recontada del dato.

D.15 / cierre v40 punto 3: la linea que trae `arista_corregida` se cuenta POR ESE
campo y no por `arista` a secas. Contadas por `arista` salen 12 auto aristas viejas
que ya llevan su correccion al lado, y ese 12 no es deuda.
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

nodos = {}
with open(os.path.join(RAIZ, "dataset", "nodos.jsonl"), encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()
        if linea:
            n = json.loads(linea)
            nodos[n["id"]] = n

filas = []
with open(os.path.join(RAIZ, "bitacora", "VEREDICTOS.jsonl"), encoding="utf-8") as f:
    for i, linea in enumerate(f, 1):
        linea = linea.strip()
        if not linea:
            continue
        v = json.loads(linea)
        if v.get("arista_en_cola") is not True:
            continue
        texto = v.get("arista_corregida") or v.get("arista", "")
        if ">" not in texto:
            filas.append((i, texto, "SIN PAR LEGIBLE", "", ""))
            continue
        madre, hijo = [p.strip() for p in texto.split(">", 1)]
        dentro_m = madre in nodos
        dentro_h = hijo in nodos
        cableada = dentro_m and hijo in nodos[madre].get("nodos_siguientes", [])
        filas.append((i, madre, hijo, dentro_m and dentro_h, cableada))

total = len(filas)
cableadas = [f for f in filas if f[4] is True]
esperan = [f for f in filas if f[3] is False]
huerfanas = [f for f in filas if f[3] is True and f[4] is False]

print("LA COLA DE ARISTAS ENTERA, de bitacora/VEREDICTOS.jsonl")
print("  lineas con arista_en_cola: true            : %d" % total)
print("  de ellas, YA CABLEADAS en el grafo         : %d" % len(cableadas))
print("  esperan a un extremo que no ha entrado     : %d" % len(esperan))
print("  con LOS DOS extremos dentro y SIN cable    : %d   <-- tiene que salir 0" % len(huerfanas))
print()
print("  %-6s %-52s %-52s %-8s %s" % ("linea", "madre", "hijo", "ambos", "cable"))
print("  " + "-" * 128)
for i, madre, hijo, ambos, cable in filas:
    print("  %-6d %-52s %-52s %-8s %s"
          % (i, madre[:52], hijo[:52],
             "si" if ambos else "NO", "si" if cable else "NO"))
if huerfanas:
    print()
    print("  NO SALE 0. Las que faltan por cablear:")
    for i, madre, hijo, _a, _c in huerfanas:
        print("    linea %d: %s > %s" % (i, madre, hijo))
