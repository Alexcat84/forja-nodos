# -*- coding: utf-8 -*-
"""ACTA 65: mis 53 clases selladas (.v66aud/mis_clases.tsv) contra las 99 lineas de .v66ext/veredictos_listos.txt,
por par sin orden. SOLO CLASES Y MADRE: no imprime ninguna razon."""
import io, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
mias = {}
for f in [l.rstrip('\n').split('\t') for l in io.open('.v66aud/mis_clases.tsv', encoding='utf-8')][1:]:
    mias[tuple(sorted((f[0], f[1])))] = (f[2], f[3], 'DUDA' in f[4])
suyas = collections.defaultdict(list)
cand = None
for l in io.open('.v66ext/veredictos_listos.txt', encoding='utf-8'):
    l = l.rstrip('\n')
    if l.startswith('## '): cand = l[3:].strip(); continue
    if not l.strip() or l.startswith('#') or cand is None: continue
    c = l.split('|')
    madre = c[2][6:] if len(c) > 3 and c[2].startswith('madre=') else ''
    suyas[tuple(sorted((cand, c[0])))].append((c[1], madre, cand))
# la fila 22 ya entro: su linea esta en la bitacora, no en este fichero
lineas = sum(len(v) for v in suyas.values())
print('lineas suyas: %d | pares suyos: %d | mis filas: %d' % (lineas, len(suyas), len(mias)))
print('mis pares sin linea suya: %s' % sorted(k for k in mias if k not in suyas))
print('pares suyos sin fila mia: %s' % sorted(k for k in suyas if k not in mias))
inc = [k for k, v in suyas.items() if len(set((x[0], x[1]) for x in v)) > 1]
print('pares con sus dos lineas en desacuerdo entre si: %s' % inc)
co = di = 0
for k in sorted(mias):
    if k not in suyas: continue
    s = suyas[k][0]
    if (mias[k][0], mias[k][1]) == (s[0], s[1]): co += 1
    else:
        di += 1
        print('DISCREPA  %s ~ %s | mia %s madre=%s%s | suya %s madre=%s (%d linea(s))' % (k[0], k[1], mias[k][0], mias[k][1] or '-', ' DUDA' if mias[k][2] else '', s[0], s[1] or '-', len(suyas[k])))
print('coinciden en clase y madre: %d | discrepan: %d' % (co, di))
print('clases suyas por linea: %s' % dict(collections.Counter(x[0] for v in suyas.values() for x in v)))
