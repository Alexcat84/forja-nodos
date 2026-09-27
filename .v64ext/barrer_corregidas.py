# -*- coding: utf-8 -*-
"""Vuelta 64, TAREA 2.c, lo que el par a par no puede ver: una correccion puede hacer
aparecer un vecino que ningun informe listaba (el par a par ya encontro uno). Barre cada
ficha corregida contra la poblacion de la aduana (grafo mas bandejas) con
aduana.buscar_vecinos, la misma funcion del informe, SIN veredicto, sin escribir nada y
sin el resto del informe. Imprime el tiempo."""
import os, sys, time
sys.path.insert(0, os.getcwd())
from src import aduana, comun
from src import config as modulo_config
t0 = time.time()
umbrales = modulo_config.cargar()
grafo = comun.leer_jsonl(comun.RUTA_DATASET)
bandejas = aduana.poblacion_de_bandejas()
pob = list(grafo) + list(bandejas)
en_grafo = set(n['id'] for n in grafo)
print('poblacion: grafo %d + bandejas %d = %d, cargada en %.0f s' % (len(grafo), len(bandejas), len(pob), time.time() - t0))
for i in sys.argv[1:]:
    t1 = time.time()
    cand, _ = aduana.normalizar_candidato(comun.leer_json('cuarentena/grove_high_output/%s.json' % i))
    vs = aduana.buscar_vecinos(cand, pob, umbrales)
    print('%s  vecinos %d  (%.0f s)' % (i, len(vs), time.time() - t1))
    for v in vs:
        s = v['senales']
        print('    %-50s %-7s %-28s texto %s familia %s paso %s' % (v['id'], 'grafo' if v['id'] in en_grafo else 'bandeja',
              ', '.join(v['levantada_por']), s['similitud_texto'], s['familia_id'], s['paso_contra_nodo']))
print('total %.0f s' % (time.time() - t0))
