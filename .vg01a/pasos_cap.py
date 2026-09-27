import json, re, sys, collections
print("INSTRUMENTO .vg01a/pasos_cap.py  SIN CONSTANTES TECLEADAS: el capitulo sale del texto UNIDAD DE ORIGEN de cada resumen_teorico; los pasos se cuentan de pasos_accionables")
n=[json.loads(l) for l in open('dataset/nodos.jsonl',encoding='utf-8') if l.strip()]
por=collections.OrderedDict()
sin=0
for x in n:
    m=re.search(r'UNIDAD DE ORIGEN: fuentes/([a-z0-9_]+)/(cap_\d+)\.md', x.get('resumen_teorico',''))
    if not m: sin+=1; continue
    k=(m.group(1),m.group(2))
    por.setdefault(k,[0,0,[]])
    por[k][0]+=1; por[k][1]+=len(x.get('pasos_accionables') or []); por[k][2].append(x['id'])
print("nodos que declaran su unidad de origen : %d de %d"%(sum(v[0] for v in por.values()), len(n)))
print("nodos que NO la declaran               : %d"%sin)
print("%-24s %-8s %6s %6s"%("libro","unidad","nodos","pasos"))
for (lib,cap),v in sorted(por.items()):
    print("%-24s %-8s %6d %6d"%(lib,cap,v[0],v[1]))
if len(sys.argv)>1:
    lib,cap=sys.argv[1],sys.argv[2]
    print("\nIDS DE %s %s:"%(lib,cap))
    for i in sorted(por[(lib,cap)][2]): print("   ",i)
