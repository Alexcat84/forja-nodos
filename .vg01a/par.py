import json,sys
print("INSTRUMENTO .vg01a/par.py  SIN CONSTANTES TECLEADAS: los dos ids llegan por argumento y todo lo demas sale de dataset/nodos.jsonl")
n={x['id']:x for x in (json.loads(l) for l in open('dataset/nodos.jsonl',encoding='utf-8') if l.strip())}
for i in sys.argv[1:]:
    x=n[i]
    print("="*100); print(i,"|",x['titulo'],"| dominio",x['dominio'])
    print("ENTREGABLE:",x['entregable_esperado'])
    print("ACTIVACION:",x['condiciones_activacion'])
    print("PASOS (%d):"%len(x['pasos_accionables']))
    for k,p in enumerate(x['pasos_accionables'],1): print("  %2d. %s"%(k,p))
