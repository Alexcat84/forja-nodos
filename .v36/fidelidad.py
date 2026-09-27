# -*- coding: utf-8 -*-
"""PASOS INVENTADOS de cap_10 (D.30). La cuenta de pasos se lee del fichero; la
columna PUENTE es el veredicto de la relectura, uno por paso, contra su linea."""
import json

TRAMO = [
    ("desplegar_tres_conversaciones_carrera",        "L19,L21,L43,L91", 0),
    ("conversar_historia_vida_descubrir_motivadores", "L47-L59",  0),
    ("conversar_suenios_cruzar_habilidades",          "L61-L75",  0),
    ("trazar_plan_dieciocho_meses_aprendizaje",       "L77-L87",  0),
    ("armar_plan_anual_crecimiento_equipo",           "L93-L125", 0),
    ("montar_proceso_contratacion_reducir_sesgo",     "L129-L163", 0),
    ("facilitar_despido_tres_cosas",                  "L169-L173", 0),
    ("admitir_pronto_mal_desempenio_cuatro_razones",  "L175-L179", 0),
    ("calibrar_decision_despido_documentarla",        "L181-L187", 0),
    ("sopesar_consejo_legal_despedir_humildad",       "L189-L195", 0),
    ("contactar_despedido_mes_despues",               "L197-L201", 0),
    ("calibrar_ascensos_evitar_politica",             "L205-L223", 0),
    ("evitar_obsesion_ascenso_estatus",               "L229-L237", 0),
    ("reconocer_excelencia_trayectoria_gradual",      "L239-L251", 0),
]

print("| unidad | lineas | pasos | TRANSCRIPCION | PUENTE | por ciento |")
print("|---|---:|---:|---:|---:|---:|")
tp = tt = tb = 0
for nid, linea, puentes in TRAMO:
    d = json.load(open("cuarentena/scott_radical_candor/%s.json" % nid, encoding="utf-8"))
    n = len(d["pasos_accionables"])
    tp += n; tb += puentes; tt += n - puentes
    print("| `%s` | %s | %d | %d | **%d** | %s |"
          % (nid, linea, n, n - puentes, puentes,
             ("%.2f" % (puentes * 100.0 / n)).replace(".", ",")))
print("| **TOTAL de `cap_10`** | | **%d** | **%d** | **%d** | **%s** |"
      % (tp, tt, tb, ("%.2f" % (tb * 100.0 / tp)).replace(".", ",")))
