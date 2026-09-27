import json,sys,os,glob
def cargar(id_):
    for l in open('dataset/nodos.jsonl',encoding='utf-8'):
        if not l.strip(): continue
        n=json.loads(l)
        if n['id']==id_: return n,'GRAFO'
    for f in glob.glob('cuarentena/*/*.json'):
        if '_insertados' in f or '_derivadas' in f: continue
        n=json.load(open(f,encoding='utf-8'))
        if n.get('id')==id_: return n,'BANDEJA '+f
    return None,None
for id_ in sys.argv[1:]:
    n,d=cargar(id_)
    if n is None: print("NO ENCONTRADO:",id_); continue
    print("="*100)
    print(id_,"  [",d,"]")
    print("titulo:",n['titulo'])
    print("fuentes:",json.dumps(n.get('fuentes'),ensure_ascii=False)[:400])
    print("activacion:",json.dumps(n.get('condiciones_activacion'),ensure_ascii=False)[:400])
    print("entregable:",n.get('entregable_esperado'))
    print("previos:",n.get('nodos_previos'),"siguientes:",n.get('nodos_siguientes'))
    print("PASOS:")
    for i,p in enumerate(n.get('pasos_accionables') or [],1):
        print(f"  {i:2d} | {p}")
    print()
