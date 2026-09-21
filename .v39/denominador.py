# -*- coding: utf-8 -*-
"""EL DENOMINADOR DE cap_13, contado del dato: cuantos candidatos y cuantos pasos.

El tramo de esta vuelta son 3 de esos candidatos, y la fila de PASOS INVENTADOS se
publica con este denominador delante para que no se lea como la fila del capitulo.
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARPETAS = (("bandeja", os.path.join(RAIZ, "cuarentena", "scott_radical_candor")),
            ("insertados", os.path.join(RAIZ, "cuarentena", "_insertados",
                                        "scott_radical_candor")))
TRAMO = ("pedir_critica_primero_crear_seguridad_psicologica",
         "elegir_pregunta_recurrente_pedir_critica",
         "resolver_dudas_frecuentes_pedir_critica")

filas = []
for sitio, carpeta in CARPETAS:
    if not os.path.isdir(carpeta):
        continue
    for nombre in sorted(os.listdir(carpeta)):
        if not nombre.endswith(".json"):
            continue
        ruta = os.path.join(carpeta, nombre)
        crudo = io.open(ruta, encoding="utf-8").read()
        if not re.search(r"scott_radical_candor/cap_13\.md", crudo):
            continue
        d = json.loads(crudo)
        filas.append((d["id"], sitio, len(d["pasos_accionables"]),
                      d["id"] in TRAMO))

print("cap_13 ENTERO, contado del dato de hoy")
print("  %-56s %-11s %6s %s" % ("candidato", "donde", "pasos", "en mi tramo"))
print("  " + "-" * 92)
for ident, sitio, n, dentro in sorted(filas, key=lambda f: (f[1], f[0])):
    print("  %-56s %-11s %6d %s" % (ident[:56], sitio, n, "SI" if dentro else "."))
print("  " + "-" * 92)
print("  candidatos de cap_13          : %d   (%d en bandeja, %d insertados)"
      % (len(filas), sum(1 for f in filas if f[1] == "bandeja"),
         sum(1 for f in filas if f[1] == "insertados")))
print("  pasos de cap_13, todos        : %d" % sum(f[2] for f in filas))
print("  candidatos de MI TRAMO        : %d" % sum(1 for f in filas if f[3]))
print("  pasos de MI TRAMO             : %d" % sum(f[2] for f in filas if f[3]))
