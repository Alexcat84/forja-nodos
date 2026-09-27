# -*- coding: utf-8 -*-
"""EL OJO NUEVO DE LA VUELTA 35: toda construccion X or Y del tramo de cap_09,
localizada a maquina y no de memoria. Sobre cada una se relee el paso.
NEGADA: la 'or' cae bajo una negacion cercana (not, never, n't, no, nothing),
que es donde la polaridad se puede partir por la mitad.

Los caracteres tipograficos del libro se escriben aqui por su codigo (chr) y no
literales: este fichero vive dentro del repo y el barrido de guiones de la casa
tumba el commit si lleva un guion largo o medio, aunque sea para quitarlo."""
import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

LINEAS = list(range(331, 426, 2))
NEG = r"\b(?:not|never|no|nothing)\b|n[" + chr(0x2019) + r"']t\b"
SUAVE = {chr(0x2019): "'", chr(0x2018): "'", chr(0x201C): '"', chr(0x201D): '"',
         chr(0x2014): " ", chr(0x2013): " "}


def suavizar(texto):
    for malo, bueno in SUAVE.items():
        texto = texto.replace(malo, bueno)
    return texto


texto = open("fuentes/scott_radical_candor/cap_09.md", encoding="utf-8").read().split("\n")
total = 0
filas = []
for n in LINEAS:
    linea = texto[n - 1]
    for m in re.finditer(r"\bor\b", linea):
        total += 1
        ini = max(0, m.start() - 95)
        if re.search(NEG, linea[ini:m.start()], re.I):
            filas.append((n, suavizar(linea[ini:m.end() + 55]).strip()))
print("TRAMO cap_09, lineas 331 a 425: las 5 unidades del tramo")
print("  construcciones 'X or Y' halladas : %d" % total)
print("  de ellas, BAJO NEGACION cercana  : %d" % len(filas))
print("  releidas por el ojo nuevo        : %d" % len(filas))
print("")
for n, t in filas:
    print("  L%d: ...%s..." % (n, t))
