#!/bin/bash
cd "$(dirname "$0")/.."
for n in examinar_entorno_expectativas_tecnologia_proveedores_grupos:p9 \
         examinar_demanda_entorno_dos_marcos_temporales:p10 \
         determinar_estado_presente_capacidades_proyectos_merma:p12 \
         cerrar_brecha_dos_preguntas_estrategia:p14 \
         fijar_horizonte_ventana_replanificacion:p22 ; do
  id="${n%%:*}"; tag="${n##*:}"
  { echo "INICIO $(date -Is)"
    time python forja.py informe "cuarentena/grove_high_output/$id.json"
    echo "FIN $(date -Is)"
  } > ".v55ext/aduana_$tag.txt" 2>&1
done
echo "CADENA COMPLETA $(date -Is)"
