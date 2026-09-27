# -*- coding: utf-8 -*-
"""Mi propio barrido de caracteres de control, sobre la poblacion COMPLETA:
346 nodos del grafo mas los 577 .json de cuarentena, sin excluir _derivadas."""
import json, os
hits, docs, fichas = [], 0, 0
def scan(label, obj, path=""):
    if isinstance(obj, str):
        for i, ch in enumerate(obj):
            if ord(ch) < 32 and ch not in "\n\t\r":
                hits.append((label, path, i, "U+%04X" % ord(ch)))
    elif isinstance(obj, dict):
        for k, v in obj.items(): scan(label, v, path + "." + k)
    elif isinstance(obj, list):
        for n, v in enumerate(obj): scan(label, v, path + "[%d]" % n)
for line in open("dataset/nodos.jsonl", encoding="utf-8"):
    if line.strip():
        docs += 1; d = json.loads(line); scan("dataset:" + d.get("id", "?"), d)
for root, _, files in os.walk("cuarentena"):
    for fn in files:
        if fn.endswith(".json"):
            p = os.path.join(root, fn); fichas += 1; docs += 1
            scan(p.replace("\\", "/"), json.load(open(p, encoding="utf-8")))
print("nodos del grafo barridos              : %d" % (docs - fichas))
print("fichas .json bajo cuarentena/ barridas: %d  (SIN excluir _derivadas)" % fichas)
print("documentos barridos                   : %d" % docs)
print("caracteres de control ENCONTRADOS     : %d" % len(hits))
for h in hits: print("  %s  campo %s  posicion %d  %s" % h)
