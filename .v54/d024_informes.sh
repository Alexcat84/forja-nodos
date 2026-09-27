set -u
cd "$(git rev-parse --show-toplevel)"
for n in clasificar_trabajo_proceso_montaje_prueba \
         construir_flujo_produccion_paso_limitante \
         detectar_arreglar_fallo_etapa_menor_valor \
         dimensionar_inventario_materia_prima_reposicion \
         equilibrar_capacidad_personal_inventario_plazo \
         preferir_inspeccion_proceso_prueba_destructiva \
         rehacer_flujo_paso_limitante_capacidad ; do
  ini=$(date +%s)
  {
    echo "\$ python forja.py informe cuarentena/grove_high_output/$n.json"
    python forja.py informe "cuarentena/grove_high_output/$n.json" 2>&1
  } > ".v54/d024_$n.txt"
  fin=$(date +%s)
  echo "$n $((fin-ini))" >> .v54/d024_reloj.txt
done
echo FIN >> .v54/d024_reloj.txt
