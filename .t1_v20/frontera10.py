# -*- coding: utf-8 -*-
"""LA FRONTERA DE cap_10, CORTADA ANTES DE EXTRAER (TAREA 3 punto 1 del encargo).

La comprobacion va ANTES de la tabla y no despues: si la suma de las filas no
es el cuerpo medido aparte, NO se publica la cuenta de piezas, se publica la
diferencia (ACTA 18 7.5 orden 1, convertida en obligacion).

La tabla se imprime, no se teclea (EXTRACTOR.md 5), y cada fila lleva pegada
la salida literal de la primera linea de su pieza (D.35). Las comillas
tipograficas y los guiones largos del original van normalizados a grafia
llana, porque la guarda guiones muerde lo que yo escribo.
"""
import unicodedata

F = 'fuentes/scott_radical_candor/cap_10.md'
L = open(F, encoding='utf-8').read().split('\n')

# (pieza, desde, hasta, da nodo, motivo)
P = [
 ("P1",    9,   9, False, "subtitulo del capitulo, 6 palabras. Nada que hacer"),
 ("P2",   11,  13, False, "entrada del capitulo: remite al capitulo tres y describe el problema. Nombrar no es procedimentar"),
 ("P3",   15,  15, False, "rotulo de seccion, 2 palabras, sin cuerpo propio"),
 ("P4",   17,  17, False, "subtitulo de la seccion, 17 palabras, sin cuerpo propio"),
 ("P5",   19,  21, False, "por que hacen falta las conversaciones de carrera y que ganan. Es la razon de la seccion, no un acto: su unico mandato, tenlas con cada persona, lo ejecutan enteras P7, P8 y P9"),
 ("P6",   23,  45, False, "EL CASO DE RUSS LARAWAY, 1.254 palabras: como llego al metodo, con sus dos personas de ejemplo. Manual 3.5, el caso no es la casa: la doctrina vive en P7, P8 y P9 y el caso entra ahi como ejemplo nombrado"),
 ("P7",   47,  59, True,  "la linea 49 pone la primera conversacion con su pregunta de arranque, sus temas y su duracion. Inventario de MEDIOS del propio libro"),
 ("P8",   61,  75, True,  "la linea 69 dice Russ recommends que empieces asi y la 71 manda crear un documento con de tres a cinco columnas. Etapas y objetos nombrados"),
 ("P9",   77,  87, True,  "la linea 79 pone las preguntas y la 81 dice Here is what to do con su lista. Inventario de MEDIOS"),
 ("P10",  89,  91, False, "cierre de la seccion: dice que esto es una vista de alto nivel y remite a una web y a un libro que Russ esta escribiendo. Remite al procedimiento de otro, que es el caso literal de la vara madre"),
 ("P11",  93,  93, False, "rotulo de seccion, 2 palabras"),
 ("P12",  95,  95, False, "subtitulo de la seccion, 15 palabras, sin cuerpo propio"),
 ("P13",  97,  99, True,  "la linea 99 manda armar un plan de gestion del crecimiento para cada persona una vez al anio y mirar el equipo entero para cruzar aspiraciones con necesidades. Acto con su periodo escrito por el libro"),
 ("P14", 101, 105, True,  "actos nombrados: escribir los nombres en sus casillas, identificar a los que estan fuera, y buscar una mirada de fuera que conozca el trabajo"),
 ("P15", 107, 113, True,  "manda un plan de crecimiento de tres a cinco puntos por persona, con proyectos que lo sostengan, y dice que hacer con quien hace mal trabajo y no mejora"),
 ("P16", 115, 119, True,  "actos nombrados: comparar notas con los iguales, y si diriges jefes, montar una via para que todos vean lo mismo"),
 ("P17", 121, 125, True,  "actos nombrados: comprobar la equidad entre niveles y no solo dentro del equipo propio"),
 ("P18", 127, 127, False, "rotulo de seccion, 6 palabras"),
 ("P19", 129, 129, True,  "la linea 129 pone el acto y su criterio: mirar la proporcion del equipo y, si tienes demasiados superestrellas, contratar una estrella de roca a continuacion"),
 ("P20", 131, 131, False, "rotulo, 1 palabra"),
 ("P21", 133, 163, True,  "la linea 135 cierra con here are some simple things you can do y detras van SEIS practicas rotuladas. Inventario de MEDIOS del propio libro, y el mismo corte que P24 y P27 de cap_09"),
 ("P22", 165, 165, False, "rotulo de seccion, 1 palabra"),
 ("P23", 167, 167, False, "subtitulo de la seccion, 3 palabras"),
 ("P24", 169, 173, True,  "la linea 173 dice if you do three things, you can make it far easier y las nombra debajo. LA CUENTA ESTA ESCRITA: es la cabeza de una serie D.37 de TRES"),
 ("P25", 175, 179, True,  "la linea 179 pone CUATRO razones numeradas por el texto para identificar pronto el bajo desempenio. Serie numerada del propio libro"),
 ("P26", 181, 187, True,  "actos nombrados: pedir consejo al jefe, calibrar con los iguales, documentar con quien sepa, y escribir tu los correos y el plan de mejora"),
 ("P27", 189, 195, True,  "actos nombrados: respirar y dar un paso atras, no quedarse atrapado en el consejo legal, y despedir con humildad"),
 ("P28", 197, 201, True,  "actos nombrados con su periodo escrito: escribir al mes, mantener la oreja en el suelo, y seguir siendo franco con quien se fue"),
 ("P29", 203, 203, False, "rotulo de seccion, 1 palabra"),
 ("P30", 205, 223, True,  "la linea 213 cierra con here are some tips for preventing the politics y detras van CINCO rotuladas. Inventario de MEDIOS"),
 ("P31", 225, 225, False, "rotulo de seccion, 4 palabras"),
 ("P32", 227, 227, False, "subtitulo de la seccion, 8 palabras, sin cuerpo propio"),
 ("P33", 229, 237, True,  "actos nombrados: no obsesionarse con el ascenso, anunciar el cambio de papel, y pensar que se elogia en publico"),
 ("P34", 239, 243, True,  "el acto y su distincion escrita: dar las gracias, y en que se diferencia de elogiar"),
 ("P35", 245, 247, True,  "actos nombrados: reconocer a alguien como referente de su area y darle el papel que eso lleva"),
 ("P36", 249, 251, True,  "el acto: dar a esa persona presentaciones publicas como manera de reconocer lo que hace"),
 ("P37", 253, 255, False, "la linea 255 dice I have developed a simple chart y el grafico NO esta en el recorte. Mapa sin sentidos: no es medio mapa, no es nada"),
 ("P38", 257, 259, False, "resumen del capitulo: nombra los seis trabajos y no trae procedimiento propio de ninguno. Nombrar no es procedimentar"),
 ("P39", 261, 263, False, "cabecera del capitulo siguiente, 8. RESULTS, 2 palabras"),
]


