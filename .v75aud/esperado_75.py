# -*- coding: utf-8 -*-
"""Fase ciega de la 75 (copia libre de .v72aud/esperado_72.py con la tanda de la 73): lo que MI lectura sellada de la 73
espera que la vuelta deje, contado con el mismo predicado y con su suma (R7), y despues, SOLO EN CUENTAS Y SI O NO, lo que
el grafo tiene. No lee la bitacora por dentro ni nada del extractor.
(1) lineas de veredicto: una por fila dirigida de mi barrido (.v73aud/vecinos_tabla.txt, 'X > Y') cuyo candidato es de
    las 7, porque la poblacion de hoy es la de ese barrido (.v75aud/huellas_hoy.py, grafo_sin_tanda.py), repartidas por la
    clase de su par en .v73aud/mis_clases.tsv CON LA CORRECCION DE LA ACTA 72 72.5 APLICADA AQUI Y DECLARADA: el par
    priorizar_lista_entrenamiento_subordinados con pedir_critica_anonima_curso_entrenamiento_dictado, que selle CONTINUA,
    se adjudico SANO (D73.9, abuela y nieta);
(2) aristas: las CONTINUA que quedan de (1); las SOSTENGO de .v73aud/aristas_lectura.tsv NO son aristas aparte, porque
    cada una dice en su fila que si el barrido levanta el par es su linea CONTINUA (ACTA 72 72.3), y se cuenta cuantas caen
    en una CONTINUA, cuantas en el par corregido y cuantas quedarian sueltas;
(3) la bitacora: la de la ACTA 73 73.1 (1081) mas (1) mas una linea por la correccion declarada de la TAREA 2
    (src/correccion.py escribe UNA con agregar_jsonl; scripts/retirar_paso.py no escribe en la bitacora), contra la
    cuenta de hoy, solo con el numero de lineas;
(4) las aristas del GRAFO con algun extremo en las 7, leidas de las dos listas de relacion de cada nodo, contra (2): SOLO
    cuantas, si cada una esta escrita por los dos lados y si el conjunto es el esperado. NO imprime ninguna clave ni ningun
    id de relacion (R6). Solo lee."""
import io, re, sys, json, collections
sys.stdout.reconfigure(encoding="utf-8")
los7 = set(io.open('.v73aud/los7.txt', encoding='utf-8').read().split())
CORR = tuple(sorted(('priorizar_lista_entrenamiento_subordinados', 'pedir_critica_anonima_curso_entrenamiento_dictado')))
cl = {}
for l in list(io.open('.v73aud/mis_clases.tsv', encoding='utf-8'))[1:]:
    f = l.rstrip('\n').split('\t'); p = tuple(sorted((f[0], f[1])))
    cl[p] = ('SANO', '') if p == CORR else (f[2], f[3])
print('pares sellados: %d | con la correccion de la ACTA 72 72.5 aplicada: %d' % (len(cl), sum(1 for p in cl if p == CORR)))
fd = collections.Counter(); dc = collections.Counter(); filas = []
for l in io.open('.v73aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +> (\S+) ', l)
    if m and m.group(1) in los7:
        fd['vecino en la tanda' if m.group(2) in los7 else 'vecino fuera de la tanda'] += 1
        dc[cl.get(tuple(sorted(m.groups())), ('SIN FILA',))[0]] += 1; filas.append(m.groups())
print('filas dirigidas de mi barrido con candidato de las 7: %d | por vecino: %s | suma: %d' % (len(filas), dict(fd), sum(fd.values())))
print('lineas de veredicto esperadas, por la clase de su par: %s | suma: %d' % (dict(dc), sum(dc.values())))
ar = set()
for p, (c, madre) in sorted(cl.items()):
    if c == 'CONTINUA': ar.add((madre, p[1] if p[0] == madre else p[0]))
so = collections.Counter()
for f in [l.rstrip('\n').split('\t') for l in io.open('.v73aud/aristas_lectura.tsv', encoding='utf-8')][1:]:
    if f[2].startswith('SOSTENGO'):
        so['cae en una CONTINUA' if (f[0], f[1]) in ar else ('es el par corregido a SANO' if tuple(sorted((f[0], f[1]))) == CORR else 'SUELTA')] += 1
print('SOSTENGO de mi lectura: %s | suma: %d' % (dict(so), sum(so.values())))
print('aristas esperadas: %d, todas CONTINUA con madre=' % len(ar))
for a in sorted(ar): print('  %s > %s' % a)
print('extremos de esas aristas que no son de las 7: %d' % sum((a[0] not in los7) + (a[1] not in los7) for a in ar))
esp = 1081 + len(filas) + 1
hoy = sum(1 for _ in open('bitacora/VEREDICTOS.jsonl', 'rb'))
print('bitacora esperada: 1081 + %d + 1 = %d | hoy (lineas): %d | %s' % (len(filas), esp, hoy, 'IGUAL' if esp == hoy else 'DISTINTA'))
G = dict((d['id'], d) for d in map(json.loads, io.open('dataset/nodos.jsonl', encoding='utf-8')))
desde_madre = set((m, h) for m in G for h in G[m].get('nodos_siguientes', []) if m in los7 or h in los7)
desde_hijo = set((m, h) for h in G for m in G[h].get('nodos_previos', []) if m in los7 or h in los7)
print('aristas del grafo con algun extremo en las 7: escritas en la madre %d | en el hijo %d | las dos listas dicen lo mismo: %s | el conjunto es el esperado: %s' % (
    len(desde_madre), len(desde_hijo), 'SI' if desde_madre == desde_hijo else 'NO', 'SI' if desde_madre == ar and desde_hijo == ar else 'NO'))
