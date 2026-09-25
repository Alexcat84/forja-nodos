# -*- coding: utf-8 -*-
"""Fase ciega de la 70: MI clasificacion de cada una de las 20, sacada solo de mis ficheros sellados de la 68
(.v68aud/los20.txt, fidelidad_fuente.txt, vecinos_tabla.txt, mis_clases.tsv) y de .v69aud/aristas_70.py: capitulo,
lineas del libro que sus pasos transcriben, filas dirigidas de mi barrido, sus pares por clase sellada con su suma (R7),
y las aristas que mi lectura le espera como hija. No lee el grafo, la bitacora ni nada del extractor. Solo lee."""
import io, re, sys, subprocess, collections
sys.stdout.reconfigure(encoding="utf-8")
los20 = io.open('.v68aud/los20.txt', encoding='utf-8').read().split()
L = collections.defaultdict(set)
for l in io.open('.v68aud/fidelidad_fuente.txt', encoding='utf-8'):
    if l.strip():
        f = l.rstrip('\n').split('|', 4)
        for x in re.findall(r'L(\d+)', f[3]): L[f[0]].add(int(x))
fd = collections.Counter()
for l in io.open('.v68aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +> (\S+) ', l)
    if m: fd[m.group(1)] += 1
cl = collections.defaultdict(collections.Counter)
for l in list(io.open('.v68aud/mis_clases.tsv', encoding='utf-8'))[1:]:
    f = l.rstrip('\n').split('\t')
    for x in (f[0], f[1]): cl[x][f[2]] += 1
sal = subprocess.run([sys.executable, '.v69aud/aristas_70.py'], capture_output=True, text=True, encoding='utf-8').stdout
hija = collections.defaultdict(list)
for l in sal.splitlines():
    a = l.split()
    if a and a[0] in ('CONTINUA', 'SOSTENGO'): hija[a[3]].append('%s de %s' % (a[0], a[1]))
for n, i in enumerate(los20, 1):
    ls = sorted(L[i])
    print('%2d %s %-50s NODO | L%s a L%s | filas %d | pares %s suma %d | hija: %s' % (
        n, 'cap_05' if n <= 12 else 'cap_06', i, ls[0], ls[-1], fd[i], dict(cl[i]), sum(cl[i].values()), '; '.join(hija[i]) or 'ninguna'))
