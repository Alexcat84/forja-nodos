# -*- coding: utf-8 -*-
import json, io, collections
N=[json.loads(l) for l in io.open('dataset/nodos.jsonl',encoding='utf-8') if l.strip()]
byid={n['id']:n for n in N}
V=[json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl',encoding='utf-8') if l.strip()]
# aristas dirigidas del grafo
dir_=0
for n in N:
    dir_+=len(n.get('nodos_siguientes') or [])+len(n.get('nodos_previos') or [])
print('aristas (suma de nodos_previos + nodos_siguientes):', dir_)
prev=sum(len(n.get('nodos_previos') or []) for n in N)
sig=sum(len(n.get('nodos_siguientes') or []) for n in N)
print('  nodos_previos:',prev,' nodos_siguientes:',sig)
# COLA DE ARISTAS entera
cola=[ (i+1,v) for i,v in enumerate(V) if v.get('arista_en_cola') ]
print('lineas con arista_en_cola truthy:', len(cola))
cab=0; esp=0; sincable=0
for i,v in cola:
    a=(v.get('arista') or '').strip()
    if '>' in a: m,h=[s.strip() for s in a.split('>',1)]
    else: m,h=None,None
    if m is None: continue
    dentro = m in byid and h in byid
    if not dentro: esp+=1; continue
    cableada = (h in (byid[m].get('nodos_siguientes') or [])) or (m in (byid[h].get('nodos_previos') or []))
    if cableada: cab+=1
    else: sincable+=1; print('   SIN CABLE:', a)
print('  YA CABLEADAS:',cab,' esperan extremo:',esp,' dentro y sin cable:',sincable)
# reparto por capitulo de scott
cnt=collections.Counter(); tot=0
for n in N:
    caps=set()
    for f in (n.get('fuentes') or []):
        if isinstance(f,dict):
            if f.get('clave')=='scott_radical_candor' or f.get('libro')=='scott_radical_candor' or f.get('fuente')=='scott_radical_candor':
                for k in ('capitulo','cap','seccion'):
                    if f.get(k): caps.add(f[k])
    if caps:
        tot+=1
        for c in caps: cnt[c]+=1
print('nodos que citan scott_radical_candor:', tot)
for c in sorted(cnt): print('   ',c,cnt[c])
print('   suma de filas:', sum(cnt.values()))
