# -*- coding: utf-8 -*-
"""Recompongo las dos fronteras de la VUELTA 55 tramo a tramo contra el fichero,
sin usar el instrumento del extractor: leo SU tabla del reporte y la mido yo."""
import re, sys, io
sys.stdout.reconfigure(encoding='utf-8')

REP = open('docs/loop/REPORTE.md', encoding='utf-8').read().split('\n')

def tabla(cap, desde, hasta):
    """Saco las filas de la tabla de frontera de <cap> del reporte."""
    filas = []
    pat = re.compile(r'^\|\s*`(L\d+) a (L\d+)`\s*\|\s*(\d+)\s*\|\s*\*\*(\d+)\*\*\s*\|')
    for l in REP[desde:hasta]:
        m = pat.match(l)
        if m:
            filas.append((int(m.group(1)[1:]), int(m.group(2)[1:]), int(m.group(3)), int(m.group(4))))
    return filas

def cuerpo(cap):
    lineas = open('fuentes/grove_high_output/%s.md' % cap, encoding='utf-8').read().split('\n')
    # cabecera: hasta el segundo guion triple
    triples = [i for i, l in enumerate(lineas) if l.strip() == '---']
    fin = triples[1] + 1  # 0-indexado; L = i+1
    return lineas, fin

for cap, desde, hasta in (('cap_09', 53038, 53067), ('cap_10', 53093, 53130)):
    filas = tabla(cap, desde, hasta)
    lineas, fin = cuerpo(cap)
    print('=' * 78)
    print('%s   filas de la tabla del reporte: %d' % (cap, len(filas)))
    print('  la cabecera acaba en la linea    : %d' % fin)
    con_contenido = [i + 1 for i in range(fin, len(lineas)) if lineas[i].strip()]
    print('  lineas con contenido tras cabecera: %d' % len(con_contenido))
    cubiertas = set()
    solapes = []
    suma = 0
    malas = []
    for a, b, pal, nod in filas:
        for L in range(a, b + 1):
            if L in cubiertas:
                solapes.append(L)
            cubiertas.add(L)
        mio = sum(len(lineas[L - 1].split()) for L in range(a, b + 1) if lineas[L - 1].strip())
        suma += pal
        if mio != pal:
            malas.append((a, b, pal, mio))
    print('  suma de las filas (reporte)      : %d' % suma)
    print('  mi recuento de palabras del cuerpo: %d' % sum(len(lineas[L - 1].split()) for L in con_contenido))
    print('  filas cuyo recuento NO me sale   : %d  %s' % (len(malas), malas))
    print('  SOLAPES                          : %d  %s' % (len(solapes), solapes))
    print('  lineas con contenido NO cubiertas: %d  %s' % (
        len([L for L in con_contenido if L not in cubiertas]),
        [L for L in con_contenido if L not in cubiertas]))
    print('  NODOS que la tabla del reporte da: %d' % sum(f[3] for f in filas))
    entero = len(open('fuentes/grove_high_output/%s.md' % cap, encoding='utf-8').read().split())
    print('  fichero entero (wc -w)           : %d' % entero)
