#!/bin/bash
# Barrido D.38.4 de la fase ciega de la 66 (copia de .v65aud/barrer.sh con la lista cambiada):
# las filas 21 y 22 ya insertadas (desde _insertados) y los 22 de cap_04 (desde la bandeja), cinco a la vez.
cd /c/Users/AlexDesk/Documents/forja-nodos
echo "INICIO $(date '+%F %T')" > .v66aud/barrido.log
( printf '%s ins\n' variar_frecuencia_inspeccion_nivel_calidad simplificar_trabajo_reducir_numero_pasos; sed 's/$/ ban/' .v66aud/los22_cap04.txt ) | xargs -P 5 -L 1 bash -c '
  t0=$(date +%s); python .v66aud/barrido_uno.py $0 $1 > .v66aud/barrido_$0.txt 2>&1; rc=$?; t1=$(date +%s)
  echo "$0 rc=$rc segundos=$((t1-t0))" >> .v66aud/barrido.log'
echo "TODOS TERMINADOS $(date '+%F %T')" >> .v66aud/barrido.log
