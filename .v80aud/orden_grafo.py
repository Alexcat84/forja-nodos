# -*- coding: utf-8 -*-
"""Fase ciega de la 80 (copia libre de .v77aud/orden_grafo.py con la tanda de Marquet), sin git y sin abrir nada del
extractor de la 80: el orden en que entraron las 20, leido del grafo (src/aduana.py escribe nodos + [nuevo], asi que cada
insertar anade su fila al final y el orden de las filas es el de entrada; .v80aud/grafo_sin_tanda.py comprueba que las 20
son las ultimas), contra (1) el orden que mi encargo de la 80 pega en su TAREA 3 (bloque de .v78ext/orden.txt, leido de
docs/loop/PROMPT_SIGUIENTE.md, que es mio), y (2) las siete restricciones que mi fase ciega de la 78 sello, leidas de la
salida de .v78aud/restricciones_orden.py corrido ahora (madre antes que hijo, que obliga, y D.36 de un solo lado, que no
obliga). Reparte con su suma (R7). NO imprime ninguna clave de relacion (R6): solo ids y posiciones. Solo lee."""
import io, re, sys, json, subprocess, collections
sys.stdout.reconfigure(encoding="utf-8")
las20 = set(io.open('.v78aud/las20.txt', encoding='utf-8').read().split())
orden = [i for i in (json.loads(l)['id'] for l in io.open('dataset/nodos.jsonl', encoding='utf-8')) if i in las20]
pos = dict((i, n) for n, i in enumerate(orden, 1))
enc = [m.group(1) for m in (re.match(r'^    \d+ +(\S+) +cap_\d+ ', l) for l in io.open('docs/loop/PROMPT_SIGUIENTE.md', encoding='utf-8')) if m]
print('orden de entrada leido del grafo: %d filas | el del bloque de mi encargo: %d filas | fila a fila iguales: %s' % (
    len(orden), len(enc), 'SI' if orden == enc else 'NO'))
for n, i in enumerate(orden, 1): print('  %2d %s' % (n, i))
out = subprocess.run([sys.executable, '.v78aud/restricciones_orden.py'], capture_output=True, text=True, encoding='utf-8').stdout
c = collections.Counter()
for l in out.splitlines():
    m = re.match(r'^\s+(\S+)\s+antes que (\S+)\s+(arista por lectura|CONTINUA|D\.36)', l)
    if not m: continue
    a, b, t = m.groups(); ok = pos[a] < pos[b]
    k = 'D.36 de un solo lado' if t.startswith('D.36') else 'obliga'
    c['%s, %s' % (k, 'la cumple' if ok else 'LA VIOLA')] += 1
    print('  %-6s %2d %-52s antes que %2d %-52s %s' % ('cumple' if ok else 'VIOLA', pos[a], a, pos[b], b, k))
print('restricciones: %d | %s | suma: %d' % (sum(c.values()), dict(c), sum(c.values())))
