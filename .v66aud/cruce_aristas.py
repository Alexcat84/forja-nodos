# Fase ciega de la 66: para cada arista por lectura de .v66aud/aristas_lectura.tsv, si el barrido levanto el par
# (entonces no es arista por lectura sino linea de veredicto, D.53) y donde vive cada extremo hoy. Solo lee.
import io, re, json, sys, glob, os
sys.stdout.reconfigure(encoding="utf-8")
pares = set()
for l in io.open('.v66aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +~ (\S+) ', l)
    if m: pares.add(tuple(sorted(m.groups())))
grafo = set(json.loads(l)['id'] for l in io.open('dataset/nodos.jsonl', encoding='utf-8'))
bandeja = set(os.path.basename(f)[:-5] for f in glob.glob('cuarentena/grove_high_output/*.json'))
sede = lambda i: 'grafo' if i in grafo else ('bandeja' if i in bandeja else 'NINGUNA')
filas = [l.rstrip('\n').split('\t') for l in io.open('.v66aud/aristas_lectura.tsv', encoding='utf-8')][1:]
for f in filas:
    lev = tuple(sorted((f[0], f[1]))) in pares
    print('%-14s %-50s (%s) > %-54s (%s) | levantado por el barrido: %s' % (f[2], f[0], sede(f[0]), f[1], sede(f[1]), 'SI' if lev else 'no'))
print('filas: %d | SOSTENGO: %d | NO: %d | levantadas por el barrido: %d' % (len(filas), sum(f[2].startswith('SOSTENGO') for f in filas), sum(f[2] == 'NO' for f in filas), sum(tuple(sorted((f[0], f[1]))) in pares for f in filas)))
