# -*- coding: utf-8 -*-
"""LA TASA DE d033, CON SU NUMERADOR Y SU DENOMINADOR NOMBRADOS (D.59).

Lee .v54/d033_tasa.txt, que es la salida cruda de las corridas de hoy, y NO
mezcla arboles: la tanda de la ACTA 47 se imprime aparte, con su arbol dicho.
"""
import re

CRUDA = ".v54/d033_tasa.txt"

filas = []
for linea in open(CRUDA, encoding="utf-8"):
    golpe = re.match(r"corrida (\d+)\s+(VERDE|ROJO)\s+(\d+) s", linea.strip())
    if golpe:
        filas.append((int(golpe.group(1)), golpe.group(2), int(golpe.group(3))))

rojas = [f for f in filas if f[1] == "ROJO"]
print("d033: test_e_guion_largo_rompe_el_hook, tasa medida HOY")
print("  arbol de hoy: el de la vuelta 54, con ab9 ya dentro (fixture de D.58 arreglado)")
print("  ROJO de las corridas de hoy            : %d" % len(rojas))
print("    numerador   %d  corridas que salieron ROJO" % len(rojas))
print("    denominador %d  corridas lanzadas hoy sobre el mismo arbol" % len(filas))
if filas:
    print("  tasa de ROJO de hoy                    : %.1f por ciento"
          % (100.0 * len(rojas) / len(filas)))
    print("  segundos por corrida                   : %.1f s" % (
        sum(f[2] for f in filas) / float(len(filas))))
    print("    numerador   %d  suma de segundos de esas corridas" % sum(f[2] for f in filas))
    print("    denominador %d  corridas lanzadas hoy" % len(filas))
print()
print("  LA TANDA DE LA ACTA 47, QUE ES DE OTRO ARBOL Y NO SE SUMA A ESTA:")
print("    1 ROJO de 6 corridas, sobre el arbol de la vuelta 48 (cita: d033)")
print("    NO se promedia con la de hoy: el arbol cambio en medio (ab99b4f).")
