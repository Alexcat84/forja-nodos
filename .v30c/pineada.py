import json,random
ver=[json.loads(l) for l in open('bitacora/VEREDICTOS.jsonl',encoding='utf-8') if l.strip()]
nuevas=[(i+1,v) for i,v in enumerate(ver) if i>=289]
sanos=[(n,v) for n,v in nuevas if v['veredicto']=='SANO']
print("SANO de la tanda:",len(sanos))
print("el mayor entre 3 y el 20 por ciento:",max(3,round(len(sanos)*0.2)),"  techo 20")
SEM=300916
m=sorted(random.Random(SEM).sample(sanos,16))
print("SEMILLA:",SEM,"  random.Random(SEM).sample(sanos,16)")
print()
for n,v in m:
    print(f"linea {n:3d}  {v['candidato']}   contra   {v['vecino']}   | senales {json.dumps(v['senales'])} | {v['levantada_por']}")
json.dump([n for n,v in m],open('.v30c/pineada_lineas.json','w'))
