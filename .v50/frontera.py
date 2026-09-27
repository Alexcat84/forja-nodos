# -*- coding: utf-8 -*-
"""MI LECTURA DE LA FRONTERA DE cap_05, PUBLICADA ANTES DE MINAR NADA (EXTRACTOR.md 10).

Es el mismo instrumento que la vuelta 46 corrio sobre cap_04 (.v46/frontera.py), con MI
lectura de cap_05 dentro, y con la tercera cifra de control que el encargo de la vuelta 50
pide ademas de las dos de siempre: CARACTERES DE CUERPO. CERO CONSTANTES TECLEADAS QUE EL
FICHERO PUEDA DAR: la cabecera se localiza buscando el segundo guion triple, las palabras y
los caracteres se cuentan del fichero y la cita de cada fila la imprime el instrumento de la
linea (D.35: la cita se pega, no se promete). Lo unico que pongo yo son los TRAMOS y el
rotulo de cada uno, que son mi lectura.

Y EL REMEDIO BLOQUEANTE HEREDADO: la cuenta de nodos se publica rotulada con la poblacion
que se conto, que aqui es UNA unidad, cap_05, y no el libro.
"""
import io
import sys
import unicodedata

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")


def llana(texto):
    texto = texto.replace(chr(0x2014), "-").replace(chr(0x2013), "-")
    texto = texto.replace(chr(0x2018), "'").replace(chr(0x2019), "'")
    texto = texto.replace(chr(0x201C), '"').replace(chr(0x201D), '"')
    texto = texto.replace(chr(0x2026), "...")
    return "".join(c for c in unicodedata.normalize("NFD", texto)
                   if unicodedata.category(c) != "Mn")


