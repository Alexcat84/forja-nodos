# -*- coding: utf-8 -*-
"""EL SALDO DE LA TANDA DE INSERCION, CONTADO DE LOS FICHEROS AL CERRAR.

Todo sale de contar ficheros y lineas, nada de la memoria de la vuelta.
"""
import glob
import io
import json
import os
import re

BANDEJA = 'cuarentena/scott_radical_candor'
ARCHIVO = 'cuarentena/_insertados/scott_radical_candor'

orden = [l.split()[1] for l in io.open('.v24/orden_insercion.txt', encoding='utf-8')
         if l.strip()]
insertados = sorted(os.path.basename(p)[:-5] for p in glob.glob(ARCHIVO + '/*.json'))
en_bandeja = sorted(os.path.basename(p)[:-5] for p in glob.glob(BANDEJA + '/*.json'))

# Los que se intentaron y bloquearon: tienen salida en .insercion_v24 y siguen en bandeja.
intentados = sorted(os.path.basename(p)[:-4] for p in glob.glob('.insercion_v24/*.txt'))
bloqueados = [i for i in intentados if i in en_bandeja]
sin_intentar = [i for i in orden if i not in intentados]

pares = 0
for i in bloqueados:
    texto = io.open('.insercion_v24/%s.txt' % i, encoding='utf-8').read()
    pares += len(re.findall(r'^  vecino ', texto, re.M))

print('| medida | valor |')
print('|---|---:|')
print('| candidatos del lote 4 al cerrar la extraccion | **%d** |' % len(orden))
print('| INSERTADOS en esta vuelta y archivados en `_insertados` | **%d** |' % len(insertados))
print('| intentados que la aduana BLOQUEO, en cola de lectura | **%d** |' % len(bloqueados))
print('| pares que esos bloqueos abren, por leer | **%d** |' % pares)
print('| todavia sin intentar, en cuarentena | **%d** |' % len(sin_intentar))
print('| nodos en el grafo | **%d** |' % len(io.open('dataset/nodos.jsonl', encoding='utf-8').read().strip().split('\n')))
print('| veredictos en `bitacora/VEREDICTOS.jsonl` | **%d** |'
      % len(io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8').read().strip().split('\n')))
print('| ficheros en `cuarentena/_insertados/` (todos los lotes) | **%d** |'
      % len(glob.glob('cuarentena/_insertados/*/*.json')))
