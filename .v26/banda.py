# -*- coding: utf-8 -*-
"""LA BANDA DE LA SENIAL 1 EN LOS PARES QUE ESTA VUELTA LEYO.

Cuenta, de los .v26/ins_*.txt que la aduana escribio hoy, cuantos pares levanto
cada senial y en que banda de similitud de texto cayeron. No mueve ningun umbral
(EXTRACTOR.md 11 lo prohibe expresamente): es una medicion para el reporte.
"""
import glob, io, re

pares = {}
for ruta in sorted(glob.glob('.v26/ins_*.txt')):
    texto = io.open(ruta, encoding='utf-8').read()
    cand = re.search(r"ADUANA DE INSERCION, candidato '([^']+)'", texto)
    if not cand:
        continue
    for bloque in re.findall(
            r'vecino (\S+).*?levantada por: ([^\n]+).*?similitud_texto\s+([\d.]+).*?'
            r'familia_id\s+([\d.]+).*?paso_contra_nodo\s+([\d.]+)', texto, re.S):
        vec, por, sim, fam, pcn = bloque
        pares[(cand.group(1), vec)] = (por.strip(), float(sim), float(fam), float(pcn))

bandas = [('0.35 a 0.40 (justo por encima)', 0.35, 0.40),
          ('0.40 en adelante (la ALTA de 11)', 0.40, 9.9),
          ('por debajo de 0.35 (no la levanta la 1)', 0.0, 0.35)]
print('pares distintos leidos en esta vuelta : %d' % len(pares))
print('')
print('QUE SENIAL LOS LEVANTA')
for clave in ('similitud_texto', 'familia_id', 'paso_contra_nodo'):
    n = sum(1 for v in pares.values() if clave in v[0])
    print('  %-18s : %d' % (clave, n))
print('')
print('EN QUE BANDA DE SIMILITUD DE TEXTO CAEN')
for nombre, bajo, alto in bandas:
    n = sum(1 for v in pares.values() if bajo <= v[1] < alto)
    print('  %-40s : %d' % (nombre, n))
print('')
print('LOS QUE PASAN DE 0.40, uno a uno')
altos = [(k, v) for k, v in pares.items() if v[1] >= 0.40]
if not altos:
    print('  ninguno')
for (c, v), val in sorted(altos):
    print('  %.3f  %s contra %s' % (val[1], c, v))
print('')
print('MAYOR SIMILITUD DE TEXTO DE LA VUELTA : %.3f' % max(v[1] for v in pares.values()))
