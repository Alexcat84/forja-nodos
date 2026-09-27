# -*- coding: utf-8 -*-
"""Mis 11 pares ciegos de hoy (.v65aud/mis_clases.tsv, escrito a las 23:47:50) contra MI apertura sellada de la
64 (git show 5b866f1:docs/loop/APERTURA_CIEGA.md, guardada en .v65aud/apertura_v64_propia.md, abierta DESPUES).
Busca las filas de tabla que nombran los dos (por sus dos primeras palabras, o por la primera con puntos suspensivos) y saca la clase en negrita."""
import io, re
v64 = [l for l in io.open('.v65aud/apertura_v64_propia.md', encoding='utf-8') if l.startswith('|')]
pre = lambda i: '_'.join(i.split('_')[:2])
esta = lambda i, f: pre(i) in f or ('`%s...`' % i.split('_')[0]) in f
igual = distinta = sin = 0
for l in io.open('.v65aud/mis_clases.tsv', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    c = [x.strip() for x in l.split('|')]
    filas = [f for f in v64 if esta(c[0], f) and esta(c[1], f)]
    clases = sorted(set(m.group(1) for f in filas for m in [re.search(r'\*\*(SANO|CONTINUA|REPITE|MUTUO|NO SOSTENIDA)', f)] if m))
    if not clases: sin += 1; e = 'SIN FILA EN LA 64'
    elif clases == [c[2]]: igual += 1; e = 'IGUAL'
    else: distinta += 1; e = 'DISTINTA %s' % clases
    print('%-9s hoy %-5s | %s | %s' % (e.split()[0], c[2], c[0], c[1]))
print('pares: %d | misma clase que mi apertura de la 64: %d | distinta: %d | sin fila alli: %d' % (igual + distinta + sin, igual, distinta, sin))
