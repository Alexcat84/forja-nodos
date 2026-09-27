import json, sys, io, os, glob
def buscar(i):
    for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
        d = json.loads(l)
        if d['id'] == i:
            return d, 'GRAFO'
    for p in glob.glob('cuarentena/*/*.json') + glob.glob('cuarentena/_insertados/*/*.json'):
        if os.path.basename(p) == i + '.json':
            return json.load(io.open(p, encoding='utf-8')), 'BANDEJA ' + p
    return None, None
for i in sys.argv[1:]:
    d, sede = buscar(i)
    if d is None:
        print('### %s  NO ENCONTRADO' % i); continue
    print('### %s   [%s]' % (i, sede))
    print('TITULO: ' + d['titulo'])
    print('ACTIVA: ' + d['condiciones_activacion'])
    print('ENTREGA: ' + d['entregable_esperado'])
    for k, p in enumerate(d['pasos_accionables'], 1):
        print('  %d| %s' % (k, p))
    print()
