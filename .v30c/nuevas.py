import json, collections
ver=[json.loads(l) for l in open('bitacora/VEREDICTOS.jsonl',encoding='utf-8') if l.strip()]
nuevas=ver[289:]
print("lineas nuevas (290..375):",len(nuevas))
print("por veredicto:",collections.Counter(v['veredicto'] for v in nuevas))
print("candidatos distintos:",len(set(v['candidato'] for v in nuevas)))
c=collections.Counter(v['candidato'] for v in nuevas)
for k,n in c.most_common(): print("   ",n,k)
print()
lp=collections.Counter(tuple(v.get('levantada_por') or []) for v in nuevas)
for k,n in lp.most_common(): print("  levantada_por",k,n)
print()
print("con arista:",sum(1 for v in nuevas if v.get('arista')))
for v in nuevas:
    if v.get('arista'):
        print("   arista:",v['arista'],"| veredicto",v['veredicto'],"| levantada_por",v.get('levantada_por'),"| en_cola",v.get('arista_en_cola'))
print()
print("SIN razon (D.8):",sum(1 for v in nuevas if not (v.get('razon') or '').strip()))
print("razon mas corta:",min(len(v.get('razon') or '') for v in nuevas))
