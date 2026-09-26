# -*- coding: utf-8 -*-
"""Vuelta 72, TAREA 4: los registros con arista que la vuelta dejo en bitacora/VEREDICTOS.jsonl (lineas 1028 en adelante, 72.0),
con su veredicto y su razon, cuantos quedan sin adjudicar, y los veredictos de la vuelta por clase. Solo lee."""
import json, io
L = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip()][1027:]
A = [d for d in L if d.get('arista')]
print('registros con arista: %d | con veredicto CONTINUA: %d | con razon escrita: %d | sin adjudicar: %d' % (len(A), sum(1 for d in A if d.get('veredicto') == 'CONTINUA'), sum(1 for d in A if (d.get('razon') or '').strip()), sum(1 for d in A if not d.get('veredicto'))))
print('veredictos de la vuelta por clase:', sorted((v, sum(1 for d in L if d.get('veredicto') == v)) for v in set(d.get('veredicto') for d in L)))
