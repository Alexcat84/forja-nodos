# Comprueba con la tabla de LL.4.b, no de memoria: los seis de la vuelta 52 son 1 nodo
# cada uno, y P21, P22 y P23 dan cero, con lo que la seccion del uno a uno queda cerrada.
import re
L = open("docs/loop/REPORTE.md", encoding="utf-8").read().split("\n")
ini = next(n for n, t in enumerate(L) if t.startswith("### LL.4.b."))
fila = re.compile(r"^\| `(L\d+ a L\d+)` \| (\d+) \| \*\*(\d+)\*\* \| (P\d+)\s+(.*?) \|")
suma = 0
print("    de la tabla LL.4.b del reporte de la vuelta 50, leida hoy linea a linea")
print("    %-5s %-14s %9s %7s  %s" % ("pieza", "tramo", "palabras", "nodos", "que es"))
for t in L[ini:ini + 120]:
    m = fila.match(t)
    if not m:
        continue
    tramo, pal, nod, pieza, que = m.groups()
    n = int(pieza[1:])
    if 15 <= n <= 23:
        suma += int(nod)
        print("    %-5s %-14s %9s %7s  %s" % (pieza, tramo, pal, nod, que[:66]))
print()
print("    NODOS DE P15 A P23, sumados de la tabla   : %d" % suma)
print("    de ellos, escritos en la vuelta 52        : 6   (P15 a P20)")
print("    P21, P22 y P23 dan                        : 0   (definicion con su cuenta y dos casos del autor)")
