# -*- coding: utf-8 -*-
"""Fase ciega de la 65. Para las 20 filas de la tanda (.v64ext/orden.txt, filas 1 a 20):
(1) el blob de su ficha en cuarentena/_insertados/ (HEAD) contra el de la ficha en el commit donde se
    leyo su fidelidad entera (b63405c para las de la 63, 997054d para los seis de d005);
(2) el nodo del dataset contra esa ficha, campo a campo, apartando nodos_previos y nodos_siguientes,
    que son las aristas y se miden aparte;
(3) cuantos pasos trae cada nodo en el dataset."""
import json, subprocess
D005 = ['archivar_indicadores_resolver_problemas', 'construir_grafico_escalonado_pronosticos',
        'construir_indicador_tendencia_patron', 'elegir_fabricar_pedido_pronostico',
        'elegir_indicador_salida_trabajo_administrativo', 'emparejar_indicadores_efecto_contraefecto']
git = lambda *a: subprocess.run(['git'] + list(a), capture_output=True, text=True, encoding='utf-8').stdout
filas = [l.split() for l in open('.v64ext/orden.txt', encoding='utf-8') if l[:1].isdigit()]
tanda = [(int(f[0]), f[1], f[2]) for f in filas if 1 <= int(f[0]) <= 20]
nodos = {json.loads(l)['id']: json.loads(l) for l in open('dataset/nodos.jsonl', encoding='utf-8')}
ARISTAS = ('nodos_previos', 'nodos_siguientes')
ig = dis = cig = cdis = 0
pasos_cap = {}
for n, i, cap in tanda:
    base = '997054d' if i in D005 else 'b63405c'
    x = git('rev-parse', '%s:cuarentena/grove_high_output/%s.json' % (base, i)).strip()
    y = git('rev-parse', 'HEAD:cuarentena/_insertados/grove_high_output/%s.json' % i).strip()
    ficha = json.loads(git('show', '%s:cuarentena/grove_high_output/%s.json' % (base, i)))
    nodo = nodos.get(i)
    if nodo is None:
        print('%2d %-48s NO ESTA EN EL DATASET' % (n, i)); continue
    campos = [k for k in sorted(set(ficha) | set(nodo)) if k not in ARISTAS and ficha.get(k) != nodo.get(k)]
    blob = 'IGUAL' if x == y else 'DISTINTA'
    if x == y: ig += 1
    else: dis += 1
    if campos: cdis += 1
    else: cig += 1
    pasos_cap[cap] = pasos_cap.get(cap, 0) + len(nodo['pasos_accionables'])
    print('%2d %-48s %s lectura %s | ficha %s | dataset contra ficha leida: %s | pasos %d'
          % (n, i, cap, base, blob, ('DIFIERE en ' + ','.join(campos)) if campos else 'igual fuera de aristas',
             len(nodo['pasos_accionables'])))
print('filas: %d | ficha igual a su lectura: %d | distinta: %d | nodo igual a su ficha leida fuera de aristas: %d | distinto: %d'
      % (len(tanda), ig, dis, cig, cdis))
for c in sorted(pasos_cap): print('pasos en el dataset de %s: %d' % (c, pasos_cap[c]))
