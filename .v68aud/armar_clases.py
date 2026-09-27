# -*- coding: utf-8 -*-
"""Fase ciega de la 68: arma .v68aud/mis_clases.tsv, una fila por par sin orden que levanta mi barrido de los 22
(.v68aud/vecinos_<id>.json), con la clase que YO escribi: de .v68aud/clases_intra.txt (pares dentro de cap_05 o de
cap_06, escritos antes de ver el barrido), de .v68aud/clases_fuera.txt (pares con un extremo fuera, leidos al recoger
el barrido), o de mi .v66aud/mis_clases.tsv sellada (las filas 21 y 22 de cap_04, sin tocarla). Solo escribe ese
fichero, y dice de donde sale cada fila."""
import io, json, glob, collections
ab = {}; fuente = {}
for l in io.open('.v68aud/clases_intra.txt', encoding='utf-8'):
    if l.startswith('@'):
        k, v = l[1:].strip().split('='); ab[k] = v
    elif l.strip() and not l.startswith('#'):
        a, b, c, m, r = l.rstrip('\n').split('|', 4)
        fuente[tuple(sorted((ab[a], ab[b])))] = (ab[a], ab[b], c, ab.get(m, ''), r, 'intra')
for l in io.open('.v68aud/clases_fuera.txt', encoding='utf-8'):
    if l.strip() and not l.startswith('#'):
        a, b, c, m, r = l.rstrip('\n').split('|', 4)
        fuente[tuple(sorted((a, b)))] = (a, b, c, m, r, 'fuera')
for l in list(io.open('.v66aud/mis_clases.tsv', encoding='utf-8'))[1:]:
    a, b, c, m, r = l.rstrip('\n').split('\t', 4)
    k = tuple(sorted((a, b)))
    if k not in fuente: fuente[k] = (a, b, c, m, r + ' (sellada en la 66)', 'la 66')
pares = collections.OrderedDict()
for f in sorted(glob.glob('.v68aud/vecinos_*.json')):
    d = json.load(io.open(f, encoding='utf-8'))
    for v in d['vecinos']: pares.setdefault(tuple(sorted((d['id'], v['id']))), 1)
sin = [p for p in pares if p not in fuente]
with io.open('.v68aud/mis_clases.tsv', 'w', encoding='utf-8', newline='\n') as o:
    o.write('a\tb\tclase\tmadre\tlectura\n')
    for p in pares:
        if p in fuente: o.write('\t'.join(fuente[p][:5]) + '\n')
print('pares del barrido: %d | filas escritas: %d | sin clase: %d %s' % (len(pares), len(pares) - len(sin), len(sin), sin))
print('de donde sale cada fila: %s' % dict(collections.Counter(fuente[p][5] for p in pares if p in fuente)))
