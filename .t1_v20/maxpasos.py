# -*- coding: utf-8 -*-
import json, glob
t = []
for f in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    t.append((len(d['pasos_accionables']), d['id']))
t.sort(reverse=True)
print("los cinco candidatos del lote 4 con mas pasos:")
for p, i in t[:5]:
    print("  %3d  %s" % (p, i))
print("candidatos del lote 4:", len(t), " pasos:", sum(p for p, _ in t))
