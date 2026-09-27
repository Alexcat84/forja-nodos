# -*- coding: utf-8 -*-
"""Imprime un paso concreto de un nodo del grafo. Uso: <id> <numero de paso>."""
import json, io, sys
nodo, n = sys.argv[1], int(sys.argv[2])
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l)
    if d['id'] == nodo:
        print('%s: %d pasos en el grafo' % (nodo, len(d['pasos_accionables'])))
        print('P%02d| %s' % (n, d['pasos_accionables'][n - 1]))
        break
else:
    print('NO ESTA EN EL GRAFO: %s' % nodo)
