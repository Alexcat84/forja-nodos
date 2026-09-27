#!/bin/bash
# Barrido D.38.4 de la fase ciega de la 68 (copia de .v66aud/barrer.sh con la lista cambiada):
# las filas 21 y 22 de cap_04 ya insertadas (desde _insertados) y los 20 de cap_05 y cap_06 (desde la bandeja), cinco a la vez.
cd /c/Users/AlexDesk/Documents/forja-nodos
echo "INICIO $(date '+%F %T')" > .v68aud/barrido.log
( printf '%s ins\n' agrupar_interrupciones_subordinados_reuniones_regulares canalizar_interrupciones_cartel_hora_oficina; sed 's/$/ ban/' .v68aud/los20.txt ) | xargs -P 5 -L 1 bash -c '
  t0=$(date +%s); python .v68aud/barrido_uno.py $0 $1 > .v68aud/barrido_$0.txt 2>&1; rc=$?; t1=$(date +%s)
  echo "$0 rc=$rc segundos=$((t1-t0))" >> .v68aud/barrido.log'
echo "TODOS TERMINADOS $(date '+%F %T')" >> .v68aud/barrido.log
