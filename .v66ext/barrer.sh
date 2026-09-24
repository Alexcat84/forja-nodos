#!/bin/bash
# COPIA DE LA VUELTA 66 de .v65aud/barrer.sh, con la lista de cap_04 (.v66ext/los22_cap04.txt) y la ruta .v66ext.
# Barrido D.38.4 de los 22 de cap_04 en la bandeja, cinco a la vez
# (no mas: la carga de aduanas en paralelo es sospechosa del cuelgue del equipo del 23 sep).
cd /c/Users/AlexDesk/Documents/forja-nodos
echo "INICIO $(date '+%F %T')" > .v66ext/barrido.log
grep -v '^#' .v66ext/los22_cap04.txt | awk 'NF{print $1}' | xargs -P 5 -I{} bash -c '
  t0=$(date +%s); python .v66ext/barrido_uno.py {} > .v66ext/barrido_{}.txt 2>&1; rc=$?; t1=$(date +%s)
  echo "{} rc=$rc segundos=$((t1-t0))" >> .v66ext/barrido.log'
echo "TODOS TERMINADOS $(date '+%F %T')" >> .v66ext/barrido.log
