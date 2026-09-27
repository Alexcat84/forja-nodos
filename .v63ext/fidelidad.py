# -*- coding: utf-8 -*-
"""La relectura de fidelidad ENTERA de la vuelta 63 (D.30, D.58), tabulada.

Los PASOS se cuentan del fichero; las marcas son la lectura del extractor de la
vuelta 63, paso a paso contra el tramo que cada ficha declara en su UNIDAD DE
ORIGEN, con el capitulo entero delante (cap_02 L15 a L79, cap_03 L13 a L173).
"""
import json
ORDEN = [
    # cap, pieza, id, tramo, pasos PUENTE enteros, pasos con verbo puente reescrito, entregable corregido
    ("cap_02", "P2", "construir_flujo_produccion_paso_limitante", "L19-L27", 0, 0, "no"),
    ("cap_02", "P11", "detectar_arreglar_fallo_etapa_menor_valor", "L73-L75", 0, 0, "no"),
    ("cap_02", "P5", "clasificar_trabajo_proceso_montaje_prueba", "L39-L45", 0, 0, "no"),
    ("cap_02", "P6", "rehacer_flujo_paso_limitante_capacidad", "L51-L55", 0, 0, "no"),
    ("cap_02", "P7", "equilibrar_capacidad_personal_inventario_plazo", "L57-L61", 0, 4, "si"),
    ("cap_02", "P9", "preferir_inspeccion_proceso_prueba_destructiva", "L67", 0, 0, "no"),
    ("cap_02", "P10", "dimensionar_inventario_materia_prima_reposicion", "L69", 0, 0, "no"),
    ("cap_03", "P2", "elegir_cinco_indicadores_diarios_fabrica", "L15-L29", 0, 0, "si"),
    ("cap_03", "P7", "representar_actividad_caja_negra_ventanas", "L73-L79", 0, 0, "no"),
    ("cap_03", "P9", "construir_indicador_linealidad_alerta_temprana", "L83-L87", 0, 0, "no"),
    ("cap_03", "P14", "casar_flujo_fabricacion_flujo_ventas", "L111-L121", 0, 0, "no"),
    ("cap_03", "P15", "dimensionar_plantilla_administrativa_pronostico", "L123-L125", 0, 0, "si"),
    ("cap_03", "P17", "decidir_aceptar_rechazar_material_defectuoso", "L135-L137", 0, 0, "si"),
    ("cap_03", "P18", "elegir_inspeccion_barrera_monitorizacion", "L139-L141", 0, 0, "si"),
    ("cap_03", "P19", "variar_frecuencia_inspeccion_nivel_calidad", "L143", 0, 0, "no"),
    ("cap_03", "P23", "simplificar_trabajo_reducir_numero_pasos", "L169-L171", 0, 0, "si"),
]
print("RELECTURA DE FIDELIDAD ENTERA, VUELTA 63, EN EL ORDEN DE INSERCION")
print("%-3s %-6s %-5s %-50s %-10s %5s %6s %6s %6s %s" % ("#", "cap", "pieza", "candidato", "tramo", "pasos", "TRANSC", "PUENTE", "verbo", "entregable"))
tot = {}
for n, (cap, pieza, i, tramo, puente, verbo, ent) in enumerate(ORDEN, 1):
    pasos = len(json.load(open("cuarentena/grove_high_output/%s.json" % i, encoding="utf-8"))["pasos_accionables"])
    t = tot.setdefault(cap, [0, 0, 0, 0, 0])
    t[0] += 1; t[1] += pasos; t[2] += puente; t[3] += verbo; t[4] += (ent == "si")
    print("%-3d %-6s %-5s %-50s %-10s %5d %6d %6d %6d %s" % (n, cap, pieza, i, tramo, pasos, pasos - puente, puente, verbo, ent))
print()
print("PASOS INVENTADOS POR CAPITULO, sobre la lectura ENTERA")
print("%-8s %10s %6s %7s %13s %14s %s" % ("cap", "candidatos", "pasos", "PUENTE", "verbo_puente", "entregables", "inventado"))
for cap in sorted(tot):
    c, p, pu, v, e = tot[cap]
    print("%-8s %10d %6d %7d %13d %14d %s" % (cap, c, p, pu, v, e, ("%.1f" % (100.0 * pu / p)).replace(".", ",") + " por ciento"))
