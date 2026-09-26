# -*- coding: utf-8 -*-
"""Fase ciega de la 75 (copia libre de .v72aud/orden_grafo.py con la tanda de la 73), sin git y sin abrir nada del
extractor: el orden en que entraron las 7, leido del grafo (src/aduana.py escribe nodos + [nuevo], asi que cada insertar
anade su fila al final y el orden de las filas es el de entrada; .v75aud/grafo_sin_tanda.py comprueba que las 7 son las
ultimas), contra las 5 restricciones que imprime MI .v73aud/restricciones_orden.py, sellado en la 73. La que salia de mi
CONTINUA de priorizar_lista a pedir_critica_anonima, caido a SANO en la ACTA 72 72.5 (D73.9), ya no obliga, y se dice; se
mide igual. Y el orden de entrada contra el orden de pieza del libro que ese mismo instrumento imprime. Reparte con su suma
(R7). NO imprime ninguna clave de relacion (R6): solo ids y posiciones. Solo lee."""
import io, re, sys, json, subprocess, collections
sys.stdout.reconfigure(encoding="utf-8")
los7 = set(io.open('.v73aud/los7.txt', encoding='utf-8').read().split())
ids = [json.loads(l)['id'] for l in io.open('dataset/nodos.jsonl', encoding='utf-8')]
orden = [i for i in ids if i in los7]
pos = dict((i, n) for n, i in enumerate(orden, 1))
print('orden de entrada leido del grafo: %d filas' % len(orden))
for n, i in enumerate(orden, 1): print('  %2d %s' % (n, i))
sal = subprocess.run([sys.executable, '.v73aud/restricciones_orden.py'], capture_output=True, text=True, encoding='utf-8').stdout
libro = [m.group(1) for m in (re.match(r'^ +\d+ cap_\d+ L\d+ (\S+)$', l) for l in sal.splitlines()) if m]
print('el orden de entrada es el orden de pieza del libro de mi instrumento sellado: %s' % ('SI' if libro == orden else 'NO'))
C = ('priorizar_lista_entrenamiento_subordinados', 'pedir_critica_anonima_curso_entrenamiento_dictado')
c = collections.Counter()
for l in sal.splitlines():
    m = re.match(r'^  (\S+) +antes que (\S+) +(CONTINUA|arista por lectura|D\.36)', l)
    if not m: continue
    a, b, por = m.groups()
    if por == 'D.36': k = 'D.36 de un solo lado'
    elif (a, b) == C: k = 'caida a SANO en la ACTA 72 72.5'
    else: k = 'obliga'
    ok = pos[a] < pos[b]
    c['%s, %s' % (k, 'la cumple' if ok else 'LA VIOLA')] += 1
    print('  %-9s %d %-52s antes que %d %-52s %s' % ('cumple' if ok else 'VIOLA', pos[a], a, pos[b], b, k))
print('restricciones: %s | suma: %d' % (dict(c), sum(c.values())))
