#!/bin/sh
# UN CANDIDATO POR VEZ Y EN EL ORDEN DEL LIBRO (EXTRACTOR.md 2, D.36).
# La cadena PARA en el primero que no entra: un bloqueo se lee, no se salta.
set -e
for ID in "$@"; do
  echo "############ $ID"
  python forja.py insertar "cuarentena/scott_radical_candor/$ID.json" \
    --sin-preguntas --censo serie=no --censo caso=no --censo marco_pais=no \
    --censo vigencia=no --censo herramienta=no
  echo "############ OK $ID"
done
