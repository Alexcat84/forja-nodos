# -*- coding: utf-8 -*-
"""EL BARRIDO DEL ANCLA UNICA, RE HECHO POR EL AUDITOR CON SU PROPIO LECTOR.
No distingue mayusculas, que es el fallo que el propio extractor declaro haber tenido."""
import json,glob,io,os,re
pat=sorted(glob.glob('cuarentena/scott_radical_candor/*.json')+
           glob.glob('cuarentena/_insertados/scott_radical_candor/*.json'))
grafo=set(json.loads(l)['id'] for l in io.open('dataset/nodos.jsonl',encoding='utf-8'))
unidades={}
for f in sorted(glob.glob('fuentes/scott_radical_candor/cap_*.md')):
    unidades[os.path.basename(f)[:-3]]=io.open(f,encoding='utf-8').read().lower()
filas=[]
for r in pat:
    d=json.load(io.open(r,encoding='utf-8'))
    txt=json.dumps(d,ensure_ascii=False)
    m=re.search(r"ancla textual unica que la sostiene,\s*'([^']+)'",txt)
    if not m: continue
    ancla=m.group(1).strip().lower()
    u=re.search(r'UNIDAD DE ORIGEN:\s*\S*?(cap_\d+)',txt)
    decl=u.group(1) if u else '?'
    donde=sorted(k for k,v in unidades.items() if ancla in v)
    filas.append((d['id'],decl,ancla,donde,d['id'] in grafo))
print('UNIDADES DEL LIBRO LEIDAS:',len(unidades))
print('CANDIDATOS CON LA FORMULA DEL ANCLA UNICA:',len(filas))
malas=[]
for i,dec,a,donde,eng in filas:
    ok=(donde==[dec])
    if not ok: malas.append((i,dec,a,donde,eng))
    print('%-54s %-7s %-30s %-22s %-8s %s'%(i[:54],dec,a[:30],','.join(donde) or 'NINGUNA',
          'grafo' if eng else 'bandeja','' if ok else '<<< NO CUADRA'))
print()
print('cuadran                          :',len(filas)-len(malas))
print('NO cuadran                       :',len(malas))
print('  con la declarada entre las que la contienen:',sum(1 for x in malas if x[1] in x[3]))
print('  con la declarada SIN su propia ancla       :',sum(1 for x in malas if x[1] not in x[3]))
print('  ya dentro del grafo                        :',sum(1 for x in malas if x[4]))
print('  todavia en la bandeja                      :',sum(1 for x in malas if not x[4]))
