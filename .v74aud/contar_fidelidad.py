# -*- coding: utf-8 -*-
"""Fase ciega de la 74 (copia de .v73aud/contar_fidelidad.py con las rutas cambiadas y los nodos leidos del GRAFO, porque
los tres de d084 viven en dataset/nodos.jsonl y no en una bandeja): arma .v74aud/fidelidad.tsv desde
.v74aud/fidelidad_fuente.txt (mi lectura ciega, clase T, P o D de duda, con su linea de cap_13) y la cruza con los pasos de
cada nodo en el grafo HOY: una fila por paso escrito, ni mas ni menos, y en orden. Una fila por nodo y el total del capitulo
(8.2), con la suma de cada reparto (R7). Y comprueba cada cita: los tramos de la frase del libro, cortados por los '...',
tienen que estar en su linea de fuentes/scott_radical_candor/cap_13.md (con el apostrofo curvo pasado a recto). No escribe
nada fuera de .v74aud/. Con un fichero de filas como argumento (la mutacion de la seccion 3) lee ese y no escribe el tsv."""
import io, os, json, re, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
CAP = 'fuentes/scott_radical_candor/cap_13.md'
libro = [l.rstrip('\n').replace('’', "'").replace('“', '').replace('”', '') for l in io.open(CAP, encoding='utf-8')]
FUENTE = sys.argv[1] if len(sys.argv) > 1 else '.v74aud/fidelidad_fuente.txt'  # con otro fichero (la mutacion), no escribe el tsv
filas = [l.rstrip('\n').split('|', 4) for l in io.open(FUENTE, encoding='utf-8') if l.strip()]
ids = list(collections.OrderedDict((f[0], 1) for f in filas))
grafo = {}
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l)
    if d['id'] in ids: grafo[d['id']] = len(d['pasos_accionables'])
malas = []
with io.open('.v74aud/fidelidad.tsv' if len(sys.argv) == 1 else os.devnull, 'w', encoding='utf-8', newline='\n') as f:
    f.write('id\tpaso\tclase\tlinea\tlectura\n')
    for i, p, c, L, t in filas:
        f.write('\t'.join([i, p, c, L, t]) + '\n')
        cita = re.split(r' (DUDA, inclinada|PUENTE de clausula)', t)[0]
        linea = libro[int(L[1:]) - 1]
        for tramo in [x.strip(' .?!') for x in cita.split('...')]:
            if tramo and tramo not in linea:
                malas.append((i, p, L, tramo))
print('%-52s %5s %5s %3s %3s %5s %5s' % ('nodo', 'grafo', 'filas', 'T', 'P', 'DUDA', 'suma'))
tot = collections.Counter()
for i in ids:
    fs = [f for f in filas if f[0] == i]
    c = collections.Counter(f[2] for f in fs)
    orden = [int(f[1]) for f in fs] == list(range(1, len(fs) + 1))
    n = grafo.get(i, -1)
    print('%-52s %5d %5d %3d %3d %5d %5d | PUENTE %5.2f por ciento | con las DUDA %5.2f%s' % (i, n, len(fs), c['T'], c['P'], c['D'], c['T'] + c['P'] + c['D'],
                                              100.0 * c['P'] / n, 100.0 * (c['P'] + c['D']) / n, '' if n == len(fs) and orden else '  DESCUADRE'))
    tot['grafo'] += n; tot['filas'] += len(fs); tot['T'] += c['T']; tot['P'] += c['P']; tot['D'] += c['D']
print('cap_13, los tres de d084: pasos en el grafo %d | filas %d | T %d | P %d | DUDA %d | suma: %d | PUENTE %d de %d = %.2f por ciento | si las DUDA cayesen: %d de %d = %.2f por ciento' % (
    tot['grafo'], tot['filas'], tot['T'], tot['P'], tot['D'], tot['T'] + tot['P'] + tot['D'], tot['P'], tot['grafo'],
    100.0 * tot['P'] / tot['grafo'], tot['P'] + tot['D'], tot['grafo'], 100.0 * (tot['P'] + tot['D']) / tot['grafo']))
print('citas comprobadas contra su linea: filas %d | con algun tramo que no esta en su linea: %d' % (len(filas), len(set((m[0], m[1]) for m in malas))))
for m in malas: print('  NO ESTA: %s paso %s %s: %s' % m)
