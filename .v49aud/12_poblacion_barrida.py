# -*- coding: utf-8 -*-
"""De que se compone la poblacion que barrio el instrumento 07 (D.38.4): grafo mas
bandejas, descartando _insertados y _derivadas y con el filtro de fuente canonica."""
import io,sys,json,os,glob
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
tabla=json.load(open('fuentes/FUENTES_CANONICAS.json',encoding='utf-8'))
canon=set(k for k in tabla if not k.startswith('_'))
n=sum(1 for l in open('dataset/nodos.jsonl',encoding='utf-8') if l.strip())
print("grafo (dataset/nodos.jsonl) : %d" % n)
tot=n
for d in sorted(os.listdir('cuarentena')):
    p=os.path.join('cuarentena',d)
    if not os.path.isdir(p) or d in ('_insertados','_derivadas'): continue
    ok=0; ficheros=glob.glob(os.path.join(p,'*.json'))
    for f in ficheros:
        c=json.load(open(f,encoding='utf-8'))
        cl=[x.get('clave') for x in (c.get('fuentes') or [])]
        if cl and all(k in canon for k in cl): ok+=1
    print("bandeja/%-22s : %d de %d ficheros pasan el filtro canonico" % (d,ok,len(ficheros)))
    tot+=ok
print("POBLACION BARRIDA (D.38.4) : %d" % tot)
