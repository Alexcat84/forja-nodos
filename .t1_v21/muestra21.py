# -*- coding: utf-8 -*-
"""MUESTRA SEMBRADA DE LOS 194 PASOS, PARA RELEERLA A MANO CONTRA SU LINEA.

La ACTA 20 6.1 releyo 12 de 95 con semilla escrita `1221`, *elegida al azar y no a
ojo*, y dijo por que: una muestra elegida a ojo se elige entre los pasos de los que
uno esta seguro. **La semilla de hoy es `2110` y va escrita aqui antes de ver el
resultado**, que es lo unico que hace la muestra ciega.

El guion NO juzga: imprime el paso y el tramo de lineas donde tiene que estar, y la
lectura la hago yo y la escribo en el reporte.
"""
import json
import random

SEMILLA = 2110
CUANTOS = 15

TRECE = [
    ("P7",         47,  59, "conversar_historia_vida_descubrir_motivadores"),
    ("P8",         61,  75, "conversar_suenios_cruzar_habilidades"),
    ("P9",         77,  87, "trazar_plan_dieciocho_meses_aprendizaje"),
    ("P13 a P17",  97, 125, "armar_plan_anual_crecimiento_equipo"),
    ("P19 y P21", 129, 163, "montar_proceso_contratacion_reducir_sesgo"),
    ("P24",       169, 173, "facilitar_despido_tres_cosas"),
    ("P25",       175, 179, "admitir_pronto_mal_desempenio_cuatro_razones"),
    ("P26",       181, 187, "calibrar_decision_despido_documentarla"),
    ("P27",       189, 195, "sopesar_consejo_legal_despedir_humildad"),
    ("P28",       197, 201, "contactar_despedido_mes_despues"),
    ("P30",       205, 223, "calibrar_ascensos_evitar_politica"),
    ("P33",       229, 237, "evitar_obsesion_ascenso_estatus"),
    ("P34 a P36", 239, 251, "reconocer_excelencia_trayectoria_gradual"),
]

todos = []
for pieza, a, b, ident in TRECE:
    d = json.load(open('cuarentena/scott_radical_candor/%s.json' % ident,
                       encoding='utf-8'))
    for j, paso in enumerate(d['pasos_accionables'], 1):
        todos.append((pieza, ident, a, b, j, paso))

print('poblacion de pasos : %d' % len(todos))
print('semilla escrita    : %d' % SEMILLA)
print('tamanio de muestra : %d' % CUANTOS)
print('')
random.seed(SEMILLA)
for pieza, ident, a, b, j, paso in sorted(random.sample(todos, CUANTOS)):
    print('%-12s %-46s paso %2d   tramo L%d a L%d' % (pieza, ident, j, a, b))
    print('   %s' % paso[:300])
    print('')
