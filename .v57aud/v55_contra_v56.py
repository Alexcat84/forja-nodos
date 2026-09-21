# -*- coding: utf-8 -*-
"""La afirmacion de WW.2: las tablas de cap_09 y cap_10 de esta vuelta son IDENTICAS
tramo a tramo a las que la vuelta 55 publico. La mido yo, celda a celda."""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
PAT = re.compile(r'^\|\s*`?(L\d+) a (L\d+)`?\s*\|\s*(\d+)\s*\|\s*\*\*(\d+)\*\*\s*\|')
def tabla(lineas, desde, hasta):
    return [(int(m.group(1)[1:]), int(m.group(2)[1:]), int(m.group(3)), int(m.group(4)))
            for m in (PAT.match(l) for l in lineas[desde:hasta]) if m]
REP = open('docs/loop/REPORTE.md', encoding='utf-8').read().split('\n')
FT  = open('.v56ext/frontera.txt', encoding='utf-8').read().split('\n')
marcas = [i for i, l in enumerate(FT) if l.startswith('| tramo de cap_')]
bl = {}
for k, i in enumerate(marcas):
    bl[re.search(r'cap_\d+', FT[i]).group(0)] = (i, marcas[k+1] if k+1 < len(marcas) else len(FT))
# la vuelta 55 publico sus dos tablas en el REPORTE, seccion VV.3 (L53008 a L53169)
for cap in ('cap_09', 'cap_10'):
    v56 = tabla(FT, *bl[cap])
    # busco el rotulo de la tabla de ese cap dentro de VV.3
    ini = next(i for i in range(53008, 53169) if REP[i].startswith('| tramo de %s ' % cap))
    fin = next((i for i in range(ini+1, 53169) if REP[i].startswith('| tramo de cap_')), 53169)
    v55 = tabla(REP, ini, fin)
    print('%s   v55: %d filas    v56: %d filas    IDENTICAS: %s'
          % (cap, len(v55), len(v56), v55 == v56))
    if v55 != v56:
        for a, b in zip(v55, v56):
            if a != b:
                print('   DIFIERE  v55=%s  v56=%s' % (a, b))
