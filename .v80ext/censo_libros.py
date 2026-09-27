# -*- coding: utf-8 -*-
"""Vuelta 80, TAREA 5 (encargo, punto 2 del cierre de la campania): el censo por libro y las aristas entre libros, leidos de
dataset/nodos.jsonl y de nada mas. Cada nodo se cuenta por la clave de su PRIMERA fuente (la casa del nodo, EXTRACTOR.md 10: la
fuente anadida por injerto va en segundo lugar), con la suma; y aparte, los nodos que llevan mas de una fuente, nombrados. Una arista
es un par madre > hijo con el hijo en nodos_siguientes de la madre; es ENTRE LIBROS si la casa de la madre y la del hijo son distintas,
y se nombran todas. Comprueba tambien que cada arista vive por los dos lados. Solo lee.
    python .v80ext/censo_libros.py"""
import io, json, collections
g = collections.OrderedDict((d['id'], d) for d in (json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()))
casa = dict((i, d['fuentes'][0]['clave']) for i, d in g.items())
c = collections.Counter(casa.values())
print('CENSO POR LIBRO (clave de la primera fuente de cada nodo de dataset/nodos.jsonl)')
for k, n in sorted(c.items(), key=lambda x: (-x[1], x[0])):
    print('  %-32s %4d' % (k, n))
print('  %-32s %4d  (nodos en el fichero: %d)' % ('SUMA', sum(c.values()), len(g)))
multi = [(i, [f['clave'] for f in d['fuentes']]) for i, d in g.items() if len(d['fuentes']) > 1]
print('nodos con mas de una fuente: %d' % len(multi))
for i, f in multi:
    print('  %s %s' % (i, f))
ar = [(m, h) for m, d in g.items() for h in (d.get('nodos_siguientes') or [])]
rotas = [(m, h) for m, h in ar if h not in g or m not in (g[h].get('nodos_previos') or [])]
entre = [(m, h) for m, h in ar if h in g and casa[m] != casa[h]]
print('aristas en el grafo: %d | que no viven por los dos lados: %d %s | entre libros distintos: %d' % (len(ar), len(rotas), rotas or '', len(entre)))
for m, h in entre:
    print('  %s (%s) > %s (%s)' % (m, casa[m], h, casa[h]))
por = collections.Counter((casa[m], casa[h]) for m, h in entre)
for (a, b), n in sorted(por.items()):
    print('  pares de libros: %s > %s: %d' % (a, b, n))
