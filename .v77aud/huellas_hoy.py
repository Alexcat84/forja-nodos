# -*- coding: utf-8 -*-
"""Fase ciega de la 77, sin git (copia de .v75aud/huellas_hoy.py con las rutas de la 76): las 43 huellas que tome al
lanzar mi barrido de la 76 (.v76aud/huellas_al_barrer.txt: las 22 fichas de Gerber, las 20 de Marquet y el grafo) contra
los ficheros de HOY. Una ficha de la bandeja de Gerber que ya no esta en su sitio se busca en
cuarentena/_insertados/gerber_emyth/ con su mismo nombre (D.31 la mueve alli al insertarla). El grafo no se compara
aqui: lo mide .v77aud/grafo_sin_tanda.py. Reparte por bandeja y por estado, con su suma (R7). Solo lee."""
import io, os, hashlib, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
BAN, INS = 'cuarentena/gerber_emyth/', 'cuarentena/_insertados/gerber_emyth/'
las22 = set(io.open('.v76aud/las22.txt', encoding='utf-8').read().split())
sha = lambda r: hashlib.sha1(open(r, 'rb').read()).hexdigest()
c = collections.Counter(); malas = []; movidas = set()
for l in io.open('.v76aud/huellas_al_barrer.txt', encoding='utf-8'):
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
extra = sorted(f[:-5] for f in os.listdir(INS) if f.endswith('.json') and f[:-5] not in las22)
print('movidas a _insertados: %d | son las 22 de .v76aud/las22.txt: %s | fichas en _insertados de Gerber fuera de ellas: %s' % (
    len(movidas), 'SI' if movidas == las22 else 'NO', extra))
print('ficheros que no cuadran: %s' % malas)
