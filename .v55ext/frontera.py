# -*- coding: utf-8 -*-
"""MI LECTURA DE LA FRONTERA DE cap_09 Y cap_10, PUBLICADA ANTES DE MINAR NADA.

Mismo instrumento que la vuelta 53 corrio sobre cap_06, cap_07 y cap_08 (.v53/frontera.py),
con MI lectura de los dos capitulos de hoy dentro, y sin tocar una linea de su maquinaria:
esto no fabrica instrumento nuevo (EXTRACTOR.md 13), reusa el que ya existe. CERO CONSTANTES
TECLEADAS QUE EL FICHERO PUEDA DAR: la cabecera se localiza buscando el segundo guion triple,
las palabras y los caracteres se cuentan del fichero, y la cita de cada fila la imprime el
instrumento de la linea (D.35: la cita se pega, no se promete). Lo unico que pongo yo son los
TRAMOS, el rotulo de cada uno y los NODOS QUE PREVE, que son mi lectura y lo que el auditor
siguiente recomputa.

LA CUENTA DE NODOS SE PUBLICA ROTULADA CON LA POBLACION QUE SE CONTO, que aqui es UNA unidad
cada vez, y no el libro.
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


# MI LECTURA. La cuarta columna es cuantos nodos preve el tramo.
TRAMOS = {
    "cap_09": [
        ("L9 a L11", 9, 11, 0,
         "P1  rotulos: el numero 8 y el titulo textual Hybrid Organizations"),
        ("L13 a L13", 13, 13, 0,
         "P2  lo que le paso a la fabrica de desayunos le pasa a toda organizacion grande: POSTURA de apertura"),
        ("L15 a L15", 15, 15, 0,
         "P3  las cajas negras del mando intermedio conectadas entre si: DEFINICION de enlace"),
        ("L17 a L17", 17, 17, 0,
         "P4  la forma orientada a mision descrita sobre la fabrica de desayunos: DEFINICION con CASO, manual 3.5"),
        ("L19 a L19", 19, 19, 0,
         "P5  pie de figura de las dos formas extremas, sin cuerpo que extraer"),
        ("L21 a L21", 21, 21, 0,
         "P6  la forma totalmente funcional, el reverso de P4: DEFINICION"),
        ("L23 a L23", 23, 23, 0,
         "P7  el compromiso entre las dos y la frase de Sloan: POSTURA, su criterio es appropriate compromise"),
        ("L25 a L25", 25, 25, 0,
         "P8  Intel como hibrido y la analogia del ejercito: DEFINICION con CASO del autor, manual 3.5"),
        ("L27 a L27", 27, 27, 0,
         "P9  los grupos funcionales como subcontratistas internos: DEFINICION"),
        ("L29 a L29", 29, 29, 0,
         "P10 pie de figura del hibrido de Intel, sin cuerpo que extraer"),
        ("L31 a L31", 31, 31, 0,
         "P11 las ventajas de organizar en grupos funcionales: inventario de VENTAJAS, de FINES, 9.1 restriccion 1"),
        ("L33 a L33", 33, 33, 0,
         "P12 las desventajas, con la sobrecarga de informacion a la cabeza: DIAGNOSTICO, ningun medio nombrado"),
        ("L35 a L35", 35, 35, 0,
         "P13 la unica ventaja de la forma de mision, la capacidad de respuesta: POSTURA"),
        ("L37 a L37", 37, 37, 0,
         "P14 no hay alternativa a la estructura hibrida, probada muchas veces: POSTURA"),
        ("L39 a L39", 39, 39, 0,
         "P15 la linea que presenta la nota de prensa: enlace, sin cuerpo que extraer"),
        ("L41 a L41", 41, 41, 0,
         "P16 rotulo ABC TECHNOLOGIES REALIGNS, sin cuerpo que extraer"),
        ("L43 a L45", 43, 45, 0,
         "P17 la nota de prensa entera con los nombres cambiados: CASO, manual 3.5"),
        ("L47 a L47", 47, 47, 0,
         "P18 la nota leida contra el patron que el capitulo describio: analisis del CASO"),
        ("L49 a L49", 49, 49, 0,
         "P19 la ley de Grove: POSTURA enunciada como ley, sin nada que ejecutar"),
        ("L51 a L51", 51, 51, 0,
         "P20 la institucion educativa como hibrido: CASO, manual 3.5"),
        ("L53 a L53", 53, 53, 0,
         "P21 Junior Achievement y sus capitulos locales: CASO, manual 3.5"),
        ("L55 a L55", 55, 55, 0,
         "P22 el bufete mediano y su comite ejecutivo: CASO, manual 3.5"),
        ("L57 a L57", 57, 57, 0,
         "P23 los conglomerados como unica excepcion, y por que lo son: DEFINICION de la excepcion"),
        ("L59 a L59", 59, 59, 0,
         "P24 el vaiven entre los dos polos: su criterio son pragmatic considerations, 9.1 restriccion 2"),
        ("L61 a L61", 61, 61, 0,
         "P25 la tarea mas importante del hibrido: POSTURA, optimum and timely es adjetivo de adecuacion"),
        ("L63 a L63", 63, 63, 0,
         "P26 los asignadores centrales y la Hungria del autor: CASO con POSTURA, manual 3.5"),
        ("L65 a L65", 65, 65, 0,
         "P27 las DOS cosas que el mando intermedio necesita: la segunda NOMBRA el procedimiento del capitulo siguiente, vara madre 9"),
    ],
    "cap_10": [
        ("L9 a L11", 9, 11, 0,
         "P1  rotulos: el numero 9 y el titulo textual Dual Reporting"),
        ("L13 a L13", 13, 13, 0,
         "P2  la luna, los contratistas y el nacimiento de la gestion matricial: CASO historico, manual 3.5"),
        ("L15 a L15", 15, 15, 0,
         "P3  la idea nuclear de la matriz y el principio de la doble dependencia: DEFINICION"),
        ("L17 a L17", 17, 17, 0,
         "P4  rotulo Where Should Plant Security Report, sin cuerpo que extraer"),
        ("L19 a L19", 19, 19, 0,
         "P5  las dos opciones para la seguridad de las plantas: CASO del autor, manual 3.5"),
        ("L21 a L21", 21, 21, 0,
         "P6  la salida del dilema y el reparto entre los dos jefes: doctrina del CASO, y su nodo es P17"),
        ("L23 a L23", 23, 23, 0,
         "P7  el staff que no acaba de aceptarlo y el si titubeante: CASO, manual 3.5"),
        ("L25 a L25", 25, 25, 0,
         "P8  como se llega a ser mando y por que el jefe no domina la especialidad: DEFINICION con CASO del vendedor"),
        ("L27 a L27", 27, 27, 0,
         "P9  por que no se arregla funcionalizando del todo: POSTURA, y anuncia que la salida es la doble dependencia"),
        ("L29 a L29", 29, 29, 0,
         "P10 como nace un grupo de pares que hace de supervisor tecnico: CASO narrado, manual 3.5"),
        ("L31 a L31", 31, 31, 0,
         "P11 la entrega voluntaria de la decision individual al grupo, con la analogia del viaje: POSTURA"),
        ("L33 a L33", 33, 33, 0,
         "P12 pie de figura de los dos supervisores, sin cuerpo que extraer"),
        ("L35 a L35", 35, 35, 0,
         "P13 la confianza como rasgo de cultura y no como principio de organizacion: DEFINICION"),
        ("L37 a L37", 37, 37, 0,
         "P14 la ambiguedad que el sistema impone y por que no existe algo mas simple: POSTURA"),
        ("L39 a L39", 39, 39, 0,
         "P15 no es que a Intel le guste la ambiguedad, es que lo demas no funciono: POSTURA"),
        ("L41 a L41", 41, 41, 0,
         "P16 rotulo Making Hybrid Organizations Work, sin cuerpo que extraer"),
        ("L43 a L43", 43, 43, 1,
         "P17 REPARTIR LA SUPERVISION DE UN PUESTO entre su grupo funcional y su division, con lo que toca a cada uno nombrado"),
        ("L45 a L45", 45, 45, 0,
         "P18 la publicidad, sus pros y sus contras a los dos lados: CASO con PREGUNTAS, manual 3.5"),
        ("L47 a L47", 47, 47, 0,
         "P19 pie de figura del controller supervisado por las dos organizaciones, sin cuerpo que extraer"),
        ("L49 a L49", 49, 49, 0,
         "P20 la solucion del caso de la publicidad: CASO resuelto, su doctrina es la de P17, manual 3.5"),
        ("L51 a L51", 51, 51, 0,
         "P21 la paciencia que la doble dependencia le cuesta al jefe de marketing: POSTURA"),
        ("L53 a L53", 53, 53, 0,
         "P22 la linea que presenta la nota de Ohio University: enlace, sin cuerpo que extraer"),
        ("L55 a L55", 55, 55, 0,
         "P23 la nota de Ohio University con los corchetes del autor: CASO citado, manual 3.5"),
        ("L57 a L57", 57, 57, 0,
         "P24 el hibrido como consecuencia inevitable, con sus tres recortes: su criterio es unnecessary y common sense, 9.1 restriccion 2"),
        ("L59 a L59", 59, 59, 0,
         "P25 rotulo Another Wrinkle, The Two-Plane Organization, sin cuerpo que extraer"),
        ("L61 a L61", 61, 61, 0,
         "P26 la variante sutil que aparece cuando alguien coordina fuera de su trabajo diario: DEFINICION"),
        ("L63 a L63", 63, 63, 0,
         "P27 Cindy y su grupo de coordinacion entre plantas: CASO del autor, manual 3.5, y su cadencia es dato del caso"),
        ("L65 a L65", 65, 65, 0,
         "P28 los dos organigramas en los que aparece el nombre de Cindy: CASO leido, manual 3.5"),
        ("L67 a L67", 67, 67, 0,
         "P29 pie de figura de los dos organigramas de Cindy, sin cuerpo que extraer"),
        ("L69 a L69", 69, 69, 0,
         "P30 el plano distinto y la analogia de la parroquia: DEFINICION con ilustracion"),
        ("L71 a L71", 71, 71, 0,
         "P31 la palanca que los grupos de coordinacion dan al mando de conocimiento: POSTURA"),
        ("L73 a L73", 73, 73, 0,
         "P32 los dos planos en la vida diaria, y el tercero: DEFINICION con ilustracion"),
        ("L75 a L75", 75, 75, 0,
         "P33 la relacion invertida entre planos, con el autor bajo su propio controller: CASO, manual 3.5"),
        ("L77 a L77", 77, 77, 0,
         "P34 para que le sirve al autor la organizacion multiplano: POSTURA"),
        ("L79 a L79", 79, 79, 0,
         "P35 los grupos temporales y el cierre que anuncia el capitulo siguiente: DEFINICION de cierre"),
    ],
}

TOPE = 30    # el techo de candidatos de D.58 en regimen ligero, para contrastar, no para decidir

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
    print("NODOS QUE MI FRONTERA DA EN ESTA UNIDAD, %s Y SOLO %s: %d"
          % (unidad, unidad, nodos))
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
print("NODOS QUE MI FRONTERA DA EN LAS DOS UNIDADES NUEVAS DE HOY: %d" % total_nodos)
print("MAS LOS QUE LE FALTABAN A cap_07 POR SU FRONTERA DE LA VUELTA 53: 8")
print("CANDIDATOS QUE ESTA VUELTA SE PROPONE ESCRIBIR                 : %d" % (total_nodos + 8))
print("TECHO DE CANDIDATOS DE D.58 EN REGIMEN LIGERO                  : %d" % TOPE)
print("DENTRO DEL TECHO DE CANDIDATOS                                 : %s"
      % ("SI" if total_nodos + 8 <= TOPE else "NO"))
