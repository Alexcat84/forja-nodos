# -*- coding: utf-8 -*-
"""ACTA 73: cruza mi fidelidad sellada (.v74aud/fidelidad.tsv, fase ciega) con la del extractor (.v74ext/fidelidad.tsv),
paso a paso: marca y linea del libro. Imprime el reparto de pares (mia, suya) con su suma (R7) y las filas que difieren."""
import io, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
mia = {}
for l in list(io.open('.v74aud/fidelidad.tsv', encoding='utf-8'))[1:]:
    i, p, c, L, t = l.rstrip('\n').split('\t', 4)
    mia[(i, int(p))] = (c, L)
suya = {}
for l in io.open('.v74ext/fidelidad.tsv', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    i, p, c, L, t = [x.strip() for x in l.rstrip('\n').split('|', 4)]
    suya[(i, int(p))] = (c, L, 'DISCUTIBLE' in t)
print('filas mias: %d | suyas: %d | solo mias: %d | solo suyas: %d' % (len(mia), len(suya), len(set(mia) - set(suya)), len(set(suya) - set(mia))))
pares = collections.Counter((mia[k][0], suya[k][0]) for k in mia if k in suya)
print('pares (mia, suya): %s | suma: %d' % (dict(sorted(pares.items())), sum(pares.values())))
print('filas con linea del libro distinta: %d' % sum(1 for k in mia if k in suya and mia[k][1] != suya[k][1]))
print('filas suyas marcadas DISCUTIBLE: %d' % sum(1 for k in suya if suya[k][2]))
for k in sorted(mia):
    if k in suya and (mia[k][0] != suya[k][0] or mia[k][1] != suya[k][1] or mia[k][0] == 'D' or suya[k][2]):
        print('  %-52s paso %2d | mia %s %s | suya %s %s%s' % (k[0], k[1], mia[k][0], mia[k][1], suya[k][0], suya[k][1], ' DISCUTIBLE' if suya[k][2] else ''))
