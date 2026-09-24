import re, sys, subprocess

def lineas_palabras(path):
    d = {}
    with open(path, encoding='utf-8') as f:
        for i, ln in enumerate(f, 1):
            n = len(ln.split())
            if i >= 8 and n > 0:
                d[i] = n
    return d

def parse_tabla(reporte, ini, fin):
    filas = []
    with open(reporte, encoding='utf-8') as f:
        ls = f.readlines()
    for ln in ls[ini-1:fin]:
        ln = ln.strip()
        if not ln.startswith('|'):
            continue
        cols = [c.strip() for c in ln.strip('|').split('|')]
        if len(cols) < 5:
            continue
        pieza = cols[0].replace('*','').strip()
        lineas = cols[1].replace('*','').strip()
        pal = cols[2].replace('*','').strip()
        if not re.match(r'^(R\d+|P\d+)$', pieza):
            continue
        filas.append((pieza, lineas, pal))
    return filas

def expande(spec):
    # ej: "L55, L73 a L93"  o "L9"
    out = []
    for parte in spec.split(','):
        parte = parte.strip().replace('`','')
        m = re.match(r'^L(\d+)\s+a\s+L(\d+)$', parte)
        if m:
            out.extend(range(int(m.group(1)), int(m.group(2))+1))
            continue
        m = re.match(r'^L(\d+)$', parte)
        if m:
            out.append(int(m.group(1)))
            continue
        raise ValueError('no parseo: '+repr(parte))
    return out

cap, path, ini, fin = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
wp = lineas_palabras(path)
filas = parse_tabla('docs/loop/REPORTE.md', ini, fin)
print('CAP', cap, ' filas de tabla parseadas:', len(filas))
cubiertas = {}
total = 0
malas = []
for pieza, lineas, pal in filas:
    ls = expande(lineas)
    suma = sum(wp.get(l, 0) for l in ls)
    try:
        declar = int(pal)
    except ValueError:
        malas.append((pieza, lineas, pal, 'palabras no numericas'))
        continue
    total += declar
    if suma != declar:
        malas.append((pieza, lineas, declar, suma))
    for l in ls:
        if l in cubiertas:
            malas.append((pieza, 'SOLAPE en L%d con %s' % (l, cubiertas[l]), '', ''))
        cubiertas[l] = pieza
print('  suma de palabras declaradas :', total)
print('  cuerpo real (L8+, wc -w)    :', sum(wp.values()))
sincubrir = sorted(set(wp) - set(cubiertas))
print('  lineas con palabras sin cubrir:', len(sincubrir), sincubrir[:20])
print('  DISCREPANCIAS fila a fila   :', len(malas))
for m in malas:
    print('   ', m)
print('  PIEZAS contadas por mi      :', len(filas))
