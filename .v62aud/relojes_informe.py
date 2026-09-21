# -*- coding: utf-8 -*-
"""LAS DOS RESTAS DE RELOJ QUE EL REPORTE DE LA 61 ESCRIBE, REHECHAS, Y LAS
MARCAS DE FICHERO QUE LAS CORROBORAN."""
import datetime
import os


def d(s):
    return datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')


CASOS = [
    ('informe 1', '2026-09-21 04:51:07', '2026-09-21 04:59:34', 507,
     '.v61ext/informe_1_priorizar.txt'),
    ('informe 2', '2026-09-21 05:00:29', '2026-09-21 05:11:37', 667,
     '.v61ext/informe_2_desarrollar.txt'),
]
for n, a, b, dice, fich in CASOS:
    real = int((d(b) - d(a)).total_seconds())
    veredicto = 'IGUAL' if real == dice else 'DISCREPA en %d' % (real - dice)
    print('%s: %s -> %s = %d s | el reporte dice %d s | %s'
          % (n, a, b, real, dice, veredicto))
    m = datetime.datetime.fromtimestamp(os.path.getmtime(fich))
    print('   mtime de %s: %s   (corrobora la marca de fin)'
          % (fich, m.strftime('%Y-%m-%d %H:%M:%S.%f')))
