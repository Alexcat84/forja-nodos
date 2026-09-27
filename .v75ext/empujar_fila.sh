#!/bin/bash
# COPIA DE LA VUELTA 75 de .v72ext/empujar_fila.sh, con .v72ext y Vuelta 72 cambiados a .v75ext y Vuelta 75 (la de la 72 era COPIA de .v70ext/empujar_fila.sh).
# Tras tras_insertar.sh (y las aristas de la fila, si las hay): anexa una nota opcional al reporte, commitea
# docs/loop/ y .v75ext/ con la fila del reporte, y pushea. Uso: bash .v75ext/empujar_fila.sh <fila> "<nota>"
set -e
F=$1; NOTA=$2
[ -n "$NOTA" ] && printf '\n%s\n' "$NOTA" >> docs/loop/REPORTE.md
git add docs/loop/REPORTE.md .v75ext dataset bitacora censos config
git commit -q -m "Vuelta 75, fila $((10#$F)): su fila en el reporte

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" > .v75ext/hook_fila_${F}.txt 2>&1 || { cat .v75ext/hook_fila_${F}.txt; exit 1; }
git push -q 2>&1 | grep -v '^$' || true
git log --oneline -1
