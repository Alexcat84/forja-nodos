# -*- coding: utf-8 -*-
"""LA SENIAL DE LA ADUANA ES PAR A PAR, Y AQUI SE MIDE CON LAS DOS VERSIONES.

Mide los dos pares que deciden M5.8 y M5.9 con la ficha de `declarar_intencion`
de HOY y con la de `git show 34aed47:...`, en la MISMA corrida y con la MISMA
poblacion. Si las cifras se mueven, lo que las mueve es el texto.
"""

import json
import subprocess
import sys

sys.path.insert(0, '.')

from src import aduana, comun
from src import config as modulo_config

DIR = 'cuarentena/marquet_turn_the_ship/'
VIEJA = '34aed47:cuarentena/marquet_turn_the_ship/declarar_intencion_reemplazar_peticion_permiso.json'


def de_ruta(nombre):
    candidato, _avisos = aduana.normalizar_candidato(
        comun.leer_json(DIR + nombre + '.json'), None)
    return candidato


def de_git(referencia):
    bruto = subprocess.check_output(['git', 'show', referencia]).decode('utf-8')
    candidato, _avisos = aduana.normalizar_candidato(json.loads(bruto), None)
    return candidato


def main():
    umbrales = modulo_config.cargar()
    hoy = de_ruta('declarar_intencion_reemplazar_peticion_permiso')
    antes = de_git(VIEJA)
    resistir = de_ruta('resistir_dar_solucion_clasificar_decision_urgencia')
    eliminar = de_ruta('eliminar_seguimiento_descendente_responsabilizar_dueno')

    def texto(uno, otro):
        return aduana.medir(uno, otro, umbrales)['senales']['similitud_texto']

    print('umbral de similitud de esta corrida : %s' % umbrales['umbral_similitud_texto'])
    print('HOY   declarar_intencion x resistir : %s' % texto(hoy, resistir))
    print('ANTES declarar_intencion x resistir : %s' % texto(antes, resistir))
    print('HOY   eliminar x declarar_intencion : %s' % texto(eliminar, hoy))
    print('ANTES eliminar x declarar_intencion : %s' % texto(eliminar, antes))
    print('')
    print('LA POBLACION NO ENTRA: las cuatro cifras salen de la misma corrida,')
    print('con las mismas fichas cargadas, cambiando solo el texto de una de ellas.')


main()
