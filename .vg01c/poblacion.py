# poblacion.py -- D.38.4: la poblacion es GRAFO + BANDEJAS, descartando
# _insertados y _derivadas. CERO IDS TECLEADOS: todo se descubre del arbol.
import json, io, os, sys
filas = []
g = 'dataset/nodos.jsonl'
for l in io.open(g, encoding='utf-8'):
    l = l.strip()
    if not l:
        continue
    d = json.loads(l)
    filas.append(('GRAFO', d.get('id',''), d.get('titulo',''), d.get('dominio','')))
raiz = 'cuarentena'
for sub in sorted(os.listdir(raiz)):
    p = os.path.join(raiz, sub)
    if not os.path.isdir(p):
        continue
    if sub.startswith('_'):
        continue
    for f in sorted(os.listdir(p)):
        if not f.endswith('.json'):
            continue
        d = json.load(io.open(os.path.join(p, f), encoding='utf-8'))
        filas.append(('BANDEJA:'+sub, d.get('id',''), d.get('titulo',''), d.get('dominio','')))
print('INSTRUMENTO poblacion.py  SIN IDS TECLEADOS: lee dataset/nodos.jsonl y cuarentena/*/ (descarta los que empiezan por _)')
from collections import Counter
c = Counter(f[0] for f in filas)
for k in sorted(c):
    print('%-32s %4d' % (k, c[k]))
print('%-32s %4d' % ('POBLACION TOTAL', len(filas)))
if len(sys.argv) > 1:
    pats = [a.lower() for a in sys.argv[1:]]
    print('--- filas que casan con: %s' % ' '.join(pats))
    n = 0
    for s, i, t, dom in filas:
        blob = (i + ' ' + t).lower()
        if any(p in blob for p in pats):
            n += 1
            print('%-28s %-46s %s' % (s, i, t))
    print('CASAN: %d' % n)
