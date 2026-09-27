# frontera.py  --  CERO CONSTANTES TECLEADAS: todo sale del fichero que recibe.
# Uso: python .vg01c/frontera.py <ruta.md>
# Corta el cuerpo (lo que hay debajo del segundo '---' del frontmatter) en
# lineas no vacias y publica numero de linea, palabras y los primeros caracteres.
import sys, io
ruta = sys.argv[1]
n_cab = int(sys.argv[2]) if len(sys.argv) > 2 else 0
lineas = io.open(ruta, encoding='utf-8').read().split('\n')
# fin del frontmatter: segundo '---'
marcas = [i for i, l in enumerate(lineas) if l.strip() == '---']
ini = marcas[1] + 1 if len(marcas) >= 2 else 0
print('INSTRUMENTO frontera.py  SIN CONSTANTES TECLEADAS: fichero=%s' % ruta)
print('frontmatter termina en la linea %d (segundo ---)' % (marcas[1] + 1))
total = 0
cuerpo = 0
for i, l in enumerate(lineas):
    if i < ini:
        continue
    t = l.strip()
    if not t:
        continue
    p = len(t.split())
    total += p
    cuerpo += 1
    print('L%-4d %5d  %s' % (i + 1, p, t[:n_cab] if n_cab else ''))
print('LINEAS NO VACIAS DE CUERPO: %d' % cuerpo)
print('PALABRAS DE CUERPO (suma de filas): %d' % total)
