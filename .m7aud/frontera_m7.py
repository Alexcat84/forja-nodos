# Recompone las dos fronteras de la vuelta 6 contra el fichero fuente, fila a fila,
# y compara la tabla pegada en REPORTE.md con la bruta de .v6m/frontera/.
import re, io
rep = io.open('docs/loop/REPORTE.md', encoding='utf-8').read().split('\n')
ini = max(i for i, l in enumerate(rep) if l.startswith('# VUELTA 6 DEL FRENTE'))
rep = rep[ini:]
def tabla(lineas, marca):
    k = lineas.index(marca) + 2
    out = []
    while k < len(lineas) and lineas[k].startswith('|'):
        out.append(lineas[k]); k += 1
    return out
def rango(c):
    c = c.strip('* ')
    m = re.match(r'L(\d+)(?: a L(\d+))?$', c)
    a = int(m.group(1)); b = int(m.group(2) or a)
    return a, b
for cap in ('cap_16', 'cap_17'):
    marca = '<!-- TALLADO: salida=.v6m/frontera/%s_bruta.txt -->' % cap
    t_rep = tabla(rep, marca)
    bruta = io.open('.v6m/frontera/%s_bruta.txt' % cap, encoding='utf-8').read().split('\n')
    t_bru = [l for l in bruta if l.startswith('|')]
    fuente = io.open('fuentes/marquet_turn_the_ship/%s.md' % cap, encoding='utf-8').read().split('\n')
    pal = {i + 1: len(l.split()) for i, l in enumerate(fuente)}
    filas = [l for l in t_rep[2:] if not l.startswith('| **')]
    total = [l for l in t_rep[2:] if l.startswith('| **')]
    disc = 0; cubiertas = {}
    for f in filas:
        cel = [c.strip() for c in f.strip('|').split('|')]
        a, b = rango(cel[1]); n = int(cel[2])
        real = sum(pal[i] for i in range(a, b + 1))
        if real != n:
            disc += 1; print('   DISCREPA', cel[0], cel[1], n, real)
        for i in range(a, b + 1):
            cubiertas[i] = cubiertas.get(i, 0) + 1
    solapes = [i for i, v in cubiertas.items() if v > 1 and pal[i] > 0]
    sin_cubrir = [i for i in range(9, len(fuente) + 1) if pal.get(i, 0) > 0 and i not in cubiertas]
    cuerpo = sum(pal[i] for i in range(9, len(fuente) + 1))
    suma = sum(int([c.strip() for c in f.strip('|').split('|')][2]) for f in filas)
    print('%s: tabla del reporte == bruta: %s; filas %d; discrepancias de palabras %d; lineas con palabras solapadas %d; lineas con palabras sin cubrir %d; cuerpo desde L9 %d; suma de filas %d; fila de total: %s' % (
        cap, t_rep == t_bru, len(filas), disc, len(solapes), len(sin_cubrir), cuerpo, suma, total[0] if total else 'NINGUNA'))
