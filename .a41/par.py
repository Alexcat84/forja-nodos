# -*- coding: utf-8 -*-
import json, io, sys
N={}
for l in io.open('dataset/nodos.jsonl',encoding='utf-8'):
    if l.strip():
        d=json.loads(l); N[d['id']]=d
for k in sys.argv[1:]:
    n=N.get(k)
    if not n: print('NO ESTA EN EL GRAFO:',k); continue
    print('='*100)
    print('id        :',n['id'])
    print('titulo    :',n.get('titulo'))
    print('activacion:',n.get('condiciones_activacion'))
    print('entregable:',n.get('entregable_esperado'))
    print('previos   :',n.get('nodos_previos'))
    print('siguientes:',n.get('nodos_siguientes'))
    print('PASOS (%d):'%len(n.get('pasos_accionables') or []))
    for i,p in enumerate(n.get('pasos_accionables') or [],1):
        print('  %2d. %s'%(i,p))
