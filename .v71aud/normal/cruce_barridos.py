# ACTA 70: mi barrido de la fase ciega (.v71aud/vecinos_*.json) contra el del extractor (.v71ext/vecinos_*.json),
# fila dirigida a fila dirigida, con sus seniales. Solo lee.
import json, io, collections
ids = [l.strip() for l in io.open('.v71aud/los20.txt', encoding='utf-8') if l.strip()]
def filas(d):
    out = {}
    for c in ids:
        j = json.load(io.open('%s/vecinos_%s.json' % (d, c), encoding='utf-8'))
        for v in j['vecinos']:
            out[(c, v.get('id') or v.get('vecino'))] = json.dumps(v, sort_keys=True)
    return out, j
m, jm = filas('.v71aud'); s, js = filas('.v71ext')
est = collections.Counter()
for k in set(m) | set(s):
    if k in m and k in s: est['en los dos, ' + ('igual con sus seniales' if m[k] == s[k] else 'seniales distintas')] += 1
    elif k in m: est['solo mia'] += 1
    else: est['solo suya'] += 1
print('filas dirigidas: mias %d | suyas %d' % (len(m), len(s)))
print('por estado:', dict(est), '| suma:', sum(est.values()))
for k in sorted(set(m) ^ set(s)): print('  ', k)
