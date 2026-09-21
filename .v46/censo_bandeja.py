# -*- coding: utf-8 -*-
"""Censo de la bandeja de grove: capitulo, pasos, aristas y tramo declarado."""
import json, os, re, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BAND = os.path.join(RAIZ, "cuarentena", "grove_high_output")
filas, total = [], 0
for n in sorted(os.listdir(BAND)):
    if not n.endswith(".json"):
        continue
    d = json.load(open(os.path.join(BAND, n), encoding="utf-8"))
    crudo = open(os.path.join(BAND, n), encoding="utf-8").read()
    caps = sorted(set(re.findall(r"grove_high_output/(cap_\d+)\.md", crudo)))
    pasos = len(d.get("pasos_accionables", []))
    total += pasos
    rt = d.get("resumen_teorico", "")
    m = re.search(r"(PIEZA\s+P\d+)[^.]*?(L\d+\s*(?:a\s*L\d+)?)", rt)
    tramo = (m.group(1) + " " + m.group(2)) if m else "?"
    filas.append((caps[0] if caps else "?", d.get("id", n), pasos,
                  len(d.get("nodos_previos", []) + d.get("nodos_siguientes", [])), tramo))
for f in sorted(filas):
    print("%s %-48s pasos=%2d aristas=%d  %s" % f)
print("candidatos=%d  pasos_totales=%d" % (len(filas), total))
