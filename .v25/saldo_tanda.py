# -*- coding: utf-8 -*-
"""EL SALDO DE LA TANDA DE INSERCION, CONTADO DE LOS FICHEROS Y DE LAS SALIDAS."""
import glob, io, json, os, re

BANDEJA = 'cuarentena/scott_radical_candor'
INSERT = 'cuarentena/_insertados/scott_radical_candor'

grafo = sum(1 for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip())
bandeja = len(glob.glob(BANDEJA + '/*.json'))
insertados = len(glob.glob(INSERT + '/*.json'))
bit = sum(1 for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip())
ver = json.load(io.open('.v25/veredictos_insercion.json', encoding='utf-8'))
v24 = json.load(io.open('.v24/veredictos_insercion.json', encoding='utf-8'))

segundos, ok, cola = [], [], []
for n in (1, 2, 3, 4, 5):
    ruta = '.v25/tanda_%d.txt' % n
    if not os.path.exists(ruta):
        continue
    for l in io.open(ruta, encoding='utf-8'):
        m = re.match(r'^(OK|COLA)\s+\S+\s+(\S+).*?([\d.]+)s', l)
        if m:
            segundos.append(float(m.group(3)))
            (ok if m.group(1) == 'OK' else cola).append(m.group(2))

print('| medida | al abrir | ahora |')
print('|---|---:|---:|')
print('| nodos en el grafo | 214 | **%d** |' % grafo)
print('| candidatos en la bandeja del lote 4 | 131 | **%d** |' % bandeja)
print('| insertados del lote 4 | 11 | **%d** |' % insertados)
print('| veredictos en `bitacora/VEREDICTOS.jsonl` | 156 | **%d** |' % bit)
print('')
print('intentos de insercion en la vuelta       : %d' % len(segundos))
print('  de ellos, NODO INSERTADO               : %d' % len(ok))
print('  de ellos, quedaron en cola de lectura  : %d' % len(cola))
print('candidatos distintos insertados          : %d' % len(set(ok)))
print('veredictos que escribi yo en esta vuelta : %d' % len(ver))
print('veredictos heredados de la vuelta 24     : %d' % len(v24))
if segundos:
    print('segundos por intento: minimo %.1f  maximo %.1f  media %.1f  total %.0f (%.1f min)'
          % (min(segundos), max(segundos), sum(segundos) / len(segundos),
             sum(segundos), sum(segundos) / 60.0))
