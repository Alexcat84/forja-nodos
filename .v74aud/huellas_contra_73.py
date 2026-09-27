# -*- coding: utf-8 -*-
"""Fase ciega de la 74 (copia de .v73aud/huellas_contra_71.py con el fichero de huellas cambiado a la 73 y el grafo
anadido): las huellas de hoy de las fichas que siguen en las tres bandejas (Grove, Gerber, Marquet) y de
dataset/nodos.jsonl, contra las que tome yo en la fase ciega de la 73 antes de barrer (.v73aud/huellas_al_barrer.txt).
Dice cuantas son iguales, cuantas cambiaron y cuantas no estaban, por sede, con la suma (R7). Solo lee."""
import io, glob, hashlib, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
viejo = {}
for l in io.open('.v73aud/huellas_al_barrer.txt', encoding='utf-8'):
    h, f = l.strip().split(' *', 1); viejo[f] = h
c = collections.Counter(); cambio = []
fs = ['dataset/nodos.jsonl']
for b in ('grove_high_output', 'gerber_emyth', 'marquet_turn_the_ship'):
    fs += sorted(f.replace(chr(92), '/') for f in glob.glob('cuarentena/%s/*.json' % b))
for f in fs:
    sede = f.split('/')[1] if f.startswith('cuarentena/') else 'grafo'
    h = hashlib.sha1(open(f, 'rb').read()).hexdigest()
    e = 'no estaba' if f not in viejo else ('igual' if viejo[f] == h else 'CAMBIO')
    c[(sede, e)] += 1
    if e != 'igual': cambio.append((e, f))
falta = [f for f in viejo if f not in fs]
print('hoy contra .v73aud/huellas_al_barrer.txt: %s | suma: %d | en aquel fichero y hoy no: %d' % (dict(sorted(c.items())), sum(c.values()), len(falta)))
for e, f in cambio: print('  %s %s' % (e, f))
for f in falta: print('  YA NO ESTA %s' % f)
