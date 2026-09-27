# imprime titulo, condicion y pasos de los ids pedidos, buscandolos en el grafo y en las bandejas
import json,io,glob,sys,os
pob={}
for l in io.open('dataset/nodos.jsonl',encoding='utf-8'):
    if l.strip(): d=json.loads(l); pob[d['id']]=('grafo',d)
for p in glob.glob('cuarentena/*/*.json'):
    if '_insertados' in p or '_derivadas' in p or 'ensayo_referencia' in p: continue
    d=json.load(io.open(p,encoding='utf-8')); pob.setdefault(d['id'],(os.path.normpath(p).split(os.sep)[1],d))
for i in sys.argv[1:]:
    sede,d=pob[i]
    print('=====',i,'[%s]'%sede); print('TIT:',d['titulo']); print('COND:',d.get('condiciones_activacion',''))
    for n,x in enumerate(d.get('pasos_accionables',[]),1): print(' %d. %s'%(n,x))
