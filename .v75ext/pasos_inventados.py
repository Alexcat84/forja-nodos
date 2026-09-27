# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 75 (encargo de la 75, TAREA 5): la lectura es .v73ext/fidelidad.tsv, la de .v73ext/contar_fidelidad.txt, que la ACTA 72 72.4 firmo con sus PUENTE corregidos en la ficha y 0 que entran; la base de comparacion es 4318e81, la apertura de la 73, antes de su TAREA 2 que corrigio los P; la tanda, las filas 1 a 7 de .v73ext/orden.txt. Lo que decia la de la 72: COPIA DE LA VUELTA 72 de .v70ext/pasos_inventados.py (encargo de la 72, TAREA 5): la tanda es la de las filas 1 a 20 de
.v71ext/orden.txt (cap_07, cap_10, cap_11, cap_12, cap_13 y cap_14), y la lectura entera adjudicada es .v71ext/fidelidad.tsv, la de
.v71ext/contar_fidelidad.txt, que la ACTA 70 70.6 firmo en 4 PUENTE de 121 y 0 que entran. Lo que se anade, porque en la 70 no
habia ningun PUENTE: los 4 P se marcaron sobre el texto de la ficha al abrir la 71 (7be17c0) y se corrigieron despues en la ficha
(TAREA 2.2 de la 71); para cada P se compara el texto de ese paso en la ficha que ENTRO con el de 7be17c0, y un P cuyo texto
cambio cuenta como CORREGIDO. PUENTE que entro = P menos corregidos. Lo demas, como estaba en la de la 70:
PASOS INVENTADOS POR CAPITULO sobre lo que ENTRO: lo que entro se lee de cuarentena/_insertados/grove_high_output/
cruzado con dataset/nodos.jsonl, y los pasos de cada ficha se cuentan de su fichero: cada paso tiene que tener su fila."""
import io, json, re, collections, os
def tsv(ruta):
    m = {}
    for l in io.open(ruta, encoding='utf-8'):
        if not l.strip() or l.startswith('#'): continue
        c = [x.strip() for x in l.split('|')]
        m.setdefault(c[0], {})[int(c[1])] = c[2]
    return m
lect = tsv('.v73ext/fidelidad.tsv')
import subprocess
BASE = '4318e81'
viejo = lambda i: json.loads(subprocess.run(['git', 'show', '%s:cuarentena/grove_high_output/%s.json' % (BASE, i)], capture_output=True, text=True, encoding='utf-8').stdout)['pasos_accionables']
grafo = set(json.loads(l)['id'] for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip())
tanda = [l.split()[1] for l in io.open('.v73ext/orden.txt', encoding='utf-8') if re.match(r'^\d+\s', l)][0:7]
entro = [i for i in tanda if os.path.exists('cuarentena/_insertados/grove_high_output/%s.json' % i) and i in grafo]
tot = collections.OrderedDict(); faltan = []
print('%-60s %-7s %5s %3s %3s %4s' % ('candidato que ENTRO', 'cap', 'pasos', 'T', 'P', 'corr'))
for i in entro:
    d = json.load(io.open('cuarentena/_insertados/grove_high_output/%s.json' % i, encoding='utf-8'))
    n = len(d['pasos_accionables'])
    cap = re.search(r'fuentes/grove_high_output/(cap_\d+)\.md', d['resumen_teorico']).group(1)
    m = lect.get(i, {})
    faltan += ['%s %d' % (i, k) for k in range(1, n + 1) if k not in m]
    k = collections.Counter(m[j] for j in range(1, n + 1) if j in m)
    ps = [j for j in range(1, n + 1) if m.get(j) == 'P']
    corr = sum(1 for j in ps if viejo(i)[j - 1] != d['pasos_accionables'][j - 1]) if ps else 0
    t = tot.setdefault(cap, [0, 0, 0, 0]); t[0] += 1; t[1] += n; t[2] += k['P']; t[3] += corr
    print('%-60s %-7s %5d %3d %3d %4d' % (i, cap, n, k['T'], k['P'], corr))
print('entraron: %d de la tanda de %d | pasos sin fila de lectura: %d %s' % (len(entro), len(tanda), len(faltan), faltan))
print()
print('| capitulo | candidatos que entraron | pasos | PUENTE marcados | por ciento | corregidos en la ficha | PUENTE que entro |')
print('|---|---:|---:|---:|---:|---:|---:|')
for cap, (c, n, p, r) in sorted(tot.items()):
    print('| `%s` | %d | %d | %d | %s | %d | %d |' % (cap, c, n, p, ('%.2f' % (100.0 * p / n)).replace('.', ','), r, p - r))
