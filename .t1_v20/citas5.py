# -*- coding: utf-8 -*-
"""Las citas de linea de las cinco piezas, con la salida literal pegada (D.35)."""
import unicodedata
F = 'fuentes/scott_radical_candor/cap_09.md'
L = open(F, encoding='utf-8').read().split('\n')


def llana(s):
    s = (s.replace(u"\u2014", ' ').replace(u"\u2013", ' ')
          .replace(u"\u2019", "'").replace(u"\u2018", "'")
          .replace(u"\u201c", '"').replace(u"\u201d", '"')
          .replace(u"\u2026", '...').replace(u"\u221a", 'v'))
    return ''.join(c for c in unicodedata.normalize('NFKD', s)
                   if not unicodedata.combining(c))


LINEAS = [301, 303, 305, 309, 311, 313,
          315, 317, 319, 321, 323, 325, 327,
          331, 339, 341, 343, 345, 347, 353, 355, 357, 359, 361,
          383, 391, 393, 395, 397, 399, 401, 403, 405, 407, 409, 411, 413,
          415, 417, 419, 421, 423, 425]
for n in LINEAS:
    print("%d:%s" % (n, llana(L[n - 1].strip())[:96]))
