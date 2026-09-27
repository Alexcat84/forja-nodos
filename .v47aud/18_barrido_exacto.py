# -*- coding: utf-8 -*-
"""BARRIDO DE VECINOS (D.38.4), EXACTO Y RAPIDO.

LA CIFRA ES LA DE LA CASA: llamo a src.aduana.senal_similitud_texto, la misma
funcion que corre la aduana, sobre el mismo texto_comparable. No reimplemento
la senial.

LO UNICO QUE ANADO ES UNA PODA QUE NO CAMBIA NINGUN NUMERO: difflib garantiza
real_quick_ratio() >= quick_ratio() >= ratio(), asi que una cota superior barata
permite descartar vecinos que NO pueden entrar en los 8 primeros. Todo vecino
que entra se mide con la funcion de la casa, al digito. Los podados se cuentan
y se dicen: no hay tope silencioso.

POBLACION: grafo + bandejas con el filtro canonico de mi ACTA 45 45.5.a.
PUBLICA LA LISTA ORDENADA ENTERA de los 8 primeros: mi remedio de ACTA 45 45.9.b
prohibe publicar un superlativo sin la lista que lo sostiene."""
import json, os, sys, io, glob, difflib
sys.path.insert(0, '.')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', write_through=True)
from src import aduana, comun

TOPE = 8
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

def cota(ta, tb):
    """Cota SUPERIOR de senal_similitud_texto, que es max(ratio_char, ratio_palabra)."""
    m = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    c1 = min(m.real_quick_ratio(), m.quick_ratio())
    pa, pb = ta.split(), tb.split()
    m2 = difflib.SequenceMatcher(None, pa, pb, autojunk=False)
    c2 = min(m2.real_quick_ratio(), m2.quick_ratio())
    return max(c1, c2)

print('umbral de la casa (config/umbrales.json): %s' % umbral)
print('poblacion barrida: %d nodos (grafo + bandejas, filtro canonico)' % len(pobl))
print('senial: src.aduana.senal_similitud_texto, la de la aduana')
for ruta in NUEVOS:
    cand = json.load(open(ruta, encoding='utf-8'))
    ta = comun.texto_comparable(cand)
    cands = [(cota(ta, tb), sede, o.get('id'), tb)
             for sede, o, tb in pobl if o.get('id') != cand['id']]
    cands.sort(reverse=True, key=lambda x: x[0])
    exactos, medidos, podados = [], 0, 0
    for cot, sede, oid, tb in cands:
        peor = sorted((e[0] for e in exactos), reverse=True)[TOPE-1] if len(exactos) >= TOPE else -1
        if cot <= peor:
            podados += 1
            continue
        exactos.append((aduana.senal_similitud_texto(ta, tb), sede, oid))
        medidos += 1
    exactos.sort(reverse=True)
    print('\n' + '=' * 78)
    print('CANDIDATO: %s   (%d pasos)' % (cand['id'], len(cand.get('pasos_accionables', []))))
    print('  medidos al digito con la funcion de la casa: %d de %d; podados por cota: %d'
          % (medidos, len(cands), podados))
    print('  LOS %d VECINOS MAS PROXIMOS, LISTA ORDENADA ENTERA:' % TOPE)
    for s, sede, oid in exactos[:TOPE]:
        marca = '  <-- nacido en esta vuelta' if oid in nuevos_ids else ''
        print('    %.4f  [%-24s] %s%s' % (s, sede, oid, marca))
    print('  por encima del umbral %s, entre los medidos: %d'
          % (umbral, sum(1 for s, _, _ in exactos if s >= umbral)))
