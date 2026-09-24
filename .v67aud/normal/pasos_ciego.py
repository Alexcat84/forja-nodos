# -*- coding: utf-8 -*-
"""COPIA DEL AUDITOR (ACTA 66, remedio R6) de .v64aud/pasos.py para la FASE CIEGA: imprime titulo, fuente, condicion y
pasos de cada id, buscandolo en el grafo y en las bandejas (D.38.4), y NO imprime previos ni siguientes, que en una
vuelta de insercion ensenian las aristas que el extractor cableo (APERTURA_CIEGA.md de la 67, seccion 1)."""
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
    print('  fuente:', [f.get('clave') for f in d.get('fuentes', [])])
    print('  cond:', d.get('condiciones_activacion'))
    for n, p in enumerate(d.get('pasos_accionables', []), 1): print('  P%d. %s' % (n, p))
