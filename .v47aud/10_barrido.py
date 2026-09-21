# -*- coding: utf-8 -*-
"""BARRIDO DE VECINOS (D.38.4) de los 6 candidatos nacidos en esta vuelta,
sobre GRAFO + BANDEJAS con el filtro canonico de mi ACTA 45 45.5.a.
Usa la funcion de la casa src.aduana.senal_similitud_texto y el umbral de
config/umbrales.json, para que mi cifra y la de la aduana sean comparables (D.38.5).
PUBLICA LA LISTA ORDENADA ENTERA de los 8 primeros por candidato: mi remedio de
ACTA 45 45.9.b prohibe publicar un superlativo sin la lista que lo sostiene."""
import json, os, sys, io, glob
sys.path.insert(0, '.')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from src import aduana, comun

umbral = json.load(open('config/umbrales.json', encoding='utf-8'))['umbral_similitud_texto']
tabla = json.load(open('fuentes/FUENTES_CANONICAS.json', encoding='utf-8'))
canon = set(k for k in tabla if not k.startswith('_'))
NUEVOS = [l.strip() for l in open('.v47aud/02_candidatos_nuevos.out', encoding='utf-8') if l.strip()]
nuevos_ids = set(json.load(open(r, encoding='utf-8'))['id'] for r in NUEVOS)

pobl = []
for l in open('dataset/nodos.jsonl', encoding='utf-8'):
    if l.strip():
        c = json.loads(l); pobl.append(('grafo', c, comun.texto_comparable(c)))
for d in sorted(os.listdir('cuarentena')):
    p = os.path.join('cuarentena', d)
    if not os.path.isdir(p) or d in ('_insertados', '_derivadas'):
        continue
    for f in sorted(glob.glob(os.path.join(p, '*.json'))):
        c = json.load(open(f, encoding='utf-8'))
        claves = [x.get('clave') for x in (c.get('fuentes') or [])]
        if claves and all(k in canon for k in claves):
            pobl.append(('bandeja/' + d, c, comun.texto_comparable(c)))

print('umbral de la casa (config/umbrales.json): %s' % umbral)
print('poblacion barrida: %d (grafo + bandejas, filtro canonico)' % len(pobl))
for ruta in NUEVOS:
    cand = json.load(open(ruta, encoding='utf-8'))
    ta = comun.texto_comparable(cand)
    filas = []
    for sede, otro, tb in pobl:
        if otro.get('id') == cand['id']:
            continue
        filas.append((aduana.senal_similitud_texto(ta, tb), sede, otro.get('id')))
    filas.sort(reverse=True)
    print('\n' + '=' * 78)
    print('CANDIDATO: %s   (%d pasos)' % (cand['id'], len(cand.get('pasos_accionables', []))))
    print('  los 8 vecinos mas proximos, LISTA ORDENADA ENTERA:')
    for s, sede, oid in filas[:8]:
        marca = '  <-- nacido en esta vuelta' if oid in nuevos_ids else ''
        print('    %.4f  [%-24s] %s%s' % (s, sede, oid, marca))
    print('  por encima del umbral %s: %d' % (umbral, sum(1 for s, _, _ in filas if s >= umbral)))
