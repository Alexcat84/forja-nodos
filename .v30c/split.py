import json, collections
ver=[json.loads(l) for l in open('bitacora/VEREDICTOS.jsonl',encoding='utf-8') if l.strip()]
nuevas=ver[289:]
lect=[v for v in nuevas if v.get('levantada_por')==['lectura declarada']]
print("lineas 'lectura declarada':",len(lect))
for v in lect:
    print("   candidato",v['candidato'],"| vecino",v['vecino'],"| arista",v.get('arista'))
aduana=[v for v in nuevas if v.get('levantada_por')!=['lectura declarada']]
print()
print("lineas de la aduana:",len(aduana))
orden=['parar_debate_emocion_agotamiento','fijar_fecha_cierre_debate_equipo','repartir_decision_cercanos_hechos',
'pedir_hechos_decision_evitar_recomendaciones','persuadir_emocion_oyente_no_propia','establecer_credibilidad_pericia_humildad',
'compartir_logica_mostrar_razonamiento','minimizar_impuesto_colaboracion_equipo','proteger_tiempo_equipo_jefe',
'mantener_manos_trabajo_real_equipo','reservar_calendario_tiempo_ejecutar','cuidarse_agotamiento_centro_rueda']
c=collections.Counter(v['candidato'] for v in aduana)
vals=[c[k] for k in orden]
print("los 12 de cap_07 en orden del libro:",vals)
print("SUMA de los 12:",sum(vals))
print("bloquear_tiempo_pensar_calendario (aduana):",c['bloquear_tiempo_pensar_calendario'])
print("TOTAL aduana:",sum(c.values()))
