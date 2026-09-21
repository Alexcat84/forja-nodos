# -*- coding: utf-8 -*-
"""LA ARITMETICA DE LA TABLA DE COSTE Y DE LA BANDA, RECOMPUTADA."""
import math, re, io, os
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print("== LA TABLA DE COSTE DE KK.5.h, SUMADA POR MI")
filas = [("aduana d027", 559.4), ("aduana d032", 1479.4),
         ("aduana cap_02 P2", 855.8), ("aduana cap_02 P5", 1174.4),
         ("20 corridas d033", 449.7), ("prueba de aceptacion", 94.8)]
total = sum(v for _, v in filas)
print("   suma de las seis filas : %.1f   (el reporte publica 4613.6)" % total)
pasadas = sum(v for n, v in filas if n.startswith("aduana"))
print("   las cuatro pasadas     : %.1f   (el reporte publica 4069.0)" % pasadas)
print("   media por pasada       : %.2f  (el reporte publica 1017.3)" % (pasadas / 4.0))
print("   prosa (d027+d032)      : %.1f   (el reporte publica 2038.8)" % (559.4 + 1479.4))
print("   por ciento pasadas     : %.2f   (el reporte publica 88.2)" % (100.0 * pasadas / total))
print("   por ciento prosa       : %.2f   (el reporte publica 44.2)" % (100.0 * 2038.8 / total))
print("   por ciento de cada fila:", ["%.2f" % (100.0 * v / total) for _, v in filas])
print("   suma de los redondeos  : %.1f" % sum(round(100.0 * v / total, 1) for _, v in filas))
print("   4613.6 / 60            : %.2f min   (el reporte publica 76.9 de 82.5)" % (total / 60.0))
print("   4949 / 60              : %.2f min" % (4949 / 60.0))
print("   techo menos pasadas    : %.1f s   (el reporte publica 880)" % (4949 - pasadas))
print("   880 - 432              : %d s     (el reporte publica 448)" % (880 - 432))
print("   1017.3 / 903.4 - 1     : %.2f por ciento  (el reporte publica 12.6)"
      % (100.0 * (1017.3 / 903.4 - 1)))

print()
print("== LA BANDA DE WILSON DE 0 DE 20")
def wilson(x, n, z=1.959963984540054):
    p = float(x) / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    r = z * math.sqrt(p * (1 - p) / n + z * z / (4.0 * n * n))
    return (c - r) / d, (c + r) / d
for n in (6, 20, 26):
    lo, hi = wilson(0, n)
    print("   0 de %2d : de %.4f a %.4f" % (n, lo, hi))
print("   el reporte publica de 0,0000 a 0,1611 para 0 de 20")
print("   1/6 = %.4f ; 1/6 menos 0.1611 = %.4f  (el reporte publica 0,0056)"
      % (1 / 6.0, 1 / 6.0 - 0.1611))

print()
print("== LOS 20 RELOJES DE d033, SUMADOS DE LA TABLA PEGADA EN EL REPORTE")
rep = io.open(os.path.join(RAIZ, "docs", "loop", "REPORTE.md"), encoding="utf-8").read()
bloque = rep[rep.index("KK.4.a."):rep.index("KK.4.b.")]
segs = [float(m) for m in re.findall(r"^\s+\d+\s+0\s+([\d.]+)\s+OK\s*$", bloque, re.M)]
print("   corridas leidas de la tabla : %d" % len(segs))
print("   suma                        : %.1f  (el reporte publica 449.7)" % sum(segs))
print("   menor %.1f  media %.2f  mayor %.1f  (el reporte publica 21.7 / 22.5 / 23.1)"
      % (min(segs), sum(segs) / len(segs), max(segs)))
