import json,sys
ver=[json.loads(l) for l in open('bitacora/VEREDICTOS.jsonl',encoding='utf-8') if l.strip()]
pares=[("bloquear_tiempo_pensar_calendario","desplegar_plan_orden_operaciones_franqueza_radical"),
("persuadir_emocion_oyente_no_propia","establecer_credibilidad_pericia_humildad"),
("establecer_credibilidad_pericia_humildad","compartir_logica_mostrar_razonamiento"),
("compartir_logica_mostrar_razonamiento","establecer_credibilidad_pericia_humildad"),
("bloquear_tiempo_pensar_calendario","calibrar_ascensos_evitar_politica"),
("fijar_fecha_cierre_debate_equipo","explicar_idea_facil_comprender_oyente"),
("bloquear_tiempo_pensar_calendario","cuidarse_agotamiento_centro_rueda"),
("cuidarse_agotamiento_centro_rueda","bloquear_tiempo_pensar_calendario"),
]
for a,b in pares:
    hit=[(i+1,v) for i,v in enumerate(ver) if {v['candidato'],v['vecino']}=={a,b}]
    print("#"*100)
    print(a,"  <->  ",b)
    if not hit: print("   NO HAY LINEA EN LA BITACORA"); print(); continue
    for n,v in hit:
        print(f"  linea {n} | {v['veredicto']} | candidato={v['candidato']} vecino={v['vecino']}")
        print("  senales:",json.dumps(v.get('senales'),ensure_ascii=False))
        print("  levantada_por:",v.get('levantada_por'),"| arista:",v.get('arista'),"| detalle:",v.get('detalle_paso'))
        print("  RAZON:",v.get('razon'))
    print()
