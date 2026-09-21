# -*- coding: utf-8 -*-
import json, io, sys
f = sys.argv[1]
d = json.load(io.open('.a41/bandeja/%s.json' % f, encoding='utf-8'))
print('ID      : %s' % d['id'])
print('TITULO  : %s' % d.get('titulo'))
print('RESUMEN : %s' % d.get('resumen_teorico'))
print('MEDIDA  : %s' % json.dumps(d.get('medida_en'), ensure_ascii=False))
print('PREVIOS : %s' % json.dumps(d.get('nodos_previos'), ensure_ascii=False))
print('PASOS (%d):' % len(d.get('pasos_accionables', [])))
for i, p in enumerate(d.get('pasos_accionables', []), 1):
    print('  %2d. %s' % (i, p))
