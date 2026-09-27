# -*- coding: utf-8 -*-
"""ACTA 77: las cifras de prosa de su 78.3 contadas sobre MI barrido sellado (.v78aud/vecinos_<id>.json): filas por encima de 0,4 de
similitud de texto por sede, la mayor, y candidatos con vecinos. Cuenta todas las clases con el mismo predicado y dice su suma (R7). Solo lee."""
import io, json, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
ids = [l.strip() for l in io.open('.v78aud/las20.txt', encoding='utf-8') if l.strip()]
c = collections.Counter(); mx = (0, None); con = collections.Counter()
for i in ids:
    j = json.load(io.open('.v78aud/vecinos_%s.json' % i, encoding='utf-8'))
    con['con vecinos' if j['vecinos'] else 'sin vecinos'] += 1
    for v in j['vecinos']:
        s = v['senales']['similitud_texto']
        c['%s, %s' % ('> 0,4' if s > 0.4 else '<= 0,4', v['sede'])] += 1
        if s > mx[0]: mx = (s, '%s > %s' % (i, v['id']))
print('candidatos: %s | suma: %d' % (dict(con), sum(con.values())))
print('filas dirigidas por similitud_texto y sede: %s | suma: %d' % (dict(sorted(c.items())), sum(c.values())))
print('la mayor: %.3f %s' % mx)
