# -*- coding: utf-8 -*-
"""Fase ciega de la 65: los PARES (candidato, vecino) que la bitacora gano desde 997054d, cruzados con
los pares de .v64ext/veredictos_listos.txt de las filas 1 a 20. SOLO IDS Y FECHA: no imprime ni el
veredicto, ni la razon, ni la arista, para que mi clase de los pares nuevos siga siendo ciega (1.2)."""
import io, json, re, subprocess
git = lambda *a: subprocess.run(['git'] + list(a), capture_output=True, text=True, encoding='utf-8').stdout
antes = len(git('show', '997054d:bitacora/VEREDICTOS.jsonl').splitlines())
todas = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8')]
nuevas = todas[antes:]
tanda = [l.split()[1] for l in io.open('.v64ext/orden.txt', encoding='utf-8') if l[:1].isdigit() and 1 <= int(l.split()[0]) <= 20]
listos = set(); cand = None
for l in io.open('.v64ext/veredictos_listos.txt', encoding='utf-8'):
    if l.startswith('## '): cand = l[3:].strip(); continue
    m = re.match(r'(\w+)\|', l)
    if m and cand in tanda: listos.add((cand, m.group(1)))
bit = [(r['candidato'], r['vecino']) for r in nuevas]
print('lineas de la bitacora en 997054d: %d | hoy: %d | nuevas: %d' % (antes, len(todas), len(nuevas)))
print('fechas de las nuevas: %s' % sorted(set(r.get('fecha') for r in nuevas)))
print('candidatos de las nuevas fuera de la tanda: %s' % sorted(set(c for c, v in bit) - set(tanda)))
rep = [p for p in set(bit) if bit.count(p) > 1]
print('pares repetidos en las nuevas: %d %s' % (len(rep), rep))
print('pares listos de las filas 1 a 20: %d' % len(listos))
for p in sorted(set(bit) - listos): print('  EN LA BITACORA Y NO EN LOS LISTOS  %s | %s' % p)
for p in sorted(listos - set(bit)): print('  EN LOS LISTOS Y NO EN LA BITACORA  %s | %s' % p)
print('en los dos: %d | solo bitacora: %d | solo listos: %d' % (len(set(bit) & listos), len(set(bit) - listos), len(listos - set(bit))))
