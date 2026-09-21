# -*- coding: utf-8 -*-
"""Mi propio recuento de pasos por capitulo sobre la bandeja de grove_high_output.
El capitulo se lee del primer 'cap_NN.md' que aparece en el fichero, que es el
mismo camino que el extractor uso en VV.2 y que puedo correr yo."""
import json, glob, os, re, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
por_cap = collections.defaultdict(lambda: [0, 0])
detalle = []
for r in sorted(glob.glob('cuarentena/grove_high_output/*.json')):
    crudo = open(r, encoding='utf-8').read()
    d = json.loads(crudo)
    m = re.search(r'cap_(\d+)\.md', crudo)
    cap = 'cap_%s' % m.group(1) if m else 'SIN CAPITULO'
    n = len(d.get('pasos_accionables', []))
    por_cap[cap][0] += 1
    por_cap[cap][1] += n
    detalle.append((cap, os.path.basename(r)[:-5], n))
print('%-14s %10s %8s' % ('capitulo', 'candidatos', 'pasos'))
tc = tp = 0
for cap in sorted(por_cap):
    c, p = por_cap[cap]
    tc += c; tp += p
    print('%-14s %10d %8d' % (cap, c, p))
print('%-14s %10d %8d' % ('TOTAL BANDEJA', tc, tp))
print()
print('LOS DE cap_07 Y cap_10, UNO A UNO:')
for cap, n, p in sorted(detalle):
    if cap in ('cap_07', 'cap_10'):
        print('  %-8s %-60s pasos=%d' % (cap, n, p))
