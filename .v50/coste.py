# -*- coding: utf-8 -*-
"""En que se fue el turno de la vuelta 50 (D.55). Los segundos NO se teclean: se leen
del fichero de reloj que escribio cada pasada, o de la linea `real` que escribio `time`."""
import io
import os
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

REAL = re.compile(r"real\s+(?:(\d+)m)?([\d.]+)s")


def del_reloj(ruta):
    m = re.search(r"segundos:\s*([\d.]+)", io.open(ruta, encoding="utf-8").read())
    if not m:
        raise SystemExit("sin linea 'segundos:' en %s" % ruta)
    return float(m.group(1))


def segundos(ruta):
    m = REAL.search(io.open(ruta, encoding="utf-8").read())
    if not m:
        raise SystemExit("sin linea 'real' en %s" % ruta)
    return int(m.group(1) or 0) * 60 + float(m.group(2))


PIEZAS = [
    ("pasada de aduana de `P41`", "`forja.py informe`", 1, del_reloj(".v50/reloj_c01.txt")),
    ("pasada de aduana de `P42`", "`forja.py informe`", 1, del_reloj(".v50/reloj_c02.txt")),
    ("pasada de aduana de `P44`", "`forja.py informe`", 1, del_reloj(".v50/reloj_c03.txt")),
    ("prueba de aceptacion al cierre", "`tests/test_aceptacion.py`", 1,
     segundos(".v50/cierre_pruebas.txt")),
]
if os.path.exists(".v50/cierre_guardas.txt"):
    PIEZAS.append(("las cuatro guardas restantes del cierre", "`gate`, `guiones`, `tallado`, `censo`",
                   4, del_reloj(".v50/cierre_guardas.txt")))

total = sum(p[3] for p in PIEZAS)
corridas = sum(p[2] for p in PIEZAS)
print("| pieza del turno | instrumento | corridas | segundos | por ciento del turno |")
print("|---|---|---:|---:|---:|")
for nombre, inst, n, s in PIEZAS:
    print("| %s | %s | %d | %.1f | %.1f |" % (nombre, inst, n, s, 100.0 * s / total))
print("| **TOTAL MEDIDO CON RELOJ** | | **%d** | **%.1f** | **100.0** |" % (corridas, total))
print()
aduana = sum(p[3] for p in PIEZAS[:3])
print("pasadas de aduana        : 3 de un techo de 3,  %.1f s,  %.1f por ciento del turno"
      % (aduana, 100.0 * aduana / total))
print("media por pasada de aduana    : %.1f s   (la cifra que la vuelta 51 tiene que usar, 47.5.c)"
      % (aduana / 3.0))
print("estimada por el encargo       : 1017.3 s por pasada, o sea 3051.9 s las tres")
print("desvio de la estimacion       : %+.1f s  (%+.1f por ciento)"
      % (aduana - 3051.9, 100.0 * (aduana - 3051.9) / 3051.9))
print("techo en minutos              : %.1f s medidos de un techo de 3420 s, o sea %.1f min de 57.0"
      % (total, total / 60.0))
