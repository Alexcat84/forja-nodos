# -*- coding: utf-8 -*-
"""RECORTE DECLARADO de las siete salidas de .v49aud/16_barrido_<id>.out, que son
el instrumento 07 (senial 1 de la casa) corrido sobre los 7 candidatos de cap_02.

NO MIDE NADA NUEVO: de cada salida toma su reloj, su cuenta sobre umbral y los
vecinos que pasan el umbral, en el orden en que el instrumento los dio. Las siete
salidas enteras, con sus 8 primeros vecinos cada una, estan en el arbol."""
import io, sys, glob, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
umbral = 0.35
tot = 0
for f in sorted(glob.glob('.v49aud/16_barrido_*.out')):
    L = io.open(f, encoding='utf-8').read().split('\n')
    fid = [x.split(': ')[1] for x in L if x.startswith('FICHA')][0]
    reloj = [x.split(': ')[1] for x in L if 'reloj' in x][0]
    cuenta = int([x.rsplit(': ', 1)[1] for x in L if 'por encima del umbral' in x][0])
    tot += cuenta
    print('%s   reloj %s   vecinos sobre %s: %d' % (fid, reloj, umbral, cuenta))
    for x in L:
        m = re.match(r'\s+(0\.\d+)\s+\[([^\]]+)\]\s+(\S+)', x)
        if m and float(m.group(1)) >= umbral:
            print('      %s  [%s] %s' % (m.group(1), m.group(2).strip(), m.group(3)))
print()
print('pares sobre umbral en los 7 candidatos de cap_02: %d' % tot)
