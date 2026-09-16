# -*- coding: utf-8 -*-
"""EL ORDEN DE LA TANDA DE LA VUELTA 26, ESCRITO ANTES DE CORRER.

PRIMERO el unico que la aduana dejo en cola al cerrar la vuelta 25
(decidir_momento_despedir_persona, cap_06, con sus 4 pares por leer de
.v25/cola_lectura.txt): es el que ya tiene la cola abierta y medida.
DESPUES el orden del libro (EXTRACTOR.md 12.3), y alfabetico por id dentro de
cada unidad, que es el desempate que la casa ya usa desde la vuelta 24.

Y CUANDO UNO BLOQUEE, SE DEJA EN COLA Y SE SIGUE (D.36): entre dos ordenes
posibles, el que abre la cola gana.
"""
import glob, io, json, os, re

BANDEJA = 'cuarentena/scott_radical_candor'
CITA = re.compile(r'cap_(\d+)')
COLA = ['decidir_momento_despedir_persona']

resto = []
for ruta in sorted(glob.glob(os.path.join(BANDEJA, '*.json'))):
    ident = os.path.basename(ruta)[:-5]
    if ident in COLA:
        continue
    d = json.load(io.open(ruta, encoding='utf-8'))
    m = CITA.findall(d.get('resumen_teorico', ''))
    resto.append(('cap_%s' % m[0] if m else 'cap_99', ident))
resto.sort()

with io.open('.v26/orden.txt', 'w', encoding='utf-8', newline='\n') as f:
    for ident in COLA:
        f.write('cola %s\n' % ident)
    for cap, ident in resto:
        f.write('%s %s\n' % (cap, ident))

print('1. el que la aduana dejo EN COLA al cerrar la vuelta 25 : %d' % len(COLA))
for i, ident in enumerate(COLA, 1):
    print('   %2d. %s   (cap_06, 4 pares por leer)' % (i, ident))
print('')
print('2. despues, el orden del libro, alfabetico por id dentro de cada unidad : %d' % len(resto))
por_cap = {}
for cap, _i in resto:
    por_cap[cap] = por_cap.get(cap, 0) + 1
for cap in sorted(por_cap):
    print('   %s : %d' % (cap, por_cap[cap]))
print('')
print('TOTAL en la bandeja del lote 4 : %d' % (len(COLA) + len(resto)))
