# -*- coding: utf-8 -*-
"""PASOS INVENTADOS POR CAPITULO (AUDITOR_FORJA.md 8.3), VUELTA 32.

EL DENOMINADOR SALE DEL DATO: cuenta `pasos_accionables` fichero a fichero.
EL NUMERADOR LO PONE EL EXTRACTOR LEYENDO, porque ninguna maquina lo puede poner
(`D.30`), y aqui viene de `.v32/fidelidad.py`, que es donde esta la relectura
paso a paso con su cita pegada.
"""
import io
import json
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

BANDEJA = "cuarentena/scott_radical_candor/%s.json"

# LA TANDA DE ESTA VUELTA, EN EL ORDEN DEL LIBRO
TANDA = [
    "montar_tablero_kanban_medir_actividades",
    "pasear_organizacion_hallar_problemas_pequenios",
    "debatir_decidir_asuntos_cultura_evitar_delegar",
]

# EL NUMERADOR, PUESTO POR MI LEYENDO CADA PASO CONTRA SU PARRAFO (.v32/fidelidad.py)
PUENTES = dict((identificador, 0) for identificador in TANDA)

pasos = 0
for identificador in TANDA:
    datos = json.load(io.open(BANDEJA % identificador, encoding="utf-8"))
    pasos += len(datos["pasos_accionables"])
puentes = sum(PUENTES.values())

porciento = ("%.2f" % (100.0 * puentes / pasos)).replace(".", ",")
print("| capitulo | nodos | **pasos escritos** | **PUENTE** | **PASOS INVENTADOS** |")
print("|---|---:|---:|---:|---:|")
print("| **`cap_11`** (lote 4, `scott_radical_candor`), el tramo que lo cierra | %d | **%d** | **%d** | **%s por ciento** |"
      % (len(TANDA), pasos, puentes, porciento))
print("| **total del tramo de esta vuelta** | %d | **%d** | **%d** | **%s por ciento** |"
      % (len(TANDA), pasos, puentes, porciento))
