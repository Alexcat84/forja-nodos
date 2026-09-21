# -*- coding: utf-8 -*-
"""CUANTOS NODOS DE cap_04 EXISTEN HOY, contados por mi sobre grafo + bandejas.
La cuenta sale de que el resumen_teorico nombre fuentes/grove_high_output/cap_04.md."""
import json, os, glob, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
fichas = []
for l in open('dataset/nodos.jsonl', encoding='utf-8'):
    if l.strip(): fichas.append(('grafo', json.loads(l)))
for d in sorted(os.listdir('cuarentena')):
    p = os.path.join('cuarentena', d)
    if os.path.isdir(p) and d not in ('_insertados', '_derivadas'):
        for f in sorted(glob.glob(os.path.join(p, '*.json'))):
            fichas.append(('bandeja/' + d, json.load(open(f, encoding='utf-8'))))
nuevos = set(l.strip().split('/')[-1][:-5] for l in open('.v48aud/02_candidatos_nuevos.out', encoding='utf-8') if l.strip())
de04 = [(s, c['id']) for s, c in fichas if 'grove_high_output/cap_04.md' in (c.get('resumen_teorico') or '')]
print('nodos que dicen salir de cap_04, LISTA ENTERA (%d):' % len(de04))
for s, i in sorted(de04, key=lambda x: x[1]):
    print('   [%-24s] %s%s' % (s, i, '  <-- nacido en esta vuelta' if i in nuevos else ''))
print()
print('nacidos en esta vuelta: %d   ya estaban: %d' % (len([1 for _, i in de04 if i in nuevos]),
                                                      len([1 for _, i in de04 if i not in nuevos])))
