# -*- coding: utf-8 -*-
"""EN QUE SE FUE EL TURNO (D.55), CONTADO DE LOS RELOJES Y NO DE MI MEMORIA.

No hay USD: este repo no tiene instrumento que mida el coste de un turno, y
EXTRACTOR.md 7 dice que lo que no se pueda medir se trae como pregunta y no se inventa.
Lo que la regla si persigue, en que se fue, se mide: cada corrida de la aduana dejo su
reloj, y las dos pruebas de aceptacion dejaron su linea `real`.
"""
import io
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

SEG = re.compile(r"segundos=(\d+)")
REAL = re.compile(r"real\s+(\d+)m([\d.]+)s")


def segundos(ruta):
    s = io.open(ruta, encoding="utf-8").read()
    m = SEG.search(s)
    if m:
        return int(m.group(1))
    m = REAL.search(s)
    return int(round(int(m.group(1)) * 60 + float(m.group(2))))


aduana = [segundos(".v47/reloj_c%02d.txt" % n) for n in range(1, 7)]
madre = segundos(".v47/reloj_madre_p27.txt")
pruebas = [segundos(".v47/apertura_pruebas.txt"), segundos(".v47/cierre_pruebas.txt")]
total = sum(aduana) + madre + sum(pruebas)

print("| en que se fue | medida | de donde sale |")
print("|---|---:|---|")
print("| **la aduana en seco de los `6` candidatos** | **%d s** | PATRON: `.v47/reloj_c0*.txt`,"
      " sumados por `.v47/coste.py` |" % sum(aduana))
print("| el repaso de aduana de la ficha corregida de `P27` | %d s | `.v47/reloj_madre_p27.txt` |"
      % madre)
print("| las dos pruebas de aceptacion, apertura y cierre | %d s | `.v47/apertura_pruebas.txt` y"
      " `.v47/cierre_pruebas.txt`, las dos con su `real` |" % sum(pruebas))
print("| el resto: leer el capitulo, escribir las `6` fichas y el reporte | sin cifra |"
      " sin instrumento propio, y por eso no le pongo cifra |")
print("| **total cronometrado del turno** | **%d s  (%.1f min)** | la suma de las filas de arriba |"
      % (total, total / 60.0))
print("")
print("EL POR CIENTO DE LO CRONOMETRADO QUE SE FUE EN LA ADUANA EN SECO: %.1f por ciento"
      % (100.0 * (sum(aduana) + madre) / total))
print("  (la aduana entera, %d s de %d s cronometrados)" % (sum(aduana) + madre, total))
print("LA PRUEBA DE ACEPTACION, LAS DOS CORRIDAS                    : %.1f por ciento"
      % (100.0 * sum(pruebas) / total))
print("")
print("Y NO HAY FILA EN USD: grep -rl USD src/ scripts/ forja.py da 0 ficheros.")
