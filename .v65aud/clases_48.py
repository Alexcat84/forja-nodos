# -*- coding: utf-8 -*-
"""Cruza los 48 pares de mi barrido (.v65aud/pares48.txt) con MI lectura ciega (.v65aud/mis_clases.tsv).
Cada par del barrido sale con mi clase si lo lei a ciegas, o marcado VISTA si su clase adjudicada ya
estaba delante de mi antes de leerlo (lo dice la seccion 6 de la apertura)."""
import io, collections
mis = {}
for l in io.open('.v65aud/mis_clases.tsv', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    c = [x.strip() for x in l.split('|')]
    mis[frozenset((c[0], c[1]))] = (c[2], c[3])
filas = [[x.strip() for x in l.split('|')] for l in io.open('.v65aud/pares48.txt', encoding='utf-8') if l.strip()]
k = collections.Counter(); usados = set()
for c in filas:
    p = frozenset((c[0], c[1]))
    if p in mis:
        usados.add(p); k[mis[p][0]] += 1; k['ciegas'] += 1
        print('CIEGA  %-6s %-5s %s -> %s' % (mis[p][0], mis[p][1], c[0], c[1]))
    else: k['vistas'] += 1
print('filas del barrido: %d | con mi lectura ciega: %d (%s) | con la clase ya vista antes de leer: %d' % (
    len(filas), k['ciegas'], ', '.join('%s %d' % (x, k[x]) for x in ('SANO', 'CONTINUA', 'REPITE', 'MUTUO') if k[x]), k['vistas']))
print('pares no ordenados en mi lectura: %d | de ellos sin fila en el barrido: %d' % (len(mis), len(set(mis) - usados)))
