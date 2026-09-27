# -*- coding: utf-8 -*-
"""EL SALDO DE MIS INFORMES DE UN CANDIDATO, CONTADO DE SUS FICHEROS.

No es el informe de lote (D.42, lo corre el arnes y esta corrida no lo trae).
Es la cuenta de los informes de UN candidato que yo si corri, uno por cada
candidato escrito o corregido, en el mismo acto (EXTRACTOR.md 16).
"""
import glob
import io
import os
import re

CARPETA = '.aduana_v23'
GRUPO = [
    ('la cola de siete (TAREA 1)', [
        'desplegar_tres_conversaciones_carrera',
        'debatir_decidir_asuntos_cultura_evitar_delegar',
        'leer_seniales_fallo_jefe_reunion_solas',
        'montar_reuniones_solas_mentalidad_frecuencia',
        'pelear_proliferacion_reuniones_bloquear_ejecucion',
        'preguntar_seguimiento_hallar_huecos',
    ]),
    ('cap_12', [
        'desplegar_plan_orden_operaciones_franqueza_radical',
        'contar_historias_propias_explicar_franqueza_radical',
    ]),
    ('cap_13', [
        'mejorar_consciencia_propia_relacional_dos_practicas',
        'contar_cuatro_historias_propias_ver_hueco_intencion',
        'practicar_triangulo_critica_tres_papeles',
        'pedir_critica_primero_crear_seguridad_psicologica',
        'elegir_pregunta_recurrente_pedir_critica',
        'resolver_dudas_frecuentes_pedir_critica',
        'abrazar_incomodidad_silencio_contar_seis',
        'escuchar_entender_critica_dominar_defensa',
        'premiar_franqueza_hacer_escucha_tangible',
        'integrar_peticion_critica_rutina_existente',
        'dar_elogio_disciplina_igual_critica',
        'medir_critica_respuesta_oyente_brujula',
    ]),
]

VEREDICTO = re.compile(r'^\[(ENTRARIA|BLOQUEARIA|CAERIA)\]', re.M)
VECINO = re.compile(r'^    vecino (\S+)\s+\[levantada por: (\S+)\]', re.M)
POBLACION = re.compile(r'poblacion del barrido\s*:\s*(\d+)\s*\((\d+) del grafo mas (\d+)')


def lee(ident):
    ruta = os.path.join(CARPETA, ident + '.txt')
    if not os.path.exists(ruta):
        return None
    return io.open(ruta, encoding='utf-8').read()


print('=' * 78)
print('1. EL SALDO DE MIS INFORMES DE UN CANDIDATO, POR GRUPO')
print('=' * 78)
print('| grupo | informes | `ENTRARIA` | `BLOQUEARIA` | `CAERIA` | vecinos levantados |')
print('|---|---:|---:|---:|---:|---:|')
tot = [0, 0, 0, 0, 0]
for rotulo, ids in GRUPO:
    fila = [0, 0, 0, 0, 0]
    for ident in ids:
        texto = lee(ident)
        if texto is None:
            continue
        fila[0] += 1
        v = VEREDICTO.search(texto)
        if v:
            fila[1 + ['ENTRARIA', 'BLOQUEARIA', 'CAERIA'].index(v.group(1))] += 1
        fila[4] += len(VECINO.findall(texto))
    print('| **%s** | %d | **%d** | **%d** | **%d** | %d |'
          % (rotulo, fila[0], fila[1], fila[2], fila[3], fila[4]))
    tot = [a + b for a, b in zip(tot, fila)]
print('| **los tres grupos** | **%d** | **%d** | **%d** | **%d** | **%d** |'
      % (tot[0], tot[1], tot[2], tot[3], tot[4]))

print('')
print('=' * 78)
print('2. LA POBLACION DEL BARRIDO, CON SU REPARTO (D.38.5)')
print('=' * 78)
print('| informe | poblacion | del grafo | de bandejas |')
print('|---|---:|---:|---:|')
primero = None
ultimo = None
for _rotulo, ids in GRUPO:
    for ident in ids:
        texto = lee(ident)
        if texto is None:
            continue
        m = POBLACION.search(texto)
        if not m:
            continue
        if primero is None:
            primero = (ident, m.groups())
        ultimo = (ident, m.groups())
for rotulo, dato in (('el primero de la vuelta', primero), ('el ultimo de la vuelta', ultimo)):
    if dato:
        print('| %s, `%s` | **%s** | %s | %s |'
              % (rotulo, dato[0], dato[1][0], dato[1][1], dato[1][2]))

print('')
print('=' * 78)
print('3. LOS PARES LEVANTADOS, UNO POR FILA, CON LA SENIAL QUE LOS LEVANTO')
print('=' * 78)
print('| candidato | vecino | senial |')
print('|---|---|---|')
pares = 0
for _rotulo, ids in GRUPO:
    for ident in ids:
        texto = lee(ident)
        if texto is None:
            continue
        for vecino, senial in VECINO.findall(texto):
            pares += 1
            print('| `%s` | `%s` | `%s` |' % (ident, vecino, senial))
print('| | **%d pares levantados** | |' % pares)

print('')
print('=' * 78)
print('4. LOS FICHEROS QUE ESTA TABLA CUENTA')
print('=' * 78)
print('ficheros en %s : %d' % (CARPETA, len(glob.glob(os.path.join(CARPETA, '*.txt')))))
