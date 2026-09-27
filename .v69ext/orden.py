# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 69 de .v68ext/orden.py: lee los mismos ficheros de .v68ext/ (las lineas corregidas por la relectura
conjunta de la 69 y el barrido de la 68), su salida va a .v69ext/orden.txt, y ANADE AL FINAL LA CUENTA DE ARISTAS ESPERADAS EN LA
70 (TAREA 2.3 del encargo de la 69): las CONTINUA con madre= de los veredictos, como pares distintos madre a hijo (un par leido
desde sus dos lados es una arista), y las filas SOSTENGO por lectura, como pares madre a hijo. ORDEN no cambia.
La de la 68 era COPIA DE LA VUELTA 68 de .v67ext/orden.py (TAREA 3.5 de la 68), con las rutas cambiadas de .v66ext a .v68ext y la lista
a los 20 de cap_05 y cap_06 (.v68ext/los20_cap05_cap06.txt); ORDEN es la propuesta de la 68. La de la 67 era COPIA DE LA
VUELTA 66 de .v64ext/orden.py con las rutas cambiadas a los 22 de cap_04. La tabla del
orden propuesto, impresa y no tecleada. Lo unico escrito a mano es ORDEN (la propuesta); todo lo demas se lee de ficheros:
  madres    : .v68ext/veredictos_listos.txt (CONTINUA madre=) y .v68ext/aristas_lectura.txt (SOSTENGO)
  informe   : el barrido de hoy, .v68ext/vecinos_<id>.json, con su poblacion (en la 64 era el informe de la 63)
  vecinos   : los que la senial levanta HOY en el sentido del candidato, dentro y fuera de los 22
  listos    : cada vecino levantado tiene su linea en veredictos_listos.txt
Lo que cambia ademas de las rutas, y se dice: una madre que ya esta en el grafo no ordena nada (ya entro), asi que
las comprobaciones solo miran madres que estan entre los 22; la columna madre(s) las imprime todas.
Y comprueba las dos reglas del orden: madre antes que hijo, y D.36 (si un par levanta en un solo sentido, el que lo
levanta entra despues)."""
import io, json, collections
ORDEN = [
    'infundir_regularidad_reunion_proceso',
    'usar_tres_clases_reunion_proceso',
    'fijar_frecuencia_reunion_individual_madurez_tarea',
    'fijar_duracion_lugar_reunion_individual',
    'preparar_guion_reunion_individual_subordinado',
    'cubrir_indicadores_problemas_reunion_individual',
    'facilitar_expresion_subordinado_pregunta_mas',
    'tomar_notas_copia_guion_reunion_individual',
    'acumular_asuntos_importantes_fichero_espera',
    'alentar_asuntos_corazon_vigilar_final_reunion',
    'conducir_reunion_individual_telefono_distancia',
    'programar_reunion_individual_cadena',
    'conducir_etapas_modelo_ideal_decision',
    'ejercer_poder_posicion_etapa_decision_clara',
    'vencer_sindrome_grupo_pares_autoconfianza',
    'tomar_mando_reunion_pares_presidente_ausente',
    'cortar_discusion_libre_momento_justo',
    'zanjar_seis_preguntas_decision_adelantado',
    'anunciar_decision_inesperada_reconvocar_reunion',
    'decidir_nivel_competente_inferior',
]
TOPE = 20
L22 = collections.OrderedDict((l.split()[0], (l.split()[1], l.split()[2]))
                              for l in io.open('.v68ext/los20_cap05_cap06.txt', encoding='utf-8') if l.strip() and not l.startswith('#'))
assert sorted(ORDEN) == sorted(L22), 'ORDEN no son los 20'
# madres
madres = collections.defaultdict(set)
sec, act = collections.defaultdict(set), None
for l in io.open('.v68ext/veredictos_listos.txt', encoding='utf-8'):
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
for l in io.open('.v68ext/aristas_lectura.txt', encoding='utf-8'):
    if l.startswith('SOSTENGO'):
        p = [c.strip() for c in l.split('|')]
        madres[p[2]].add(p[1])
# vecinos levantados hoy, y el informe de cada uno: su barrido
lev, pob = collections.defaultdict(set), {}
for i in L22:
    d = json.load(io.open('.v68ext/vecinos_%s.json' % i, encoding='utf-8'))
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

print()
print('ARISTAS ESPERADAS EN LA 70')
cont = set()
act = None
for l in io.open('.v68ext/veredictos_listos.txt', encoding='utf-8'):
    l = l.rstrip(chr(10))
    if l.startswith('## '):
        act = l[3:].strip(); continue
    if not l.strip() or l.startswith('#'):
        continue
    p = l.split('|')
    if p[1] == 'CONTINUA':
        m = p[2].split('=', 1)[1]
        cont.add((m, p[0] if m == act else act))
lec = []
for l in io.open('.v68ext/aristas_lectura.txt', encoding='utf-8'):
    if l.startswith('SOSTENGO'):
        p = [c.strip() for c in l.split('|')]
        lec.append((p[1], p[2]))
for m, h in sorted(cont):
    print('  CONTINUA   %-56s > %s' % (m, h))
for m, h in lec:
    print('  LECTURA    %-56s > %s' % (m, h))
print('  CONTINUA con madre= (aristas distintas): %d | SOSTENGO por lectura: %d | solapes entre las dos: %d | aristas esperadas en la 70: %d' % (
    len(cont), len(lec), len(cont & set(lec)), len(cont | set(lec))))
