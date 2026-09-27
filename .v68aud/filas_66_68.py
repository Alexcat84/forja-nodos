# -*- coding: utf-8 -*-
"""Fase ciega de la 68: para las filas 21 y 22 de cap_04, los vecinos que levanta HOY mi barrido (.v68aud/vecinos_<id>.json,
desde _insertados) contra los que levanto mi barrido sellado de la 66 (.v66aud/vecinos_<id>.json, desde la bandeja), y
cuantos de hoy tienen ya su fila de clase en mi .v66aud/mis_clases.tsv sellada. Solo lee."""
import io, json
clases = set()
for l in io.open('.v66aud/mis_clases.tsv', encoding='utf-8'):
    c = l.rstrip('\n').split('\t')
    clases.add(tuple(sorted(c[:2])))
for i in ['agrupar_interrupciones_subordinados_reuniones_regulares', 'canalizar_interrupciones_cartel_hora_oficina']:
    a = set(v['id'] for v in json.load(io.open('.v66aud/vecinos_%s.json' % i, encoding='utf-8'))['vecinos'])
    b = set(v['id'] for v in json.load(io.open('.v68aud/vecinos_%s.json' % i, encoding='utf-8'))['vecinos'])
    con = sum(tuple(sorted((i, v))) in clases for v in b)
    print('%s | 66: %d | hoy: %d | solo 66: %s | solo hoy: %s | de hoy con su fila en .v66aud/mis_clases.tsv: %d' % (
        i, len(a), len(b), sorted(a - b), sorted(b - a), con))
