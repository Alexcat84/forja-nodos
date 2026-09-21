# -*- coding: utf-8 -*-
"""LAS 8 FICHAS DE cap_04 QUE DECLARAN MAS PALABRAS QUE SU RANGO: de donde puede salir la cifra."""
import io, sys, re, json, glob, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
L = io.open('fuentes/grove_high_output/cap_04.md', encoding='utf-8').read().split('\n')
def pal(a, b):
    return sum(len(L[i - 1].split()) for i in range(a, b + 1))

CASOS = []
for f in sorted(glob.glob('cuarentena/grove_high_output/*.json')):
    d = json.loads(io.open(f, encoding='utf-8').read())
    r = d.get('resumen_teorico', '')
    if 'cap_04.md' not in r:
        continue
    for m in re.finditer(r'PIEZA (P\d+[a-z]?)[^.;]{0,90}?L(\d+)(?: a L(\d+))?, ([\d.]+) palabras', r):
        pz, a, b, w = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2)), int(m.group(4).replace('.', ''))
        CASOS.append((os.path.basename(f)[:-5], pz, a, b, w))

print("%-52s %-5s %-14s %6s %6s  %s" % ("ficha", "pieza", "rango declarado", "dice", "cuento", "que rango daria la cifra declarada"))
malos = 0
for nombre, pz, a, b, w in CASOS:
    c = pal(a, b)
    explica = "-- cuadra --"
    if c != w:
        malos += 1
        explica = "ninguno cercano"
        for ini in range(max(1, a - 8), a + 1):
            for fin in range(b, min(len(L), b + 12) + 1):
                if pal(ini, fin) == w:
                    explica = "L%d a L%d" % (ini, fin)
                    break
            if explica != "ninguno cercano":
                break
    print("%-52s %-5s L%-4d a L%-4d %6d %6d  %s" % (nombre[:52], pz, a, b, w, c, explica))
print()
print("piezas declaradas leidas: %d ; cuadran %d ; discrepan %d" % (len(CASOS), len(CASOS) - malos, malos))