# MI LECTURA. La cuarta columna es cuantos nodos da el tramo.
TRAMOS = {
    "cap_05": [
        ("L9 a L11", 9, 11, 0,
         "P1  rotulos: el numero 4 y el titulo textual Meetings, The Medium of Managerial Work"),
        ("L13 a L13", 13, 13, 0,
         "P2  la mala fama de la reunion, con Drucker y Whyte citados: POSTURA con cifras de otros autores"),
        ("L15 a L15", 15, 15, 0,
         "P3  la reunion es el medio por el que se hace el trabajo de mando: DEFINICION, no hay nada que ejecutar"),
        ("L17 a L17", 17, 17, 0,
         "P4  las DOS clases de reunion, de proceso y de mision: DEFINICION, nombra sin poner inventario de medios"),
        ("L19 a L19", 19, 19, 0,
         "P5  rotulo de seccion Process-Oriented Meetings, sin cuerpo que extraer"),
        ("L21 a L21", 21, 21, 1,
         "P6  INFUNDIR REGULARIDAD A LA REUNION DE PROCESO: sus medios nombrados uno a uno y el control de produccion"),
        ("L23 a L23", 23, 23, 1,
         "P7  CABEZA DE SERIE: las TRES clases de reunion de proceso, contadas y nombradas una a una"),
        ("L25 a L25", 25, 25, 0,
         "P8  rotulo ONE-ON-ONES, sin cuerpo que extraer"),
        ("L27 a L29", 27, 29, 0,
         "P9  que es el uno a uno y para que sirve, mas las clases privadas del autor: DEFINICION mas CASO"),
        ("L31 a L31", 31, 31, 0,
         "P10 con quien se tiene: el autor acota DE QUE va a hablar, y acotar el alcance no es procedimentar"),
        ("L33 a L35", 33, 35, 1,
         "P11 CADA CUANTO: la madurez relevante para la tarea y la velocidad de cambio del area, con sus dos frecuencias"),
        ("L37 a L39", 37, 39, 1,
         "P12 CUANTO DURA Y DONDE: la hora como minimo y el area de trabajo del subordinado, con lo que alli se aprende"),
        ("L41 a L41", 41, 41, 1,
         "P13 LA REUNION ES DEL SUBORDINADO: el guion que el prepara y el paseo por el material"),
        ("L43 a L43", 43, 43, 1,
         "P14 QUE SE TRATA: los indicadores, lo ocurrido desde la ultima, el problema potencial y la intuicion"),
        ("L45 a L47", 45, 47, 1,
         "P15 EL PAPEL DEL SUPERVISOR y el principio de una pregunta mas, con la frase de Drucker dentro"),
        ("L49 a L49", 49, 49, 1,
         "P16 LAS PISTAS MECANICAS: las dos copias del guion, las notas, y lo que escribirlo simboliza"),
        ("L51 a L51", 51, 51, 1,
         "P17 EL FICHERO DE ESPERA donde los dos acumulan lo importante y no urgente: la tanda aplicada al uno a uno"),
        ("L53 a L53", 53, 53, 1,
         "P18 LOS ASUNTOS DE CORAZON A CORAZON y la guardia contra el que se suelta al final de la reunion"),
        ("L55 a L55", 55, 55, 1,
         "P19 EL UNO A UNO POR TELEFONO A DISTANCIA: la preparacion que exige y el intercambio de notas despues"),
        ("L57 a L57", 57, 57, 1,
         "P20 PROGRAMAR EN CADENA: fijar el siguiente al terminar el que se tiene, para evitar la cancelacion"),
        ("L59 a L59", 59, 59, 0,
         "P21 la palanca del uno a uno, noventa minutos por ochenta horas: DEFINICION con su cuenta"),
        ("L61 a L63", 61, 63, 0,
         "P22 el uno a uno con el responsable de ventas de Intel: CASO del autor, manual 3.5"),
        ("L65 a L65", 65, 65, 0,
         "P23 el uno a uno en casa con sus hijas: CASO del autor, y el propio libro lo llama digresion"),
        ("L67 a L67", 67, 67, 0,
         "P24 rotulo STAFF MEETINGS, sin cuerpo que extraer"),
        ("L69 a L73", 69, 73, 0,
         "P25 que es la reunion de personal y para que sirve, mas su primer grupo de ingenieros: DEFINICION mas CASO"),
        ("L75 a L75", 75, 75, 1,
         "P26 QUE SE TRATA EN LA REUNION DE PERSONAL: el criterio de mas de dos, y que hacer si degenera en dos"),
        ("L77 a L77", 77, 77, 1,
         "P27 CUANTO SE ESTRUCTURA: la agenda con antelacion y la sesion abierta, con lo que cabe en cada una"),
        ("L79 a L83", 79, 83, 1,
         "P28 EL PAPEL DEL SUPERVISOR en la reunion de personal: moderador y facilitador, y nunca conferenciante"),
        ("L85 a L85", 85, 85, 0,
         "P29 rotulo OPERATION REVIEWS, sin cuerpo que extraer"),
        ("L87 a L87", 87, 87, 0,
         "P30 que es la revision de operaciones y su proposito: DEFINICION con sus FINES, 9.1 restriccion 1"),
        ("L89 a L89", 89, 89, 1,
         "P31 CABEZA DE SERIE: los CUATRO jugadores de la revision, contados y nombrados uno a uno"),
        ("L91 a L91", 91, 91, 1,
         "P32 EL MANDO ORGANIZADOR: sus tareas nombradas una a una, incluida la de llevar el tiempo"),
        ("L93 a L93", 93, 93, 1,
         "P33 EL MANDO REVISOR: preguntar, comentar, dar el espiritu, y no leer el material por adelantado"),
        ("L95 a L95", 95, 95, 1,
         "P34 LOS PRESENTADORES: los apoyos visuales, los cuatro minutos por apoyo, resaltar y vigilar al publico"),
        ("L97 a L97", 97, 97, 1,
         "P35 EL PUBLICO: preguntar, anotar, hablar si no se esta de acuerdo, y dejar constancia del error de hecho"),
        ("L99 a L99", 99, 99, 0,
         "P36 rotulo Mission-Oriented Meetings, sin cuerpo que extraer"),
        ("L101 a L101", 101, 101, 0,
         "P37 que es la reunion de mision y de quien es la culpa si falla: DEFINICION con POSTURA"),
        ("L103 a L103", 103, 103, 1,
         "P38 ANTES DE CONVOCAR: el objetivo claro y las TRES preguntas que hay que contestar que si"),
        ("L105 a L105", 105, 105, 1,
         "P39 EL COSTE EN DINERO de la reunion y que hacer con el: CIFRA DEL AUTOR mas procedimiento propio"),
        ("L107 a L109", 107, 109, 1,
         "P40 LA ASISTENCIA: identificar, conseguir el compromiso, el sustituto con poder, y el corte de ocho"),
        ("L111 a L111", 111, 111, 1,
         "P41 LA DISCIPLINA: no dejar pasar la tardanza y encarar al que llega tarde, con el coste por hora delante"),
        ("L113 a L113", 113, 113, 1,
         "P42 LA LOGISTICA: el equipo de la sala y la agenda que dice el proposito y el papel de cada uno"),
        ("L115 a L169", 115, 169, 0,
         "P43 el ejemplar de agenda de la reunion de Filipinas: CASO del autor reproducido entero, manual 3.5"),
        ("L171 a L171", 171, 171, 0,
         "P44 regimentacion contra disciplina, y el quirofano: POSTURA"),
        ("L173 a L173", 173, 173, 1,
         "P45 EL ACTA DESPUES DE LA REUNION: que resuma, que llegue rapido, y que diga que, quien y cuando"),
        ("L175 a L175", 175, 175, 0,
         "P46 el ochenta contra veinte y la senial de mala organizacion: POSTURA con cifra de Drucker"),
    ],
}

