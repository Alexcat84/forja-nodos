# -*- coding: utf-8 -*-
"""RECUENTO PROPIO DE LOS PARES QUE LA ADUANA LEVANTO EN LA VUELTA 23.

El auditor me corrige la cifra `14 pares` y dice `21 pares distintos, 28 filas,
7 levantados por los dos lados`. EXTRACTOR.md 5: una cifra de un acta ajena no es
fuente de una cifra mia. La recuento de los 20 informes crudos.
"""
import glob
import io
import os
import re

CAND = re.compile(r'^\[BLOQUEARIA\] (\S+)')
VEC = re.compile(r'^    vecino (\S+)')

filas = []
for ruta in sorted(glob.glob('.aduana_v23/*.txt')):
    cand = None
    for linea in io.open(ruta, encoding='utf-8'):
        m = CAND.match(linea.rstrip('\n'))
        if m:
            cand = m.group(1)
            continue
        m = VEC.match(linea.rstrip('\n'))
        if m and cand:
            filas.append((cand, m.group(1)))

pares = set(tuple(sorted(f)) for f in filas)
espejo = set(p for p in pares if (p[0], p[1]) in [tuple(x) for x in filas] and (p[1], p[0]) in [tuple(x) for x in filas])

# LA TABLA SE IMPRIME, NO SE TECLEA (EXTRACTOR.md 5 y D.41): el instrumento
# saca la tabla en markdown y el reporte la pega entera desde este fichero.
print('| medida | valor |')
print('|---|---:|')
print('| informes crudos leidos | **%d** |' % len(glob.glob('.aduana_v23/*.txt')))
print('| filas vecino (candidato, vecino) | **%d** |' % len(filas))
print('| pares DISTINTOS sin orden | **%d** |' % len(pares))
print('| pares levantados por los DOS lados | **%d** |' % len(espejo))
