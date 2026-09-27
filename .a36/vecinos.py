# -*- coding: utf-8 -*-
"""D.38.4 y D.38.5: BARRIDO DE VECINOS SOBRE GRAFO MAS BANDEJAS.

No es instrumento nuevo: llama a las mismas funciones de src/aduana.py que
corre la aduana (poblacion_de_bandejas, buscar_vecinos, medir) con los mismos
config/umbrales.json. Lo unico que hace de mas es correrlas sobre los 14
candidatos del tramo de una vez y pegar la cola de lectura de cada uno.
"""
import json, glob, os, sys, io
sys.path.insert(0, os.getcwd())
from src import aduana, comun, config as modulo_config

umbrales = modulo_config.cargar()
tabla = comun.leer_json(comun.RUTA_FUENTES)
nodos = [json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
bandejas = aduana.poblacion_de_bandejas(tabla_fuentes=tabla)
pob = aduana.Poblacion(grafo=len(nodos), bandejas=len(bandejas))
print('POBLACION DEL BARRIDO (D.38.4): %s' % pob)

ids_tramo = []
for f in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    if 'cap_12.md' in d.get('resumen_teorico','') or 'cap_13.md' in d.get('resumen_teorico',''):
        ids_tramo.append(f)
print('CANDIDATOS DEL TRAMO: %d' % len(ids_tramo))
print()

poblacion = nodos + bandejas
total_vecinos = 0
for f in ids_tramo:
    bruto = json.load(open(f, encoding='utf-8'))
    cand, _ = aduana.normalizar_candidato(bruto)
    vecinos = aduana.buscar_vecinos(cand, poblacion, umbrales)
    total_vecinos += len(vecinos)
    print('%s  ->  %d vecino(s) por encima de umbral' % (cand['id'], len(vecinos)))
    for v in vecinos:
        senales = ', '.join('%s=%s' % (k, w) for k, w in sorted(v['senales'].items())
                            if k in v['levantada_por'])
        donde = 'GRAFO' if any(n.get('id') == v['id'] for n in nodos) else 'BANDEJA'
        print('    %-8s %-52s %s' % (donde, v['id'], senales))
    sys.stdout.flush()
print()
print('TOTAL DE PARES LEVANTADOS EN EL TRAMO: %d' % total_vecinos)
