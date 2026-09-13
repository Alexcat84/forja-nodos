#!/bin/sh
# Barrido D.38.4 de los 17 candidatos de la vuelta 22, con el MISMO guion y la
# MISMA poblacion declarada que la ACTA 21 seccion 5 (.aud_v21/barrido_uno.py).
cd /c/Users/AlexDesk/Documents/forja-nodos
while read id; do
  [ -z "$id" ] && continue
  python .aud_v21/barrido_uno.py "$id" > .aud_v22/barrido/"$id".txt 2>&1
  echo "hecho $id" >> .aud_v22/barrido/PROGRESO.txt
done < .aud_v22/pendientes.txt
echo "BARRIDO COMPLETO" >> .aud_v22/barrido/PROGRESO.txt
