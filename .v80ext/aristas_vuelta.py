# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 80 de .v77ext/aristas_vuelta.py (encargo de la 80, TAREA 3.5). Lo cambiado, y nada mas: la linea de apertura, que es la 1172 (ACTA 78 78.1: lo que la vuelta 80 escribe en la bitacora son las lineas 1173 en adelante); las sedes, .v78ext/veredictos_listos.txt y .v78ext/aristas_lectura.txt; y la tanda, las filas 1 a 20 de .v78ext/orden.txt. Lo que decia la de la 77: COPIA DE LA VUELTA 77 de .v75ext/aristas_vuelta.py, con la linea de apertura en la 1111, las sedes en .v77ext/ y la tanda en las filas 1 a 22 de .v76ext/orden.txt, y dos columnas: los DOS LADOS (madre con el hijo en nodos_siguientes E hijo con la madre en nodos_previos) y el veredicto que la arista lleva en la bitacora, para que ninguna quede sin adjudicar. Cruza las aristas que la vuelta dejo en la bitacora con las ESPERADAS: las CONTINUA con madre= de la tanda en veredictos_listos.txt (sin las lineas #) y las SOSTENGO de aristas_lectura.txt cuyo hijo esta en la tanda."""
import io, json, re
L = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip()][1172:]
g = dict((d['id'], d) for d in (json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()))
tanda = [l.split()[1] for l in io.open('.v78ext/orden.txt', encoding='utf-8') if re.match(r'^\d+\s', l)][0:20]
esperadas, act = set(), None
for l in io.open('.v78ext/veredictos_listos.txt', encoding='utf-8'):
    l = l.rstrip('\n')
    if l.startswith('## '):
        act = l[3:].strip(); continue
    if not l.strip() or l.startswith('#') or act not in tanda: continue
    p = l.split('|')
    if p[1] == 'CONTINUA':
        m = p[2].split('=', 1)[1]; h = p[0] if m == act else act
        esperadas.add((m, h))
for l in io.open('.v78ext/aristas_lectura.txt', encoding='utf-8'):
    if l.startswith('SOSTENGO'):
        p = [c.strip() for c in l.split('|')]
        if p[2] in tanda: esperadas.add((p[1], p[2]))
cab = cola = 0; vistas = {}
print('registros de la vuelta en la bitacora: %d' % len(L))
for d in L:
    a = d.get('arista')
    if not a: continue
    m, h = [x.strip() for x in a.split('>')]
    vive = m in g and h in g and h in (g[m].get('nodos_siguientes') or []) and m in (g[h].get('nodos_previos') or [])
    por = 'lectura declarada' if 'lectura declarada' in (d.get('levantada_por') or []) else 'veredicto CONTINUA'
    vistas[(m, h)] = vive
    print('%-10s %-19s %-9s %s > %s' % ('EN GRAFO' if vive else 'EN COLA', por, d.get('veredicto') or 'SIN', m, h))
print('registros con arista sin veredicto: %d' % sum(1 for d in L if d.get('arista') and not d.get('veredicto')))
print('registros con arista: %d | aristas DISTINTAS: %d | en el grafo: %d | en cola: %d (un par CONTINUA leido desde sus dos lados deja dos registros y una sola arista)' % (
    sum(1 for d in L if d.get('arista')), len(vistas), sum(vistas.values()), sum(1 for v in vistas.values() if not v)))
print('esperadas: %d | esperadas que viven en el grafo: %d | esperadas sin registro: %s | registradas no esperadas: %s' % (
    len(esperadas), sum(1 for e in esperadas if vistas.get(e)), sorted(esperadas - set(vistas)) or 0, sorted(set(vistas) - esperadas) or 0))
