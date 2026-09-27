import json,glob,os,re
band=[]
for f in glob.glob('cuarentena/scott_radical_candor/*.json'):
    n=json.load(open(f,encoding='utf-8'))
    t=json.dumps(n,ensure_ascii=False)
    if 'cap_07.md' in t: band.append(n['id'])
print("candidatos en bandeja que citan cap_07.md:",len(band),band)
graf=[]
for l in open('dataset/nodos.jsonl',encoding='utf-8'):
    if not l.strip(): continue
    n=json.loads(l)
    if 'cap_07.md' in json.dumps(n,ensure_ascii=False): graf.append(n['id'])
print("nodos del grafo que citan cap_07.md:",len(graf))
ins=[os.path.basename(f)[:-5] for f in glob.glob('cuarentena/_insertados/scott_radical_candor/*.json')]
print("archivados en _insertados/scott_radical_candor:",len(ins))
ids_graf=set()
for l in open('dataset/nodos.jsonl',encoding='utf-8'):
    if l.strip(): ids_graf.add(json.loads(l)['id'])
dentro=[i for i in ins if i in ids_graf]
print("archivados que estan en el grafo:",len(dentro)," fuera:",len(ins)-len(dentro))
print()
# entradillas: rotulos de etapa de cap_07
rot=['LISTEN','CLARIFY','DEBATE','DECIDE','PERSUADE','EXECUTE','LEARN']
lineas={}
for i,l in enumerate(open('fuentes/scott_radical_candor/cap_07.md',encoding='utf-8'),1):
    s=l.strip()
    if s in rot and s not in lineas: lineas[s]=i
print("rotulos de etapa y su linea:",lineas)
# tramos declarados
import re
tram={}
for l in open('dataset/nodos.jsonl',encoding='utf-8'):
    if not l.strip(): continue
    n=json.loads(l); t=n.get('resumen_teorico','')
    m=re.search(r'cap_07\.md[^0-9]{0,20}(\d+)\s*(?:a|-|\u2013)\s*(\d+)',t)
    if m: tram[n['id']]=(int(m.group(1)),int(m.group(2)))
for r,ln in lineas.items():
    cub=[k for k,(a,b) in tram.items() if a<=ln<=b]
    print(f"  {r:9s} L{ln:<4d} -> {cub if cub else 'NINGUNO: es cola'}")
