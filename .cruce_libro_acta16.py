import json
import collections

nodos = {}
for l in open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l)
    nodos[d['id']] = d['fuentes'][0]['clave']
c = collections.Counter()
cruces = []
for l in open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l)
    for h in d.get('nodos_siguientes', []):
        par = (nodos[d['id']], nodos.get(h, '?'))
        c[par] += 1
        if par[0] != par[1]:
            cruces.append((d['id'], h, par))
for k, v in sorted(c.items()):
    print('%-32s -> %-32s %3d' % (k[0], k[1], v))
print('total aristas:', sum(c.values()))
print('ARISTAS QUE CRUZAN DE LIBRO:', len(cruces))
