import json, sys

GRAFO = {}
for l in open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l)
    GRAFO[d['id']] = d


def carga(nid):
    if nid in GRAFO:
        return GRAFO[nid], 'GRAFO'
    p = 'cuarentena/scott_radical_candor/%s.json' % nid
    return json.load(open(p, encoding='utf-8')), 'BANDEJA'


for nid in sys.argv[1:]:
    d, donde = carga(nid)
    print('=' * 78)
    print('%s  [%s]  fuente=%s' % (nid, donde, d['fuentes'][0]['clave']))
    print('TITULO     :', d['titulo'])
    print('ACTIVACION :', d['condiciones_activacion'])
    print('ENTREGABLE :', d['entregable_esperado'])
    for i, s in enumerate(d['pasos_accionables'], 1):
        print(' P%-2d %s' % (i, s))
