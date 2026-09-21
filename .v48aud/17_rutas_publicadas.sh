#!/bin/sh
# COSECHA 7.B: una ruta publicada como evidencia CUENTA COMO CIFRA PUBLICADA en su sede.
# Si apunta a un fichero inexistente o de CERO BYTES, es caida de cifra. Esta es la
# comprobacion que me cazo dos rutas en la ACTA 46 antes de commitear.
# Se miran FICHEROS: la mencion de la carpeta .v48aud/ a secas no promete ninguna salida.
malas=0
for r in $(grep -o "\.v4[0-9]aud/[A-Za-z0-9_][A-Za-z0-9_.]*" docs/loop/APERTURA_CIEGA.md | sort -u); do
  if [ ! -e "$r" ]; then echo "NO EXISTE     $r"; malas=$((malas+1))
  elif [ ! -s "$r" ]; then echo "CERO BYTES    $r"; malas=$((malas+1))
  else echo "OK  $(wc -c < "$r" | tr -d ' ') bytes   $r"; fi
done
echo "rutas publicadas que no existen o estan en cero bytes: $malas"
