#!/bin/bash
# Barrido D.38.4 de la fase ciega de la 65: los 20 insertados de la tanda, cinco a la vez
# (no mas: la carga de aduanas en paralelo es sospechosa del cuelgue del equipo del 23 sep).
cd /c/Users/AlexDesk/Documents/forja-nodos
echo "INICIO $(date '+%F %T')" > .v65aud/barrido.log
grep -v '^#' .v64ext/los22.txt | awk 'NF{print $1}' | head -20 | xargs -P 5 -I{} bash -c '
  t0=$(date +%s); python .v65aud/barrido_uno.py {} > .v65aud/barrido_{}.txt 2>&1; rc=$?; t1=$(date +%s)
  echo "{} rc=$rc segundos=$((t1-t0))" >> .v65aud/barrido.log'
echo "TODOS TERMINADOS $(date '+%F %T')" >> .v65aud/barrido.log
