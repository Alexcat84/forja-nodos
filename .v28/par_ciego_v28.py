# -*- coding: utf-8 -*-
"""Imprime los DOS lados de un par (titulo, activacion, entregable, pasos)
SIN la razon escrita en la bitacora. Poblacion: grafo mas bandejas (D.38.4),
descartando _insertados y _derivadas.

Uso: python .v28/par_ciego_v28.py <id_a> <id_b> [...]
"""
import json
import sys
import glob

SEP = chr(92)


def poblacion():
    d = {}
    for l in open('dataset/nodos.jsonl', encoding='utf-8'):
        if l.strip():
            n = json.loads(l)
            d[n['id']] = ('GRAFO', n)
    for f in glob.glob('cuarentena/*/*.json'):
        p = f.replace(SEP, '/')
        if '/_insertados/' in p or '/_derivadas/' in p:
            continue
        try:
            n = json.load(open(f, encoding='utf-8'))
        except Exception:
            continue
        if isinstance(n, dict) and 'id' in n and n['id'] not in d:
            d[n['id']] = ('BANDEJA ' + p, n)
    return d


def pinta(idx, sede, n):
    print('=' * 78)
    print('%s   [%s]' % (idx, sede))
    print('=' * 78)
    print('TITULO      : %s' % n.get('titulo', ''))
    print('ACTIVACION  : %s' % n.get('condiciones_activacion', ''))
    print('ENTREGABLE  : %s' % n.get('entregable_esperado', ''))
    rt = n.get('resumen_teorico', '')
    print('UNIDAD      : %s' % rt[:200])
    pasos = n.get('pasos_accionables', [])
    print('PASOS (%d):' % len(pasos))
    for i, p in enumerate(pasos, 1):
        print('  %2d. %s' % (i, p))
    print()


if __name__ == '__main__':
    pob = poblacion()
    print('poblacion del lector: %d (grafo mas bandejas, D.38.4)' % len(pob))
    print()
    for i in sys.argv[1:]:
        if i not in pob:
            print('NO EXISTE EN GRAFO NI EN BANDEJA: %s' % i)
            continue
        sede, n = pob[i]
        pinta(i, sede, n)
