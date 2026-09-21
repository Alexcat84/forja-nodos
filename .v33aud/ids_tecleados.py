# -*- coding: utf-8 -*-
# PRIMERA LINEA, D.40 HEREDADO 4: CERO IDS TECLEADOS AQUI. La nomina contra la
# que casa sale de dataset/nodos.jsonl y de cuarentena/, y los literales salen
# del propio fichero por analisis de sintaxis (ast), no de una lista mia.
import ast, io, json, os, sys

nomina = set()
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    if l.strip(): nomina.add(json.loads(l)['id'])
for libro in os.listdir('cuarentena'):
    d = os.path.join('cuarentena', libro)
    if not os.path.isdir(d) or libro.startswith('_'): continue
    for f in os.listdir(d):
        if f.endswith('.json'): nomina.add(f[:-5])

ruta = sys.argv[1]
arbol = ast.parse(io.open(ruta, encoding='utf-8').read())
hallados = []
for nodo in ast.walk(arbol):
    if isinstance(nodo, ast.Constant) and isinstance(nodo.value, str):
        if nodo.value in nomina:
            hallados.append((nodo.lineno, nodo.value))
print('%s: %d literal(es) que son un id de la nomina (%d ids en la nomina)'
      % (ruta, len(hallados), len(nomina)))
for ln, v in sorted(set(hallados)):
    print('  L%-4d %s' % (ln, v))
