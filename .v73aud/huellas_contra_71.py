# -*- coding: utf-8 -*-
"""Fase ciega de la 73, sin git: las huellas de hoy de las fichas que siguen en las tres bandejas (Grove, Gerber, Marquet),
contra las que tome yo en la fase ciega de la 71 antes de barrer (.v71aud/huellas_al_barrer.txt). Dice cuantas son iguales,
cuantas cambiaron y cuantas no estaban, por bandeja, con la suma (R7). Solo lee."""
import io, glob, hashlib, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
viejo = {}
for l in io.open('.v71aud/huellas_al_barrer.txt', encoding='utf-8'):
    h, f = l.strip().split(' *', 1); viejo[f] = h
c = collections.Counter(); cambio = []
for b in ('grove_high_output', 'gerber_emyth', 'marquet_turn_the_ship'):
    for f in sorted(glob.glob('cuarentena/%s/*.json' % b)):
        f = f.replace(chr(92), '/')
        h = hashlib.sha1(open(f, 'rb').read()).hexdigest()
        e = 'no estaba' if f not in viejo else ('igual' if viejo[f] == h else 'CAMBIO')
        c[(b, e)] += 1
        if e != 'igual': cambio.append((e, f))
print('fichas de hoy contra .v71aud/huellas_al_barrer.txt: %s | suma: %d' % (dict(sorted(c.items())), sum(c.values())))
for e, f in cambio: print('  %s %s' % (e, f))
