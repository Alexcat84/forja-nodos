# -*- coding: utf-8 -*-
"""Saca de cada candidato del tramo (cap_12 y cap_13) el tramo de lineas que dice
ocupar y su titulo, para cruzarlos contra MI lectura de frontera hecha antes."""
import json, glob, os, re
pat_cap = re.compile(r'UNIDAD DE ORIGEN:\s*fuentes/scott_radical_candor/(cap_\d+)\.md')
pat_lin = re.compile(r'Sale de las?\s+lineas?\s+([^.]{0,90})')
filas = []
for f in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    r = d.get('resumen_teorico', '')
    m = pat_cap.search(r)
    cap = m.group(1) if m else 'SIN_RUTA'
    if cap not in ('cap_12', 'cap_13'):
        continue
    ml = pat_lin.search(r)
    filas.append((cap, d['id'], len(d['pasos_accionables']),
                  (ml.group(1).strip() if ml else 'SIN TRAMO DECLARADO')))
for cap, i, p, l in sorted(filas):
    print('%s %-52s %3d pasos | lineas %s' % (cap, i, p, l))
print('TOTAL DEL TRAMO: %d candidatos, %d pasos' % (len(filas), sum(f[2] for f in filas)))
