# ACTA 71: los 20 insertar de la 72, por sus ficheros .v72ext/insertar_NN_<id>.txt: codigo de salida, y que ninguno empezo
# antes de que terminara el anterior (inicio de la fila N+1 contra fin de la fila N).
import glob, re
from datetime import datetime
F = sorted(glob.glob('.v72ext/insertar_[0-9][0-9]_*.txt'))
filas = []
for f in F:
    t = open(f, encoding='utf-8').read()
    ini = re.search(r'^inicio (\S+ \S+)', t, re.M).group(1)
    fin = re.findall(r'^fin (\S+ \S+) \| codigo de salida (\d+)', t, re.M)[-1]
    filas.append((datetime.fromisoformat(ini), datetime.fromisoformat(fin[0]), int(fin[1])))
cod = sum(1 for f in filas if f[2] == 0)
sol = sum(1 for a, b in zip(filas, filas[1:]) if b[0] < a[1])
print('insertar: %d | con codigo 0: %d | con otro codigo: %d | suma: %d' % (len(filas), cod, len(filas) - cod, len(filas)))
print('solapes entre consecutivos: %d | primer inicio %s | ultimo fin %s' % (sol, filas[0][0], filas[-1][1]))
