# -*- coding: utf-8 -*-
"""Pasos escritos POR CAPITULO de scott_radical_candor, contados sobre el grafo
de hoy. El denominador de PASOS INVENTADOS (AUDITOR_FORJA.md 8) sale de aqui y
no de ninguna tabla."""
import json, io, re, collections
cuenta = collections.Counter(); nodos = collections.Counter()
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    if not l.strip(): continue
    d = json.loads(l)
    r = d.get('resumen_teorico', '') or ''
    caps = sorted(set(re.findall(r'scott_radical_candor/(cap_\d\d)\.md', r)))
    if not caps: continue
    c = caps[0]
    cuenta[c] += len(d.get('pasos_accionables', []))
    nodos[c] += 1
print('%-8s %6s %8s' % ('cap', 'nodos', 'pasos'))
tn = tp = 0
for c in sorted(cuenta):
    print('%-8s %6d %8d' % (c, nodos[c], cuenta[c]))
    tn += nodos[c]; tp += cuenta[c]
print('%-8s %6d %8d' % ('TOTAL', tn, tp))
