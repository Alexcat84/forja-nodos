# -*- coding: utf-8 -*-
"""El estado de la linea serial al abrir la vuelta 42, contado del dato."""
import collections
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
from src import comun  # noqa: E402

print("poblacion: el arbol entero, sin filtrar")
print("dataset/nodos.jsonl                        : %d nodos"
      % len(comun.leer_jsonl(comun.RUTA_DATASET)))
print("bitacora/VEREDICTOS.jsonl                  : %d lineas"
      % len(comun.leer_jsonl(comun.RUTA_VEREDICTOS)))
for carpeta in ("cuarentena/scott_radical_candor",
                "cuarentena/_insertados/scott_radical_candor",
                "cuarentena/grove_high_output"):
    ruta = os.path.join(RAIZ, carpeta)
    cuenta = len([f for f in os.listdir(ruta) if f.endswith(".json")]) \
        if os.path.isdir(ruta) else 0
    print("%-43s: %d" % (carpeta, cuenta))
caps = collections.Counter()
bandeja = os.path.join(RAIZ, "cuarentena", "scott_radical_candor")
for nombre in os.listdir(bandeja):
    if not nombre.endswith(".json"):
        continue
    crudo = comun.leer_texto(os.path.join(bandeja, nombre))
    for capitulo in set(re.findall(r"scott_radical_candor/(cap_\d+)\.md", crudo)):
        caps[capitulo] += 1
print("la bandeja de scott por capitulo           : %s"
      % ", ".join("%s %d" % (c, n) for c, n in sorted(caps.items())))
