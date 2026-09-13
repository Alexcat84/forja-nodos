# -*- coding: utf-8 -*-
"""PEGA LA TABLA DE UN FICHERO DE SALIDA EN EL SITIO DE SU MARCADOR.

Es el remedio mecanico de D.41 llevado hasta el final: la tabla no se copia a
mano ni una vez, ni siquiera al armar el reporte. El marcador se sustituye por
las lineas de tabla del fichero del instrumento, tal cual salieron.

    python .t1_v23/pegar.py <fragmento.md> <MARCADOR> <salida.txt> [n_tabla]

n_tabla es el indice (desde 0) del bloque de tabla dentro del fichero; sin el se
pegan TODOS los bloques, separados por una linea en blanco.
"""
import io
import sys


def bloques(texto):
    fuera, actual = [], []
    for linea in texto.split('\n'):
        if linea.lstrip().startswith('|'):
            actual.append(linea.rstrip())
        elif actual:
            fuera.append(actual)
            actual = []
    if actual:
        fuera.append(actual)
    return fuera


ruta_frag, marcador, ruta_salida = sys.argv[1], sys.argv[2], sys.argv[3]
cuales = bloques(io.open(ruta_salida, encoding='utf-8').read())
if len(sys.argv) > 4:
    cuales = [cuales[int(sys.argv[4])]]

pegado = '\n\n'.join('\n'.join(b) for b in cuales)
texto = io.open(ruta_frag, encoding='utf-8').read()
if marcador not in texto:
    raise SystemExit('el marcador %s no esta en %s' % (marcador, ruta_frag))
io.open(ruta_frag, 'w', encoding='utf-8', newline='\n').write(texto.replace(marcador, pegado))
print('pegadas %d tabla(s) de %s en %s' % (len(cuales), ruta_salida, ruta_frag))
