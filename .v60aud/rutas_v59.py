# -*- coding: utf-8 -*-
"""Cosecha 7.B: toda ruta publicada como evidencia de una corrida es CIFRA.
Saca cada ruta del tramo de la vuelta 59 del REPORTE y comprueba que existe
y que no esta en cero bytes."""
import os, re

rep = open('docs/loop/REPORTE.md', encoding='utf-8').read().split('\n')
ini = next(i for i, l in enumerate(rep)
           if l.startswith('# VUELTA 59 DE LA LINEA SERIAL'))
tramo = '\n'.join(rep[ini:])

patron = re.compile(r'[\w./_-]*\.(?:txt|py|json|jsonl|md|sh)\b')
rutas = sorted(set(r for r in patron.findall(tramo)
                   if '/' in r and not r.startswith('http')))
falla = 0
for r in rutas:
    r2 = r.lstrip('.') if r.startswith('./') else r
    if os.path.exists(r2):
        n = os.path.getsize(r2)
        estado = 'OK  %8d bytes' % n if n else 'CERO BYTES'
    else:
        estado = 'NO EXISTE'
    if estado != 'OK  %8d bytes' % os.path.getsize(r2) if os.path.exists(r2) else True:
        pass
    if not os.path.exists(r2) or os.path.getsize(r2) == 0:
        falla += 1
    print('%-11s %s' % (estado.split()[0], r))
print()
print('rutas publicadas por el tramo de la vuelta 59 : %d' % len(rutas))
print('rutas inexistentes o de cero bytes            : %d' % falla)
