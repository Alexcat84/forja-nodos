# -*- coding: utf-8 -*-
"""MI LECTURA DE LA FRONTERA DE cap_03, PUBLICADA ANTES DE CORTAR (EXTRACTOR.md 10).

CERO CONSTANTES TECLEADAS QUE EL FICHERO PUEDA DAR: la cabecera se localiza
buscando el segundo guion triple, las palabras se cuentan del fichero y la cita de
cada fila se imprime de la linea (D.35: la cita se pega, no se promete). Lo unico
que pongo yo son los TRAMOS, que son mi lectura, y el rotulo de cada uno.

Y EL REMEDIO BLOQUEANTE HEREDADO: la cuenta de nodos se publica rotulada con la
poblacion que se conto, que aqui es UNA unidad, cap_03, y no el libro.
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
    "cap_03": [
        ("L9 a L13", 9, 13, 0,
         "P1  rotulos: el numero, el titulo y el subtitulo Indicators as a Key Tool"),
        ("L15 a L29", 15, 29, 1,
         "P2  LOS CINCO INDICADORES DIARIOS: el libro los nombra uno a uno y anade el repaso de primera hora"),
        ("L31 a L33", 31, 33, 1,
         "P3  el indicador dirige la atencion, y el par de efecto y contraefecto, con su caso del compilador"),
        ("L35 a L37", 35, 37, 1,
         "P4  las dos varas del indicador administrativo: salida y no actividad, y cosa fisica y contable"),
        ("L39 a L67", 39, 67, 0,
         "P5  la TABLA de seis funciones administrativas con su indicador, y su pie: material del nodo de P4"),
        ("L69 a L69", 69, 69, 0,
         "P6  para que sirven esos indicadores: objetivos, objetividad y comparacion entre grupos, POSTURA"),
        ("L71 a L79", 71, 79, 1,
         "P7  LA CAJA NEGRA: entrada, salida y trabajo, y las ventanas que se abren para ver dentro"),
        ("L81 a L81", 81, 81, 0,
         "P8  los indicadores adelantados han de ser CREIBLES: adjetivo de adecuacion en el sitio del criterio, 9.1 restriccion 2"),
        ("L83 a L87", 83, 87, 1,
         "P9  EL INDICADOR DE LINEALIDAD: la recta ideal contra lo real, con sus dos casos"),
        ("L89 a L89", 89, 89, 1,
         "P10 el indicador de tendencia: la salida contra el tiempo y contra un patron"),
        ("L91 a L97", 91, 97, 1,
         "P11 EL GRAFICO ESCALONADO: el pronostico rehecho cada mes sobre los anteriores"),
        ("L99 a L99", 99, 99, 1,
         "P12 el archivo de indicadores para resolver averias"),
        ("L101 a L109", 101, 109, 1,
         "P13 fabricar contra pedido o contra pronostico: las dos vias nombradas, con su riesgo de inventario"),
        ("L111 a L121", 111, 121, 1,
         "P14 casar el flujo de fabricacion con el de ventas: dos pronosticos, holgura en inventario y escalonados"),
        ("L123 a L125", 123, 125, 1,
         "P15 dimensionar la plantilla administrativa con el pronostico y los patrones de hecho"),
        ("L127 a L133", 127, 133, 0,
         "P16 rechazar al menor valor y los NOMBRES de los tres puntos de inspeccion: DEFINICION, y el fondo ya vive en cap_02"),
        ("L135 a L137", 135, 137, 1,
         "P17 aceptar o rechazar el material defectuoso, con su grupo equilibrado y su excepcion de fiabilidad"),
        ("L139 a L141", 139, 141, 1,
         "P18 barrera contra monitorizacion: las dos mecanicas enteras y su regla de pulgar"),
        ("L143 a L145", 143, 145, 1,
         "P19 la inspeccion variable: la frecuencia sigue al nivel de calidad"),
        ("L147 a L153", 147, 153, 0,
         "P20 la embajada de Londres y sus visados: CASO de P19, manual 3.5, entra nombrado dentro de su nodo"),
        ("L155 a L155", 155, 155, 0,
         "P21 la inspeccion variable aplicada al mando: su procedimiento vive en otro capitulo, extraerlo aqui fabrica el gemelo de su donante"),
        ("L157 a L167", 157, 167, 0,
         "P22 productividad como salida partida por trabajo, y la palanca: DEFINICION y concepto"),
        ("L169 a L173", 169, 173, 1,
         "P23 LA SIMPLIFICACION DEL TRABAJO: diagrama, cuenta, meta de reduccion y la pregunta a cada paso"),
        ("L175 a L179", 175, 179, 0,
         "P24 el rotulo de la parte II del libro, que ya no es de esta unidad"),
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
    print("NODOS QUE MI FRONTERA DA EN ESTA UNIDAD, cap_03 Y SOLO cap_03: %d" % nodos)
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
print("NODOS QUE MI FRONTERA DA EN LA UNIDAD DE ESTA VUELTA (cap_03): %d" % total_nodos)
print("TECHO DE CANDIDATOS POR VUELTA (EXTRACTOR.md 12.4): entre 5 y %d" % TOPE)
print("DENTRO DEL TECHO                                             : %s"
      % ("SI" if 5 <= total_nodos <= TOPE else "NO"))
print("LA VUELTA CIERRA EN cap_03 (12.4, precedencia): las otras 17 unidades del")
print("libro pasan a la vuelta siguiente, y eso se declara en el reporte.")
