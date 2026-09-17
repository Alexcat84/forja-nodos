# cuerpo.py: palabras del CUERPO de cada unidad (lo que hay tras el segundo '---'),
# derivado del fichero. Ninguna constante tecleada: el arranque se busca, no se pone.
import sys, glob, os
total = 0
for ruta in sorted(glob.glob(os.path.join(sys.argv[1], 'cap_*.md'))):
    lineas = open(ruta, encoding='utf-8', errors='replace').read().splitlines()
    cortes = [i for i, l in enumerate(lineas) if l.strip() == '---']
    desde = cortes[1] + 1 if len(cortes) >= 2 else 0
    cuerpo = lineas[desde:]
    palabras = sum(len(l.split()) for l in cuerpo)
    total += palabras
    print("%-10s arranque del cuerpo L%-4d lineas del fichero %-5d palabras del cuerpo %d"
          % (os.path.basename(ruta)[:-3], desde + 1, len(lineas), palabras))
print("TOTAL de las %d unidades: %d palabras de cuerpo" % (len(glob.glob(os.path.join(sys.argv[1],'cap_*.md'))), total))
