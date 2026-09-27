# -*- coding: utf-8 -*-
"""En que se fue el turno de la vuelta 49 (D.55). Los segundos NO se teclean: se leen
de la linea `real` de cada salida guardada, que es la que escribio `time`."""
import re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REAL = re.compile(r"real\s+(?:(\d+)m)?([\d.]+)s")


def segundos(ruta):
    t = io.open(ruta, encoding="utf-8").read()
    m = REAL.search(t)
    if not m:
        raise SystemExit("sin linea 'real' en %s" % ruta)
    return int(m.group(1) or 0) * 60 + float(m.group(2))


def de_la_tasa(ruta):
    t = io.open(ruta, encoding="utf-8").read()
    m = re.search(r"reloj de las 20\s+:\s+([\d.]+) s", t)
    return float(m.group(1))


PIEZAS = [
    ("pasada de aduana de `d027`", "`forja.py informe`", 1, segundos(".v49/informe_d027.txt")),
    ("pasada de aduana de `d032`", "`forja.py informe`", 1, segundos(".v49/informe_d032.txt")),
    ("pasada de aduana de `cap_02` `P2`", "`forja.py informe`", 1, segundos(".v49/informe_cap02_1.txt")),
    ("pasada de aduana de `cap_02` `P5`", "`forja.py informe`", 1, segundos(".v49/informe_cap02_2.txt")),
    ("las 20 corridas de `d033`", "`unittest PruebaE`", 20, de_la_tasa(".v49/d033_veinte.txt")),
    ("prueba de aceptacion al cierre", "`tests/test_aceptacion.py`", 1, segundos(".v49/cierre_pruebas.txt")),
]
total = sum(p[3] for p in PIEZAS)
corridas = sum(p[2] for p in PIEZAS)
print("| pieza del turno | instrumento | corridas | segundos | por ciento del turno |")
print("|---|---|---:|---:|---:|")
for nombre, inst, n, s in PIEZAS:
    print("| %s | %s | %d | %.1f | %.1f |" % (nombre, inst, n, s, 100.0 * s / total))
print("| **TOTAL MEDIDO CON RELOJ** | | **%d** | **%.1f** | **100.0** |" % (corridas, total))
print()
aduana = sum(p[3] for p in PIEZAS[:4])
prosa = PIEZAS[0][3] + PIEZAS[1][3]
print("pasadas de aduana        : 4 de un techo de 5,  %.1f s,  %.1f por ciento del turno"
      % (aduana, 100.0 * aduana / total))
print("de ellas, correccion de prosa : 2,  %.1f s,  %.1f por ciento del turno"
      % (prosa, 100.0 * prosa / total))
print("media por pasada de aduana    : %.1f s   (la cifra que la vuelta 50 tiene que usar, 47.5.c)"
      % (aduana / 4.0))
print("techo en minutos              : %.1f s medidos de un techo de 4949 s, o sea %.1f min de 82.5"
      % (total, total / 60.0))
