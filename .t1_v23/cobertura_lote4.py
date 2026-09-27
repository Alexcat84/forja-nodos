# -*- coding: utf-8 -*-
"""QUE UNIDADES DEL LOTE 4 TIENEN YA CANDIDATO ESCRITO, CONTADO DEL FICHERO.

La condicion de D.39 es LOTE CERRADO EN EXTRACCION, y eso se mide comparando la
bandeja de entrada con lo que cada candidato declara como unidad de origen. No se
supone: se cuenta.
"""
import glob
import io
import json
import os
import re

BANDEJA = sorted(os.path.basename(p)[:-3]
                 for p in glob.glob('fuentes/scott_radical_candor/*.md'))
CITA = re.compile(r'fuentes/scott_radical_candor/(cap_\d+)\.md')

vistas = set()
for ruta in glob.glob('cuarentena/scott_radical_candor/*.json'):
    d = json.load(io.open(ruta, encoding='utf-8'))
    for cap in CITA.findall(d.get('resumen_teorico', '')):
        vistas.add(cap)

# UNA UNIDAD SIN CANDIDATO NO ES LO MISMO QUE UNA UNIDAD SIN MINAR, y confundirlas
# haria creer que al lote le faltan tres capitulos cuando le falta uno. Las dos
# excepciones van escritas con su rotulo leido del propio fichero.
SALDADAS = {
    'cap_00': 'Copyright Page: no minable, no hay procedimiento que extraer',
    'cap_02': 'Introduction: minado en su vuelta con resultado CERO candidatos',
}

faltan = [c for c in BANDEJA if c not in vistas and c not in SALDADAS]
print('unidades en la bandeja de entrada : %d' % len(BANDEJA))
print('unidades con candidato escrito    : %d' % len([c for c in BANDEJA if c in vistas]))
print('unidades saldadas sin candidato   : %d   %s' % (len(SALDADAS), sorted(SALDADAS)))
print('unidades SIN MINAR                : %d   %s' % (len(faltan), faltan))
for cap, razon in sorted(SALDADAS.items()):
    rotulo = [l.split(':', 1)[1].strip()
              for l in io.open('fuentes/scott_radical_candor/%s.md' % cap,
                               encoding='utf-8').read().splitlines()[:7]
              if l.startswith('unidad:')]
    print('  %s  unidad=%s  -> %s' % (cap, rotulo[0] if rotulo else '?', razon))
