#!/bin/sh
# PRIMERA LINEA (HEREDADO 4): ESTE INSTRUMENTO NO TIENE NI UNA LISTA DE IDS TECLEADA.
# Los ids de la tanda salen de .v33a/tanda_ids.txt, que .v33a/tanda.py genero del
# git diff de dataset/nodos.jsonl entre ef3e7f9 y HEAD, es decir DEL DATO.
# POBLACION DE CADA CORRIDA (D.38.4 mas D.38.5): dataset/nodos.jsonl de 282 nodos
# MENOS el propio candidato, mas las bandejas de cuarentena/, que las pone la aduana sola.
set -e
mkdir -p .v33a/cand .v33a/pob
while read ID; do
  [ -z "$ID" ] && continue
  cp "cuarentena/_insertados/scott_radical_candor/$ID.json" ".v33a/cand/$ID.json"
  python -c "
import json,sys,io
ident=sys.argv[1]
sal=io.open(sys.argv[2],'w',encoding='utf-8'); n=0; q=0
for linea in io.open('dataset/nodos.jsonl',encoding='utf-8'):
    if not linea.strip(): continue
    if json.loads(linea).get('id')==ident: n+=1; continue
    sal.write(linea); q+=1
sal.close()
print('    poblacion de grafo para %s: quitadas %d lineas suyas, quedan %d'%(ident,n,q))
" "$ID" ".v33a/pob/$ID.jsonl"
  echo "===== BARRIDO DE $ID ====="
  FORJA_DATASET=".v33a/pob/$ID.jsonl" python forja.py informe ".v33a/cand/$ID.json"
done < .v33a/tanda_ids.txt
