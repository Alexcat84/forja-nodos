import json,subprocess
print("INSTRUMENTO .vg01a/cap11_entrada.py  SIN IDS TECLEADOS: los 16 ids salen del resumen_teorico; el commit de entrada lo busca git log -S sobre dataset/nodos.jsonl")
n=[json.loads(l) for l in open('dataset/nodos.jsonl',encoding='utf-8') if l.strip()]
ids=[(x['id'],len(x.get('pasos_accionables') or [])) for x in n if 'fuentes/scott_radical_candor/cap_11.md' in x.get('resumen_teorico','')]
for i,p in ids:
    out=subprocess.run('git log --format="%%h|%%ad|%%s" --date=format:"%%m-%%d %%H:%%M" -S"\\"id\\": \\"%s\\"," -- dataset/nodos.jsonl'%i,shell=True,capture_output=True,text=True).stdout.strip().splitlines()
    print("%-52s pasos=%2d  %s"%(i,p,(out[-1][:110] if out else '(no hallado)')))
