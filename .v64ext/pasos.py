# -*- coding: utf-8 -*-
"""Imprime titulo, sede y pasos numerados de las fichas pedidas, del grafo o de las bandejas."""
import glob, io, json, sys
grafo = dict((json.loads(l)['id'], json.loads(l)) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip())
for i in sys.argv[1:]:
    if i in grafo:
        d, sede = grafo[i], 'grafo'
    else:
        r = [p for p in glob.glob('cuarentena/*/%s.json' % i) if '_insertados' not in p]
        d, sede = json.load(io.open(r[0], encoding='utf-8')), r[0]
    print('=== %s  [%s]' % (i, sede))
    print('TITULO: %s' % d.get('titulo'))
    for k, p in enumerate(d.get('pasos_accionables') or [], 1):
        print('  %d. %s' % (k, p))
