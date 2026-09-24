# -*- coding: utf-8 -*-
"""ACTA 66: los pasos de las dos filas de cap_04 que no entraron, por la ficha de la bandeja y por las filas de
.v66ext/fidelidad.tsv del extractor."""
import io, json
tsv = io.open('.v66ext/fidelidad.tsv', encoding='utf-8').read().split('\n')
for i in ('agrupar_interrupciones_subordinados_reuniones_regulares', 'canalizar_interrupciones_cartel_hora_oficina'):
    d = json.load(io.open('cuarentena/grove_high_output/%s.json' % i, encoding='utf-8'))
    print('%-58s pasos en la ficha: %d | filas en fidelidad.tsv: %d' % (i, len(d['pasos_accionables']), sum(1 for l in tsv if l.split(' | ')[0] == i)))
