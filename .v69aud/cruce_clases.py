# -*- coding: utf-8 -*-
"""Fase ciega de la 69 (copia de .v68aud/cruce_clases.py, con R7): cada par sin orden de mi barrido sellado de la 68
(.v68aud/vecinos_tabla.txt) contra su fila de .v68aud/mis_clases.tsv, y las clases contadas con el mismo predicado
(igualdad exacta del campo clase) y con su suma. Aparte, los pares que tocan a los 20 de cap_05 y cap_06
(.v68aud/los20.txt), que son los que entran en la 70, y los de la cabeza usar_tres_clases_reunion_proceso. Solo lee."""
import io, re, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
los20 = set(io.open('.v68aud/los20.txt', encoding='utf-8').read().split())
filas_dir = 0; pares = set()
for l in io.open('.v68aud/vecinos_tabla.txt', encoding='utf-8'):
    if re.match(r'^    (\S+) +> (\S+) ', l) and l.split()[0] in los20: filas_dir += 1
    m = re.match(r'^    (\S+) +~ (\S+) ', l)
    if m: pares.add(tuple(sorted(m.groups())))
filas = [l.rstrip('\n').split('\t') for l in io.open('.v68aud/mis_clases.tsv', encoding='utf-8')][1:]
clases = {tuple(sorted((f[0], f[1]))): f for f in filas}
def cuenta(fs):
    c = collections.Counter(f[2] for f in fs)
    return '%s | suma: %d' % (dict(c), sum(c.values()))
print('pares del barrido: %d | filas de clase: %d | pares sin fila: %s | filas sin par: %s' % (
    len(pares), len(filas), sorted(pares - set(clases)), sorted(set(clases) - pares)))
print('todas las filas por clase: %s' % cuenta(filas))
t = [f for f in filas if f[0] in los20 or f[1] in los20]
print('filas de vecino (dirigidas) de los 20: %d' % filas_dir)
print('pares sin orden que tocan a los 20: %d | por clase: %s' % (len(t), cuenta(t)))
for f in t:
    if f[2] != 'SANO': print('  %-9s %s ~ %s | madre %s' % (f[2], f[0], f[1], f[3]))
cab = [f for f in t if 'usar_tres_clases_reunion_proceso' in (f[0], f[1])]
print('pares con la cabeza usar_tres_clases_reunion_proceso: %d | por clase: %s' % (len(cab), cuenta(cab)))
for f in cab: print('  %-9s %s' % (f[2], f[1] if f[0] == 'usar_tres_clases_reunion_proceso' else f[0]))
