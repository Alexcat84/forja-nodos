#!/bin/bash
cd /c/Users/AlexDesk/Documents/forja-nodos
export PYTHONIOENCODING=utf-8
while read -r f; do
  id="${f%.json}"; [ -z "$id" ] && continue
  [ -s ".v30b/barrido/$id.txt" ] && { echo "ya $id"; continue; }
  rm -f .v30b/uno/*.json
  cp "cuarentena/_insertados/scott_radical_candor/$id.json" .v30b/uno/
  python -c "
import io,json,sys
idx=sys.argv[1]
out=[l for l in io.open('dataset/nodos.jsonl',encoding='utf-8') if l.strip() and json.loads(l).get('id')!=idx]
assert len(out)==255, len(out)
io.open('.v30b/pob.jsonl','w',encoding='utf-8').writelines(out)
" "$id" || { echo "FALLO $id"; continue; }
  FORJA_DATASET=".v30b/pob.jsonl" python forja.py informe --carpeta .v30b/uno > ".v30b/barrido/$id.txt" 2>&1
  echo "hecho $id : $(grep -c '^    vecino ' .v30b/barrido/$id.txt)"
done < .v30b/los13.txt
echo FIN
