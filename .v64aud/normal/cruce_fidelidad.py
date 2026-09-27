# -*- coding: utf-8 -*-
"""Cruza paso a paso mi clase ciega de fidelidad (.v64aud/fidelidad.tsv, fichas de 067c9df) contra la del
extractor (.v64ext/fidelidad.tsv). Las DUDA mias cuentan con la clase escrita en la columna clase."""
import io
def lee(ruta, sep):
    d = {}
    for l in io.open(ruta, encoding='utf-8'):
        if l.startswith('#') or l.startswith('id\t') or not l.strip(): continue
        c = [x.strip() for x in l.split(sep)]
        d[(c[0], int(c[1]))] = c[2]
    return d
a = lee('.v64aud/fidelidad.tsv', '\t'); e = lee('.v64ext/fidelidad.tsv', '|')
co = 0
for k in sorted(set(a) | set(e)):
    if a.get(k) == e.get(k): co += 1
    else: print('DISCREPA  %s paso %d  ciega %s  extractor %s' % (k[0], k[1], a.get(k), e.get(k)))
print('pasos: ciega %d | extractor %d | coinciden %d | discrepan %d' % (len(a), len(e), co, len(set(a) | set(e)) - co))
print('PUENTE: ciega %d | extractor %d' % (list(a.values()).count('P'), list(e.values()).count('P')))
