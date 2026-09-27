#!/bin/bash
# COPIA DE LA VUELTA 70 de .v68ext/bloque_arista.sh, con .v68ext y Vuelta 68 cambiados a .v70ext y Vuelta 70.
# Anexa al reporte el bloque de una arista cableada: frase de $3 y la salida entera del fichero de $1__$2.
f=.v70ext/arista_$1__$2.txt
{ printf '\n%s Salida entera en `%s`:\n\n' "$3" "$f"; grep -v '^codigo ' "$f" | tr -d '\r' | sed 's/^/    /; s/^ *$//' | cat -s; } >> docs/loop/REPORTE.md
