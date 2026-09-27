# -*- coding: utf-8 -*-
"""ACTA 72: R8 (72.11) medido sobre mi encargo de la 74 (docs/loop/PROMPT_SIGUIENTE.md) ANTES de cerrarlo. Copia de
.v72aud/normal/r8_encargo73.py con la seccion cambiada a la ACTA 72 (`72.N`), y con lo que prometio mi fase ciega de la 73
(APERTURA_CIEGA.md 9, punto 8): ademas de las lineas con digito, imprime las que traen una PALABRA de numero (las cuentas en
letra, que el instrumento de la 71 no veia). Cuenta las lineas por estado con su suma (R7). Solo lee."""
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
    sec = bool(re.search(r'`72\.\d+`', l))
    c['prosa con numero, %s seccion de la ACTA 72' % ('con' if sec else 'sin')] += 1
    print('  L%d %s %s %s | %s' % (n, 'S' if sec else '-', nums, pals, l.strip()[:100]))
print('lineas del encargo: %s | suma: %d' % (dict(sorted(c.items())), sum(c.values())))
