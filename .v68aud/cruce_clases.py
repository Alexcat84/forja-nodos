# Fase ciega de la 68 (copia de .v66aud/cruce_clases.py con las rutas cambiadas): comprueba que cada par sin orden de .v68aud/vecinos_tabla.txt tiene su fila en
# .v68aud/mis_clases.tsv y cada fila su par, y cuenta las clases. Solo lee.
import io, re, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
pares = set()
for l in io.open('.v68aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +~ (\S+) ', l)
    if m: pares.add(tuple(sorted(m.groups())))
filas = [l.rstrip('\n').split('\t') for l in io.open('.v68aud/mis_clases.tsv', encoding='utf-8')][1:]
clases = {tuple(sorted((f[0], f[1]))): f for f in filas}
print('pares del barrido: %d | filas de clase: %d' % (len(pares), len(filas)))
print('pares sin fila: %s' % sorted(pares - set(clases)))
print('filas sin par: %s' % sorted(set(clases) - pares))
print('clases: %s' % dict(collections.Counter(f[2] for f in filas)))
print('con DUDA escrita: %d' % sum('DUDA' in f[4] for f in filas))
for f in filas:
    if f[2] != 'SANO': print('  %-9s %s ~ %s | madre %s' % (f[2], f[0], f[1], f[3]))
