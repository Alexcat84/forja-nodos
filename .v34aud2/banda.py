# -*- coding: utf-8 -*-
"""Banda de Wilson al 95 por ciento, el mismo metodo que las actas 29 a 32."""
import math, sys
def wilson(k, n, z=1.959963985):
    if n == 0: return (0.0, 100.0)
    p = float(k)/n
    d = 1 + z*z/n
    c = p + z*z/(2*n)
    r = z*math.sqrt(p*(1-p)/n + z*z/(4.0*n*n))
    return (100*max(0.0,(c-r)/d), 100*min(1.0,(c+r)/d))
for k, n, rot in ((0, 11, 'muestra pineada de los SANO'), (1, 181, 'PUENTE sobre los pasos del tramo'), (0, 13, 'caida de CLASE sobre los 13 veredictos')):
    lo, hi = wilson(k, n)
    print('%-42s %d de %-4d -> tasa %5.2f por ciento, banda al 95 por ciento: %.2f a %.2f' % (rot, k, n, 100.0*k/n, lo, hi))
