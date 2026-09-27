# -*- coding: utf-8 -*-
"""CUANTOS PARES DE COLA ABRIO ESTA VUELTA, CONTADOS DE LOS INFORMES Y NO DE MI MEMORIA.

Suma la linea 'vecinos levantados en total' de cada .v53/aduana_c*.txt y la cruza con el
numero de filas de veredicto que el reporte publica. EXTRACTOR.md 5: la tabla se cuenta de su
fichero, y si las dos cuentas no coinciden, la que manda es la del instrumento.
"""
import glob
import io
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

total = 0
print("    %-28s %10s %10s" % ("informe", "saldo", "vecinos"))
for ruta in sorted(glob.glob(".v53/aduana_c*.txt")):
    crudo = io.open(ruta, encoding="utf-8").read()
    vecinos = re.search(r"vecinos levantados en total\s*:\s*(\d+)", crudo)
    bloquea = re.search(r"BLOQUEARIAN esperando veredicto\s*:\s*(\d+)", crudo)
    cae = re.search(r"CAERIAN por una guarda\s*:\s*(\d+)", crudo)
    n = int(vecinos.group(1)) if vecinos else 0
    if cae and int(cae.group(1)):
        saldo = "CAERIA"
    elif bloquea and int(bloquea.group(1)):
        saldo = "BLOQUEARIA"
    else:
        saldo = "ENTRARIA"
    total += n
    print("    %-28s %10s %10d" % (ruta, saldo, n))
print("")
print("    PARES DE COLA QUE ESTA VUELTA ABRE, sumados de los informes : %d" % total)
