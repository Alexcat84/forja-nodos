#!/bin/sh
# CADA CANDIDATO CORREGIDO VUELVE A PASAR POR LA ADUANA (EXTRACTOR.md 16).
cd /c/Users/AlexDesk/Documents/forja-nodos
for id in debatir_decidir_asuntos_cultura_evitar_delegar \
          leer_seniales_fallo_jefe_reunion_solas \
          montar_reuniones_solas_mentalidad_frecuencia \
          pelear_proliferacion_reuniones_bloquear_ejecucion \
          preguntar_seguimiento_hallar_huecos ; do
  python forja.py informe "cuarentena/scott_radical_candor/$id.json" > ".aduana_v23/$id.txt" 2>&1
  echo "HECHO $id"
done
echo "ADUANA DE LAS CORRECCIONES TERMINADA"
