import json
ver=[json.loads(l) for l in open('bitacora/VEREDICTOS.jsonl',encoding='utf-8') if l.strip()]
for i,v in enumerate(ver,1):
    if v['candidato']=='bloquear_tiempo_pensar_calendario' or v['vecino']=='bloquear_tiempo_pensar_calendario':
        print(i,v['veredicto'],"cand:",v['candidato'],"| vec:",v['vecino'],"|",json.dumps(v['senales']),"|",v.get('levantada_por'))
print()
print("--- cuidarse_agotamiento_centro_rueda, todas sus lineas ---")
for i,v in enumerate(ver,1):
    if v['candidato']=='cuidarse_agotamiento_centro_rueda' or v['vecino']=='cuidarse_agotamiento_centro_rueda':
        print(i,v['veredicto'],"cand:",v['candidato'],"| vec:",v['vecino'],"|",json.dumps(v['senales']),"|",v.get('levantada_por'))
