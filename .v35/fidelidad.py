# -*- coding: utf-8 -*-
"""PASOS INVENTADOS del tramo de cap_09 (D.30). La cuenta de pasos se lee del
fichero; la columna PUENTE es el veredicto de la relectura, uno por paso."""
import json

TRAMO = [
    ("entregar_evaluacion_formal_desempenio_nueve_consejos", "L331", 0),
    ("impedir_punialadas_espalda_equipo",                    "L363", 0),
    ("fomentar_guia_reciproca_companieros",                  "L369", 0),
    ("conducir_reuniones_salto_nivel_diez_reglas",           "L383", 0),
    ("resolver_dudas_frecuentes_reuniones_salto_nivel",      "L415", 0),
]

print("| unidad | linea | pasos | TRANSCRIPCION | PUENTE | por ciento |")
print("|---|---:|---:|---:|---:|---:|")
tp = tt = tb = 0
for nid, linea, puentes in TRAMO:
    d = json.load(open("cuarentena/scott_radical_candor/%s.json" % nid, encoding="utf-8"))
    n = len(d["pasos_accionables"])
    tp += n; tb += puentes; tt += n - puentes
    print("| `%s` | %s | %d | %d | **%d** | %s |"
          % (nid, linea, n, n - puentes, puentes,
             ("%.2f" % (puentes * 100.0 / n)).replace(".", ",")))
print("| **TOTAL del tramo** | | **%d** | **%d** | **%d** | **%s** |"
      % (tp, tt, tb, ("%.2f" % (tb * 100.0 / tp)).replace(".", ",")))
