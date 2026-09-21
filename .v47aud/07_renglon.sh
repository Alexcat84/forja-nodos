#!/bin/sh
# Imprime renglones concretos de cap_04.md con su numero, para casar paso contra libro.
for n in "$@"; do
  printf '=== L%s ===\n' "$n"
  sed -n "${n}p" fuentes/grove_high_output/cap_04.md
done
