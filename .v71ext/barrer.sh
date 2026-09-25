#!/bin/bash
# COPIA DE LA VUELTA 71 de .v68ext/barrer.sh (que era COPIA de .v66ext/barrer.sh). Lo cambiado en la 71: la ruta .v71ext, la
# lista y el log por argumento (bash .v71ext/barrer.sh <lista> <log>, D71.2: una tanda por capitulo) y la variable
# FORJA_PROCESOS_SIMILITUD=3 del src/aduana.py del fundador (68d6946), para no abrir 19 procesos por ficha (D71.1). Lo de la 68:
# Barrido D.38.4 de los 20 de cap_05 y cap_06 en la bandeja, cinco a la vez
# (no mas: la carga de aduanas en paralelo es sospechosa del cuelgue del equipo del 23 sep).
cd /c/Users/AlexDesk/Documents/forja-nodos
export FORJA_PROCESOS_SIMILITUD=3
echo "INICIO $(date '+%F %T')" > "$2"
grep -v '^#' "$1" | awk 'NF{print $2}' | xargs -P 5 -I{} bash -c '
  t0=$(date +%s); python .v71ext/barrido_uno.py {} > .v71ext/barrido_{}.txt 2>&1; rc=$?; t1=$(date +%s)
  echo "{} rc=$rc segundos=$((t1-t0))" >> '"$2"
echo "TODOS TERMINADOS $(date '+%F %T')" >> "$2"
