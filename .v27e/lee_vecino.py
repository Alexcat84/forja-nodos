# -*- coding: utf-8 -*-
"""Imprime los pasos ENTEROS de un nodo, viva en el grafo o en la bandeja.
Remedio 1 del auditor aplicado a mi: un par se juzga con los DOS lados impresos."""
import json, io, os, sys

def cargar(ident):
    for ln in io.open("dataset/nodos.jsonl", encoding="utf-8"):
        n = json.loads(ln)
        if n["id"] == ident:
            return n, "grafo"
    for raiz, _, ficheros in os.walk("cuarentena"):
        if "_derivadas" in raiz:
            continue
        for f in ficheros:
            if f == ident + ".json":
                return json.load(io.open(os.path.join(raiz, f), encoding="utf-8")), raiz
    return None, None

for ident in sys.argv[1:]:
    n, donde = cargar(ident)
    if n is None:
        print("NO ENCONTRADO: %s" % ident); continue
    print("=== %s  [%s]  %d pasos" % (n["id"], donde, len(n["pasos_accionables"])))
    print("  titulo    : %s" % n["titulo"])
    print("  activacion: %s" % n["condiciones_activacion"])
    for i, p in enumerate(n["pasos_accionables"], 1):
        print("  %2d. %s" % (i, p))
    print("  ENTREGABLE: %s" % n["entregable_esperado"])
    print()
