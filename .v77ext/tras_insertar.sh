#!/bin/bash
# COPIA DE LA VUELTA 77 de .v75ext/tras_insertar.sh, con .v75ext, Vuelta 75 y grove_high_output cambiados a .v77ext, Vuelta 77 y gerber_emyth, y el mkdir -p de _insertados/gerber_emyth, que no existe hasta la primera (la de la 75 era COPIA DE LA VUELTA 75 de .v72ext/tras_insertar.sh, con .v72ext y Vuelta 72 cambiados a .v75ext y Vuelta 75; la de la 72 era COPIA de .v70ext/tras_insertar.sh).
# Tras un insertar que VOLVIO con NODO INSERTADO: mueve la ficha a _insertados (D.31), commitea la
# insercion, anexa la fila tallada al reporte, commitea y pushea. Uso: bash .v77ext/tras_insertar.sh <fila> <id> [nota]
set -e
F=$1; ID=$2
grep -q "NODO INSERTADO" .v77ext/insertar_${F}_${ID}.txt || { echo "NO INSERTADO: no muevo nada"; exit 1; }
mkdir -p cuarentena/_insertados/gerber_emyth
git mv cuarentena/gerber_emyth/${ID}.json cuarentena/_insertados/gerber_emyth/
git add dataset bitacora censos config cuarentena .v77ext
git commit -q -m "Vuelta 77, fila $((10#$F)): ${ID} insertado por la aduana, movido a _insertados

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" > .v77ext/hook_${F}.txt 2>&1 || { cat .v77ext/hook_${F}.txt; exit 1; }
H=$(git rev-parse --short HEAD)
{ echo; python .v77ext/fila.py $F $ID $H | tr -d '\r'; } >> docs/loop/REPORTE.md
echo "$H"
