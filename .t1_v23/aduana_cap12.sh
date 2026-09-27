#!/bin/sh
cd /c/Users/AlexDesk/Documents/forja-nodos
for id in desplegar_plan_orden_operaciones_franqueza_radical \
          contar_historias_propias_explicar_franqueza_radical ; do
  python forja.py informe "cuarentena/scott_radical_candor/$id.json" > ".aduana_v23/$id.txt" 2>&1
  echo "HECHO $id"
done
echo "ADUANA DE cap_12 TERMINADA"
