# -*- coding: utf-8 -*-
"""LAS CUATRO ARISTAS DE LA TAREA 3, IMPRESAS DEL FICHERO Y NO TECLEADAS.

D.41 y EXTRACTOR.md 5: la tabla se imprime, no se teclea. Este instrumento abre
los ficheros de la madre y de los cuatro hijos, saca el paso de la madre que
nombra a cada hijo y cuenta los pasos del hijo. Si manana alguien mueve un paso,
la tabla cambia sola y el hook lo canta.
"""
import io
import json
import os

BANDEJA = 'cuarentena/scott_radical_candor'
MADRE = 'abrazar_incomodidad_arrancar_critica_equipo'

# (hijo, paso de la madre que lo nombra, el elemento que L237 nombra)
CABLES = [
    ('elegir_pregunta_recurrente_pedir_critica', 7, 'dar con una pregunta recurrente'),
    ('abrazar_incomodidad_silencio_contar_seis', 8, 'abrazar la incomodidad'),
    ('escuchar_entender_critica_dominar_defensa', 12, 'escuchar con intencion de entender'),
    ('premiar_franqueza_hacer_escucha_tangible', 14, 'hacer tangible la escucha premiando la franqueza'),
]


def cargar(identificador):
    ruta = os.path.join(BANDEJA, identificador + '.json')
    return json.load(io.open(ruta, encoding='utf-8'))


madre = cargar(MADRE)

print('| # | madre | hijo | `--paso` | especie | pasos del hijo | pasos de la madre |')
print('|---:|---|---|---:|---|---:|---:|')
for indice, (hijo_id, paso, _elemento) in enumerate(CABLES, start=54):
    hijo = cargar(hijo_id)
    print('| %d | `%s` | `%s` | **%d** | `D.29` | **%d** | **%d** |'
          % (indice, MADRE, hijo_id, paso,
             len(hijo['pasos_accionables']), len(madre['pasos_accionables'])))

print('')
print('| # | el elemento que `L237` nombra | el paso de la madre, impreso entero de su fichero |')
print('|---:|---|---|')
for indice, (hijo_id, paso, elemento) in enumerate(CABLES, start=54):
    texto = madre['pasos_accionables'][paso - 1]
    print('| %d | %s | `%s` |' % (indice, elemento, texto))
