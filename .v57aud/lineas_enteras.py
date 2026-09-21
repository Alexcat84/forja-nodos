# -*- coding: utf-8 -*-
"""Las lineas ENTERAS sobre las que concluyo, pegadas del fichero (remedio heredado
de ACTA 54 54.11). LOS GUIONES PROHIBIDOS DEL LIBRO SE SUSTITUYEN POR EL CORTO:
la regla del manual seccion 2 exime `fuentes/<clave>/` como bandeja de entrada
(src/comun.py BANDEJAS_DE_ENTRADA) pero NO exime este fichero mio, y la exencion es
de capa y no de contenido. Se declara aqui y en el acta: la cita NO es byte a byte,
lo unico que cambia es el caracter del guion."""
import sys
sys.path.insert(0, '.')
from src.comun import GUIONES_PROHIBIDOS
sys.stdout.reconfigure(encoding='utf-8')

def corto(t):
    for c in GUIONES_PROHIBIDOS:
        t = t.replace(c, '-')
    return t

CASOS = [('cap_09', 31), ('cap_09', 65), ('cap_08', 19), ('cap_08', 25), ('cap_08', 27)]
sust = 0
for cap, n in CASOS:
    lineas = open('fuentes/grove_high_output/%s.md' % cap, encoding='utf-8').read().split('\n')
    cruda = lineas[n - 1]
    limpia = corto(cruda)
    sust += sum(1 for a, b in zip(cruda, limpia) if a != b)
    print("=== %s L%d ENTERA (awk 'NR==%d') ===" % (cap, n, n))
    print(limpia)
    print()
print('GUIONES PROHIBIDOS SUSTITUIDOS POR EL CORTO EN ESTE FICHERO: %d' % sust)
print('NINGUNA OTRA LETRA TOCADA: solo el caracter del guion.')
