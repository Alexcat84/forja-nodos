# -*- coding: utf-8 -*-
"""Las dos caidas de PROSA de la vuelta 54, localizadas por su linea."""
import glob
rep = open("docs/loop/REPORTE.md", encoding="utf-8", errors="replace").read().splitlines()
ini = next(i for i, l in enumerate(rep) if l.startswith("# VUELTA 54 DE LA LINEA SERIAL"))
v54 = rep[ini:]
print("LA VUELTA 54 DEL REPORTE: lineas %d a %d" % (ini + 1, len(rep)))
print()
print("A. LA MISMA RUTA PEGADA DOS VECES CON DOS SALIDAS DISTINTAS")
for i, l in enumerate(v54):
    if "deuda_cierre.txt" in l:
        print("   linea %d del fichero: %s" % (ini + i + 1, l.strip()))
        for j in range(i + 1, min(i + 8, len(v54))):
            if "pendientes:" in v54[j]:
                print("        -> pega: %s" % v54[j].strip()); break
print("   $ grep -n 'pendientes:' .v54/deuda_cierre.txt   (la ruta que las dos citan, hoy)")
for n, l in enumerate(open(".v54/deuda_cierre.txt", encoding="utf-8"), 1):
    if "pendientes:" in l: print("        %d:%s" % (n, l.rstrip()))
print()
print("B. EL DENOMINADOR DEL BARRIDO DE LA PREGUNTA 11")
for i, l in enumerate(v54):
    if "fichas de cuarentena barridas" in l or "documentos barridos" in l:
        print("   linea %d: %s" % (ini + i + 1, l.strip()))
n = len(glob.glob("cuarentena/**/*.json", recursive=True))
der = len(glob.glob("cuarentena/_derivadas/*.json"))
print("   $ find cuarentena -name '*.json' | wc -l")
print("        %d" % n)
print("   $ ls cuarentena/_derivadas/*.json | wc -l")
print("        %d" % der)
print("   la cifra publicada, %d, es %d menos las %d de _derivadas." % (n - der, n, der))
print("   mi barrido propio sobre los %d va en .v55aud/p11_barrido_propio.txt: las mismas 4." % (346 + n))
