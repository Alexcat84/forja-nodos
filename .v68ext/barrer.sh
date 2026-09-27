#!/bin/bash
# COPIA DE LA VUELTA 68 de .v66ext/barrer.sh, con la lista de cap_05 y cap_06 (.v68ext/los20_cap05_cap06.txt) y la ruta .v68ext.
# Barrido D.38.4 de los 20 de cap_05 y cap_06 en la bandeja, cinco a la vez
# (no mas: la carga de aduanas en paralelo es sospechosa del cuelgue del equipo del 23 sep).
cd /c/Users/AlexDesk/Documents/forja-nodos
echo "INICIO $(date '+%F %T')" > .v68ext/barrido.log
grep -v '^#' .v68ext/los20_cap05_cap06.txt | awk 'NF{print $1}' | xargs -P 5 -I{} bash -c '
  t0=$(date +%s); python .v68ext/barrido_uno.py {} > .v68ext/barrido_{}.txt 2>&1; rc=$?; t1=$(date +%s)
  echo "{} rc=$rc segundos=$((t1-t0))" >> .v68ext/barrido.log'
echo "TODOS TERMINADOS $(date '+%F %T')" >> .v68ext/barrido.log
