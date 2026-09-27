#!/bin/bash
# Vuelta 66: por cada fila de .v66ext/fidelidad.tsv, el grep -n -o del arranque literal de su cita en cap_04.md
# (lo que va antes del primer ' ...', del primer '. ' con mayuscula, del primer ', y L' o del primer '; ').
# Imprime el comando y su salida, y al final cuantas filas caen en su linea declarada. Como .v64ext/citas.txt.
ok=0; mal=0
while IFS='|' read -r id paso marca linea nota; do
  l=$(echo $linea | tr -d 'L ')
  frag=$(echo "$nota" | sed 's/^ *//; s/ \.\.\..*//; s/\. [A-Z][a-z].*//; s/, y L[0-9].*//; s/; .*//; s/ (.*//' | cut -c1-70)
  echo "\$ grep -n -o -F '$frag' fuentes/grove_high_output/cap_04.md    # $(echo $id) paso$paso"
  r=$(grep -n -o -F -- "$frag" fuentes/grove_high_output/cap_04.md)
  echo "$r"
  if echo "$r" | grep -q "^$l:"; then ok=$((ok+1)); else mal=$((mal+1)); echo "  NO CAE EN L$l"; fi
done < <(grep -v '^#' .v66ext/fidelidad.tsv)
echo "filas: $((ok+mal)) | en su linea declarada: $ok | fuera: $mal"
