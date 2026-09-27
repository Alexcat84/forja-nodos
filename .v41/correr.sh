#!/bin/sh
# El corredor de la vuelta 41, heredado de .v40/correr.sh con UNA cosa nueva, la que
# la TAREA 2 del encargo ordena: `cuadra`, que cuenta los --veredicto del guion contra
# los vecinos del informe ANTES de lanzar, y se niega solo si no cuadran.
#
# No es maquinaria nueva (EXTRACTOR.md 13): es un grep -c y una comparacion de enteros
# dentro del corredor que ya existia. La vuelta 40 perdio sus cuatro inserciones porque
# su guion traia 4 veredictos por lectura y ninguno de los 3 que levanta la senial.
cd /c/Users/AlexDesk/Documents/forja-nodos
COMUN="--sin-preguntas --censo caso=no --censo marco_pais=no --censo vigencia=no --censo herramienta=no"

# LA GUARDA DE LA TAREA 2.2. Dos cuentas y una lista, todo con grep.
cuadra() {
  informe="$1"; guion="$2"
  vecinos=$(grep -c "^    vecino " "$informe")
  veredictos=$(grep -c -- "--veredicto" "$guion")
  echo "GUARDA cuadra: $informe tiene $vecinos vecino(s); $guion trae $veredictos --veredicto"
  if [ "$veredictos" -lt "$vecinos" ]; then
    echo "NO CUADRA: menos veredictos que vecinos. NO SE LANZA."
    return 1
  fi
  faltan=0
  for v in $(grep "^    vecino " "$informe" | awk '{print $2}'); do
    if ! grep -q -- "--veredicto \"$v|" "$guion"; then
      echo "  FALTA el veredicto de $v"
      faltan=$((faltan+1))
    fi
  done
  if [ "$faltan" -gt 0 ]; then
    echo "NO CUADRA: $faltan vecino(s) del informe sin --veredicto. NO SE LANZA."
    return 1
  fi
  echo "CUADRA: los $vecinos vecino(s) del informe tienen su --veredicto en el guion."
  return 0
}

corre() {
  salida="$1"; shift
  id="$1"; shift
  { echo "\$ python forja.py insertar cuarentena/scott_radical_candor/$id.json [veredictos y censos]"
    python forja.py insertar "cuarentena/scott_radical_candor/$id.json" "$@"
    echo "CODIGO DE SALIDA: $?"
  } > ".v41/informes/$salida" 2>&1 < /dev/null
  if ! grep -q "CODIGO DE SALIDA: 0" ".v41/informes/$salida"; then
    echo "PARADA EN $id" >> .v41/informes/_cadena.txt
    exit 1
  fi
  git mv "cuarentena/scott_radical_candor/$id.json" "cuarentena/_insertados/scott_radical_candor/$id.json" >> ".v41/informes/$salida" 2>&1
  echo "  ARCHIVADO EN EL MISMO ACTO (D.31): cuarentena/_insertados/scott_radical_candor/$id.json" >> ".v41/informes/$salida"
  echo "OK $id  ($(wc -l < dataset/nodos.jsonl) nodos, bandeja $(ls cuarentena/scott_radical_candor/*.json | wc -l))" >> .v41/informes/_cadena.txt
}

arista() {
  salida="$1"; shift
  { echo "\$ python forja.py arista --madre $2 --hijo $4 --paso $6 --razon ..."
    python forja.py arista "$@"
    echo "CODIGO DE SALIDA: $?"
  } > ".v41/informes/$salida" 2>&1 < /dev/null
  if ! grep -q "CODIGO DE SALIDA: 0" ".v41/informes/$salida"; then
    echo "PARADA EN ARISTA $salida" >> .v41/informes/_cadena.txt
    exit 1
  fi
  echo "ARISTA ESCRITA ($salida)" >> .v41/informes/_cadena.txt
}

anota() {
  salida="$1"; shift
  { echo "\$ python forja.py anotar --linea $1 --anade \"VIGENCIA DECLARADA ...\" --razon ..."
    python forja.py anotar --linea "$1" --anade "$2" --razon "$3"
    echo "CODIGO DE SALIDA: $?"
  } > ".v41/informes/$salida" 2>&1 < /dev/null
  if ! grep -q "CODIGO DE SALIDA: 0" ".v41/informes/$salida"; then
    echo "PARADA EN ANOTAR LINEA $1" >> .v41/informes/_cadena.txt
    exit 1
  fi
  echo "ANOTADA LINEA $1 (vigencia declarada)" >> .v41/informes/_cadena.txt
}
