# -*- coding: utf-8 -*-
"""Palabras por RENGLON no vacio de cap_04.md, y palabras de los CUATRO tramos
de la tanda de la vuelta 48 cuyos rangos estan escritos dentro de las fichas de
cuarentena. Instrumento corrido en la APERTURA CIEGA de la vuelta 49, leyendo el
texto fuente y NINGUN reporte."""
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
L=open('fuentes/grove_high_output/cap_04.md',encoding='utf-8').read().split('\n')
tot=sum(len(x.split()) for x in L)
nova=[(i+1,len(x.split())) for i,x in enumerate(L) if x.strip()]
print("cap_04.md: %d renglones, %d no vacios, %d palabras en total" % (len(L),len(nova),tot))
print()
print("LOS 12 RENGLONES MAS LARGOS, LISTA ORDENADA ENTERA de mas a menos:")
for n,w in sorted(nova,key=lambda t:-t[1])[:12]:
    print("   L%-4d %5d palabras" % (n,w))
print()
def pal(a,b): return sum(len(L[i-1].split()) for i in range(a,b+1))
print("LOS TRAMOS DE LA TANDA DE LA VUELTA 48 (rangos leidos de los resumen_teorico de sus fichas):")
for p,a,b in [("P34",273,285),("P36",289,289),("P38",293,301),("P39",303,307)]:
    print("   %-4s L%-3d a L%-3d %5d palabras" % (p,a,b,pal(a,b)))
print()
print("EL TRAMO DE d027, P7 (rango leido de su ficha):")
print("   P7   L145 a L147 %5d palabras" % pal(145,147))
print()
print("RENGLONES DE cap_04 CON MAS DE 396 PALABRAS, que es el techo de P38:")
for n,w in sorted(nova,key=lambda t:-t[1]):
    if w>396: print("   L%-4d %5d palabras" % (n,w))
