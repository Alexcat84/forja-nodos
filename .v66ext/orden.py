# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 66 de .v64ext/orden.py (TAREA 3.5), con las rutas cambiadas a los 22 de cap_04. La tabla del
orden propuesto, impresa y no tecleada. Lo unico escrito a mano es ORDEN (la propuesta); todo lo demas se lee de ficheros:
  madres    : .v66ext/veredictos_listos.txt (CONTINUA madre=) y .v66ext/aristas_lectura.txt (SOSTENGO)
  informe   : el barrido de hoy, .v66ext/vecinos_<id>.json, con su poblacion (en la 64 era el informe de la 63)
  vecinos   : los que la senial levanta HOY en el sentido del candidato, dentro y fuera de los 22
  listos    : cada vecino levantado tiene su linea en veredictos_listos.txt
Lo que cambia ademas de las rutas, y se dice: una madre que ya esta en el grafo no ordena nada (ya entro), asi que
las comprobaciones solo miran madres que estan entre los 22; la columna madre(s) las imprime todas.
Y comprueba las dos reglas del orden: madre antes que hijo, y D.36 (si un par levanta en un solo sentido, el que lo
levanta entra despues)."""
import io, json, collections
ORDEN = [
    'reunir_informacion_gerencial_vias_variadas', 'escalonar_fuentes_informacion_gerencial',
    'programar_visita_area_observar_despachar', 'transmitir_objetivos_prioridades_preferencias',
    'empujar_persona_reunion_direccion_preferida', 'subir_productividad_gerencial_tres_vias',
    'buscar_actividad_alta_palanca_tres_vias', 'elegir_momento_actividad_palanca_maxima',
    'detectar_palanca_negativa_actividad_mando', 'delegar_tarea_base_comun_seguimiento',
    'supervisar_tarea_delegada_etapa_menor_valor', 'supervisar_decision_delegada_preguntas_concretas',
    'identificar_paso_limitante_jornada_desfases', 'agrupar_tareas_semejantes_aprovechar_preparacion',
    'decir_no_trabajo_excede_capacidad', 'usar_calendario_herramienta_planificacion_produccion',
    'dimensionar_numero_subordinados_medio_dia_semanal', 'buscar_regularidad_bloques_iguales_trabajo_mando',
    'preparar_respuestas_estandar_interrupciones_repetidas', 'llevar_inventario_proyectos_discrecionales',
    'agrupar_interrupciones_subordinados_reuniones_regulares', 'canalizar_interrupciones_cartel_hora_oficina']
TOPE = 20
L22 = collections.OrderedDict((l.split()[0], (l.split()[1], l.split()[2]))
                              for l in io.open('.v66ext/los22_cap04.txt', encoding='utf-8') if l.strip() and not l.startswith('#'))
assert sorted(ORDEN) == sorted(L22), 'ORDEN no son los 22'
# madres
madres = collections.defaultdict(set)
sec, act = collections.defaultdict(set), None
for l in io.open('.v66ext/veredictos_listos.txt', encoding='utf-8'):
    l = l.rstrip('\n')
    if l.startswith('## '):
        act = l[3:].strip(); continue
    if not l.strip() or l.startswith('#'):
        continue
    p = l.split('|')
    sec[act].add(p[0])
    if p[1] == 'CONTINUA':
        m = p[2].split('=', 1)[1]
        h = p[0] if m == act else act
        madres[h].add(m)
for l in io.open('.v66ext/aristas_lectura.txt', encoding='utf-8'):
    if l.startswith('SOSTENGO'):
        p = [c.strip() for c in l.split('|')]
        madres[p[2]].add(p[1])
# vecinos levantados hoy, y el informe de cada uno: su barrido
lev, pob = collections.defaultdict(set), {}
for i in L22:
    d = json.load(io.open('.v66ext/vecinos_%s.json' % i, encoding='utf-8'))
    lev[i] = set(v['id'] for v in d['vecinos'])
    pob[i] = d['grafo'] + d['bandejas']
pos = dict((i, k) for k, i in enumerate(ORDEN))
print('%-3s %-56s %-6s %-4s %-50s %-4s %-10s %-4s %-5s %s' % ('#', 'candidato', 'cap', 'pza', 'madre(s)', 'pob', 'dijo', 'vec', 'lin', 'listos'))
for k, i in enumerate(ORDEN, 1):
    cap, pz = L22[i]
    falta = sorted(lev[i] - sec[i])
    print('%-3d %-56s %-6s %-4s %-50s %-4d %-10s %-4d %-5d %s%s' % (
        k, i, cap, pz, ', '.join(sorted(madres[i])) or '-', pob[i], 'BLOQUEARIA' if lev[i] else 'ENTRARIA',
        len(lev[i]), len(sec[i]), 'SI' if not falta else 'FALTAN %s' % falta, '   <- corte del tope' if k == TOPE else ''))
print()
print('COMPROBACIONES')
mal = [(m, h) for h in madres for m in madres[h] if m in pos and h in pos and pos[m] > pos[h]]
print('  hijo delante de su madre: %d %s' % (len(mal), mal))
d36 = [(a, b) for a in L22 for b in lev[a] if b in L22 and a not in lev[b] and pos[a] < pos[b]]
print('  D.36, par que levanta en un solo sentido con el que lo levanta entrando antes: %d %s' % (len(d36), d36))
fuera = [(m, h) for h in ORDEN[:TOPE] for m in madres[h] if m in ORDEN[TOPE:]]
print('  hijo dentro del tope con su madre fuera: %d %s' % (len(fuera), fuera))
print('  tanda propuesta: %d de %d; fuera del tope: %s' % (TOPE, len(ORDEN), ', '.join(ORDEN[TOPE:])))
