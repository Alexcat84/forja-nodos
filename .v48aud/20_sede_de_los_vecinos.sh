#!/bin/sh
# De los 8 vecinos mas proximos de cada uno de los 5 candidatos (40 filas en total),
# cuantos viven en el GRAFO y cuantos en una BANDEJA. La fila la escribe el propio
# barrido con su sede entre corchetes. Y cuantas medidas pasan del umbral en total.
cat .v48aud/03_barrido_c0.out .v48aud/03_barrido_c1.out .v48aud/03_barrido_c2.out \
    .v48aud/03_barrido_c3.out .v48aud/03_barrido_c4.out > .v48aud/03_barrido.out
echo "filas de vecino publicadas en total : $(grep -c '^    0\.' .v48aud/03_barrido.out)"
echo "de ellas en [grafo]                 : $(grep -c '^    0\..*\[grafo' .v48aud/03_barrido.out)"
echo "de ellas en [bandeja/...]           : $(grep -c '^    0\..*\[bandeja' .v48aud/03_barrido.out)"
grep -h 'por encima del umbral' .v48aud/03_barrido.out | sed 's/.*: //' \
  | awk '{s+=$1} END {print "medidas por encima del umbral 0.35  : " s}'
