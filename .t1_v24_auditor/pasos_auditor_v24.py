# -*- coding: utf-8 -*-
"""Cuenta MIA de los pasos de los 15 candidatos de cap_14, leida del fichero
de cada candidato y no de ninguna tabla. AUDITOR_FORJA.md 8.3 punto 1."""
import io, json, glob, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
filas = []
for f in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')):
    bruto = io.open(f, encoding='utf-8').read()
    if 'cap_14' not in bruto:
        continue
    d = json.loads(bruto)
    filas.append((d['id'], len(d['pasos_accionables'])))
print('%-56s %6s' % ('candidato de cap_14', 'pasos'))
for i, n in filas:
    print('%-56s %6d' % (i, n))
print()
print('candidatos : %d' % len(filas))
print('pasos      : %d' % sum(n for _, n in filas))
print('menor %d | mediana %d | mayor %d' % (
    min(n for _, n in filas),
    sorted(n for _, n in filas)[len(filas)//2],
    max(n for _, n in filas)))
