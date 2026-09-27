# -*- coding: utf-8 -*-
"""Fase ciega de la 80 (copia libre de .v77aud/esperado_77.py con la tanda de Marquet): lo que MI lectura sellada de la
78 espera que la vuelta deje, con lo que la ACTA 77 77.4 y 77.5 adjudico (mis clases y mi unica SOSTENGO se sostuvieron
enteras: ninguna adjudicacion que aplicar aqui), contado con el mismo predicado y con su suma (R7), y despues, SOLO EN
CUENTAS Y SI O NO, lo que el grafo tiene. No lee la bitacora por dentro ni nada del extractor de la 80.
(1) lineas de veredicto: una por fila dirigida de mi barrido (.v78aud/vecinos_tabla.txt, 'X > Y'), porque la poblacion
    de hoy es la de ese barrido (.v80aud/huellas_hoy.py, grafo_sin_tanda.py), repartidas por la clase de su par
    (.v78aud/mis_clases.tsv);
(2) aristas: las CONTINUA con madre de (1), mas las SOSTENGO de .v78aud/aristas_lectura.tsv que no caen en una CONTINUA;
(3) la bitacora: la de la ACTA 78 78.1 (1172) mas (1), mas una linea por arista por lectura, mas una por la correccion
    declarada de d183 (src/correccion.py escribe una linea CORREGIDO), contra la cuenta de hoy, solo con el numero de lineas;
(4) las aristas del GRAFO con algun extremo en las 20, leidas de las dos listas de relacion de cada nodo, contra (2): SOLO
    cuantas, si cada una esta escrita por los dos lados, si el conjunto es el esperado, y cuantas de las esperadas estan
    y cuantas sobran. NO imprime ninguna clave ni ningun id de relacion leido del grafo (R6). Solo lee."""
import io, re, sys, json, collections
sys.stdout.reconfigure(encoding="utf-8")
las20 = set(io.open('.v78aud/las20.txt', encoding='utf-8').read().split())
cl = {}
for l in list(io.open('.v78aud/mis_clases.tsv', encoding='utf-8'))[1:]:
    f = l.rstrip('\n').split('\t'); cl[tuple(sorted((f[0], f[1])))] = (f[2], f[3])
pc = collections.Counter(c for c, _ in cl.values())
print('pares sellados: %d | por clase: %s | suma: %d' % (len(cl), dict(pc), sum(pc.values())))
fd = collections.Counter(); dc = collections.Counter(); filas = []
for l in io.open('.v78aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +> (\S+) ', l)
    if m and m.group(1) in las20:
        fd['vecino en la tanda' if m.group(2) in las20 else 'vecino fuera de la tanda'] += 1
        dc[cl.get(tuple(sorted(m.groups())), ('SIN FILA',))[0]] += 1; filas.append(m.groups())
print('filas dirigidas de mi barrido con candidato de las 20: %d | por vecino: %s | suma: %d' % (len(filas), dict(fd), sum(fd.values())))
print('lineas de veredicto esperadas, por la clase de su par: %s | suma: %d' % (dict(dc), sum(dc.values())))
ar = set()
for p, (c, madre) in sorted(cl.items()):
    if c == 'CONTINUA': ar.add((madre, p[1] if p[0] == madre else p[0]))
lect = set(); so = collections.Counter()
for f in [l.rstrip('\n').split('\t') for l in io.open('.v78aud/aristas_lectura.tsv', encoding='utf-8')][1:]:
    q = f[2].split()[0]
    if q != 'SOSTENGO': so[q] += 1; continue
    a = (f[0], f[1])
    if a in ar: so['SOSTENGO que cae en una CONTINUA'] += 1
    else: so['SOSTENGO, arista por lectura'] += 1; lect.add(a)
print('filas de mi lectura de aristas: %s | suma: %d' % (dict(so), sum(so.values())))
esp = ar | lect
print('aristas esperadas: %d | CONTINUA con madre= %d | por lectura %d | en las dos: %d' % (len(esp), len(ar), len(lect), len(ar & lect)))
for a in sorted(ar): print('  CONTINUA  %s > %s' % a)
for a in sorted(lect): print('  LECTURA   %s > %s' % a)
print('extremos de esas aristas que no son de las 20: %d' % sum((a[0] not in las20) + (a[1] not in las20) for a in esp))
e = 1172 + len(filas) + len(lect) + 1
hoy = sum(1 for _ in open('bitacora/VEREDICTOS.jsonl', 'rb'))
print('bitacora esperada: 1172 + %d + %d + 1 (d183) = %d | hoy (lineas): %d | %s' % (len(filas), len(lect), e, hoy, 'IGUAL' if e == hoy else 'DISTINTA'))
G = dict((d['id'], d) for d in map(json.loads, io.open('dataset/nodos.jsonl', encoding='utf-8')))
dm = set((m, h) for m in G for h in G[m].get('nodos_siguientes', []) if m in las20 or h in las20)
dh = set((m, h) for h in G for m in G[h].get('nodos_previos', []) if m in las20 or h in las20)
print('aristas del grafo con algun extremo en las 20: escritas en la madre %d | en el hijo %d | las dos listas dicen lo mismo: %s | el conjunto es el esperado: %s' % (
    len(dm), len(dh), 'SI' if dm == dh else 'NO', 'SI' if dm == esp and dh == esp else 'NO'))
print('de las %d esperadas, en el grafo por los dos lados: %d | en el grafo y no esperadas: %d' % (len(esp), len(esp & dm & dh), len((dm | dh) - esp)))
