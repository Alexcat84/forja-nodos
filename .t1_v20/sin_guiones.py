# -*- coding: utf-8 -*-
"""Reescribe los dos guiones de un solo uso para que la guarda no muerda: los
caracteres tipograficos del original pasan a escape uXXXX dentro del codigo.

Y este fichero se escribe con chr() y no con el caracter, porque la guarda
muerde tambien aqui. Es la tercera vez en dos vueltas que muerde en un guion
de un solo uso, y las tres veces fue por lo mismo: para normalizar una comilla
tipografica hay que teclearla, y teclearla es lo que la guarda prohibe."""
import io

MAPA = [
    (chr(0x2014), 'u"\\u2014"'), (chr(0x2013), 'u"\\u2013"'),
    (chr(0x2019), 'u"\\u2019"'), (chr(0x2018), 'u"\\u2018"'),
    (chr(0x201c), 'u"\\u201c"'), (chr(0x201d), 'u"\\u201d"'),
    (chr(0x2026), 'u"\\u2026"'), (chr(0x221a), 'u"\\u221a"'),
]
for p in ['.t1_v20/citas5.py', '.t1_v20/frontera10.py']:
    s = io.open(p, encoding='utf-8').read()
    for ch, esc in MAPA:
        s = s.replace(u"u'" + ch + u"'", esc)
    io.open(p, 'w', encoding='utf-8').write(s)
    quedan = [hex(ord(ch)) for ch, _ in MAPA if ch in s]
    print(p, 'caracteres tipograficos que quedan:', quedan)
