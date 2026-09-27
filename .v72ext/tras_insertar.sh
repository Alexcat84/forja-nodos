#!/bin/bash
# COPIA DE LA VUELTA 72 de .v70ext/tras_insertar.sh, con .v70ext y Vuelta 70 cambiados a .v72ext y Vuelta 72 (la de la 70 era COPIA de .v68ext/tras_insertar.sh).
# Tras un insertar que VOLVIO con NODO INSERTADO: mueve la ficha a _insertados (D.31), commitea la
# insercion, anexa la fila tallada al reporte, commitea y pushea. Uso: bash .v72ext/tras_insertar.sh <fila> <id> [nota]
set -e
F=$1; ID=$2
grep -q "NODO INSERTADO" .v72ext/insertar_${F}_${ID}.txt || { echo "NO INSERTADO: no muevo nada"; exit 1; }
git mv cuarentena/grove_high_output/${ID}.json cuarentena/_insertados/grove_high_output/
git add dataset bitacora censos config cuarentena .v72ext
git commit -q -m "Vuelta 72, fila $((10#$F)): ${ID} insertado por la aduana, movido a _insertados

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" > .v72ext/hook_${F}.txt 2>&1 || { cat .v72ext/hook_${F}.txt; exit 1; }
H=$(git rev-parse --short HEAD)
{ echo; python .v72ext/fila.py $F $ID $H | tr -d '\r'; } >> docs/loop/REPORTE.md
echo "$H"
