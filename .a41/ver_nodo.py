# -*- coding: utf-8 -*-
import json, io, sys
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    if not l.strip(): continue
    d = json.loads(l)
    if d['id'] == sys.argv[1]:
        print('id            : %s' % d['id'])
        print('nodos_previos : %s' % json.dumps(d.get('nodos_previos'), ensure_ascii=False))
        print('nodos_siguient: %s' % json.dumps(d.get('nodos_siguientes'), ensure_ascii=False))
        print('claves        : %s' % sorted(d.keys()))
