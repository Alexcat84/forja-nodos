# -*- coding: utf-8 -*-
"""La tanda de la vuelta 42 en bitacora/VEREDICTOS.jsonl: de la linea 515 (la 514
era el cierre de la vuelta 41, segun .v42/estado.py del encargo) hasta el final."""
import json, io, collections
lineas = [l for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip()]
print('lineas totales: %d   tanda = 515..%d  (%d lineas)' % (len(lineas), len(lineas), len(lineas) - 514))
c = collections.Counter(); sin_razon = []; con_arista = []; disc = []
for i, l in enumerate(lineas[514:], start=515):
    d = json.loads(l)
    v = d.get('veredicto', '(sin campo)')
    c[v] += 1
    if not (d.get('razon') or '').strip():
        sin_razon.append(i)
    if (d.get('arista') or '').strip():
        con_arista.append((i, d.get('arista')))
    if 'DISCUTIBLE' in (d.get('razon') or '') or d.get('discutible'):
        disc.append(i)
print()
for k, n in sorted(c.items(), key=lambda x: -x[1]):
    print('  %-12s %d' % (k, n))
print()
print('sin razon escrita       : %s' % (sin_razon or 'NINGUNA'))
print('con campo arista escrito: %d  %s' % (len(con_arista), [a for a, _ in con_arista] or 'NINGUNA'))
print('razon que dice DISCUTIBLE: %d  %s' % (len(disc), disc or 'NINGUNA'))
