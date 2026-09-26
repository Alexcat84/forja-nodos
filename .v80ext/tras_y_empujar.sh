#!/bin/bash
# Vuelta 80: encadena .v80ext/tras_insertar.sh y .v80ext/empujar_fila.sh con la nota de la fila, que abre con el bloque de
# .v80ext/contra_barrido.py corrido en el acto. No mide nada nuevo: junta en una llamada los tres pasos que la 77 daba sueltos.
# Uso: bash .v80ext/tras_y_empujar.sh <fila> <id> "<prosa>"
set -e
F=$1; ID=$2; PROSA=$3
bash .v80ext/tras_insertar.sh $F $ID
C=$(python .v80ext/contra_barrido.py $F $ID | tr -d '\r')
bash .v80ext/empujar_fila.sh $F "    \$ python .v80ext/contra_barrido.py $F $ID
    $C

$PROSA"
