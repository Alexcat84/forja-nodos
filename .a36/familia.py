# -*- coding: utf-8 -*-
"""Senial 2 (familia_id) de la casa sobre los 14 del tramo contra GRAFO MAS
BANDEJAS. Es la unica de las tres que no cuesta nada, asi que la corro entera y
sin recortes: aduana.senal_familia_id, umbral de config/umbrales.json."""
import json, glob, io, os, sys
sys.path.insert(0, os.getcwd())
from src import aduana, comun
U = comun.leer_json('config/umbrales.json')['umbral_familia_id']
tabla = comun.leer_json(comun.RUTA_FUENTES)
nodos = [json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
band = aduana.poblacion_de_bandejas(tabla_fuentes=tabla)
print('POBLACION (D.38.4): %s' % aduana.Poblacion(len(nodos), len(band)))
print('umbral familia_id: %s' % U)
ids_grafo = set(n['id'] for n in nodos)
tramo = []
for f in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')
                + glob.glob('cuarentena/_insertados/scott_radical_candor/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    r = d.get('resumen_teorico', '')
    if 'cap_12.md' in r or 'cap_13.md' in r:
        tramo.append(d)
print('CANDIDATOS DEL TRAMO MEDIDOS: %d' % len(tramo))
print()
total = 0
for c in tramo:
    lev = []
    for v in nodos + band:
        if v['id'] == c['id']:
            continue
        s = aduana.senal_familia_id(c['id'], v['id'])
        if not isinstance(s, aduana.NoAplica) and s >= U:
            lev.append((v['id'], 'GRAFO' if v['id'] in ids_grafo else 'BANDEJA', s))
    total += len(lev)
    print('%-52s %d' % (c['id'], len(lev)))
    for i, d_, s in sorted(lev):
        print('    %-8s %-52s familia_id=%.3f' % (d_, i, s))
print()
print('TOTAL DE PARES LEVANTADOS POR familia_id EN EL TRAMO: %d' % total)
