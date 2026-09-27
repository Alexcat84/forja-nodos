# -*- coding: utf-8 -*-
"""LAS ARISTAS NUEVAS DE LA VUELTA 23, CON EL PASO DE LA MADRE IMPRESO DEL FICHERO.

D.37 manda que el auditor pueda abrir el paso n de la madre y comprobar que ahi
se nombra al hijo. Una arista sin su linea es una afirmacion sin cita, asi que
la cita se imprime, no se teclea.
"""
import io
import json
import os

C = 'cuarentena/scott_radical_candor'
NUEVAS = [
    (38, 'desplegar_plan_orden_operaciones_franqueza_radical', 'contar_historias_propias_explicar_franqueza_radical', 4, 'D.29'),
    (39, 'desplegar_plan_orden_operaciones_franqueza_radical', 'desplegar_tres_conversaciones_carrera', 12, 'D.29'),
    (40, 'desplegar_plan_orden_operaciones_franqueza_radical', 'bloquear_tiempo_pensar_calendario', 30, 'D.29'),
    (41, 'desplegar_plan_orden_operaciones_franqueza_radical', 'armar_plan_anual_crecimiento_equipo', 32, 'D.29'),
    (42, 'contar_historias_propias_explicar_franqueza_radical', 'contar_cuatro_historias_propias_ver_hueco_intencion', 4, 'D.29'),
    (43, 'mejorar_consciencia_propia_relacional_dos_practicas', 'contar_cuatro_historias_propias_ver_hueco_intencion', 11, 'D.37'),
    (44, 'mejorar_consciencia_propia_relacional_dos_practicas', 'practicar_triangulo_critica_tres_papeles', 12, 'D.37'),
    (45, 'pedir_critica_primero_crear_seguridad_psicologica', 'elegir_pregunta_recurrente_pedir_critica', 17, 'D.37'),
    (46, 'pedir_critica_primero_crear_seguridad_psicologica', 'abrazar_incomodidad_silencio_contar_seis', 17, 'D.37'),
    (47, 'pedir_critica_primero_crear_seguridad_psicologica', 'escuchar_entender_critica_dominar_defensa', 17, 'D.37'),
    (48, 'pedir_critica_primero_crear_seguridad_psicologica', 'premiar_franqueza_hacer_escucha_tangible', 17, 'D.37'),
    (49, 'pedir_critica_primero_crear_seguridad_psicologica', 'dar_elogio_disciplina_igual_critica', 2, 'D.29'),
    (50, 'pedir_critica_primero_crear_seguridad_psicologica', 'criticar_trabajo_evitar_desanimo', 3, 'D.29'),
    (51, 'pedir_critica_primero_crear_seguridad_psicologica', 'medir_critica_respuesta_oyente_brujula', 4, 'D.29'),
    (52, 'pedir_critica_primero_crear_seguridad_psicologica', 'fomentar_guia_reciproca_companieros', 5, 'D.29'),
    # LA 53 NO ESTABA EN LA PRIMERA LISTA: la levanto el informe de un candidato de
    # medir_critica (paso contra nodo 0,723), la lei y la anado con su correccion declarada.
    (53, 'desplegar_marco_franqueza_radical', 'medir_critica_respuesta_oyente_brujula', 6, 'D.29'),
]


def paso(ident, n):
    d = json.load(io.open(os.path.join(C, ident + '.json'), encoding='utf-8'))
    return d['pasos_accionables'][n - 1], len(d['pasos_accionables'])


print('=' * 78)
print('1. LAS DIECISEIS ARISTAS NUEVAS, CON SU PASO DE MADRE IMPRESO Y SU HIJO CONTADO')
print('=' * 78)
print('| # | madre | hijo | `--paso` | especie | el paso de la madre, impreso del fichero | pasos del hijo |')
print('|---:|---|---|---:|---|---|---:|')
for num, madre, hijo, n, especie in NUEVAS:
    texto, _ = paso(madre, n)
    _, cuantos = paso(hijo, 1)
    print('| %d | `%s` | `%s` | **%d** | `%s` | `%s` | **%d** |'
          % (num, madre, hijo, n, especie, texto, cuantos))
print('| | | **%d aristas nuevas** | | | | |' % len(NUEVAS))

print('')
print('=' * 78)
print('2. LA COMPROBACION QUE D.37 PIDE: LOS DOS EXTREMOS EXISTEN COMO FICHERO')
print('=' * 78)
faltan = 0
for num, madre, hijo, n, _e in NUEVAS:
    for ident in (madre, hijo):
        if not os.path.exists(os.path.join(C, ident + '.json')):
            faltan += 1
            print('FALTA %s' % ident)
print('extremos comprobados : %d' % (len(NUEVAS) * 2))
print('extremos que faltan  : %d' % faltan)
