# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 77 de .v76ext/orden.py (encargo de la 77, TAREA 2). Lo cambiado, y nada mas: las dos sedes que la TAREA 2 copio,
.v77ext/veredictos_listos.txt y .v77ext/aristas_lectura.txt, y el rotulo de las aristas esperadas; la lista, el barrido y ORDEN siguen
leyendose de .v76ext/. Lo que decia la de la 76: COPIA DE LA VUELTA 76 de .v73ext/orden.py (TAREA 4.3 del encargo de la 76). Lo cambiado, y nada mas: las rutas de .v73ext a
.v76ext; la lista, que es .v76ext/lista_barrido.txt (capitulo, id, la palabra pasos y su cuenta; el id en la segunda columna, como
en la 73); la bandeja de la que se lee la PIEZA, que es cuarentena/gerber_emyth/; ORDEN, que es la propuesta de la 76; TOPE, que es
22; el patron de la PIEZA, que en Gerber es una letra y un numero (P1, R3, C1, D2) y no solo P; y el rotulo de las aristas esperadas, que es de la vuelta que inserte estas 22. Lo que decia la de la 73: COPIA DE LA VUELTA 73 de .v71ext/orden.py (TAREA 4.3 del encargo de la 73). Lo cambiado, y nada mas: las rutas de .v71ext a
.v73ext; la lista, que es .v73ext/las7.txt (capitulo, id, pasos, como en la 71); ORDEN, que es la propuesta de la 73; TOPE, que es 7;
y el rotulo de las aristas esperadas, que es de la vuelta que inserte estas 7. Lo que decia la de la 71: COPIA DE LA VUELTA 71 de .v69ext/orden.py (TAREA 4.4 del encargo de la 71). Lo cambiado, y nada mas: las rutas de .v68ext a
.v71ext; la lista, que es .v71ext/los20.txt con el id en su SEGUNDA columna (capitulo, id, pasos), y la columna pza, que se lee de
la PIEZA que cada ficha declara en su resumen_teorico porque los20.txt no la trae; ORDEN, que es la propuesta de la 71; los
anchos; y el rotulo de las aristas esperadas, que es de la vuelta que inserte estas 20 y no de la 70.
Lo que decia la de la 69: COPIA DE LA VUELTA 69 de .v71ext/orden.py: lee los mismos ficheros de .v71ext/ (las lineas corregidas por la relectura
conjunta de la 69 y el barrido de la 68), su salida va a .v69ext/orden.txt, y ANADE AL FINAL LA CUENTA DE ARISTAS ESPERADAS EN LA
70 (TAREA 2.3 del encargo de la 69): las CONTINUA con madre= de los veredictos, como pares distintos madre a hijo (un par leido
desde sus dos lados es una arista), y las filas SOSTENGO por lectura, como pares madre a hijo. ORDEN no cambia.
La de la 68 era COPIA DE LA VUELTA 68 de .v67ext/orden.py (TAREA 3.5 de la 68), con las rutas cambiadas de .v66ext a .v68ext y la lista
a los 20 de cap_05 y cap_06 (.v71ext/los20_cap05_cap06.txt); ORDEN es la propuesta de la 68. La de la 67 era COPIA DE LA
VUELTA 66 de .v64ext/orden.py con las rutas cambiadas a los 22 de cap_04. La tabla del
orden propuesto, impresa y no tecleada. Lo unico escrito a mano es ORDEN (la propuesta); todo lo demas se lee de ficheros:
  madres    : .v71ext/veredictos_listos.txt (CONTINUA madre=) y .v71ext/aristas_lectura.txt (SOSTENGO)
  informe   : el barrido de hoy, .v71ext/vecinos_<id>.json, con su poblacion (en la 64 era el informe de la 63)
  vecinos   : los que la senial levanta HOY en el sentido del candidato, dentro y fuera de los 22
  listos    : cada vecino levantado tiene su linea en veredictos_listos.txt
