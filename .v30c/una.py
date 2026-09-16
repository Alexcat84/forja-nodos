import json,sys
n=int(sys.argv[1])
l=open('bitacora/VEREDICTOS.jsonl',encoding='utf-8').read().split('\n')[n-1]
v=json.loads(l)
print(f"linea {n} | {v['veredicto']} | {v['candidato']} contra {v['vecino']}")
print("RAZON:",v['razon'])
