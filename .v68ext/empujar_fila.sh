#!/bin/bash
# COPIA DE LA VUELTA 68 de .v67ext/empujar_fila.sh, con .v67ext y Vuelta 67 cambiados a .v68ext y Vuelta 68.
# Tras tras_insertar.sh (y las aristas de la fila, si las hay): anexa una nota opcional al reporte, commitea
# docs/loop/ y .v68ext/ con la fila del reporte, y pushea. Uso: bash .v68ext/empujar_fila.sh <fila> "<nota>"
set -e
F=$1; NOTA=$2
[ -n "$NOTA" ] && printf '\n%s\n' "$NOTA" >> docs/loop/REPORTE.md
git add docs/loop/REPORTE.md .v68ext dataset bitacora censos config
git commit -q -m "Vuelta 68, fila $((10#$F)): su fila en el reporte

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" > .v68ext/hook_fila_${F}.txt 2>&1 || { cat .v68ext/hook_fila_${F}.txt; exit 1; }
git push -q 2>&1 | grep -v '^$' || true
git log --oneline -1
