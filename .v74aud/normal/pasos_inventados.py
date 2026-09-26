# -*- coding: utf-8 -*-
"""ACTA 73: PASOS INVENTADOS de los tres nodos de cap_13 de scott_radical_candor que nombra d084, contados desde las marcas del
extractor (.v74ext/fidelidad.tsv) con las adjudicaciones de la ACTA 73 73.5 aplicadas encima, que se imprimen. Denominador: los
pasos de cada nodo en dataset/nodos.jsonl HOY. Una fila por nodo y el total, con la suma de cada reparto (R7). Solo lee."""
import io, json, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
ADJ = {('dar_elogio_disciplina_igual_critica', 8): 'P'}   # ACTA 73 73.5: PUENTE fuera de su marcado; el 17 ya es P suyo
marca = {}
for l in io.open('.v74ext/fidelidad.tsv', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    i, p, c = [x.strip() for x in l.split('|')[:3]]
    marca[(i, int(p))] = c
for k, v in ADJ.items():
    print('adjudicada por la ACTA 73: %s paso %d, %s de su marca pasa a %s' % (k[0], k[1], marca[k], v)); marca[k] = v
grafo = {}
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l)
    if any(k[0] == d['id'] for k in marca): grafo[d['id']] = len(d['pasos_accionables'])
tot = collections.Counter()
for i in sorted(grafo):
    c = collections.Counter(v for k, v in marca.items() if k[0] == i)
    tot.update(c)
    print('%-52s pasos en el grafo %2d | por marca: %s | suma: %d | PUENTE %d de %d = %.2f por ciento' % (i, grafo[i], dict(sorted(c.items())), sum(c.values()), c['P'], grafo[i], 100.0 * c['P'] / grafo[i]))
n = sum(grafo.values())
print('cap_13, los tres: pasos en el grafo %d | por marca: %s | suma: %d | PUENTE %d de %d = %.2f por ciento' % (n, dict(sorted(tot.items())), sum(tot.values()), tot['P'], n, 100.0 * tot['P'] / n))
