# -*- coding: utf-8 -*-
"""Cruza, para las dos vueltas que audito, los pares que la ADUANA levanto con
las aristas que la MISMA vuelta declaro por lectura. Las dos listas se teclean
de docs/loop/REPORTE.md (Z.2.c, Z.4, AA.2.e, AA.4, AA.5.c) y el cruce lo hace
el instrumento, que es la parte que no se puede hacer a ojo."""
import sys
sys.stdout.reconfigure(encoding='utf-8')

# (candidato, vecino, veredicto publicado)
PARES = {
 "VUELTA 1": [
  ("construir_flujo_produccion_paso_limitante","retirar_barreras_politicas_metodo","SANO"),
  ("rehacer_flujo_paso_limitante_capacidad","construir_flujo_produccion_paso_limitante","SANO"),
  ("construir_flujo_produccion_paso_limitante","rehacer_flujo_paso_limitante_capacidad","SANO"),
  ("preferir_inspeccion_proceso_prueba_destructiva","clasificar_trabajo_proceso_montaje_prueba","SANO"),
  ("preferir_inspeccion_proceso_prueba_destructiva","equilibrar_capacidad_personal_inventario_plazo","SANO"),
  ("dimensionar_inventario_materia_prima_reposicion","preferir_inspeccion_proceso_prueba_destructiva","SANO"),
  ("dimensionar_inventario_materia_prima_reposicion","equilibrar_capacidad_personal_inventario_plazo","SANO"),
  ("detectar_arreglar_fallo_etapa_menor_valor","construir_flujo_produccion_paso_limitante","SANO"),
  ("detectar_arreglar_fallo_etapa_menor_valor","rehacer_flujo_paso_limitante_capacidad","SANO"),
 ],
 "VUELTA 2": [
  ("emparejar_indicadores_efecto_contraefecto","revisar_tres_preguntas_valor_carrera","SANO"),
  ("elegir_indicador_salida_trabajo_administrativo","evaluar_directivo_resultados_fortaleza","SANO"),
  ("elegir_indicador_salida_trabajo_administrativo","emparejar_indicadores_efecto_contraefecto","CONTINUA"),
  ("construir_indicador_tendencia_patron","construir_grafico_escalonado_pronosticos","SANO"),
  ("construir_indicador_tendencia_patron","archivar_indicadores_resolver_problemas","SANO"),
  ("construir_indicador_tendencia_patron","equilibrar_capacidad_personal_inventario_plazo","SANO"),
  ("construir_grafico_escalonado_pronosticos","elegir_fabricar_pedido_pronostico","SANO"),
  ("construir_grafico_escalonado_pronosticos","emparejar_indicadores_efecto_contraefecto","SANO"),
  ("archivar_indicadores_resolver_problemas","revisar_tres_preguntas_valor_carrera","SANO"),
 ],
}
# (madre, hijo, donde se declaro)
ARISTAS = {
 "VUELTA 1": [
  ("construir_flujo_produccion_paso_limitante","rehacer_flujo_paso_limitante_capacidad","Z.4 1"),
  ("clasificar_trabajo_proceso_montaje_prueba","preferir_inspeccion_proceso_prueba_destructiva","Z.4 2"),
  ("detectar_arreglar_fallo_etapa_menor_valor","clasificar_trabajo_proceso_montaje_prueba","Z.4 3"),
  ("detectar_arreglar_fallo_etapa_menor_valor","dimensionar_inventario_materia_prima_reposicion","Z.4 4"),
 ],
 "VUELTA 2": [
  ("dimensionar_inventario_materia_prima_reposicion","decidir_aceptar_rechazar_material_defectuoso","AA.4 1"),
  ("casar_flujo_fabricacion_flujo_ventas","detectar_arreglar_fallo_etapa_menor_valor","AA.4 2"),
  ("dimensionar_plantilla_administrativa_pronostico","elegir_indicador_salida_trabajo_administrativo","AA.4 3"),
  ("representar_actividad_caja_negra_ventanas","construir_indicador_linealidad_alerta_temprana","AA.4 4"),
  ("representar_actividad_caja_negra_ventanas","construir_indicador_tendencia_patron","AA.4 5"),
  ("elegir_fabricar_pedido_pronostico","casar_flujo_fabricacion_flujo_ventas","AA.4 6"),
  ("elegir_indicador_salida_trabajo_administrativo","emparejar_indicadores_efecto_contraefecto","AA.5.c 7"),
  ("casar_flujo_fabricacion_flujo_ventas","construir_grafico_escalonado_pronosticos","AA.5.c 8"),
 ],
}
choca = 0
for vuelta in ("VUELTA 1", "VUELTA 2"):
    pares, aristas = PARES[vuelta], ARISTAS[vuelta]
    ar = {frozenset((m, h)): d for m, h, d in aristas}
    print("%s : %d pares juzgados, %d aristas declaradas por lectura"
          % (vuelta, len(pares), len(aristas)))
    tocados = 0
    for a, b, ver in pares:
        k = frozenset((a, b))
        if k in ar:
            tocados += 1
            marca = "COHERENTE" if ver == "CONTINUA" else "NO COHERENTE"
            choca += (ver != "CONTINUA")
            print("   par juzgado %-9s Y con arista declarada en %-9s -> %s"
                  % (ver, ar[k], marca))
            print("        %s  con  %s" % (a, b))
    print("   pares que son ADEMAS arista declarada : %d" % tocados)
    print("   aristas que NINGUNA senal levanto (D.29 puro) : %d" % (len(aristas) - tocados))
    print()
print("PARES JUZGADOS SANO QUE LA MISMA VUELTA DECLARA MADRE E HIJO : %d" % choca)
print("EN LA SEDE (bitacora/VEREDICTOS.jsonl) ESE CASO EXISTE        : 0 de 396")
