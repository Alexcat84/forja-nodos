# -*- coding: utf-8 -*-
"""ACTA 72: mi fidelidad sellada (.v73aud/fidelidad.tsv, tabuladores, leida sobre el texto de HOY de las fichas) contra la del
extractor (.v73ext/fidelidad.tsv, barras, que marca P los seis pasos que corrigio, leidos sobre su texto VIEJO), fila a fila
por (id, paso). Imprime el reparto de los pares de marcas con su suma, y cada fila que difiere con su linea en las dos. Solo lee."""
import io, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
def leer(ruta):
    d = collections.OrderedDict()
    for l in io.open(ruta, encoding='utf-8'):
        if l.startswith('#') or l.startswith('id\t') or not l.strip(): continue
        if '\t' in l:
            c = l.rstrip('\n').split('\t')            # id, paso, clase, capitulo, linea, lectura
            d[(c[0], int(c[1]))] = (c[2], c[4])
        else:
            c = [x.strip() for x in l.split('|', 4)]  # id, paso, marca, linea, lectura
            d[(c[0], int(c[1]))] = (c[2], c[3])
    return d
yo, el = leer('.v73aud/fidelidad.tsv'), leer('.v73ext/fidelidad.tsv')
print('filas mias: %d | suyas: %d | solo mias: %d | solo suyas: %d' % (len(yo), len(el), len(set(yo) - set(el)), len(set(el) - set(yo))))
par = collections.Counter((yo[k][0], el[k][0]) for k in yo if k in el)
print('pares (mia, suya): %s | suma: %d' % (dict(sorted(par.items())), sum(par.values())))
print('filas con linea del libro distinta: %d' % sum(1 for k in yo if k in el and yo[k][1] != el[k][1]))
for k in yo:
    if k in el and (yo[k][0] != el[k][0] or yo[k][1] != el[k][1]):
        print('  %-52s paso %d | mia %s %s | suya %s %s' % (k[0], k[1], yo[k][0], yo[k][1], el[k][0], el[k][1]))
