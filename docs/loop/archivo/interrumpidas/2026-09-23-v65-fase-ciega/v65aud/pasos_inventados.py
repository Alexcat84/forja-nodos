# -*- coding: utf-8 -*-
"""PASOS INVENTADOS POR CAPITULO sobre lo que ENTRA en la 65 (filas 1 a 20 de .v64ext/orden.txt),
contados desde las lecturas enteras ya ADJUDICADAS, no desde cero y no a ojo:
  - .v63aud/fidelidad.tsv (fase ciega de la 63), con lo que adjudico la ACTA 62 62.5:
      equilibrar_capacidad_personal_inventario_plazo: los pasos que en b63405c^ llevaban 'y apunta su coste' -> P
      detectar_arreglar_fallo_etapa_menor_valor paso 1: D -> T
  - .v64aud/fidelidad.tsv (fase ciega de la 64, los seis de d005), con lo que adjudico la ACTA 63 63.3.a:
      emparejar_indicadores_efecto_contraefecto 1 -> T, construir_grafico_escalonado_pronosticos 5 -> P,
      elegir_fabricar_pedido_pronostico 8 -> P
Cada paso del nodo que entro tiene que tener su fila, y ninguna fila puede sobrar."""
import io, json, re, subprocess, collections
git = lambda *a: subprocess.run(['git'] + list(a), capture_output=True, text=True, encoding='utf-8').stdout
tanda = [(l.split()[1], l.split()[2]) for l in io.open('.v64ext/orden.txt', encoding='utf-8')
         if l[:1].isdigit() and 1 <= int(l.split()[0]) <= 20]
lect = collections.defaultdict(dict)
for l in io.open('.v63aud/fidelidad.tsv', encoding='utf-8'):
    if l.strip() and not l.startswith('#'):
        c = [x.strip() for x in l.split('|')]; lect[c[0]][int(c[1])] = c[2]
for l in io.open('.v64aud/fidelidad.tsv', encoding='utf-8'):
    c = l.rstrip('\n').split('\t')
    if c[0] != 'id' and len(c) > 2: lect[c[0]][int(c[1])] = c[2]
adj = {}
viejo = json.loads(git('show', 'b63405c^:cuarentena/grove_high_output/equilibrar_capacidad_personal_inventario_plazo.json'))
for k, p in enumerate(viejo['pasos_accionables'], 1):
    if 'y apunta su coste' in p: adj[('equilibrar_capacidad_personal_inventario_plazo', k)] = ('P', 'ACTA 62 62.5')
adj[('detectar_arreglar_fallo_etapa_menor_valor', 1)] = ('T', 'ACTA 62 62.5')
adj[('emparejar_indicadores_efecto_contraefecto', 1)] = ('T', 'ACTA 63 63.3.a')
adj[('construir_grafico_escalonado_pronosticos', 5)] = ('P', 'ACTA 63 63.3.a')
adj[('elegir_fabricar_pedido_pronostico', 8)] = ('P', 'ACTA 63 63.3.a')
nodos = {json.loads(l)['id']: json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8')}
tot = collections.defaultdict(collections.Counter); faltan = []; sobran = []
for i, cap in tanda:
    n = len(nodos[i]['pasos_accionables'])
    faltan += ['%s %d' % (i, k) for k in range(1, n + 1) if k not in lect[i]]
    sobran += ['%s %d' % (i, k) for k in lect[i] if k > n]
    for k in range(1, n + 1):
        clase = adj.get((i, k), (lect[i].get(k, '?'),))[0]
        tot[cap][clase] += 1; tot[cap]['pasos'] += 1
for (i, k), (c, cita) in sorted(adj.items()):
    print('adjudicado  %-48s paso %d  %s -> %s  (%s)' % (i, k, lect[i].get(k), c, cita))
print('pasos sin fila: %d %s | filas sin paso: %d %s' % (len(faltan), faltan, len(sobran), sobran))
print('%-8s %5s %4s %4s %4s %8s' % ('capitulo', 'pasos', 'T', 'P', 'D', 'P/pasos'))
for c in sorted(tot):
    t = tot[c]; print('%-8s %5d %4d %4d %4d %7.2f%%' % (c, t['pasos'], t['T'], t['P'], t['D'], 100.0 * t['P'] / t['pasos']))
