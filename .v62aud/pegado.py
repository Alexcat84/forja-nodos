# -*- coding: utf-8 -*-
"""COMPARA LOS BLOQUES QUE EL REPORTE PEGA CONTRA LOS FICHEROS QUE EL EXTRACTOR
GUARDO.

`D.38.3` manda que toda cifra salga de un instrumento corrido con su salida
literal al lado. Este script mide si la salida pegada ES la salida guardada:
cuenta las lineas que el reporte anade y las que se come, y despues compara las
cifras una a una.
"""
import io
import re

RAIZ = ''
REPORTE = 'docs/loop/REPORTE.md'


def tramo_de_la_vuelta(n):
    lineas = io.open(REPORTE, encoding='utf-8').read().split('\n')
    i = [k for k, l in enumerate(lineas) if l.startswith('# VUELTA %d,' % n)][0]
    return lineas[i:]


def bloque_indentado(lineas, arranque):
    """Las lineas indentadas a cuatro espacios que siguen al indice `arranque`."""
    out = []
    for l in lineas[arranque:]:
        if l.strip() == '':
            out.append('')
            continue
        if l.startswith('    '):
            out.append(l[4:])
        else:
            break
    while out and out[-1] == '':
        out.pop()
    return out


def cifras(lineas):
    """Toda similitud, familia, paso_contra_nodo, poblacion y conteo del bloque."""
    fuera = []
    for l in lineas:
        for c in re.findall(r'\d+\.\d{3}', l):
            fuera.append(c)
        m = re.search(r'poblacion del barrido\s*:\s*(\d+)', l)
        if m:
            fuera.append('pob=' + m.group(1))
        m = re.search(r'vecinos levantados en total\s*:\s*(\d+)', l)
        if m:
            fuera.append('vec=' + m.group(1))
        m = re.search(r'BLOQUEARIAN esperando veredicto\s*:\s*(\d+)', l)
        if m:
            fuera.append('blo=' + m.group(1))
    return fuera


tramo = tramo_de_la_vuelta(61)
for marca, fich in (('informe_1_priorizar', '.v61ext/informe_1_priorizar.txt'),
                    ('informe_2_desarrollar', '.v61ext/informe_2_desarrollar.txt')):
    k = [n for n, l in enumerate(tramo)
         if marca in l and l.strip().startswith('$ python forja.py informe')][0]
    peg = bloque_indentado(tramo, k + 1)
    fil = io.open(fich, encoding='utf-8').read().split('\n')
    pegs = [x.rstrip() for x in peg if x.strip()]
    fils = [x.rstrip() for x in fil if x.strip()]
    sobran = [x for x in pegs if x not in fils]
    faltan = [x for x in fils if x not in pegs]
    print('=' * 78)
    print(fich)
    print('  lineas NO vacias pegadas en el reporte        : %d' % len(pegs))
    print('  lineas NO vacias del fichero guardado         : %d' % len(fils))
    print('  lineas del REPORTE que el fichero NO imprime  : %d' % len(sobran))
    for x in sobran:
        print('     +', x)
    print('  lineas del FICHERO que el reporte NO pega     : %d' % len(faltan))
    for x in faltan:
        print('     -', x)
    cp, cf = cifras(pegs), cifras(fils)
    print('  CIFRAS pegadas en el reporte                  : %d' % len(cp))
    print('  CIFRAS del fichero guardado                   : %d' % len(cf))
    print('  CIFRAS del reporte que el fichero NO trae     : %s'
          % sorted(set(cp) - set(cf)))
    print('  CIFRAS del fichero que el reporte NO pega     : %s'
          % sorted(set(cf) - set(cp)))
