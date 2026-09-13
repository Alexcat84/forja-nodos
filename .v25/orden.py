# -*- coding: utf-8 -*-
"""EL ORDEN DE LA TANDA, ESCRITO ANTES DE CORRER Y NO DESPUES (ACTA 24 3.3).

PRIMERO los 7 que la aduana bloqueo en la vuelta 24, porque sus 24 pares ya estan
leidos y sus veredictos escritos: el trabajo de lectura ya esta pagado y meterlos
primero no abre cola nueva. DESPUES el orden del libro (EXTRACTOR.md 12.3),
cap_01 a cap_14, y alfabetico por id dentro de cada unidad, que es el desempate
que la casa ya usa.

Y CUANDO UNO BLOQUEE, SE DEJA EN COLA Y SE SIGUE, por el criterio que D.36
escribe: entre dos ordenes posibles, el que abre la cola gana. Dejar en cola al
bloqueado y seguir mete a ese candidato mas tarde, con mas nodos delante, y por
tanto abre MAS pares, no menos.
"""
import glob, io, json, os, re

BANDEJA = 'cuarentena/scott_radical_candor'
CITA = re.compile(r'cap_(\d+)')

cola = [l.split()[1] for l in io.open('.v24/cola_lectura.txt', encoding='utf-8')
        if l.strip()]

resto = []
for ruta in sorted(glob.glob(os.path.join(BANDEJA, '*.json'))):
    ident = os.path.basename(ruta)[:-5]
    if ident in cola:
        continue
    d = json.load(io.open(ruta, encoding='utf-8'))
    m = CITA.findall(d.get('resumen_teorico', ''))
    resto.append(('cap_%s' % m[0] if m else 'cap_99', ident))
resto.sort()

with io.open('.v25/orden.txt', 'w', encoding='utf-8', newline='\n') as f:
    for ident in cola:
        f.write('cola %s\n' % ident)
    for cap, ident in resto:
        f.write('%s %s\n' % (cap, ident))

print('1. los que la aduana BLOQUEO en la vuelta 24, con sus pares ya leidos : %d' % len(cola))
for i, ident in enumerate(cola, 1):
    print('   %2d. %s' % (i, ident))
print('')
print('2. despues, el orden del libro, alfabetico por id dentro de cada unidad : %d' % len(resto))
por_cap = {}
for cap, _i in resto:
    por_cap[cap] = por_cap.get(cap, 0) + 1
for cap in sorted(por_cap):
    print('   %s : %d' % (cap, por_cap[cap]))
print('')
print('TOTAL en la bandeja del lote 4 : %d' % (len(cola) + len(resto)))
