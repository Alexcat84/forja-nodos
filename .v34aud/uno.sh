#!/bin/sh
RUTA="$1"
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
" "$ID" ".v34aud/pob/$ID.jsonl" > ".v34aud/vec_$ID.txt"
echo "===== BARRIDO DE $ID =====" >> ".v34aud/vec_$ID.txt"
FORJA_DATASET=".v34aud/pob/$ID.jsonl" python forja.py informe ".v34aud/cand/$ID.json" >> ".v34aud/vec_$ID.txt" 2>&1
echo "LISTO $ID"
