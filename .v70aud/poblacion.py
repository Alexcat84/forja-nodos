# -*- coding: utf-8 -*-
"""Fase ciega de la 70 (copia de .v69aud/poblacion.py): la poblacion del barrido D.38.4 HOY (grafo mas bandejas), con las mismas funciones de
src/aduana.py que usa .v68aud/barrido_uno.py, repartida por sede con su suma (R7). Solo lee."""
import sys, collections
sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding="utf-8")
from src import aduana, comun
nodos = comun.leer_jsonl(comun.RUTA_DATASET)
bandejas = aduana.poblacion_de_bandejas(fecha=aduana._hoy())
ids_grafo = set(n['id'] for n in nodos)
por = collections.Counter('grafo' for n in nodos)
for b in bandejas:
    por['bandeja' if b['id'] not in ids_grafo else 'bandeja con id del grafo'] += 1
print('poblacion: %d | por sede: %s | suma: %d' % (len(nodos) + len(bandejas), dict(por), sum(por.values())))
