# -*- coding: utf-8 -*-
"""LA COMPROBACION DE LA ARISTA COLGADA DE identificar_paso_limitante_jornada_desfases.

El encargo de la vuelta 48, 2.b, dice que ese nodo declara una arista hacia
usar_calendario_herramienta_planificacion_produccion y que ese id no vivia en ninguna
sede. Esto lo recuenta HOY sobre las mismas dos sedes que el auditor conto: el grafo
(dataset/nodos.jsonl) y las bandejas de cuarentena, incluidas las de insertados.
"""
import glob
import io
import json
import os
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

DIANA = "usar_calendario_herramienta_planificacion_produccion"

ids_grafo = set()
for linea in io.open("dataset/nodos.jsonl", encoding="utf-8"):
    linea = linea.strip()
    if linea:
        ids_grafo.add(json.loads(linea)["id"])

ids_bandeja = {}
for ruta in glob.glob("cuarentena/**/*.json", recursive=True):
    if os.sep + "_" in ruta or ruta.replace("\\", "/").split("/")[1].startswith("_"):
        sede = "cuarentena/_insertados"
    else:
        sede = "/".join(ruta.replace("\\", "/").split("/")[:2])
    try:
        d = json.load(io.open(ruta, encoding="utf-8"))
    except ValueError:
        continue
    if isinstance(d, dict) and "id" in d:
        ids_bandeja.setdefault(d["id"], []).append(sede)

print("$ python .v48/arista_colgada.py")
print("fichas contadas: %d en el grafo, %d en bandejas, %d en total"
      % (len(ids_grafo), len(ids_bandeja), len(ids_grafo) + len(ids_bandeja)))
print("")
print("el id que la arista de identificar_paso_limitante_jornada_desfases nombra:")
print("   %s" % DIANA)
print("   en dataset/nodos.jsonl : %s" % ("SI" if DIANA in ids_grafo else "NO"))
sedes = ids_bandeja.get(DIANA, [])
print("   en cuarentena          : %s   %s"
      % ("SI" if sedes else "NO", ", ".join(sorted(set(sedes)))))
print("")
print("ARISTA COLGADA: %s" % ("NO, el destino existe" if (DIANA in ids_grafo or sedes)
                              else "SI, el destino no existe en ninguna sede"))
