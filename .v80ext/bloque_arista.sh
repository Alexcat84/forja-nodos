#!/bin/bash
# COPIA DE LA VUELTA 80 de .v77ext/bloque_arista.sh, con .v77ext cambiado a .v80ext y nada mas (la de la 77 era COPIA DE LA VUELTA 77 de .v72ext/bloque_arista.sh).
# Anexa al reporte el bloque de una arista cableada: frase de $3 y la salida entera del fichero de $1__$2.
f=.v80ext/arista_$1__$2.txt
{ printf '\n%s Salida entera en `%s`:\n\n' "$3" "$f"; grep -v '^codigo ' "$f" | tr -d '\r' | sed 's/^/    /; s/^ *$//' | cat -s; } >> docs/loop/REPORTE.md
