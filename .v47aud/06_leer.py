# -*- coding: utf-8 -*-
"""Vuelca UN candidato entero, campo a campo, sin recortar. Es el fichero que leo."""
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
d = json.load(open(sys.argv[1], encoding='utf-8'))
for k in ['id','titulo','dominio','estado','resumen_teorico','condiciones_activacion',
          'entregable_esperado','atribuciones','denominaciones','ids_alias',
          'nodos_previos','nodos_siguientes','fuentes']:
    v = d.get(k)
    print('--- %s ---' % k.upper())
    print(json.dumps(v, ensure_ascii=False, indent=2) if not isinstance(v,str) else v)
print('--- PASOS_ACCIONABLES (%d) ---' % len(d.get('pasos_accionables',[])))
for i,p in enumerate(d.get('pasos_accionables',[]),1):
    print('%2d. %s' % (i, json.dumps(p, ensure_ascii=False) if not isinstance(p,str) else p))
