# -*- coding: utf-8 -*-
# Recuento MIO de nodos y pasos por fichero de capitulo, leido del dataset de HOY.
import io, json, re, collections
nodos = [json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
c = collections.Counter(); p = collections.Counter()
for n in nodos:
    m = re.search(r'fuentes/scott_radical_candor/(cap_\d+)\.md', n.get('resumen_teorico') or '')
    if m:
        c[m.group(1)] += 1; p[m.group(1)] += len(n['pasos_accionables'])
print('nodos del dataset: %d' % len(nodos))
print('%-10s %6s %8s' % ('capitulo', 'nodos', 'pasos'))
for k in sorted(c): print('%-10s %6d %8d' % (k, c[k], p[k]))
print('suma %d nodos, %d pasos' % (sum(c.values()), sum(p.values())))
print()
n6 = [x for x in nodos if x['id'] == 'construir_confianza_equipo_tiempo_solas'][0]
print('paso 6 de construir_confianza_equipo_tiempo_solas:')
print('  %s' % n6['pasos_accionables'][5])
print('paso 7:')
print('  %s' % n6['pasos_accionables'][6])
print('nodos_siguientes: %s' % n6['nodos_siguientes'])
