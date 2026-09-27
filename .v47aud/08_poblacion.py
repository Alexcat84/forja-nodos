# -*- coding: utf-8 -*-
"""D.38.4: la poblacion del barrido es GRAFO + BANDEJAS.
Grafo   = dataset/nodos.jsonl
Bandejas= cuarentena/<libro>/*.json, DESCARTANDO _insertados y _derivadas.
Imprime el censo por sede. Cero interpretacion."""
import json, os, sys, io, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
grafo = [json.loads(l) for l in open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
print('grafo   dataset/nodos.jsonl        : %4d' % len(grafo))
tot_b = 0
for d in sorted(os.listdir('cuarentena')):
    p = os.path.join('cuarentena', d)
    if not os.path.isdir(p) or d in ('_insertados', '_derivadas'):
        continue
    n = len(glob.glob(os.path.join(p, '*.json')))
    tot_b += n
    print('bandeja cuarentena/%-26s: %4d' % (d + '/', n))
print('-' * 48)
print('POBLACION DEL BARRIDO (grafo + bandejas): %4d' % (len(grafo) + tot_b))
print('  ... de los cuales bandejas            : %4d' % tot_b)
print('DESCARTADOS a proposito (D.38.4):')
for d in ('_insertados', '_derivadas'):
    p = os.path.join('cuarentena', d)
    n = len(glob.glob(os.path.join(p, '*.json'))) if os.path.isdir(p) else 0
    print('  cuarentena/%-12s: %4d' % (d + '/', n))
