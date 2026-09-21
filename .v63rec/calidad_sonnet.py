# -*- coding: utf-8 -*-
"""PASOS INVENTADOS POR CAPITULO de la corrida con Sonnet (vueltas 56 a 62).

Las filas NO se derivan aqui: se transcriben de la seccion del acta que las
firmo, una por una, y este script solo SUMA y divide, que es lo que D.59 pide
que haga un instrumento y no una frase.

  acta 55 -> vuelta 56 | acta 56 -> 57 | acta 57 -> 58 | acta 58 -> 59
  acta 59 -> vuelta 60 | acta 60 -> 61 | acta 61 -> 62
"""
# (vuelta, acta, seccion, capitulo, pasos escritos, pasos de la muestra D.58,
#  pasos leidos por el auditor, PUENTE)
FILAS = [
    (56, 55, "55.2", "cap_08",  0, None,  0, 0),
    (56, 55, "55.2", "cap_09",  0, None,  0, 0),
    (56, 55, "55.2", "cap_10",  8,    8,  8, 0),
    (57, 56, "56.2", "cap_11", 17,   15, 17, 0),
    (57, 56, "56.2", "cap_12", 11,   11, 11, 0),
    (57, 56, "56.2", "cap_13", 14,   14, 14, 0),
    (58, 57, "57.2", "cap_14", 18,   15, 18, 0),
    (58, 57, "57.2", "cap_15", 22,   15, 22, 0),
    (58, 57, "57.2", "cap_16",  4, None,  4, 0),
    (60, 59, "59.5", "cap_17", 16,   15, 16, 0),
    (60, 59, "59.5", "cap_18",  0, None,  0, 0),
]
# vueltas 59, 61 y 62 escribieron CERO pasos: SIN SUPERFICIE, y consta
# en 58.8, 60.7 y 61.6. No aportan filas porque no hay denominador.

print("PASOS INVENTADOS POR CAPITULO, CORRIDA CON SONNET (vueltas 56 a 62)")
print()
print("%-8s %-6s %-7s %7s %8s %8s %7s  %s"
      % ("cap", "vuelta", "acta", "escritos", "muestra", "leidos", "PUENTE", "inventado"))
print("-" * 78)
esc = mue = lei = pue = 0
con_superficie = 0
supera_10 = []
for v, a, s, cap, e, m, l, p in FILAS:
    if e == 0:
        pct = "SIN SUPERFICIE"
    else:
        con_superficie += 1
        r = 100.0 * p / e
        pct = ("%.1f por ciento" % r).replace(".", ",")
        if r > 10.0:
            supera_10.append(cap)
    esc += e
    lei += l
    pue += p
    mue += (m if m is not None else 0)
    print("%-8s %-6d %-7s %7d %8s %8d %7d  %s"
          % (cap, v, "ACTA %d" % a, e, ("ENTERO" if m is None else m), l, p, pct))
print("-" * 78)
print("%-8s %-6s %-7s %7d %8d %8d %7d" % ("TOTAL", "", "", esc, mue, lei, pue))
print()
print("capitulos con superficie (pasos > 0)  : %d" % con_superficie)
print("pasos escritos por Sonnet             : %d" % esc)
print("pasos que la muestra de D.58 cubrio   : %d" % mue)
print("pasos que el auditor leyo de verdad   : %d" % lei)
print("pasos PUENTE encontrados              : %d" % pue)
print("cobertura de la lectura, leidos/escritos : %.1f por ciento"
      % (100.0 * lei / esc))
print("pasos inventados, PUENTE/escritos        : %.1f por ciento"
      % (100.0 * pue / esc))
print()
print("CAPITULOS QUE SUPERAN EL 10 POR CIENTO SIN RELECTURA ENTERA : %d"
      % len(supera_10))
print("   %s" % (", ".join(supera_10) if supera_10 else "NINGUNO"))
