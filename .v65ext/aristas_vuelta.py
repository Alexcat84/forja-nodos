# -*- coding: utf-8 -*-
"""Las aristas que la vuelta 65 dejo en bitacora/VEREDICTOS.jsonl (lineas 741 en adelante, las de esta vuelta),
y las que siguen EN COLA porque un extremo espera en la bandeja. Comprueba que cada arista cableada vive en el
grafo (madre con el hijo en nodos_siguientes)."""
import io, json, os
L = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip()][740:]
g = dict((d['id'], d) for d in (json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()))
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
print('supervisar_tarea_delegada_etapa_menor_valor sigue en la bandeja: %s' % os.path.exists('cuarentena/grove_high_output/supervisar_tarea_delegada_etapa_menor_valor.json'))
