# -*- coding: utf-8 -*-
"""EL FRENO DE FIDELIDAD, FILA POR CAPITULO, CON EL DENOMINADOR RECONTADO HOY.

QUE MIDE Y QUE NO, y conviene leerlo antes de la tabla. El DENOMINADOR (pasos por
capitulo) lo recuenta este guion de los ficheros, hoy. El NUMERADOR (pasos que
escribio el extractor y el libro no dice) NO lo puede contar ningun codigo: sale
de la relectura de fidelidad D.30, que es una lectura contra el libro. Por eso el
numerador entra como dato firmado, con la vuelta y el nombre de quien lo firmo al
lado, y las filas que nadie ha releido con el instrumento ancho salen dichas como
tales en vez de salir como si estuvieran cerradas.

UN CERO QUE NADIE HA MEDIDO NO ES UN CERO: ES UN HUECO, y se dice.
"""
import glob
import io
import json
import re

CITA = re.compile(r'cap_(\d+)')

# EL CAPITULO DE CADA CANDIDATO. Se lee del resumen_teorico: la costumbre de esta
# casa es escribir la ruta entera, pero seis candidatos de cap_04 son anteriores a
# esa costumbre y solo escriben `cap_04` suelto, asi que se busca el primer cap_NN
# que el resumen nombre, sea con ruta o sin ella.
por_cap = {}
for ruta in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')):
    d = json.load(io.open(ruta, encoding='utf-8'))
    m = CITA.findall(d.get('resumen_teorico', ''))
    cap = 'cap_%s' % m[0] if m else 'SIN CITA'
    fila = por_cap.setdefault(cap, [0, 0])
    fila[0] += 1
    fila[1] += len(d['pasos_accionables'])

# NUMERADORES, cada uno con quien lo firmo. Los heredados se citan como contraste
# (EXTRACTOR.md 5) y NO se recalculan aqui: lo que se recalcula es el denominador.
NUM = [
    ('cap_01', 0, 'sin releer con el ancho: 1 ocurrencia', False),
    ('cap_03', 0, 'sin releer con el ancho: 6 ocurrencias en 7 pasos', False),
    ('cap_04', 8, 'FIRMADO por el extractor en la vuelta 22, leido uno a uno', True),
    ('cap_05', 2, 'sin releer con el ancho: 20 ocurrencias', False),
    ('cap_06', 0, 'sin releer con el ancho: 33 ocurrencias', False),
    ('cap_07', 0, 'sin releer con el ancho: 20 ocurrencias', False),
    ('cap_08', 0, 'sin releer con el ancho: 17 ocurrencias', False),
    ('cap_09', 7, 'FIRMADO por el extractor en la vuelta 22, leido uno a uno', True),
    ('cap_10', 17, 'numerador del auditor (ACTA 21 7.2); denominador recontado hoy', True),
    ('cap_11', 1, 'el candelabro que el auditor cazo (ACTA 22 4.1), corregido en la vuelta 23', True),
    ('cap_12', 0, 'MIO, leido en el acto de escribir los 2', True),
    ('cap_13', 0, 'MIO, leido en el acto de escribir los 12', True),
]

print('=' * 78)
print('1. PASOS INVENTADOS POR CAPITULO, CON EL DENOMINADOR RECONTADO HOY')
print('=' * 78)
print('| unidad | candidatos | pasos | numerador | tasa | quien firma el numerador |')
print('|---|---:|---:|---:|---:|---|')
tot_cand = tot_pasos = tot_num = 0
peor = (None, -1.0)
for cap, num, quien, firmado in NUM:
    cand, pasos = por_cap.get(cap, [0, 0])
    tasa = (100.0 * num / pasos) if pasos else 0.0
    tot_cand += cand
    tot_pasos += pasos
    tot_num += num
    if firmado and tasa > peor[1]:
        peor = (cap, tasa)
    print('| `%s` | %d | %d | **%d** | **%.2f** | %s |' % (cap, cand, pasos, num, tasa, quien))
print('| **el lote 4 hasta `cap_13`** | **%d** | **%d** | **%d** | **%.2f** | **INCOMPLETO: %d filas sin releer con el ancho** |'
      % (tot_cand, tot_pasos, tot_num, 100.0 * tot_num / tot_pasos,
         len([1 for _c, _n, _q, f in NUM if not f])))

print('')
print('=' * 78)
print('2. EL FRENO SE DECIDE SOBRE EL PEOR CAPITULO FIRMADO, NO SOBRE EL TOTAL')
print('=' * 78)
print('| | |')
print('|---|---:|')
print('| filas con numerador FIRMADO | **%d** de **%d** |'
      % (len([1 for _c, _n, _q, f in NUM if f]), len(NUM)))
print('| **la fila que decide, que es la peor firmada** | `%s` con **%.2f** |' % peor)
print('| tope de `PASOS INVENTADOS` | **10,00** |')
print('| **el freno** | **%s** |' % ('DISPARADO' if peor[1] > 10.0 else 'no disparado'))
print('| tramo que el freno deja | **%s** |'
      % ('DOS capitulos' if peor[1] > 10.0 else 'sin bajar'))

print('')
print('=' * 78)
print('3. LA COMPROBACION DE QUE NINGUN CANDIDATO SE QUEDA FUERA DE LA TABLA')
print('=' * 78)
en_tabla = set(c for c, _n, _q, _f in NUM)
sueltos = sorted(c for c in por_cap if c not in en_tabla)
print('candidatos en cuarentena del lote 4 : %d'
      % len(glob.glob('cuarentena/scott_radical_candor/*.json')))
print('candidatos contados en la tabla     : %d' % tot_cand)
print('capitulos fuera de la tabla         : %d   %s' % (len(sueltos), sueltos))
