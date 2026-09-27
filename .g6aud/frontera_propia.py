# -*- coding: utf-8 -*-
"""Codigo del AUDITOR, no del extractor: recuenta las piezas de cap_15 al digito."""
import io, re, sys

PIEZAS = [("R1",8,20),("R2",21,42),("R3",43,86),("R4",87,166),
          ("R5",167,178),("R6",179,184),("R7",185,279)]

ruta = "fuentes/gerber_emyth/cap_15.md"
lineas = io.open(ruta, encoding="utf-8").read().split("\n")
total = len([l for l in io.open(ruta, encoding="utf-8")])
print("lineas del fichero (wc -l equivalente): %d" % total)

def palabras(a, b):
    trozo = "\n".join(lineas[a-1:b])
    return len(re.findall(r"[^\s]+", trozo))

cubiertas = set()
solape = 0
suma = 0
for nombre, a, b in PIEZAS:
    p = palabras(a, b)
    suma += p
    print("  %-3s L%-3d a L%-3d  palabras %5d" % (nombre, a, b, p))
    for n in range(a, b+1):
        if n in cubiertas:
            solape += 1
        cubiertas.add(n)
cuerpo = palabras(8, 279)
print("cuerpo L8 a L279 : %d" % cuerpo)
print("suma de piezas   : %d" % suma)
print("residuo          : %d" % (cuerpo - suma))
print("lineas solapadas : %d" % solape)
sin = [n for n in range(8, 280) if n not in cubiertas]
print("lineas sin cubrir: %d" % len(sin))
print("borde superior de R7 contra el fichero: R7 acaba en %d, el fichero tiene %d" % (PIEZAS[-1][2], total))
