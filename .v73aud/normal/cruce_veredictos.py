# -*- coding: utf-8 -*-
"""ACTA 72: las 29 lineas de .v73ext/veredictos_listos.txt (una por fila dirigida del barrido, candidato > vecino) contra mis
clases selladas (.v73aud/mis_clases.tsv, una por par sin orden). Cada linea se lee con src/aduana.py parsear_veredicto, el
parser de --veredicto. Compara clase y madre; imprime el reparto con su suma y cada par que difiere. Solo lee."""
import io, os, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.getcwd())
from src import aduana
mias = {}
for l in io.open('.v73aud/mis_clases.tsv', encoding='utf-8'):
    c = l.rstrip('\n').split('\t')
    if c[0] == 'a' or len(c) < 4: continue
    mias[frozenset((c[0], c[1]))] = (c[2], c[3] or None)
suyas, cand = collections.defaultdict(list), None
for l in io.open('.v73ext/veredictos_listos.txt', encoding='utf-8'):
    l = l.rstrip('\n')
    if l.startswith('## '): cand = l[3:].strip(); continue
    if not l.strip() or l.startswith('#'): continue
    v = aduana.parsear_veredicto(l)
    vid = v.get('vecino') or v.get('id') or l.split('|')[0]
    madre = v.get('madre') or (l.split('|')[2][6:] if l.split('|')[1] == 'CONTINUA' else None)
    suyas[frozenset((cand, vid))].append((l.split('|')[1], madre))
print('lineas suyas: %d | pares sin orden: %d | mis pares: %d' % (sum(len(x) for x in suyas.values()), len(suyas), len(mias)))
cl = collections.Counter(x[0] for xs in suyas.values() for x in xs)
print('lineas por clase: %s | suma: %d' % (dict(cl), sum(cl.values())))
inc = [p for p, xs in suyas.items() if len(set(xs)) > 1]
print('pares con sus dos lineas en distinta clase o madre: %d' % len(inc))
est = collections.Counter()
dif = []
for p in set(suyas) | set(mias):
    if p not in mias: est['sin fila mia'] += 1; dif.append(p); continue
    if p not in suyas: est['sin linea suya'] += 1; dif.append(p); continue
    s = suyas[p][0]
    if s == mias[p]: est['igual clase y madre'] += 1
    else: est['difiere'] += 1; dif.append(p)
print('pares: %s | suma: %d' % (dict(est), sum(est.values())))
for p in dif: print('  %s | suya %s | mia %s' % (' ~ '.join(sorted(p)), suyas.get(p), mias.get(p)))
