#!/bin/bash
cd "$(dirname "$0")/.."
for n in contestar_dos_preguntas_direccion_objetivos:p27 \
         fijar_periodo_direccion_objetivos_retroalimentacion:p29 \
         repartir_supervision_puesto_funcional_mision:c10p17 ; do
  id="${n%%:*}"; tag="${n##*:}"
  { echo "INICIO $(date -Is)"
    time python forja.py informe "cuarentena/grove_high_output/$id.json"
    echo "FIN $(date -Is)"
  } > ".v55ext/aduana_$tag.txt" 2>&1
done
echo "CADENA 2 COMPLETA $(date -Is)"
