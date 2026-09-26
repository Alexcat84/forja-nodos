# -*- coding: utf-8 -*-
"""Fase ciega de la 72, sin git (copia de .v70aud/huellas_hoy.py con las rutas de la 71): las 70 huellas que tome al
lanzar mi barrido de la 71 (.v71aud/huellas_al_barrer.txt: las fichas de las tres bandejas y el grafo) contra los
ficheros de HOY. Una ficha de la bandeja de Grove que ya no esta en su sitio se busca en
cuarentena/_insertados/grove_high_output/ con su mismo nombre (D.31 la mueve alli al insertarla). El grafo no se compara
aqui: lo mide .v72aud/grafo_sin_tanda.py. Reparte por bandeja y por estado, con su suma (R7). Solo lee."""
import io, os, hashlib, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
BAN, INS = 'cuarentena/grove_high_output/', 'cuarentena/_insertados/grove_high_output/'
los20 = set(io.open('.v71aud/los20.txt', encoding='utf-8').read().split())
sha = lambda r: hashlib.sha1(open(r, 'rb').read()).hexdigest()
c = collections.Counter(); malas = []; movidas = set()
for l in io.open('.v71aud/huellas_al_barrer.txt', encoding='utf-8'):
    h, r = l.strip().split(' *', 1)
    if r == 'dataset/nodos.jsonl': c['grafo, aparte'] += 1; continue
    b = r.split('/')[1]
    if os.path.exists(r): donde = r; est = 'en su sitio'
    elif r.startswith(BAN) and os.path.exists(INS + r[len(BAN):]):
        donde = INS + r[len(BAN):]; est = 'movida a _insertados'; movidas.add(os.path.basename(r)[:-5])
    else: c[b + ', NO ESTA'] += 1; malas.append(r); continue
    if sha(donde) == h: c[b + ', ' + est + ', misma huella'] += 1
    else: c[b + ', ' + est + ', HUELLA DISTINTA'] += 1; malas.append(donde)
print('huellas: %d | suma: %d' % (sum(c.values()), sum(c.values())))
for k in sorted(c): print('  %s: %d' % (k, c[k]))
print('movidas a _insertados: %d | son las 20 de .v71aud/los20.txt: %s | fuera de ellas: %s' % (
    len(movidas), 'SI' if movidas == los20 else 'NO', sorted(movidas - los20)))
print('ficheros que no cuadran: %s' % malas)
