# -*- coding: utf-8 -*-
"""EL DISCUTIBLE AUTOESCRITO DE CADA UNA DE LAS TRES FICHAS DE cap_17.

El reporte de la `61` dice que las tres traen el mismo, el de fundir los TRES.
Esto mide de cuantos habla cada una.
"""
import io
import json
import re

FICHAS = [
    'priorizar_lista_entrenamiento_subordinados',
    'desarrollar_primer_curso_entrenamiento',
    'pedir_critica_anonima_curso_entrenamiento_dictado',
]
for i in FICHAS:
    d = json.load(io.open('cuarentena/grove_high_output/%s.json' % i,
                          encoding='utf-8'))
    r = d['resumen_teorico']
    m = re.search(r'podria fundir[^.;]*', r)
    frase = m.group(0) if m else '(sin la frase)'
    cuantos = 'TRES' if ' los tres ' in frase else 'DOS'
    print('  %-14s: "...%s"  -> %s' % (i.split('_')[0], frase.strip(), cuantos))
