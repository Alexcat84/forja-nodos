# -*- coding: utf-8 -*-
"""ACTA 72: los vecinos del barrido del extractor (.v73ext/vecinos_<id>.json) contra los de mi barrido sellado
(.v73aud/vecinos_<id>.json), fila dirigida a fila dirigida: id, sede, las tres seniales, levantada_por y detalle_paso.
Solo lee."""
import io, json, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
los7 = io.open('.v73aud/los7.txt', encoding='utf-8').read().split()
def filas(d):
    r = {}
    for i in los7:
        j = json.load(io.open('%s/vecinos_%s.json' % (d, i), encoding='utf-8'))
        for v in j['vecinos']:
            r[(i, v['id'])] = (v['sede'], tuple(sorted(v['senales'].items())), tuple(v['levantada_por']), v.get('detalle_paso'))
        r[(i, '_poblacion')] = (j['grafo'], j['bandejas'])
    return r
el, yo = filas('.v73ext'), filas('.v73aud')
c = collections.Counter('identica' if el.get(k) == yo.get(k) else ('solo suya' if k not in yo else ('solo mia' if k not in el else 'difiere')) for k in set(el) | set(yo) if k[1] != '_poblacion')
print('filas dirigidas: suyas %d | mias %d' % (sum(1 for k in el if k[1] != '_poblacion'), sum(1 for k in yo if k[1] != '_poblacion')))
print('por estado: %s | suma: %d' % (dict(c), sum(c.values())))
p = collections.Counter('igual' if el[(i, '_poblacion')] == yo[(i, '_poblacion')] else 'distinta' for i in los7)
print('poblacion por candidato (grafo, bandejas) igual en los dos: %s | suma: %d | %s' % (dict(p), sum(p.values()), sorted(set(yo[(i, '_poblacion')] for i in los7))))
for k in sorted(set(el) | set(yo)):
    if el.get(k) != yo.get(k): print('  ', k, el.get(k), yo.get(k))
