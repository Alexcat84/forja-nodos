# -*- coding: utf-8 -*-
"""Fase ciega de la 79 (d135): de que capitulo sale cada nodo de gerber_emyth del grafo, leido de la frase
'UNIDAD DE ORIGEN: fuentes/gerber_emyth/cap_NN.md' con la que abre su resumen_teorico, y el reparto por capitulo con su
suma (R7). Y aparte, cuantos nodos NOMBRAN cap_01 o cap_03 en cualquier sitio de su resumen (no como origen). No imprime
ninguna clave de relacion (R6). Solo lee."""
import io, json, re, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
por = collections.Counter(); nombran = collections.Counter(); n = 0
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l)
    if not any(f.get('clave') == 'gerber_emyth' for f in d.get('fuentes', [])): continue
    n += 1
    r = d.get('resumen_teorico', '')
    m = re.match(r'UNIDAD DE ORIGEN: fuentes/gerber_emyth/(cap_\d+)\.md', r)
    por[m.group(1) if m else 'SIN FRASE DE ORIGEN'] += 1
    for c in ('cap_01', 'cap_03'):
        if re.search(r'\b%s\b' % c, r): nombran[c] += 1
print('nodos de gerber_emyth en el grafo: %d' % n)
print('por capitulo de origen: %s | suma: %d' % (dict(sorted(por.items())), sum(por.values())))
print('de origen cap_01: %d | de origen cap_03: %d' % (por['cap_01'], por['cap_03']))
print('nodos cuyo resumen NOMBRA cap_01: %d | NOMBRA cap_03: %d' % (nombran['cap_01'], nombran['cap_03']))
