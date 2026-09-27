#!/bin/bash
# Corre python forja.py informe sobre cada ficha recibida, en paralelo, cada
# una a su fichero en .v8m/aduana/, y anota su tiempo en .v8m/aduana_tiempos.txt
set -u
cd "C:/Users/AlexDesk/Documents/forja-marquet_turn_the_ship"
for ficha in "$@"; do
  (
    inicio=$(date +%s)
    python forja.py informe "cuarentena/marquet_turn_the_ship/${ficha}.json" > ".v8m/aduana/${ficha}.txt" 2>&1
    fin=$(date +%s)
    echo "${ficha} $((fin - inicio))s" >> .v8m/aduana_tiempos.txt
  ) &
done
wait
echo "TANDA RECOGIDA: $@"
