# -*- coding: utf-8 -*-
"""EL BORDE DE ARRIBA DE CADA FRONTERA QUE ESTE FRENTE HA ESCRITO.

Codigo del auditor. Para cada fichero de piezas de .gerber_v*/, compara la
ultima linea que declara la ultima pieza contra las lineas reales del fichero
del libro. Sirve para saber si una pieza que rebasa el fichero es convencion
del instrumento o es una celda suelta.
"""
import ast, glob, io, re

for f in sorted(glob.glob('.gerber_v*/piezas_cap*.txt')):
    # literal_eval y no eval: el fichero es una lista de tuplas del repo
    piezas = ast.literal_eval(io.open(f, encoding='utf-8').read())
    cap = re.search(r'piezas_cap_?(\d+)', f).group(1)
    ruta = 'fuentes/gerber_emyth/cap_%s.md' % cap.zfill(2)
    reales = len(io.open(ruta, encoding='utf-8').read().splitlines())
    fin = max(p[2] for p in piezas)
    print('%-32s ultima pieza L%-4d  fichero %-4d  %s'
          % (f, fin, reales, 'REBASA' if fin > reales else 'exacta'))
