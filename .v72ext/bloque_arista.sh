#!/bin/bash
# COPIA DE LA VUELTA 72 de .v70ext/bloque_arista.sh, con .v70ext y Vuelta 70 cambiados a .v72ext y Vuelta 72 (la de la 70 era COPIA de .v68ext/bloque_arista.sh).
# Anexa al reporte el bloque de una arista cableada: frase de $3 y la salida entera del fichero de $1__$2.
f=.v72ext/arista_$1__$2.txt
{ printf '\n%s Salida entera en `%s`:\n\n' "$3" "$f"; grep -v '^codigo ' "$f" | tr -d '\r' | sed 's/^/    /; s/^ *$//' | cat -s; } >> docs/loop/REPORTE.md
