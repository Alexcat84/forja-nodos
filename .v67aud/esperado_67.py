# -*- coding: utf-8 -*-
"""Fase ciega de la 67: lo que MI lectura espera que la tanda de las 20 deje, escrito antes de ver el reporte.
(1) lineas de veredicto: una por fila de vecino de mi barrido de la 66 (.v66aud/vecinos_tabla.txt) cuyo candidato es
    de los 20, porque la poblacion de hoy es la misma que la de aquel barrido (.v67aud/poblacion.txt);
(2) aristas: mis CONTINUA de .v66aud/mis_clases.tsv y mis SOSTENGO de .v66aud/aristas_lectura.tsv cuyo hijo es de
    los 20, con dos correcciones declaradas: la CONTINUA de decir_no la perdi en la ACTA 65 65.4.b (SANO), y la arista
    buscar_actividad a detectar_palanca la dejo en NO por mi relectura de hoy (APERTURA_CIEGA.md de la 67, seccion 5).
No lee el grafo ni nada del extractor."""
import io, json, subprocess, collections
los22 = [l.strip() for l in io.open('.v66aud/los22_cap04.txt', encoding='utf-8') if l.strip()]
FUERA = ('agrupar_interrupciones_subordinados_reuniones_regulares', 'canalizar_interrupciones_cartel_hora_oficina')
T = set(i for i in los22 if i not in FUERA)
filas = collections.Counter()
for l in io.open('.v66aud/vecinos_tabla.txt', encoding='utf-8'):
    c = l.split()
    if len(c) > 2 and c[1] == '>' and c[0] in T: filas[c[0]] += 1
print('candidatos: %d | filas de vecino de mi barrido de la 66 con candidato de los 20: %d' % (len(T), sum(filas.values())))
QUITA = {('usar_calendario_herramienta_planificacion_produccion', 'decir_no_trabajo_excede_capacidad'): 'SANO, ACTA 65 65.4.b',
         ('buscar_actividad_alta_palanca_tres_vias', 'detectar_palanca_negativa_actividad_mando'): 'NO, relectura de la 67'}
ar = []
for l in io.open('.v66aud/mis_clases.tsv', encoding='utf-8'):
    c = l.rstrip('\n').split('\t')
    if c[0] == 'a' or c[2] != 'CONTINUA': continue
    m = c[3]; h = c[1] if c[0] == m else c[0]
    if h in T: ar.append((m, h, 'veredicto CONTINUA'))
for l in io.open('.v66aud/aristas_lectura.tsv', encoding='utf-8'):
    c = l.rstrip('\n').split('\t')
    if c[0] == 'madre' or not c[2].startswith('SOSTENGO'): continue
    if c[1] in T: ar.append((c[0], c[1], 'por lectura'))
n = 0
for m, h, k in ar:
    q = QUITA.get((m, h))
    if q: print('  QUITADA   %-52s > %-52s %-18s | %s' % (m, h, k, q)); continue
    n += 1; print('  ESPERADA  %-52s > %-52s %s' % (m, h, k))
print('aristas que mi lectura espera en la tanda: %d | quitadas por correccion declarada: %d' % (n, len(ar) - n))
G0 = set(json.loads(l)['id'] for l in subprocess.run(['git', 'show', '4648cbc:dataset/nodos.jsonl'], capture_output=True,
         text=True, encoding='utf-8').stdout.splitlines() if l.strip())
esp = [(m, h, k) for m, h, k in ar if (m, h) not in QUITA]
print('esperadas por lectura: %d | por veredicto CONTINUA: %d' % (sum(1 for x in esp if x[2] == 'por lectura'),
      sum(1 for x in esp if x[2] != 'por lectura')))
mg = sorted(set(m for m, h, k in esp if m in G0))
print('madres esperadas que ya vivian en el grafo de 4648cbc: %d %s' % (len(mg), mg))
