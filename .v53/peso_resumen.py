# -*- coding: utf-8 -*-
"""CUANTO PESA EL resumen_teorico EN EL TEXTO DEL QUE LA SENIAL 1 SE CALCULA.

EXTRACTOR.md 11: una similitud de texto de 0,4 en adelante son gemelos y nada mas, y hay que
leer ese par antes que ningun otro. Esta vuelta levanta DOS pares por encima de 0,4, y antes de
veredictarlos mido de donde sale el texto que la senial compara, en vez de suponerlo.

Usa la MISMA funcion que la aduana (comun.texto_comparable), no una imitacion.
"""
import io
import json
import os
import sys

sys.path.insert(0, ".")
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

from src import comun  # noqa: E402

IDS = ["anunciar_decision_inesperada_reconvocar_reunion",
       "vencer_sindrome_grupo_pares_autoconfianza",
       "cortar_discusion_libre_momento_justo",
       "conducir_etapas_modelo_ideal_decision",
       "zanjar_seis_preguntas_decision_adelantado"]

print("    %-46s %10s %10s %10s %8s" % ("id", "comparable", "resumen", "pasos", "resumen"))
print("    %-46s %10s %10s %10s %8s" % ("", "caracteres", "caracteres", "caracteres", "%"))
for i in IDS:
    d = json.load(io.open("cuarentena/grove_high_output/%s.json" % i, encoding="utf-8"))
    comparable = comun.texto_comparable(d)
    resumen = d["resumen_teorico"]
    pasos = " ".join(d["pasos_accionables"])
    print("    %-46s %10d %10d %10d %7.1f" % (
        i[:46], len(comparable), len(resumen), len(pasos),
        100.0 * len(resumen) / max(1, len(comparable))))
