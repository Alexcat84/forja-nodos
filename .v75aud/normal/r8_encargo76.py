# -*- coding: utf-8 -*-
"""ACTA 74: R8 (ACTA 72 72.11) medido sobre mi encargo de la 76 (docs/loop/PROMPT_SIGUIENTE.md) ANTES de cerrarlo. Copia de
.v74aud/normal/r8_encargo75.py con la seccion cambiada a la ACTA 74 (`74.N`). Imprime las lineas de prosa con digito o con
PALABRA de numero, y cuenta las lineas por estado con su suma (R7). Solo lee."""
import io, re, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
PAL = r'\b(?:dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|veinte|cero|ambos|ambas)\b'
c = collections.Counter()
for n, l in enumerate(io.open('docs/loop/PROMPT_SIGUIENTE.md', encoding='utf-8'), 1):
    if l.startswith('    '):
        c['linea de bloque sangrado'] += 1
        continue
    nums = re.findall(r'\d+(?:[.,]\d+)*', l)
    pals = re.findall(PAL, l, re.I)
    if not nums and not pals:
        c['prosa sin digito ni palabra de numero'] += 1
        continue
    sec = bool(re.search(r'`74\.\d+`', l))
    c['prosa con numero, %s seccion de la ACTA 74' % ('con' if sec else 'sin')] += 1
    print('  L%d %s %s %s | %s' % (n, 'S' if sec else '-', nums, pals, l.strip()[:100]))
print('lineas del encargo: %s | suma: %d' % (dict(sorted(c.items())), sum(c.values())))
