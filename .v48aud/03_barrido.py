# -*- coding: utf-8 -*-
"""BARRIDO DE VECINOS (D.38.4) de los candidatos de la vuelta 48.

LA CIFRA ES LA DE LA CASA: el valor que publico de cada vecino sale de
src.aduana.senal_similitud_texto, la misma funcion que corre la aduana, sobre
comun.texto_comparable. No reimplemento la senial y no la aproximo: MIDO LOS 389
VECINOS AL DIGITO, uno a uno. No hay cota, no hay muestra y no hay tope callado.

POBLACION: grafo + bandejas, con el filtro canonico de mi ACTA 45 45.5.a
(descartando _insertados y _derivadas), que es lo que D.38.4 manda barrer.

LISTA ORDENADA ENTERA de los 8 primeros por candidato: mi REMEDIO DE LA VUELTA 48
me prohibe publicar un superlativo sin la lista que lo sostiene.

Se corre UN CANDIDATO POR PROCESO (argumento en la linea de ordenes) solo para que
los cinco vayan a la vez: la cuenta de cada uno es identica a la del guion entero."""
from __future__ import print_function
import json, os, sys, glob
sys.path.insert(0, '.')
from src import aduana, comun

TOPE = 8
cual = int(sys.argv[1])
umbral = json.load(open('config/umbrales.json', encoding='utf-8'))['umbral_similitud_texto']
tabla = json.load(open('fuentes/FUENTES_CANONICAS.json', encoding='utf-8'))
canon = set(k for k in tabla if not k.startswith('_'))
NUEVOS = [l.strip() for l in open('.v48aud/02_candidatos_nuevos.out', encoding='utf-8') if l.strip()]
nuevos_ids = set(json.load(open(r, encoding='utf-8'))['id'] for r in NUEVOS)

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

cand = json.load(open(NUEVOS[cual], encoding='utf-8'))
ta = comun.texto_comparable(cand)
medidos = [(aduana.senal_similitud_texto(ta, tb), sede, oid)
           for sede, oid, tb in pobl if oid != cand['id']]
medidos.sort(reverse=True)
print('=' * 78)
print('CANDIDATO %d: %s   (%d pasos)' % (cual + 1, cand['id'], len(cand['pasos_accionables'])))
print('  poblacion barrida: %d nodos (grafo + bandejas, filtro canonico)' % len(pobl))
print('  medidos al digito con src.aduana.senal_similitud_texto: %d de %d; descartados: 0'
      % (len(medidos), len(medidos)))
print('  umbral de la casa (config/umbrales.json): %s' % umbral)
print('  LOS %d VECINOS MAS PROXIMOS, LISTA ORDENADA ENTERA:' % TOPE)
for s, sede, oid in medidos[:TOPE]:
    marca = '  <-- nacido en esta vuelta' if oid in nuevos_ids else ''
    print('    %.4f  [%-24s] %s%s' % (s, sede, oid, marca))
print('  vecinos por encima del umbral %s: %d' % (umbral, sum(1 for s, _, _ in medidos if s >= umbral)))
