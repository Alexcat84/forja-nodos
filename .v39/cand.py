# -*- coding: utf-8 -*-
import json, os, sys
for cid in sys.argv[1:]:
    d = json.load(open('cuarentena/scott_radical_candor/%s.json' % cid, encoding='utf-8'))
    print('=== %s ===' % cid)
    print('titulo: %s' % d['titulo'])
    print('activacion: %s' % d['condiciones_activacion'])
    print('entregable: %s' % d['entregable_esperado'])
    for i, p in enumerate(d['pasos_accionables'], 1):
        print('  P%02d: %s' % (i, p))
    print('  resumen: %s' % d['resumen_teorico'])
    print()
