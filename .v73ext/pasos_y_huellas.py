# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 73 de .v71ext/pasos_y_huellas.py (encargo de la 73, TAREA 5). Lo cambiado, y nada mas: la lista, que son
las filas 1 a 7 de .v73ext/orden.txt; el commit de comparacion, que es 4318e81, la apertura de la 73; y el rotulo de la ultima
linea. En la 73 cambian cuatro fichas por la TAREA 2 (.v73ext/corregir_t2.py), asi que tienen que salir DISTINTAS las cuatro y
solo ellas, e iguales las otras tres. Lo que decia la de la 71: COPIA DE LA VUELTA 71 de .v70ext/pasos_y_huellas.py (encargo de la 71, TAREA 5: la huella de las 20 fichas preparadas,
corrida despues del ultimo cambio de ficha). Lo cambiado: la lista, que son las filas 1 a 20 de .v71ext/orden.txt; el commit de
comparacion, que es 7be17c0, la apertura de la 71; y dos columnas que la de la 70 no necesitaba porque en ella no cambio ninguna
ficha: la cuenta de pasos de la ficha y si el fichero de trabajo es el mismo blob que HEAD (git hash-object), para que la huella
publicada sea la del fichero que se commitea. En la 71 cambian tres fichas por la TAREA 2 (.v71ext/corregir_t2.py), asi que
tienen que salir DISTINTAS las tres y solo ellas, e iguales las otras diecisiete. El blob que imprime es la huella contra la que
la vuelta de insercion comprobara que entra lo que se leyo. Lo demas, la de la 70: """ """en HEAD la busca en
cuarentena/grove_high_output/ y, si ya no esta, en cuarentena/_insertados/grove_high_output/."""
import io, json, subprocess
BASE = '4318e81'
git = lambda *a: subprocess.run(['git'] + list(a), capture_output=True, text=True, encoding='utf-8').stdout
ruta = lambda i: 'cuarentena/grove_high_output/%s.json' % i
hoy = lambda i: ruta(i) if subprocess.run(['git', 'cat-file', '-e', 'HEAD:' + ruta(i)], stderr=subprocess.DEVNULL).returncode == 0 else 'cuarentena/_insertados/grove_high_output/%s.json' % i
filas = [l.split() for l in io.open('.v73ext/orden.txt', encoding='utf-8') if l[:1].isdigit()]
lista = [f[1] for f in filas if 1 <= int(f[0]) <= 7]
iguales = distintos = trabajo_distinto = pasos = 0
for k, i in enumerate(lista, 1):
    x = git('rev-parse', '%s:%s' % (BASE, ruta(i))).strip(); y = git('rev-parse', 'HEAD:' + hoy(i)).strip()
    w = git('hash-object', hoy(i)).strip()
    n = len(json.load(io.open(hoy(i), encoding='utf-8'))['pasos_accionables']); pasos += n
    if x and x == y: iguales += 1
    else: distintos += 1
    if w != y: trabajo_distinto += 1
    print('%-3d %-60s %s %2d pasos %s %s %s' % (k, i, 'bandeja   ' if hoy(i) == ruta(i) else '_insertados', n, y[:10],
          'igual' if x and x == y else 'DISTINTA', 'trabajo=HEAD' if w == y else 'TRABAJO DISTINTO DE HEAD'))
print('fichas de las filas 1 a 7: %d | pasos: %d | iguales a su blob en %s: %d | distintas: %d | fichero de trabajo distinto de HEAD: %d' % (
    len(lista), pasos, BASE, iguales, distintos, trabajo_distinto))
