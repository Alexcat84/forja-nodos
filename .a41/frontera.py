# -*- coding: utf-8 -*-
"""Que nodos del grafo citan cap_13 o cap_14 de scott, y que lineas dicen cubrir."""
import json, io, re, sys
cap = sys.argv[1]
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    if not l.strip():
        continue
    d = json.loads(l)
    r = d.get('resumen_teorico', '') or ''
    if cap + '.md' not in r:
        continue
    m = re.search(r'Sale de las? lineas? ([0-9 ayl,]+?)[,.]', r)
    print('%-58s %s' % (d['id'], (m.group(1).strip() if m else '(sin formula)')))
