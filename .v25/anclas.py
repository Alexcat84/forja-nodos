# -*- coding: utf-8 -*-
"""EL ANCLA QUE UN RESUMEN LLAMA UNICA, CONTADA CONTRA LAS QUINCE UNIDADES DEL LIBRO.

La vuelta 19 anadio la UNIDAD DE ORIGEN a 24 candidatos que no la nombraban, y
cada uno declara el ancla textual que la sostiene con la formula 'el ancla textual
unica que la sostiene, X, corrida con grep contra las quince unidades del libro'.
ESO ES UNA AFIRMACION VERIFICABLE Y SE VERIFICA: se saca el ancla de cada resumen
y se cuenta en cuantas unidades aparece. Una que aparezca en dos NO es unica, y la
unidad que el fichero declara puede no ser la unica de la que sale el nodo.
"""
import glob, io, json, os, re

ANCLA = re.compile(r"ancla textual unica que la sostiene, '([^']+)'")
UNIDAD = re.compile(r'UNIDAD DE ORIGEN: fuentes/scott_radical_candor/(cap_\d+)')

fuentes = {}
for ruta in sorted(glob.glob('fuentes/scott_radical_candor/cap_*.md')):
    fuentes[os.path.basename(ruta)[:-3]] = io.open(ruta, encoding='utf-8').read()

filas = []
for ruta in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')
                   + glob.glob('cuarentena/_insertados/scott_radical_candor/*.json')):
    d = json.load(io.open(ruta, encoding='utf-8'))
    r = d.get('resumen_teorico', '')
    m, u = ANCLA.search(r), UNIDAD.search(r)
    if not m:
        continue
    ancla, unidad = m.group(1), (u.group(1) if u else '?')
    donde = sorted(c for c, t in fuentes.items() if ancla in t)
    filas.append((os.path.basename(ruta)[:-5], unidad, ancla, donde))

print('| candidato | unidad declarada | ancla que llama UNICA | unidades donde aparece |')
print('|---|---|---|---|')
malas = 0
for ident, unidad, ancla, donde in filas:
    bien = (len(donde) == 1 and donde[0] == unidad)
    if not bien:
        malas += 1
    print('| `%s` | `%s` | `%s` | **%s**%s |'
          % (ident, unidad, ancla, ', '.join(donde) or 'NINGUNA',
             '' if bien else '  # NO ES UNICA'))
print('')
print('candidatos con ancla declarada     : %d' % len(filas))
print('anclas que SI son unicas y cuadran : %d' % (len(filas) - malas))
print('anclas que NO lo son               : %d' % malas)
