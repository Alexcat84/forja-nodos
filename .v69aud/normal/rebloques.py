# -*- coding: utf-8 -*-
"""ACTA 68: mi R5 sobre mi propia acta. Cada bloque indentado de .v69aud/normal/acta68.md que abre con `$`, partido en
comandos; cada comando se vuelve a correr con bash y su salida se compara linea a linea con lo pegado debajo."""
import io, os, sys, subprocess
BASH = os.environ.get('BASH_GIT', 'bash')
sys.stdout.reconfigure(encoding='utf-8')
L = io.open('.v69aud/normal/acta68.md', encoding='utf-8').read().split('\n')
bloques, cur = [], None
for l in L:
    if l.startswith('    ') and l.strip():
        cur = cur if cur is not None else []; cur.append(l[4:])
    elif not l.strip() and cur is not None: cur.append('')
    else:
        if cur: bloques.append(cur)
        cur = None
if cur: bloques.append(cur)
n = mal = 0
for b in bloques:
    while b and not b[-1]: b.pop()
    if not b or not b[0].startswith('$ '): continue
    cmds = []
    for x in b:
        if x.startswith('$ '): cmds.append([x[2:], []])
        else: cmds[-1][1].append(x)
    for c, pegado in cmds:
        n += 1
        out = subprocess.run([BASH, '-c', c], capture_output=True).stdout.decode('utf-8').rstrip('\n').split('\n')
        out = [o.rstrip('\r') for o in out]
        while pegado and not pegado[-1]: pegado.pop()
        if out != pegado:
            mal += 1
            print('DISTINTO: %s' % c[:100])
            for a, bb in zip(out, pegado):
                if a != bb: print('   corre : %s\n   pegado: %s' % (a[:150], bb[:150])); break
            if len(out) != len(pegado): print('   lineas corre %d pegado %d' % (len(out), len(pegado)))
print('comandos re corridos: %d | identicos: %d | distintos: %d' % (n, n - mal, mal))
