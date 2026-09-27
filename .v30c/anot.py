import json
lineas=[json.loads(l) for l in open('bitacora/VEREDICTOS.jsonl',encoding='utf-8') if l.strip()]
esperadas=[252,256,258,260,261,262,263,264]
con_anot=[i+1 for i,v in enumerate(lineas) if v.get('anotaciones')]
print("lineas con campo anotaciones:",len(con_anot))
import collections
tipos=collections.Counter()
for i,v in enumerate(lineas):
    for a in (v.get('anotaciones') or []):
        tipos[a.get('tipo') or a.get('operacion') or json.dumps(sorted(a.keys()))]+=1
print("tipos de anotacion:",dict(tipos))
vd=[i+1 for i,v in enumerate(lineas) if 'VIGENCIA DECLARADA' in json.dumps(v.get('anotaciones') or [],ensure_ascii=False)]
print("lineas con VIGENCIA DECLARADA:",len(vd))
print("cuales:",vd)
print("las 8 esperadas estan:",all(x in vd for x in esperadas))
# de esas, cuales son las SIN HUELLA
print()
for n in esperadas:
    v=lineas[n-1]
    print(n, v['veredicto'], v['candidato'],"vs",v['vecino'],"| len razon",len(v.get('razon') or ''))
