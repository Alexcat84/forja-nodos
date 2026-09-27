# -*- coding: utf-8 -*-
"""Fase ciega de la 78 (copia de .v76aud/armar_clases.py con las rutas cambiadas): arma
.v78aud/mis_clases.tsv, una fila por par sin orden que levanta mi barrido de las 20 (.v78aud/vecinos_<id>.json), con la clase
que YO escribi: de .v78aud/clases_intra.txt (pares dentro de un mismo capitulo, escritos antes de mirar el barrido) o de
.v78aud/clases_fuera.txt (pares entre capitulos de la tanda o con un extremo fuera, leidos al recogerlo). Solo escribe ese
fichero, y dice de donde sale cada fila, con su suma (R7). Cuenta tambien las filas de clases_intra.txt que el barrido NO
levanta, que no entran en mis_clases.tsv."""
import io, json, glob, collections
ab = {}; fuente = {}
for l in io.open('.v78aud/clases_intra.txt', encoding='utf-8'):
    if l.startswith('@'):
        k, v = l[1:].strip().split('='); ab[k] = v
    elif l.strip() and not l.startswith('#'):
        a, b, c, m, r = l.rstrip('\n').split('|', 4)
        fuente[tuple(sorted((ab[a], ab[b])))] = (ab[a], ab[b], c, ab.get(m, ''), r, 'intra')
intra = set(fuente)
for l in io.open('.v78aud/clases_fuera.txt', encoding='utf-8'):
    if l.strip() and not l.startswith('#'):
        a, b, c, m, r = l.rstrip('\n').split('|', 4)
        fuente[tuple(sorted((a, b)))] = (a, b, c, m, r, 'fuera')
pares = collections.OrderedDict()
for f in sorted(glob.glob('.v78aud/vecinos_*.json')):
    d = json.load(io.open(f, encoding='utf-8'))
    for v in d['vecinos']: pares.setdefault(tuple(sorted((d['id'], v['id']))), 1)
sin = [p for p in pares if p not in fuente]
with io.open('.v78aud/mis_clases.tsv', 'w', encoding='utf-8', newline='\n') as o:
    o.write('a\tb\tclase\tmadre\tlectura\n')
    for p in pares:
        if p in fuente: o.write('\t'.join(fuente[p][:5]) + '\n')
print('pares del barrido: %d | filas escritas: %d | sin clase: %d %s' % (len(pares), len(pares) - len(sin), len(sin), sin))
c = collections.Counter(fuente[p][5] for p in pares if p in fuente)
print('de donde sale cada fila: %s | suma: %d' % (dict(c), sum(c.values())))
n = collections.Counter('levantada' if p in pares else 'no levantada' for p in intra)
print('filas de clases_intra.txt: %d | por el barrido: %s | suma: %d' % (len(intra), dict(n), sum(n.values())))
