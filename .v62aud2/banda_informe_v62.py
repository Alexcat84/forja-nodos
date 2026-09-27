# -*- coding: utf-8 -*-
"""La banda del reloj de un forja.py informe, con las dos medidas de hoy."""
m = [(388.6, 437, "ACTA 57 57.10"), (477.8, 437, "ACTA 57 57.10"),
     (490.0, 440, "ACTA 60 60.4, el auditor"), (507.0, 440, "VUELTA 61 61.2.a, el extractor"),
     (510.0, 439, "ACTA 59 59.10, el auditor"), (668.0, 440, "VUELTA 61 61.2.b, el extractor"),
     (1002.0, 437, "ACTA 58 58.10"), (1062.0, 437, "ACTA 58 58.10"),
     (579.0, 440, "VUELTA 62 62.4, el extractor, reloj de sus dos date"),
     (438.5, 440, "ACTA 61, el auditor, HOY: .v62aud2/informe_detectar_AUDITOR.txt")]
m.sort()
print("MEDIDAS DIRECTAS DEL RELOJ DE UN python forja.py informe")
for s, p, c in m:
    print("  %7.1f s   poblacion %d   %s" % (s, p, c))
v = [x[0] for x in m]; n = len(v)
med = (v[n // 2 - 1] + v[n // 2]) / 2 if n % 2 == 0 else v[n // 2]
print("  " + "-" * 66)
print("  medidas   : %d" % n)
print("  BANDA     : %.1f a %.1f s   (factor %.2f entre extremos)" % (v[0], v[-1], v[-1] / v[0]))
print("  MEDIANA   : %.1f s" % med)
print("  media     : %.1f s   (se publica junto a la banda, NUNCA sola)" % (sum(v) / n))
