import json,sys,glob,os
print("INSTRUMENTO .vg01a/par2.py  SIN CONSTANTES TECLEADAS: los ids llegan por argumento; busca en dataset/nodos.jsonl y en cuarentena/ entera")
pool={}
for l in open('dataset/nodos.jsonl',encoding='utf-8'):
    if l.strip():
        d=json.loads(l); pool[d['id']]=('GRAFO',d)
for f in glob.glob(os.path.join('cuarentena','**','*.json'),recursive=True):
    try: d=json.load(open(f,encoding='utf-8'))
    except Exception: continue
    if isinstance(d,dict) and 'id' in d and d['id'] not in pool: pool[d['id']]=(f,d)
for i in sys.argv[1:]:
    sede,x=pool[i]
    print("="*100); print(i,"| SEDE:",sede)
    print("TITULO:",x.get('titulo'))
    print("ENTREGABLE:",x.get('entregable_esperado'))
    print("ACTIVACION:",x.get('condiciones_activacion'))
    ps=x.get('pasos_accionables') or []
    print("PASOS (%d):"%len(ps))
    for k,p in enumerate(ps,1): print("  %2d. %s"%(k,p))
