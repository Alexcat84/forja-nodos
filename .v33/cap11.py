# -*- coding: utf-8 -*-
"""REGENERA LA CIFRA CAIDA DE LA VUELTA 32 DEL DATO, NO DE LA TABLA QUE CORRIJO.

Es el `REMEDIO 2` que la `ACTA 31` dejo escrito: *todo recuento que publico corrigiendo
una tabla ajena lo genero del dato, nunca leyendo la tabla que corrijo.*

    poblacion : dataset/nodos.jsonl ENTERO, sin filtrar por bandeja
    criterio  : el nodo CITA su unidad de origen en `resumen_teorico`, que es donde esta
                casa la escribe (hallazgo de la ACTA 26); sus pasos son
                `pasos_accionables`
    CERO constantes tecleadas dentro: no hay lista de ids en este fichero (D.41)
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
from src import comun  # noqa: E402

UNIDAD = "cap_11"

nodos = comun.leer_jsonl(comun.RUTA_DATASET)
print("poblacion: %s, %d nodos, SIN filtrar por bandeja"
      % (comun.relativa(comun.RUTA_DATASET), len(nodos)))
print("criterio : '%s' citado en resumen_teorico" % UNIDAD)
de_la_unidad, pasos = [], 0
for n in nodos:
    if UNIDAD in (n.get("resumen_teorico") or ""):
        de_la_unidad.append(n.get("id", "?"))
        pasos += len(n.get("pasos_accionables", []) or [])
print("")
print("nodos del GRAFO con %s como unidad de origen : %d" % (UNIDAD, len(de_la_unidad)))
print("sus pasos_accionables                          : %d" % pasos)
print("")
for id_nodo in sorted(de_la_unidad):
    print("   %s" % id_nodo)
