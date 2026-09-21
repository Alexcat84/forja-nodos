# -*- coding: utf-8 -*-
"""Cuantos de los 36 de la bandeja grove_high_output salen de cada unidad de
origen, leido del propio campo resumen_teorico (UNIDAD DE ORIGEN:)."""
import json, glob, re, sys, io, collections, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
cuenta = collections.Counter()
cap04 = []
for f in sorted(glob.glob('cuarentena/grove_high_output/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    m = re.search(r'UNIDAD DE ORIGEN:\s*fuentes/grove_high_output/(cap_\d+)', d.get('resumen_teorico',''))
    u = m.group(1) if m else '(no la dice)'
    cuenta[u] += 1
    if u == 'cap_04':
        cap04.append((os.path.getmtime(f), d['id']))
for u, n in sorted(cuenta.items()):
    print('%-14s %3d' % (u, n))
print('---')
print('total bandeja grove_high_output: %d' % sum(cuenta.values()))
print()
print('LOS DE cap_04, por orden de escritura en disco:')
for i, (t, i_) in enumerate(sorted(cap04), 1):
    print('  %2d. %s' % (i, i_))
