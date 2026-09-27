# -*- coding: utf-8 -*-
"""COMPROBACION DEL HEREDADO 1, mecanica y no de palabra.

Lee docs/loop/APERTURA_CIEGA.md, saca cada comando pegado (las lineas que
empiezan por '    $ '), cuenta las lineas de salida que van debajo, y para los
que son grep, sed o awk los VUELVE A CORRER y compara las dos cuentas."""
import io, re, subprocess, sys

RUTA = 'docs/loop/APERTURA_CIEGA.md'
lineas = io.open(RUTA, encoding='utf-8').read().split('\n')

bloques = []
i = 0
while i < len(lineas):
    l = lineas[i]
    if l.startswith('    $ '):
        crudo = l[6:]
        cortada = None
        m = re.search(r'\s+\[(CORTADA[^\]]*)\]\s*$', crudo)
        if m:
            cortada = m.group(1)
            crudo = crudo[:m.start()]
        salida = []
        j = i + 1
        while j < len(lineas):
            s = lineas[j]
            if s.startswith('    $ '):
                break
            if s.strip() == '':
                # una linea en blanco dentro de un bloque indentado sigue siendo del bloque
                k = j + 1
                while k < len(lineas) and lineas[k].strip() == '':
                    k += 1
                if k < len(lineas) and lineas[k].startswith('    ') and not lineas[k].startswith('    $ '):
                    salida.extend(lineas[j:k]); j = k; continue
                break
            if not s.startswith('    '):
                break
            salida.append(s); j += 1
        bloques.append((i + 1, crudo.strip(), cortada, len(salida)))
        i = j
    else:
        i += 1

ESCANEABLES = ('grep', 'sed', 'awk')
pegados = len(bloques)
recorridos = 0
cortados = sum(1 for _, _, c, _ in bloques if c)
discrepan = []
print('%-5s %-4s %-6s %-6s %s' % ('linea', 'rec', 'pegad', 'corre', 'comando'))
for ln, cmd, cortada, n in bloques:
    prim = cmd.split()[0]
    if prim not in ESCANEABLES:
        print('%-5d %-4s %-6d %-6s %s' % (ln, 'no', n, '.', cmd[:78]))
        continue
    recorridos += 1
    r = subprocess.run(['bash', '-lc', cmd], capture_output=True, text=True, encoding='utf-8', errors='replace')
    salida = [x for x in (r.stdout or '').split('\n')]
    if salida and salida[-1] == '':
        salida.pop()
    m = len(salida)
    marca = 'SI' if (m == n or cortada) else 'NO'
    if m != n and not cortada:
        discrepan.append((ln, cmd, n, m))
    print('%-5d %-4s %-6d %-6d %s  %s' % (ln, 'si', n, m, cmd[:70], '' if marca == 'SI' else '<-- NO CUADRA'))
print()
print('COMANDOS PEGADOS   : %d' % pegados)
print('COMANDOS RECORRIDOS: %d  (los grep, sed y awk, que son los que el remedio nombra)')
print('COMANDOS RECORRIDOS: %d' % recorridos)
print('CORTADOS Y DECLARADOS: %d' % cortados)
print('DISCREPANCIAS SIN DECLARAR: %d' % len(discrepan))
for ln, cmd, n, m in discrepan:
    print('   L%d  pegue %d, da %d   %s' % (ln, n, m, cmd))
