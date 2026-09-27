# ACTA 77 (copia de .v77aud/normal/correr.sh): corre cada comando que recibe (uno por linea en stdin) con bash -c, imprimiendo antes "$ " y el comando tal cual,
# para que la linea $ pegada sea exactamente la que se ejecuto. Solo lee.
while IFS= read -r c; do echo "\$ $c"; bash -c "$c" 2>&1; done
