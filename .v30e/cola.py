import json, io, os, glob

vivos = {}
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    n = json.loads(l)
    vivos[n['id']] = n
bandeja = set(os.path.basename(p)[:-5]
              for p in glob.glob('cuarentena/*/*.json') if '_insertados' not in p)

def sede(i):
    if i in vivos:
        return 'GRAFO'
    if i in bandeja:
        return 'bandeja'
    return 'NO EXISTE'

def arista(madre, hijo):
    n = vivos.get(madre)
    if n is None:
        return 'la madre no vive'
    return 'CABLEADA' if hijo in n['nodos_siguientes'] else 'sin cablear'

print('| fila de la cola del encargo | lo que mido hoy | estado |')
print('|---|---|---|')
print('| arista `crear_espacio_seguro_madurar_ideas_nuevas > nutrir_ideas_nuevas_reunion_solas` '
      '| madre %s, hijo %s, arista %s | SIGUE ABIERTA |'
      % (sede('crear_espacio_seguro_madurar_ideas_nuevas'),
         sede('nutrir_ideas_nuevas_reunion_solas'),
         arista('crear_espacio_seguro_madurar_ideas_nuevas',
                'nutrir_ideas_nuevas_reunion_solas')))
partes = ['proteger_tiempo_equipo_jefe', 'mantener_manos_trabajo_real_equipo',
          'reservar_calendario_tiempo_ejecutar']
print('| serie `D.37` de `minimizar_impuesto_colaboracion_equipo`, 3 partes '
      '| %s | CERRADA HOY |'
      % '; '.join('%s %s' % (p, arista('minimizar_impuesto_colaboracion_equipo', p))
                  for p in partes))
print('| mitad `Burnout` de `aprender_resultados_vencer_dos_presiones` '
      '| cuidarse_agotamiento_centro_rueda %s, arista %s | CERRADA HOY |'
      % (sede('cuidarse_agotamiento_centro_rueda'),
         arista('aprender_resultados_vencer_dos_presiones',
                'cuidarse_agotamiento_centro_rueda')))
print('| arista NUEVA `desplegar_plan_orden_operaciones_franqueza_radical > '
      'bloquear_tiempo_pensar_calendario` | madre %s, hijo %s, arista %s | ABIERTA DESDE HOY |'
      % (sede('desplegar_plan_orden_operaciones_franqueza_radical'),
         sede('bloquear_tiempo_pensar_calendario'),
         arista('desplegar_plan_orden_operaciones_franqueza_radical',
                'bloquear_tiempo_pensar_calendario')))
print('| lote 5 (`marquet_turn_the_ship`), que no se toca hasta que el 4 cierre '
      '| %d candidatos en bandeja | SIGUE ABIERTA |'
      % len(glob.glob('cuarentena/marquet_turn_the_ship/*.json')))
print('| bandeja del lote 4, lo que queda por insertar | %d candidatos '
      '| SIGUE ABIERTA |' % len(glob.glob('cuarentena/scott_radical_candor/*.json')))
