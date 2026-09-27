# -*- coding: utf-8 -*-
"""ACTA 78: el censo del grafo por libro (la clave de `fuentes`) y las aristas cuya madre y cuyo hijo son de libros distintos,
nombradas. Punto de partida del PARA_ALEXIS de cierre (PARALELO.md 4.c). Solo lee."""
import io, json, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
g = dict((d['id'], d) for d in (json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()))
lib = lambda d: '+'.join(sorted(f if isinstance(f, str) else f.get('clave', '?') for f in d['fuentes']))
c = collections.Counter(lib(d) for d in g.values())
print('nodos por libro: %s | suma: %d' % (dict(c), sum(c.values())))
x = [(m, h) for m, d in g.items() for h in d['nodos_siguientes'] if lib(g[h]) != lib(d)]
tot = sum(len(d['nodos_siguientes']) for d in g.values())
print('aristas del grafo: %d | entre libros distintos: %d | dentro de un libro: %d | suma: %d' % (tot, len(x), tot - len(x), tot))
for m, h in x: print('  %s (%s) > %s (%s)' % (m, lib(g[m]), h, lib(g[h])))
