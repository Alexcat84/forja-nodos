# -*- coding: utf-8 -*-
"""Que lineas de cuerpo de cap_14 NO estan dentro de ningun nodo del grafo.
Cuerpo = de la linea 8 en adelante, que es donde acaba el frontmatter."""
import io
cubiertas = set()
for a, b in [(21,33),(35,63),(65,71),(73,93),(95,97),(99,115),(117,123),(125,141),
             (143,151),(153,169),(171,185),(187,195),(197,203),(205,219),(221,239)]:
    cubiertas.update(range(a, b + 1))
lineas = io.open('fuentes/scott_radical_candor/cap_14.md', encoding='utf-8').read().split('\n')
fuera = []
for n in range(8, len(lineas) + 1):
    t = lineas[n-1] if n-1 < len(lineas) else ''
    if t.strip() and n not in cubiertas:
        fuera.append(n)
print('lineas de cuerpo CON TEXTO fuera de todo nodo: %d' % len(fuera))
print('sus numeros: %s' % fuera)
for n in fuera:
    print('  %d: %s' % (n, lineas[n-1][:95]))
