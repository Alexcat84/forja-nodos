#!/bin/bash
# EL PASADOR DE LA ADUANA, UNO POR VEZ (EXTRACTOR.md 16).
#
# NO es un instrumento nuevo de medida ni una guarda: es la MISMA
# python forja.py informe de siempre, puesta en fila para que dos informes no
# se peleen por la maquina. La medida la sigue dando la aduana; esto solo ordena
# el turno. Cada candidato deja su informe en .v2g/informe_<n>_<id>.txt.
#
# Lee .v2g/cola.txt, una ruta por linea, y no repite lo ya hecho.
cd "$(dirname "$0")/.." || exit 1
while true; do
  hecho=1
  while IFS= read -r ruta; do
    [ -z "$ruta" ] && continue
    id=$(basename "$ruta" .json)
    salida=".v2g/informe_${id}.txt"
    if [ ! -s "$salida" ]; then
      hecho=0
      echo "[$(date +%H:%M:%S)] ADUANA EN SECO: $id" >> .v2g/cola.log
      inicio=$(date +%s)
      python forja.py informe "$ruta" > "$salida" 2>&1
      codigo=$?
      fin=$(date +%s)
      echo "[$(date +%H:%M:%S)] $id codigo=$codigo $((fin-inicio))s" >> .v2g/cola.log
    fi
  done < .v2g/cola.txt
  [ "$hecho" = "1" ] && sleep 10
  if [ -f .v2g/cola.fin ]; then
    pendientes=0
    while IFS= read -r ruta; do
      [ -z "$ruta" ] && continue
      id=$(basename "$ruta" .json)
      [ ! -s ".v2g/informe_${id}.txt" ] && pendientes=1
    done < .v2g/cola.txt
    [ "$pendientes" = "0" ] && break
  fi
done
echo "[$(date +%H:%M:%S)] COLA VACIA" >> .v2g/cola.log
