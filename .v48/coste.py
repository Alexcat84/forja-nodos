# -*- coding: utf-8 -*-
"""EN QUE SE FUE EL TURNO (D.55), CONTADO DE LOS RELOJES Y NO DE MI MEMORIA.

No hay USD: este repo no tiene instrumento que mida el coste de un turno, y
EXTRACTOR.md 7 dice que lo que no se pueda medir se trae como pregunta y no se inventa.
Lo que la regla si persigue, en que se fue, se mide: cada corrida de la aduana dejo su
reloj, y las dos pruebas de aceptacion dejaron su linea `real`.

Esta vuelta NO tiene fila de ficha corregida: ninguna ficha vieja se retoco, porque la
arista colgada de 2.b se resolvio escribiendo el candidato 1 con el id que ya nombraba.
"""
import glob
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


relojes = sorted(glob.glob(".v48/reloj_c0*.txt"))
aduana = [segundos(r) for r in relojes]
pruebas = [segundos(".v48/apertura_pruebas.txt"), segundos(".v48/cierre_pruebas.txt")]
# LA CORRIDA DE CIERRE QUE SALIO EN ROJO TAMBIEN COSTO TIEMPO Y SE CUENTA APARTE:
# no es una guarda publicada, es lo que la intermitencia de .v48/pruebas_intermitentes.txt
# obligo a gastar. La corrida de diagnostico no lleva `real` y por eso no tiene cifra.
extra = [segundos(".v48/cierre_pruebas_rojo.txt")]
total = sum(aduana) + sum(pruebas) + sum(extra)

print("| en que se fue | medida | de donde sale |")
print("|---|---:|---|")
print("| **la aduana en seco de los `%d` candidatos** | **%d s** | PATRON: `.v48/reloj_c0*.txt`,"
      " sumados por `.v48/coste.py` |" % (len(aduana), sum(aduana)))
print("| las dos pruebas de aceptacion, apertura y cierre | %d s | `.v48/apertura_pruebas.txt` y"
      " `.v48/cierre_pruebas.txt`, las dos con su `real` |" % sum(pruebas))
print("| la corrida de cierre que salio en ROJO, repetida | %d s | `.v48/cierre_pruebas_rojo.txt`,"
      " con su `real`. La de diagnostico no lleva `real` y por eso no tiene cifra |" % sum(extra))
print("| ninguna ficha vieja retocada | 0 s | VACIA A PROPOSITO: esta vuelta no corrigio"
      " ninguna ficha ya escrita, asi que no hay reloj que citar |")
print("| el resto: leer el capitulo, escribir las `%d` fichas y el reporte | sin cifra |"
      " sin instrumento propio, y por eso no le pongo cifra |" % len(aduana))
print("| **total cronometrado del turno** | **%d s  (%.1f min)** | la suma de las filas de arriba |"
      % (total, total / 60.0))
print("")
print("EL POR CIENTO DE LO CRONOMETRADO QUE SE FUE EN LA ADUANA EN SECO: %.1f por ciento"
      % (100.0 * sum(aduana) / total))
print("  (la aduana entera, %d s de %d s cronometrados)" % (sum(aduana), total))
print("LA PRUEBA DE ACEPTACION, LAS DOS CORRIDAS PUBLICADAS         : %.1f por ciento"
      % (100.0 * sum(pruebas) / total))
print("LA CORRIDA EN ROJO QUE HUBO QUE REPETIR                      : %.1f por ciento"
      % (100.0 * sum(extra) / total))
print("")
print("Y NO HAY FILA EN USD: grep -rl USD src/ scripts/ forja.py da 0 ficheros.")
