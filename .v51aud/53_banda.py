# -*- coding: utf-8 -*-
"""La banda de Wilson al 95 por ciento para 0 caidas de 9 releidos (seccion 7:
una tasa sin banda es media cifra)."""
import math
def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 1.0)
    p = float(k) / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    r = z * math.sqrt(p * (1 - p) / n + z * z / (4.0 * n * n))
    return ((c - r) / d, (c + r) / d)

for k, n, que in ((0, 9, "SANO de la tanda releidos por mi"),
                  (0, 21, "pares que mire en la fase ciega"),
                  (0, 13, "discutibles marcados")):
    lo, hi = wilson(k, n)
    print("%2d de %2d caen  ->  tasa %.4f   banda de Wilson 95%%: [%.4f, %.4f]   %s"
          % (k, n, float(k) / n, lo, hi, que))
