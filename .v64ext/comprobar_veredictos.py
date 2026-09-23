# -*- coding: utf-8 -*-
"""Vuelta 64: comprueba .v64ext/veredictos_listos.txt contra dos cosas, sin tocar nada.
1. Cada linea la acepta src/aduana.py parsear_veredicto (el mismo parser de --veredicto).
2. Los vecinos de cada seccion son EXACTAMENTE los que la senial levanta HOY en el sentido
   candidato -> vecino segun .v64ext/pares_despues.txt: ni falta uno, ni sobra uno que la
   senial ya no levanta (ese se registraria como lectura declarada, no como veredicto)."""
import io, os, re, sys, collections
sys.path.insert(0, os.getcwd())
from src import aduana
sec = collections.OrderedDict()
actual = None
for l in io.open('.v64ext/veredictos_listos.txt', encoding='utf-8'):
    l = l.rstrip('\n')
    if l.startswith('## '):
        actual = l[3:].strip(); sec[actual] = []
    elif l.strip() and not l.startswith('#'):
        sec[actual].append(l)
hoy = collections.defaultdict(set)
no_levanta = collections.defaultdict(set)
for l in io.open('.v64ext/pares_despues.txt', encoding='utf-8'):
    c = l.split()
    if len(c) < 4 or c[0] not in ('d005', 'd140', 'lectura'):
        continue
    (no_levanta if l.rstrip().endswith('NO LEVANTA') else hoy)[c[1]].add(c[2])
total = malas = 0
for cand, lineas in sec.items():
    vistos = []
    for l in lineas:
        try:
            v = aduana.parsear_veredicto(l)
            vistos.append(v['vecino'])
            total += 1
            print('  OK  %-48s %-48s %-9s %s' % (cand, v['vecino'], v['clase'], ('madre=' + v['madre']) if v['madre'] else ''))
        except aduana.Rechazo as r:
            malas += 1
            print('  MAL %-48s %s' % (cand, r.titulo))
    falta = sorted(hoy[cand] - set(vistos))
    sobra = sorted(set(vistos) - hoy[cand])
    print('%-50s lineas %d | levantados hoy %d | FALTAN %s | SOBRAN %s | medidos y ya no levantan %s' % (
        cand, len(lineas), len(hoy[cand]), falta or '0', sobra or '0', sorted(no_levanta[cand]) or '0'))
print('secciones %d, lineas %d, ilegibles %d' % (len(sec), total + malas, malas))
