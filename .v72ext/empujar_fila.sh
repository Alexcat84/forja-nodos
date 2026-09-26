#!/bin/bash
# COPIA DE LA VUELTA 72 de .v70ext/empujar_fila.sh, con .v70ext y Vuelta 70 cambiados a .v72ext y Vuelta 72 (la de la 70 era COPIA de .v68ext/empujar_fila.sh).
# Tras tras_insertar.sh (y las aristas de la fila, si las hay): anexa una nota opcional al reporte, commitea
# docs/loop/ y .v72ext/ con la fila del reporte, y pushea. Uso: bash .v72ext/empujar_fila.sh <fila> "<nota>"
set -e
F=$1; NOTA=$2
[ -n "$NOTA" ] && printf '\n%s\n' "$NOTA" >> docs/loop/REPORTE.md
git add docs/loop/REPORTE.md .v72ext dataset bitacora censos config
git commit -q -m "Vuelta 72, fila $((10#$F)): su fila en el reporte

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" > .v72ext/hook_fila_${F}.txt 2>&1 || { cat .v72ext/hook_fila_${F}.txt; exit 1; }
git push -q 2>&1 | grep -v '^$' || true
git log --oneline -1
