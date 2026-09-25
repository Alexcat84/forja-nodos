# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 70 de .v68ext/pasos_inventados.py (encargo, TAREA 5): la tanda es la de las filas 1 a 20 de
.v69ext/orden.txt (cap_05 y cap_06), y la lectura entera adjudicada es .v68ext/fidelidad.tsv, la de .v68ext/contar_fidelidad.txt,
que la ACTA 67 67.4.a firmo en 0 de 84 y 0 de 62. Lo demas, como estaba.
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
lect = tsv('.v68ext/fidelidad.tsv')
grafo = set(json.loads(l)['id'] for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip())
tanda = [l.split()[1] for l in io.open('.v69ext/orden.txt', encoding='utf-8') if re.match(r'^\d+\s', l)][0:20]
entro = [i for i in tanda if os.path.exists('cuarentena/_insertados/grove_high_output/%s.json' % i) and i in grafo]
tot = collections.OrderedDict(); faltan = []
print('%-56s %-7s %5s %3s %3s' % ('candidato que ENTRO', 'cap', 'pasos', 'T', 'P'))
for i in entro:
    d = json.load(io.open('cuarentena/_insertados/grove_high_output/%s.json' % i, encoding='utf-8'))
    n = len(d['pasos_accionables'])
    cap = re.search(r'fuentes/grove_high_output/(cap_\d+)\.md', d['resumen_teorico']).group(1)
    m = lect.get(i, {})
    faltan += ['%s %d' % (i, k) for k in range(1, n + 1) if k not in m]
    k = collections.Counter(m[j] for j in range(1, n + 1) if j in m)
    t = tot.setdefault(cap, [0, 0, 0]); t[0] += 1; t[1] += n; t[2] += k['P']
    print('%-56s %-7s %5d %3d %3d' % (i, cap, n, k['T'], k['P']))
print('entraron: %d de la tanda de %d | pasos sin fila de lectura: %d %s' % (len(entro), len(tanda), len(faltan), faltan))
print()
print('| capitulo | candidatos que entraron | pasos | PUENTE | por ciento |')
print('|---|---:|---:|---:|---:|')
for cap, (c, n, p) in tot.items():
    print('| `%s` | %d | %d | %d | %s |' % (cap, c, n, p, ('%.2f' % (100.0 * p / n)).replace('.', ',')))
