#!/bin/bash
cd /c/Users/AlexDesk/Documents/forja-nodos
export PYTHONIOENCODING=utf-8
while read -r id; do
  [ -z "$id" ] && continue
  rm -f .v30a/uno2/*.json
  cp "cuarentena/_insertados/scott_radical_candor/$id.json" .v30a/uno2/
  python -c "
import io,json,sys
idx=sys.argv[1]
out=[l for l in io.open('dataset/nodos.jsonl',encoding='utf-8') if l.strip() and json.loads(l).get('id')!=idx]
assert len(out)==255, len(out)
io.open('.v30a/pob2.jsonl','w',encoding='utf-8').writelines(out)
" "$id" || { echo "FALLO poblacion $id"; continue; }
  FORJA_DATASET=".v30a/pob2.jsonl" python forja.py informe --carpeta .v30a/uno2 > ".v30a/barrido2/$id.txt" 2>&1
  echo "hecho $id : $(grep -o 'poblacion del barrido.*' .v30a/barrido2/$id.txt)"
done < .v30a/los13.txt
echo FIN
