# -*- coding: utf-8 -*-
import io, json, os, re, collections
D = 'cuarentena/scott_radical_candor'
c = collections.Counter(); det = collections.defaultdict(list)
for f in sorted(os.listdir(D)):
    if not f.endswith('.json'): continue
    d = json.load(io.open(os.path.join(D, f), encoding='utf-8'))
    rt = d.get('resumen_teorico') or ''
    m = re.search(r'fuentes/[a-z_]+/(cap_\d+)\.md', rt)
    cap = m.group(1) if m else 'SIN CAPITULO'
    lin = re.search(r'l[ií]neas? (\d+)\s*(?:a|-|hasta)\s*(\d+)', rt)
    c[cap] += 1
    det[cap].append((int(lin.group(1)) if lin else 10**9, d['id'], len(d['pasos_accionables'])))
print('BANDEJA %s: %d ficheros' % (D, sum(c.values())))
for k in sorted(c): print('  %-14s %3d' % (k, c[k]))
print()
for k in sorted(det):
    if k != 'cap_09': continue
    print('LOS QUE QUEDAN DE cap_09 EN BANDEJA:')
    for a, i, p in sorted(det[k]):
        print('  linea %-6s %-52s %2d pasos' % (a if a < 10**9 else '?', i, p))
