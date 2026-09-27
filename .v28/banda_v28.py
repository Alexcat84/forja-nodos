# -*- coding: utf-8 -*-
"""La banda de una tasa, para que no se publique una tasa sin banda (seccion 7).

Wilson al 95 por ciento (z = 1,96) y Clopper-Pearson de dos colas al lado,
las dos con su formula escrita, porque una tasa sin banda es media cifra.

Uso: python .v28/banda_v28.py <caidas> <releidos>
"""
import math
import sys

Z = 1.959963985


def wilson(k, n, z=Z):
    if n == 0:
        return (0.0, 1.0)
    p = float(k) / n
    den = 1.0 + z * z / n
    centro = (p + z * z / (2.0 * n)) / den
    medio = (z * math.sqrt(p * (1.0 - p) / n + z * z / (4.0 * n * n))) / den
    return (max(0.0, centro - medio), min(1.0, centro + medio))


def clopper_alta(k, n, alfa=0.05):
    """Para k = 0 la cota alta exacta es 1 - (alfa/2)**(1/n)."""
    if k != 0:
        return None
    return 1.0 - (alfa / 2.0) ** (1.0 / n)


if __name__ == '__main__':
    k = int(sys.argv[1])
    n = int(sys.argv[2])
    lo, hi = wilson(k, n)
    print('releidos            : %d' % n)
    print('caidas              : %d' % k)
    print('tasa                : %.2f por ciento' % (100.0 * k / n if n else 0.0))
    print('banda Wilson 95 pct : %.1f a %.1f por ciento' % (100 * lo, 100 * hi))
    ca = clopper_alta(k, n)
    if ca is not None:
        print('cota alta exacta    : %.1f por ciento  (Clopper-Pearson, 1 - 0,025^(1/%d))'
              % (100 * ca, n))
