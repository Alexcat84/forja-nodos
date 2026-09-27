# -*- coding: utf-8 -*-
import json,io,glob,os,re,collections
pob={}
for l in io.open('dataset/nodos.jsonl',encoding='utf-8'):
    l=l.strip()
    if l:
        d=json.loads(l); pob[d['id']]=('GRAFO',d)
for f in glob.glob(os.path.join('cuarentena','*','*.json')):
    if '_insertados' in f or '_derivadas' in f: continue
    d=json.load(io.open(f,encoding='utf-8'))
    pob.setdefault(d['id'],('BANDEJA:'+os.path.basename(os.path.dirname(f)),d))
for f in glob.glob(os.path.join('.v60ext','pendientes','*.json')):
    d=json.load(io.open(f,encoding='utf-8'))
    pob.setdefault(d['id'],('PENDIENTE',d))
print('POBLACION (grafo + bandejas + pendiente):', len(pob))
# ids duplicados dentro de la bandeja de grove
vistos=collections.Counter()
for f in glob.glob(os.path.join('cuarentena','grove_high_output','*.json')):
    vistos[json.load(io.open(f,encoding='utf-8'))['id']]+=1
dup=[k for k,v in vistos.items() if v>1]
print('ids repetidos en la bandeja de grove:', len(dup), dup)

CLAVES=('entrena','curso','clase','instructor','ensen','capacit','training')
print()
print('=== todo nodo de la poblacion cuyo titulo o id toca el tema del entrenamiento ===')
for nid,(donde,d) in sorted(pob.items()):
    t=(d.get('titulo') or '').lower()
    if any(k in nid for k in CLAVES) or any(k in t for k in CLAVES):
        print('  %-14s %-52s %s' % (donde, nid[:52], (d.get('titulo') or '')[:95]))
