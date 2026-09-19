# -*- coding: utf-8 -*-
"""Los ids que las cinco fichas nombran dentro de su resumen_teorico como arista
declarada, contra la poblacion REAL de hoy (grafo + bandejas). Un id nombrado que no
existe en ninguna sede es una arista colgada."""
import json, os, re, glob, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
viven = {}
for l in open('dataset/nodos.jsonl', encoding='utf-8'):
    if l.strip(): viven[json.loads(l)['id']] = 'grafo'
for d in sorted(os.listdir('cuarentena')):
    p = os.path.join('cuarentena', d)
    if os.path.isdir(p) and d not in ('_insertados', '_derivadas'):
        for f in sorted(glob.glob(os.path.join(p, '*.json'))):
            viven.setdefault(json.load(open(f, encoding='utf-8'))['id'], 'bandeja/' + d)
print("poblacion de ids vivos (grafo + bandejas): %d" % len(viven))
rutas = [l.strip() for l in open('.v48aud/02_candidatos_nuevos.out', encoding='utf-8') if l.strip()]
colgadas = 0
nombrados = 0
for r in rutas:
    c = json.load(open(r, encoding='utf-8'))
    rt = c['resumen_teorico']
    # todo id plausible: minusculas con guion bajo y al menos tres tramos
    cit = sorted(set(x for x in re.findall(r'\b[a-z]+(?:_[a-z0-9]+){2,}\b', rt)
                     if not x.endswith('.md') and x != c['id']))
    cit = [x for x in cit if x in viven or x.count('_') >= 3]
    print()
    print("== %s" % c['id'])
    nombrados += len(cit)
    for x in cit:
        sede = viven.get(x)
        if sede: print("   VIVE en %-24s  %s" % (sede, x))
        else:
            print("   >>> NO EXISTE en ninguna sede        %s" % x); colgadas += 1
print()
print("ids nombrados que no existen en ninguna sede: %d" % colgadas)
print("ids nombrados en total por las cinco fichas: %d" % nombrados)
