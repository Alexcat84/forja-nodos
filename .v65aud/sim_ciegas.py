# -*- coding: utf-8 -*-
"""Las 17 filas de mi lectura ciega (.v65aud/clases_48.txt) con su similitud de texto (.v65aud/pares48.txt),
de mayor a menor, y cuantas pasan de 0,4 (la frontera que la ACTA 63 63.3.c cita para D64.3 sin nombrar pares)."""
import io, re
ciegas = set()
for l in io.open('.v65aud/clases_48.txt', encoding='utf-8'):
    m = re.match(r'CIEGA\s+\S+\s+\S+\s+(\S+) -> (\S+)', l)
    if m: ciegas.add(m.groups())
filas = []
for l in io.open('.v65aud/pares48.txt', encoding='utf-8'):
    c = [x.strip() for x in l.split('|')]
    if (c[0], c[1]) in ciegas:
        filas.append((float(re.search(r'sim (\S+)', c[4]).group(1)), c[0], c[1]))
for s, a, b in sorted(filas, reverse=True): print('%.3f  %s -> %s' % (s, a, b))
print('filas ciegas: %d | con similitud de texto sobre 0,4: %d' % (len(filas), len([f for f in filas if f[0] > 0.4])))
