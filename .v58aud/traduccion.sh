# DISCUTIBLE 5: SI OTRA FICHA DEL CATALOGO CITA esteem/recognition O self-actualization EN INGLES DENTRO DE SUS PASOS
echo "-- 'self-actualization' en el grafo:"; grep -c "self-actualization" dataset/nodos.jsonl
echo "-- 'esteem/recognition' en el grafo:"; grep -c "esteem/recognition" dataset/nodos.jsonl
echo "-- 'autorrealizacion' en el grafo:"; grep -c "autorrealizacion" dataset/nodos.jsonl
echo "-- en que nodo y en que campo:"
python -c "
import json,io
for l in io.open('dataset/nodos.jsonl',encoding='utf-8'):
    d=json.loads(l); s=json.dumps(d,ensure_ascii=False)
    if 'autorrealizacion' in s:
        print(' nodo:',d['id'])
        for k,v in d.items():
            if 'autorrealizacion' in json.dumps(v,ensure_ascii=False): print('   campo:',k)
"
