# -*- coding: utf-8 -*-
"""Caracteres no ASCII en los pasos: primero los del tramo, despues los del
grafo entero, para saber si uno del tramo es anomalo o es la casa."""
import json, glob, io, collections, sys
mal = []
for f in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')
                + glob.glob('cuarentena/_insertados/scott_radical_candor/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    r = d.get('resumen_teorico', '')
    if 'cap_12.md' not in r and 'cap_13.md' not in r:
        continue
    for i, p in enumerate(d.get('pasos_accionables', []), 1):
        for ch in p:
            if ord(ch) > 127:
                j = p.index(ch)
                mal.append((d['id'], i, ord(ch), p[max(0, j - 45):j + 18]))
for i, n, cp, ctx in mal:
    print('%s P%02d: U+%04X en: ...%s...' % (i, n, cp, ctx))
print('TOTAL de caracteres no ASCII en los pasos del tramo: %d' % len(mal))
print()
c = collections.Counter()
tot = 0
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    if not l.strip():
        continue
    d = json.loads(l)
    for p in d.get('pasos_accionables', []):
        tot += 1
        for ch in p:
            if ord(ch) > 127:
                c[ch] += 1
print('pasos en el grafo: %d' % tot)
print('no ASCII en los pasos del grafo: %d' % sum(c.values()))
for ch, n in c.most_common():
    print('  U+%04X x%d' % (ord(ch), n))
