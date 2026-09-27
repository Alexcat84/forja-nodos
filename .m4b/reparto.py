# -*- coding: utf-8 -*-
"""Reparto de clases de la frontera de cap_06 (vuelta 2), contado por el auditor."""
import re, collections
ls = open('docs/loop/REPORTE.md', encoding='utf-8').read().splitlines()
filas = []
for ln in ls[57712-1:57834]:
    s = ln.strip()
    if not s.startswith('|'):
        continue
    c = [x.strip().replace('*', '').replace('`', '') for x in s.strip('|').split('|')]
    if len(c) < 5 or not re.fullmatch(r'[RP]\d+', c[0]):
        continue
    filas.append((c[0], c[-1]))
R = [f for f in filas if f[0].startswith('R')]
print('filas de la frontera de cap_06: %d   (%d filas R, %d filas P)' % (len(filas), len(R), len(filas) - len(R)))
fam = collections.Counter()
for p, cl in R:
    fam[cl.split(':')[0].split('/')[0].split(',')[0].strip()] += 1
print('solo filas R:')
for k, v in fam.most_common():
    print('  %-28s %3d' % (k, v))
