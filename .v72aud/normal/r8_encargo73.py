# -*- coding: utf-8 -*-
"""ACTA 71: R8, escalado (71.11), medido sobre mi encargo de la 73 (docs/loop/PROMPT_SIGUIENTE.md) ANTES de cerrarlo.
Mas estricto que .v72aud/r8_encargo.py, que tenia un hueco (una seccion en la linea tapaba otra cifra sin seccion, APERTURA_CIEGA.md 6):
imprime TODA linea de prosa (no de bloque sangrado) que trae algun digito, entre comillas invertidas o no, con todos sus
numeros y si trae una seccion de la ACTA 71 (`71.N`). La lectura de cada una (cifra de medida o identificador) la escribe el
auditor a mano en el acta. Cuenta las lineas por estado con su suma (R7). Solo lee."""
import io, re, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
c = collections.Counter()
for n, l in enumerate(io.open('docs/loop/PROMPT_SIGUIENTE.md', encoding='utf-8'), 1):
    if l.startswith('    '):
        c['linea de bloque sangrado'] += 1
        continue
    nums = re.findall(r'\d+(?:[.,]\d+)*', l)
    if not nums:
        c['prosa sin digito'] += 1
        continue
    sec = bool(re.search(r'`71\.\d+`', l))
    c['prosa con digito, %s seccion de la ACTA 71' % ('con' if sec else 'sin')] += 1
    print('  L%d %s %s | %s' % (n, 'S' if sec else '-', nums, l.strip()[:110]))
print('lineas del encargo: %s | suma: %d' % (dict(sorted(c.items())), sum(c.values())))
