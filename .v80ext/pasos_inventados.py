# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 80 de .v77ext/pasos_inventados.py (encargo de la 80, TAREA 5). Lo cambiado, y nada mas: la lectura, que es .v78ext/fidelidad.tsv (la de .v78ext/contar_fidelidad.txt, que la ACTA 77 77.3 firmo con sus PUENTE corregidos en la ficha y 0 que entran); la base, e9d0309, la apertura de la 78, antes de su TAREA 2 que corrigio los P; la bandeja, marquet_turn_the_ship; y la tanda, las filas 1 a 20 de .v78ext/orden.txt. Lo que decia la de la 77: COPIA DE LA VUELTA 77 de .v75ext/pasos_inventados.py, con la lectura .v78ext/fidelidad.tsv, la base 2407dbb, la bandeja marquet_turn_the_ship y la tanda de las filas 1 a 22 de .v76ext/orden.txt. PUENTE que entro = P menos corregidos: para cada P se compara el texto de ese paso en la ficha que ENTRO con el de la base, y un P cuyo texto cambio cuenta como CORREGIDO. PASOS INVENTADOS POR CAPITULO sobre lo que ENTRO: lo que entro se lee de cuarentena/_insertados/<bandeja>/ cruzado con dataset/nodos.jsonl, y los pasos de cada ficha se cuentan de su fichero: cada paso tiene que tener su fila."""
import io, json, re, collections, os
def tsv(ruta):
    m = {}
    for l in io.open(ruta, encoding='utf-8'):
        if not l.strip() or l.startswith('#'): continue
        c = [x.strip() for x in l.split('|')]
        m.setdefault(c[0], {})[int(c[1])] = c[2]
    return m
lect = tsv('.v78ext/fidelidad.tsv')
import subprocess
BASE = 'e9d0309'
viejo = lambda i: json.loads(subprocess.run(['git', 'show', '%s:cuarentena/marquet_turn_the_ship/%s.json' % (BASE, i)], capture_output=True, text=True, encoding='utf-8').stdout)['pasos_accionables']
grafo = set(json.loads(l)['id'] for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip())
tanda = [l.split()[1] for l in io.open('.v78ext/orden.txt', encoding='utf-8') if re.match(r'^\d+\s', l)][0:20]
entro = [i for i in tanda if os.path.exists('cuarentena/_insertados/marquet_turn_the_ship/%s.json' % i) and i in grafo]
tot = collections.OrderedDict(); faltan = []
print('%-60s %-7s %5s %3s %3s %4s' % ('candidato que ENTRO', 'cap', 'pasos', 'T', 'P', 'corr'))
for i in entro:
    d = json.load(io.open('cuarentena/_insertados/marquet_turn_the_ship/%s.json' % i, encoding='utf-8'))
    n = len(d['pasos_accionables'])
    cap = re.search(r'fuentes/marquet_turn_the_ship/(cap_\d+)\.md', d['resumen_teorico']).group(1)
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
