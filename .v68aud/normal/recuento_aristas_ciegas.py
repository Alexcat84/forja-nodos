# -*- coding: utf-8 -*-
"""ACTA 67, mi caida propia: el recuento de .v68aud/aristas_lectura.tsv que la ultima linea de .v68aud/cruce_aristas.py publico
en APERTURA_CIEGA.md 7 cuenta SOSTENGO con startswith y NO con igualdad, asi que deja fuera las filas 'NO, DUDA'. Aqui cada
clase con el MISMO predicado (la palabra antes de la coma), y la suma contra el total."""
import io, collections
filas = [l.rstrip('\n').split('\t') for l in io.open('.v68aud/aristas_lectura.tsv', encoding='utf-8')][1:]
c = collections.Counter(f[2].split(',')[0].strip() for f in filas)
d = collections.Counter(f[2].split(',')[0].strip() for f in filas if 'DUDA' in f[2])
print('filas: %d | por clase: %s | de ellas con DUDA: %s | suma: %d' % (len(filas), dict(c), dict(d), sum(c.values())))
print("lo que publico la apertura: SOSTENGO %d (startswith) | NO %d (igualdad exacta)" % (sum(f[2].startswith('SOSTENGO') for f in filas), sum(f[2] == 'NO' for f in filas)))
