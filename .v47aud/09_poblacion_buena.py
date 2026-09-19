# -*- coding: utf-8 -*-
"""LA POBLACION BUENA, con la adjudicacion de mi ACTA 45 45.5.a aplicada:
una bandeja solo cuenta si su clave de fuente esta en la tabla canonica
(src/aduana.py:465, _fuentes_canonicas). Un ensayo no es un libro."""
import json, os, sys, io, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
tabla = json.load(open('fuentes/FUENTES_CANONICAS.json', encoding='utf-8'))
canon = set(k for k in tabla if not k.startswith('_'))
grafo = [json.loads(l) for l in open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
pobl = list(grafo)
print('grafo                                : %4d' % len(grafo))
for d in sorted(os.listdir('cuarentena')):
    p = os.path.join('cuarentena', d)
    if not os.path.isdir(p) or d in ('_insertados', '_derivadas'):
        continue
    dentro = fuera = 0
    for f in glob.glob(os.path.join(p, '*.json')):
        c = json.load(open(f, encoding='utf-8'))
        claves = [x.get('clave') for x in (c.get('fuentes') or [])]
        if claves and all(k in canon for k in claves):
            pobl.append(c); dentro += 1
        else:
            fuera += 1
    if dentro or fuera:
        print('bandeja %-26s: %4d cuentan, %4d fuera de la tabla canonica' % (d, dentro, fuera))
print('-' * 62)
print('POBLACION DEL BARRIDO, la buena      : %4d' % len(pobl))
json.dump([{'id': c.get('id'), 'titulo': c.get('titulo'),
            'pasos': c.get('pasos_accionables', []),
            'resumen': c.get('resumen_teorico', '')} for c in pobl],
          open('.v47aud/09_poblacion.json', 'w', encoding='utf-8'), ensure_ascii=False)
