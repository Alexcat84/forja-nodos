# -*- coding: utf-8 -*-
"""EL PEGADO DE LA CITA (D.35), CORTADO ANTES DEL PRIMER GUION PROHIBIDO DEL LIBRO.

Convencion ya usada por esta casa en la vuelta 12 (A.1) y en la vuelta 27: el
barrido de guiones barre docs/ y no barre fuentes/, asi que la cita se corta antes
del primer guion prohibido del original y las comillas tipograficas se bajan a
rectas. POR NADA MAS: no se corrige ortografia, no se completa la frase, no se
traduce dentro de la cita.
"""
import io, sys
sys.path.insert(0, '.')
from src import comun

RUTA, ANCHO = sys.argv[1], 130
lineas = io.open(RUTA, encoding='utf-8').read().splitlines()
for arg in sys.argv[2:]:
    n = int(arg)
    t = lineas[n - 1].strip()
    corte = min([t.index(c) for c in comun.GUIONES_PROHIBIDOS if c in t] or [len(t)])
    cortada = corte < len(t)
    t = t[:corte].rstrip()
    for malo, bueno in ((u'‘', "'"), (u'’', "'"), (u'“', '"'), (u'”', '"')):
        t = t.replace(malo, bueno)
    sufijo = ''
    if len(t) > ANCHO:
        t, sufijo = t[:ANCHO].rstrip(), ' ...'
    elif cortada:
        sufijo = ' [CORTADA ANTE GUION DEL LIBRO]'
    print('%d: %s%s' % (n, t, sufijo))
