# -*- coding: utf-8 -*-
"""Tasa con su banda (Wilson 95 por ciento). Una tasa sin banda es media cifra
(AUDITOR_FORJA 7)."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8')
def wilson(caen, n, z=1.96):
    if n == 0: return (0.0, 0.0, 0.0)
    p = caen / n
    d = 1 + z*z/n
    c = (p + z*z/(2*n)) / d
    h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return (p, max(0.0, c-h), min(1.0, c+h))
for nombre, caen, n in [("muestra pineada de los SANO, las dos tandas juntas", 1, 6),
                        ("muestra pineada, solo VUELTA 1", 1, 3),
                        ("muestra pineada, solo VUELTA 2", 0, 3)]:
    p, lo, hi = wilson(caen, n)
    print("%-52s caen %d de %d | tasa %5.1f por ciento | banda 95 [%.1f , %.1f]"
          % (nombre, caen, n, 100*p, 100*lo, 100*hi))
