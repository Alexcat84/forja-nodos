# -*- coding: utf-8 -*-
# PRIMERA LINEA, D.40 HEREDADO 4: CERO IDS TECLEADOS. Recorro carpetas y el
# dataset entero; lo unico literal es la FORMULA de redaccion que estoy midiendo,
# que no es un id ni una lista de nodos.
import io, json, os, re, sys

FORMULA = re.compile(r'lo que el texto dice que', re.IGNORECASE)

def pasos_de(d):
    return d.get('pasos_accionables') or []

fuentes = []
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    if l.strip(): fuentes.append(('grafo', json.loads(l)))
bandejas = 0
for libro in sorted(os.listdir('cuarentena')):
    d = os.path.join('cuarentena', libro)
    if not os.path.isdir(d) or libro.startswith('_') or libro.startswith('ensayo'): continue
    n = 0
    for f in sorted(os.listdir(d)):
        if f.endswith('.json'):
            fuentes.append(('bandeja:' + libro, json.load(io.open(os.path.join(d, f), encoding='utf-8'))))
            n += 1
    if n: print('  bandeja %-28s %d' % (libro, n)); bandejas += n
print('poblacion: %d del grafo mas %d en bandejas = %d'
      % (sum(1 for o, _ in fuentes if o == 'grafo'), bandejas, len(fuentes)))

tot = con = 0
nodos_con = 0
for origen, d in fuentes:
    hay = 0
    for p in pasos_de(d):
        tot += 1
        if FORMULA.search(p): con += 1; hay += 1
    if hay: nodos_con += 1
print('pasos en la poblacion                       : %d' % tot)
print('pasos que llevan la formula "lo que el texto dice que": %d' % con)
print('nodos que la usan al menos una vez          : %d de %d' % (nodos_con, len(fuentes)))
