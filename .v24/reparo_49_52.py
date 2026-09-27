# -*- coding: utf-8 -*-
"""EL REPARO DE LAS ARISTAS 49 A 52: POR QUE ESE HIJO Y NO OTRO DE SU FAMILIA.

La ACTA 23 adjudica que las cuatro se sostienen y que el dia del cableado cada
una lleva escrito por que ESE hijo. La tabla se imprime del fichero: para cada
arista, el hijo elegido y sus rivales de familia, con la unidad de origen y la
condicion de activacion de cada uno, que es lo que decide.
"""
import io
import json
import os
import re

BANDEJA = 'cuarentena/scott_radical_candor'
MADRE = 'pedir_critica_primero_crear_seguridad_psicologica'

# (numero, paso de la madre, hijo elegido, rivales de la misma familia)
CASOS = [
    (49, 2, 'dar_elogio_disciplina_igual_critica',
     ['elogiar_trabajo_especifico_contexto', 'equilibrar_elogio_critica_equipo',
      'elogiar_publico_criticar_privado_sus_tres_matices']),
    (50, 3, 'criticar_trabajo_evitar_desanimo',
     ['dar_critica_inmediata_ayuda_tangible', 'elogiar_publico_criticar_privado_sus_tres_matices']),
    (51, 4, 'medir_critica_respuesta_oyente_brujula',
     ['medir_guia_propia_pegatinas_marco']),
    (52, 5, 'fomentar_guia_reciproca_companieros',
     ['pedir_critica_equipo_premiarla']),
]


def cargar(identificador):
    return json.load(io.open(os.path.join(BANDEJA, identificador + '.json'),
                             encoding='utf-8'))


def unidad(nodo):
    caps = sorted(set(re.findall(r'(cap_\d+)\.md', nodo.get('resumen_teorico', ''))))
    return ', '.join(caps) if caps else '(sin unidad declarada)'


madre = cargar(MADRE)

print('| # | `--paso` | el paso de la madre, impreso | el hijo elegido | unidad | pasos |')
print('|---:|---:|---|---|---|---:|')
for numero, paso, hijo_id, _rivales in CASOS:
    hijo = cargar(hijo_id)
    print('| %d | **%d** | `%s` | `%s` | `%s` | **%d** |'
          % (numero, paso, madre['pasos_accionables'][paso - 1], hijo_id,
             unidad(hijo), len(hijo['pasos_accionables'])))

print('')
print('| # | quien compite por esa etapa | unidad | pasos | su condicion de activacion, impresa del fichero |')
print('|---:|---|---|---:|---|')
for numero, _paso, hijo_id, rivales in CASOS:
    for identificador in [hijo_id] + rivales:
        nodo = cargar(identificador)
        marca = 'ELEGIDO' if identificador == hijo_id else 'rival'
        print('| %d | **%s** `%s` | `%s` | **%d** | %s |'
              % (numero, marca, identificador, unidad(nodo),
                 len(nodo['pasos_accionables']), nodo['condiciones_activacion']))
