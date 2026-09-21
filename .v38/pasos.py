import json, sys
ids = sys.argv[1:]
for l in open('dataset/nodos.jsonl', encoding='utf-8'):
    l = l.strip()
    if not l: continue
    n = json.loads(l)
    if n['id'] in ids:
        print('=== %s ===' % n['id'])
        for i, p in enumerate(n['pasos_accionables'], 1):
            print('  P%02d: %s' % (i, p))
        print('  previos   :', n.get('nodos_previos'))
        print('  siguientes:', n.get('nodos_siguientes'))
        print()
