# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 68 de .v67ext/pasos_y_huellas.py (encargo, TAREA 4, la huella de las 20 fichas preparadas), con la
lista cambiada a las filas 1 a 20 de .v68ext/orden.txt (cap_05 y cap_06) y el commit cambiado a fd190d7, la apertura de la
68: ninguna ficha de las 20 se toco en esta vuelta, asi que tienen que salir iguales a su blob de la apertura, y el blob
que imprime es la huella contra la que la 70 comprobara que entra lo que se leyo. Compara el blob de cada ficha en d8f4e2a contra HEAD;
en HEAD la busca en cuarentena/grove_high_output/ y, si ya no esta, en cuarentena/_insertados/grove_high_output/."""
import io, subprocess
BASE = 'fd190d7'
git = lambda *a: subprocess.run(['git'] + list(a), capture_output=True, text=True, encoding='utf-8').stdout
ruta = lambda i: 'cuarentena/grove_high_output/%s.json' % i
hoy = lambda i: ruta(i) if subprocess.run(['git', 'cat-file', '-e', 'HEAD:' + ruta(i)], stderr=subprocess.DEVNULL).returncode == 0 else 'cuarentena/_insertados/grove_high_output/%s.json' % i
filas = [l.split() for l in io.open('.v68ext/orden.txt', encoding='utf-8') if l[:1].isdigit()]
lista = [f[1] for f in filas if 1 <= int(f[0]) <= 20]
iguales = distintos = 0
for k, i in enumerate(lista, 1):
    x = git('rev-parse', '%s:%s' % (BASE, ruta(i))).strip(); y = git('rev-parse', 'HEAD:' + hoy(i)).strip()
    if x and x == y: iguales += 1
    else: distintos += 1
    print('%-3d %-56s %s %s %s' % (k, i, 'bandeja   ' if hoy(i) == ruta(i) else '_insertados', y[:10], 'igual' if x and x == y else 'DISTINTA'))
print('fichas de las filas 1 a 20: %d | iguales a su blob en %s: %d | distintas: %d' % (len(lista), BASE, iguales, distintos))
