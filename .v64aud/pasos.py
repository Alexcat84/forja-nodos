# -*- coding: utf-8 -*-
"""Imprime titulo, condicion y pasos de cada id pedido, buscandolo en el grafo
y en las bandejas (D.38.4). Dice de donde lo saco."""
import io, json, glob, sys
def buscar(i):
    for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
        d = json.loads(l)
        if d['id'] == i: return 'grafo', d
    for f in glob.glob('cuarentena/*/%s.json' % i):
        if '_insertados' in f or '_derivadas' in f or 'ensayo_' in f: continue
        return f, json.load(io.open(f, encoding='utf-8'))
    return None, None
for i in sys.argv[1:]:
    sede, d = buscar(i)
    print('=====', i, '|', sede)
    if not d: continue
    print('  titulo:', d.get('titulo'))
    print('  fuente:', [f.get('clave') for f in d.get('fuentes', [])], '| previos:', d.get('nodos_previos'), '| siguientes:', d.get('nodos_siguientes'))
    print('  cond:', d.get('condiciones_activacion'))
    for n, p in enumerate(d.get('pasos_accionables', []), 1): print('  P%d. %s' % (n, p))
