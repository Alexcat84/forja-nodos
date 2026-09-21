# PRIMERA LINEA (HEREDADO 4): CERO IDS Y CERO RANGOS TECLEADOS EN LA CUENTA.
# Los rangos salen del propio fichero fuente: se corta por rotulo, no por linea escrita a mano.
# Lo unico tecleado es el nombre del fichero fuente, que es el sujeto del instrumento.
import io, re, sys
RUTA = 'fuentes/scott_radical_candor/cap_08.md'
lineas = io.open(RUTA, encoding='utf-8').read().split('\n')
# cuerpo = todo lo que va despues del frontmatter (dos lineas '---')
ini = [n for n,l in enumerate(lineas) if l.strip()=='---'][1] + 1
def pal(txt):
    return len(re.findall(r"[A-Za-z0-9’'-]+", txt))
cuerpo = '\n'.join(lineas[ini:])
print("FICHERO: %s   lineas del fichero: %d   cuerpo desde la linea %d" % (RUTA, len(lineas)-1, ini+1))
print("PALABRAS DEL CUERPO ENTERO DEL CAPITULO: %d" % pal(cuerpo))
print()
# tramo FREE AT WORK: del rotulo en mayusculas a la siguiente linea en mayusculas
rot = [n for n,l in enumerate(lineas) if l.strip() and l.strip()==l.strip().upper() and len(l.strip())>6 and not l.startswith('---')]
print("ROTULOS EN MAYUSCULAS QUE EL FICHERO TRAE, con su linea (1-indexada):")
for n in rot:
    print("   L%-4d %s" % (n+1, lineas[n].strip()))
print()
for k,n in enumerate(rot):
    fin = rot[k+1] if k+1 < len(rot) else len(lineas)
    tramo = '\n'.join(lineas[n+1:fin])
    print("   tramo tras %-42s L%-4d a L%-4d  palabras de cuerpo: %d"
          % (lineas[n].strip()[:42], n+2, fin, pal(tramo)))
