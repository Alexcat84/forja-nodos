"""ACTA 79: que cada insertar de la vuelta 80 volvio antes de lanzarse el siguiente, que su commit cae entre su fin y el inicio
del siguiente, que la arista se declaro entre el fin de la fila 5 y el inicio de la 6, y que corregir (d183) corrio despues del
fin de la fila 20. Lee los relojes de .v80ext/insertar_*.txt y las horas de commit de git. Solo lee."""
import glob, io, re, subprocess, datetime as dt, collections

def t(s):
    return dt.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')

filas = []
for f in sorted(glob.glob('.v80ext/insertar_*.txt')):
    x = io.open(f, encoding='utf-8').read()
    n = int(re.search(r'insertar_(\d+)_', f).group(1))
    ini = t(re.search(r'^inicio (\S+ \S+)', x, re.M).group(1))
    m = re.search(r'^fin (\S+ \S+) \| codigo de salida (\d+)', x, re.M)
    fin, cod = t(m.group(1)), m.group(2)
    fin_fichero = io.open(f.replace('.txt', '.fin'), encoding='utf-8').read().strip()
    filas.append((n, ini, fin, cod, fin_fichero))

log = subprocess.run(['git', 'log', '--format=%cI|%s', '0da1d2b7..67f2bee3'], capture_output=True, text=True, encoding='utf-8').stdout
commits = {}
otros = {}
for l in log.splitlines():
    fecha, asunto = l.split('|', 1)
    fecha = dt.datetime.fromisoformat(fecha).replace(tzinfo=None)
    m = re.match(r'Vuelta 80, fila (\d+): \S+ insertado', asunto)
    if m:
        commits[int(m.group(1))] = fecha
    elif asunto.startswith('Vuelta 80, T4'):
        otros['T4'] = fecha

res = collections.Counter()
for i, (n, ini, fin, cod, ff) in enumerate(filas):
    sig = filas[i + 1][1] if i + 1 < len(filas) else None
    ok_orden = sig is None or sig >= fin
    c = commits.get(n)
    ok_commit = c is not None and c >= fin and (sig is None or c <= sig)
    res['codigo %s y .fin %s' % (cod, ff)] += 1
    res['inicio del siguiente despues de su fin: %s' % ('SI' if ok_orden else 'NO')] += 1
    res['su commit entre su fin y el inicio del siguiente: %s' % ('SI' if ok_commit else 'NO')] += 1
    print('%2d inicio %s fin %s codigo %s .fin %s | commit %s | hueco hasta el siguiente %s s' % (
        n, ini.time(), fin.time(), cod, ff, c.time() if c else None, int((sig - fin).total_seconds()) if sig else '-'))
print('filas: %d | numeradas 1 a 20 sin hueco: %s' % (len(filas), [f[0] for f in filas] == list(range(1, 21))))
for k, v in res.items():
    print('  %s: %d' % (k, v))

ar = subprocess.run(['git', 'log', '--format=%cI', '-1', '--diff-filter=A', '--',
                     '.v80ext/arista_observar_reunion_rutinaria_senales_plantilla__seguir_frustrado_preguntar_implantacion_ideas.txt'],
                    capture_output=True, text=True).stdout.strip()
ar = dt.datetime.fromisoformat(ar).replace(tzinfo=None)
f5, i6 = filas[4][2], filas[5][1]
print('arista: primer commit de su salida %s | fin de la fila 5 %s | inicio de la fila 6 %s | entre las dos: %s' % (
    ar.time(), f5.time(), i6.time(), f5 <= ar <= i6))
print('T4 (corregir, d183): commit %s | fin de la fila 20 %s | despues: %s' % (otros['T4'].time(), filas[-1][2].time(), otros['T4'] > filas[-1][2]))
