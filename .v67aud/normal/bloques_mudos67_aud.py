# -*- coding: utf-8 -*-
"""R5 por el otro lado: en el tramo de la vuelta 67 (copia del auditor, ACTA 66, cabecera cambiada) de REPORTE.md, cada bloque indentado que
abre con `$`, partido en comandos. Imprime los comandos que en el bloque NO llevan ni una linea
de salida debajo, y si el bloque trae la formula (recortado, entero en ...). El instrumento de
la ACTA 62 (pegado63.py) mira elisiones y texto anadido; este mira la salida que falta."""
import io
L = io.open('docs/loop/REPORTE.md', encoding='utf-8').read().split('\n')
i0 = [k for k, l in enumerate(L) if l.startswith('# VUELTA 67 ')][0]
bloques, cur = [], None
for k in range(i0, len(L)):
    l = L[k]
    if l.startswith('    ') and l.strip():
        if cur is None: cur = [k + 1, []]
        cur[1].append(l[4:])
    elif not l.strip() and cur is not None:
        cur[1].append('')
    else:
        if cur: bloques.append(cur)
        cur = None
if cur: bloques.append(cur)
abren = mudos = cmds = 0
for ini, ls in bloques:
    while ls and not ls[-1]: ls.pop()
    if not ls or not ls[0].startswith('$ '): continue
    abren += 1
    formula = any('(recortado, entero en' in x for x in ls)
    for j, x in enumerate(ls):
        if x.startswith('$ '):
            cmds += 1
            sig = ls[j + 1] if j + 1 < len(ls) else None
            if sig is None or sig.startswith('$ ') or not sig.strip():
                mudos += 1
                print('linea %d  formula dentro: %s  %s' % (ini + j, 'SI' if formula else 'NO', x[:110]))
print('bloques abiertos con `$`: %d | comandos `$`: %d | comandos sin ninguna linea de salida en su bloque: %d' % (abren, cmds, mudos))
