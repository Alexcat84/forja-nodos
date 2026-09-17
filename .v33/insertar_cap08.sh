#!/bin/sh
# EL TRAMO DE cap_08 EN EL ORDEN DEL LIBRO, UNO POR VEZ Y PARANDO EN EL PRIMERO QUE NO ENTRE.
# No es carga masiva: cada `insertar` termina entero antes de que arranque el siguiente
# (el cerrojo de `D.44` lo impone por su cuenta), y el guion SE DETIENE en cuanto uno
# bloquea o cae, para que el veredicto se escriba LEYENDO A LOS VECINOS y no en lote.
for id in "$@"; do
  echo "### $id"
  python forja.py insertar "cuarentena/scott_radical_candor/$id.json" \
      --censo serie=no --censo caso=no --censo marco_pais=no \
      --censo vigencia=no --censo herramienta=no > ".v33/ins_$id.txt" 2>&1
  codigo=$?
  if [ "$codigo" -ne 0 ]; then
    echo "PARADA EN $id, codigo $codigo"
    cat ".v33/ins_$id.txt"
    exit 0
  fi
  tail -4 ".v33/ins_$id.txt"
done
echo "TRAMO COMPLETO"
