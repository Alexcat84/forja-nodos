#!/bin/sh
# El corredor de la vuelta 39. El archivado D.31 va DENTRO de la misma funcion que
# corre la aduana, detras de su codigo de salida: remedio mecanico, no memoria.
cd /c/Users/AlexDesk/Documents/forja-nodos
COMUN="--sin-preguntas --censo caso=no --censo marco_pais=no --censo vigencia=no --censo herramienta=no"

corre() {
  salida="$1"; shift
  id="$1"; shift
  { echo "\$ python forja.py insertar cuarentena/scott_radical_candor/$id.json [veredictos y censos]"
    python forja.py insertar "cuarentena/scott_radical_candor/$id.json" "$@"
    echo "CODIGO DE SALIDA: $?"
  } > ".v39/informes/$salida" 2>&1 < /dev/null
  if ! grep -q "CODIGO DE SALIDA: 0" ".v39/informes/$salida"; then
    echo "PARADA EN $id" >> .v39/informes/_cadena.txt
    exit 1
  fi
  git mv "cuarentena/scott_radical_candor/$id.json" "cuarentena/_insertados/scott_radical_candor/$id.json" >> ".v39/informes/$salida" 2>&1
  echo "  ARCHIVADO EN EL MISMO ACTO (D.31): cuarentena/_insertados/scott_radical_candor/$id.json" >> ".v39/informes/$salida"
  echo "OK $id  ($(wc -l < dataset/nodos.jsonl) nodos, bandeja $(ls cuarentena/scott_radical_candor/*.json | wc -l))" >> .v39/informes/_cadena.txt
}

arista() {
  salida="$1"; shift
  { echo "\$ python forja.py arista --madre $1 --hijo $2 --paso $3 --razon ..."
    python forja.py arista --madre "$1" --hijo "$2" --paso "$3" --razon "$4"
    echo "CODIGO DE SALIDA: $?"
  } > ".v39/informes/$salida" 2>&1 < /dev/null
  if ! grep -q "CODIGO DE SALIDA: 0" ".v39/informes/$salida"; then
    echo "PARADA EN ARISTA $1 > $2" >> .v39/informes/_cadena.txt
    exit 1
  fi
  echo "ARISTA $1 > $2 (paso $3)" >> .v39/informes/_cadena.txt
}
