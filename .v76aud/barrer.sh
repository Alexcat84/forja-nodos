#!/bin/bash
# Barrido D.38.4 de la fase ciega de la 76 (copia de .v73aud/barrer.sh con la lista y la ruta cambiadas):
# las 22 fichas de la bandeja de Gerber (.v76aud/las22.txt), cinco a la vez.
cd /c/Users/AlexDesk/Documents/forja-nodos
echo "INICIO $(date '+%F %T')" > .v76aud/barrido.log
sed 's/$/ ban/' .v76aud/las22.txt | xargs -P 5 -L 1 bash -c '
  t0=$(date +%s); python .v76aud/barrido_uno.py $0 $1 > .v76aud/barrido_$0.txt 2>&1; rc=$?; t1=$(date +%s)
  echo "$0 rc=$rc segundos=$((t1-t0))" >> .v76aud/barrido.log'
echo "TODOS TERMINADOS $(date '+%F %T')" >> .v76aud/barrido.log
