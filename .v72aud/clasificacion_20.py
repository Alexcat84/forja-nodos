# -*- coding: utf-8 -*-
"""Fase ciega de la 72 (copia libre de .v70aud/clasificacion_20.py con la tanda de la 71): MI clasificacion de cada una
de las 20, sacada solo de mis ficheros sellados de la 71 (.v71aud/los20.txt, fidelidad_fuente.txt, vecinos_tabla.txt,
mis_clases.tsv) con la correccion de la ACTA 70 70.5 que aplica .v72aud/esperado_72.py, y de las aristas que ese mismo
instrumento imprime: capitulo, lineas del libro que sus pasos transcriben, filas dirigidas de mi barrido en que es
candidata, sus pares sin orden por clase con su suma (R7; cuenta los pares en que esta de cualquiera de los dos lados, y
por eso puede pasar de sus filas), y las aristas que mi lectura le espera como hija y como madre. No lee el grafo, la
bitacora ni nada del extractor. Solo lee."""
import io, re, sys, subprocess, collections
sys.stdout.reconfigure(encoding="utf-8")
los20 = io.open('.v71aud/los20.txt', encoding='utf-8').read().split()
cap = dict((l.split()[1], l.split()[0]) for l in io.open('.v70aud/normal/bandeja_grove.txt', encoding='utf-8') if l.strip())
L = collections.defaultdict(set)
for l in io.open('.v71aud/fidelidad_fuente.txt', encoding='utf-8'):
    if l.strip():
        f = l.rstrip('\n').split('|', 4)
        for x in re.findall(r'L(\d+)', f[3]): L[f[0]].add(int(x))
fd = collections.Counter()
for l in io.open('.v71aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +> (\S+) ', l)
    if m: fd[m.group(1)] += 1
CB = 'cerrar_brecha_dos_preguntas_estrategia'
CORR = set(tuple(sorted((CB, x))) for x in ('examinar_demanda_entorno_dos_marcos_temporales', 'determinar_estado_presente_capacidades_proyectos_merma'))
cl = collections.defaultdict(collections.Counter)
for l in list(io.open('.v71aud/mis_clases.tsv', encoding='utf-8'))[1:]:
    f = l.rstrip('\n').split('\t')
    c = 'SANO' if tuple(sorted((f[0], f[1]))) in CORR else f[2]
    for x in (f[0], f[1]): cl[x][c] += 1
sal = subprocess.run([sys.executable, '.v72aud/esperado_72.py'], capture_output=True, text=True, encoding='utf-8').stdout
hija = collections.defaultdict(list); madre = collections.defaultdict(list)
for l in sal.splitlines():
    m = re.match(r'^  (CONTINUA|SOSTENGO D\.\d+) +(\S+) > (\S+)$', l)
    if m: hija[m.group(3)].append('%s de %s' % (m.group(1), m.group(2))); madre[m.group(2)].append(m.group(3))
for n, i in enumerate(los20, 1):
    ls = sorted(L[i])
    print('%2d %s %-58s NODO | L%s a L%s | filas %d | pares %s suma %d | hija: %s | madre de: %d' % (
        n, cap[i], i, ls[0], ls[-1], fd[i], dict(cl[i]), sum(cl[i].values()), '; '.join(hija[i]) or 'ninguna', len(madre[i])))
