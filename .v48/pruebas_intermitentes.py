# -*- coding: utf-8 -*-
"""LAS CORRIDAS DE LA PRUEBA DE ACEPTACION DE ESTA VUELTA, CONTADAS DE SUS FICHEROS.

La corrida de cierre salio en ROJO la primera vez y VERDE la segunda, sin que nada del
arbol cambiara entre las dos. Esto no lo resuelve: lo MIDE, contando la linea `total:`
de cada fichero de corrida que esta vuelta dejo, para que la afirmacion tenga su fichero
y no mi memoria (EXTRACTOR.md 4).
"""
import io
import os
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

TOTAL = re.compile(r"total: (\d+) pruebas, (\d+) fallos, (\d+) errores")

CORRIDAS = [
    (".v48/apertura_pruebas.txt", "apertura, en su sitio del ciclo"),
    (".v48/cierre_pruebas_rojo.txt", "cierre, primera corrida"),
    (".v48/pruebas_diag.txt", "diagnostico, corrida suelta"),
    (".v48/cierre_pruebas.txt", "cierre, corrida aislada, la que se publica"),
]

verdes = rojas = 0
print("| # | fichero de la corrida | que corrida es | pruebas | fallos | errores |")
print("|---:|---|---|---:|---:|---:|")
for i, (ruta, que) in enumerate(CORRIDAS, 1):
    if not os.path.exists(ruta):
        continue
    m = TOTAL.search(io.open(ruta, encoding="utf-8").read())
    if m is None:
        continue
    pruebas, fallos, errores = m.group(1), m.group(2), m.group(3)
    if int(fallos) or int(errores):
        rojas += 1
    else:
        verdes += 1
    print("| %d | `%s` | %s | %s | **%s** | %s |" % (i, ruta, que, pruebas, fallos, errores))
print("")
print("corridas con fichero que citar : %d" % (verdes + rojas))
print("   en VERDE                    : %d" % verdes)
print("   en ROJO                     : %d" % rojas)
print("")
print("EL ARBOL NO CAMBIO ENTRE ELLAS: ni src/, ni tests/, ni scripts/, ni dataset/.")
print("LO QUE SE PUBLICA ES LA ULTIMA, AISLADA Y EN VERDE, Y EL ROJO SE DECLARA AL LADO.")
