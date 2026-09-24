# -*- coding: utf-8 -*-
"""Muestra pineada de los SANO (AUDITOR_FORJA.md 7) tomada en la fase ciega de la 65 sobre los SANO de
.v64ext/veredictos_listos.txt de las filas 1 a 20, que son las lineas que el encargo mando copiar tal
cual a la bitacora. Un par visto desde los dos lados cuenta como UN par. Tamano: el mayor entre 3 y el
20 por ciento, techo 20. Semilla escrita."""
import io, re, random
SEMILLA = 65023
tanda = [l.split()[1] for l in io.open('.v64ext/orden.txt', encoding='utf-8') if l[:1].isdigit() and 1 <= int(l.split()[0]) <= 20]
pares = set(); cand = None
for l in io.open('.v64ext/veredictos_listos.txt', encoding='utf-8'):
    if l.startswith('## '): cand = l[3:].strip(); continue
    m = re.match(r'(\w+)\|SANO\|', l)
    if m and cand in tanda: pares.add(tuple(sorted((cand, m.group(1)))))
pares = sorted(pares)
k = min(20, max(3, -(-len(pares) * 20 // 100)))
print('pares SANO distintos en las filas 1 a 20: %d | muestra: %d | semilla %d' % (len(pares), k, SEMILLA))
for p in random.Random(SEMILLA).sample(pares, k): print('  %s | %s' % p)
