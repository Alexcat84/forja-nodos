# -*- coding: utf-8 -*-
"""LOS 42 PASOS DE LA TANDA 57, CONTADOS POR MI FICHA A FICHA Y REPARTIDOS POR CAPITULO.

No leo la tabla del reporte: leo los siete JSON de cuarentena y el capitulo que cada
resumen_teorico declara como UNIDAD DE ORIGEN.
"""
import io
import json
import os
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

NUEVOS = [
    "elegir_modo_control_motivacion_factor_cua",
    "escalonar_complejidad_puesto_empleado_nuevo",
    "diagnosticar_capacidad_motivacion_prueba_vida",
    "fijar_meta_direccion_objetivos_mitad_probabilidad",
    "diagnosticar_nivel_motivacion_reaccion_aumento_salario",
    "elegir_estilo_direccion_madurez_relevante_tarea",
    "decidir_amistad_subordinado_prueba_revision_dificil",
]

por_cap = {}
total = 0
print("ficha                                                    pasos  capitulo")
print("-" * 78)
for n in NUEVOS:
    ruta = os.path.join("cuarentena", "grove_high_output", n + ".json")
    d = json.load(io.open(ruta, encoding="utf-8"))
    pasos = len(d.get("pasos_accionables", []))
    m = re.search(r"UNIDAD DE ORIGEN: fuentes/grove_high_output/(cap_\d+)\.md",
                  d.get("resumen_teorico", ""))
    cap = m.group(1) if m else "SIN DECLARAR"
    print("%-56s %3d  %s" % (n, pasos, cap))
    por_cap[cap] = por_cap.get(cap, 0) + pasos
    total += pasos

print("")
print("PASOS POR CAPITULO, contados por mi:")
for cap in sorted(por_cap):
    print("  %-10s %3d" % (cap, por_cap[cap]))
print("  TOTAL      %3d" % total)
