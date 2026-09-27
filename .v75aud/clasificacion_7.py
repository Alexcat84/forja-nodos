# -*- coding: utf-8 -*-
"""Fase ciega de la 75 (copia libre de .v72aud/clasificacion_20.py con la tanda de la 73): MI clasificacion de cada una
de las 7, sacada solo de mis ficheros sellados de la 73 (.v73aud/los7.txt, fidelidad_fuente.txt, vecinos_tabla.txt,
mis_clases.tsv) con la correccion de la ACTA 72 72.5 (D73.9) que aplica .v75aud/esperado_75.py, y de las aristas que ese
mismo instrumento imprime: capitulo, lineas del libro que sus pasos transcriben, filas dirigidas de mi barrido en que es
candidata, sus pares sin orden por clase con su suma (R7; cuenta los pares en que esta de cualquiera de los dos lados, y
por eso puede pasar de sus filas), y las aristas que mi lectura le espera como hija y como madre. No lee la bitacora ni
nada del extractor. Solo lee."""
import io, re, sys, subprocess, collections
sys.stdout.reconfigure(encoding="utf-8")
los7 = [l.strip() for l in io.open('.v73aud/los7.txt', encoding='utf-8') if l.strip()]
cap = dict((l.split()[1], l.split()[0]) for l in io.open('.v72aud/normal/siete.txt', encoding='utf-8') if l.startswith('cap_'))
L = collections.defaultdict(set)
for l in io.open('.v73aud/fidelidad_fuente.txt', encoding='utf-8'):
    if l.strip():
        f = l.rstrip('\n').split('|', 4)
        for x in re.findall(r'L(\d+)', f[3]): L[f[0]].add(int(x))
fd = collections.Counter()
for l in io.open('.v73aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +> (\S+) ', l)
    if m: fd[m.group(1)] += 1
CORR = tuple(sorted(('priorizar_lista_entrenamiento_subordinados', 'pedir_critica_anonima_curso_entrenamiento_dictado')))
cl = collections.defaultdict(collections.Counter)
for l in list(io.open('.v73aud/mis_clases.tsv', encoding='utf-8'))[1:]:
    f = l.rstrip('\n').split('\t')
    c = 'SANO' if tuple(sorted((f[0], f[1]))) == CORR else f[2]
    for x in (f[0], f[1]): cl[x][c] += 1
sal = subprocess.run([sys.executable, '.v75aud/esperado_75.py'], capture_output=True, text=True, encoding='utf-8').stdout
hija = collections.defaultdict(list); madre = collections.defaultdict(list)
for l in sal.splitlines():
    m = re.match(r'^  (\S+) > (\S+)$', l)
    if m: hija[m.group(2)].append('CONTINUA de %s' % m.group(1)); madre[m.group(1)].append(m.group(2))
for n, i in enumerate(los7, 1):
    ls = sorted(L[i])
    print('%d %s %-50s NODO | L%s a L%s | filas %d | pares %s suma %d | hija: %s | madre de: %d' % (
        n, cap[i], i, ls[0], ls[-1], fd[i], dict(cl[i]), sum(cl[i].values()), '; '.join(hija[i]) or 'ninguna', len(madre[i])))
