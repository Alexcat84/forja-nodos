# -*- coding: utf-8 -*-
"""Vuelta 64, TAREA 4: la tabla del orden propuesto para los 22 de cap_02 y cap_03, impresa y no
tecleada. Lo unico escrito a mano es ORDEN (la propuesta); todo lo demas se lee de ficheros:
  madres    : .v64ext/veredictos_listos.txt (CONTINUA madre=) y .v64ext/aristas_lectura.txt (SOSTENGO)
  informe   : .v63aud/informe_<id>.txt o el archivo de la fase ciega 2, con su poblacion
  vecinos   : los que la senial levanta HOY en el sentido del candidato, dentro de los 22
              (.v64ext/matriz22_*.txt) y fuera de ellos (.v64ext/pares_despues.txt)
  listos    : cada vecino levantado tiene su linea en veredictos_listos.txt
Y comprueba las dos reglas del orden: madre antes que hijo, y D.36 (si un par levanta en un solo
sentido, el que lo levanta entra despues)."""
import glob, io, os, re, collections
A = 'docs/loop/archivo/interrumpidas/2026-09-23-v63-fase-ciega-2/v63ciega'
ORDEN = [
    'construir_flujo_produccion_paso_limitante', 'clasificar_trabajo_proceso_montaje_prueba',
    'detectar_arreglar_fallo_etapa_menor_valor', 'dimensionar_inventario_materia_prima_reposicion',
    'rehacer_flujo_paso_limitante_capacidad', 'equilibrar_capacidad_personal_inventario_plazo',
    'preferir_inspeccion_proceso_prueba_destructiva',
    'elegir_cinco_indicadores_diarios_fabrica', 'emparejar_indicadores_efecto_contraefecto',
    'elegir_indicador_salida_trabajo_administrativo', 'representar_actividad_caja_negra_ventanas',
    'construir_indicador_linealidad_alerta_temprana', 'construir_indicador_tendencia_patron',
    'construir_grafico_escalonado_pronosticos', 'archivar_indicadores_resolver_problemas',
    'elegir_fabricar_pedido_pronostico', 'casar_flujo_fabricacion_flujo_ventas',
    'dimensionar_plantilla_administrativa_pronostico', 'decidir_aceptar_rechazar_material_defectuoso',
    'elegir_inspeccion_barrera_monitorizacion', 'variar_frecuencia_inspeccion_nivel_calidad',
    'simplificar_trabajo_reducir_numero_pasos']
TOPE = 20
L22 = collections.OrderedDict((l.split()[0], (l.split()[1], l.split()[2]))
                              for l in io.open('.v64ext/los22.txt', encoding='utf-8') if l.strip() and not l.startswith('#'))
assert sorted(ORDEN) == sorted(L22), 'ORDEN no son los 22'
# madres
madres = collections.defaultdict(set)
sec, act = collections.defaultdict(set), None
for l in io.open('.v64ext/veredictos_listos.txt', encoding='utf-8'):
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
        if m in L22 and h in L22:
            madres[h].add(m)
for l in io.open('.v64ext/aristas_lectura.txt', encoding='utf-8'):
    if l.startswith('SOSTENGO'):
        p = [c.strip() for c in l.split('|')]
        madres[p[2]].add(p[1])
# vecinos levantados hoy
lev = collections.defaultdict(set)
for f in sorted(glob.glob('.v64ext/matriz22_*.txt')):
    for l in io.open(f, encoding='utf-8'):
        m = re.match(r'LEVANTA\s+(\S+)\s+->\s+(\S+)', l)
        if m:
            lev[m.group(1)].add(m.group(2))
for l in io.open('.v64ext/pares_despues.txt', encoding='utf-8'):
    c = l.split()
    if len(c) > 3 and c[0] in ('d005', 'd140', 'lectura') and c[2] not in L22 and not l.rstrip().endswith('NO LEVANTA'):
        lev[c[1]].add(c[2])
def informe(i):
    for r in ('.v63aud/informe_%s.txt' % i, '%s/informe_%s.txt' % (A, i)):
        if os.path.exists(r) and os.path.getsize(r):
            t = io.open(r, encoding='utf-8').read()
            pob = re.search(r'poblacion del barrido\s*:\s*(\d+)', t)
            ver = re.search(r'^\[(\w+)\] %s' % re.escape(i), t, re.M)
            return ('.v63aud' if r.startswith('.v63aud') else 'archivo fase 2'), pob.group(1) if pob else '?', ver.group(1) if ver else '?'
    return 'NINGUNO', '?', '?'
pos = dict((i, k) for k, i in enumerate(ORDEN))
print('%-3s %-48s %-6s %-4s %-44s %-15s %-4s %-10s %-4s %-5s %s' % ('#', 'candidato', 'cap', 'pza', 'madre(s)', 'informe', 'pob', 'dijo(462)', 'vec', 'lin', 'listos'))
for k, i in enumerate(ORDEN, 1):
    cap, pz = L22[i]
    sede, pob, ver = informe(i)
    falta = sorted(lev[i] - sec[i])
    print('%-3d %-48s %-6s %-4s %-44s %-15s %-4s %-10s %-4d %-5d %s%s' % (
        k, i, cap, pz, ', '.join(sorted(madres[i])) or '-', sede, pob, ver, len(lev[i]), len(sec[i]),
        'SI' if not falta else 'FALTAN %s' % falta, '   <- corte del tope' if k == TOPE else ''))
print()
print('COMPROBACIONES')
mal = [(m, h) for h in madres for m in madres[h] if pos[m] > pos[h]]
print('  hijo delante de su madre: %d %s' % (len(mal), mal))
d36 = [(a, b) for a in L22 for b in lev[a] if b in L22 and a not in lev[b] and pos[a] < pos[b]]
print('  D.36, par que levanta en un solo sentido con el que lo levanta entrando antes: %d %s' % (len(d36), d36))
fuera = [(m, h) for h in ORDEN[:TOPE] for m in madres[h] if m in ORDEN[TOPE:]]
print('  hijo dentro del tope con su madre fuera: %d %s' % (len(fuera), fuera))
print('  tanda propuesta: %d de %d; fuera del tope: %s' % (TOPE, len(ORDEN), ', '.join(ORDEN[TOPE:])))
