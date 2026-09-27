# -*- coding: utf-8 -*-
"""Fase ciega de la 65: los vecinos que MI barrido (.v65aud/vecinos_<id>.json, grafo mas bandejas de HOY)
levanta a cada uno de los 20, contra las lineas YA ADJUDICADAS en la ACTA 63: .v64ext/veredictos_listos.txt
(un bloque por candidato) y .v63ext/cmd_02_detectar.sh (las de detectar). No lee la bitacora.
Separa los vecinos que son de los 17 candidatos de Marquet que la cosecha (f770c8c) trajo DESPUES de la 65."""
import io, json, re, os, collections
los22 = [l.split()[0] for l in io.open('.v64ext/los22.txt', encoding='utf-8') if l.strip() and not l.startswith('#')]
tanda = los22[:20]
mq = set(os.path.basename(l.strip())[:-5] for l in io.open('.v65aud/marquet_nuevos.txt', encoding='utf-8') if l.strip())
listos = collections.defaultdict(dict); sec = None
for l in io.open('.v64ext/veredictos_listos.txt', encoding='utf-8'):
    if l.startswith('## '): sec = l[3:].strip(); continue
    c = l.strip().split('|')
    if sec and len(c) > 2: listos[sec][c[0]] = c[1]
for m in re.finditer(r'--veredicto "([a-z0-9_]+)\|([A-Z]+)\|', io.open('.v63ext/cmd_02_detectar.sh', encoding='utf-8').read()):
    listos['detectar_arreglar_fallo_etapa_menor_valor'].setdefault(m.group(1), m.group(2))
tot = collections.Counter(); nuevos = []
for i in tanda:
    f = '.v65aud/vecinos_%s.json' % i
    if not os.path.exists(f): print('%-48s SIN BARRIDO TODAVIA' % i); tot['sin'] += 1; continue
    v = json.load(io.open(f, encoding='utf-8'))
    b = {x['id']: x for x in v['vecinos']}; L = listos.get(i, {})
    ambos = [k for k in b if k in L]; solo_b = [k for k in b if k not in L]; solo_l = [k for k in L if k not in b]
    tot['barrido'] += len(b); tot['ambos'] += len(ambos); tot['solo_b'] += len(solo_b); tot['solo_l'] += len(solo_l)
    tot['solo_b_mq'] += len([k for k in solo_b if k in mq])
    print('%-48s pob %d barrido %2d | con linea %2d | sin linea %2d (de marquet nuevo %d) | linea sin vecino hoy %d' % (
        i, v['grafo'] + v['bandejas'], len(b), len(ambos), len(solo_b), len([k for k in solo_b if k in mq]), len(solo_l)))
    for k in solo_b:
        s = b[k]['senales']
        print('    SIN LINEA  %-46s %-7s %s sim %s fam %s paso %s%s' % (k, b[k]['sede'], ','.join(b[k]['levantada_por']), s.get('similitud_texto'), s.get('familia_id'), s.get('paso_contra_nodo'), '  MARQUET NUEVO' if k in mq else ''))
    for k in solo_l: print('    LINEA SIN VECINO HOY  %s (%s)' % (k, L[k]))
print('pares del barrido %d | con linea adjudicada %d | sin linea %d, de ellos de los 17 de marquet %d | lineas sin vecino hoy %d | candidatos sin barrido %d' % (
    tot['barrido'], tot['ambos'], tot['solo_b'], tot['solo_b_mq'], tot['solo_l'], tot['sin']))
print('lineas adjudicadas en total: %d en %d bloques' % (sum(len(x) for x in listos.values()), len(listos)))