Lo que cambia ademas de las rutas, y se dice: una madre que ya esta en el grafo no ordena nada (ya entro), asi que
las comprobaciones solo miran madres que estan entre los 22; la columna madre(s) las imprime todas.
Y comprueba las dos reglas del orden: madre antes que hijo, y D.36 (si un par levanta en un solo sentido, el que lo
levanta entra despues)."""
import io, json, collections
ORDEN = [
    'hacer_trabajo_futuro_imaginar_negocio',
    'dictar_ritmo_crecimiento_preguntas_escritas',
    'construir_empresa_plantilla_vision_diaria',
    'trazar_modelo_negocio_cliente_primero',
    'fingir_prototipo_cinco_mil_replicas',
    'dar_valor_constante_cuatro_publicos',
    'interrogar_negocio_cinco_preguntas',
    'operar_modelo_gente_destreza_minima',
    'unificar_color_forma_vestuario_modelo',
    'cambiar_saludo_cliente_dos_ramas',
    'probar_traje_azul_seis_semanas',
    'cuantificar_impacto_innovacion_6_pasos',
    'recorrer_siete_pasos_programa_desarrollo_negocio',
    'responder_8_preguntas_construir_primary_aim',
    'responder_4_preguntas_estandares_objetivo_estrategico',
    'distinguir_tres_tipos_sistemas_negocio',
    'aplicar_seis_pasos_sistema_venta',
    'medir_sistema_venta_trece_indicadores_benchmark',
    'construir_estrategia_gente_cuatro_componentes',
    'documentar_trabajo_manual_operaciones',
    'aplicar_ocho_reglas_juego_personas',
    'aplicar_cinco_pasos_proceso_contratacion',
]
TOPE = 22
import re
def _pieza(i):
    r = json.load(io.open('cuarentena/gerber_emyth/%s.json' % i, encoding='utf-8'))['resumen_teorico']
    m = re.search(r'PIEZAS? ([A-Z][0-9]+|COMPUESTA)', r)
    return m.group(1) if m else '?'
L22 = collections.OrderedDict((l.split()[1], (l.split()[0], _pieza(l.split()[1])))
                              for l in io.open('.v76ext/lista_barrido.txt', encoding='utf-8') if l.strip() and not l.startswith('#'))
assert sorted(ORDEN) == sorted(L22), 'ORDEN no son las 22'
# madres
madres = collections.defaultdict(set)
sec, act = collections.defaultdict(set), None
for l in io.open('.v77ext/veredictos_listos.txt', encoding='utf-8'):
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
for l in io.open('.v77ext/aristas_lectura.txt', encoding='utf-8'):
    if l.startswith('SOSTENGO'):
        p = [c.strip() for c in l.split('|')]
        madres[p[2]].add(p[1])
# vecinos levantados hoy, y el informe de cada uno: su barrido
lev, pob = collections.defaultdict(set), {}
for i in L22:
    d = json.load(io.open('.v76ext/vecinos_%s.json' % i, encoding='utf-8'))
    lev[i] = set(v['id'] for v in d['vecinos'])
    pob[i] = d['grafo'] + d['bandejas']
pos = dict((i, k) for k, i in enumerate(ORDEN))
print('%-3s %-60s %-6s %-9s %-60s %-4s %-10s %-4s %-5s %s' % ('#', 'candidato', 'cap', 'pza', 'madre(s)', 'pob', 'dijo', 'vec', 'lin', 'listos'))
for k, i in enumerate(ORDEN, 1):
    cap, pz = L22[i]
    falta = sorted(lev[i] - sec[i])
    print('%-3d %-60s %-6s %-9s %-60s %-4d %-10s %-4d %-5d %s%s' % (
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
print('ARISTAS ESPERADAS EN LA VUELTA 77, CON LAS SEDES DE LA TAREA 2')
cont = set()
act = None
for l in io.open('.v77ext/veredictos_listos.txt', encoding='utf-8'):
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
for l in io.open('.v77ext/aristas_lectura.txt', encoding='utf-8'):
    if l.startswith('SOSTENGO'):
        p = [c.strip() for c in l.split('|')]
        lec.append((p[1], p[2]))
for m, h in sorted(cont):
    print('  CONTINUA   %-56s > %s' % (m, h))
for m, h in lec:
    print('  LECTURA    %-56s > %s' % (m, h))
print('  CONTINUA con madre= (aristas distintas): %d | SOSTENGO por lectura: %d | solapes entre las dos: %d | aristas esperadas: %d' % (
    len(cont), len(lec), len(cont & set(lec)), len(cont | set(lec))))
