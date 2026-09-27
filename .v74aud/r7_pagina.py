# -*- coding: utf-8 -*-
"""Fase ciega de la 74 (copia de .v73aud/r7_pagina.py, sin cambios en el codigo), R7 medido sobre la pagina: en docs/loop/APERTURA_CIEGA.md, las lineas de salida de los
bloques $ (sangradas y que no son el propio comando) que reparten una cifra en clases con la forma {'clase': N, ...},
y cuantas traen 'suma'. Solo lee."""
import io, re, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
c = collections.Counter()
for l in io.open('docs/loop/APERTURA_CIEGA.md', encoding='utf-8'):
    if l.startswith('    ') and not l.startswith('    $ ') and re.search(r"\{'[^}]*': \d+", l):
        c['con suma' if 'suma' in l else 'sin suma'] += 1
print('lineas de bloque que reparten en clases: %d | por estado: %s | suma: %d' % (sum(c.values()), dict(c), sum(c.values())))
