import json,re,glob,os,subprocess
print("INSTRUMENTO .vg01a/cap11_origen.py  SIN IDS TECLEADOS: la unidad sale del resumen_teorico y el commit de entrada lo busca git log -S sobre dataset/nodos.jsonl")
n=[json.loads(l) for l in open('dataset/nodos.jsonl',encoding='utf-8') if l.strip()]
ids=[x['id'] for x in n if 'fuentes/scott_radical_candor/cap_11.md' in x.get('resumen_teorico','')]
pas={x['id']:len(x.get('pasos_accionables') or []) for x in n}
arch=set()
for f in glob.glob(os.path.join('cuarentena','_insertados','scott_radical_candor','*.json')):
    d=json.load(open(f,encoding='utf-8'))
    if 'fuentes/scott_radical_candor/cap_11.md' in d.get('resumen_teorico',''): arch.add(d['id'])
print("nodos de cap_11 en el grafo        : %d, %d pasos"%(len(ids),sum(pas[i] for i in ids)))
print("de ellos con candidato archivado    : %d, %d pasos"%(len(arch),sum(pas[i] for i in arch)))
fuera=[i for i in ids if i not in arch]
print("SIN candidato archivado de cap_11   : %d, %d pasos"%(len(fuera),sum(pas[i] for i in fuera)))
for i in fuera:
    h=subprocess.run('git log --format="%%h %%ad %%s" --date=short -S"\\"id\\": \\"%s\\"" -- dataset/nodos.jsonl'%i,shell=True,capture_output=True,text=True).stdout.strip().splitlines()
    print("   %-52s pasos=%2d  entro en: %s"%(i,pas[i],h[-1] if h else '(no hallado)'))
