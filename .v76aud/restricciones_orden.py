# -*- coding: utf-8 -*-
"""Fase ciega de la 76 (copia de .v73aud/restricciones_orden.py con la tanda cambiada): las restricciones de orden que MI
lectura pone a la insercion de las 7, escritas antes de ver el orden del extractor. (a) madre antes que hijo (D.29, D.36)
por mis CONTINUA de .v76aud/mis_clases.tsv y mis SOSTENGO de .v76aud/aristas_lectura.tsv con los dos extremos en la tanda;
(b) D.36: par de la tanda que el barrido levanta desde un solo lado; se publica aparte y NO obliga, porque la aduana de
insertar mide grafo mas bandejas (D.38.5). Y cuantas viola el orden de pieza del libro, que aqui NO es el de
.v76aud/las22.txt (esa lista va por capitulo y alfabetica): lo tomo por capitulo y primera linea de mi fidelidad
(.v76aud/fidelidad_fuente.txt). Solo lee."""
import io, re, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
tanda = [l.strip() for l in io.open('.v76aud/las22.txt', encoding='utf-8') if l.strip()]
cap = dict((l.split()[1], l.split()[0]) for l in io.open('.v76aud/bandeja_gerber.txt', encoding='utf-8') if l.startswith('cap_'))
primera = collections.defaultdict(lambda: 10 ** 6)
for l in io.open('.v76aud/fidelidad_fuente.txt', encoding='utf-8'):
    if l.strip():
        i, p, c, L, t = l.split('|', 4); primera[i] = min(primera[i], int(L[1:]))
libro = sorted(tanda, key=lambda i: (cap[i], primera[i]))
print('orden de pieza del libro (capitulo y primera linea de mi fidelidad): %d' % len(libro))
for n, i in enumerate(libro, 1): print('  %2d %s L%d %s' % (n, cap[i], primera[i], i))
dentro = set(tanda); antes = []
for f in [l.rstrip('\n').split('\t') for l in io.open('.v76aud/mis_clases.tsv', encoding='utf-8')][1:]:
    if f[2] == 'CONTINUA' and f[0] in dentro and f[1] in dentro:
        hijo = f[1] if f[3] == f[0] else f[0]
        antes.append((f[3], hijo, 'CONTINUA'))
for f in [l.rstrip('\n').split('\t') for l in io.open('.v76aud/aristas_lectura.tsv', encoding='utf-8')][1:]:
    if f[2].startswith('SOSTENGO') and f[0] in dentro and f[1] in dentro and (f[0], f[1], 'CONTINUA') not in antes:
        antes.append((f[0], f[1], 'arista por lectura'))
for l in io.open('.v76aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +~ (\S+) +tanda-tanda solo (\S+)', l)
    if m:
        a, b, lado = m.groups(); otro = b if lado == a else a
        antes.append((otro, lado, 'D.36, solo lo levanta %s' % lado))
pos = dict((i, n) for n, i in enumerate(libro))
print('restricciones: %d' % len(antes))
for a, b, por in antes:
    print('  %-58s antes que %-60s %-22s %s' % (a, b, por, 'el orden del libro la cumple' if pos[a] < pos[b] else 'EL ORDEN DEL LIBRO LA VIOLA'))
oblig = [r for r in antes if not r[2].startswith('D.36')]
print('que obligan (madre antes que hijo): %d | violadas por el orden del libro: %d' % (len(oblig), sum(pos[a] > pos[b] for a, b, _ in oblig)))
print('D.36 de un solo lado, informativas: %d' % (len(antes) - len(oblig)))
