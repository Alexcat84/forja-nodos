# -*- coding: utf-8 -*-
"""EL CUADRE DE LA BITACORA (TAREA 2 del encargo de la vuelta 15).

Lo ordena expresamente la TAREA 2: *al cerrar, publica el cuadre: veredictos en
la bitacora antes, escritos en esta vuelta, y cuantos siguen viviendo solo en el
reporte, con su razon*. No fabrica maquinaria nueva (EXTRACTOR.md 13): es el
lector que esa tarea pide, y NO ESCRIBE EN NINGUNA SEDE.

COMO CUENTA LO QUE VIVE SOLO EN EL REPORTE, y la convencion se declara porque la
cifra depende de ella: recorre las filas de tabla de docs/loop/REPORTE.md que
llevan un veredicto (SANO, CONTINUA, REPITE, MUTUO), se queda con las que nombran
DOS ids conocidos entre comillas invertidas (conocido es: vive en el grafo o es un
fichero de cuarentena), y comprueba si ese par esta en bitacora/VEREDICTOS.jsonl
en cualquiera de los dos sentidos. Las filas que no nombran dos ids conocidos NO
se cuentan, y se dice cuantas son.
"""
import glob
import io
import json
import os
import re
import sys

REP = 'docs/loop/REPORTE.md'
BIT = 'bitacora/VEREDICTOS.jsonl'
GRAFO = 'dataset/nodos.jsonl'


def cargar():
    bit = [json.loads(l) for l in io.open(BIT, encoding='utf-8') if l.strip()]
    pares = {tuple(sorted((r['candidato'], r['vecino']))) for r in bit}
    grafo = set()
    for l in io.open(GRAFO, encoding='utf-8'):
        if l.strip():
            grafo.add(json.loads(l)['id'])
    cuar = {}
    for f in glob.glob('cuarentena/*/*.json'):
        partes = f.replace('\\', '/').split('/')
        cuar[os.path.basename(f)[:-5]] = partes[1]
    return bit, pares, grafo, cuar


def main():
    bit, pares, grafo, cuar = cargar()
    conocidos = grafo | set(cuar)
    rep = io.open(REP, encoding='utf-8').read()
    filas = [ln for ln in rep.split('\n')
             if ln.startswith('|') and re.search(r'(SANO|CONTINUA|REPITE|MUTUO)', ln)]
    enc = re.compile(r'`([a-z][a-z0-9_]{8,})`')
    solo_reporte, ya_en_bitacora, sin_par = {}, 0, 0
    for ln in filas:
        ids = list(dict.fromkeys(n for n in enc.findall(ln) if n in conocidos))
        if len(ids) < 2:
            sin_par += 1
            continue
        par = tuple(sorted(ids[:2]))
        if par in pares:
            ya_en_bitacora += 1
        else:
            solo_reporte.setdefault(par, re.search(r'(SANO|CONTINUA|REPITE|MUTUO)', ln).group(1))

    print('LA BITACORA HOY')
    print('  veredictos en bitacora/VEREDICTOS.jsonl   : %d' % len(bit))
    print('  de ellos con arista cableada              : %d' % sum(1 for r in bit if r.get('arista')))
    print('  de ellos por lectura declarada            : %d'
          % sum(1 for r in bit if 'lectura declarada' in str(r.get('levantada_por'))))
    print('  nodos en el grafo                         : %d' % len(grafo))
    print()
    print('LAS FILAS DE VEREDICTO DEL REPORTE')
    print('  filas de tabla con un veredicto           : %d' % len(filas))
    print('  su par YA esta en la bitacora             : %d' % ya_en_bitacora)
    print('  sin dos ids conocidos en la fila, no cuenta: %d' % sin_par)
    print()
    a = {p: v for p, v in solo_reporte.items() if p[0] in grafo and p[1] in grafo}
    b = {p: v for p, v in solo_reporte.items() if p not in a}
    print('LO QUE VIVE SOLO EN EL REPORTE: %d pares distintos' % len(solo_reporte))
    print('  A) los dos ids VIVEN EN EL GRAFO          : %d   (CONTINUA %d, SANO %d)'
          % (len(a), sum(1 for v in a.values() if v == 'CONTINUA'),
             sum(1 for v in a.values() if v == 'SANO')))
    print('  B) uno sigue en CUARENTENA, lote abierto  : %d   (CONTINUA %d, SANO %d)'
          % (len(b), sum(1 for v in b.values() if v == 'CONTINUA'),
             sum(1 for v in b.values() if v == 'SANO')))
    print()
    print('  A) EL DETALLE, que es la especie sin sede de hoy:')
    for p, v in sorted(a.items(), key=lambda x: (x[1], x[0])):
        print('     %-8s %s  <->  %s' % (v, p[0], p[1]))
    print()
    print('  B) EL DETALLE, con quien espera y en que lote:')
    for p, v in sorted(b.items()):
        q = [x for x in p if x not in grafo]
        print('     %-8s %s <-> %s   (espera: %s, lote %s)'
              % (v, p[0], p[1], q[0], cuar.get(q[0], '?')))
    return 0


if __name__ == '__main__':
    sys.exit(main())
