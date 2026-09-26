#!/bin/bash
# COPIA DE LA VUELTA 78 de .v76ext/citas.sh, con las rutas cambiadas a .v78ext/fidelidad.tsv, a fuentes/marquet_turn_the_ship/ y a
# cuarentena/marquet_turn_the_ship/, y nada mas. Lo que decia la de la 76: COPIA DE LA VUELTA 76 de .v73ext/citas.sh, con la ruta cambiada, y UNA cosa mas,
# dicha: la columna de linea admite cap_NN:LNN, y entonces el capitulo que se lee es ese y no el de la UNIDAD DE ORIGEN de la ficha
# (encargo de la 76, TAREA 2.1: hay fichas que citan mas de un capitulo). Lo que decia la de la 73: COPIA DE LA VUELTA 73 de
# .v71ext/citas.sh, con la ruta cambiada. Por cada fila, el grep -n -o del arranque literal de su cita en su capitulo
# (lo que va antes del primer ' ...', del primer '. ' con mayuscula, del primer ', y L' o del primer '; ').
# Imprime el comando y su salida, y al final cuantas filas caen en su linea declarada.
ok=0; mal=0
while IFS='|' read -r id paso marca linea nota; do
  linea=$(echo $linea)
  id=$(echo $id)
  case "$linea" in
    cap_*) cap="fuentes/marquet_turn_the_ship/${linea%%:*}.md"; l=$(echo ${linea#*:} | tr -d 'L ');;
    *) l=$(echo $linea | tr -d 'L '); cap=$(grep -o "fuentes/marquet_turn_the_ship/cap_[0-9][0-9]\.md" cuarentena/marquet_turn_the_ship/$id.json | head -1);;
  esac
  frag=$(echo "$nota" | sed 's/^ *//; s/ \.\.\..*//; s/\. [A-Z][a-z].*//; s/? [A-Z][a-z].*//; s/, y L[0-9].*//; s/; .*//; s/ (.*//' | cut -c1-70)
  echo "\$ grep -n -o -F '$frag' $cap    # $id paso$paso"
  r=$(grep -n -o -F -- "$frag" $cap)
  echo "$r"
  if echo "$r" | grep -q "^$l:"; then ok=$((ok+1)); else mal=$((mal+1)); echo "  NO CAE EN L$l"; fi
done < <(grep -v '^#' .v78ext/fidelidad.tsv)
echo "filas: $((ok+mal)) | en su linea declarada: $ok | fuera: $mal"
