# -*- coding: utf-8 -*-
"""Fase ciega de la 69: las aristas que MI lectura espera que la 70 cree al insertar los 20 de cap_05 y cap_06, y
las que no, contadas con el mismo predicado y con su suma (R7). Dos fuentes, las dos mias y selladas en la 68:
(a) los pares CONTINUA de .v68aud/mis_clases.tsv que tocan a los 20 (una arista por par, con madre=);
(b) las filas de .v68aud/aristas_lectura.tsv, por su clase SIN la marca de duda (SOSTENGO, NO, EN VEREDICTO).
Y UNA SOLA CORRECCION, DECLARADA: la fila agrupar_tareas > infundir, que la tsv dice NO, DUDA, la adjudique SOSTENGO
en la ACTA 67 67.4.d (gana el extractor, dentro de mi duda). Se aplica aqui y la tsv sellada no se toca. Solo lee."""
import io, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
los20 = set(io.open('.v68aud/los20.txt', encoding='utf-8').read().split())
ADJ = {('agrupar_tareas_semejantes_aprovechar_preparacion', 'infundir_regularidad_reunion_proceso'): 'SOSTENGO'}
cls = [l.rstrip('\n').split('\t') for l in io.open('.v68aud/mis_clases.tsv', encoding='utf-8')][1:]
cont = [(f[3], f[1] if f[3] == f[0] else f[0]) for f in cls if f[2] == 'CONTINUA' and (f[0] in los20 or f[1] in los20)]
ar = [l.rstrip('\n').split('\t') for l in io.open('.v68aud/aristas_lectura.tsv', encoding='utf-8')][1:]
def clase(f):
    return ADJ.get((f[0], f[1]), f[2].split(',')[0].strip())
c = collections.Counter(clase(f) for f in ar)
print('filas de aristas_lectura.tsv: %d | por clase (sin la marca DUDA, con ACTA 67 67.4.d aplicada): %s | suma: %d' % (len(ar), dict(c), sum(c.values())))
sost = [(f[0], f[1]) for f in ar if clase(f) == 'SOSTENGO']
print('aristas esperadas en la 70: %d | por origen: %s | suma: %d' % (len(cont) + len(sost), {'CONTINUA de veredicto': len(cont), 'SOSTENGO por lectura': len(sost)}, len(cont) + len(sost)))
for m, h in cont: print('  CONTINUA   %-52s > %s' % (m, h))
for m, h in sost: print('  SOSTENGO   %-52s > %s%s' % (m, h, '   (ACTA 67 67.4.d)' if (m, h) in ADJ else ''))
cab = [x for x in cont + sost if x[0] == 'usar_tres_clases_reunion_proceso']
print('de ellas con madre usar_tres_clases_reunion_proceso: %d' % len(cab))
