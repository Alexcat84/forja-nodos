# -*- coding: utf-8 -*-
"""Pasos de cap_04 contados de las fichas, que es el denominador de toda la
fidelidad D.30 del capitulo. Sostiene el 47.8 de la ACTA 47."""
import json, glob, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
nuevos = {'usar_calendario_herramienta_planificacion_produccion',
          'decir_no_trabajo_excede_capacidad',
          'llevar_inventario_proyectos_discrecionales',
          'dimensionar_numero_subordinados_medio_dia_semanal',
          'buscar_regularidad_bloques_iguales_trabajo_mando'}
filas = []
for f in sorted(glob.glob('cuarentena/grove_high_output/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    if 'cap_04' not in d.get('resumen_teorico', ''): continue
    filas.append((len(d['pasos_accionables']), d['id'], d['id'] in nuevos))
for n, i, nu in sorted(filas, reverse=True):
    print('  %3d pasos  %-10s %s' % (n, 'NUEVO' if nu else 'ya estaba', i))
print()
print('fichas de cap_04           : %d' % len(filas))
print('pasos de los 5 de hoy      : %d' % sum(n for n, i, nu in filas if nu))
print('pasos de los 14 anteriores : %d' % sum(n for n, i, nu in filas if not nu))
print('pasos de cap_04 entero     : %d' % sum(n for n, i, nu in filas))
