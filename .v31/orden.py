# -*- coding: utf-8 -*-
"""EL ORDEN DEL LIBRO PARA cap_11, GENERADO DEL PROPIO DATO Y NO TECLEADO.

Lee el rango `cap_11.md ... lineas N a M` del `resumen_teorico` de cada fichero de
la bandeja y ordena por el. **La forma del rango NO es la de `cap_07`**, y eso se
descubre corriendo el instrumento, no suponiendolo: `cap_07` escribia
`cap_07.md, lineas N a M` y `cap_11` escribe `cap_11.md, unidad Cap. 8, Results.
Sale de las lineas N a M`.
"""
import glob
import json
import re

BANDEJA = "cuarentena/scott_radical_candor"
CAPITULO = "cap_11"
RANGO = re.compile(CAPITULO + r"\.md[^\n]*?lineas (\d+) a (\d+)")

filas = []
sin_rango = []
for ruta in sorted(glob.glob(BANDEJA + "/*.json")):
    datos = json.load(open(ruta, encoding="utf-8"))
    resumen = datos.get("resumen_teorico", "")
    if CAPITULO not in resumen:
        continue
    encaje = RANGO.search(resumen)
    if not encaje:
        sin_rango.append(datos["id"])
        continue
    filas.append((int(encaje.group(1)), int(encaje.group(2)),
                  datos["id"], len(datos["pasos_accionables"])))
filas.sort()

print("ORDEN DEL LIBRO, %s, LO QUE QUEDA EN BANDEJA" % CAPITULO)
print("poblacion: %s, filtrada por resumen_teorico que cita %s.md"
      % (BANDEJA, CAPITULO))
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
