# -*- coding: utf-8 -*-
"""PASOS INVENTADOS POR CAPITULO (AUDITOR_FORJA.md 8.3), VUELTA 34.

Es el instrumento de la vuelta 33 (`.v33/pasos_inventados.py`) apuntado a `cap_09`:
`D.47` manda cero instrumentos nuevos, y este no lo es.

EL DENOMINADOR SALE DEL DATO: cuenta `pasos_accionables` fichero a fichero.
EL NUMERADOR LO PONE EL EXTRACTOR LEYENDO, porque ninguna maquina lo puede poner
(`D.30`), y aqui viene de `.v34/fidelidad.py`, que es donde esta la relectura paso a paso
con su cita pegada y comprobada contra el libro.

LA TANDA NO SE TECLEA DOS VECES: se importa de `.v34/fidelidad.py`, asi que una tanda y
la otra no pueden separarse.
"""
import io
import json
import os
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_stdout = sys.stdout
sys.stdout = io.StringIO()          # la relectura imprime lo suyo; aqui solo quiero su tanda
import fidelidad                     # noqa: E402
sys.stdout = _stdout

UNIDAD = "cap_09"

pasos = 0
puentes = 0
for identificador, filas in fidelidad.TANDA:
    datos = fidelidad.ficha(identificador)
    pasos += len(datos["pasos_accionables"])
    puentes += sum(1 for f in filas if "PUENTE" in f[3])

porciento = ("%.2f" % (100.0 * puentes / pasos)).replace(".", ",")
print("| capitulo | nodos | **pasos escritos** | **PUENTE** | **PASOS INVENTADOS** |")
print("|---|---:|---:|---:|---:|")
print("| **`%s`** (lote 4, `scott_radical_candor`), el tramo de esta vuelta | %d | **%d** | "
      "**%d** | **%s por ciento** |"
      % (UNIDAD, len(fidelidad.TANDA), pasos, puentes, porciento))
print("| **total del tramo de esta vuelta** | %d | **%d** | **%d** | **%s por ciento** |"
      % (len(fidelidad.TANDA), pasos, puentes, porciento))
print("")
print("EL PEOR CAPITULO ES EL UNICO: la vuelta cierra en %s y no toca ninguna otra unidad,"
      % UNIDAD)
print("asi que el peor y el promedio son la misma cifra (AUDITOR_FORJA.md 8.3, la escalada")
print("se decide sobre el peor capitulo).")
