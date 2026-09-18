# -*- coding: utf-8 -*-
import json, io, sys
lineas = [l for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip()]
for n in [int(x) for x in sys.argv[1:]]:
    d = json.loads(lineas[n-1])
    print('--- linea %d ---' % n)
    for k in ('vuelta','fecha','tipo','clase','veredicto','par','a','b','nodo','contra','razon','arista','paso','cita'):
        if k in d:
            print('  %-10s %s' % (k, json.dumps(d[k], ensure_ascii=False)))
    faltan = [k for k in d if k not in ('vuelta','fecha','tipo','clase','veredicto','par','a','b','nodo','contra','razon','arista','paso','cita')]
    if faltan:
        print('  (otras claves: %s)' % faltan)
