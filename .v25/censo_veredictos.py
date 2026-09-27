# -*- coding: utf-8 -*-
"""CUANTOS DE LOS PARES EN COLA TIENEN VEREDICTO MIO ESCRITO, CONTADO Y NO SUPUESTO.

El encargo dice que los 24 pares de los 7 bloqueados YA tienen sus veredictos
escritos en .v24/veredictos_insercion.json. Esto lo cuenta contra el fichero.
"""
import io, json
V = json.load(io.open('.v24/veredictos_insercion.json', encoding='utf-8'))
filas = [l.split() for l in io.open('.v24/cola_lectura.txt', encoding='utf-8') if l.strip()]
tot = con = 0
print('| candidato bloqueado | pares en la cola de la vuelta 24 | con veredicto escrito | sin el |')
print('|---|---:|---:|---:|')
for _c, ident, vecinos in filas:
    vs = vecinos.split(',')
    hay = [v for v in vs if ('%s>%s' % (ident, v)) in V]
    tot += len(vs); con += len(hay)
    print('| `%s` | %d | %d | **%d** |' % (ident, len(vs), len(hay), len(vs) - len(hay)))
print('| **los 7** | **%d** | **%d** | # **%d** |' % (tot, con, tot - con))
print('')
print('veredictos guardados en el fichero, en total : %d' % len(V))
print('de esos, que son de los 7 bloqueados         : %d'
      % len([k for k in V if k.split('>')[0] in [f[1] for f in filas]]))
