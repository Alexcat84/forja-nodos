# -*- coding: utf-8 -*-
"""Fase ciega de la 70: lo que MI lectura sellada de la 68 espera que la insercion de las 20 deje, contado con el
mismo predicado y con su suma (R7). No lee el grafo por dentro, ni la bitacora por dentro, ni nada del extractor.
(1) lineas de veredicto: una por fila dirigida de mi barrido (.v68aud/vecinos_tabla.txt, 'X > Y') cuyo candidato es de
    las 20, porque la poblacion de hoy es la de ese barrido (.v70aud/huellas_hoy.py, grafo_sin_tanda.py, poblacion.py);
(2) aristas: las de .v69aud/aristas_70.py (CONTINUA de mis_clases.tsv y SOSTENGO de aristas_lectura.tsv, con la
    ACTA 67 67.4.d aplicada); las SOSTENGO van con python forja.py arista, que escribe su propia linea en la bitacora
    (src/arista.py), y las CONTINUA ya estan dentro de las lineas de (1);
(3) de esas aristas, cuantas madres son de los 390 que ya vivian: son los nodos viejos que la tanda tiene que reescribir.
Y la cuenta de hoy de la bitacora, solo con wc: 904 era la de mi ACTA 68 68.1. Solo lee."""
import io, re, sys, subprocess, collections
sys.stdout.reconfigure(encoding="utf-8")
los20 = set(io.open('.v68aud/los20.txt', encoding='utf-8').read().split())
fd = collections.Counter()
for l in io.open('.v68aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +> (\S+) ', l)
    if m and m.group(1) in los20: fd['vecino en la tanda' if m.group(2) in los20 else 'vecino fuera de la tanda'] += 1
print('filas dirigidas de mi barrido con candidato de las 20: %d | por vecino: %s | suma: %d' % (sum(fd.values()), dict(fd), sum(fd.values())))
sal = subprocess.run([sys.executable, '.v69aud/aristas_70.py'], capture_output=True, text=True, encoding='utf-8').stdout
ar = [l.split() for l in sal.splitlines() if l.startswith('  CONTINUA') or l.startswith('  SOSTENGO')]
k = collections.Counter(a[0] for a in ar)
print('aristas esperadas: %d | por origen: %s | suma: %d' % (len(ar), dict(k), sum(k.values())))
viejas = sorted(set(a[1] for a in ar if a[1] not in los20))
hijos_viejos = sorted(set(a[3] for a in ar if a[3] not in los20))
print('madres esperadas que no son de las 20 (viven en el grafo desde antes): %d %s' % (len(viejas), viejas))
print('hijos esperados que no son de las 20: %d %s' % (len(hijos_viejos), hijos_viejos))
esp = 904 + sum(fd.values()) + k['SOSTENGO']
hoy = sum(1 for _ in open('bitacora/VEREDICTOS.jsonl', 'rb'))
print('bitacora esperada: 904 + %d + %d = %d | hoy (lineas): %d | %s' % (sum(fd.values()), k['SOSTENGO'], esp, hoy, 'IGUAL' if esp == hoy else 'DISTINTA'))
# (4) las filas dirigidas de (1), por la clase de su par sin orden en .v68aud/mis_clases.tsv, que es la que la conjunta
#     de la 69 dejo igual en los 70 pares (ACTA 68 68.3); es la poblacion de la muestra pineada de los SANO (7).
cl = {}
for l in list(io.open('.v68aud/mis_clases.tsv', encoding='utf-8'))[1:]:
    f = l.rstrip('\n').split('\t'); cl[tuple(sorted((f[0], f[1])))] = f[2]
dc = collections.Counter()
for l in io.open('.v68aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +> (\S+) ', l)
    if m and m.group(1) in los20: dc[cl.get(tuple(sorted(m.groups())), 'SIN FILA')] += 1
print('filas dirigidas por la clase sellada de su par: %s | suma: %d' % (dict(dc), sum(dc.values())))
