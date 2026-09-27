# -*- coding: utf-8 -*-
"""Vuelve a correr cada comando `$` de docs/loop/APERTURA_CIEGA.md (bloques con 4 o 7 espacios) con bash y
compara su salida con las lineas pegadas debajo hasta el siguiente `$` o el fin del bloque."""
import io, re, subprocess, sys
BASH = sys.argv[1]
L = io.open('docs/loop/APERTURA_CIEGA.md', encoding='utf-8').read().split('\n')
ok = mal = 0; k = 0
while k < len(L):
    m = re.match(r'^( {4}| {7})\$ (.*)$', L[k])
    if not m: k += 1; continue
    ind, cmd = m.group(1), m.group(2); pegado = []; k += 1
    while k < len(L) and L[k].startswith(ind) and not L[k][len(ind):].startswith('$ '):
        pegado.append(L[k][len(ind):]); k += 1
    r = subprocess.run([BASH, '-c', cmd], capture_output=True, text=True, encoding='utf-8')
    sale = (r.stdout + r.stderr).rstrip('\n').split('\n')
    if sale == pegado: ok += 1
    else: mal += 1; print('DISTINTO: %s\n  pegado %r\n  hoy    %r' % (cmd[:100], pegado[:3], sale[:3]))
print('comandos: %d | identicos: %d | distintos: %d' % (ok + mal, ok, mal))
