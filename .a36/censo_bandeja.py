# -*- coding: utf-8 -*-
"""Censo de la bandeja de scott_radical_candor: capitulo de origen, pasos y lineas.
El capitulo sale de la cadena 'UNIDAD DE ORIGEN: fuentes/<clave>/cap_NN.md' del
resumen_teorico, que es la convencion que el propio material escribe."""
import json, glob, os, re, collections

BAND = 'cuarentena/scott_radical_candor'
pat = re.compile(r'UNIDAD DE ORIGEN:\s*fuentes/scott_radical_candor/(cap_\d+)\.md')
filas = []
for f in sorted(glob.glob(os.path.join(BAND, '*.json'))):
    d = json.load(open(f, encoding='utf-8'))
    m = pat.search(d.get('resumen_teorico', ''))
    cap = m.group(1) if m else 'SIN_RUTA'
    filas.append((cap, d['id'], len(d.get('pasos_accionables', [])),
                  len(d.get('nodos_previos', [])) + len(d.get('nodos_siguientes', []))))

por_cap = collections.Counter(c for c, _, _, _ in filas)
pasos_cap = collections.Counter()
for c, _, p, _ in filas:
    pasos_cap[c] += p

print('CANDIDATOS EN BANDEJA: %d' % len(filas))
for cap in sorted(por_cap):
    print('  %s: %d candidatos, %d pasos' % (cap, por_cap[cap], pasos_cap[cap]))
print()
print('%-8s %-56s %5s %7s' % ('cap', 'id', 'pasos', 'aristas'))
for cap, i, p, a in sorted(filas):
    print('%-8s %-56s %5d %7d' % (cap, i, p, a))
