# -*- coding: utf-8 -*-
"""Vuelta 75: las lineas que la vuelta escribio en bitacora/VEREDICTOS.jsonl (de la 1082 en adelante; 1081 al abrir, 75.0), por
veredicto, con su suma, y cuantas van sin razon. Solo lee."""
import io, json, collections
L = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip()][1081:]
c = collections.Counter(d['veredicto'] for d in L)
print('lineas de la vuelta 75 en la bitacora (1082 en adelante): %d | por veredicto: %s | suma: %d | sin razon: %d' % (
    len(L), dict(c), sum(c.values()), sum(1 for d in L if not (d.get('razon') or '').strip())))
