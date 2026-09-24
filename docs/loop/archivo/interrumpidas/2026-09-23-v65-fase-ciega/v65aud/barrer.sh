#!/bin/bash
# Barrido D.38.4 de la fase ciega de la 65: las 20 filas de la tanda, una por proceso, y se espera a todas.
cd /c/Users/AlexDesk/Documents/forja-nodos
echo "INICIO $(date '+%F %T')" > .v65aud/barrido.log
for id in $(awk 'NR>1 && $1+0>=1 && $1+0<=20 {print $2}' .v64ext/orden.txt); do
  (
    t0=$(date +%s)
    python .v65aud/barrido_uno.py "$id" > ".v65aud/err_$id.txt" 2>&1
    rc=$?
    t1=$(date +%s)
    echo "$id rc=$rc segundos=$((t1-t0))" >> .v65aud/barrido.log
  ) &
done
wait
echo "TODOS TERMINADOS $(date '+%F %T')" >> .v65aud/barrido.log
