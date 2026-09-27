# ACTA 70: las seniales de las filas de vecino con extremo en el grafo, del barrido de mi fase ciega (.v71aud/vecinos_*.json). Solo lee.
import json, io, glob
for f in sorted(glob.glob('.v71aud/vecinos_*.json')):
    d = json.load(io.open(f, encoding='utf-8'))
    for v in d['vecinos']:
        if v['sede'] == 'grafo':
            print('%-58s %-48s %s %s' % (d['id'], v['id'], v['levantada_por'], v['senales']))
