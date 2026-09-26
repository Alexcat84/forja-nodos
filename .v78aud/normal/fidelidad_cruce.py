# -*- coding: utf-8 -*-
"""ACTA 77: mi fidelidad sellada (.v78aud/fidelidad.tsv, fase ciega) contra la suya (.v78ext/fidelidad.tsv), paso a paso: marca y
linea. Mis marcas son sobre el texto de hoy de la ficha; las suyas sobre el texto al abrir la vuelta. Cuenta todas las clases con el
mismo predicado y dice su suma (R7). Solo lee."""
import io, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
mia, suya = {}, {}
for l in io.open('.v78aud/fidelidad.tsv', encoding='utf-8'):
    c = l.rstrip('\r\n').split('\t')
    if len(c) < 6 or c[0] == 'id': continue
    mia[(c[0], int(c[1]))] = (c[2], c[4])
for l in io.open('.v78ext/fidelidad.tsv', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    c = [x.strip() for x in l.rstrip('\r\n').split('|')]
    suya[(c[0], int(c[1]))] = (c[2], c[3], 'DISCUTIBLE' in l)
print('filas: mias %d | suyas %d | en las dos: %d | solo mias: %d | solo suyas: %d' % (len(mia), len(suya), len(set(mia) & set(suya)), len(set(mia) - set(suya)), len(set(suya) - set(mia))))
par = collections.Counter(); lin = collections.Counter(); dif = []
for k in sorted(set(mia) & set(suya)):
    m, s = mia[k], suya[k]
    par['mia %s / suya %s' % (m[0], s[0])] += 1
    lm = m[1].split(':')[-1]; ls = s[1].split(':')[-1]
    lin['misma linea' if lm == ls else 'linea distinta'] += 1
    if m[0] != s[0] or lm != ls or s[2]:
        dif.append('  %-55s paso %2d | mia %s %-5s | suya %s %-5s%s' % (k[0], k[1], m[0], lm, s[0], ls, ' | DISCUTIBLE suyo' if s[2] else ''))
print('marcas: %s | suma: %d' % (dict(sorted(par.items())), sum(par.values())))
print('lineas: %s | suma: %d' % (dict(sorted(lin.items())), sum(lin.values())))
print('filas con marca o linea distinta, o discutible suyo: %d' % len(dif))
print('\n'.join(dif))
