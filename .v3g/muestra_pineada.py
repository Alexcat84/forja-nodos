# -*- coding: utf-8 -*-
"""Muestra pineada de los SANO de las dos tandas que audito (AUDITOR_FORJA 7).
La semilla se escribe en el acta; la eleccion NO se hace a ojo."""
import random, sys
sys.stdout.reconfigure(encoding='utf-8')

# Los SANO publicados por cada tanda, leidos de docs/loop/REPORTE.md (Z.2.c y AA.2.e).
SANO_V1 = [
 ("construir_flujo_produccion_paso_limitante","retirar_barreras_politicas_metodo"),
 ("rehacer_flujo_paso_limitante_capacidad","construir_flujo_produccion_paso_limitante"),
 ("construir_flujo_produccion_paso_limitante","rehacer_flujo_paso_limitante_capacidad"),
 ("preferir_inspeccion_proceso_prueba_destructiva","clasificar_trabajo_proceso_montaje_prueba"),
 ("preferir_inspeccion_proceso_prueba_destructiva","equilibrar_capacidad_personal_inventario_plazo"),
 ("dimensionar_inventario_materia_prima_reposicion","preferir_inspeccion_proceso_prueba_destructiva"),
 ("dimensionar_inventario_materia_prima_reposicion","equilibrar_capacidad_personal_inventario_plazo"),
 ("detectar_arreglar_fallo_etapa_menor_valor","construir_flujo_produccion_paso_limitante"),
 ("detectar_arreglar_fallo_etapa_menor_valor","rehacer_flujo_paso_limitante_capacidad"),
]
SANO_V2 = [
 ("emparejar_indicadores_efecto_contraefecto","revisar_tres_preguntas_valor_carrera"),
 ("elegir_indicador_salida_trabajo_administrativo","evaluar_directivo_resultados_fortaleza"),
 ("construir_indicador_tendencia_patron","construir_grafico_escalonado_pronosticos"),
 ("construir_indicador_tendencia_patron","archivar_indicadores_resolver_problemas"),
 ("construir_indicador_tendencia_patron","equilibrar_capacidad_personal_inventario_plazo"),
 ("construir_grafico_escalonado_pronosticos","elegir_fabricar_pedido_pronostico"),
 ("construir_grafico_escalonado_pronosticos","emparejar_indicadores_efecto_contraefecto"),
 ("archivar_indicadores_resolver_problemas","revisar_tres_preguntas_valor_carrera"),
]
SEMILLA = "ACTA32-grove-17sep2026"
def tomar(nombre, pobl):
    cuantos = max(3, round(0.20*len(pobl)))
    cuantos = min(cuantos, 20, len(pobl))
    r = random.Random(SEMILLA + "|" + nombre)
    elegidos = r.sample(range(len(pobl)), cuantos)
    print("%s : SANO publicados %d | 20 por ciento %.1f | mayor entre 3 y eso %d | techo 20 -> RELEO %d"
          % (nombre, len(pobl), 0.20*len(pobl), max(3, round(0.20*len(pobl))), cuantos))
    for i in sorted(elegidos):
        print("   par %2d  %s  con  %s" % (i+1, pobl[i][0], pobl[i][1]))
    print()
print("SEMILLA ESCRITA EN EL ACTA: %s" % SEMILLA)
print()
tomar("VUELTA 1 (cap_01 y cap_02)", SANO_V1)
tomar("VUELTA 2 (cap_03)", SANO_V2)
