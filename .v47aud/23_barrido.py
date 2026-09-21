# -*- coding: utf-8 -*-
"""BARRIDO DE VECINOS (D.38.4), EXACTO, con cota y con descarga inmediata.

LA CIFRA ES LA DE LA CASA: el valor que publico de cada vecino sale de
src.aduana.senal_similitud_texto, la misma funcion que corre la aduana, sobre
comun.texto_comparable. No reimplemento la senial.

LA SENIAL ES max(ratio_de_caracteres, ratio_de_palabras). El ratio de palabras
es BARATO y es una COTA INFERIOR de la senial; quick_ratio de caracteres es una
COTA SUPERIOR del otro sumando. Con las dos, descarto vecinos que NO pueden
entrar en los 8 primeros y mido al digito los que si. Los descartados se cuentan
y se dicen: no hay tope silencioso (AUDITOR_FORJA.md, ningun recorte callado).

POBLACION: grafo + bandejas con el filtro canonico de mi ACTA 45 45.5.a.
LISTA ORDENADA ENTERA de los 8 primeros por candidato: mi remedio de la
ACTA 45 45.9.b prohibe publicar un superlativo sin la lista que lo sostiene."""
from __future__ import print_function
import json, os, sys, glob, difflib, functools
sys.path.insert(0, '.')
from src import aduana, comun

def say(*a):
    print(*a)
    sys.stdout.flush()

TOPE = 8
umbral = json.load(open('config/umbrales.json', encoding='utf-8'))['umbral_similitud_texto']
tabla = json.load(open('fuentes/FUENTES_CANONICAS.json', encoding='utf-8'))
canon = set(k for k in tabla if not k.startswith('_'))
NUEVOS = [l.strip() for l in open('.v47aud/02_candidatos_nuevos.out', encoding='utf-8') if l.strip()]
nuevos_ids = set(json.load(open(r, encoding='utf-8'))['id'] for r in NUEVOS)

pobl = []
for l in open('dataset/nodos.jsonl', encoding='utf-8'):
    if l.strip():
        c = json.loads(l); t = comun.texto_comparable(c)
        pobl.append(('grafo', c.get('id'), t, t.split()))
for d in sorted(os.listdir('cuarentena')):
    p = os.path.join('cuarentena', d)
    if not os.path.isdir(p) or d in ('_insertados', '_derivadas'):
        continue
    for f in sorted(glob.glob(os.path.join(p, '*.json'))):
        c = json.load(open(f, encoding='utf-8'))
        claves = [x.get('clave') for x in (c.get('fuentes') or [])]
        if claves and all(k in canon for k in claves):
            t = comun.texto_comparable(c)
            pobl.append(('bandeja/' + d, c.get('id'), t, t.split()))

say('umbral de la casa (config/umbrales.json): %s' % umbral)
say('poblacion barrida: %d nodos (grafo + bandejas, filtro canonico)' % len(pobl))
say('senial publicada: src.aduana.senal_similitud_texto, la de la aduana')
for ruta in NUEVOS:
    cand = json.load(open(ruta, encoding='utf-8'))
    ta = comun.texto_comparable(cand); pa = ta.split()
    filas = []
    for sede, oid, tb, pb in pobl:
        if oid == cand['id']:
            continue
        inf = difflib.SequenceMatcher(None, pa, pb, autojunk=False).ratio()   # cota INFERIOR exacta
        sup = difflib.SequenceMatcher(None, ta, tb, autojunk=False).quick_ratio()  # cota SUPERIOR
        filas.append((max(inf, sup), inf, sede, oid, tb))
    filas.sort(reverse=True, key=lambda x: x[0])
    exactos, medidos, podados = [], 0, 0
    umbral_vivo = sorted((f[1] for f in filas), reverse=True)[TOPE-1] if len(filas) >= TOPE else -1
    for sup, inf, sede, oid, tb in filas:
        peor = sorted((e[0] for e in exactos), reverse=True)[TOPE-1] if len(exactos) >= TOPE else umbral_vivo
        if sup < peor:
            podados += 1
            continue
        exactos.append((aduana.senal_similitud_texto(ta, tb), sede, oid))
        medidos += 1
    exactos.sort(reverse=True)
    say('')
    say('=' * 78)
    say('CANDIDATO: %s   (%d pasos)' % (cand['id'], len(cand.get('pasos_accionables', []))))
    say('  medidos al digito con la funcion de la casa: %d de %d; descartados por cota: %d'
        % (medidos, len(filas), podados))
    say('  LOS %d VECINOS MAS PROXIMOS, LISTA ORDENADA ENTERA:' % TOPE)
    for s, sede, oid in exactos[:TOPE]:
        marca = '  <-- nacido en esta vuelta' if oid in nuevos_ids else ''
        say('    %.4f  [%-24s] %s%s' % (s, sede, oid, marca))
    say('  por encima del umbral %s, entre los medidos: %d'
        % (umbral, sum(1 for s, _, _ in exactos if s >= umbral)))
