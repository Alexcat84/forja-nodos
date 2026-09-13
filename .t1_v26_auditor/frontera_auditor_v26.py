import io, sys, re
# Corta un capitulo en PIEZAS por rangos de linea dados y cierra al digito
# contra el cuerpo (todo lo que no es cabecera yaml ni linea en blanco).
ruta = sys.argv[1]
rangos = []  # (etiqueta, ini, fin, clase)
for a in sys.argv[2:]:
    et, ini, fin, cl = a.split(":")
    rangos.append((et, int(ini), int(fin), cl))
lineas = io.open(ruta, encoding="utf-8").read().split("\n")
def pal(txt):
    return len([w for w in txt.split() if w.strip()])
# cuerpo = de la linea 8 al final, sin blancos
cuerpo_n = 0
usadas = set()
for i in range(8, len(lineas)+1):
    t = lineas[i-1] if i-1 < len(lineas) else ""
    if t.strip():
        cuerpo_n += pal(t)
print("FICHERO:", ruta)
print("CUERPO (linea 8 al final, sin blancos):", cuerpo_n, "palabras")
print("-"*90)
tot = 0
for et, ini, fin, cl in rangos:
    n = 0
    for i in range(ini, fin+1):
        t = lineas[i-1] if i-1 < len(lineas) else ""
        if t.strip():
            n += pal(t)
            if i in usadas: print("  !! LINEA REPETIDA:", i)
            usadas.add(i)
    tot += n
    print("%-6s L%-3d-L%-3d  %-12s %5d palabras" % (et, ini, fin, cl, n))
print("-"*90)
print("SUMA DE PIEZAS:", tot)
print("CUERPO        :", cuerpo_n)
print("RESIDUO (cuerpo - piezas):", cuerpo_n - tot)
faltan = [i for i in range(8, len(lineas)+1) if (lineas[i-1] if i-1 < len(lineas) else "").strip() and i not in usadas]
print("LINEAS DE CUERPO NO ASIGNADAS:", faltan)
