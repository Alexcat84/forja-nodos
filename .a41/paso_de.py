# -*- coding: utf-8 -*-
import json, io, sys
idn, n = sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else None
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    if not l.strip(): continue
    d = json.loads(l)
    if d['id'] != idn: continue
    ps = d.get('pasos_accionables', [])
    print('%s  (%d pasos)' % (idn, len(ps)))
    for i, p in enumerate(ps, 1):
        if n is None or i == n:
            print('  %2d. %s' % (i, p))
