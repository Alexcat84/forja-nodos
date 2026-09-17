# -*- coding: utf-8 -*-
"""LO QUE QUEDA EN BANDEJA AL CERRAR, CONTADO DE SU FICHERO (EXTRACTOR.md 5).

La unidad de origen NO se teclea: sale del `resumen_teorico` de cada candidato, que es
donde esta casa la escribe (hallazgo de la ACTA 26).

Es el instrumento de la vuelta 32 (`.v32/cola.py`) apuntado a este cierre.
"""
import collections
import glob
import io
import json
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

LOTES = [("lote 4", "scott_radical_candor"), ("lote 5", "marquet_turn_the_ship")]

UNIDADES = {"cap_04": "Cap. 1", "cap_05": "Cap. 2", "cap_06": "Cap. 3", "cap_07": "Cap. 4",
            "cap_08": "Cap. 5", "cap_09": "Cap. 6", "cap_10": "Cap. 7", "cap_11": "Cap. 8",
            "cap_12": "Getting Started", "cap_13": "Afterword", "cap_14": "Bonus Chapter"}

print("| lote | unidad | del libro | en bandeja | pasos escritos |")
print("|---|---|---|---:|---:|")
gran_total = gran_pasos = 0
for nombre, clave in LOTES:
    cuenta = collections.Counter()
    pasos = collections.Counter()
    for ruta in sorted(glob.glob("cuarentena/%s/*.json" % clave)):
        datos = json.load(io.open(ruta, encoding="utf-8"))
        hallazgo = re.search(r"cap_(\d+)\.md", datos.get("resumen_teorico") or "")
        unidad = "cap_%s" % hallazgo.group(1) if hallazgo else "*sin unidad citada*"
        cuenta[unidad] += 1
        pasos[unidad] += len(datos.get("pasos_accionables") or [])
    for unidad in sorted(cuenta):
        print("| %s, `%s` | `%s` | %s | **%d** | %d |"
              % (nombre, clave, unidad, UNIDADES.get(unidad, "*no mapeada*"),
                 cuenta[unidad], pasos[unidad]))
        gran_total += cuenta[unidad]
        gran_pasos += pasos[unidad]
print("| **las dos bandejas** | | | **%d** | **%d** |" % (gran_total, gran_pasos))
