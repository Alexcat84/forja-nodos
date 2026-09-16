import json, io
IDS = ['minimizar_impuesto_colaboracion_equipo', 'proteger_tiempo_equipo_jefe',
       'mantener_manos_trabajo_real_equipo', 'reservar_calendario_tiempo_ejecutar',
       'aprender_resultados_vencer_dos_presiones', 'cuidarse_agotamiento_centro_rueda',
       'cambiar_posicion_hechos_explicar_cambio']
d = {}
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    n = json.loads(l)
    if n['id'] in IDS:
        d[n['id']] = n
print('| nodo | previos | siguientes |')
print('|---|---|---|')
for i in IDS:
    n = d[i]
    print('| `%s` | %s | %s |'
          % (i,
             ', '.join('`%s`' % x for x in n['nodos_previos']) or 'ninguno',
             ', '.join('`%s`' % x for x in n['nodos_siguientes']) or 'ninguno'))
