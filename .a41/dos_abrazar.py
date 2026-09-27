# -*- coding: utf-8 -*-
import json, io, re
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    if not l.strip(): continue
    d = json.loads(l)
    if not d['id'].startswith('abrazar_incomodidad'): continue
    r = d.get('resumen_teorico', '') or ''
    caps = sorted(set(re.findall(r'([a-z_]+)/(cap_\d\d)\.md', r)))
    print('id      : %s' % d['id'])
    print('titulo  : %s' % d.get('titulo'))
    print('fuente  : %s' % caps)
    print('pasos   : %d' % len(d.get('pasos_accionables', [])))
    print('siguient: %s' % json.dumps(d.get('nodos_siguientes'), ensure_ascii=False))
    print()
