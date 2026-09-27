# -*- coding: utf-8 -*-
"""CUANTOS NODOS DEL GRAFO SALEN DE CADA CAPITULO DE scott_radical_candor."""
import collections
import json
import re

cuenta = collections.Counter()
for l in open('dataset/nodos.jsonl', encoding='utf-8'):
    l = l.strip()
    if not l:
        continue
    n = json.loads(l)
    crudo = json.dumps(n, ensure_ascii=False)
    for cap in set(re.findall(r'scott_radical_candor/(cap_\d+)\.md', crudo)):
        cuenta[cap] += 1
print('nodos del grafo por capitulo de scott_radical_candor')
for c, k in sorted(cuenta.items()):
    print('  %-8s %d' % (c, k))
print('  TOTAL de nodos que citan el libro: %d' % sum(
    1 for l in open('dataset/nodos.jsonl', encoding='utf-8')
    if l.strip() and 'scott_radical_candor' in l))
