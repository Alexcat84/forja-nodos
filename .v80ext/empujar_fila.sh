#!/bin/bash
# COPIA DE LA VUELTA 80 de .v77ext/empujar_fila.sh, con .v77ext y Vuelta 77 cambiados a .v80ext y Vuelta 80, y nada mas (la de la 77 era COPIA DE LA VUELTA 77 de .v75ext/empujar_fila.sh).
# Tras tras_insertar.sh (y las aristas de la fila, si las hay): anexa una nota opcional al reporte, commitea
# docs/loop/ y .v80ext/ con la fila del reporte, y pushea. Uso: bash .v80ext/empujar_fila.sh <fila> "<nota>"
set -e
F=$1; NOTA=$2
[ -n "$NOTA" ] && printf '\n%s\n' "$NOTA" >> docs/loop/REPORTE.md
git add docs/loop/REPORTE.md .v80ext dataset bitacora censos config
git commit -q -m "Vuelta 80, fila $((10#$F)): su fila en el reporte

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" > .v80ext/hook_fila_${F}.txt 2>&1 || { cat .v80ext/hook_fila_${F}.txt; exit 1; }
git push -q 2>&1 | grep -v '^$' || true
git log --oneline -1
