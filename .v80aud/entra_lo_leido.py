# -*- coding: utf-8 -*-
"""Fase ciega de la 80, sin git (copia libre de .v77aud/entra_lo_leido.py con la tanda de Marquet y la correccion de
d183): para las 20 de .v78aud/las20.txt, (1) donde estan hoy: grafo, bandeja de Marquet, _insertados; (2) que el nodo del
grafo trae lo que se leyo: titulo, condiciones, pasos, entregable y resumen, contra su ficha de _insertados (cuya huella
es la de mi barrido de la 78, .v80aud/huellas_hoy.py). En eliminar_seguimiento_descendente_responsabilizar_dueno el resumen
puede traer ademas la correccion declarada de d183: src/correccion.py escribe resumen viejo + ' ' + texto anadido, asi que
se comprueba que el resumen de hoy es EXACTAMENTE el de la ficha, un espacio y la linea ANADE de .v79ext/frontera_grove.txt
(el texto que la ACTA 78 78.3 firmo contra mis dos posiciones selladas); (3) la linea CORREGIDO de la bitacora sobre ese
nodo, POR CAMPO y sin imprimir su texto: cuantas hay, su numero de linea, y si su texto anadido y su razon son las dos
lineas del fichero, SI o NO; (4) PASOS INVENTADOS de lo que ENTRO, por capitulo (8.2), desde MI lectura sellada de la 78
(.v78aud/fidelidad.tsv, una fila T, P o D por paso, leida sobre el texto de la bandeja ya corregido), con su suma (R7).
Mis dos D las cerro T la ACTA 77 77.5 (D78.6). NO imprime ninguna clave de relacion (R6). Solo lee."""
import io, os, json, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
las20 = io.open('.v78aud/las20.txt', encoding='utf-8').read().split()
E = 'eliminar_seguimiento_descendente_responsabilizar_dueno'
FG = io.open('.v79ext/frontera_grove.txt', encoding='utf-8').read().split('\n')
ANADE = FG[FG.index('ANADE:') + 1].strip(); RAZON = FG[FG.index('RAZON:') + 1].strip()
grafo = {}
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l); grafo[d['id']] = d
CAMPOS = ['titulo', 'condiciones_activacion', 'pasos_accionables', 'entregable_esperado', 'resumen_teorico']
M = collections.defaultdict(list)
for l in list(io.open('.v78aud/fidelidad.tsv', encoding='utf-8'))[1:]:
    if l.strip(): f = l.rstrip('\n').split('\t'); M[f[0]].append(f)
sede = collections.Counter(); ig = collections.Counter(); desc = []
tot = collections.defaultdict(collections.Counter)
for i in las20:
    s = []
    if i in grafo: s.append('grafo')
    if os.path.exists('cuarentena/marquet_turn_the_ship/%s.json' % i): s.append('bandeja')
    if os.path.exists('cuarentena/_insertados/marquet_turn_the_ship/%s.json' % i): s.append('_insertados')
    sede[' y '.join(s) or 'NINGUNA'] += 1
    if i not in grafo: continue
    ficha = json.load(io.open('cuarentena/_insertados/marquet_turn_the_ship/%s.json' % i, encoding='utf-8'))
    dif = [k for k in CAMPOS if grafo[i].get(k) != ficha.get(k)]
    if i == E and dif == ['resumen_teorico'] and grafo[i]['resumen_teorico'] == ficha['resumen_teorico'] + ' ' + ANADE:
        ig['igual salvo el resumen, que es el de la ficha mas la linea ANADE de d183'] += 1
    elif dif:
        ig['DISTINTO'] += 1; print('  DISTINTO de su ficha: %s %s' % (i, dif))
    else: ig['igual en los cinco'] += 1
    n = len(grafo[i]['pasos_accionables']); fs = M[i]
    if n != len(fs) or [int(f[1]) for f in fs] != list(range(1, n + 1)): desc.append(i)
    caps = set(f[3] for f in fs)
    t = tot['/'.join(sorted(caps))]; t['cand'] += 1; t['pasos'] += n
    for f in fs: t[f[2]] += 1
print('las 20 por sede hoy: %s | suma: %d' % (dict(sede), sum(sede.values())))
print('nodos del grafo contra su ficha, cinco campos: %s | suma: %d' % (dict(ig), sum(ig.values())))
print('nodos con descuadre entre sus pasos en el grafo y mis filas selladas: %d %s' % (len(desc), desc))
C = []
for n, l in enumerate(io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8'), 1):
    d = json.loads(l)
    if d.get('veredicto') == 'CORREGIDO' and d.get('candidato') == E: C.append((n, d))
print('lineas CORREGIDO de la bitacora sobre %s: %d | en la linea: %s' % (E, len(C), [n for n, _ in C]))
for n, d in C:
    print('  linea %d: texto anadido igual a la linea ANADE de .v79ext/frontera_grove.txt: %s | razon igual a la linea RAZON: %s | caracteres antes %s, despues %s' % (
        n, 'SI' if d.get('texto_anadido') == ANADE else 'NO', 'SI' if d.get('razon') == RAZON else 'NO', d.get('caracteres_antes'), d.get('caracteres_despues')))
T = collections.Counter()
for k in sorted(tot):
    t = tot[k]; m = dict((c, t[c]) for c in ('T', 'P', 'D'))
    for c in ('cand', 'pasos', 'T', 'P', 'D'): T[c] += t[c]
    print('%s lo que ENTRO: candidatos %d | pasos %d | mis marcas: %s | suma: %d | PUENTE %d de %d = %.2f por ciento' % (
        k, t['cand'], t['pasos'], m, sum(m.values()), t['P'], t['pasos'], 100.0 * t['P'] / t['pasos']))
m = dict((c, T[c]) for c in ('T', 'P', 'D'))
print('los trece: candidatos %d | pasos %d | mis marcas: %s | suma: %d | PUENTE %d de %d | con las D cerradas T (ACTA 77 77.5): T %d, P %d, suma %d' % (
    T['cand'], T['pasos'], m, sum(m.values()), T['P'], T['pasos'], T['T'] + T['D'], T['P'], T['T'] + T['D'] + T['P']))
