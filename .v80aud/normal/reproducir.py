# ACTA 79: copia de .v79aud/normal/reproducir.py (ACTA 78); vuelve a correr cada linea "$ cmd" de un fichero de evidencia del extractor y compara su salida con la guardada.
# Solo corre comandos de lectura: salta los que escriben (deuda.py --pagar, corregir, arista, git tag y push, y los que redirigen a .v80ext/), y lo dice.
import subprocess, sys, io
ESCRIBEN = ('--pagar', '--saneamiento', '--anotar', 'forja.py corregir', 'forja.py arista', 'git tag', 'git push', '> .v80ext')
BASH = r'C:\Program Files\Git\usr\bin\bash.exe'
def bloques(ruta):
    L = io.open(ruta, encoding='utf-8').read().split('\n')
    out, cmd, sal = [], None, []
    for l in L:
        if l.startswith('$ '):
            if cmd is not None: out.append((cmd, sal))
            cmd, sal = l[2:], []
        elif cmd is not None and not l.startswith('# '):
            sal.append(l)
    if cmd is not None: out.append((cmd, sal))
    return out
tot = {'IDENTICA': 0, 'DISTINTA': 0, 'NO CORRIDA (escribe)': 0}
for ruta in sys.argv[1:]:
    for cmd, sal in bloques(ruta):
        if any(e in cmd for e in ESCRIBEN):
            tot['NO CORRIDA (escribe)'] += 1; print('  NO CORRIDA (escribe) | %s | %s' % (ruta, cmd[:90])); continue
        r = subprocess.run([BASH, '-c', cmd], capture_output=True)
        hoy = r.stdout.decode('utf-8', 'replace').replace('\r', '').rstrip('\n').split('\n')
        guard = '\n'.join(sal).rstrip('\n').split('\n')
        k = 'IDENTICA' if hoy == guard else 'DISTINTA'
        tot[k] += 1
        if k == 'DISTINTA':
            print('  DISTINTA | %s | %s' % (ruta, cmd[:110]))
            print('     guardada: %s' % ' / '.join(guard)[:300])
            print('     hoy     : %s' % ' / '.join(hoy)[:300])
print('comandos: %s | suma: %d' % (tot, sum(tot.values())))
