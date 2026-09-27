# -*- coding: utf-8 -*-
"""PASOS INVENTADOS POR CAPITULO (AUDITOR_FORJA 8): el DENOMINADOR, contado
del dato y no del reporte.

El numerador (cuantos resultaron PUENTE) NO lo puede contar una maquina: la
aduana no tiene el libro delante (D.30). Lo pone el auditor leyendo paso a paso
contra el parrafo, y este instrumento le da la poblacion exacta y el rango de
lineas declarado de cada nodo, para que la lectura no se haga de memoria.

Uso: python .v28/pasos_inventados_v28.py <id> [<id> ...]
"""
import json
import re
import sys

RANGO = re.compile(r'lineas?\s+(\d+)\s+a\s+(\d+)')
UNIDAD = re.compile(r'(cap_\d+)\.md')


def main(ids):
    grafo = {}
    for l in open('dataset/nodos.jsonl', encoding='utf-8'):
        if l.strip():
            n = json.loads(l)
            grafo[n['id']] = n
    total = 0
    print('PASOS INVENTADOS: LA POBLACION, contada del dataset')
    print('')
    print('%-52s %6s  %-9s %s' % ('nodo', 'pasos', 'unidad', 'lineas declaradas'))
    print('-' * 100)
    for i in ids:
        n = grafo.get(i)
        if n is None:
            print('%-52s   NO VIVE EN EL GRAFO' % i)
            continue
        rt = n.get('resumen_teorico', '')
        pasos = len(n.get('pasos_accionables', []))
        total += pasos
        mr = RANGO.search(rt)
        mu = UNIDAD.search(rt)
        print('%-52s %6d  %-9s %s' % (i, pasos,
                                      mu.group(1) if mu else '?',
                                      ('L%s a L%s' % mr.groups()) if mr else '(no declara rango)'))
    print('-' * 100)
    print('%-52s %6d' % ('TOTAL DE PASOS DE LA POBLACION', total))


if __name__ == '__main__':
    main(sys.argv[1:])
