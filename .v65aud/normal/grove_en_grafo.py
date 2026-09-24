# ACTA 64: la fila de los tres libros que faltan en el TABLERO (arbol de trabajo) contra el grafo, _insertados y la bandeja
import json, glob
from collections import Counter
for l in open('docs/loop/TABLERO.jsonl', encoding='utf-8'):
    d = json.loads(l)
    if d.get('clave') in ('grove_high_output', 'gerber_emyth', 'marquet_turn_the_ship'):
        print('TABLERO', d['clave'], '| insertados', d['insertados'], '| nodos_en_grafo', d['nodos_en_grafo'], '| bandeja', d['candidatos_en_bandeja'])
c = Counter()
for l in open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l)
    for f in {f.get('clave') for f in d.get('fuentes', [])}: c[f] += 1
for k in ('grove_high_output', 'gerber_emyth', 'marquet_turn_the_ship'):
    print('MEDIDO ', k, '| nodos del grafo con esa fuente', c[k], '| en _insertados', len(glob.glob('cuarentena/_insertados/%s/*.json' % k)), '| en bandeja', len(glob.glob('cuarentena/%s/*.json' % k)))
