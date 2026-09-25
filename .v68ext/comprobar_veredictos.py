# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 68 de .v67ext/comprobar_veredictos.py (que era COPIA de la 66 de .v64ext/comprobar_veredictos.py),
con las rutas cambiadas de .v66ext a .v68ext y la lista de los 22 de cap_04 a los 20 de cap_05 y cap_06
(.v68ext/los20_cap05_cap06.txt). Lee el barrido de hoy, .v68ext/vecinos_<id>.json (TAREA 3.2 de la 68).
Comprueba .v68ext/veredictos_listos.txt contra dos cosas, sin tocar nada:
1. Cada linea la acepta src/aduana.py parsear_veredicto (el mismo parser de --veredicto).
2. Los vecinos de cada seccion son EXACTAMENTE los que la senial levanta HOY en el sentido candidato a vecino:
   ni falta uno, ni sobra uno.
Y lo que la copia anade, porque la sede de las aristas por lectura dice que ninguna senial las levanta: para cada
SOSTENGO de .v68ext/aristas_lectura.txt, si el barrido de hoy levanta el par en algun sentido (deberia salir NO)."""
import glob, io, json, os, sys, collections
sys.path.insert(0, os.getcwd())
from src import aduana
sec = collections.OrderedDict()
actual = None
for l in io.open('.v68ext/veredictos_listos.txt', encoding='utf-8'):
    l = l.rstrip('\n')
    if l.startswith('## '):
        actual = l[3:].strip(); sec[actual] = []
    elif l.strip() and not l.startswith('#'):
        sec[actual].append(l)
hoy = collections.defaultdict(set)
for f in sorted(glob.glob('.v68ext/vecinos_*.json')):
    d = json.load(io.open(f, encoding='utf-8'))
    hoy[d['id']] = set(v['id'] for v in d['vecinos'])
los22 = [l.split()[0] for l in io.open('.v68ext/los20_cap05_cap06.txt', encoding='utf-8') if l.strip() and not l.startswith('#')]
total = malas = faltan_t = sobran_t = 0
for cand in los22:
    lineas = sec.get(cand)
    if lineas is None:
        print('SIN SECCION %s' % cand); malas += 1; continue
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
    faltan_t += len(falta); sobran_t += len(sobra)
    print('%-50s lineas %d | levantados hoy %d | FALTAN %s | SOBRAN %s' % (
        cand, len(lineas), len(hoy[cand]), falta or '0', sobra or '0'))
print('secciones %d de %d, lineas %d, ilegibles %d, vecinos sin linea %d, lineas sin vecino %d' % (
    len([c for c in los22 if c in sec]), len(los22), total + malas, malas, faltan_t, sobran_t))
print()
print('ARISTAS POR LECTURA (SOSTENGO) contra el barrido de hoy')
for l in io.open('.v68ext/aristas_lectura.txt', encoding='utf-8'):
    if not l.startswith('SOSTENGO'):
        continue
    p = [c.strip() for c in l.split('|')]
    m, h = p[1], p[2]
    lev = (m in hoy.get(h, set())) or (h in hoy.get(m, set()))
    print('  %-50s > %-52s levantada hoy: %s' % (m, h, 'SI' if lev else 'NO'))
