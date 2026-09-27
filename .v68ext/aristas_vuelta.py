# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 68 de .v67ext/aristas_vuelta.py (encargo, TAREA 4): las aristas que la vuelta 68 dejo en
bitacora/VEREDICTOS.jsonl (lineas 894 en adelante; la 893 era la ultima al abrir, 68.0), y las que siguen EN COLA
porque un extremo espera en la bandeja. Comprueba que cada arista cableada vive en el grafo (madre con el hijo en
nodos_siguientes), y la cruza con las ESPERADAS: las CONTINUA con madre= de las filas 21 y 22 en
.v66ext/veredictos_listos.txt y las SOSTENGO de .v66ext/aristas_lectura.txt cuyo hijo esta en las filas 21 y 22."""
import io, json, re
L = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip()][893:]
g = dict((d['id'], d) for d in (json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()))
tanda = [l.split()[1] for l in io.open('.v66ext/orden.txt', encoding='utf-8') if re.match(r'^\d+\s', l)][20:22]
esperadas, act = set(), None
for l in io.open('.v66ext/veredictos_listos.txt', encoding='utf-8'):
    l = l.rstrip('\n')
    if l.startswith('## '):
        act = l[3:].strip(); continue
    if not l.strip() or l.startswith('#') or act not in tanda: continue
    p = l.split('|')
    if p[1] == 'CONTINUA':
        m = p[2].split('=', 1)[1]; h = p[0] if m == act else act
        esperadas.add((m, h))
for l in io.open('.v66ext/aristas_lectura.txt', encoding='utf-8'):
    if l.startswith('SOSTENGO'):
        p = [c.strip() for c in l.split('|')]
        if p[2] in tanda: esperadas.add((p[1], p[2]))
cab = cola = 0; vistas = {}
print('registros de la vuelta en la bitacora: %d' % len(L))
for d in L:
    a = d.get('arista')
    if not a: continue
    m, h = [x.strip() for x in a.split('>')]
    vive = m in g and h in g and h in (g[m].get('nodos_siguientes') or [])
    por = 'lectura declarada' if 'lectura declarada' in (d.get('levantada_por') or []) else 'veredicto CONTINUA'
    vistas[(m, h)] = vive
    print('%-10s %-19s %s > %s' % ('EN GRAFO' if vive else 'EN COLA', por, m, h))
print('registros con arista: %d | aristas DISTINTAS: %d | en el grafo: %d | en cola: %d (un par CONTINUA leido desde sus dos lados deja dos registros y una sola arista)' % (
    sum(1 for d in L if d.get('arista')), len(vistas), sum(vistas.values()), sum(1 for v in vistas.values() if not v)))
print('esperadas: %d | esperadas que viven en el grafo: %d | esperadas sin registro: %s | registradas no esperadas: %s' % (
    len(esperadas), sum(1 for e in esperadas if vistas.get(e)), sorted(esperadas - set(vistas)) or 0, sorted(set(vistas) - esperadas) or 0))
