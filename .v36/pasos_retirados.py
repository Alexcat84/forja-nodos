# -*- coding: utf-8 -*-
"""MIDE LOS NODOS CUYO resumen_teorico RETIRA UN PASO QUE SIGUE EN EL CAMPO (D.54).

    poblacion: dataset/nodos.jsonl entero, sin filtrar
    criterio : el resumen_teorico declara una RETIRADA de un paso, y `pasos_accionables`
               todavia trae ese paso
CERO constantes tecleadas: no hay lista de ids dentro de este fichero (D.41).
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
from src import comun  # noqa: E402

# La forma con la que esta casa declara una retirada dentro del resumen.
RETIRADA = re.compile(
    r"(?:paso|P)\s*(\d+)[^.\n]{0,120}?\bretirad[oa]\b"
    r"|\bretirad[oa]\b[^.\n]{0,120}?(?:paso|P)\s*(\d+)", re.I)

nodos = comun.leer_jsonl(comun.RUTA_DATASET)
print("poblacion: %s, %d nodos, SIN filtrar" % (comun.relativa(comun.RUTA_DATASET),
                                                len(nodos)))
print("criterio : resumen_teorico declara una retirada de paso N, y pasos_accionables")
print("           todavia tiene N pasos o mas")
print("")

casos = []
for nodo in nodos:
    resumen = nodo.get("resumen_teorico") or ""
    pasos = nodo.get("pasos_accionables") or []
    for encaje in RETIRADA.finditer(resumen):
        numero = int(encaje.group(1) or encaje.group(2))
        if 1 <= numero <= len(pasos):
            casos.append((nodo.get("id", "?"), numero, len(pasos),
                          encaje.group(0).strip()))
            break

print("nodos con una retirada declarada y el paso todavia en el campo : %d" % len(casos))
print("")
for id_nodo, numero, total, frase in casos:
    print("  %s" % id_nodo)
    print("     paso %d de %d, y el resumen dice: %s" % (numero, total, frase[:90]))
