# -*- coding: utf-8 -*-
"""Fase ciega de la 76, sin git (copia de la idea de .v75aud/huellas_hoy.py, con la bandeja de Gerber y la de Marquet): las
huellas que tome al lanzar mi barrido de la 73 (.v73aud/huellas_al_barrer.txt) contra los ficheros de HOY, solo de las fichas
de gerber_emyth y marquet_turn_the_ship. Reparte por bandeja y por estado, con su suma (R7), y nombra las que cambiaron. Solo lee."""
import io, os, hashlib, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
sha = lambda r: hashlib.sha1(open(r, 'rb').read()).hexdigest()
c = collections.Counter(); cambian = []
for l in io.open('.v73aud/huellas_al_barrer.txt', encoding='utf-8'):
    h, r = l.strip().split(' *', 1)
    if not (r.startswith('cuarentena/gerber_emyth/') or r.startswith('cuarentena/marquet_turn_the_ship/')): continue
    b = r.split('/')[1]
    if not os.path.exists(r): c[b + ', NO ESTA'] += 1; continue
    if sha(r) == h: c[b + ', igual'] += 1
    else: c[b + ', CAMBIA'] += 1; cambian.append(r)
hoy = collections.Counter(b for b in ('gerber_emyth', 'marquet_turn_the_ship') for f in os.listdir('cuarentena/' + b) if f.endswith('.json'))
print('fichas hoy: %s | suma: %d' % (dict(hoy), sum(hoy.values())))
print('contra mis huellas de la 73: %s | suma: %d' % (dict(sorted(c.items())), sum(c.values())))
for r in cambian: print('  CAMBIA:', r)
