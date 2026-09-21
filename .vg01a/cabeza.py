import json,re,sys
print("INSTRUMENTO .vg01a/cabeza.py  SIN IDS TECLEADOS: la cabeza llega por argumento; los rotulos se leen del indice del fichero de fuente y los nodos del dataset por su rango declarado")
cab=sys.argv[1]; fich=sys.argv[2]
n={x['id']:x for x in (json.loads(l) for l in open('dataset/nodos.jsonl',encoding='utf-8') if l.strip())}
c=n[cab]
print("cabeza:",cab,"| pasos",len(c['pasos_accionables']))
print("hijos (nodos_siguientes) : %d"%len(c['nodos_siguientes']))
for h in c['nodos_siguientes']:
    ok = h in n and cab in (n[h].get('nodos_previos') or [])
    print("   %-52s en el grafo=%s reciproco=%s"%(h, h in n, ok))
lin=open(fich,encoding='utf-8').read().splitlines()
print("RANGO DE LA CABEZA declarado en su resumen:", re.search(r'Sale de las lineas (\d+) a (\d+)',c['resumen_teorico']).group(0))
a,b=[int(x) for x in re.search(r'Sale de las lineas (\d+) a (\d+)',c['resumen_teorico']).groups()]
print("EL INDICE DE LA CABEZA, lineas %d a %d del fichero:"%(a,b))
for i in range(a-1,b):
    t=lin[i].strip()
    if t: print("   L%-4d %s"%(i+1,t[:90]))
print("NODOS DEL CAPITULO Y SU RANGO, ordenados por linea de origen:")
filas=[]
for x in n.values():
    if fich in x.get('resumen_teorico',''):
        m=re.search(r'Sale de las lineas (\d+) a (\d+)',x['resumen_teorico'])
        if m: filas.append((int(m.group(1)),int(m.group(2)),x['id']))
for s,e,i in sorted(filas): print("   L%-4d a L%-4d %s"%(s,e,i))
