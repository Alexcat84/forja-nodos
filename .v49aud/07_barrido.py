# -*- coding: utf-8 -*-
"""BARRIDO DE VECINOS (D.38.4) de las DOS fichas que la vuelta 49 corrigio.

LA CIFRA ES LA DE LA CASA: cada valor sale de src.aduana.senal_similitud_texto sobre
comun.texto_comparable, la misma funcion que corre la aduana (src/aduana.py:278). No
reimplemento la senial y no la aproximo.

POBLACION: grafo + bandejas (D.38.4), descartando _insertados y _derivadas y con el
filtro de fuente canonica. LISTA ORDENADA ENTERA de los 8 primeros por ficha.

Se corre UNA FICHA POR PROCESO (argumento en la linea de ordenes)."""
from __future__ import print_function
import json, os, sys, glob, time
sys.path.insert(0, '.')
from src import aduana, comun

TOPE = 8
fid = sys.argv[1]
umbral = json.load(open('config/umbrales.json', encoding='utf-8'))['umbral_similitud_texto']
tabla = json.load(open('fuentes/FUENTES_CANONICAS.json', encoding='utf-8'))
canon = set(k for k in tabla if not k.startswith('_'))

pobl = []
for l in open('dataset/nodos.jsonl', encoding='utf-8'):
    if l.strip():
        c = json.loads(l)
        pobl.append(('grafo', c.get('id'), comun.texto_comparable(c)))
for d in sorted(os.listdir('cuarentena')):
    p = os.path.join('cuarentena', d)
    if not os.path.isdir(p) or d in ('_insertados', '_derivadas'):
        continue
    for f in sorted(glob.glob(os.path.join(p, '*.json'))):
        c = json.load(open(f, encoding='utf-8'))
        claves = [x.get('clave') for x in (c.get('fuentes') or [])]
        if claves and all(k in canon for k in claves):
            pobl.append(('bandeja/' + d, c.get('id'), comun.texto_comparable(c)))

cand = json.load(open('cuarentena/grove_high_output/%s.json' % fid, encoding='utf-8'))
ta = comun.texto_comparable(cand)
t0 = time.time()
medidos = [(aduana.senal_similitud_texto(ta, tb), sede, oid)
           for sede, oid, tb in pobl if oid != cand['id']]
medidos.sort(reverse=True)
print('=' * 78)
print('FICHA: %s   (%d pasos)' % (cand['id'], len(cand['pasos_accionables'])))
print('  poblacion barrida: %d nodos (grafo + bandejas, filtro canonico)' % len(pobl))
print('  medidos al digito: %d de %d; descartados: 0' % (len(medidos), len(medidos)))
print('  umbral de la casa (config/umbrales.json): %s' % umbral)
print('  reloj del barrido: %.1f s' % (time.time() - t0))
print('  LOS %d VECINOS MAS PROXIMOS, LISTA ORDENADA ENTERA:' % TOPE)
for s, sede, oid in medidos[:TOPE]:
    print('    %.4f  [%-24s] %s' % (s, sede, oid))
print('  vecinos por encima del umbral %s: %d' % (umbral, sum(1 for s, _, _ in medidos if s >= umbral)))
