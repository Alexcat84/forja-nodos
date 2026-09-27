# -*- coding: utf-8 -*-
"""Tasa y banda de la muestra pineada de los SANO de la fase ciega de la 65 (AUDITOR_FORJA.md 7):
intervalo de Wilson al 95 por ciento sobre caen k de n. k y n son los de .v65aud/muestra_sano.txt y
de la tabla de la seccion 7 de la apertura, y se escriben aqui a mano porque son el resultado de leer."""
import math
k, n, z = 0, 6, 1.96
p = k / n; d = 1 + z * z / n; c = (p + z * z / (2 * n)) / d
h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
print('caen %d de %d | tasa %.3f | banda Wilson 95%%: %.3f a %.3f' % (k, n, p, max(0, c - h), min(1, c + h)))
