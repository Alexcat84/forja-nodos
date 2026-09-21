# celdas.py -- HEREDADO 1: saca TODA celda de tabla de un .md que lleve un
# numero, para poder mirar una a una si su fuente es un instrumento.
# SIN CONSTANTES TECLEADAS: no sabe que cifras espera, solo que son cifras.
import re, io, sys
ruta = sys.argv[1]
print('INSTRUMENTO celdas.py  SIN CONSTANTES TECLEADAS: fichero=%s' % ruta)
n = 0
for k, l in enumerate(io.open(ruta, encoding='utf-8'), 1):
    t = l.rstrip('\n')
    if not t.startswith('|'):
        continue
    celdas = [c.strip() for c in t.strip('|').split('|')]
    if all(set(c) <= set('-: ') for c in celdas):
        continue
    for c in celdas:
        if re.search(r'\d', c) and not re.match(r'^`?L\d', c):
            n += 1
            print('L%-4d  %s' % (k, c))
print('CELDAS DE TABLA CON CIFRA: %d' % n)
