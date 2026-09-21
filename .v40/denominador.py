# -*- coding: utf-8 -*-
"""EL DENOMINADOR DE LA FILA DE PASOS INVENTADOS, contado del dato y no copiado.

cap_13 entero = los que siguen en bandeja + los ya insertados y archivados cuya
ficha declara cap_13 como unidad de origen.
"""
import io
import json
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RX = re.compile(r"scott_radical_candor/cap_13\.md")

TRAMO = ("abrazar_incomodidad_silencio_contar_seis",
         "escuchar_entender_critica_dominar_defensa",
         "premiar_franqueza_hacer_escucha_tangible",
         "integrar_peticion_critica_rutina_existente")

filas = []
for carpeta, sede in (("cuarentena/scott_radical_candor", "bandeja"),
                      ("cuarentena/_insertados/scott_radical_candor", "insertado")):
    base = os.path.join(RAIZ, carpeta)
    for nombre in sorted(os.listdir(base)):
        if not nombre.endswith(".json"):
            continue
        ruta = os.path.join(base, nombre)
        crudo = io.open(ruta, encoding="utf-8").read()
        if not RX.search(crudo):
            continue
        d = json.loads(crudo)
        filas.append((sede, d["id"], len(d["pasos_accionables"])))

print("  %-11s %-56s %s" % ("sede", "candidato", "pasos"))
print("  " + "-" * 78)
for sede, cid, n in sorted(filas, key=lambda f: (f[0], f[1])):
    marca = "  <-- tramo de hoy" if cid in TRAMO else ""
    print("  %-11s %-56s %5d%s" % (sede, cid[:56], n, marca))
print("  " + "-" * 78)
tot = sum(n for _s, _c, n in filas)
tramo = [f for f in filas if f[1] in TRAMO]
print("  cap_13 ENTERO      : %2d candidato(s), %3d paso(s)" % (len(filas), tot))
print("  de ellos, MI TRAMO : %2d candidato(s), %3d paso(s)" % (len(tramo), sum(n for _s, _c, n in tramo)))
print("  los que NO he releido yo esta vuelta: %d candidato(s), %d paso(s)"
      % (len(filas) - len(tramo), tot - sum(n for _s, _c, n in tramo)))
