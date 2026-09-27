# -*- coding: utf-8 -*-
"""R9 de la ACTA 73 seccion 73.11, vuelta 75, sobre los 18 pasos que quedan de dar_elogio_disciplina_igual_critica: el grep de
clausulas que COMPARAN o CONTRASTAN (y X no, mas que, menos que, en vez de, a diferencia de, no solo, sino, igual de, lo contrario)
o que CALIFICAN LA PRUEBA del libro (ha medido, medid, demuestr, probad, comprob, estudi, investig, dato, el texto dice). Imprime
cada paso que casa, con lo que casa. Solo lee el grafo."""
import io, json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
PAT = re.compile(r"\by [^,.:;]{1,40}? no\b|\bmas [^,.:;]{0,40}?\bque\b|\bmenos [^,.:;]{0,40}?\bque\b|\ben vez de\b|\ba diferencia de\b|\bno solo\b|\bsino\b|\bigual de\b|\blo contrario\b"
                 r"|\bha medido\b|\bmedid[oa]s?\b|\bdemuestr\w*|\bprobad[oa]\b|\bcomprob\w*|\bestudi\w*|\binvestig\w*|\bdatos?\b|\bel texto dice\b", re.I)
n = [d for d in map(json.loads, io.open('dataset/nodos.jsonl', encoding='utf-8')) if d['id'] == 'dar_elogio_disciplina_igual_critica'][0]
casan = 0
for k, p in enumerate(n['pasos_accionables'], 1):
    m = [x.group(0) for x in PAT.finditer(p)]
    if m:
        casan += 1
        print('paso %2d | casa: %s' % (k, ' / '.join(m)))
print('pasos: %d | pasos que casan: %d | pasos sin ninguna clausula del patron: %d' % (len(n['pasos_accionables']), casan, len(n['pasos_accionables']) - casan))
