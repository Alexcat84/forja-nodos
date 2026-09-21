#!/bin/sh
# El corredor de la vuelta 37. EL ARCHIVADO D.31 VA DENTRO DE LA MISMA FUNCION QUE
# CORRE LA ADUANA, detras de su codigo de salida: es remedio mecanico y no memoria,
# que es lo que el encargo pide tras la caida de la vuelta 36.
cd /c/Users/AlexDesk/Documents/forja-nodos
COMUN="--sin-preguntas --censo caso=no --censo marco_pais=no --censo vigencia=no --censo herramienta=no"

corre() {
  salida="$1"; shift
  id="$1"; shift
  { echo "\$ python forja.py insertar cuarentena/scott_radical_candor/$id.json [veredictos y censos]"
    python forja.py insertar "cuarentena/scott_radical_candor/$id.json" "$@"
    echo "CODIGO DE SALIDA: $?"
  } > ".v37/informes/$salida" 2>&1 < /dev/null
  if ! grep -q "CODIGO DE SALIDA: 0" ".v37/informes/$salida"; then
    echo "PARADA EN $id" >> .v37/informes/_cadena.txt
    exit 1
  fi
  git mv "cuarentena/scott_radical_candor/$id.json" "cuarentena/_insertados/scott_radical_candor/$id.json" >> ".v37/informes/$salida" 2>&1
  echo "  ARCHIVADO EN EL MISMO ACTO (D.31): cuarentena/_insertados/scott_radical_candor/$id.json" >> ".v37/informes/$salida"
  echo "OK $id  ($(wc -l < dataset/nodos.jsonl) nodos, bandeja $(ls cuarentena/scott_radical_candor/*.json | wc -l))" >> .v37/informes/_cadena.txt
}

arista() {
  salida="$1"; shift
  { echo "\$ python forja.py arista --madre $1 --hijo $2 --paso $3 --razon ..."
    python forja.py arista --madre "$1" --hijo "$2" --paso "$3" --razon "$4"
    echo "CODIGO DE SALIDA: $?"
  } > ".v37/informes/$salida" 2>&1 < /dev/null
  if ! grep -q "CODIGO DE SALIDA: 0" ".v37/informes/$salida"; then
    echo "PARADA EN ARISTA $1 > $2" >> .v37/informes/_cadena.txt
    exit 1
  fi
  echo "ARISTA $1 > $2 (paso $3)" >> .v37/informes/_cadena.txt
}
