#!/bin/bash
# Barrido D.38.4 de la fase ciega de la 78 (copia de .v76aud/barrer.sh con la lista y la ruta cambiadas):
# las 20 fichas de la bandeja de Marquet (.v78aud/las20.txt), cinco a la vez.
cd /c/Users/AlexDesk/Documents/forja-nodos
echo "INICIO $(date '+%F %T')" > .v78aud/barrido.log
sed 's/$/ ban/' .v78aud/las20.txt | xargs -P 5 -L 1 bash -c '
  t0=$(date +%s); python .v78aud/barrido_uno.py $0 $1 > .v78aud/barrido_$0.txt 2>&1; rc=$?; t1=$(date +%s)
  echo "$0 rc=$rc segundos=$((t1-t0))" >> .v78aud/barrido.log'
echo "TODOS TERMINADOS $(date '+%F %T')" >> .v78aud/barrido.log
