# -*- coding: utf-8 -*-
"""Recompone una frontera del REPORTE fila a fila contra el fichero del libro.
Auditor de la ACTA M4. No reutiliza nada: parsea la tabla del reporte, expande
los rangos de linea, suma con wc -w por linea y compara al digito.
"""
import re, sys

cap, libro, ini, fin = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])

# palabras por linea del fichero del libro, cuerpo desde L8
pal = {}
for i, ln in enumerate(open(libro, encoding='utf-8'), 1):
    n = len(ln.split())
    if i >= 8 and n:
        pal[i] = n

filas = []
todas = open('docs/loop/REPORTE.md', encoding='utf-8').read().splitlines()
for ln in todas[ini-1:fin]:
    s = ln.strip()
    if not s.startswith('|'):
        continue
    c = [x.strip().replace('*', '').replace('`', '') for x in s.strip('|').split('|')]
    if len(c) < 5 or not re.fullmatch(r'[RP]\d+', c[0]):
        continue
    filas.append((c[0], c[1], c[2]))

vistas = {}
malas = []
suma_dec = 0
for pieza, spec, p in filas:
    ls = []
    for tramo in spec.split(','):
        t = tramo.strip()
        m = re.fullmatch(r'L(\d+)\s+a\s+L(\d+)', t)
        if m:
            ls += list(range(int(m.group(1)), int(m.group(2)) + 1))
            continue
        m = re.fullmatch(r'L(\d+)', t)
        if not m:
            malas.append((pieza, 'RANGO ILEGIBLE', t))
            continue
        ls.append(int(m.group(1)))
    real = sum(pal.get(x, 0) for x in ls)
    dec = int(p)
    suma_dec += dec
    if real != dec:
        malas.append((pieza, spec, 'declara %d, el fichero da %d' % (dec, real)))
    for x in ls:
        if x in vistas and x in pal:
            malas.append((pieza, 'SOLAPE en L%d' % x, 'ya era de ' + vistas[x]))
        vistas[x] = pieza

sin_cubrir = sorted(set(pal) - set(vistas))
print('FRONTERA DE %s, RECOMPUESTA POR EL AUDITOR DE LA ACTA M4' % cap)
print('  fichero                        : %s' % libro)
print('  filas de la tabla del reporte  : %d' % len(filas))
print('  suma de palabras DECLARADA     : %d' % suma_dec)
print('  cuerpo real L8+ (suma wc -w)   : %d' % sum(pal.values()))
print('  lineas con palabras SIN CUBRIR : %d  %s' % (len(sin_cubrir), sin_cubrir[:20]))
print('  DISCREPANCIAS fila a fila      : %d' % len(malas))
for m in malas:
    print('    ', m)
