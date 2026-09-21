# -*- coding: utf-8 -*-
"""El estado de la linea serial al cerrar la vuelta 33, contado del dato."""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
from src import comun  # noqa: E402

print("poblacion: el arbol entero, sin filtrar")
print("dataset/nodos.jsonl                     : %d nodos"
      % len(comun.leer_jsonl(comun.RUTA_DATASET)))
print("bitacora/VEREDICTOS.jsonl               : %d lineas"
      % len(comun.leer_jsonl(comun.RUTA_VEREDICTOS)))
for carpeta in ("cuarentena/scott_radical_candor",
                "cuarentena/_insertados/scott_radical_candor"):
    ruta = os.path.join(RAIZ, carpeta)
    cuenta = len([f for f in os.listdir(ruta) if f.endswith(".json")]) \
        if os.path.isdir(ruta) else 0
    print("%-40s: %d" % (carpeta, cuenta))
