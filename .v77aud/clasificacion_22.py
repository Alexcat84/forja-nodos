# -*- coding: utf-8 -*-
"""Fase ciega de la 77 (copia libre de .v75aud/clasificacion_7.py con la tanda de la 76): MI clasificacion de cada una
de las 22, sacada solo de mis ficheros sellados de la 76 (.v76aud/las22.txt, fidelidad.tsv, vecinos_tabla.txt,
mis_clases.tsv) con la adjudicacion (i) de la ACTA 75 75.4 que aplica .v77aud/esperado_77.py, y de las aristas que ese
mismo instrumento imprime: capitulo, lineas del libro que sus pasos transcriben, filas dirigidas de mi barrido en que es
candidata, sus pares sin orden por clase con su suma (R7; cuenta los pares en que esta de cualquiera de los dos lados, y
por eso puede pasar de sus filas), y las aristas que mi lectura le espera como hija y cuantas como madre. En el orden de
entrada de .v77aud/orden_grafo.py. No lee la bitacora ni nada del extractor. Solo lee."""
import io, re, sys, subprocess, collections
sys.stdout.reconfigure(encoding="utf-8")
orden = [m.group(1) for m in (re.match(r'^ +\d+ (\S+)$', l) for l in subprocess.run([sys.executable, '.v77aud/orden_grafo.py'], capture_output=True, text=True, encoding='utf-8').stdout.splitlines()) if m]
L = collections.defaultdict(set); cap = {}
for l in list(io.open('.v76aud/fidelidad.tsv', encoding='utf-8'))[1:]:
    if l.strip():
        f = l.rstrip('\n').split('\t'); cap[f[0]] = f[3]
        for x in re.findall(r'L(\d+)', f[4]): L[f[0]].add(int(x))
fd = collections.Counter()
for l in io.open('.v76aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +> (\S+) ', l)
    if m: fd[m.group(1)] += 1
RC = tuple(sorted(('recorrer_siete_pasos_programa_desarrollo_negocio', 'construir_estrategia_gente_cuatro_componentes')))
cl = collections.defaultdict(collections.Counter)
for l in list(io.open('.v76aud/mis_clases.tsv', encoding='utf-8'))[1:]:
    f = l.rstrip('\n').split('\t')
    c = 'SANO' if tuple(sorted((f[0], f[1]))) == RC else f[2]
    for x in (f[0], f[1]): cl[x][c] += 1
sal = subprocess.run([sys.executable, '.v77aud/esperado_77.py'], capture_output=True, text=True, encoding='utf-8').stdout
hija = collections.defaultdict(list); madre = collections.Counter()
for l in sal.splitlines():
    m = re.match(r'^  (CONTINUA|LECTURA) +(\S+) > (\S+)$', l)
    if m: hija[m.group(3)].append('%s de %s' % (m.group(1), m.group(2))); madre[m.group(2)] += 1
for n, i in enumerate(orden, 1):
    ls = sorted(L[i])
    print('%2d %s %-52s NODO | L%s a L%s | filas %d | pares %s suma %d | hija: %s | madre de: %d' % (
        n, cap[i], i, ls[0], ls[-1], fd[i], dict(cl[i]), sum(cl[i].values()), '; '.join(hija[i]) or 'ninguna', madre[i]))
