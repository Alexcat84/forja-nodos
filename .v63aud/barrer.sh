#!/bin/bash
# Barrido D.38.4 vigente: uno por vez, la aduana pone las bandejas.
cd /c/Users/AlexDesk/Documents/forja-nodos
while read id; do
  (
    t0=$(date +%s)
    python forja.py informe "cuarentena/grove_high_output/$id.json" > ".v63aud/informe_$id.txt" 2>&1
    rc=$?
    t1=$(date +%s)
    echo "$id rc=$rc segundos=$((t1-t0))" >> .v63aud/barrido.log
  ) &
done < .v63aud/tanda.txt
wait
echo "TODOS TERMINADOS $(date '+%F %T')" >> .v63aud/barrido.log
