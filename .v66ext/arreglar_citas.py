# -*- coding: utf-8 -*-
"""Vuelta 66: cambia el arranque de la cita de las filas de .v66ext/fidelidad.tsv cuyo arranque no es literal
del libro (apostrofos curvos, comillas y guiones largos del original). El resto de la nota queda igual."""
import io
NUEVO = {
 ('programar_visita_area_observar_despachar', 1): 'visit a particular place in the company and observe what ... going on there',
 ('subir_productividad_gerencial_tres_vias', 1): 'the output of a manager per unit of time worked',
 ('subir_productividad_gerencial_tres_vias', 4): 'from those with lower to those with higher leverage',
 ('buscar_actividad_alta_palanca_tres_vias', 3): 'activity or behavior over a long period of time is affected by a manager ... brief, well-focused set of words or actions',
 ('buscar_actividad_alta_palanca_tres_vias', 4): 'work is affected by an individual supplying a unique, key piece of knowledge or information',
 ('delegar_tarea_base_comun_seguimiento', 4): 'really want to delegate simply because we like doing them',
 ('supervisar_tarea_delegada_etapa_menor_valor', 7): 'work improves over time, you should respond with a corresponding reduction in the intensity of the monitoring',
 ('supervisar_decision_delegada_preguntas_concretas', 5): 'If he answers them convincingly ... approve what he wants',
 ('identificar_paso_limitante_jornada_desfases', 2): 'First, we must identify our limiting step: what is the ... egg ... in our work',
 ('decir_no_trabajo_excede_capacidad', 1): 'allow material to begin its journey through the factory if they think it is already operating at capacity',
 ('decir_no_trabajo_excede_capacidad', 3): 'at the outset and keep the start level from overloading the system',
 ('decir_no_trabajo_excede_capacidad', 8): 'earlier rather than later because we ... losing more money and time',
 ('decir_no_trabajo_excede_capacidad', 9): 'either explicitly or implicitly, because by not delivering',
 ('decir_no_trabajo_excede_capacidad', 10): 'your time is your one finite resource ... inevitably saying',
 ('usar_calendario_herramienta_planificacion_produccion', 4): 'It is something very simple: his calendar',
 ('usar_calendario_herramienta_planificacion_produccion', 5): 'Most people use their calendars as a repository of ... mindless passivity',
 ('usar_calendario_herramienta_planificacion_produccion', 6): 'planning tool, taking a firm initiative to schedule work that is not time-critical between those ... limiting steps',
 ('llevar_inventario_proyectos_discrecionales', 3): 'need to finish right away',
 ('dimensionar_numero_subordinados_medio_dia_semanal', 9): 'as one of the two subordinates, choosing to be his own engineering manager',
 ('buscar_regularidad_bloques_iguales_trabajo_mando', 6): 'a time bomb on your hands means you can address a problem when you want to',
 ('preparar_respuestas_estandar_interrupciones_repetidas', 2): 'if you can pin down what kind of interruptions',
 ('preparar_respuestas_estandar_interrupciones_repetidas', 4): 'come up with totally new questions and problems day in and day out',
 ('agrupar_interrupciones_subordinados_reuniones_regulares', 1): 'handling a group of similar chores at one time',
 ('agrupar_interrupciones_subordinados_reuniones_regulares', 5): 'protest too much if they ... batch questions and problems for scheduled times',
}
ruta = '.v66ext/fidelidad.tsv'
out = []
for l in io.open(ruta, encoding='utf-8').read().split('\n'):
    if l and not l.startswith('#'):
        c = l.split(' | ')
        k = (c[0], int(c[1]))
        if k in NUEVO:
            c[4] = NUEVO.pop(k)
            l = ' | '.join(c)
    out.append(l)
io.open(ruta, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
print('sin aplicar:', NUEVO)
