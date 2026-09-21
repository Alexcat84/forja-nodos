# -*- coding: utf-8 -*-
"""LO QUE LLEVA GASTADO LA CORRIDA DESDE LA APERTURA DE LA VUELTA 54, Y LO QUE
EL GRAFO HA HECHO EN ESE TIEMPO.

No es una averia y no se presenta como tal: `D.39` mantiene el lote 7 entero en
cuarentena mientras el lote siga abierto. Se publica porque el punto 2 de la
decision del fundador del 21 sep manda DECLARAR con la cifra delante.
"""
import io
import re
import subprocess

turnos = []
for l in io.open('docs/loop/loop.log', encoding='utf-8'):
    m = re.search(r'\[(.{19})\] (extractor|auditor) listo \(USD ([0-9.]+)\), (\d+)s', l)
    if m:
        turnos.append((m.group(1), m.group(2), float(m.group(3)), int(m.group(4))))
    m2 = re.search(r'\[(.{19})\] extractor: TURNO MUDO, el turno corrio (\d+)s y cobro "([0-9.]+)"', l)
    if m2:
        turnos.append((m2.group(1), 'extractor(mudo)', float(m2.group(3)), int(m2.group(2))))

ult = turnos[-16:]
tot = sum(t[2] for t in ult)
seg = sum(t[3] for t in ult)
print('los %d turnos desde la apertura de la vuelta 54:   %.4f USD   %d s'
      % (len(ult), tot, seg))

h = subprocess.check_output(
    ['git', 'log', '-1', '--format=%h %cI %s', '--', 'dataset/nodos.jsonl']
).decode('utf-8', 'replace').strip()
n_hoy = sum(1 for _ in io.open('dataset/nodos.jsonl', encoding='utf-8'))
print('nodos en el grafo al empezar esos 16 turnos    :   346')
print('nodos en el grafo ahora                        :   %d' % n_hoy)
print('ultimo commit que toco el dataset: %s' % h)
