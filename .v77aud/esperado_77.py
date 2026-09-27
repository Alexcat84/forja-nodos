# -*- coding: utf-8 -*-
"""Fase ciega de la 77 (copia libre de .v75aud/esperado_75.py con la tanda de la 76): lo que MI lectura sellada de la 76
espera que la vuelta deje, con las adjudicaciones de la ACTA 75 75.4 aplicadas AQUI Y DECLARADAS, contado con el mismo
predicado y con su suma (R7), y despues, SOLO EN CUENTAS Y SI O NO, lo que el grafo tiene. No lee la bitacora por dentro
ni nada del extractor.
Las adjudicaciones de la ACTA 75 75.4 que aplico: (i) el par recorrer_siete_pasos_programa_desarrollo_negocio con
construir_estrategia_gente_cuatro_componentes, que selle CONTINUA, es SANO con arista por lectura D.37 (D.53); (ii) mis dos
D.29 de los cuestionarios responder_8 y responder_4 a construir caen; (iii) la arista D.37 de construir a
documentar_trabajo_manual_operaciones, que yo no tenia, se sostiene (D76.14). Lo que la ACTA 75 mando a relectura
conjunta lo cuento con MI lectura, que mantengo en esta fase (seccion 6 de la apertura): el par de la contratacion
CONTINUA con madre construir, y la arista D.29 de fingir a recorrer.
(1) lineas de veredicto: una por fila dirigida de mi barrido (.v76aud/vecinos_tabla.txt, 'X > Y'), porque la poblacion
    de hoy es la de ese barrido (.v77aud/huellas_hoy.py, grafo_sin_tanda.py), repartidas por la clase de su par;
(2) aristas: las CONTINUA con madre de (1), mas las aristas por lectura que no caen en una CONTINUA;
(3) la bitacora: la de la ACTA 75 75.1 (1111) mas (1) mas una linea por arista por lectura, contra la cuenta de hoy,
    solo con el numero de lineas;
(4) las aristas del GRAFO con algun extremo en las 22, leidas de las dos listas de relacion de cada nodo, contra (2): SOLO
    cuantas, si cada una esta escrita por los dos lados, si el conjunto es el esperado, y cuantas de las esperadas estan
    y cuantas sobran. NO imprime ninguna clave ni ningun id de relacion leido del grafo (R6). Solo lee."""
import io, re, sys, json, collections
sys.stdout.reconfigure(encoding="utf-8")
las22 = set(io.open('.v76aud/las22.txt', encoding='utf-8').read().split())
RC = tuple(sorted(('recorrer_siete_pasos_programa_desarrollo_negocio', 'construir_estrategia_gente_cuatro_componentes')))
cl = {}
for l in list(io.open('.v76aud/mis_clases.tsv', encoding='utf-8'))[1:]:
    f = l.rstrip('\n').split('\t'); p = tuple(sorted((f[0], f[1])))
    cl[p] = ('SANO', '') if p == RC else (f[2], f[3])
print('pares sellados: %d | con la adjudicacion (i) de la ACTA 75 75.4 aplicada: %d' % (len(cl), sum(1 for p in cl if p == RC)))
fd = collections.Counter(); dc = collections.Counter(); filas = []
for l in io.open('.v76aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +> (\S+) ', l)
    if m and m.group(1) in las22:
        fd['vecino en la tanda' if m.group(2) in las22 else 'vecino fuera de la tanda'] += 1
        dc[cl.get(tuple(sorted(m.groups())), ('SIN FILA',))[0]] += 1; filas.append(m.groups())
print('filas dirigidas de mi barrido con candidato de las 22: %d | por vecino: %s | suma: %d' % (len(filas), dict(fd), sum(fd.values())))
print('lineas de veredicto esperadas, por la clase de su par: %s | suma: %d' % (dict(dc), sum(dc.values())))
ar = set()
for p, (c, madre) in sorted(cl.items()):
    if c == 'CONTINUA': ar.add((madre, p[1] if p[0] == madre else p[0]))
CAEN = {('responder_8_preguntas_construir_primary_aim', 'construir_estrategia_gente_cuatro_componentes'),
        ('responder_4_preguntas_estandares_objetivo_estrategico', 'construir_estrategia_gente_cuatro_componentes')}
lect = set(); so = collections.Counter()
for f in [l.rstrip('\n').split('\t') for l in io.open('.v76aud/aristas_lectura.tsv', encoding='utf-8')][1:]:
    if not f[2].startswith('SOSTENGO'): continue
    a = (f[0], f[1])
    if a in ar: so['cae en una CONTINUA'] += 1
    elif a in CAEN: so['cae por la ACTA 75 75.4 (ii)'] += 1
    else: so['arista por lectura'] += 1; lect.add(a)
lect.add(('construir_estrategia_gente_cuatro_componentes', 'documentar_trabajo_manual_operaciones')); so['anadida por la ACTA 75 75.4 (iii)'] += 1
print('SOSTENGO de mi lectura sellada y la de la ACTA 75: %s | suma: %d' % (dict(so), sum(so.values())))
esp = ar | lect
print('aristas esperadas: %d | CONTINUA con madre= %d | por lectura %d | en las dos: %d' % (len(esp), len(ar), len(lect), len(ar & lect)))
for a in sorted(ar): print('  CONTINUA  %s > %s' % a)
for a in sorted(lect): print('  LECTURA   %s > %s' % a)
print('extremos de esas aristas que no son de las 22: %d' % sum((a[0] not in las22) + (a[1] not in las22) for a in esp))
e = 1111 + len(filas) + len(lect)
hoy = sum(1 for _ in open('bitacora/VEREDICTOS.jsonl', 'rb'))
print('bitacora esperada: 1111 + %d + %d = %d | hoy (lineas): %d | %s' % (len(filas), len(lect), e, hoy, 'IGUAL' if e == hoy else 'DISTINTA'))
G = dict((d['id'], d) for d in map(json.loads, io.open('dataset/nodos.jsonl', encoding='utf-8')))
dm = set((m, h) for m in G for h in G[m].get('nodos_siguientes', []) if m in las22 or h in las22)
dh = set((m, h) for h in G for m in G[h].get('nodos_previos', []) if m in las22 or h in las22)
print('aristas del grafo con algun extremo en las 22: escritas en la madre %d | en el hijo %d | las dos listas dicen lo mismo: %s | el conjunto es el esperado: %s' % (
    len(dm), len(dh), 'SI' if dm == dh else 'NO', 'SI' if dm == esp and dh == esp else 'NO'))
print('de las %d esperadas, en el grafo por los dos lados: %d | en el grafo y no esperadas: %d' % (len(esp), len(esp & dm & dh), len((dm | dh) - esp)))
