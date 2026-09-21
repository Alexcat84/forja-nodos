# -*- coding: utf-8 -*-
"""MI LECTURA DE LA FRONTERA DE cap_04, PUBLICADA ANTES DE CORTAR (EXTRACTOR.md 10).

Es el mismo instrumento que la vuelta 2 del frente corrio sobre cap_03 (.v2g/frontera.py),
con MI lectura de cap_04 dentro. CERO CONSTANTES TECLEADAS QUE EL FICHERO PUEDA DAR: la
cabecera se localiza buscando el segundo guion triple, las palabras se cuentan del fichero
y la cita de cada fila se imprime de la linea (D.35: la cita se pega, no se promete). Lo
unico que pongo yo son los TRAMOS y el rotulo de cada uno, que son mi lectura.

Y EL REMEDIO BLOQUEANTE HEREDADO: la cuenta de nodos se publica rotulada con la poblacion
que se conto, que aqui es UNA unidad, cap_04, y no el libro.
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
    "cap_04": [
        ("L9 a L13", 9, 13, 0,
         "P1  rotulos: el numero, el titulo Managerial Leverage y el subtitulo de la salida del mando"),
        ("L15 a L47", 15, 47, 0,
         "P2  la salida del mando es la de su organizacion mas la de las vecinas: DEFINICION con su ecuacion"),
        ("L49 a L55", 49, 55, 0,
         "P3  actividad no es salida, y la caja de engranajes: POSTURA"),
        ("L57 a L61", 57, 61, 0,
         "P4  Daddy, What Do You Really Do, y el anuncio de la tabla del dia"),
        ("L63 a L139", 63, 139, 0,
         "P5  LA TABLA A Day from My Life: CASO del autor, manual 3.5, entra nombrado dentro de sus nodos"),
        ("L141 a L143", 141, 143, 0,
         "P6  el dia sin patron y mover la energia adonde la palanca sea mayor: POSTURA"),
        ("L145 a L147", 145, 147, 1,
         "P7  LAS VIAS POR LAS QUE LLEGA LA INFORMACION, nombradas una a una, y la verbal por delante"),
        ("L149 a L151", 149, 151, 0,
         "P8  para que sirve el informe escrito: son sus FINES, y 9.1 restriccion 1 los deja fuera"),
        ("L153 a L153", 153, 153, 1,
         "P9  LA JERARQUIA DE LA INFORMACION: los escalones nombrados uno a uno y su redundancia"),
        ("L155 a L157", 155, 157, 1,
         "P10 LA VISITA AL SITIO, y la visita programada con su propio inventario de lo que se mira"),
        ("L159 a L159", 159, 159, 1,
         "P11 transmitir objetivos, prioridades y preferencias, que el libro llama la llave de la delegacion"),
        ("L161 a L165", 161, 165, 0,
         "P12 las formas de participar en una decision y las dos clases de decision: DEFINICION"),
        ("L167 a L167", 167, 167, 1,
         "P13 EL EMPUJON: sus medios nombrados y su frontera con la orden"),
        ("L169 a L173", 169, 173, 0,
         "P14 el modelo de conducta y el ejemplo: POSTURA con sus tres casos"),
        ("L175 a L175", 175, 175, 0,
         "P15 el tiempo propio como unico recurso finito: POSTURA, y su procedimiento vive en P32 y siguientes"),
        ("L177 a L177", 177, 177, 0,
         "P16 la reunion es un medio y no una actividad: POSTURA, y el capitulo de reuniones es otro"),
        ("L179 a L193", 179, 193, 0,
         "P17 la ecuacion de la palanca, L1 por A1 mas L2 por A2: DEFINICION"),
        ("L195 a L201", 195, 201, 1,
         "P18 CABEZA DE SERIE: las TRES vias de subir la productividad gerencial, numeradas y nombradas"),
        ("L203 a L213", 203, 213, 1,
         "P19 CABEZA DE SERIE: las TRES vias basicas de la actividad de alta palanca, contadas y nombradas"),
        ("L215 a L217", 215, 217, 1,
         "P20 la palanca depende de CUANDO: el trabajo por delante del acontecimiento y la accion inmediata"),
        ("L219 a L219", 219, 219, 0,
         "P21 la palanca negativa de la reunion a la que llegas sin preparar: material del nodo de P24"),
        ("L221 a L225", 221, 225, 0,
         "P22 impartir conocimiento a un grupo: son los CASOS de la primera via, cuyo nodo es P19"),
        ("L227 a L229", 227, 229, 0,
         "P23 la evaluacion de desempeno y el fichero recordatorio: NOMBRADOS y no procedimentados aqui"),
        ("L231 a L235", 231, 235, 1,
         "P24 LA PALANCA NEGATIVA: desanimo, indecision e intromision, con la prueba que la separa del seguimiento"),
        ("L237 a L239", 237, 239, 0,
         "P25 el especialista de conocimiento: son los CASOS de la tercera via, cuyo nodo es P19"),
        ("L241 a L241", 241, 241, 0,
         "P26 el arte de elegir una o dos actividades: una intuicion en el sitio del criterio, 9.1 restriccion 2"),
        ("L243 a L249", 243, 249, 1,
         "P27 QUE SE DELEGA: la base comun de informacion, el lapiz, y delegar sin seguimiento es abdicar"),
        ("L251 a L251", 251, 251, 0,
         "P28 las dos presentaciones de seguimiento de la reunion del dia: CASO del autor"),
        ("L253 a L255", 253, 255, 1,
         "P29 SUPERVISAR LO DELEGADO: etapa de menor valor anadido, frecuencia variable y detalle al azar"),
        ("L257 a L257", 257, 257, 1,
         "P30 SUPERVISAR LA DECISION DELEGADA: las preguntas concretas en la reunion de revision"),
        ("L259 a L265", 259, 265, 0,
         "P31 subir el ritmo, y la critica a las tecnicas de gestion del tiempo: POSTURA"),
        ("L267 a L267", 267, 267, 1,
         "P32 EL PASO LIMITANTE DE LA JORNADA y los desfases que se crean alrededor"),
        ("L269 a L271", 269, 271, 1,
         "P33 AGRUPAR TAREAS SEMEJANTES para aprovechar una sola preparacion"),
        ("L273 a L285", 273, 285, 2,
         "P34 EL CALENDARIO como herramienta de planificacion, y su segunda responsabilidad: decir que no"),
        ("L287 a L287", 287, 287, 0,
         "P35 la holgura: el grado OPTIMO de carga es adjetivo de adecuacion en el sitio del criterio, 9.1 restriccion 2"),
        ("L289 a L289", 289, 289, 1,
         "P36 EL INVENTARIO DE PROYECTOS DISCRECIONALES, con su criterio propio y su contraste"),
        ("L291 a L291", 291, 291, 0,
         "P37 el metodo establecido y el pensamiento que lo sostiene: POSTURA, sin inventario propio"),
        ("L293 a L301", 293, 301, 1,
         "P38 SEIS A OCHO SUBORDINADOS: la cifra, su guia de medio dia por semana y el caso del reparto estrecho"),
        ("L303 a L307", 303, 307, 1,
         "P39 LA REGULARIDAD: los mismos bloques de tiempo para actividades iguales, coordinados con los demas"),
        ("L309 a L313", 309, 313, 0,
         "P40 el experimento de los veinte mandos y las soluciones que no sirven: CASO"),
        ("L315 a L315", 315, 315, 1,
         "P41 RESPUESTAS ESTANDAR a las interrupciones que se repiten, y su delegacion"),
        ("L317 a L317", 317, 317, 1,
         "P42 AGRUPAR LAS INTERRUPCIONES en las reuniones regulares en vez de atenderlas al azar"),
        ("L319 a L319", 319, 319, 0,
         "P43 el banco de indicadores para responder rapido: ese objeto ya vive entero en cap_03, P.19"),
        ("L321 a L323", 321, 323, 1,
         "P44 EL CARTEL EN LA PUERTA Y LA HORA DE OFICINA ABIERTA, con el texto del cartel dado por el libro"),
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
    print("fichero entero, para cruzar con wc -w  : %d palabras" % fichero)
    print("IGUALES                                : %s" % (suma == cuerpo))
    print("NODOS QUE MI FRONTERA DA EN ESTA UNIDAD, cap_04 Y SOLO cap_04: %d" % nodos)
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
print("NODOS QUE MI FRONTERA DA EN LA UNIDAD DE ESTA VUELTA (cap_04): %d" % total_nodos)
print("TECHO DE CANDIDATOS POR VUELTA (EXTRACTOR.md 12.4): entre 5 y %d" % TOPE)
print("DENTRO DEL TECHO                                             : %s"
      % ("SI" if 5 <= total_nodos <= TOPE else "NO"))
print("SI DA NO, MANDA LA REGLA DE PRECEDENCIA DE 12.4: la vuelta cierra en esta unidad,")
print("se mina hasta el techo y la linea del tramo dice en que candidato corto.")
