# -*- coding: utf-8 -*-
"""Fase ciega de la 72: R8 (ACTA 70 70.12) medido sobre su primera sede, MI encargo de la 72 (docs/loop/PROMPT_SIGUIENTE.md,
escrito al cerrar la ACTA 70). Imprime cada linea de prosa (no de bloque sangrado) que trae alguna cifra entre comillas
invertidas y NINGUNA seccion de acta entre comillas invertidas (`NN.N`), con sus cifras y su texto cortado a 150 caracteres; y cuenta las lineas por estado
con su suma (R7). No decide que cifra es de medida: eso lo lee el auditor y lo escribe como LECTURA. Solo lee."""
import io, re, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
c = collections.Counter()
for n, l in enumerate(io.open('docs/loop/PROMPT_SIGUIENTE.md', encoding='utf-8'), 1):
    if l.startswith('    '): c['linea de bloque sangrado'] += 1; continue
    nums = re.findall(r'`(\d[\d.,]*)`', l)
    if not nums: c['prosa sin cifra'] += 1; continue
    if re.search(r'`\d+\.\d+`', l): c['prosa con cifra y con seccion'] += 1; continue
    c['prosa con cifra y SIN seccion'] += 1
    print('  L%d %s | %s' % (n, nums, l.strip()[:150]))
print('lineas del encargo: %s | suma: %d' % (dict(c), sum(c.values())))
