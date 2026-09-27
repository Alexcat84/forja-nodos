# -*- coding: utf-8 -*-
"""Una fila por candidato de la tanda: capitulo y pieza (.v64ext/los22.txt), pasos y PUENTE adjudicados
(.v65aud/entra_lo_leido.txt), vecinos de mi barrido y cuantos con linea adjudicada (.v65aud/cruce_barrido.txt),
filas con mi lectura ciega y su clase (.v65aud/clases_48.txt), y aristas vivas del grafo en las que es madre o
hijo (.v65aud/aristas.txt). Solo junta salidas ya guardadas: no mide nada nuevo."""
import io, re, collections
los22 = [l.split() for l in io.open('.v64ext/los22.txt', encoding='utf-8') if l.strip() and not l.startswith('#')][:20]
ent = {}
for l in io.open('.v65aud/entra_lo_leido.txt', encoding='utf-8'):
    m = re.match(r'(\S+)\s+cap_\d+ \S+\s+leida en (\S+) pasos\s+(\d+) P (\d+)', l)
    if m: ent[m.group(1)] = (m.group(2), int(m.group(3)), int(m.group(4)))
bar = {}
for l in io.open('.v65aud/cruce_barrido.txt', encoding='utf-8'):
    m = re.match(r'(\S+)\s+pob \d+ barrido\s+(\d+) \| con linea\s+(\d+) \| sin linea\s+(\d+)', l)
    if m: bar[m.group(1)] = tuple(int(x) for x in m.group(2, 3, 4))
ciega = collections.Counter()
for l in io.open('.v65aud/clases_48.txt', encoding='utf-8'):
    m = re.match(r'CIEGA\s+(\S+)\s+\S+\s+(\S+) -> (\S+)', l)
    if m: ciega[m.group(2)] += 1
ari = collections.Counter()
for l in io.open('.v65aud/aristas.txt', encoding='utf-8'):
    m = re.match(r'VIVE\s+(\S+)\s+-> (\S+)', l)
    if m: ari[m.group(1)] += 1; ari[m.group(2)] += 1
print('| linea de los22 | candidato | cap | pieza | leida en | pasos | PUENTE | vecinos hoy | con linea | sin linea | filas mias ciegas | aristas vivas |')
print('|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|')
for n, (i, c, p) in enumerate(los22, 1):
    e = ent[i]; b = bar[i]
    print('| %d | `%s` | `%s` | %s | `%s` | %d | %d | %d | %d | %d | %d | %d |' % (n, i, c, p, e[0], e[1], e[2], b[0], b[1], b[2], ciega[i], ari[i]))
