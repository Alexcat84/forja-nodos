# -*- coding: utf-8 -*-
"""Reparto de bitacora/VEREDICTOS.jsonl: por consumada, por veredicto, y las nuevas."""
import json, io, collections
lineas=[json.loads(l) for l in io.open("bitacora/VEREDICTOS.jsonl",encoding="utf-8") if l.strip()]
print("lineas totales            : %d" % len(lineas))
cons=collections.Counter(d.get("consumada") for d in lineas)
for k in sorted(cons, key=lambda x: str(x)):
    print("  consumada=%-6s -> %d" % (k, cons[k]))
print()
print("--- LAS DECLARADAS NO CONSUMADAS, con su numero de linea ---")
for i,d in enumerate(lineas,1):
    if d.get("consumada") is False:
        print("  linea %3d  %-28s %-46s %s" % (i, d.get("veredicto"), d.get("candidato"), d.get("vecino")))
print()
print("--- LINEAS 265 EN ADELANTE (las nuevas sobre las 264 de la ACTA 27) ---")
print("%-5s %-9s %-10s %-44s %s" % ("linea","veredicto","consumada","candidato","vecino"))
for i,d in enumerate(lineas,1):
    if i>=265:
        print("%-5d %-9s %-10s %-44s %s" % (i, d.get("veredicto"), d.get("consumada"), d.get("candidato"), d.get("vecino")))
print()
nuevas=[d for i,d in enumerate(lineas,1) if i>=265]
print("nuevas: %d   de ellas consumadas: %d   no consumadas: %d" % (
    len(nuevas), sum(1 for d in nuevas if d.get("consumada") is True),
    sum(1 for d in nuevas if d.get("consumada") is False)))
print("veredictos de las nuevas: %s" % dict(collections.Counter(d.get("veredicto") for d in nuevas)))
