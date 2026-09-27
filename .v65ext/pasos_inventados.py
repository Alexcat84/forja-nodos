# -*- coding: utf-8 -*-
"""PASOS INVENTADOS POR CAPITULO sobre lo que ENTRO en la vuelta 65 (encargo, TAREA 4), contado desde las
lecturas enteras YA ADJUDICADAS, no desde cero:
  - los 16 de la 63: .v63aud/fidelidad.tsv (apertura sellada del auditor), con las dos adjudicaciones de la
    ACTA 62: 62.5 D1 CAE (equilibrar pasos 2 a 5, la clausula `apunta su coste`, cuentan PUENTE) y la duda
    ciega de detectar paso 1 cerrada TRANSCRIPCION. Da la tabla de 62.6: cap_02 4 de 50, cap_03 0 de 80.
  - los seis de d005: .v64ext/fidelidad.tsv, que la ACTA 63 63.3.a y 63.5 adjudica entera (2 de 41).
Lo que entro se lee de cuarentena/_insertados/grove_high_output/ cruzado con dataset/nodos.jsonl, y los pasos
de cada ficha se cuentan de su fichero: cada paso tiene que tener su fila."""
import io, json, re, collections, glob, os
def tsv(ruta):
    m = {}
    for l in io.open(ruta, encoding='utf-8'):
        if not l.strip() or l.startswith('#'): continue
        c = [x.strip() for x in l.split('|')]
        m.setdefault(c[0], {})[int(c[1])] = c[2]
    return m
lect = tsv('.v63aud/fidelidad.tsv')
for k in (2, 3, 4, 5): lect['equilibrar_capacidad_personal_inventario_plazo'][k] = 'P'   # ACTA 62 62.5, D1 CAE
lect['detectar_arreglar_fallo_etapa_menor_valor'][1] = 'T'                                 # ACTA 62 62.5, duda cerrada
lect.update(tsv('.v64ext/fidelidad.tsv'))                                                  # ACTA 63 63.3.a y 63.5
grafo = set(json.loads(l)['id'] for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip())
tanda = [l.split()[1] for l in io.open('.v65ext/orden.txt', encoding='utf-8') if re.match(r'^\d+\s', l)][:20]
entro = [i for i in tanda if os.path.exists('cuarentena/_insertados/grove_high_output/%s.json' % i) and i in grafo]
tot = collections.OrderedDict(); faltan = []
print('%-50s %-7s %5s %3s %3s' % ('candidato que ENTRO', 'cap', 'pasos', 'T', 'P'))
for i in entro:
    d = json.load(io.open('cuarentena/_insertados/grove_high_output/%s.json' % i, encoding='utf-8'))
    n = len(d['pasos_accionables'])
    cap = re.search(r'fuentes/grove_high_output/(cap_\d+)\.md', d['resumen_teorico']).group(1)
    m = lect.get(i, {})
    faltan += ['%s %d' % (i, k) for k in range(1, n + 1) if k not in m]
    k = collections.Counter(m[j] for j in range(1, n + 1) if j in m)
    t = tot.setdefault(cap, [0, 0, 0]); t[0] += 1; t[1] += n; t[2] += k['P']
    print('%-50s %-7s %5d %3d %3d' % (i, cap, n, k['T'], k['P']))
print('entraron: %d de la tanda de %d | pasos sin fila de lectura: %d %s' % (len(entro), len(tanda), len(faltan), faltan))
print()
print('| capitulo | candidatos que entraron | pasos | PUENTE | por ciento |')
print('|---|---:|---:|---:|---:|')
for cap, (c, n, p) in tot.items():
    print('| `%s` | %d | %d | %d | %s |' % (cap, c, n, p, ('%.2f' % (100.0 * p / n)).replace('.', ',')))
