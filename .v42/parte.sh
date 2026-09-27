#!/bin/sh
# EL CORREDOR DE LAS PARTES DE LA SERIE DE TRECE.
# Monta el comando de insercion con: los veredictos PROPIOS que escribo a mano para cada
# candidato (.v42/propios_<n>.txt) mas la linea SANO de cada HERMANO que siga en la
# bandeja, impresa por .v42/hermanos.py. No decide nada: solo evita que un hermano se me
# quede sin veredicto y me cueste una corrida entera de la aduana.
#   uso: sh .v42/parte.sh <n> <id> <censo_serie>
cd /c/Users/AlexDesk/Documents/forja-nodos
N="$1"; ID="$2"; CENSO="$3"
COMUN="--sin-preguntas --censo caso=no --censo marco_pais=no --censo vigencia=no --censo herramienta=no"
GUION=".v42/comando_$N.sh"
{
  echo "python forja.py insertar cuarentena/scott_radical_candor/$ID.json \\"
  cat ".v42/propios_$N.txt"
  python .v42/hermanos.py "$ID"
  echo " --censo \"$CENSO\" $COMUN"
} > "$GUION"
date "+%H:%M:%S arranca insercion candidato $N ($ID)" >> .v42/informes/_tiempos.txt
{
  echo "\$ python forja.py insertar cuarentena/scott_radical_candor/$ID.json [veredictos y censos]"
  sh "$GUION"
  echo "CODIGO DE SALIDA: $?"
} > ".v42/informes/n${N}_${ID}.txt" 2>&1 < /dev/null
date "+%H:%M:%S termina insercion candidato $N" >> .v42/informes/_tiempos.txt
tail -12 ".v42/informes/n${N}_${ID}.txt"
