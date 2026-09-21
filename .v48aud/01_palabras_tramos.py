# -*- coding: utf-8 -*-
"""Cuenta de palabras de los tramos de la tanda de la vuelta 48, LEIDA DEL TEXTO FUENTE
y no de ningun reporte. Los rangos de linea salen de los propios resumen_teorico de las
cinco fichas de cuarentena. Instrumento corrido en la APERTURA CIEGA."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
L = open("fuentes/grove_high_output/cap_04.md", encoding="utf-8").read().split("\n")
def pal(a, b):            # a y b en numeracion 1..N, inclusive
    return sum(len(L[i-1].split()) for i in range(a, b+1))
TRAMOS = [("P34", 273, 285, "candidatos usar_calendario... y decir_no..."),
          ("P36", 289, 289, "candidato llevar_inventario_proyectos_discrecionales"),
          ("P38", 293, 301, "candidato dimensionar_numero_subordinados..."),
          ("P39", 303, 307, "candidato buscar_regularidad_bloques_iguales...")]
print("LOS TRAMOS DE LA TANDA DE LA VUELTA 48, LISTA ORDENADA ENTERA de mas a menos palabras:")
for p, a, b, q in sorted(TRAMOS, key=lambda t: -pal(t[1], t[2])):
    print("   %-4s  L%-3d a L%-3d  %4d palabras   %s" % (p, a, b, pal(a, b), q))
