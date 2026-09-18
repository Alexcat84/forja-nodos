# -*- coding: utf-8 -*-
"""Anexa al reporte la fila de UN candidato, en el acto en que entra.

    python .v41/fila.py <n> <titulo de la subseccion> <ruta del informe> <ruta de la prosa> [mas informes...]

La prosa la escribe la lectura y va en su fichero; la salida del instrumento se pega
entera del informe. Asi la fila baja con el candidato ya dentro y no al final.
"""
import io
import sys


def leer(p):
    return io.open(p, encoding='utf-8').read().rstrip('\n')


def sangrar(t, n=4):
    return '\n'.join((' ' * n + l) if l.strip() else '' for l in t.split('\n'))


n = sys.argv[1]
titulo = sys.argv[2]
informe = sys.argv[3]
prosa = sys.argv[4]
extras = sys.argv[5:]

partes = ['\n#### EC.6.a.%s. %s\n\n%s\n' % (n, titulo, leer(prosa))]
partes.append('\n<!-- TALLADO: parcial salida=%s -->\n\n%s\n' % (informe, sangrar(leer(informe))))
for e in extras:
    partes.append('\n<!-- TALLADO: parcial salida=%s -->\n\n%s\n' % (e, sangrar(leer(e))))

with io.open('docs/loop/REPORTE.md', 'a', encoding='utf-8') as f:
    f.write(''.join(partes))
print('fila %s anexada' % n)
