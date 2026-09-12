# Clopper y Pearson al 95 por ciento.
# Se usa la relacion exacta entre la beta y la binomial acumulada:
#   limite bajo  = el p que cumple  P(X >= k | p) = 0.025
#   limite alto  = el p que cumple  P(X <= k | p) = 0.025
# Se resuelve por biseccion sobre la binomial acumulada, sin integrar nada.
from math import comb


def cola_alta(k, n, p):
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))


def cola_baja(k, n, p):
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(0, k + 1))


def biseccion(f, objetivo, creciente):
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        v = f(mid)
        if (v < objetivo) == creciente:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def banda(k, n):
    baja = 0.0 if k == 0 else biseccion(lambda p: cola_alta(k, n, p), 0.025, True)
    alta = 1.0 if k == n else biseccion(lambda p: cola_baja(k, n, p), 0.025, False)
    return 100.0 * k / n, 100.0 * baja, 100.0 * alta


for nombre, k, n in [('cap_01', 0, 9), ('cap_03', 0, 7), ('cap_04', 3, 48),
                     ('cap_05', 2, 68), ('cap_06', 0, 117),
                     ('lote 4 entero', 5, 249), ('lote 3 firmado', 13, 393),
                     ('muestra SANO', 0, 4)]:
    p, lo, hi = banda(k, n)
    print('%-16s %2d de %3d = %5.2f por ciento   banda %4.2f a %5.2f' % (nombre, k, n, p, lo, hi))
