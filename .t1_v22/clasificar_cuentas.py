# -*- coding: utf-8 -*-
"""SEPARA LAS OCURRENCIAS POR LA FORMA DE LA FRASE, PARA ORDENAR LA LECTURA A MANO.

LA ESPECIE QUE LA VUELTA 21 RETIRO, leida de `.t1_v21/arreglo_cuentas.py`, es UNA
Y SE PUEDE DESCRIBIR: el paso ATRIBUYE UNA CUENTA AL LIBRO (`el texto nombra
tres`, `sus dos ejemplares`, `las tres preguntas del texto`) Y EL LIBRO NO ESCRIBE
ESE NUMERO. Sus ejemplares corregidos alli son literales:

    "El texto da sus dos ejemplares:"        -> "El texto da sus ejemplares:"
    "y el texto nombra tres, tu jefe, ..."   -> "y el texto los nombra: tu jefe, ..."
    "hazte las tres preguntas del texto:"    -> "hazte las preguntas del texto:"

ASI QUE LA FORMA DELATA AL CANDIDATO, y este guion la busca: un numeral a menos de
40 caracteres de una marca de atribucion (`el texto`, `que el texto`, `el libro`,
`que pone`, `que nombra`, `que da`, `que marca`, `que enumera`, `que numera`).

NO DECIDE NADA. Las que caen en el grupo A se leen contra su linea para ver si el
libro escribe la cuenta o no. Las del grupo B se leen igual, pero son las que
llevan la cifra DENTRO del contenido transcrito (`cuarenta y cinco minutos`,
`veinte dolares`), donde el riesgo es otro y menor.
"""
import io
import json
import glob
import re
import sys

CAP = sys.argv[1] if len(sys.argv) > 1 else 'cap_09'

MARCAS = ['el texto', 'el libro', 'que pone', 'que nombra', 'que da ', 'que marca',
          'que enumera', 'que numera', 'que anuncia', 'que dice', 'segun el texto',
          'que el texto', 'que hace el texto']

_ns = {'__name__': '__c21__'}
_out = io.StringIO()
_so = sys.stdout
sys.stdout = _out
try:
    exec(compile(io.open('.t1_v21/cuentas21.py', encoding='utf-8').read(),
                 '.t1_v21/cuentas21.py', 'exec'), _ns)
finally:
    sys.stdout = _so
CUENTAS = _ns['CUENTAS']

A, B = [], []
for ruta in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')):
    d = json.load(io.open(ruta, encoding='utf-8'))
    r = d['resumen_teorico']
    caps = re.findall(r'cap_(\d\d)\.md', r) or re.findall(r'cap_(\d\d)', r)
    if not caps or 'cap_' + caps[0] != CAP:
        continue
    for j, paso in enumerate(d['pasos_accionables'], 1):
        bajo = paso.lower()
        for pal in CUENTAS:
            for m in re.finditer(r'\b' + pal + r'\b', bajo):
                ventana = bajo[max(0, m.start() - 40):m.end() + 40]
                atribuye = [k for k in MARCAS if k in ventana]
                ini = max(0, m.start() - 70)
                fin = min(len(paso), m.end() + 95)
                fila = (d['id'], j, pal, ','.join(atribuye), paso[ini:fin])
                (A if atribuye else B).append(fila)

print('=' * 78)
print('CLASIFICACION DE %s POR LA FORMA DE LA FRASE' % CAP)
print('=' * 78)
print('GRUPO A, el numeral va pegado a una marca de atribucion : %d' % len(A))
print('GRUPO B, el numeral va dentro del contenido transcrito  : %d' % len(B))
print('TOTAL                                                   : %d' % (len(A) + len(B)))
print('')
print('--- GRUPO A: LAS QUE HAY QUE COMPROBAR CONTRA LA LINEA, UNA A UNA ---')
for i, (ident, j, pal, marca, frag) in enumerate(A, 1):
    print('%2d. %-50s P%-2d [%s] (%s)' % (i, ident, j, pal, marca))
    print('      ...%s...' % frag)
print('')
print('--- GRUPO B: EL NUMERAL DENTRO DEL CONTENIDO ---')
for i, (ident, j, pal, _m, frag) in enumerate(B, 1):
    print('%2d. %-50s P%-2d [%s]  ...%s...' % (i, ident, j, pal, frag))
