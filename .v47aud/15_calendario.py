# -*- coding: utf-8 -*-
"""Existe en alguna sede un nodo del CALENDARIO como herramienta de planificacion
(L273 a L279 de cap_04)? Busco por id y por titulo en grafo + bandejas."""
import json, os, sys, io, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
pobl = []
for l in open('dataset/nodos.jsonl', encoding='utf-8'):
    if l.strip():
        pobl.append(('grafo', json.loads(l)))
for d in sorted(os.listdir('cuarentena')):
    p = os.path.join('cuarentena', d)
    if not os.path.isdir(p) or d in ('_insertados', '_derivadas'):
        continue
    for f in sorted(glob.glob(os.path.join(p, '*.json'))):
        pobl.append(('bandeja/' + d, json.load(open(f, encoding='utf-8'))))
print('buscado en %d nodos (grafo + TODAS las bandejas, sin filtro)' % len(pobl))
for clave in ('calendar', 'planificacion', 'holgura', 'slack', 'decir_no', 'inventario_proyectos'):
    hits = [(s, n.get('id')) for s, n in pobl
            if clave in (n.get('id') or '').lower() or clave in (n.get('titulo') or '').lower()]
    print('  %-22s -> %s' % (clave, hits if hits else 'CERO'))
