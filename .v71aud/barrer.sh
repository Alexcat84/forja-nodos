#!/bin/bash
# Barrido D.38.4 de la fase ciega de la 71 (copia de .v68aud/barrer.sh con la lista cambiada):
# las 20 fichas de cap_07, cap_10 a cap_14 (desde la bandeja, .v71aud/los20.txt), cinco a la vez.
cd /c/Users/AlexDesk/Documents/forja-nodos
echo "INICIO $(date '+%F %T')" > .v71aud/barrido.log
sed 's/$/ ban/' .v71aud/los20.txt | xargs -P 5 -L 1 bash -c '
  t0=$(date +%s); python .v71aud/barrido_uno.py $0 $1 > .v71aud/barrido_$0.txt 2>&1; rc=$?; t1=$(date +%s)
  echo "$0 rc=$rc segundos=$((t1-t0))" >> .v71aud/barrido.log'
echo "TODOS TERMINADOS $(date '+%F %T')" >> .v71aud/barrido.log
