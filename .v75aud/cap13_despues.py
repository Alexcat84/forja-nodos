# -*- coding: utf-8 -*-
"""Fase ciega de la 75: los tres nodos de cap_13 de scott_radical_candor que la ACTA 73 firmo (d084), HOY, despues de la
TAREA 2. (1) PASOS INVENTADOS de cap_13 despues de la retirada (8, 8.2), desde MI lectura sellada de la 74
(.v74aud/fidelidad.tsv, 70 filas) con las adjudicaciones de la ACTA 73 73.5 aplicadas aqui y declaradas: mis cuatro D caen
a T, y dar_elogio paso 17 pasa de T a P (el 8 ya era P mio); quitadas las filas de los pasos retirados y renumeradas las que
quedan, cada fila se cruza con el paso del grafo de hoy, texto a texto contra el viejo de .v74aud/pasos_tres.txt.
(2) R9 con su letra aplicada a mi propia lectura (ACTA 73 73.11): un grep de clausulas que COMPARAN o CONTRASTAN o que
CALIFICAN LA PRUEBA del libro sobre los pasos de hoy, con su linea del libro de mi fila. Reparte con su suma (R7). NO
imprime ninguna clave de relacion (R6). Solo lee."""
import io, re, json, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
DE = 'dar_elogio_disciplina_igual_critica'
viejos = collections.defaultdict(list); act = None
for l in io.open('.v74aud/pasos_tres.txt', encoding='utf-8'):
    if l.startswith('====='): act = l.split()[1]; continue
    m = re.match(r'^  P(\d+)\. (.*)$', l.rstrip('\n'))
    if m: viejos[act].append(m.group(2))
filas = [l.rstrip('\n').split('\t') for l in list(io.open('.v74aud/fidelidad.tsv', encoding='utf-8'))[1:] if l.strip()]
ids = list(collections.OrderedDict((f[0], 1) for f in filas))
grafo = dict((d['id'], d) for d in map(json.loads, io.open('dataset/nodos.jsonl', encoding='utf-8')) if d['id'] in ids)
adj = collections.Counter(); porn = {}; mal = 0
for f in filas:
    i, p, c = f[0], int(f[1]), f[2]
    if c == 'D': c = 'T'; adj['D a T (73.5)'] += 1
    if i == DE and p == 17 and c == 'T': c = 'P'; adj['dar_elogio 17, T a P (73.5)'] += 1
    f[2] = c
print('adjudicaciones de la ACTA 73 73.5 aplicadas: %s | suma: %d' % (dict(adj), sum(adj.values())))
TOT = collections.Counter(); r9 = []
PAT = re.compile(r"(\by (?:el|la|los|las|lo) \w+ no\b|\by \w+ no\b|\bmas que\b|\bmenos que\b|\bmejor que\b|\bpeor que\b|a diferencia de|en cambio|mientras que|\bsino\b|\bno solo\b|\bcompar\w*|ha medido|\bmedid\w*|\bmide\b|demostr\w*|demuestr\w*|\bprobad\w*|\bprueba\w*|estudios?\b|investigaci\w*|\bdatos\b|esta probado|\b(?:pesa|importa|vale)\w* mas\b)", re.I)
for i in ids:
    mias = [f for f in filas if f[0] == i]
    fuera = (8, 17) if i == DE else ()
    quedan = [f for f in mias if int(f[1]) not in fuera]
    hoy = grafo[i]['pasos_accionables']
    ok = len(quedan) == len(hoy) and all(hoy[n] == viejos[i][int(f[1]) - 1] for n, f in enumerate(quedan))
    k = collections.Counter(f[2] for f in quedan)
    for c in ('T', 'P'): TOT[c] += k[c]
    print('%-52s pasos hoy %2d | mis filas que quedan %2d, cada una su paso de hoy texto a texto: %s | por marca: %s | suma: %d | PUENTE %d de %d' % (
        i, len(hoy), len(quedan), 'SI' if ok else 'NO', dict(k), sum(k.values()), k['P'], len(hoy)))
    for n, f in enumerate(quedan, 1):
        for m in PAT.finditer(hoy[n - 1]):
            a = max(0, m.start() - 70); r9.append((i, n, int(f[1]), f[3], hoy[n - 1][a:m.end() + 50].replace('\n', ' ')))
print('cap_13, los tres, despues de la TAREA 2: pasos %d | por marca: %s | suma: %d | PUENTE %d de %d = %.2f por ciento' % (
    sum(TOT.values()), dict(TOT), sum(TOT.values()), TOT['P'], sum(TOT.values()), 100.0 * TOT['P'] / sum(TOT.values())))
print('R9, clausulas que comparan o califican la prueba en los pasos de hoy: %d coincidencias' % len(r9))
for i, n, v, L, t in r9: print('  %s paso %d (viejo %d) %s: ...%s...' % (i[:24], n, v, L, t))
