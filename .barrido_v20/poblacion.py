# D.38.4: poblacion = dataset/nodos.jsonl + cuarentena/<libro>/*.json
# descartando _insertados y _derivadas. Y, por la correccion declarada de la
# ACTA 18, MENOS EL PROPIO CANDIDATO: un nodo no es vecino de si mismo.
import io, json, glob, os, sys

grafo = [l for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
bandeja = [p for p in glob.glob(os.path.join('cuarentena', '*', '*.json'))
           if '_insertados' not in p and '_derivadas' not in p]
bandeja.sort()
excluir = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1] else None
salida = sys.argv[2] if len(sys.argv) > 2 else '.barrido_v20/pob.jsonl'

filas = list(grafo)
usados = 0
for p in bandeja:
    if excluir and os.path.abspath(p) == excluir:
        continue
    filas.append(json.dumps(json.load(io.open(p, encoding='utf-8')), ensure_ascii=False) + chr(10))
    usados += 1
io.open(salida, 'w', encoding='utf-8').writelines(filas)
sys.stderr.write('grafo=%d bandeja=%d total=%d' % (len(grafo), usados, len(filas)) + chr(10))
