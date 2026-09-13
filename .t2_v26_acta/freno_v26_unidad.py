# -*- coding: utf-8 -*-
"""PASOS INVENTADOS POR CAPITULO (AUDITOR_FORJA.md 8) para un lote.

LA VERSION BUENA DEL INSTRUMENTO DE MI APERTURA, y esta escrita aparte a proposito:
`.t1_v26_auditor/freno_v26.py` atribuye la unidad al PRIMER cap_NN que aparezca en
cualquier parte del JSON, y eso le corre el rotulo a un candidato cuyo resumen_teorico
menciona otro capitulo. Aqui la unidad sale de `UNIDAD DE ORIGEN`, que es la misma
atribucion que usa `.t2_v24_acta/freno_auditor.py`.

NO SOBREESCRIBO EL MALO: es la prueba de la caida que declaro en ACTA 25 7.2.

    $ python .t2_v26_acta/freno_v26_unidad.py marquet_turn_the_ship
"""
import collections
import glob
import io
import json
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
lote = sys.argv[1]
rutas = sorted(glob.glob('cuarentena/%s/*.json' % lote) +
               glob.glob('cuarentena/_insertados/%s/*.json' % lote))
filas = collections.defaultdict(lambda: [0, 0, []])
for r in rutas:
    d = json.load(io.open(r, encoding='utf-8'))
    txt = json.dumps(d, ensure_ascii=False)
    m = (re.search(r'UNIDAD DE ORIGEN:\s*\S*?(cap_\d+)', txt) or
         re.search(r'(cap_\d+)\.md', txt) or
         re.search(r'(cap_\d+)', txt))
    u = m.group(1) if m else 'SIN_UNIDAD'
    filas[u][0] += 1
    filas[u][1] += len(d.get('pasos_accionables') or [])
    filas[u][2].append(d['id'])
tc = tp = 0
print('unidad      candidatos   pasos   ids')
for u in sorted(filas):
    c, p, ids = filas[u]
    tc += c
    tp += p
    print('%-10s %10d %7d   %s' % (u, c, p, ', '.join(sorted(ids))))
print('%-10s %10d %7d' % ('TOTAL', tc, tp))
print('ficheros leidos:', len(rutas))
