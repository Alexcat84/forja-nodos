# -*- coding: utf-8 -*-
"""LO QUE QUEDA EN LA BANDEJA DEL LOTE 4, CONTADO POR UNIDAD Y AL CERRAR.

Recuenta la bandeja de verdad, no el fichero de orden que se escribio al abrir:
la bandeja se ha movido dentro de esta misma vuelta y una cifra de cola envejece
dentro de su propia vuelta (leccion de la vuelta 25).
"""
import glob, io, json, os, re
CITA = re.compile(r'cap_(\d+)')
por_cap = {}
for ruta in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')):
    d = json.load(io.open(ruta, encoding='utf-8'))
    m = CITA.findall(d.get('resumen_teorico', ''))
    cap = 'cap_%s' % m[0] if m else 'cap_99'
    por_cap[cap] = por_cap.get(cap, 0) + 1
total = 0
for cap in sorted(por_cap):
    print('  %s : %d' % (cap, por_cap[cap]))
    total += por_cap[cap]
print('  TOTAL en la bandeja del lote 4 : %d' % total)
print('  insertados del lote 4          : %d'
      % len(glob.glob('cuarentena/_insertados/scott_radical_candor/*.json')))
