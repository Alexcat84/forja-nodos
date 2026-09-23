#!/bin/bash
# Barrido D.38.4 de la fase ciega de la 64: los seis de d005 tal como estan HOY en la bandeja,
# contra grafo mas bandejas. Uno por candidato, en paralelo, y se espera a todos.
cd /c/Users/AlexDesk/Documents/forja-nodos
echo "INICIO $(date '+%F %T')" > .v64aud/barrido.log
for id in archivar_indicadores_resolver_problemas construir_grafico_escalonado_pronosticos construir_indicador_tendencia_patron elegir_fabricar_pedido_pronostico elegir_indicador_salida_trabajo_administrativo emparejar_indicadores_efecto_contraefecto; do
  (
    t0=$(date +%s)
    python forja.py informe "cuarentena/grove_high_output/$id.json" > ".v64aud/informe_$id.txt" 2>&1
    rc=$?
    t1=$(date +%s)
    echo "$id rc=$rc segundos=$((t1-t0))" >> .v64aud/barrido.log
  ) &
done
wait
echo "TODOS TERMINADOS $(date '+%F %T')" >> .v64aud/barrido.log
