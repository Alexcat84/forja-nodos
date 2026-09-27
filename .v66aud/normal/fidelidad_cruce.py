# -*- coding: utf-8 -*-
"""ACTA 65: mi fidelidad sellada de cap_04 (.v66aud/fidelidad.tsv, tabuladores, T/P/D) contra la del
extractor (.v66ext/fidelidad.tsv, barras, T/P), paso a paso: marca y linea del libro."""
import io
mia, suya = {}, {}
for l in io.open('.v66aud/fidelidad.tsv', encoding='utf-8'):
    c = l.rstrip('\n').split('\t')
    if len(c) < 4 or c[0] == 'id' or l.startswith('#'): continue
    mia[(c[0], int(c[1]))] = (c[2], c[3], c[4] if len(c) > 4 else '')
for l in io.open('.v66ext/fidelidad.tsv', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    c = [x.strip() for x in l.rstrip('\n').split(' | ')]
    suya[(c[0], int(c[1]))] = (c[2], c[3], c[4] if len(c) > 4 else '')
print('filas mias: %d | suyas: %d | solo mias: %d | solo suyas: %d' % (len(mia), len(suya), len(set(mia) - set(suya)), len(set(suya) - set(mia))))
from collections import Counter
print('marcas mias:', dict(Counter(v[0] for v in mia.values())), '| suyas:', dict(Counter(v[0] for v in suya.values())))
dm = [k for k in sorted(mia) if k in suya and mia[k][0] != suya[k][0]]
dl = [k for k in sorted(mia) if k in suya and mia[k][1] != suya[k][1]]
print('marca distinta: %d' % len(dm))
for k in dm: print('  %-52s paso %2d  mia %s %s | suya %s %s' % (k[0], k[1], mia[k][0], mia[k][1], suya[k][0], suya[k][1]))
print('linea distinta: %d' % len(dl))
for k in dl: print('  %-52s paso %2d  mia %s | suya %s' % (k[0], k[1], mia[k][1], suya[k][1]))
dis = [k for k in sorted(suya) if 'DISCUTIBLE' in suya[k][2]]
print('pasos que el extractor marca DISCUTIBLE: %d' % len(dis))
for k in dis: print('  %-52s paso %2d  suya %s | mia %s' % (k[0], k[1], suya[k][0], mia.get(k, ('?',))[0]))
