# Fase ciega de la 78 (copia de .v76aud/cruce_aristas.py con las rutas cambiadas): para cada arista por lectura de .v78aud/aristas_lectura.tsv, si el barrido levanto el par
# (entonces no es arista por lectura sino linea de veredicto, D.53) y donde vive cada extremo hoy. Solo lee.
import io, re, json, sys, glob, os
sys.stdout.reconfigure(encoding="utf-8")
pares = set()
for l in io.open('.v78aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +~ (\S+) ', l)
    if m: pares.add(tuple(sorted(m.groups())))
grafo = set(json.loads(l)['id'] for l in io.open('dataset/nodos.jsonl', encoding='utf-8'))
bandeja = set(os.path.basename(f)[:-5] for f in glob.glob('cuarentena/marquet_turn_the_ship/*.json'))
sede = lambda i: 'grafo' if i in grafo else ('bandeja' if i in bandeja else 'NINGUNA')
filas = [l.rstrip('\n').split('\t') for l in io.open('.v78aud/aristas_lectura.tsv', encoding='utf-8')][1:]
for f in filas:
    lev = tuple(sorted((f[0], f[1]))) in pares
    print('%-14s %-50s (%s) > %-54s (%s) | levantado por el barrido: %s' % (f[2], f[0], sede(f[0]), f[1], sede(f[1]), 'SI' if lev else 'no'))
import collections
c = collections.Counter(f[2].split(',')[0].split(' D.')[0] for f in filas)
print('filas: %d | por lo que queda: %s | suma: %d' % (len(filas), dict(c), sum(c.values())))
print('filas con DUDA escrita: %d de %d' % (sum('DUDA' in f[2] for f in filas), len(filas)))
lev = collections.Counter('levantada' if tuple(sorted((f[0], f[1]))) in pares else 'no levantada' for f in filas)
print('por el barrido: %s | suma: %d' % (dict(lev), sum(lev.values())))
