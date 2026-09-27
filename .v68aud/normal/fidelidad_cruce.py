# -*- coding: utf-8 -*-
"""ACTA 67: mi fidelidad sellada de la fase ciega (.v68aud/fidelidad.tsv, tabuladores) contra la del extractor
(.v68ext/fidelidad.tsv, barras), paso a paso: marca, capitulo y linea. Imprime cada paso donde difieren y las de DUDA mia."""
import io, collections
M = {}
for l in io.open('.v68aud/fidelidad.tsv', encoding='utf-8'):
    c = l.rstrip('\n').split('\t')
    if c[0] == 'id' or len(c) < 5: continue
    M[(c[0], int(c[1]))] = (c[2], c[3], c[4])
E = {}; disc = {}
for l in io.open('.v68ext/fidelidad.tsv', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    c = [x.strip() for x in l.rstrip('\n').split('|')]
    try: k = (c[0], int(c[1]))
    except: continue
    E[k] = c
print('filas mias: %d | filas suyas: %d | pasos en las dos: %d | solo mias: %s | solo suyas: %s' % (
    len(M), len(E), len(set(M) & set(E)), sorted(set(M) - set(E)), sorted(set(E) - set(M))))
cnt = collections.Counter()
for k in sorted(set(M) & set(E), key=lambda k: (k[0], k[1])):
    mia = M[k][0]; suya = E[k][2]
    cnt[(mia, suya)] += 1
    lin_m = M[k][2].lstrip('L'); lin_s = ''.join(ch for ch in E[k][4] if ch.isdigit() or ch == ',') if len(E[k]) > 4 else ''
    if mia != suya or mia == 'D' or 'DISCUTIBLE' in '|'.join(E[k]):
        print('  %-52s paso %2d | mia %s %s | suya %s | %s' % (k[0], k[1], mia, M[k][2], suya, '|'.join(E[k][3:6])[:90]))
print('pares de marca (mia, suya): %s' % dict(cnt))
dl = [(k, M[k][2], E[k][3]) for k in sorted(set(M) & set(E)) if M[k][2].strip() != E[k][3].strip()]
print('pasos con la linea del libro distinta entre las dos lecturas: %d %s' % (len(dl), dl))
