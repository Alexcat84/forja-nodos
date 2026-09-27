# -*- coding: utf-8 -*-
"""Fase ciega de la 72, sin git y sin abrir nada del extractor: el orden en que entraron las 20, leido del grafo
(src/aduana.py escribe dataset_futuro = nodos + [nuevo], asi que cada insertar anade su fila al final y el orden de las
filas es el de entrada; .v72aud/grafo_sin_tanda.py comprueba que las 20 son las ultimas), contra las 12 restricciones que
imprime MI .v71aud/restricciones_orden.py, sellado en la 71. Las 2 restricciones que salian de los dos CONTINUA de
cerrar_brecha_dos_preguntas_estrategia caidos a SANO en la ACTA 70 70.5 ya no obligan, y se dice; se miden igual.
Reparte con su suma (R7). NO imprime ninguna clave de relacion (R6): solo ids y posiciones. Solo lee."""
import io, re, sys, json, subprocess, collections
sys.stdout.reconfigure(encoding="utf-8")
los20 = set(io.open('.v71aud/los20.txt', encoding='utf-8').read().split())
ids = [json.loads(l)['id'] for l in io.open('dataset/nodos.jsonl', encoding='utf-8')]
orden = [i for i in ids if i in los20]
pos = dict((i, n) for n, i in enumerate(orden, 1))
print('orden de entrada leido del grafo: %d filas' % len(orden))
for n, i in enumerate(orden, 1): print('  %2d %s' % (n, i))
sal = subprocess.run([sys.executable, '.v71aud/restricciones_orden.py'], capture_output=True, text=True, encoding='utf-8').stdout
CB = 'cerrar_brecha_dos_preguntas_estrategia'
c = collections.Counter()
for l in sal.splitlines():
    m = re.match(r'^  (\S+) +antes que (\S+) +(CONTINUA|arista por lectura|D\.36)', l)
    if not m: continue
    a, b, por = m.groups()
    if por == 'D.36': k = 'D.36 de un solo lado'
    elif por == 'CONTINUA' and b == CB: k = 'caida a SANO en la ACTA 70 70.5'
    else: k = 'obliga'
    ok = pos[a] < pos[b]
    c['%s, %s' % (k, 'la cumple' if ok else 'LA VIOLA')] += 1
    print('  %-9s %2d %-58s antes que %2d %-60s %s' % ('cumple' if ok else 'VIOLA', pos[a], a, pos[b], b, k))
print('restricciones: %s | suma: %d' % (dict(c), sum(c.values())))
