# Banda de Wilson al 95 por ciento, que es la que la ACTA 30 uso para su 6 de 6.
import math
def wilson(k, n, z=1.959963984540054):
    if n == 0: return (0.0, 100.0)
    p = k / n
    d = 1 + z*z/n
    c = (p + z*z/(2*n)) / d
    h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return (max(0.0, (c-h)*100), min(100.0, (c+h)*100))
for k, n in ((0,1),):
    lo, hi = wilson(k, n)
    print("caidas %d de %d -> tasa %.2f por ciento, banda al 95 por ciento: %.2f a %.2f" % (k, n, 100*k/n, lo, hi))
