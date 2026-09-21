# -*- coding: utf-8 -*-
"""TODOS LOS DESTINOS DE LAS ARISTAS DE HOY EXISTEN, COMPROBADO Y NO PROMETIDO.

Es la mitad mecanica de la leccion de 2.b: una arista declarada hacia un id que nadie
ha escrito queda colgada y ninguna guarda lo canta, porque el gate solo mira el grafo.
Esto recorre las 18 aristas que .v48/aristas.py lista y comprueba cada destino contra
las dos sedes donde un id puede vivir: el grafo y las bandejas de cuarentena.
"""
import glob
import io
import json
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

ids = set()
for l in io.open("dataset/nodos.jsonl", encoding="utf-8"):
    l = l.strip()
    if l:
        ids.add(json.loads(l)["id"])
for r in glob.glob("cuarentena/**/*.json", recursive=True):
    try:
        d = json.load(io.open(r, encoding="utf-8"))
    except ValueError:
        continue
    if isinstance(d, dict) and "id" in d:
        ids.add(d["id"])

LINEA = re.compile(r"\((\d)\) (D\.\d\d), ([A-Z ]+?) ([a-z0-9_]+),")
TANDA = ["usar_calendario_herramienta_planificacion_produccion",
         "decir_no_trabajo_excede_capacidad",
         "llevar_inventario_proyectos_discrecionales",
         "dimensionar_numero_subordinados_medio_dia_semanal",
         "buscar_regularidad_bloques_iguales_trabajo_mando"]

faltan = []
total = 0
for i in TANDA:
    d = json.load(io.open("cuarentena/grove_high_output/%s.json" % i, encoding="utf-8"))
    for m in LINEA.finditer(d["resumen_teorico"]):
        total += 1
        if m.group(4) not in ids:
            faltan.append((i, m.group(4)))

print("destinos de arista comprobados : %d" % total)
print("destinos que NO existen        : %d" % len(faltan))
for a, b in faltan:
    print("   %s  ->  %s" % (a, b))
print("CERO ARISTAS COLGADAS: %s" % ("SI" if not faltan else "NO"))
