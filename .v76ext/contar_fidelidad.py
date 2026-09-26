# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 76 de .v73ext/contar_fidelidad.py, con la ruta cambiada a .v76ext/fidelidad.tsv y a
cuarentena/gerber_emyth/, y el rotulo a las 22 de Gerber; nada mas cambiado. El capitulo de cada ficha es el de su UNIDAD DE
ORIGEN (la primera cita de fuentes/gerber_emyth/cap_NN.md de su resumen_teorico). Lo que decia la de la 73:
COPIA DE LA VUELTA 73 de .v71ext/contar_fidelidad.py, con la ruta cambiada a .v73ext/fidelidad.tsv y el rotulo a las 7 de
cap_15 a cap_17; nada mas cambiado. Lo que decia la de la 71: COPIA DE LA VUELTA 71 de .v68ext/contar_fidelidad.py, con la ruta cambiada a .v71ext/fidelidad.tsv, el rotulo a las 20
de cap_07 a cap_14, la columna del id ensanchada a 60 y, al final, la linea que nombra el peor capitulo (encargo TAREA 2.3,
8.2), calculada y no tecleada. Lo que decia la de la 68: COPIA DE LA VUELTA 68 de .v66ext/contar_fidelidad.py, con la ruta
cambiada a .v68ext/fidelidad.tsv y el rotulo a los 20 de cap_05 y cap_06; nada mas cambiado.
Cuenta la relectura de .v68ext/fidelidad.tsv contra las fichas de la bandeja: cada paso de
cada ficha tiene que tener su fila y ninguna fila puede sobrar. Los pasos se cuentan del
fichero, no a ojo. Imprime por candidato y por capitulo T y P, y el por ciento."""
import io, json, re, collections
filas = [[c.strip() for c in l.rstrip('\n').split('|')]
         for l in io.open('.v76ext/fidelidad.tsv', encoding='utf-8') if l.strip() and not l.startswith('#')]
por_id = collections.OrderedDict()
for f in filas:
    por_id.setdefault(f[0], {})[int(f[1])] = f[2]
faltan, sobran, cap = [], [], {}
print('%-60s %-7s %5s %3s %3s' % ('candidato', 'cap', 'pasos', 'T', 'P'))
for i, m in por_id.items():
    d = json.load(io.open('cuarentena/gerber_emyth/%s.json' % i, encoding='utf-8'))
    n = len(d['pasos_accionables'])
    cap[i] = re.search(r'fuentes/gerber_emyth/(cap_\d+)\.md', d['resumen_teorico']).group(1)
    faltan += ['%s %d' % (i, k) for k in range(1, n + 1) if k not in m]
    sobran += ['%s %d' % (i, k) for k in m if k > n]
    k = collections.Counter(m.values())
    print('%-60s %-7s %5d %3d %3d' % (i, cap[i], n, k['T'], k['P']))
print('pasos sin fila: %d %s | filas sin paso: %d %s' % (len(faltan), faltan, len(sobran), sobran))
print()
print('PASOS INVENTADOS POR CAPITULO, las 22 de Gerber (COPIA de la vuelta 76 de .v73ext/contar_fidelidad.py, ruta cambiada)')
peor = []
for c in sorted(set(cap.values())):
    ids = [i for i in cap if cap[i] == c]
    k = collections.Counter(v for i in ids for v in por_id[i].values())
    n = sum(len(por_id[i]) for i in ids)
    print('%-7s candidatos %d  pasos %d  T %d  P %d  inventado %s por ciento' % (
        c, len(ids), n, k['T'], k['P'], ('%.1f' % (100.0 * k['P'] / n)).replace('.', ',')))
    peor.append((100.0 * k['P'] / n, c, k['P'], n))
p = max(peor)
print('peor capitulo: %s, %d de %d, %s por ciento; por encima del 10: %s' % (p[1], p[2], p[3], ('%.1f' % p[0]).replace('.', ','),
      ', '.join(c for x, c, _, _ in sorted(peor) if x > 10) or 'ninguno'))
