#!/bin/sh
# ARMA EL CIERRE DE LA VUELTA 23: corre cada instrumento, guarda su salida, y
# pega cada tabla en su marcador del fragmento. Ninguna celda se teclea.
set -e
cd /c/Users/AlexDesk/Documents/forja-nodos

python .t1_v23/saldo_v23.py       > .t1_v23/salida_saldo_v23.txt 2>&1
python .t1_v23/veredictos_v23.py  > .t1_v23/salida_veredictos_v23.txt 2>&1
python .t1_v23/cierre_v23.py      > .t1_v23/salida_cierre_v23.txt 2>&1
python .t1_v23/freno_v23.py       > .t1_v23/salida_freno_v23.txt 2>&1

python forja.py gate              > .t1_v23/salida_gate_cierre.txt 2>&1
python forja.py guiones           > .t1_v23/salida_guiones_cierre.txt 2>&1
python tests/test_aceptacion.py   > .t1_v23/salida_aceptacion_cierre.txt 2>&1

{
  echo '$ git rev-parse --abbrev-ref HEAD'
  git rev-parse --abbrev-ref HEAD
  echo '$ git log --oneline b05d040..HEAD | wc -l'
  git log --oneline b05d040..HEAD | wc -l
  echo '$ git log -1 --format="%h %ad" --date=iso'
  git log -1 --format='%h %ad' --date=iso
  echo '$ git diff --name-only b05d040..HEAD | sed "s#/.*##" | sort | uniq -c'
  git diff --name-only b05d040..HEAD | sed 's#/.*##' | sort | uniq -c
} > .t1_v23/identidad_v23.txt 2>&1

echo "INSTRUMENTOS DEL CIERRE CORRIDOS"
