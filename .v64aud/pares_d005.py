# -*- coding: utf-8 -*-
"""Pares distintos (sin orden) de los seis de d005, en el archivo (poblacion 462, fichas de
067c9df) y en el barrido de hoy (.v64aud/). Un par levantado desde los dos lados cuenta una vez."""
import re
src = open('.v64aud/vecinos_hoy.py', encoding='utf-8').read().split('sig = dejan')[0]
exec(src)
arch, hoy = set(), set()
for i in D005:
    for v in lee('%s/informe_%s.txt' % (A, i))[2]: arch.add(tuple(sorted((i, v))))
    for v in lee('.v64aud/informe_%s.txt' % i)[2]: hoy.add(tuple(sorted((i, v))))
print('pares distintos: archivo %d | hoy %d | en los dos %d | solo archivo %d | solo hoy %d' % (len(arch), len(hoy), len(arch & hoy), len(arch - hoy), len(hoy - arch)))
for a, b in sorted(arch - hoy): print('   SOLO ARCHIVO  ', a, '|', b)
for a, b in sorted(hoy - arch): print('   SOLO HOY      ', a, '|', b)
