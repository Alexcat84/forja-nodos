# -*- coding: utf-8 -*-
"""QUE LINEAS DE cap_04 DICEN CUBRIR LOS NODOS QUE EXISTEN HOY (grafo + bandejas).
Se lee la cita 'L<num>' que cada resumen_teorico escribe, sin interpretar nada mas.
Sirve para ver que renglones del capitulo NO tiene reclamado ningun nodo."""
import json, os, re, glob, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
fichas = []
for l in open('dataset/nodos.jsonl', encoding='utf-8'):
    if l.strip(): fichas.append(('grafo', json.loads(l)))
for d in sorted(os.listdir('cuarentena')):
    p = os.path.join('cuarentena', d)
    if os.path.isdir(p) and d not in ('_insertados', '_derivadas'):
        for f in sorted(glob.glob(os.path.join(p, '*.json'))):
            fichas.append(('bandeja/' + d, json.load(open(f, encoding='utf-8'))))
print("fichas leidas (grafo + bandejas): %d" % len(fichas))
cubre = {}
for sede, c in fichas:
    rt = c.get('resumen_teorico') or ''
    if 'grove_high_output/cap_04.md' not in rt: continue
    for n in set(int(x) for x in re.findall(r'\bL(\d{1,4})\b', rt)):
        cubre.setdefault(n, []).append(c['id'])
L = open('fuentes/grove_high_output/cap_04.md', encoding='utf-8').read().split('\n')
print("renglones NO VACIOS de cap_04 entre L265 y L310, y quien los cita:")
for n in range(265, 311):
    if not L[n-1].strip(): continue
    q = cubre.get(n, [])
    print("  L%-4d %2d palabras  %s" % (n, len(L[n-1].split()),
          ('CITADO por ' + ', '.join(sorted(q))) if q else '>>> SIN CITA DE NINGUN NODO'))
