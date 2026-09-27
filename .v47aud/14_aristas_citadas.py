# -*- coding: utf-8 -*-
"""Los nodos que los 6 candidatos NOMBRAN en sus aristas declaradas por lectura:
existen o no, y en que sede. Una arista a un nodo que no existe en ninguna sede
es una ruta que promete prueba (cosecha 7.B)."""
import json, os, sys, io, glob, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sedes = {}
for l in open('dataset/nodos.jsonl', encoding='utf-8'):
    if l.strip():
        sedes[json.loads(l)['id']] = 'grafo'
for d in sorted(os.listdir('cuarentena')):
    p = os.path.join('cuarentena', d)
    if not os.path.isdir(p) or d in ('_insertados', '_derivadas'):
        continue
    for f in sorted(glob.glob(os.path.join(p, '*.json'))):
        i = json.load(open(f, encoding='utf-8')).get('id')
        if i:
            sedes.setdefault(i, 'bandeja/' + d)
CITADOS = {
 'detectar_palanca_negativa_actividad_mando': ['buscar_actividad_alta_palanca_tres_vias'],
 'delegar_tarea_base_comun_seguimiento': ['transmitir_objetivos_prioridades_preferencias',
    'supervisar_tarea_delegada_etapa_menor_valor', 'detectar_palanca_negativa_actividad_mando'],
 'supervisar_tarea_delegada_etapa_menor_valor': ['delegar_tarea_base_comun_seguimiento',
    'supervisar_decision_delegada_preguntas_concretas', 'elegir_inspeccion_barrera_monitorizacion'],
 'supervisar_decision_delegada_preguntas_concretas': ['delegar_tarea_base_comun_seguimiento',
    'supervisar_tarea_delegada_etapa_menor_valor'],
 'identificar_paso_limitante_jornada_desfases': ['subir_productividad_gerencial_tres_vias',
    'agrupar_tareas_semejantes_aprovechar_preparacion',
    'usar_calendario_herramienta_planificacion_produccion',
    'construir_flujo_produccion_paso_limitante'],
 'agrupar_tareas_semejantes_aprovechar_preparacion': ['subir_productividad_gerencial_tres_vias',
    'identificar_paso_limitante_jornada_desfases', 'clasificar_trabajo_proceso_montaje_prueba'],
}
falta = 0
for cand, lista in CITADOS.items():
    print('=== %s' % cand)
    for o in lista:
        s = sedes.get(o)
        if s is None:
            falta += 1
        print('    %-12s %s' % (s or 'NO EXISTE', o))
print('---')
print('aristas declaradas hacia un id que NO existe en ninguna sede: %d' % falta)
