# -*- coding: utf-8 -*-
"""LA COLA DEL CAPITULO: renglones de cuerpo desde L273 hasta el final que
ninguna ficha de cap_04 cita, con su primera frase, para poder decir QUE queda.
Medida, no conclusion: la conclusion va marcada LECTURA en la apertura."""
import json, glob, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
citados = set()
for f in sorted(glob.glob('cuarentena/grove_high_output/*.json')):
    rt = json.load(open(f, encoding='utf-8')).get('resumen_teorico', '')
    if 'cap_04' not in rt:
        continue
    for a, b in re.findall(r'L(\d+) a L(\d+)', rt):
        citados |= set(range(int(a), int(b) + 1))
    citados |= set(int(n) for n in re.findall(r'\(L(\d+):', rt))
lineas = open('fuentes/grove_high_output/cap_04.md', encoding='utf-8').read().split(chr(10))
n_sin = 0
for i in range(273, 324):
    t = lineas[i-1].strip()
    if not t or i in citados:
        continue
    n_sin += 1
    print('L%-4d %s' % (i, (t[:150] + ('...' if len(t) > 150 else ''))))
print('---')
print('renglones de cuerpo SIN CITAR de L273 al final: %d' % n_sin)
