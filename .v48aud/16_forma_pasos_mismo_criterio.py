# -*- coding: utf-8 -*-
"""EL MISMO CRITERIO DE .v47aud/43_forma_pasos.py, LETRA POR LETRA (primera palabra
en 'cuenta' o 'en'), aplicado ahora tambien a la tanda de la vuelta 48. Se corre asi
para que las tres cifras sean comparables: cambiar el criterio y comparar seria trampa."""
import json, io, sys, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
T48 = [l.strip().split('/')[-1][:-5] for l in open('.v48aud/02_candidatos_nuevos.out', encoding='utf-8') if l.strip()]
T47 = ["detectar_palanca_negativa_actividad_mando", "delegar_tarea_base_comun_seguimiento",
       "supervisar_tarea_delegada_etapa_menor_valor", "supervisar_decision_delegada_preguntas_concretas",
       "identificar_paso_limitante_jornada_desfases", "agrupar_tareas_semejantes_aprovechar_preparacion"]
T46 = ["reunir_informacion_gerencial_vias_variadas", "escalonar_fuentes_informacion_gerencial",
       "programar_visita_area_observar_despachar", "transmitir_objetivos_prioridades_preferencias",
       "empujar_persona_reunion_direccion_preferida", "subir_productividad_gerencial_tres_vias",
       "buscar_actividad_alta_palanca_tres_vias", "elegir_momento_actividad_palanca_maxima"]
def mide(tanda, nombre):
    c = collections.Counter(); cuenta = []
    for i in tanda:
        d = json.load(open("cuarentena/grove_high_output/%s.json" % i, encoding="utf-8"))
        for n, p in enumerate(d["pasos_accionables"], 1):
            w = p.split()[0].strip(",:.")
            c[w] += 1
            if w.lower() in ("cuenta", "en"): cuenta.append("%s#%d" % (i[:34], n))
    tot = sum(c.values())
    print("== %s : %d pasos" % (nombre, tot))
    for w, n in c.most_common():
        print("   %-12s %3d   (%.1f por ciento)" % (w, n, 100.0*n/tot))
    print("   pasos que ABREN declarando y no ejecutando: %d de %d = %.1f por ciento"
          % (len(cuenta), tot, 100.0*len(cuenta)/tot))
    for x in cuenta: print("      %s" % x)
    print()
mide(T48, "tanda de la vuelta 48")
mide(T47, "tanda de la vuelta 47")
mide(T46, "tanda de la vuelta 46")
