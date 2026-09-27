# -*- coding: utf-8 -*-
"""LA RELECTURA DE FIDELIDAD D.30 DE LOS 20 CANDIDATOS DE LA VUELTA 42.

Imprime, candidato a candidato, cuantos pasos trae y con que lineas del libro los
tengo contrastados en esta vuelta. La CUENTA sale del fichero; la MARCA de
TRANSCRIPCION o PUENTE la pongo yo leyendo el parrafo, que es lo que D.30 dice que
ninguna guarda puede hacer por mi.
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCHIVO = os.path.join(RAIZ, "cuarentena", "_insertados", "scott_radical_candor")
ORDEN = [l.split()[-1] for l in io.open(
    os.path.join(RAIZ, ".v42", "orden_apertura.txt"), encoding="utf-8")
    if l.strip() and l.split()[0].isdigit()]

# LA COLUMNA DE LA DERECHA CUENTA, NO RESUME. Cuenta CUANTAS lineas distintas del
# libro cita el resumen del candidato, que es lo unico que este instrumento sabe medir.
# La primera version imprimia un TRAMO de la menor a la mayor y era FALSO en dos filas
# (la 14 daba L143 a L145 donde el tramo es L145 a L151), asi que el tramo se retira y
# queda la cuenta. Un instrumento que resume lo que no sabe medir no mide: dicta.
total = 0
citas = 0
print("%-4s %-56s %-6s %-8s %s"
      % ("#", "candidato", "pasos", "puente", "lineas del libro citadas en su resumen"))
for i, ident in enumerate(ORDEN, 1):
    ficha = json.load(io.open(os.path.join(ARCHIVO, ident + ".json"), encoding="utf-8"))
    pasos = len(ficha["pasos_accionables"])
    total += pasos
    lineas = sorted(set(int(x) for x in re.findall(r"linea[s]? (\d+)", ficha["resumen_teorico"])))
    citas += len(lineas)
    print("%-4d %-56s %-6d %-8d %d" % (i, ident, pasos, 0, len(lineas)))
print()
print("TOTAL: %d pasos en 20 candidatos, 0 PUENTE, %d citas de linea" % (total, citas))
