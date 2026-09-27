# -*- coding: utf-8 -*-
"""Fase ciega de la 65. Para los 20 de la tanda (las 20 primeras filas de .v64ext/los22.txt):
(1) que lo que vive HOY en dataset/nodos.jsonl es lo que se leyo entero (D.58): titulo, condiciones,
    pasos y entregable del nodo del grafo contra la ficha en el commit de su lectura entera
    (b63405c para los 16 de la 63, 997054d para los seis de d005), y el blob de
    cuarentena/_insertados/ contra ese mismo commit;
(2) PASOS INVENTADOS POR CAPITULO sobre lo que ENTRO, desde las lecturas enteras YA ADJUDICADAS:
    .v63ext/fidelidad.txt columnas PUENTE y verbo (ACTA 62 62.5: la clausula reescrita cuenta como P)
    y .v64ext/fidelidad.tsv filas P (ACTA 63 63.3.a, las tres discrepancias ganadas por el extractor)."""
import io, json, re, subprocess, collections
git = lambda *a: subprocess.run(['git'] + list(a), capture_output=True, text=True, encoding='utf-8').stdout
D005 = ['archivar_indicadores_resolver_problemas', 'construir_grafico_escalonado_pronosticos',
        'construir_indicador_tendencia_patron', 'elegir_fabricar_pedido_pronostico',
        'elegir_indicador_salida_trabajo_administrativo', 'emparejar_indicadores_efecto_contraefecto']
los22 = [l.split() for l in io.open('.v64ext/los22.txt', encoding='utf-8') if l.strip() and not l.startswith('#')]
tanda = los22[:20]
grafo = {}
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l); grafo[d['id']] = d
# P adjudicados
P = collections.Counter()
for l in io.open('.v63ext/fidelidad.txt', encoding='utf-8'):
    c = l.split()
    if len(c) >= 10 and c[0].isdigit():
        P[c[3]] += int(c[7]) + int(c[8])
for l in io.open('.v64ext/fidelidad.tsv', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    c = [x.strip() for x in l.split('|')]
    if c[2] == 'P': P[c[0]] += 1
CAMPOS = ['titulo', 'condiciones_activacion', 'pasos_accionables', 'entregable_esperado']
por_cap = collections.defaultdict(lambda: [0, 0, 0])
iguales = distintas = blob_ok = blob_mal = 0
for i, cap, pieza in tanda:
    base = '997054d' if i in D005 else 'b63405c'
    leida = json.loads(git('show', '%s:cuarentena/grove_high_output/%s.json' % (base, i)))
    nodo = grafo.get(i)
    if nodo is None:
        print('NO ESTA EN EL GRAFO: %s' % i); continue
    dif = [k for k in CAMPOS if nodo.get(k) != leida.get(k)]
    if dif: distintas += 1; print('DISTINTO de su lectura: %s campos %s' % (i, dif))
    else: iguales += 1
    b1 = git('rev-parse', '%s:cuarentena/grove_high_output/%s.json' % (base, i)).strip()
    b2 = git('rev-parse', 'HEAD:cuarentena/_insertados/grove_high_output/%s.json' % i).strip()
    if b1 == b2: blob_ok += 1
    else: blob_mal += 1; print('BLOB de _insertados distinto del leido: %s' % i)
    n = len(nodo['pasos_accionables'])
    por_cap[cap][0] += 1; por_cap[cap][1] += n; por_cap[cap][2] += P[i]
    print('%-50s %s %-4s leida en %s pasos %2d P %d' % (i, cap, pieza, base, n, P[i]))
print('nodos de la tanda en el grafo iguales a su lectura entera: %d | distintos: %d' % (iguales, distintas))
print('fichas de _insertados con el mismo blob que su lectura entera: %d | distintas: %d' % (blob_ok, blob_mal))
print('%-8s %5s %5s %4s %8s' % ('capitulo', 'cand', 'pasos', 'P', 'por100'))
t = [0, 0, 0]
for c in sorted(por_cap):
    a, b, p = por_cap[c]; t = [t[0] + a, t[1] + b, t[2] + p]
    print('%-8s %5d %5d %4d %8.2f' % (c, a, b, p, 100.0 * p / b))
print('%-8s %5d %5d %4d %8.2f' % ('tanda', t[0], t[1], t[2], 100.0 * t[2] / t[1]))
