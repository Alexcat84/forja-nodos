# -*- coding: utf-8 -*-
import json,io,glob,os,collections,re
for l in io.open('dataset/nodos.jsonl',encoding='utf-8'):
    l=l.strip()
    if not l: continue
    d=json.loads(l)
    if any(f.get('clave')=='grove_high_output' for f in d.get('fuentes',[])):
        print('NODO DE GROVE EN EL GRAFO:', d['id'])
        print('  titulo:', d['titulo'][:120])
        print('  fuentes:', json.dumps(d['fuentes'],ensure_ascii=False))
print()
# capitulos representados en la bandeja de grove
caps=collections.Counter()
for f in glob.glob(os.path.join('cuarentena','grove_high_output','*.json')):
    d=json.load(io.open(f,encoding='utf-8'))
    for fu in d.get('fuentes',[]):
        u=fu.get('unidad') or fu.get('cap') or ''
        caps[str(u)]+=1
print('unidades declaradas en las fichas de la bandeja de grove:')
for k,v in caps.most_common(): print('   %-20s %d' % (k or '(sin unidad)',v))
