# -*- coding: utf-8 -*-
"""Vuelta 75, encargo TAREA 5: la fila de cap_13 de scott_radical_candor despues de la TAREA 2. Lee las 70 marcas de
.v74ext/fidelidad.tsv (numeracion vieja, de 20 pasos en dar_elogio), aplica la unica adjudicacion de la ACTA 73 73.4 y 73.5 que las
mueve (dar_elogio_disciplina_igual_critica paso 8, T pasa a P), toma los pasos de los tres nodos en 9a5151a (75.0, antes de la
TAREA 2) y mira, para cada PUENTE, si su texto sigue hoy en pasos_accionables del grafo. Solo lee."""
import io, json, subprocess, collections
ADJ = {('dar_elogio_disciplina_igual_critica', 8): 'P'}
marca = collections.OrderedDict()
for l in io.open('.v74ext/fidelidad.tsv', encoding='utf-8'):
    if not l.strip() or l.startswith('#'): continue
    c = [x.strip() for x in l.split('|')]
    marca[(c[0], int(c[1]))] = ADJ.get((c[0], int(c[1])), c[2])
ids = list(dict.fromkeys(i for i, _ in marca))
antes = dict((d['id'], d) for d in (json.loads(l) for l in subprocess.run(['git', 'show', '9a5151a:dataset/nodos.jsonl'],
         capture_output=True, text=True, encoding='utf-8').stdout.splitlines() if l.strip()) if d['id'] in ids)
hoy = dict((d['id'], d) for d in (json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()) if d['id'] in ids)
tp = tn = tpg = 0
for i in ids:
    k = collections.Counter(v for (j, _), v in marca.items() if j == i)
    ps = [n for (j, n), v in marca.items() if j == i and v == 'P']
    siguen = [n for n in ps if antes[i]['pasos_accionables'][n - 1] in hoy[i]['pasos_accionables']]
    tp += k['P']; tn += sum(k.values()); tpg += len(siguen)
    print('%-52s marcas %2d | T %2d P %d | pasos en 9a5151a %2d | hoy %2d | PUENTE %s | que siguen hoy en el grafo: %d' % (
        i, sum(k.values()), k['T'], k['P'], len(antes[i]['pasos_accionables']), len(hoy[i]['pasos_accionables']), ps or '-', len(siguen)))
print('cap_13 de scott, los tres: pasos marcados %d | PUENTE %d | %s por ciento | pasos hoy en el grafo %d | PUENTE que siguen en el grafo %d' % (
    tn, tp, ('%.2f' % (100.0 * tp / tn)).replace('.', ','), sum(len(hoy[i]['pasos_accionables']) for i in ids), tpg))
