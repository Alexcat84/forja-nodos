"""NN.1.c: TODA DIVISION QUE PUBLICO, RECORRIDA CON LOS DOS NUMEROS DE SU PROPIA CELDA.

La vuelta 51 cayo en REPORTE por una division de su tabla del techo que se contradecia
con su propia celda (29,5 min donde la celda escribe 1728,2 s, que son 28,80). Ninguno de
sus trece discutibles era una cifra. Este guion es la consecuencia que la TAREA 1.c pide:
cada division publicada se declara aqui con su numerador y su denominador, se recomputa, y
se compara con lo publicado. Si una no cuadra, sale en rojo.
"""

# (donde vive, que divide, numerador, denominador, lo que publico, tolerancia)
DIVISIONES = [
    ("NN.2.c aviso de coste", "la primera pasada contra la media de la vuelta 51",
     1045.6, 327.0, 3.2, 0.05),
    ("NN.5.f", "media por pasada de la vuelta 52", 4387.4, 6.0, 731.2, 0.05),
    ("NN.5.f", "la suma de relojes en minutos", 4387.4, 60.0, 73.1, 0.05),
    ("NN.5.f", "veces la media de la vuelta 51", 731.2, 327.0, 2.24, 0.005),
    ("NN.5.f", "el techo en minutos que el encargo fija, contra lo que costo",
     4387.4, 42.0, 104.5, 0.5),
    # el denominador NO lo estimo: es len(comun.texto_comparable(ficha)), medido en
    # .v52/peso_resumen.txt sobre la misma ficha y con la misma funcion que usa la aduana.
    ("NN.3.c", "peso del resumen en la ficha de fijar_duracion, sobre su texto comparable",
     11444.0, 12366.0, 0.93, 0.005),
    ("NN.5.e", "PASOS INVENTADOS de cap_05, que es 0 de 84", 0.0, 84.0, 0.0, 0.0001),
    ("NN.5.e", "PASOS INVENTADOS del libro entero, que es 0 de 418", 0.0, 418.0, 0.0, 0.0001),
    ("NN.5.d", "cap_05 en 12 de 26 nodos de su frontera", 12.0, 26.0, 0.4615, 0.0005),
]

print("    %-22s %-56s %10s %10s %9s %9s %s"
      % ("donde", "que divide", "numerador", "denominad", "publico", "recompu", "cuadra"))
todas = True
for donde, que, num, den, publicado, tol in DIVISIONES:
    r = num / den
    # la cifra publicada puede ser el cociente o el cociente redondeado a un decimal
    cuadra = abs(r - publicado) <= tol
    todas = todas and cuadra
    print("    %-22s %-56s %10s %10s %9s %9s %s"
          % (donde, que[:56], ("%.1f" % num).replace(".", ","), ("%.1f" % den).replace(".", ","),
             ("%.4f" % publicado).replace(".", ","), ("%.4f" % r).replace(".", ","),
             "SI" if cuadra else "NO, ROJO"))
print()
print("    divisiones publicadas y recorridas    : %d" % len(DIVISIONES))
print("    TODAS CUADRAN CON SU PROPIA CELDA     : %s" % todas)
