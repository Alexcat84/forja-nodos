import json, collections
nodos=[json.loads(l) for l in open('dataset/nodos.jsonl',encoding='utf-8') if l.strip()]
ver=[json.loads(l) for l in open('bitacora/VEREDICTOS.jsonl',encoding='utf-8') if l.strip()]
print("nodos:",len(nodos))
print("veredictos:",len(ver))
def fuente_txt(n):
    return json.dumps(n.get('fuentes',n.get('fuente','')),ensure_ascii=False)
sc=[n for n in nodos if 'scott_radical_candor' in json.dumps(n,ensure_ascii=False)]
print("nodos que mencionan scott_radical_candor:",len(sc))
# no_consumada
nc=[v for v in ver if isinstance(v.get('anotaciones'),(list,dict)) and 'no_consumada' in json.dumps(v.get('anotaciones'),ensure_ascii=False)]
nc2=[v for v in ver if '"no_consumada": true' in json.dumps(v,ensure_ascii=False) or v.get('no_consumada') is True]
print("con no_consumada true (json dump):",len(nc2))
# aristas
sig=sum(len(n.get('nodos_siguientes') or []) for n in nodos)
prev=sum(len(n.get('nodos_previos') or []) for n in nodos)
print("aristas por nodos_siguientes:",sig," por nodos_previos:",prev)
# claves de nodo
print("claves de un nodo:",sorted(nodos[0].keys()))
print("claves de un veredicto:",sorted(ver[-1].keys()))
