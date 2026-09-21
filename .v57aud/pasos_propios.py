# -*- coding: utf-8 -*-
"""MI propio recuento de pasos por capitulo sobre la bandeja de grove_high_output
(AUDITOR_FORJA.md 8.3.1: la cifra de volumen no se copia, se cuenta).
Mismo camino que .v56aud/pasos_propios.py: el capitulo se lee del primer
'cap_NN.md' que aparece en el fichero. Instrumento REUSADO, no nuevo (D.47)."""
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
print('LOS TRES CAPITULOS DE LA VUELTA 56, UNO A UNO:')
for cap in ('cap_08', 'cap_09', 'cap_10'):
    c, p = por_cap.get(cap, [0, 0])
    print('  %-8s candidatos=%d  pasos=%d  %s' % (cap, c, p, 'SIN SUPERFICIE' if p == 0 else ''))
    for ca, n, pa in sorted(detalle):
        if ca == cap:
            print('      %-62s pasos=%d' % (n, pa))
print()
print('LA POBLACION QUE EL BARRIDO DE LA ADUANA DICE MEDIR (D.38.4), contada por mi:')
graf = sum(1 for _ in open('dataset/nodos.jsonl', encoding='utf-8'))
band = 0
for d in sorted(glob.glob('cuarentena/*')):
    if not os.path.isdir(d) or os.path.basename(d).startswith('_'):
        continue
    n = len([x for x in glob.glob(os.path.join(d, '*.json'))])
    if n:
        print('  bandeja %-34s %4d' % (os.path.basename(d), n))
        band += n
print('  grafo dataset/nodos.jsonl                %4d' % graf)
print('  POBLACION                                %4d' % (graf + band))
