#!/bin/bash
# COPIA DE LA VUELTA 77 de .v75ext/empujar_fila.sh, con .v75ext y Vuelta 75 cambiados a .v77ext y Vuelta 77 (la de la 75 era COPIA DE LA VUELTA 75 de .v72ext/empujar_fila.sh, con .v72ext y Vuelta 72 cambiados a .v75ext y Vuelta 75 (la de la 72 era COPIA de .v70ext/empujar_fila.sh).
# Tras tras_insertar.sh (y las aristas de la fila, si las hay): anexa una nota opcional al reporte, commitea
# docs/loop/ y .v77ext/ con la fila del reporte, y pushea. Uso: bash .v77ext/empujar_fila.sh <fila> "<nota>"
set -e
F=$1; NOTA=$2
[ -n "$NOTA" ] && printf '\n%s\n' "$NOTA" >> docs/loop/REPORTE.md
git add docs/loop/REPORTE.md .v77ext dataset bitacora censos config
git commit -q -m "Vuelta 77, fila $((10#$F)): su fila en el reporte

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" > .v77ext/hook_fila_${F}.txt 2>&1 || { cat .v77ext/hook_fila_${F}.txt; exit 1; }
git push -q 2>&1 | grep -v '^$' || true
git log --oneline -1
