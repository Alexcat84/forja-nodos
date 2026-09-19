# -*- coding: utf-8 -*-
"""LOS DOS PASOS QUE LA SENIAL 3 CHOCO EN EL PAR 7, IMPRESOS DE SUS FICHAS.

El par 7 de la cola de esta tanda es el unico que levanta paso_contra_nodo en las tres
tandas de cap_04, y lo levanta a 0.718 contra un umbral de 0.60. El informe dice que
choca el paso 1 contra el paso 1. Esto los saca de las dos fichas para poder leerlos.
"""
import io
import json
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

for i in ("buscar_regularidad_bloques_iguales_trabajo_mando",
          "agrupar_tareas_semejantes_aprovechar_preparacion"):
    d = json.load(io.open("cuarentena/grove_high_output/%s.json" % i, encoding="utf-8"))
    print(i)
    print("  paso 1: %s" % d["pasos_accionables"][0])
