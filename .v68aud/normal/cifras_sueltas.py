# -*- coding: utf-8 -*-
"""ACTA 67: tres cifras de su 68.3 contadas por instrumento. (1) filas y pares SOSTENGO / NO SOSTENGO de .v68ext/aristas_lectura.txt;
(2) pares dirigidos de .v68aud/vecinos_tabla.txt con los dos extremos en cap_05, y su similitud de texto minima y maxima;
(3) la linea de poblacion de las dos salidas de insertar."""
import io, re, glob, sys
sys.stdout.reconfigure(encoding="utf-8")
filas = {'SOSTENGO': 0, 'NO SOSTENGO': 0}; pares = {'SOSTENGO': 0, 'NO SOSTENGO': 0}
for l in io.open('.v68ext/aristas_lectura.txt', encoding='utf-8'):
    if l.startswith('#') or '|' not in l: continue
    c = [x.strip() for x in l.split('|')]
    if c[0] in filas:
        filas[c[0]] += 1; pares[c[0]] += len(c[2].split(','))
print('aristas_lectura.txt: filas %s | pares %s' % (filas, pares))
cap05 = []
for l in io.open('.v68aud/los20.txt', encoding='utf-8'):
    if l.strip(): cap05.append(l.strip())
cap05 = set(cap05[:12])
sims = []
for l in io.open('.v68aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +> (\S+) +\S+ +\S+ +([\d.]+) +([\d.]+) +([\d.]+)', l)
    if m and m.group(1) in cap05 and m.group(2) in cap05: sims.append(float(m.group(3)))
print('pares dirigidos entre dos de cap_05: %d | similitud de texto min %.3f max %.3f' % (len(sims), min(sims), max(sims)))
for f in sorted(glob.glob('.v68ext/insertar_2*_*.txt')):
    L = io.open(f, encoding='utf-8').read().split('\n')
    for i, l in enumerate(L, 1):
        if 'poblacion' in l.lower() or 'grafo' in l and 'bandeja' in l: print('%s linea %d: %s' % (f.split('/')[-1][:30], i, l.strip()[:150])); break
