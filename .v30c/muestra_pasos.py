import json,random
nodos={}
for l in open('dataset/nodos.jsonl',encoding='utf-8'):
    if l.strip():
        n=json.loads(l); nodos[n['id']]=n
leidos_ciegos=['parar_debate_emocion_agotamiento','pedir_hechos_decision_evitar_recomendaciones',
'minimizar_impuesto_colaboracion_equipo','reservar_calendario_tiempo_ejecutar','proteger_tiempo_equipo_jefe',
'mantener_manos_trabajo_real_equipo','bloquear_tiempo_pensar_calendario','cuidarse_agotamiento_centro_rueda']
tanda=['parar_debate_emocion_agotamiento','fijar_fecha_cierre_debate_equipo','repartir_decision_cercanos_hechos',
'pedir_hechos_decision_evitar_recomendaciones','persuadir_emocion_oyente_no_propia','establecer_credibilidad_pericia_humildad',
'compartir_logica_mostrar_razonamiento','minimizar_impuesto_colaboracion_equipo','proteger_tiempo_equipo_jefe',
'mantener_manos_trabajo_real_equipo','reservar_calendario_tiempo_ejecutar','cuidarse_agotamiento_centro_rueda',
'bloquear_tiempo_pensar_calendario']
tot=0
for i in tanda:
    tot+=len(nodos[i]['pasos_accionables'])
print("pasos de los 13 de la tanda:",tot)
cap07=[i for i in tanda if i!='bloquear_tiempo_pensar_calendario']
print("pasos de los 12 de cap_07:",sum(len(nodos[i]['pasos_accionables']) for i in cap07))
pob=[]
for i in cap07:
    if i in leidos_ciegos: continue
    for k,p in enumerate(nodos[i]['pasos_accionables'],1):
        pob.append((i,k,p))
print("poblacion NO leida en mi fase ciega (cap_07):",len(pob))
SEMILLA=160926
m=random.Random(SEMILLA).sample(pob,16)
print("SEMILLA:",SEMILLA)
print()
for i,(nid,k,p) in enumerate(sorted(m),1):
    print(f"{i:2d}. {nid} paso {k}")
    print(f"      {p}")
