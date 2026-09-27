# -*- coding: utf-8 -*-
"""LAS TRES ESPECIES DE PUENTE DEL LOTE 1, BUSCADAS UNA A UNA EN LOS 194 PASOS.

`EXTRACTOR.md` 15.4 las nombra: **el destinatario**, **el periodo** y **el
responsable**. Son las tres que el lote 1 pago con una vuelta entera de reparacion,
y son las que se vuelven a escribir sin darse cuenta.

Igual que `cuentas21.py`, ESTE NO DECIDE: LISTA. Saca todo paso que contenga una
marca de plazo, de destinatario o de responsable, y yo lo releo contra su linea. La
marca que el libro escribe se queda; la que escribi yo, se retira.
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

MARCAS = {
    'PERIODO': ['cada cuanto', 'cada anio', 'una vez al anio', 'al anio',
                'cada mes', 'cada semana', 'cada trimestre', 'periodicamente',
                'plazo', 'para cuando', 'antes de que acabe', 'cada dia',
                'dos veces al anio', 'un mes despues', 'al mes'],
    'DESTINATARIO': ['traslada', 'eleva a', 'remite a', 'comunicalo a',
                     'informa a', 'reporta a', 'manda a', 'envia a'],
    'RESPONSABLE': ['escribe quien responde', 'designa a', 'nombra responsable',
                    'asigna la responsabilidad', 'quien responde de'],
}

n = 0
for pieza, _a, _b, ident in TRECE:
    d = json.load(open('cuarentena/scott_radical_candor/%s.json' % ident,
                       encoding='utf-8'))
    for j, paso in enumerate(d['pasos_accionables'], 1):
        bajo = paso.lower()
        for especie, marcas in sorted(MARCAS.items()):
            for marca in marcas:
                if marca in bajo:
                    n += 1
                    k = bajo.index(marca)
                    print('%-12s %-46s paso %2d  [%s: %s]'
                          % (pieza, ident, j, especie, marca))
                    print('     ...%s...' % paso[max(0, k - 40):k + len(marca) + 55])
print('')
print('marcas de las tres especies encontradas en los 194 pasos: %d' % n)
