# -*- coding: utf-8 -*-
"""MAPA DE LECTURA de una unidad: linea, palabras y su arranque. Ayuda de lectura."""
import io, sys, unicodedata

def llana(t):
    t = t.replace(chr(0x2014), '-').replace(chr(0x2013), '-')
    t = t.replace(u'‘', "'").replace(u'’', "'")
    t = t.replace(u'“', '"').replace(u'”', '"').replace(u'…', '...')
    return ''.join(c for c in unicodedata.normalize('NFD', t)
                   if unicodedata.category(c) != 'Mn')

ruta = sys.argv[1]
lineas = io.open(ruta, encoding='utf-8').read().split('\n')
for i, l in enumerate(lineas, 1):
    if l.strip():
        print('%4d  %4d  %s' % (i, len(l.split()), llana(l)[:100]))
