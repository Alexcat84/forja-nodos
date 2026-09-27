# -*- coding: utf-8 -*-
"""MI LECTURA DE LA FRONTERA DE LAS DOS UNIDADES QUE MINO, PUBLICADA ANTES DE CORTAR
(EXTRACTOR.md 10, y TAREA 1 del encargo: se cierra contra el cuerpo o no se publica
ninguna cuenta de nodos).

CERO CONSTANTES TECLEADAS QUE EL FICHERO PUEDA DAR: la cabecera se localiza
buscando el segundo '---', las palabras se cuentan del fichero y la cita de cada
fila se imprime de la linea (D.35: la cita se pega, no se promete). Lo unico que
pongo yo son los TRAMOS, que son mi lectura, y el rotulo de cada uno.
"""
import io
import sys
import unicodedata

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")


def llana(texto):
    texto = texto.replace(chr(0x2014), "-").replace(chr(0x2013), "-")
    texto = texto.replace(u"‘", "'").replace(u"’", "'")
    texto = texto.replace(u"“", '"').replace(u"”", '"').replace(u"…", "...")
    return "".join(c for c in unicodedata.normalize("NFD", texto)
                   if unicodedata.category(c) != "Mn")


# MI LECTURA. La cuarta columna es cuantos nodos da el tramo.
TRAMOS = {
    "cap_01": [
        ("L9 a L11", 9, 11, 0, "P1  los rotulos: el titulo y la seccion I"),
        ("L13 a L17", 13, 17, 0, "P2  el libro de 1983 y los dos sucesos que obligan una introduccion nueva"),
        ("L19 a L25", 19, 25, 0, "P3  el ataque japones de las DRAM y la salida de Intel de ese negocio: CASO historico"),
        ("L27 a L35", 27, 35, 0, "P4  la globalizacion y su consecuencia sobre cada empleado: POSTURA"),
        ("L37 a L49", 37, 49, 0, "P5  el correo electronico y el fin de los escondites: POSTURA con su caso del correo postal"),
        ("L51 a L59", 51, 59, 0, "P6  a quien va dirigido el libro: el mando intermedio y el gestor de conocimiento, DEFINICION"),
        ("L61 a L67", 61, 67, 0, "P7  las reglas del entorno nuevo, la tolerancia al desorden y el micro CEO: POSTURA, y el lema es lema"),
        ("L69 a L75", 69, 75, 0, "P8  las tres ideas del libro: MAPA del propio libro, cada una desarrollada en su capitulo"),
        ("L77 a L79", 77, 79, 0, "P9  planear como planea un cuerpo de bomberos y menos niveles de mando: POSTURA"),
        ("L81 a L85", 81, 85, 0, "P10 el 1:1 con mas reportados, menos veces y mas corto: su procedimiento vive en su capitulo, extraerlo aqui fabrica el gemelo de su donante"),
        ("L87 a L99", 87, 99, 0, "P11 gestionar tu carrera: eres un negocio de un solo empleado, POSTURA"),
        ("L101 a L107", 101, 107, 1, "P12 LAS TRES PREGUNTAS PARA EXAMINARTE: el libro pone su propio inventario y lo nombra uno a uno"),
        ("L109 a L115", 109, 115, 0, "P13 el cierre y el paso al capitulo 1"),
        ("L117 a L119", 117, 119, 0, "P14 la firma y la fecha"),
    ],
    "cap_02": [
        ("L9 a L13", 9, 13, 0, "P1  rotulo, titulo y subtitulo"),
        ("L15 a L27", 15, 27, 1, "P2  el huevo de tres minutos: los requisitos, el PASO LIMITANTE y el escalonado"),
        ("L29 a L29", 29, 29, 0, "P3  pie de figura"),
        ("L31 a L35", 31, 35, 0, "P4  el reclutamiento universitario: CASO del mismo principio, manual 3.5"),
        ("L37 a L47", 37, 47, 1, "P5  proceso, montaje y prueba: los tres tipos nombrados uno a uno, con sus dos casos"),
        ("L49 a L55", 49, 55, 1, "P6  la cola del tostador: la capacidad limitada cambia cual es el paso limitante"),
        ("L57 a L61", 57, 61, 1, "P7  los intercambios entre equipo, personal e inventario contra el plazo"),
        ("L63 a L65", 63, 65, 0, "P8  la fabrica de desayunos continua: CASO mas un intercambio, y el paso que falta seria puente"),
        ("L67 a L67", 67, 67, 1, "P9  prueba funcional contra inspeccion en proceso"),
        ("L69 a L69", 69, 69, 1, "P10 inspeccion de recepcion, inventario de materia prima y oportunidad en riesgo"),
        ("L71 a L75", 71, 75, 1, "P11 el valor que se anade y arreglar en la etapa de menor valor"),
        ("L77 a L79", 77, 79, 0, "P12 la justicia penal como proceso de produccion: CASO, y sus cifras sin fecha de corte en el recorte"),
    ],
}

TOPE = 15    # el techo de EXTRACTOR.md 12.4, para contrastar, no para decidir

total_nodos = 0
for unidad in sorted(TRAMOS):
    ruta = "fuentes/grove_high_output/%s.md" % unidad
    lineas = io.open(ruta, encoding="utf-8").read().split("\n")
    # LA CABECERA NO SE TECLEA: es hasta el SEGUNDO '---'
    cortes = [i for i, l in enumerate(lineas, 1) if l.strip() == "---"]
    fin_cabecera = cortes[1]
    cuerpo = len(" ".join(lineas[fin_cabecera:]).split())
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
    print("la cabecera acaba en la linea          : %d   (segundo '---', no tecleado)" % fin_cabecera)
    print("tramos de mi lectura                   : %d" % len(filas))
    print("lineas con contenido tras la cabecera  : %d" % len(con_contenido))
    print("lineas NO cubiertas                    : %d  %s" % (len(sin_cubrir), sin_cubrir))
    print("SOLAPES                                : %d  %s" % (len(solapes), solapes))
    print("suma de las filas                      : %d palabras" % suma)
    print("cuerpo medido aparte                   : %d palabras" % cuerpo)
    print("fichero entero, para cruzar con wc -w  : %d palabras" % fichero)
    print("IGUALES                                : %s" % (suma == cuerpo))
    print("NODOS QUE MI FRONTERA DA EN ESTA UNIDAD: %d" % nodos)
    if suma != cuerpo or sin_cubrir or solapes:
        print("\nLA CUENTA DE NODOS NO SE PUBLICA. Diferencia: %d palabras." % (suma - cuerpo))
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
print("NODOS QUE MI FRONTERA DA EN LAS DOS UNIDADES : %d" % total_nodos)
print("TECHO DE CANDIDATOS POR VUELTA (EXTRACTOR.md 12.4): entre 5 y %d" % TOPE)
print("DENTRO DEL TECHO                             : %s"
      % ("SI" if 5 <= total_nodos <= TOPE else "NO"))
