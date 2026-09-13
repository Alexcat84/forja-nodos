# -*- coding: utf-8 -*-
"""TODA CUENTA QUE MIS PASOS ATRIBUYEN AL LIBRO, LISTADA PARA RELEERLA A MANO.

POR QUE EXISTE ESTE GUION Y NO BASTA `cifras21.py`. La vuelta 20 se cazo a si
misma un puente de esta especie exacta (ACTA 20 1.4): *mi P16 decia la diferencia
que el texto pone entre LAS DOS MANERAS de compadecerse, y el texto NO da esa
cuenta*. `cifras21.py` no lo caza siempre, porque busca el numeral en el tramo
entero y el tramo puede traer ese mismo numero por otra razon: si el libro dice
`three to five columns`, mi `las tres preguntas` pasa sin que nadie las compare.

ASI QUE ESTE NO DECIDE NADA: LISTA. Saca toda ocurrencia de un numeral en los 194
pasos con su frase alrededor, y yo las releo una a una contra la linea. La cuenta
que el libro escribe se queda; la que escribo yo y le atribuyo a el, se retira.
"""
import json
import re

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

# Solo los numerales que CUENTAN COSAS. `un` y `una` quedan fuera a proposito y
# lo digo: en castellano son articulo indeterminado mucho mas a menudo que
# numeral, y meterlos llena la lista de falsos positivos como `una relacion`.
CUENTAS = ['dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve',
           'diez', 'once', 'doce', 'quince', 'veinte', 'treinta', 'cuarenta',
           'cincuenta', 'cien', 'ambas', 'ambos', 'sendas']

n = 0
for pieza, _a, _b, ident in TRECE:
    d = json.load(open('cuarentena/scott_radical_candor/%s.json' % ident,
                       encoding='utf-8'))
    for j, paso in enumerate(d['pasos_accionables'], 1):
        for pal in CUENTAS:
            for m in re.finditer(r'\b' + pal + r'\b', paso.lower()):
                n += 1
                ini = max(0, m.start() - 45)
                fin = min(len(paso), m.end() + 60)
                print('%-11s %-46s paso %2d  [%s]  ...%s...'
                      % (pieza, ident, j, pal, paso[ini:fin]))
print('')
print('ocurrencias de numeral que cuentan cosas, en los 194 pasos: %d' % n)
