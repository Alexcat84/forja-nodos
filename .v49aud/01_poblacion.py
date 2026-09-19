# -*- coding: utf-8 -*-
"""Poblacion de la linea, leida del arbol en la APERTURA CIEGA de la vuelta 49.
Por cada ficha de la bandeja de grove: capitulo de origen (del resumen_teorico),
pieza citada, pasos, y si su id ya vive en dataset/nodos.jsonl."""
import io,sys,json,glob,os,re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
graf = [json.loads(l) for l in open('dataset/nodos.jsonl',encoding='utf-8') if l.strip()]
ids = set(n['id'] for n in graf)
print("dataset/nodos.jsonl : %d nodos" % len(graf))
vs = [l for l in open('bitacora/VEREDICTOS.jsonl',encoding='utf-8') if l.strip()]
print("bitacora/VEREDICTOS.jsonl : %d lineas" % len(vs))
pm = [l for l in open('config/pares_mutuos.jsonl',encoding='utf-8') if l.strip()]
print("config/pares_mutuos.jsonl : %d lineas" % len(pm))
fich = sorted(glob.glob('cuarentena/grove_high_output/*.json'))
print("cuarentena/grove_high_output/ : %d fichas" % len(fich))
print()
print("%-52s %-7s %-6s %5s %s" % ("ficha","cap","pieza","pasos","ya en el grafo"))
porcap={}
for f in fich:
    d=json.load(open(f,encoding='utf-8'))
    r=d.get('resumen_teorico','')
    cap=re.search(r'cap_(\d+)\.md',r)
    cap='cap_'+cap.group(1) if cap else '?'
    pz=re.search(r'PIEZA (P\d+[a-z]?)',r)
    pz=pz.group(1) if pz else '?'
    porcap.setdefault(cap,[]).append(os.path.basename(f))
    print("%-52s %-7s %-6s %5d %s" % (os.path.basename(f)[:-5][:52],cap,pz,len(d.get('pasos_accionables',[])), "SI" if d['id'] in ids else "no"))
print()
for c in sorted(porcap):
    print("%s : %d fichas en la bandeja" % (c,len(porcap[c])))
