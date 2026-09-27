# -*- coding: utf-8 -*-
"""LOS OCHO PASOS DE LA VUELTA 4, CONTRA LA LINEA DEL LIBRO QUE CADA UNO CITA.

La cita que cada paso lleva detras de "El texto lo dice asi:" tiene que estar
LITERAL en alguna linea de su capitulo. Comillas tipograficas normalizadas y
espacios colapsados; nada mas se toca.
"""

import io
import json
import re

CAPITULO = {
    'eliminar_seguimiento_descendente_responsabilizar_dueno': 'cap_09',
    'acoger_inspectores_externos_fuente_aprendizaje': 'cap_10',
    'tomar_accion_deliberada_pausar_vocalizar_gesticular': 'cap_11',
}


def normal(texto):
    texto = (texto.replace(u'“', '"').replace(u'”', '"')
             .replace(u'‘', "'").replace(u'’', "'"))
    return re.sub(r'\s+', ' ', texto).strip()


def main():
    total = 0
    sin_sustento = 0
    for nodo in sorted(CAPITULO):
        cap = CAPITULO[nodo]
        fuente = [normal(l) for l in io.open(
            'fuentes/marquet_turn_the_ship/%s.md' % cap, encoding='utf-8'
        ).read().splitlines()]
        ficha = json.load(io.open(
            'cuarentena/marquet_turn_the_ship/%s.json' % nodo, encoding='utf-8'))
        for orden, paso in enumerate(ficha['pasos_accionables'], 1):
            total += 1
            partes = re.split(r'El texto lo dice asi:', paso)
            if len(partes) < 2:
                print('%-12s P%d  SIN CITA' % (cap, orden))
                sin_sustento += 1
                continue
            cita = normal(partes[1]).rstrip('.')
            donde = [n + 1 for n, linea in enumerate(fuente) if cita in linea]
            print('%-12s P%d  cita literal en lineas %s  %s'
                  % (cap, orden, donde or 'NINGUNA', '' if donde else '<-- PUENTE'))
            if not donde:
                sin_sustento += 1
    print('TOTAL pasos: %d   sin sustento literal: %d' % (total, sin_sustento))


main()
