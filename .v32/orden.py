# -*- coding: utf-8 -*-
"""EL ORDEN DEL LIBRO PARA cap_11, GENERADO DEL PROPIO DATO Y NO TECLEADO (`D.36`).

VERSION 2 de la de `.v31`, con el MISMO endurecimiento que la `TAREA 2` puso en
`.v32/cabeza.py`: el rango se toma **solo de la formula literal `Sale de las
lineas`**, que es el que el nodo declara DE SI MISMO. La version de `.v31` tomaba
el primer `lineas N a M` que apareciera tras el nombre del capitulo, y eso en
`montar_reunion_gran_debate` habria dado el tramo del vecino si el orden de la
prosa hubiera sido otro.
"""
import glob
import io
import json
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

BANDEJA = "cuarentena/scott_radical_candor"
CAPITULO = "cap_11"
FUENTE = "fuentes/scott_radical_candor/%s.md" % CAPITULO
FORMULA = "Sale de las lineas "
TRAMO = re.compile(r"^(\d+)\s+a\s+(?:las\s+)?(\d+)")

filas = []
sin_rango = []
for ruta in sorted(glob.glob(BANDEJA + "/*.json")):
    datos = json.load(io.open(ruta, encoding="utf-8"))
    resumen = datos.get("resumen_teorico", "")
    if FUENTE not in resumen:
        continue
    posicion = resumen.find(FORMULA)
    casa = TRAMO.match(resumen[posicion + len(FORMULA):]) if posicion >= 0 else None
    if not casa:
        sin_rango.append(datos["id"])
        continue
    filas.append((int(casa.group(1)), int(casa.group(2)),
                  datos["id"], len(datos["pasos_accionables"])))
filas.sort()

print("ORDEN DEL LIBRO, %s, LO QUE QUEDA EN BANDEJA" % CAPITULO)
print("poblacion: %s, filtrada por resumen_teorico que cita %s" % (BANDEJA, FUENTE))
print("el rango sale de la formula literal `%s`, no del primero que aparezca" % FORMULA.strip())
print()
print("| # | id | lineas | pasos |")
print("|---:|---|---|---:|")
total = 0
for indice, (desde, hasta, identificador, pasos) in enumerate(filas, 1):
    print("| %d | `%s` | `L%d` a `L%d` | %d |"
          % (indice, identificador, desde, hasta, pasos))
    total += pasos
print()
print("candidatos: %d   pasos: %d" % (len(filas), total))
print()
print("Y LOS QUE NOMBRAN %s SIN SALIR DE EL: %d" % (CAPITULO, len(sin_rango)))
for identificador in sin_rango:
    print("  %s   (lo nombra en un veredicto, su origen es otro capitulo)"
          % identificador)
