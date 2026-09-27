#!/bin/sh
# BARRIDO DE VECINOS (D.38.4) de los 7 candidatos de cap_02 que d024 dejo sin informe
# por candidato. Mismo instrumento que el 07: src.aduana.senal_similitud_texto sobre
# grafo mas bandejas. Cuatro procesos a la vez.
for f in construir_flujo_produccion_paso_limitante clasificar_trabajo_proceso_montaje_prueba rehacer_flujo_paso_limitante_capacidad equilibrar_capacidad_personal_inventario_plazo; do
  python .v49aud/07_barrido.py $f > .v49aud/16_barrido_$f.out 2>&1 &
done
wait
for f in preferir_inspeccion_proceso_prueba_destructiva dimensionar_inventario_materia_prima_reposicion detectar_arreglar_fallo_etapa_menor_valor; do
  python .v49aud/07_barrido.py $f > .v49aud/16_barrido_$f.out 2>&1 &
done
wait
echo LISTO