TOPE = 15    # el techo de EXTRACTOR.md 12.4, para contrastar, no para decidir

total_nodos = 0
for unidad in sorted(TRAMOS):
    ruta = "fuentes/grove_high_output/%s.md" % unidad
    lineas = io.open(ruta, encoding="utf-8").read().split("\n")
    cortes = [i for i, l in enumerate(lineas, 1) if l.strip() == "-" * 3]
    fin_cabecera = cortes[1]
    cuerpo = len(" ".join(lineas[fin_cabecera:]).split())
    caracteres = len("\n".join(lineas[fin_cabecera:]))
    fichero = len(" ".join(lineas).split())

    def palabras(desde, hasta):
        return len(" ".join(lineas[desde - 1:hasta]).split())

    def cita(desde):
        return "%d:%s" % (desde, llana(lineas[desde - 1])[:64])

    filas = TRAMOS[unidad]
    cubiertas, solapes = {}, []
    for nombre, desde, hasta, _n, _r in filas:
        for i in range(desde, hasta + 1):
            if i in cubiertas:
                solapes.append((i, cubiertas[i], nombre))
            cubiertas[i] = nombre
    con_contenido = [i for i in range(fin_cabecera + 1, len(lineas) + 1)
                     if lineas[i - 1].strip()]
    sin_cubrir = [i for i in con_contenido if i not in cubiertas]
    suma = sum(palabras(d, h) for _n, d, h, _x, _r in filas)
    nodos = sum(n for _a, _b, _c, n, _d in filas)
    total_nodos += nodos

    print("=" * 78)
    print("1. LA COMPROBACION DE %s, ANTES DE SU TABLA" % unidad)
    print("=" * 78)
    print("fichero                                : %s" % ruta)
    print("la cabecera acaba en la linea          : %d   (segundo guion triple, no tecleado)"
          % fin_cabecera)
    print("tramos de mi lectura                   : %d" % len(filas))
    print("lineas con contenido tras la cabecera  : %d" % len(con_contenido))
    print("lineas NO cubiertas                    : %d  %s" % (len(sin_cubrir), sin_cubrir))
    print("SOLAPES                                : %d  %s" % (len(solapes), solapes))
    print("suma de las filas                      : %d palabras" % suma)
    print("cuerpo medido aparte                   : %d palabras" % cuerpo)
    print("CARACTERES DE CUERPO                   : %d caracteres" % caracteres)
    print("fichero entero, para cruzar con wc -w  : %d palabras" % fichero)
    print("IGUALES                                : %s" % (suma == cuerpo))
    print("NODOS QUE MI FRONTERA DA EN ESTA UNIDAD, cap_05 Y SOLO cap_05: %d" % nodos)
    if suma != cuerpo or sin_cubrir or solapes:
        print("")
        print("LA CUENTA DE NODOS NO SE PUBLICA. Diferencia: %d palabras." % (suma - cuerpo))
        raise SystemExit(1)
    print("")
    print("=" * 78)
    print("2. LA TABLA DE %s, IMPRESA Y NO TECLEADA" % unidad)
    print("=" * 78)
    print("| tramo de %s | palabras | nodos | que es, y por que | la salida, pegada |" % unidad)
    print("|---|---:|---:|---|---|")
    for nombre, desde, hasta, n, razon in filas:
        print("| `%s` | %d | **%d** | %s | `%s` |"
              % (nombre, palabras(desde, hasta), n, razon, cita(desde)))
    print("| | **%d** | **%d** | **el cuerpo entero de %s, cero lineas sin cubrir y cero solapes** | |"
          % (suma, nodos, unidad))
    print("")

print("=" * 78)
print("3. EL TECHO, CONTRASTADO Y NO DECIDIDO AQUI")
print("=" * 78)
print("NODOS QUE MI FRONTERA DA EN LA UNIDAD DE LA VUELTA SIGUIENTE (cap_05): %d" % total_nodos)
print("TECHO DE CANDIDATOS POR VUELTA (EXTRACTOR.md 12.4): entre 5 y %d" % TOPE)
print("DENTRO DEL TECHO                                             : %s"
      % ("SI" if 5 <= total_nodos <= TOPE else "NO"))
print("SI DA NO, MANDA LA REGLA DE PRECEDENCIA DE 12.4: la vuelta cierra en esta unidad,")
print("se mina hasta el techo y la linea del tramo dice en que candidato corto.")
