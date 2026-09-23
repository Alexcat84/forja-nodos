# cuantos de los candidatos de unidades.txt viven ya en el grafo
import json,io
ids=[l.split()[1] for l in io.open('.v63ciega/unidades.txt',encoding='utf-8')]
g=[json.loads(l)['id'] for l in io.open('dataset/nodos.jsonl',encoding='utf-8') if l.strip()]
print('de los %d, ya en el grafo: %d' % (len(ids), sum(i in g for i in ids)))
