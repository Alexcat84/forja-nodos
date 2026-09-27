# -*- coding: utf-8 -*-
"""Fase ciega de la 80 (copia libre de .v79aud/normal/censo_libros.py): el censo del grafo por libro (la clave de
`fuentes`) con su suma (R7), y las aristas cuya madre y cuyo hijo son de libros distintos, SOLO en cuentas y SI o NO
contra la unica que la ACTA 78 78.10 nombro (de Zhuo a Scott), sin imprimir ningun id de relacion leido del grafo (R6).
Solo lee."""
import io, json, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
g = dict((d['id'], d) for d in (json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()))
lib = lambda d: '+'.join(sorted(f if isinstance(f, str) else f.get('clave', '?') for f in d['fuentes']))
c = collections.Counter(lib(d) for d in g.values())
print('nodos por libro: %s | suma: %d' % (dict(c), sum(c.values())))
x = set((m, h) for m, d in g.items() for h in d['nodos_siguientes'] if lib(g[h]) != lib(d))
tot = sum(len(d['nodos_siguientes']) for d in g.values())
print('aristas del grafo: %d | entre libros distintos: %d | dentro de un libro: %d | suma: %d' % (tot, len(x), tot - len(x), tot))
print('las aristas entre libros son la unica de la ACTA 78 78.10: %s' % ('SI' if x == {('despedir_persona_respeto_franqueza', 'despedir_persona_franqueza_radical')} else 'NO'))
