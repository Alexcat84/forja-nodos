# -*- coding: utf-8 -*-
# Vuelca los candidatos de la bandeja en texto plano legible, uno por uno.
import io, json, glob, os, sys

carpeta = 'cuarentena/grove_high_output'
desde = int(sys.argv[1]) if len(sys.argv) > 1 else 0
hasta = int(sys.argv[2]) if len(sys.argv) > 2 else 99
campos = sys.argv[3] if len(sys.argv) > 3 else 'todo'

rutas = sorted(glob.glob(carpeta + '/*.json'), key=os.path.getmtime)
for i, p in enumerate(rutas):
    if not (desde <= i < hasta):
        continue
    d = json.load(io.open(p, encoding='utf-8'))
    print('=' * 78)
    print('[%02d] %s' % (i, d['id']))
    print('titulo : %s' % d.get('titulo', ''))
    print('dominio: %s   |  fuentes: %s'
          % (d.get('dominio'), [f.get('clave') for f in d.get('fuentes', [])]))
    if campos == 'todo':
        print('activacion : %s' % d.get('condiciones_activacion', ''))
        print('entregable : %s' % d.get('entregable_esperado', ''))
        print('escala_min : %s' % d.get('escala_minima', ''))
    print('PASOS (%d):' % len(d.get('pasos_accionables', [])))
    for n, s in enumerate(d.get('pasos_accionables', []), 1):
        print('  %2d. %s' % (n, s))
    if campos == 'todo':
        print('RESUMEN_TEORICO:')
        print(d.get('resumen_teorico', ''))
    print()
