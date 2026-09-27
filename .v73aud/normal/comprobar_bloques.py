# -*- coding: utf-8 -*-
"""ACTA 72: cada comando `$` de los bloques sangrados de .v73aud/normal/acta72.md, corrido con bash ahora, contra las lineas que
el acta pega debajo (hasta el siguiente `$` o el fin del bloque). Imprime los que difieren y la cuenta con su suma. Solo lee."""
import io, subprocess, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
L = io.open('.v73aud/normal/acta72.md', encoding='utf-8').read().split('\n')
cmds, i = [], 0
while i < len(L):
    if L[i].startswith('    $ '):
        c, out, i = L[i][6:], [], i + 1
        while i < len(L) and L[i].startswith('    ') and not L[i].startswith('    $ '):
            out.append(L[i][4:]); i += 1
        cmds.append((c, out))
    else:
        i += 1
est = collections.Counter()
for c, out in cmds:
    r = subprocess.run([r'C:/Program Files/Git/usr/bin/bash.exe', '-c', c], capture_output=True, text=True, encoding='utf-8', errors='replace')
    got = [x.rstrip() for x in r.stdout.rstrip('\n').split('\n')]
    ok = got == [x.rstrip() for x in out]
    est['igual' if ok else 'DIFIERE'] += 1
    if not ok:
        print('DIFIERE: $ %s' % c[:120])
        for a, b in zip(got + [''] * 20, out + [''] * 20):
            if a != b: print('   hoy : %s\n   acta: %s' % (a[:150], b[:150])); break
print('comandos: %s | suma: %d' % (dict(est), sum(est.values())))
