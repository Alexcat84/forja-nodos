#!/bin/bash
# Anexa al reporte el bloque de una arista cableada: frase de $3 y la salida entera del fichero de $1__$2.
f=.v67ext/arista_$1__$2.txt
{ printf '\n%s Salida entera en `%s`:\n\n' "$3" "$f"; grep -v '^codigo ' "$f" | tr -d '\r' | sed 's/^/    /; s/^ *$//' | cat -s; } >> docs/loop/REPORTE.md
