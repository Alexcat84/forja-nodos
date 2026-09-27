# -*- coding: utf-8 -*-
"""Fase ciega de la 67 (copia de .v66aud/entra_lo_leido.py con la tanda cambiada). Para las 20 primeras de cap_04
(.v66aud/los22_cap04.txt, las 22 en orden de pieza menos agrupar_interrupciones y canalizar, que el encargo deja a la 68):
(1) que lo que vive HOY en dataset/nodos.jsonl es lo que se leyo entero: titulo, condiciones, pasos y entregable del
    nodo contra la ficha en d8f4e2a (cierre de la 66, sobre el que se leyo la fidelidad entera), y el blob de
    cuarentena/_insertados/ contra ese mismo commit;
(2) PASOS INVENTADOS de lo que ENTRO, desde MI lectura entera de cap_04 (.v66aud/fidelidad.tsv, filas P), con mis
    cuatro D contadas aparte (la ACTA 65 65.4.a las adjudico T)."""
import io, json, subprocess, collections
git = lambda *a: subprocess.run(['git'] + list(a), capture_output=True, text=True, encoding='utf-8').stdout
los22 = [l.strip() for l in io.open('.v66aud/los22_cap04.txt', encoding='utf-8') if l.strip()]
tanda = [i for i in los22 if i not in ('agrupar_interrupciones_subordinados_reuniones_regulares',
                                       'canalizar_interrupciones_cartel_hora_oficina')]
grafo = {}
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l); grafo[d['id']] = d
M = collections.defaultdict(collections.Counter)
for l in io.open('.v66aud/fidelidad.tsv', encoding='utf-8'):
    c = l.rstrip('\n').split('\t')
    if c[0] == 'id' or len(c) < 3: continue
    M[c[0]][c[2]] += 1
CAMPOS = ['titulo', 'condiciones_activacion', 'pasos_accionables', 'entregable_esperado']
iguales = distintas = blob_ok = blob_mal = 0
tot = collections.Counter()
for i in tanda:
    leida = json.loads(git('show', 'd8f4e2a:cuarentena/grove_high_output/%s.json' % i))
    nodo = grafo.get(i)
    if nodo is None:
        print('NO ESTA EN EL GRAFO: %s' % i); continue
    dif = [k for k in CAMPOS if nodo.get(k) != leida.get(k)]
    if dif: distintas += 1; print('DISTINTO de su lectura: %s campos %s' % (i, dif))
    else: iguales += 1
    b1 = git('rev-parse', 'd8f4e2a:cuarentena/grove_high_output/%s.json' % i).strip()
    b2 = git('rev-parse', 'HEAD:cuarentena/_insertados/grove_high_output/%s.json' % i).strip()
    if b1 == b2: blob_ok += 1
    else: blob_mal += 1; print('BLOB de _insertados distinto del leido: %s' % i)
    n = len(nodo['pasos_accionables'])
    filas = sum(M[i].values())
    tot.update({'cand': 1, 'pasos': n, 'filas': filas, 'P': M[i]['P'], 'D': M[i]['D']})
    print('%-54s pasos %2d filas mias %2d P %d D %d' % (i, n, filas, M[i]['P'], M[i]['D']))
print('nodos de la tanda en el grafo iguales a su lectura entera: %d | distintos: %d' % (iguales, distintas))
print('fichas de _insertados con el mismo blob que en d8f4e2a: %d | distintas: %d' % (blob_ok, blob_mal))
print('cap_04 lo que entro: candidatos %d | pasos %d | filas de mi lectura %d | P %d | D %d' % (
    tot['cand'], tot['pasos'], tot['filas'], tot['P'], tot['D']))
print('PUENTE sobre pasos que entraron: %d de %d = %.2f por ciento' % (tot['P'], tot['pasos'], 100.0 * tot['P'] / tot['pasos']))
print('si mis D cayesen a PUENTE: %d de %d = %.2f por ciento' % (tot['P'] + tot['D'], tot['pasos'], 100.0 * (tot['P'] + tot['D']) / tot['pasos']))
