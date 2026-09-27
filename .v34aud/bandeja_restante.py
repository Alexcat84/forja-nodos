# -*- coding: utf-8 -*-
"""LO QUE cap_09 DEJA EN BANDEJA, con su linea del libro. CERO IDS TECLEADOS."""
import io, json, os, re
D = 'cuarentena/scott_radical_candor'
f5 = []
for f in sorted(os.listdir(D)):
    if not f.endswith('.json'): continue
    d = json.load(io.open(os.path.join(D, f), encoding='utf-8'))
    rt = d.get('resumen_teorico') or ''
    if 'cap_09.md' not in rt: continue
    m = re.search(r'l[ií]neas? (\d+)\s*(?:a|-|hasta)\s*(\d+)', rt)
    f5.append((int(m.group(1)), int(m.group(2)), d['id'], len(d['pasos_accionables'])))
print('| # | candidato de `cap_09` que SIGUE EN BANDEJA | lineas del libro | pasos |')
print('|---:|---|---|---:|')
for k, (a, b, i, p) in enumerate(sorted(f5), 1):
    print('| %d | `%s` | L%d a L%d | %d |' % (k, i, a, b, p))
print()
print('candidatos de cap_09 en bandeja : %d' % len(f5))
print('candidatos de cap_09 insertados : %d' % sum(
    1 for l in io.open('dataset/nodos.jsonl', encoding='utf-8')
    if l.strip() and 'scott_radical_candor/cap_09.md' in json.loads(l).get('resumen_teorico', '')))
print('total del capitulo              : %d   techo de EXTRACTOR.md 12.4: 15' % (len(f5) + sum(
    1 for l in io.open('dataset/nodos.jsonl', encoding='utf-8')
    if l.strip() and 'scott_radical_candor/cap_09.md' in json.loads(l).get('resumen_teorico', ''))))
