#!/bin/bash
# COPIA DE LA VUELTA 74 de .v73ext/citas.sh, con la ruta cambiada a .v74ext/fidelidad.tsv y el capitulo fijo en
# fuentes/scott_radical_candor/cap_13.md, porque los tres nodos de d084 viven en el grafo y no en la bandeja de Grove; nada mas.
# Lo que decia la de la 73: COPIA DE LA VUELTA 73 de .v71ext/citas.sh, con la ruta cambiada a .v73ext/fidelidad.tsv y nada mas (las 7 de cap_15, cap_16 y
# cap_17). Lo que decia la de la 71: COPIA DE LA VUELTA 71 de .v68ext/citas.sh; el capitulo leido de la UNIDAD DE ORIGEN de su ficha.
# se lee de la UNIDAD DE ORIGEN de su ficha (cap_05 o cap_06) en vez de ser cap_04 fijo; y el corte anade el primer
# '? ' con mayuscula, porque en cap_05 y cap_06 hay citas que acaban en pregunta del libro.
# Por cada fila, el grep -n -o del arranque literal de su cita en su capitulo
# (lo que va antes del primer ' ...', del primer '. ' con mayuscula, del primer ', y L' o del primer '; ').
# Imprime el comando y su salida, y al final cuantas filas caen en su linea declarada. Como .v64ext/citas.txt.
ok=0; mal=0
while IFS='|' read -r id paso marca linea nota; do
  l=$(echo $linea | tr -d 'L ')
  frag=$(echo "$nota" | sed 's/^ *//; s/ \.\.\..*//; s/\. [A-Z][a-z].*//; s/? [A-Z][a-z].*//; s/, y L[0-9].*//; s/; .*//; s/ (.*//' | cut -c1-70)
  id=$(echo $id); cap=fuentes/scott_radical_candor/cap_13.md
  echo "\$ grep -n -o -F '$frag' $cap    # $id paso$paso"
  r=$(grep -n -o -F -- "$frag" $cap)
  echo "$r"
  if echo "$r" | grep -q "^$l:"; then ok=$((ok+1)); else mal=$((mal+1)); echo "  NO CAE EN L$l"; fi
done < <(grep -v '^#' .v74ext/fidelidad.tsv)
echo "filas: $((ok+mal)) | en su linea declarada: $ok | fuera: $mal"
