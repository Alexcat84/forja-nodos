# -*- coding: utf-8 -*-
"""Cuenta la relectura de .v66ext/fidelidad.tsv contra las fichas de la bandeja: cada paso de
cada ficha tiene que tener su fila y ninguna fila puede sobrar. Los pasos se cuentan del
fichero, no a ojo. Imprime por candidato y por capitulo T y P, y el por ciento."""
import io, json, re, collections
filas = [[c.strip() for c in l.rstrip('\n').split('|')]
         for l in io.open('.v66ext/fidelidad.tsv', encoding='utf-8') if l.strip() and not l.startswith('#')]
por_id = collections.OrderedDict()
for f in filas:
    por_id.setdefault(f[0], {})[int(f[1])] = f[2]
faltan, sobran, cap = [], [], {}
print('%-48s %-7s %5s %3s %3s' % ('candidato', 'cap', 'pasos', 'T', 'P'))
for i, m in por_id.items():
    d = json.load(io.open('cuarentena/grove_high_output/%s.json' % i, encoding='utf-8'))
    n = len(d['pasos_accionables'])
    cap[i] = re.search(r'fuentes/grove_high_output/(cap_\d+)\.md', d['resumen_teorico']).group(1)
    faltan += ['%s %d' % (i, k) for k in range(1, n + 1) if k not in m]
    sobran += ['%s %d' % (i, k) for k in m if k > n]
    k = collections.Counter(m.values())
    print('%-48s %-7s %5d %3d %3d' % (i, cap[i], n, k['T'], k['P']))
print('pasos sin fila: %d %s | filas sin paso: %d %s' % (len(faltan), faltan, len(sobran), sobran))
print()
print('PASOS INVENTADOS POR CAPITULO, los 22 de cap_04 (COPIA de la vuelta 66 de .v64ext/contar_fidelidad.py, ruta cambiada)')
for c in sorted(set(cap.values())):
    ids = [i for i in cap if cap[i] == c]
    k = collections.Counter(v for i in ids for v in por_id[i].values())
    n = sum(len(por_id[i]) for i in ids)
    print('%-7s candidatos %d  pasos %d  T %d  P %d  inventado %s por ciento' % (
        c, len(ids), n, k['T'], k['P'], ('%.1f' % (100.0 * k['P'] / n)).replace('.', ',')))
