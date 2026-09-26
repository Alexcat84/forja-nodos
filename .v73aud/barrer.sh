#!/bin/bash
# Barrido D.38.4 de la fase ciega de la 73 (copia de .v71aud/barrer.sh con la lista cambiada):
# las 7 fichas de cap_15, cap_16 y cap_17 (desde la bandeja, .v73aud/los7.txt), cinco a la vez.
cd /c/Users/AlexDesk/Documents/forja-nodos
echo "INICIO $(date '+%F %T')" > .v73aud/barrido.log
sed 's/$/ ban/' .v73aud/los7.txt | xargs -P 5 -L 1 bash -c '
  t0=$(date +%s); python .v73aud/barrido_uno.py $0 $1 > .v73aud/barrido_$0.txt 2>&1; rc=$?; t1=$(date +%s)
  echo "$0 rc=$rc segundos=$((t1-t0))" >> .v73aud/barrido.log'
echo "TODOS TERMINADOS $(date '+%F %T')" >> .v73aud/barrido.log
