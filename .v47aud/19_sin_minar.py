# -*- coding: utf-8 -*-
"""Que renglones de cuerpo de cap_04.md NO estan citados por ninguno de los 14
candidatos de cap_04 que hay hoy en la bandeja. Leo los rangos L<n> a L<m> que
cada ficha declara en su propio resumen_teorico. Es una medida de COBERTURA
DECLARADA, no de frontera: la frontera vive en el reporte y yo no lo abro."""
import json, glob, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
citados = set()
print('rangos que cada ficha de cap_04 declara:')
for f in sorted(glob.glob('cuarentena/grove_high_output/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    rt = d.get('resumen_teorico', '')
    if 'cap_04' not in rt:
        continue
    rangos = re.findall(r'L(\d+) a L(\d+)', rt)
    marcas = set()
    for a, b in rangos:
        for n in range(int(a), int(b) + 1):
            marcas.add(n)
    for n in re.findall(r'\(L(\d+):', rt):
        marcas.add(int(n))
    citados |= marcas
    print('  %-52s %s' % (d['id'][:52], sorted(marcas) if marcas else '(ninguno)'))
lineas = open('fuentes/grove_high_output/cap_04.md', encoding='utf-8').read().split(chr(10))
cuerpo = [i for i in range(9, 324) if lineas[i-1].strip()]
sin = [n for n in cuerpo if n not in citados]
print()
print('renglones de cuerpo con contenido (L9 a L323) : %d' % len(cuerpo))
print('citados por alguna ficha de cap_04            : %d' % len([n for n in cuerpo if n in citados]))
print('SIN CITAR POR NINGUNA FICHA                   : %d' % len(sin))
print('  y son: %s' % sin)
