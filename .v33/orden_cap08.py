# -*- coding: utf-8 -*-
"""EL TRAMO DE cap_08, EN EL ORDEN DEL LIBRO Y CON SU SEDE DE HOY.

*La tabla se cuenta de su fichero* (EXTRACTOR.md 5). El orden NO se teclea: sale de la
linea de arranque que cada candidato declara en su `resumen_teorico`, y la sede sale de
mirar en cual de las dos carpetas esta hoy el fichero.

Es el instrumento de la vuelta 32 (`.v32/orden.py`) apuntado a este capitulo.
"""
import io
import json
import os
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_stdout = sys.stdout
sys.stdout = io.StringIO()
import fidelidad                     # noqa: E402  la tanda no se teclea dos veces
sys.stdout = _stdout

BANDEJA = "cuarentena/scott_radical_candor/%s.json"
ARCHIVO = "cuarentena/_insertados/scott_radical_candor/%s.json"

EN_GRAFO = set()
for linea in io.open("dataset/nodos.jsonl", encoding="utf-8"):
    EN_GRAFO.add(json.loads(linea)["id"])

filas = []
for identificador, _relectura in fidelidad.TANDA:
    datos = fidelidad.ficha(identificador)
    arranque = re.search(r"lineas? (\d+) a", datos["resumen_teorico"])
    filas.append((int(arranque.group(1)) if arranque else 0,
                  identificador,
                  len(datos["pasos_accionables"]),
                  "**si**" if identificador in EN_GRAFO else "NO",
                  "`_insertados`" if os.path.exists(ARCHIVO % identificador)
                  else ("`cuarentena`" if os.path.exists(BANDEJA % identificador)
                        else "*sin fichero*")))

print("| # | arranca en | candidato | pasos | en el grafo | sede del fichero |")
print("|---:|---:|---|---:|---|---|")
for orden, (linea, identificador, pasos, grafo, sede) in enumerate(sorted(filas), 1):
    print("| %d | `L%d` | `%s` | %d | %s | %s |"
          % (orden, linea, identificador, pasos, grafo, sede))
print("| | | **%d candidatos** | **%d** | **%d en el grafo** | |"
      % (len(filas), sum(f[2] for f in filas),
         sum(1 for f in filas if f[3] == "**si**")))
