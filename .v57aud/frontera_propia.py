# -*- coding: utf-8 -*-
"""Recompongo las TRES fronteras de la VUELTA 56 tramo a tramo contra el fichero.
Reuso el camino de .v56aud/frontera_propia.py (austero: instrumento reusado, no nuevo):
leo LA TABLA que el extractor publico y la mido yo contra fuentes/.
Las tres tablas estan en .v56ext/frontera.txt; la de cap_08 esta ademas en el reporte,
y las tres de la vuelta 55 estan en el reporte de la vuelta 55 para el contraste."""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')

PAT = re.compile(r'^\|\s*`?(L\d+) a (L\d+)`?\s*\|\s*(\d+)\s*\|\s*\*\*(\d+)\*\*\s*\|')

def tabla(lineas, desde, hasta):
    out = []
    for l in lineas[desde:hasta]:
        m = PAT.match(l)
        if m:
            out.append((int(m.group(1)[1:]), int(m.group(2)[1:]), int(m.group(3)), int(m.group(4))))
    return out

def cuerpo(cap):
    lineas = open('fuentes/grove_high_output/%s.md' % cap, encoding='utf-8').read().split('\n')
    triples = [i for i, l in enumerate(lineas) if l.strip() == '---']
    return lineas, triples[1] + 1

FT = open('.v56ext/frontera.txt', encoding='utf-8').read().split('\n')
# los tres bloques de tabla de .v56ext/frontera.txt, por sus rotulos
marcas = [i for i, l in enumerate(FT) if l.startswith('| tramo de cap_')]
bloques = []
for k, i in enumerate(marcas):
    fin = marcas[k + 1] if k + 1 < len(marcas) else len(FT)
    bloques.append((re.search(r'cap_\d+', FT[i]).group(0), i, fin))

for cap, desde, hasta in bloques:
    filas = tabla(FT, desde, hasta)
    lineas, fin = cuerpo(cap)
    print('=' * 78)
    print('%s   filas de la tabla del extractor: %d' % (cap, len(filas)))
    print('  la cabecera acaba en la linea      : %d' % fin)
    con = [i + 1 for i in range(fin, len(lineas)) if lineas[i].strip()]
    print('  lineas con contenido tras cabecera : %d' % len(con))
    cubiertas, solapes, suma, malas = set(), [], 0, []
    for a, b, pal, nod in filas:
        for L in range(a, b + 1):
            if L in cubiertas:
                solapes.append(L)
            cubiertas.add(L)
        mio = sum(len(lineas[L - 1].split()) for L in range(a, b + 1) if lineas[L - 1].strip())
        suma += pal
        if mio != pal:
            malas.append((a, b, pal, mio))
    print('  suma de las filas (del extractor)  : %d' % suma)
    print('  MI recuento de palabras del cuerpo : %d' % sum(len(lineas[L - 1].split()) for L in con))
    print('  filas cuyo recuento NO me sale     : %d  %s' % (len(malas), malas))
    print('  SOLAPES                            : %d  %s' % (len(solapes), solapes))
    sin = [L for L in con if L not in cubiertas]
    print('  lineas con contenido NO cubiertas  : %d  %s' % (len(sin), sin))
    print('  NODOS que la tabla del extractor da: %d' % sum(f[3] for f in filas))
    print('  fichero entero (wc -w)             : %d'
          % len(open('fuentes/grove_high_output/%s.md' % cap, encoding='utf-8').read().split()))

# cap_08: la tabla DEL REPORTE contra la tabla DEL INSTRUMENTO, celda a celda
REP = open('docs/loop/REPORTE.md', encoding='utf-8').read().split('\n')
r08 = tabla(REP, 53880, 53905)
f08 = tabla(FT, bloques[0][1], bloques[0][2])
print('=' * 78)
print('cap_08: tabla DEL REPORTE contra tabla DEL INSTRUMENTO')
print('  filas en el reporte     : %d' % len(r08))
print('  filas en el instrumento : %d' % len(f08))
print('  IDENTICAS celda a celda : %s' % (r08 == f08))
