import json,glob,subprocess

def sh(c):
    return subprocess.run(c,shell=True,capture_output=True,text=True).stdout.strip()

nodos=[json.loads(l) for l in open('dataset/nodos.jsonl',encoding='utf-8') if l.strip()]
ver=[json.loads(l) for l in open('bitacora/VEREDICTOS.jsonl',encoding='utf-8') if l.strip()]
noc=sum(1 for v in ver if json.dumps(v,ensure_ascii=False).find('"no_consumada": true')>=0)
sig=sum(len(n.get('nodos_siguientes',[])) for n in nodos)
pre=sum(len(n.get('nodos_previos',[])) for n in nodos)
band4=len(glob.glob('cuarentena/scott_radical_candor/*.json'))
ins4=len(glob.glob('cuarentena/_insertados/scott_radical_candor/*.json'))
band5=len(glob.glob('cuarentena/marquet_turn_the_ship/*.json'))
tot4=band4+ins4
filas=[
 ("rama", sh("git rev-parse --abbrev-ref HEAD"), "`git rev-parse --abbrev-ref HEAD`"),
 ("commit al abrir mi turno", "`"+sh("git rev-parse --short HEAD")+"`", "`git rev-parse --short HEAD`"),
 ("nodos en `dataset/nodos.jsonl`", f"**{len(nodos)}**", "`dataset/nodos.jsonl`"),
 ("veredictos en `bitacora/VEREDICTOS.jsonl`", f"**{len(ver)}**", "`bitacora/VEREDICTOS.jsonl`"),
 ("de ellos, con alguna anotacion `no_consumada: true`", f"**{noc}**", "`bitacora/VEREDICTOS.jsonl`"),
 ("aristas por `nodos_siguientes`", f"**{sig}**", "`dataset/nodos.jsonl`"),
 ("aristas por `nodos_previos`", f"**{pre}**", "`dataset/nodos.jsonl`"),
 ("candidatos en bandeja, lote 4", f"**{band4}**", "PATRON: `cuarentena/scott_radical_candor/*.json`"),
 ("insertados y archivados, lote 4", f"**{ins4}**", "PATRON: `cuarentena/_insertados/scott_radical_candor/*.json`"),
 ("candidatos en bandeja, lote 5", f"**{band5}**", "PATRON: `cuarentena/marquet_turn_the_ship/*.json`"),
 (f"lote 4 insertado sobre `{tot4}`, por ciento", f"**{ins4*100.0/tot4:.1f}".replace('.',',')+"**", "`cuarentena/_insertados/scott_radical_candor/`"),
]
print("| pieza | valor | de donde sale |")
print("|---|---:|---|")
for a,b,c in filas:
    print(f"| {a} | {b} | {c} |")
