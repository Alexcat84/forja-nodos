#!/bin/bash
# COPIA DE LA VUELTA 68 de .v66ext/citas.sh. Lo cambiado: la ruta a .v68ext/fidelidad.tsv; el capitulo de cada fila, que
# se lee de la UNIDAD DE ORIGEN de su ficha (cap_05 o cap_06) en vez de ser cap_04 fijo; y el corte anade el primer
# '? ' con mayuscula, porque en cap_05 y cap_06 hay citas que acaban en pregunta del libro.
# Por cada fila, el grep -n -o del arranque literal de su cita en su capitulo
# (lo que va antes del primer ' ...', del primer '. ' con mayuscula, del primer ', y L' o del primer '; ').
# Imprime el comando y su salida, y al final cuantas filas caen en su linea declarada. Como .v64ext/citas.txt.
ok=0; mal=0
while IFS='|' read -r id paso marca linea nota; do
  l=$(echo $linea | tr -d 'L ')
  frag=$(echo "$nota" | sed 's/^ *//; s/ \.\.\..*//; s/\. [A-Z][a-z].*//; s/? [A-Z][a-z].*//; s/, y L[0-9].*//; s/; .*//; s/ (.*//' | cut -c1-70)
  id=$(echo $id); cap=$(grep -o "fuentes/grove_high_output/cap_0[56]\.md" cuarentena/grove_high_output/$id.json | head -1)
  echo "\$ grep -n -o -F '$frag' $cap    # $id paso$paso"
  r=$(grep -n -o -F -- "$frag" $cap)
  echo "$r"
  if echo "$r" | grep -q "^$l:"; then ok=$((ok+1)); else mal=$((mal+1)); echo "  NO CAE EN L$l"; fi
done < <(grep -v '^#' .v68ext/fidelidad.tsv)
echo "filas: $((ok+mal)) | en su linea declarada: $ok | fuera: $mal"
