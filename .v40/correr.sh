#!/bin/sh
# El corredor de la vuelta 40, heredado entero de .v39/correr.sh. El archivado D.31
# va DENTRO de la misma funcion que corre la aduana, detras de su codigo de salida:
# remedio mecanico, no memoria.
cd /c/Users/AlexDesk/Documents/forja-nodos
COMUN="--sin-preguntas --censo caso=no --censo marco_pais=no --censo vigencia=no --censo herramienta=no"

corre() {
  salida="$1"; shift
  id="$1"; shift
  { echo "\$ python forja.py insertar cuarentena/scott_radical_candor/$id.json [veredictos y censos]"
    python forja.py insertar "cuarentena/scott_radical_candor/$id.json" "$@"
    echo "CODIGO DE SALIDA: $?"
  } > ".v40/informes/$salida" 2>&1 < /dev/null
  if ! grep -q "CODIGO DE SALIDA: 0" ".v40/informes/$salida"; then
    echo "PARADA EN $id" >> .v40/informes/_cadena.txt
    exit 1
  fi
  git mv "cuarentena/scott_radical_candor/$id.json" "cuarentena/_insertados/scott_radical_candor/$id.json" >> ".v40/informes/$salida" 2>&1
  echo "  ARCHIVADO EN EL MISMO ACTO (D.31): cuarentena/_insertados/scott_radical_candor/$id.json" >> ".v40/informes/$salida"
  echo "OK $id  ($(wc -l < dataset/nodos.jsonl) nodos, bandeja $(ls cuarentena/scott_radical_candor/*.json | wc -l))" >> .v40/informes/_cadena.txt
}

anota() {
  salida="$1"; shift
  { echo "\$ python forja.py anotar --linea $1 --anade \"VIGENCIA DECLARADA ...\" --razon ..."
    python forja.py anotar --linea "$1" --anade "$2" --razon "$3"
    echo "CODIGO DE SALIDA: $?"
  } > ".v40/informes/$salida" 2>&1 < /dev/null
  if ! grep -q "CODIGO DE SALIDA: 0" ".v40/informes/$salida"; then
    echo "PARADA EN ANOTAR LINEA $1" >> .v40/informes/_cadena.txt
    exit 1
  fi
  echo "ANOTADA LINEA $1 (vigencia declarada)" >> .v40/informes/_cadena.txt
}
