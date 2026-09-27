# -*- coding: utf-8 -*-
"""CUANTAS ARISTAS DEL GRAFO CRUZAN DE UN LIBRO A OTRO.

Se corre porque un par de esta tanda (despedir_persona_franqueza_radical contra
despedir_persona_respeto_franqueza) es el mismo trabajo escrito por DOS libros, y
antes de declarar una arista entre libros conviene saber si esta casa ha declarado
alguna. No mueve ninguna vara: es una medicion.
"""
import io, json
nodos, fuentes = {}, {}
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l)
    nodos[d['id']] = d
    fuentes[d['id']] = set(f['clave'] for f in d.get('fuentes', []))
mismo = cruce = 0
for ident, d in nodos.items():
    for hijo in d.get('nodos_siguientes', []):
        if hijo not in fuentes:
            continue
        if fuentes[ident] & fuentes[hijo]:
            mismo += 1
        else:
            cruce += 1
            print('   CRUCE: %s > %s' % (ident, hijo))
print('nodos en el grafo                        : %d' % len(nodos))
print('aristas madre a hijo con libro compartido: %d' % mismo)
print('aristas madre a hijo ENTRE LIBROS        : %d' % cruce)
