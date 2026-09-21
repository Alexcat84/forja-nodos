# -*- coding: utf-8 -*-
"""LO QUE ESTA VUELTA ESCRIBIO EN bitacora/VEREDICTOS.jsonl, CONTADO DE SU FICHERO.

*La tabla se cuenta de su fichero* (EXTRACTOR.md 5). Aqui la poblacion son las lineas
que la maquina estampa con la fecha de hoy, que es el unico sello que dice de quien es
la linea, y **la fecha de hoy tampoco se teclea**: sale de `src/aduana._hoy()`, que es la
misma funcion que escribio esas lineas.
"""
import io
import json
import os
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import aduana  # noqa: E402

HOY = aduana._hoy()

filas = []
for numero, linea in enumerate(io.open("bitacora/VEREDICTOS.jsonl", encoding="utf-8"), 1):
    if not linea.strip():
        continue
    datos = json.loads(linea)
    if datos.get("fecha") != HOY:
        continue
    if datos.get("arista"):
        # en una arista por lectura el registro guarda `arista` como "madre > hijo",
        # y eso es lo que se publica: `candidato` y `vecino` ahi son hijo y madre,
        # y ponerlos en columnas de vecindad leeria la direccion al reves.
        clase = "**ARISTA por lectura**, paso %s" % datos.get("paso_citado")
        par = "`%s`" % datos["arista"]
    else:
        clase = datos.get("veredicto") or "?"
        par = "`%s` contra `%s`" % (datos.get("candidato") or "",
                                    datos.get("vecino") or "")
    filas.append((numero, par, clase,
                  ", ".join(datos.get("levantada_por") or []) or "ninguna"))

print("poblacion: bitacora/VEREDICTOS.jsonl, lineas con fecha %s (src/aduana._hoy())" % HOY)
print("lineas escritas por esta vuelta: %d" % len(filas))
print("")
print("| linea | el par, en el sentido en que el registro lo escribe | que se escribio | levantada por |")
print("|---:|---|---|---|")
for numero, par, clase, levantada in filas:
    print("| %d | %s | %s | %s |" % (numero, par, clase, levantada))
