#!/bin/bash
# COPIA DE LA VUELTA 70 de .v68ext/empujar_fila.sh, con .v68ext y Vuelta 68 cambiados a .v70ext y Vuelta 70.
# Tras tras_insertar.sh (y las aristas de la fila, si las hay): anexa una nota opcional al reporte, commitea
# docs/loop/ y .v70ext/ con la fila del reporte, y pushea. Uso: bash .v70ext/empujar_fila.sh <fila> "<nota>"
set -e
F=$1; NOTA=$2
[ -n "$NOTA" ] && printf '\n%s\n' "$NOTA" >> docs/loop/REPORTE.md
git add docs/loop/REPORTE.md .v70ext dataset bitacora censos config
git commit -q -m "Vuelta 70, fila $((10#$F)): su fila en el reporte

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" > .v70ext/hook_fila_${F}.txt 2>&1 || { cat .v70ext/hook_fila_${F}.txt; exit 1; }
git push -q 2>&1 | grep -v '^$' || true
git log --oneline -1
