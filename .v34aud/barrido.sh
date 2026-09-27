#!/bin/sh
# D.38.4 / D.38.5: poblacion = GRAFO MAS BANDEJAS. Las bandejas las pone la
# aduana sola; el grafo lo recorto yo quitando el propio candidato, porque el
# nodo ya vive dentro (ACTA 18). CERO IDS TECLEADOS: salen de .v34aud/tanda.txt.
set -e
mkdir -p .v34aud/cand .v34aud/pob
while read RUTA; do
  ID=$(basename "$RUTA" .json)
  cp "$RUTA" ".v34aud/cand/$ID.json"
  python -c "
import json,sys,io
ident=sys.argv[1]
sal=io.open(sys.argv[2],'w',encoding='utf-8')
n=0
for linea in io.open('dataset/nodos.jsonl',encoding='utf-8'):
    if not linea.strip(): continue
    if json.loads(linea).get('id')==ident: n+=1; continue
    sal.write(linea)
sal.close()
print('    poblacion de grafo para %s: quitadas %d lineas suyas'%(ident,n))
" "$ID" ".v34aud/pob/$ID.jsonl"
  echo "===== BARRIDO DE $ID ====="
  FORJA_DATASET=".v34aud/pob/$ID.jsonl" python forja.py informe ".v34aud/cand/$ID.json"
done < .v34aud/tanda.txt
