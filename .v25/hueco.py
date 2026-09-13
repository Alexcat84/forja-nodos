# -*- coding: utf-8 -*-
"""EL HUECO DEL FRENO, CONTADO DE LOS FICHEROS Y DE LA LISTA `NUM`, HOY.

Una cifra del encargo no es fuente de una cifra mia (EXTRACTOR.md 5). El encargo
me entrega 6 filas, 57 candidatos, 539 pasos y 97 ocurrencias. Esto las vuelve a
contar: las filas y las ocurrencias de la lista `NUM` del instrumento del freno,
y los candidatos y los pasos de los ficheros del lote, bandeja mas insertados.
"""
import glob, io, json, re

CITA = re.compile(r'cap_(\d+)')
por_cap = {}
for ruta in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')
                   + glob.glob('cuarentena/_insertados/scott_radical_candor/*.json')):
    d = json.load(io.open(ruta, encoding='utf-8'))
    m = CITA.findall(d.get('resumen_teorico', ''))
    cap = 'cap_%s' % m[0] if m else 'SIN CITA'
    fila = por_cap.setdefault(cap, [0, 0])
    fila[0] += 1
    fila[1] += len(d['pasos_accionables'])

fuente = io.open('.v24/freno_cierre.py', encoding='utf-8').read()
NUM = eval(re.search(r'^NUM = \[.*?^\]', fuente, re.S | re.M).group(0).split('=', 1)[1].strip())

print('| fila de hueco | candidatos | pasos | ocurrencias que su rotulo declara |')
print('|---|---:|---:|---:|')
tc = tp = to = 0
for cap, _num, quien, firmado in NUM:
    if firmado:
        continue
    cand, pasos = por_cap.get(cap, [0, 0])
    occ = int(re.search(r'(\d+) ocurrencia', quien).group(1))
    tc += cand; tp += pasos; to += occ
    print('| `%s` | %d | %d | %d |' % (cap, cand, pasos, occ))
print('| **el hueco entero** | **%d** | **%d** | **%d** |' % (tc, tp, to))
print('')
print('filas de hueco contadas : %d' % len([1 for _c, _n, _q, f in NUM if not f]))
print('filas firmadas          : %d de %d' % (len([1 for _c, _n, _q, f in NUM if f]), len(NUM)))
