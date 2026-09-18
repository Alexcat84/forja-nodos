import glob, os, json, re
from collections import Counter
print("poblacion: el arbol entero, sin filtrar")
for r in ('dataset/nodos.jsonl','bitacora/VEREDICTOS.jsonl','config/pares_mutuos.jsonl'):
    print("%-43s: %d lineas" % (r, sum(1 for _ in open(r,encoding='utf-8'))))
for c in ('grove_high_output','scott_radical_candor','gerber_emyth','marquet_turn_the_ship'):
    print("%-43s: %d" % ('cuarentena/'+c, len(glob.glob('cuarentena/%s/*.json'%c))))
    print("%-43s: %d" % ('cuarentena/_insertados/'+c, len(glob.glob('cuarentena/_insertados/%s/*.json'%c))))
cnt=Counter()
for p in glob.glob('cuarentena/grove_high_output/*.json'):
    d=json.load(open(p,encoding='utf-8'))
    m=re.search(r'fuentes/grove_high_output/(cap_\d+)\.md', d.get('resumen_teorico',''))
    cnt[m.group(1) if m else 'SIN CAP']+=1
print("%-43s: %s" % ('la bandeja de grove por capitulo', ', '.join('%s %d'%(k,v) for k,v in sorted(cnt.items()))))
n=sum(1 for _ in open('dataset/nodos.jsonl',encoding='utf-8'))
g=0
for l in open('dataset/nodos.jsonl',encoding='utf-8'):
    if '"grove_high_output"' in l: g+=1
print("%-43s: %d" % ('nodos de grove_high_output en el grafo', g))
