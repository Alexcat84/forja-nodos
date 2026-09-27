# Reconstruye la poblacion D.38.4 (grafo mas bandejas, sin _insertados ni _derivadas).
# Los .jsonl que produce NO se dejan en el arbol: llevan guiones largos copiados del
# catalogo de control y ponen el barrido de estilo en rojo. Se generan, se usan y se borran.
import io,json,glob,os
grafo=[l for l in io.open('dataset/nodos.jsonl',encoding='utf-8') if l.strip()]
io.open('.barrido_v19/grafo.jsonl','w',encoding='utf-8').writelines(grafo)
with io.open('.barrido_v19/bandejas.jsonl','w',encoding='utf-8') as fh:
    n=0
    for d in ['scott_radical_candor','ensayo_referencia_163','smart_who','onu_consumidor','zhuo_manager']:
        for f in sorted(glob.glob('cuarentena/%s/*.json'%d)):
            fh.write(json.dumps(json.load(open(f,encoding='utf-8')),ensure_ascii=False)+'\n'); n+=1
print('grafo %d + bandejas %d = poblacion %d'%(len(grafo),n,len(grafo)+n))