def llana(s):
    s = (s.replace(u"\u2014", ' ').replace(u"\u2013", ' ')
          .replace(u"\u2019", "'").replace(u"\u2018", "'")
          .replace(u"\u201c", '"').replace(u"\u201d", '"')
          .replace(u"\u2026", '...'))
    return ''.join(c for c in unicodedata.normalize('NFKD', s)
                   if not unicodedata.combining(c))


def pal(a, b):
    return sum(len(L[k - 1].split()) for k in range(a, b + 1))


# LA COMPROBACION, ANTES DE LA TABLA
contenido = set(i for i, l in enumerate(L[7:], start=8) if l.strip())
cubiertas = []
for _, a, b, _, _ in P:
    cubiertas.extend(range(a, b + 1))
sin_cubrir = sorted(contenido - set(cubiertas))
solapes = sorted(set(x for x in cubiertas if cubiertas.count(x) > 1))
nocont = sorted(set(cubiertas) - contenido - set(
    i for i, l in enumerate(L[7:], start=8) if not l.strip()))
suma = sum(pal(a, b) for _, a, b, _, _ in P)
cuerpo = sum(len(l.split()) for l in L[7:])

print("$ python .t1_v20/frontera10.py    (la comprobacion va ANTES de la tabla)")
print("piezas                                 : %d" % len(P))
print("lineas con contenido de L8 en adelante : %d" % len(contenido))
print("lineas NO cubiertas                    : %d  %s" % (len(sin_cubrir), sin_cubrir))
print("SOLAPES                                : %d  %s" % (len(solapes), solapes))
print("cubiertas que no son contenido         : %d" % len(nocont))
print("suma de las filas                      : %d palabras" % suma)
print("cuerpo medido aparte (sed 8,$ | wc -w) : %d palabras" % cuerpo)
print("IGUALES                                : %s" % (suma == cuerpo))
print()
if suma != cuerpo or sin_cubrir or solapes:
    print("LA CUENTA DE PIEZAS NO SE PUBLICA. LA DIFERENCIA ES: %d palabras" % (suma - cuerpo))
    raise SystemExit(1)

print("| pieza | tramo | palabras | da nodo? | **la salida, pegada** |")
print("|---|---|---:|---|---|")
for n, a, b, da, _ in P:
    prim = llana(L[a - 1].strip())[:86]
    print("| **%s** | `L%d` a `L%d` | %d | **%s** | `%d:%s` |"
          % (n, a, b, pal(a, b), 'SI' if da else 'NO', a, prim))
print()
print("| pieza | **da nodo?** | motivo |")
print("|---|---|---|")
for n, a, b, da, m in P:
    print("| **%s** `L%d`%s | **%s** | %s |"
          % (n, a, (' a `L%d`' % b) if b != a else '', 'SI' if da else 'NO', m))
print()
si = [n for n, _, _, da, _ in P if da]
print("piezas de la frontera        : %d" % len(P))
print("piezas que DAN NODO          : %d   %s" % (len(si), ' '.join(si)))
print("piezas que NO dan nodo       : %d" % (len(P) - len(si)))
print("palabras de las que dan nodo : %d de %d"
      % (sum(pal(a, b) for _, a, b, da, _ in P if da), cuerpo))
