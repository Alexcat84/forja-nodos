# Fase ciega de la 66: ids de GRAFO MAS BANDEJAS (D.38.4, sin _insertados ni _derivadas ni ensayo_) que
# contienen una palabra, para saber que vecinos de lectura mirar ademas de los que levante el barrido. Solo lee.
import json, glob, io, os, sys
sys.stdout.reconfigure(encoding="utf-8")
ids = []
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l); ids.append(('grafo', d['id']))
for f in glob.glob('cuarentena/*/*.json'):
    if '_insertados' in f or '_derivadas' in f or 'ensayo_' in f: continue
    d = json.load(io.open(f, encoding='utf-8'))
    ids.append((os.path.basename(os.path.dirname(f)), d['id']))
print('poblacion: %d' % len(ids))
for p in sys.argv[1:]:
    m = [(s, i) for s, i in ids if p in i]
    print('%s %d' % (p, len(m)))
    for s, i in m: print('    %-24s %s' % (s, i))
