#!/bin/bash
# COPIA DE LA VUELTA 80 de .v77ext/tras_insertar.sh, con .v77ext, Vuelta 77 y gerber_emyth cambiados a .v80ext, Vuelta 80 y marquet_turn_the_ship, y nada mas; el mkdir -p de _insertados/marquet_turn_the_ship, que no existe hasta la primera, ya venia en la de la 77, que era COPIA DE LA VUELTA 77 de .v75ext/tras_insertar.sh.
# Tras un insertar que VOLVIO con NODO INSERTADO: mueve la ficha a _insertados (D.31), commitea la
# insercion, anexa la fila tallada al reporte, commitea y pushea. Uso: bash .v80ext/tras_insertar.sh <fila> <id> [nota]
set -e
F=$1; ID=$2
grep -q "NODO INSERTADO" .v80ext/insertar_${F}_${ID}.txt || { echo "NO INSERTADO: no muevo nada"; exit 1; }
mkdir -p cuarentena/_insertados/marquet_turn_the_ship
git mv cuarentena/marquet_turn_the_ship/${ID}.json cuarentena/_insertados/marquet_turn_the_ship/
git add dataset bitacora censos config cuarentena .v80ext
git commit -q -m "Vuelta 80, fila $((10#$F)): ${ID} insertado por la aduana, movido a _insertados

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" > .v80ext/hook_${F}.txt 2>&1 || { cat .v80ext/hook_${F}.txt; exit 1; }
H=$(git rev-parse --short HEAD)
{ echo; python .v80ext/fila.py $F $ID $H | tr -d '\r'; } >> docs/loop/REPORTE.md
echo "$H"
