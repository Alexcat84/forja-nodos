# -*- coding: utf-8 -*-
import json,io,glob,collections,os
libros=collections.Counter()
for l in io.open('dataset/nodos.jsonl',encoding='utf-8'):
    l=l.strip()
    if not l: continue
    d=json.loads(l)
    for f in d.get('fuentes',[]):
        libros[f.get('clave')]+=1
print('=== libros presentes en dataset/nodos.jsonl (por fuente) ===')
for k,v in libros.most_common(): print('  %-34s %4d' % (k,v))
print()
print("grove_high_output en el dataset :", libros.get('grove_high_output',0))
band=collections.Counter()
for f in glob.glob(os.path.join('cuarentena','*','*.json')):
    if '_insertados' in f or '_derivadas' in f: continue
    band[os.path.basename(os.path.dirname(f))]+=1
print()
print('=== bandejas ===')
for k,v in band.most_common(): print('  %-34s %4d' % (k,v))
