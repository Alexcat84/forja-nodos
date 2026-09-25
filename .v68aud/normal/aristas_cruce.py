# -*- coding: utf-8 -*-
"""ACTA 67: sus aristas por lectura (.v68ext/aristas_lectura.txt, SOSTENGO / NO SOSTENGO, mas la EN ESPERA comentada) contra
las mias selladas (.v68aud/aristas_lectura.tsv), par a par. Una fila suya con dos hijos cuenta como dos pares."""
import io, re, sys
sys.stdout.reconfigure(encoding="utf-8")
S = {}
for l in io.open('.v68ext/aristas_lectura.txt', encoding='utf-8'):
    if l.startswith('#') or '|' not in l: continue
    c = [x.strip() for x in l.split('|')]
    if c[0] not in ('SOSTENGO', 'NO SOSTENGO'): continue
    for h in c[2].split(','): S[(c[1], h.strip())] = c[0]
S[('elegir_estilo_direccion_madurez_relevante_tarea', 'fijar_frecuencia_reunion_individual_madurez_tarea')] = 'EN ESPERA'
M = {}
for l in list(io.open('.v68aud/aristas_lectura.tsv', encoding='utf-8'))[1:]:
    f = l.rstrip('\n').split('\t'); M[(f[0], f[1])] = f[2]
norm = lambda x: 'SI' if x.startswith('SOSTENGO') or x == 'EN ESPERA' else ('VEREDICTO' if x.startswith('EN VEREDICTO') else 'NO')
print('pares suyos: %d (SOSTENGO %d) | filas mias: %d (SOSTENGO %d)' % (len(S), sum(v == 'SOSTENGO' for v in S.values()), len(M), sum(v.startswith('SOSTENGO') for v in M.values())))
for k in sorted(set(S) | set(M)):
    s = S.get(k, '(sin fila)'); m = M.get(k, '(sin fila)')
    ns = norm(s) if k in S else 'NO'; nm = norm(m) if k in M else 'NO'
    if nm == 'VEREDICTO': continue
    print('  %-9s %-50s > %-50s | suya %-12s | mia %s' % ('COINCIDE' if ns == nm else 'DISCREPA', k[0], k[1], s, m))
