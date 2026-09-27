# -*- coding: utf-8 -*-
"""LOS PASOS DE LOS TRES CANDIDATOS DE cap_17, CONTADOS POR EL AUDITOR, Y LAS
LINEAS DEL LIBRO QUE SOSTIENEN SU TRAMO.

EL PUENTE NO LO CUENTA ESTE SCRIPT (`8.3.2`): lo lee el auditor contra el
parrafo del libro y su veredicto va en el acta.
"""
import io
import json
import re

LIBRO = 'fuentes/grove_high_output/cap_17.md'
FICHAS = [
    'priorizar_lista_entrenamiento_subordinados',
    'desarrollar_primer_curso_entrenamiento',
    'pedir_critica_anonima_curso_entrenamiento_dictado',
]

lineas = io.open(LIBRO, encoding='utf-8').read().split('\n')
total = 0
for i in FICHAS:
    d = json.load(io.open('cuarentena/grove_high_output/%s.json' % i,
                          encoding='utf-8'))
    n = len(d['pasos_accionables'])
    total += n
    m = re.search(r'(L\d+ a L\d+|L\d+), \d+ palabras', d['resumen_teorico'])
    print('  %-52s %d paso(s)   tramo %s' % (i, n, m.group(1) if m else '?'))
print('  ' + '=' * 74)
print('  cap_17 : %d candidato(s), %d paso(s) escritos' % (len(FICHAS), total))
print('  cap_18 : 0 candidato(s), 0 paso(s) escritos, SIN SUPERFICIE')
print('  LAS LINEAS DEL LIBRO QUE SOSTIENEN ESOS TRAMOS:')
for k in (49, 51, 53, 55, 57, 59, 61):
    print('    L%d: %s...' % (k, lineas[k - 1][:74]))
