# -*- coding: utf-8 -*-
"""Los 7 candidatos de cap_02 de grove_high_output, ordenados por su pieza del libro (d024)."""
import json, glob, re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
filas = []
for f in sorted(glob.glob('cuarentena/grove_high_output/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    t = d.get('resumen_teorico') or ''
    if 'cap_02.md' not in t:
        continue
    m = re.search(r'PIEZA (P(\d+))', t)
    filas.append((int(m.group(2)), m.group(1), d['id']))
print('LOS 7 DE cap_02, EN EL ORDEN DEL LIBRO:')
for i, (n, p, nid) in enumerate(sorted(filas), 1):
    print('  %d  %-4s  %s' % (i, p, nid))
print()
print('total: %d' % len(filas))
