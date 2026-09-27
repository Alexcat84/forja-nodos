# -*- coding: utf-8 -*-
"""Fase ciega de la 80, sin git (copia libre de .v77aud/huellas_hoy.py con la tanda de Marquet): las 21 huellas que tome
al lanzar mi barrido de la 78 (.v78aud/huellas_al_barrer.txt: las 20 fichas de Marquet y el grafo) contra los ficheros de
HOY. Una ficha de la bandeja que ya no esta en su sitio se busca en cuarentena/_insertados/marquet_turn_the_ship/ con su
mismo nombre (D.31 la mueve alli al insertarla). El grafo no se compara aqui: lo mide .v80aud/grafo_sin_tanda.py.
Reparte por estado, con su suma (R7). Solo lee."""
import io, os, hashlib, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
BAN, INS = 'cuarentena/marquet_turn_the_ship/', 'cuarentena/_insertados/marquet_turn_the_ship/'
las20 = set(io.open('.v78aud/las20.txt', encoding='utf-8').read().split())
sha = lambda r: hashlib.sha1(open(r, 'rb').read()).hexdigest()
c = collections.Counter(); malas = []; movidas = set()
for l in io.open('.v78aud/huellas_al_barrer.txt', encoding='utf-8'):
    h, r = l.strip().split(' *', 1)
    if r == 'dataset/nodos.jsonl': c['grafo, aparte'] += 1; continue
    if os.path.exists(r): donde = r; est = 'en la bandeja'
    elif r.startswith(BAN) and os.path.exists(INS + r[len(BAN):]):
        donde = INS + r[len(BAN):]; est = 'movida a _insertados'; movidas.add(os.path.basename(r)[:-5])
    else: c['NO ESTA'] += 1; malas.append(r); continue
    if sha(donde) == h: c[est + ', misma huella'] += 1
    else: c[est + ', HUELLA DISTINTA'] += 1; malas.append(donde)
print('huellas: %d | %s | suma: %d' % (sum(c.values()), dict(sorted(c.items())), sum(c.values())))
extra = sorted(f[:-5] for f in os.listdir(INS) if f.endswith('.json') and f[:-5] not in las20)
print('movidas a _insertados: %d | son las 20 de .v78aud/las20.txt: %s | fichas en _insertados de Marquet fuera de ellas: %s' % (
    len(movidas), 'SI' if movidas == las20 else 'NO', extra))
print('fichas que quedan en la bandeja de Marquet: %d' % len([f for f in os.listdir(BAN) if f.endswith('.json')]))
print('ficheros que no cuadran: %s' % malas)
