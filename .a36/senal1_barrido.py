# -*- coding: utf-8 -*-
"""Senial 1 (similitud_texto) de la casa, entera, sobre los 14 del tramo contra
GRAFO MAS BANDEJAS. Usa aduana.senal_similitud_texto sobre comun.texto_comparable,
que es exactamente lo que corre la aduana. Y al lado, la MISMA funcion sobre solo
titulo+pasos, para repartir cuanto del valor viene del resumen_teorico."""
import json, glob, io, os, sys
sys.path.insert(0, os.getcwd())
from src import aduana, comun
U = comun.leer_json('config/umbrales.json')['umbral_similitud_texto']
tabla = comun.leer_json(comun.RUTA_FUENTES)
nodos = [json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
band = aduana.poblacion_de_bandejas(tabla_fuentes=tabla)
print('POBLACION (D.38.4): %s' % aduana.Poblacion(len(nodos), len(band)))
print('umbral similitud_texto: %s' % U)
ids_grafo = set(n['id'] for n in nodos)
FUERA = ('repartir_semana_cuarenta_horas_jefe',)
tramo = []
for f in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')
                + glob.glob('cuarentena/_insertados/scott_radical_candor/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    r = d.get('resumen_teorico', '')
    if ('cap_12.md' in r or 'cap_13.md' in r) and d['id'] not in FUERA:
        tramo.append(d)
print('CANDIDATOS DEL TRAMO MEDIDOS: %d' % len(tramo))
print()

def solo(n):
    return comun.normalizar_texto(' '.join([n.get('titulo') or ''] + list(n.get('pasos_accionables') or [])))

pob = nodos + band
cache = {}
total = solo_resumen = 0
for c in tramo:
    tc, sc = comun.texto_comparable(c), solo(c)
    lev = []
    for v in pob:
        if v['id'] == c['id']:
            continue
        if v['id'] not in cache:
            cache[v['id']] = (comun.texto_comparable(v), solo(v))
        tv, sv = cache[v['id']]
        s = aduana.senal_similitud_texto(tc, tv)
        if not isinstance(s, aduana.NoAplica) and s >= U:
            p = aduana.senal_similitud_texto(sc, sv)
            lev.append((v['id'], 'GRAFO' if v['id'] in ids_grafo else 'BANDEJA', s, p))
    total += len(lev)
    solo_resumen += sum(1 for x in lev if x[3] < U)
    print('%-52s %d' % (c['id'], len(lev)))
    for i, d_, s, p in sorted(lev):
        marca = '  <-- cruza SOLO por el resumen_teorico' if p < U else ''
        print('    %-8s %-52s casa=%.3f  solo_pasos=%.3f%s' % (d_, i, s, p, marca))
    sys.stdout.flush()
print()
print('TOTAL DE PARES LEVANTADOS POR similitud_texto: %d' % total)
print('DE ELLOS, CRUZAN SOLO POR EL resumen_teorico: %d' % solo_resumen)
