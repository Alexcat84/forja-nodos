# -*- coding: utf-8 -*-
import json, io, sys
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    if not l.strip(): continue
    d = json.loads(l)
    if d['id'] in sys.argv[1:]:
        print('%s' % d['id'])
        print('  entregable: %s' % (d.get('entregable_esperado') or '(ninguno)'))
