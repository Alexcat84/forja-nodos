# -*- coding: utf-8 -*-
"""ACTA 77: mi barrido de la fase ciega (.v78aud/vecinos_<id>.json) contra el suyo (.v78ext/vecinos_<id>.json), fila dirigida a fila
dirigida con sede, seniales y quien la levanta; y sus lineas de .v78ext/veredictos_listos.txt contra mis clases selladas
(.v78aud/mis_clases.tsv, un par sin orden por fila). Cuenta todas las clases con el mismo predicado y dice su suma (R7). Solo lee."""
import io, json, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
ids = [l.strip() for l in io.open('.v78aud/las20.txt', encoding='utf-8') if l.strip()]
def filas(d):
    r = {}
    for i in ids:
        j = json.load(io.open('%s/vecinos_%s.json' % (d, i), encoding='utf-8'))
        for v in j['vecinos']:
            r[(i, v['id'])] = (v['sede'], tuple(sorted(v['senales'].items())), tuple(v['levantada_por']))
        r[(i, '__pob')] = (j['grafo'], j['bandejas'])
    return r
m, s = filas('.v78aud'), filas('.v78ext')
pob = collections.Counter('%s' % (m[(i, '__pob')] == s[(i, '__pob')]) for i in ids)
print('poblacion igual por candidato: %s | suma: %d' % (dict(pob), sum(pob.values())))
fm = {k: v for k, v in m.items() if k[1] != '__pob'}; fs = {k: v for k, v in s.items() if k[1] != '__pob'}
c = collections.Counter()
for k in set(fm) | set(fs):
    if k not in fs: c['solo mia'] += 1
    elif k not in fm: c['solo suya'] += 1
    else: c['igual en sede, seniales y quien la levanta' if fm[k] == fs[k] else 'distinta'] += 1
print('filas dirigidas: mias %d | suyas %d | %s | suma: %d' % (len(fm), len(fs), dict(c), sum(c.values())))
# sus lineas
lin, cand = {}, None
for l in io.open('.v78ext/veredictos_listos.txt', encoding='utf-8'):
    l = l.rstrip('\r\n')
    if l.startswith('## '): cand = l[3:].strip(); continue
    if not l or l.startswith('#'): continue
    p = l.split('|')
    lin[(cand, p[0].strip())] = p[1].strip()
print('sus lineas: %d | por clase: %s | suma: %d' % (len(lin), dict(collections.Counter(lin.values())), len(lin)))
print('sus lineas contra mis filas dirigidas: iguales en el conjunto: %s' % ('SI' if set(lin) == set(fm) else 'NO'))
mc = {}
for l in io.open('.v78aud/mis_clases.tsv', encoding='utf-8'):
    p = l.rstrip('\r\n').split('\t')
    if p[0] == 'a' or len(p) < 3: continue
    mc[frozenset((p[0], p[1]))] = (p[2], p[3] if len(p) > 3 else '')
k2 = collections.Counter(); dif = []
for (a, b), cl in lin.items():
    mine = mc.get(frozenset((a, b)))
    if mine is None: k2['sin fila mia'] += 1; dif.append((a, b, cl, None)); continue
    if mine[0] == cl: k2['su clase es la mia'] += 1
    else: k2['clase distinta'] += 1; dif.append((a, b, cl, mine))
print('sus lineas contra mis clases selladas: %s | suma: %d | distintas: %s' % (dict(k2), sum(k2.values()), dif))
