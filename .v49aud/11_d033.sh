#!/bin/sh
# d033: tasa de la corrida intermitente. SEIS corridas aisladas del mismo caso,
# sin tocar tests/ (D.45 prohibe modificar, no correr).
i=1
while [ $i -le 6 ]; do
  inicio=$(date +%s)
  python -m unittest tests.test_aceptacion.PruebaE.test_e_guion_largo_rompe_el_hook > .v49aud/11_d033_corrida_$i.log 2>&1
  codigo=$?
  fin=$(date +%s)
  echo "corrida $i: codigo $codigo, $((fin-inicio)) s"
  i=$((i+1))
done
