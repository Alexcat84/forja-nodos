# -*- coding: utf-8 -*-
"""Fase ciega de la 77 (copia libre de .v75aud/orden_grafo.py con la tanda de la 76), sin git y sin abrir nada del
extractor: el orden en que entraron las 22, leido del grafo (src/aduana.py escribe nodos + [nuevo], asi que cada insertar
anade su fila al final y el orden de las filas es el de entrada; .v77aud/grafo_sin_tanda.py comprueba que las 22 son las
ultimas), contra (1) el orden que mi encargo de la 77 pega en su TAREA 4 (bloque de .v76ext/orden.txt, leido de
docs/loop/PROMPT_SIGUIENTE.md, que es mio), y (2) las 16 restricciones de la ACTA 75 75.4, leidas de la lista R de
.v76aud/normal/orden_contra_restricciones.py (importada, no copiada): madre antes que hijo, y D.36 de un solo lado, que
no obliga. Reparte con su suma (R7). NO imprime ninguna clave de relacion (R6): solo ids y posiciones. Solo lee."""
import io, re, sys, json, ast, collections
sys.stdout.reconfigure(encoding="utf-8")
las22 = set(io.open('.v76aud/las22.txt', encoding='utf-8').read().split())
orden = [i for i in (json.loads(l)['id'] for l in io.open('dataset/nodos.jsonl', encoding='utf-8')) if i in las22]
pos = dict((i, n) for n, i in enumerate(orden, 1))
enc = [m.group(1) for m in (re.match(r'^    \d+ +(\S+) +cap_\d+ ', l) for l in io.open('docs/loop/PROMPT_SIGUIENTE.md', encoding='utf-8')) if m]
print('orden de entrada leido del grafo: %d filas | el del bloque de mi encargo: %d filas | fila a fila iguales: %s' % (
    len(orden), len(enc), 'SI' if orden == enc else 'NO'))
for n, i in enumerate(orden, 1): print('  %2d %s' % (n, i))
src = io.open('.v76aud/normal/orden_contra_restricciones.py', encoding='utf-8').read()
R = ast.literal_eval(src[src.index('R = [') + 4:src.index('\n]\n') + 2])
c = collections.Counter()
for a, b, o in R:
    k = 'D.36 de un solo lado' if o.startswith('D.36') else ('cae en la ACTA 75 75.4' if 'cae' in o else 'obliga')
    ok = pos[a] < pos[b]
    c['%s, %s' % (k, 'la cumple' if ok else 'LA VIOLA')] += 1
    print('  %-6s %2d %-52s antes que %2d %-52s %s' % ('cumple' if ok else 'VIOLA', pos[a], a, pos[b], b, o))
print('restricciones: %d | %s | suma: %d' % (len(R), dict(c), sum(c.values())))
