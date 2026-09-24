# -*- coding: utf-8 -*-
"""ACTA 65: los vecinos de bandeja del barrido del extractor de cap_04, por libro de la bandeja donde esperan."""
import json, glob, os, collections
libro = {}
for k in os.listdir('cuarentena'):
    if k.startswith('_') or not os.path.isdir(os.path.join('cuarentena', k)): continue
    for f in glob.glob(os.path.join('cuarentena', k, '*.json')): libro[os.path.basename(f)[:-5]] = k
c = collections.Counter()
for f in glob.glob('.v66ext/vecinos_*.json'):
    for v in json.load(open(f, encoding='utf-8'))['vecinos']:
        if v['sede'] == 'bandeja': c[libro.get(v['id'], '?')] += 1
print('vecinos de bandeja por libro:', dict(c))
