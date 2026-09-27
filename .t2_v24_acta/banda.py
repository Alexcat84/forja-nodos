"""Instrumento del auditor, vuelta 24, ACTA 24 seccion 4.3 y 5.

Banda exacta de Clopper-Pearson para la muestra pineada, sin dependencias fuera
de la libreria estandar, mas las tres cifras del freno que el acta firma.

    python .t2_v24_acta/banda.py
"""
from math import comb


def bino_cola(k, n, p):
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(0, k + 1))


n, k = 8, 0
a, b = 0.0, 1.0
for _ in range(200):
    m = (a + b) / 2
    if bino_cola(k, n, m) > 0.025:
        a = m
    else:
        b = m
hi = (a + b) / 2
print("caidas %d de %d  ->  tasa %.4f" % (k, n, k / n))
print("banda exacta (Clopper-Pearson) al 95 por ciento: [%.4f , %.4f]" % (0.0, hi))
print("es decir: entre 0 y %.1f por ciento" % (hi * 100))
print()
print("cap_14 con 1 puente de 174 pasos: %.2f por ciento" % (100 * 1 / 174))
print("lote 4 con 36 de 1688:            %.2f por ciento" % (100 * 36 / 1688))
print("hueco de SEIS filas: candidatos %d, pasos %d" % (1 + 1 + 8 + 10 + 25 + 12,
                                                       9 + 10 + 76 + 117 + 225 + 102))
print("ocurrencias del hueco (1+6+20+33+20+17) =", 1 + 6 + 20 + 33 + 20 + 17)
