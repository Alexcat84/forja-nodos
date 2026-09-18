# -*- coding: utf-8 -*-
"""Contador de pasos y lector de capitulo de los 20 candidatos de la bandeja
tal como estaban al abrir la vuelta 42 (commit 671b6f3). Instrumento del
auditor: no toca el arbol, solo lee."""
import json, glob, io, re, os, sys
sys.path.insert(0, os.getcwd())
grafo = set()
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    if l.strip():
        grafo.add(json.loads(l)['id'])
print('%-55s %-8s %5s %5s %s' % ('id', 'cap', 'pasos', 'prev', 'en grafo'))
tot = 0
for f in sorted(glob.glob('.a41/bandeja/*.json')):
    d = json.load(io.open(f, encoding='utf-8'))
    r = d.get('resumen_teorico', '') + ' ' + json.dumps(d.get('medida_en', ''), ensure_ascii=False)
    caps = sorted(set(re.findall(r'cap_\d\d', r)))
    n = len(d.get('pasos_accionables', []))
    tot += n
    prev = len(d.get('nodos_previos', []) or [])
    print('%-55s %-8s %5d %5d %s' % (d['id'], ','.join(caps) or '?', n, prev,
                                      'SI' if d['id'] in grafo else 'NO'))
print()
print('CANDIDATOS: %d   PASOS ESCRITOS EN TOTAL: %d' % (len(glob.glob('.a41/bandeja/*.json')), tot))
