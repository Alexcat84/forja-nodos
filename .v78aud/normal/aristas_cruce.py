# -*- coding: utf-8 -*-
"""ACTA 77: mis aristas por lectura selladas (.v78aud/aristas_lectura.tsv) contra las suyas (.v78ext/aristas_lectura.txt), par a par
y con direccion. Cuenta todas las clases con el mismo predicado y dice su suma (R7). Solo lee."""
import io, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
mia = {}
for l in io.open('.v78aud/aristas_lectura.tsv', encoding='utf-8'):
    p = l.rstrip('\r\n').split('\t')
    if len(p) < 3 or p[0] == 'madre': continue
    mia[(p[0], p[1])] = 'SOSTENGO' if p[2].startswith('SOSTENGO') else 'DESCARTO'
suya = {}
for l in io.open('.v78ext/aristas_lectura.txt', encoding='utf-8'):
    if l.startswith('#') or '|' not in l: continue
    p = [x.strip() for x in l.split('|')]
    suya[(p[1], p[2])] = 'SOSTENGO' if p[0] == 'SOSTENGO' else 'DESCARTO'
print('filas: mias %d %s | suyas %d %s' % (len(mia), dict(collections.Counter(mia.values())), len(suya), dict(collections.Counter(suya.values()))))
c = collections.Counter()
for k in sorted(set(mia) | set(suya)):
    e = 'en las dos, %s y %s' % (mia[k], suya[k]) if k in mia and k in suya else ('solo mia, %s' % mia[k] if k in mia else 'solo suya, %s' % suya[k])
    c[e] += 1
    if k in mia: print('  %-52s > %-52s | %s' % (k[0], k[1], e))
print('pares: %s | suma: %d' % (dict(c), sum(c.values())))
print('SOSTENGO mias: %s' % sorted(k for k, v in mia.items() if v == 'SOSTENGO'))
print('SOSTENGO suyas: %s' % sorted(k for k, v in suya.items() if v == 'SOSTENGO'))
