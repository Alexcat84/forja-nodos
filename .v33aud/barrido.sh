#!/bin/sh
# PRIMERA LINEA, D.40 HEREDADO 4: ESTE INSTRUMENTO NO TIENE NI UNA LISTA DE IDS
# TECLEADA. Los ids de la tanda salen de `git diff --name-only 74ddc8c HEAD`, es
# decir del dato, y la poblacion de cada corrida sale de dataset/nodos.jsonl
# menos el propio candidato (D.38.4 corregida en ACTA 18: uno por vez, su id
# excluido). Las bandejas las pone la aduana sola (metodo vigente, D.38.5).
set -e
mkdir -p .v33aud/cand .v33aud/pob
git diff --name-only 74ddc8c HEAD -- cuarentena/_insertados/ > .v33aud/tanda.txt
while read RUTA; do
  ID=$(basename "$RUTA" .json)
  cp "$RUTA" ".v33aud/cand/$ID.json"
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
" "$ID" ".v33aud/pob/$ID.jsonl"
  echo "===== BARRIDO DE $ID ====="
  FORJA_DATASET=".v33aud/pob/$ID.jsonl" python forja.py informe ".v33aud/cand/$ID.json"
done < .v33aud/tanda.txt
