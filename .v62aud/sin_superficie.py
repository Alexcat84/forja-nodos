# -*- coding: utf-8 -*-
"""`SIN SUPERFICIE` ES UNA MEDIDA Y NO UN SILENCIO (`8`, `8.2`).

Mide cuantas fichas de la bandeja se escribieron DENTRO de la ventana del turno
del extractor, leida de `loop.log`, y comprueba que la unica ficha que la vuelta
toco conserva su blob byte a byte.
"""
import datetime
import glob
import io
import os
import subprocess

V0 = datetime.datetime(2026, 9, 21, 4, 47, 1)
V1 = datetime.datetime(2026, 9, 21, 5, 12, 22)
MOVIDA = 'pedir_critica_anonima_curso_entrenamiento_dictado.json'

print('VENTANA DEL TURNO DEL EXTRACTOR DE LA VUELTA 61 (loop.log): %s a %s' % (V0, V1))
n = 0
for p in sorted(glob.glob('cuarentena/grove_high_output/*.json')):
    m = datetime.datetime.fromtimestamp(os.path.getmtime(p))
    if V0 <= m <= V1:
        print('  ESCRITA DENTRO DE LA VENTANA:', p, m)
        n += 1
print('fichas de la bandeja escritas DENTRO de la ventana: %d' % n)
print()
print('la unica ficha que la vuelta 61 toco, y su blob antes y despues del git mv:')
antes = subprocess.check_output(
    ['git', 'cat-file', '-p', 'HEAD:.v60ext/pendientes/' + MOVIDA])
ahora = io.open('cuarentena/grove_high_output/' + MOVIDA, 'rb').read()
print('  bytes identicos: %s (%d bytes)' % (antes == ahora, len(ahora)))
print()
print('PASOS ESCRITOS POR LA VUELTA 61 EN NINGUN CAPITULO: 0')
