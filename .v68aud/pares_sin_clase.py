# -*- coding: utf-8 -*-
"""Fase ciega de la 68: de los pares que levanta mi barrido hasta ahora (.v68aud/vecinos_<id>.json), cuales NO tienen ya
una clase escrita, ni en mis pares de dentro de cada capitulo (.v68aud/clases_intra.txt, escritos antes de ver el
barrido) ni en mi .v66aud/mis_clases.tsv sellada (las filas 21 y 22). Son los que me quedan por leer. Solo lee."""
import io, json, glob, os
ab = {}; hechos = set()
for l in io.open('.v68aud/clases_intra.txt', encoding='utf-8'):
    if l.startswith('@'):
        k, v = l[1:].strip().split('='); ab[k] = v
    elif l.strip() and not l.startswith('#'):
        c = l.split('|'); hechos.add(tuple(sorted((ab[c[0]], ab[c[1]]))))
for l in io.open('.v66aud/mis_clases.tsv', encoding='utf-8'):
    c = l.split('\t'); hechos.add(tuple(sorted(c[:2])))
pares = {}
for f in sorted(glob.glob('.v68aud/vecinos_*.json')):
    d = json.load(io.open(f, encoding='utf-8'))
    for v in d['vecinos']:
        pares.setdefault(tuple(sorted((d['id'], v['id']))), []).append((d['id'], v['sede'], '+'.join(v['levantada_por'])))
falta = sorted(p for p in pares if p not in hechos)
print('fichas barridas: %d | pares levantados: %d | con clase ya escrita: %d | sin clase: %d' % (
    len(glob.glob('.v68aud/vecinos_*.json')), len(pares), len(pares) - len(falta), len(falta)))
for p in falta: print('  %s ~ %s | %s' % (p[0], p[1], pares[p]))
