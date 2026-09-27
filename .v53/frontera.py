# -*- coding: utf-8 -*-
"""MI LECTURA DE LA FRONTERA DE cap_06, cap_07 Y cap_08, PUBLICADA ANTES DE MINAR NADA.

Mismo instrumento que la vuelta 50 corrio sobre cap_05 (.v50/frontera.py), con MI lectura de
los tres capitulos de hoy dentro. CERO CONSTANTES TECLEADAS QUE EL FICHERO PUEDA DAR: la
cabecera se localiza buscando el segundo guion triple, las palabras y los caracteres se cuentan
del fichero, y la cita de cada fila la imprime el instrumento de la linea (D.35: la cita se
pega, no se promete). Lo unico que pongo yo son los TRAMOS, el rotulo de cada uno y los NODOS
QUE PREVE, que son mi lectura y lo que el auditor siguiente recomputa.

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
    "cap_06": [
        ("L9 a L11", 9, 11, 0,
         "P1  rotulos: el numero 5 y el titulo textual Decisions, Decisions"),
        ("L13 a L13", 13, 13, 0,
         "P2  el abanico de decisiones, del edificio a las bebidas de la fiesta: DEFINICION con ejemplos"),
        ("L15 a L15", 15, 15, 0,
         "P3  poder de posicion contra poder de conocimiento: DEFINICION, nombra el fenomeno y no pone medios"),
        ("L17 a L17", 17, 17, 0,
         "P4  el titulado que se vuelve obsoleto con los anios: CASO del autor sobre si mismo, manual 3.5"),
        ("L19 a L19", 19, 19, 0,
         "P5  el mando intermedio como llave del engranaje: POSTURA, su criterio es la clave del exito"),
        ("L21 a L21", 21, 21, 0,
         "P6  rotulo Ideal Model, sin cuerpo que extraer"),
        ("L23 a L29", 23, 29, 1,
         "P7  EL MODELO IDEAL CON SUS TRES ETAPAS nombradas una a una: discusion libre, decision clara y apoyo pleno"),
        ("L31 a L31", 31, 31, 0,
         "P8  a quien le sale facil el modelo y a quien no: POSTURA sobre dos clases de empleado"),
        ("L33 a L33", 33, 33, 1,
         "P9  DECIDIR EN EL NIVEL COMPETENTE MAS BAJO: la mezcla de conocimiento y juicio, con sus medios nombrados"),
        ("L35 a L35", 35, 35, 0,
         "P10 los simbolos de estatus y el igualitarismo: POSTURA, respuesta del autor a un periodista"),
        ("L37 a L37", 37, 37, 0,
         "P11 rotulo The Peer-Group Syndrome, sin cuerpo que extraer"),
        ("L39 a L39", 39, 39, 0,
         "P12 las emociones que estorban al modelo, orgullo, ambicion, miedo e inseguridad: POSTURA"),
        ("L41 a L41", 41, 41, 0,
         "P13 el juego de papeles que dio nombre al par mas uno: CASO del autor, manual 3.5, su doctrina vive en P18"),
        ("L43 a L43", 43, 43, 0,
         "P14 la linea que presenta la cita del ingeniero John: enlace, sin cuerpo que extraer"),
        ("L45 a L45", 45, 45, 0,
         "P15 la cita de John sobre por que nadie se moja: TESTIMONIO citado, POSTURA"),
        ("L47 a L47", 47, 47, 0,
         "P16 la diferencia entre los dos silencios, el del jefe y el del consenso: POSTURA"),
        ("L49 a L49", 49, 49, 1,
         "P17 INFUNDIR LA AUTOCONFIANZA que vence al sindrome, con sus tres fuentes nombradas una a una"),
        ("L51 a L51", 51, 51, 1,
         "P18 QUIEN TOMA EL MANDO cuando no hay presidente: el que mas se juega, y si no, el mas senior presente"),
        ("L53 a L53", 53, 53, 0,
         "P19 el miedo a parecer tonto: DIAGNOSTICO con un recordatorio, sin inventario de medios, 9.1"),
        ("L55 a L55", 55, 55, 0,
         "P20 el miedo del subalterno a ser desautorizado: DIAGNOSTICO, ningun medio nombrado"),
        ("L57 a L57", 57, 57, 0,
         "P21 la inteligencia y la voluntad contra los dos miedos: POSTURA, 9.1 restriccion 2"),
        ("L59 a L59", 59, 59, 0,
         "P22 rotulo Striving for the Output, sin cuerpo que extraer"),
        ("L61 a L61", 61, 61, 1,
         "P23 CUANDO ES LEGITIMO QUE EL SENIOR DECIDA SOLO: la condicion y su prohibicion, las dos escritas"),
        ("L63 a L63", 63, 63, 1,
         "P24 EL CRITERIO DEL MOMENTO: ni antes de oir lo de fondo, ni despues de haberlo oido todo"),
        ("L65 a L65", 65, 65, 1,
         "P25 CABEZA DE SERIE: las SEIS preguntas que el mando zanja por adelantado, contadas por el libro"),
        ("L67 a L77", 67, 77, 0,
         "P26 las seis preguntas, una por linea: partes de la cabeza P25 y sin procedimiento propio ninguna"),
        ("L79 a L79", 79, 79, 0,
         "P27 la planta de Filipinas, el planteamiento: CASO del autor, manual 3.5"),
        ("L81 a L87", 81, 87, 0,
         "P28 las seis preguntas aplicadas a Filipinas una a una: CASO del autor, manual 3.5"),
        ("L89 a L89", 89, 89, 0,
         "P29 como se tomo y se ratifico aquella decision: CASO del autor, manual 3.5"),
        ("L91 a L91", 91, 91, 0,
         "P30 el valor de decidir siempre igual y el veto que llega tarde: POSTURA que justifica P25"),
        ("L93 a L93", 93, 93, 1,
         "P31 ANUNCIAR UNA DECISION QUE DEFRAUDA: no te vayas, levanta la sesion, reconvoca y pide sus opiniones"),
        ("L95 a L95", 95, 95, 0,
         "P32 Sloan y el mando de mentalidad John Wayne que volvio: CASO y POSTURA de cierre"),
    ],
    "cap_07": [
        ("L9 a L11", 9, 11, 0,
         "P1  rotulos: el numero 6 y el titulo textual de la planificacion como accion de hoy"),
        ("L13 a L13", 13, 13, 0,
         "P2  rotulo The Planning Process, sin cuerpo que extraer"),
        ("L15 a L15", 15, 15, 0,
         "P3  planificar es cotidiano, con el ejemplo del deposito de gasolina: DEFINICION con ilustracion"),
        ("L17 a L17", 17, 17, 0,
         "P4  los tres pasos en la fabrica: RECAPITULACION declarada del Cap. 2 y molde de P5, no nodo propio"),
        ("L19 a L19", 19, 19, 1,
         "P5  CABEZA DE SERIE: los TRES pasos del proceso general de planificacion, contados y nombrados"),
        ("L21 a L21", 21, 21, 0,
         "P6  la linea que anuncia el detalle de cada paso: enlace, sin cuerpo que extraer"),
        ("L23 a L23", 23, 23, 0,
         "P7  rotulo STEP 1, ENVIRONMENTAL DEMAND, sin cuerpo que extraer"),
        ("L25 a L25", 25, 25, 1,
         "P8  DEFINIR TU ENTORNO como si tu grupo fuera empresa: clientes, proveedores y competencia, nombrados"),
        ("L27 a L27", 27, 27, 1,
         "P9  QUE MIRAR AL EXAMINAR EL ENTORNO: los cuatro objetos de revision, nombrados uno a uno"),
        ("L29 a L31", 29, 31, 1,
         "P10 LOS DOS MARCOS TEMPORALES y el analisis de la diferencia, con la prohibicion de rebajar la demanda"),
        ("L33 a L33", 33, 33, 0,
         "P11 rotulo STEP 2, PRESENT STATUS, sin cuerpo que extraer"),
        ("L35 a L35", 35, 35, 1,
         "P12 DETERMINAR EL ESTADO PRESENTE: capacidades, proyectos en curso, la misma moneda, el plazo y la merma"),
        ("L37 a L37", 37, 37, 0,
         "P13 rotulo STEP 3, WHAT TO DO TO CLOSE THE GAP, sin cuerpo que extraer"),
        ("L39 a L39", 39, 39, 1,
         "P14 CERRAR LA BRECHA con sus dos preguntas separadas, y el conjunto de acciones que sale es la estrategia"),
        ("L41 a L41", 41, 41, 0,
         "P15 estrategia contra tactica, con el correo electronico del jefe de comunicacion: DEFINICION con CASO"),
        ("L43 a L43", 43, 43, 0,
         "P16 rotulo SOME EXAMPLES, sin cuerpo que extraer"),
        ("L45 a L47", 45, 47, 0,
         "P17 el caso de Bruce y su inventario de proyectos: CASO del autor, manual 3.5"),
        ("L49 a L53", 49, 53, 0,
         "P18 el caso de Cindy y su plan con los ingenieros de desarrollo: CASO del autor, manual 3.5"),
        ("L55 a L55", 55, 55, 0,
         "P19 rotulo The Output of the Planning Process, sin cuerpo que extraer"),
        ("L57 a L57", 57, 57, 0,
         "P20 la brecha de hoy es un fallo de planificacion de ayer: POSTURA con la analogia de la gasolina"),
        ("L59 a L59", 59, 59, 0,
         "P21 la verdadera salida del proceso son las tareas que provoca: DEFINICION"),
        ("L61 a L61", 61, 61, 1,
         "P22 EL HORIZONTE Y LA VENTANA: cinco anios de vista, solo el proximo se implementa, y no replanificar tanto"),
        ("L63 a L63", 63, 63, 0,
         "P23 quien participa, la direccion operativa: POSTURA, una respuesta sin inventario de medios"),
        ("L65 a L65", 65, 65, 0,
         "P24 decir que si es decir que no a otra cosa: POSTURA, su criterio son agallas, honradez y disciplina"),
        ("L67 a L67", 67, 67, 0,
         "P25 rotulo Management by Objectives, sin cuerpo que extraer"),
        ("L69 a L69", 69, 69, 0,
         "P26 que supone el sistema de direccion por objetivos y en que dos pasos se concentra: DEFINICION"),
        ("L71 a L75", 71, 75, 1,
         "P27 CABEZA DE SERIE: las DOS preguntas que el sistema tiene que contestar, contadas y nombradas"),
        ("L77 a L77", 77, 77, 0,
         "P28 el aeropuerto y los pueblos A, B y C: ILUSTRACION del autor de un objetivo y sus resultados clave"),
        ("L79 a L79", 79, 79, 1,
         "P29 FIJAR EL PERIODO del sistema por el plazo de la retroalimentacion, con su cadencia contra el plan anual"),
        ("L81 a L81", 81, 81, 0,
         "P30 mantener pocos objetivos: 9.1 restriccion 2, el criterio es small y a few well-chosen"),
        ("L83 a L83", 83, 83, 0,
         "P31 rotulo TWO CASE HISTORIES, sin cuerpo que extraer"),
        ("L85 a L89", 85, 89, 0,
         "P32 Isabel y Colon, el objetivo anidado: CASO historico contado por el autor, manual 3.5"),
        ("L91 a L93", 91, 93, 0,
         "P33 los resultados clave se cumplen y el objetivo se falla; el sistema no es documento legal: POSTURA"),
        ("L95 a L95", 95, 95, 0,
         "P34 Filipinas en terminos de objetivo y resultados clave: CASO del autor, manual 3.5"),
        ("L97 a L97", 97, 97, 0,
         "P35 el resultado clave con redaccion muy especifica y fechas: 9.1 restriccion 2, very specific"),
        ("L99 a L99", 99, 99, 0,
         "P36 el objetivo del supervisor del jefe de obra: CASO del autor, manual 3.5"),
        ("L101 a L101", 101, 101, 0,
         "P37 el paralelismo entre Isabel e Intel, y que el sistema pide juicio y sentido comun: POSTURA"),
        ("L103 a L105", 103, 105, 0,
         "P38 rotulos de la parte III, Team of Teams: material de division del libro, sin cuerpo que extraer"),
    ],
    "cap_08": [
        ("L9 a L11", 9, 11, 0,
         "P1  rotulos: el numero 7 y el titulo textual The Breakfast Factory Goes National"),
        ("L13 a L13", 13, 13, 0,
         "P2  donde quedo la fabrica de desayunos y su hervidor continuo: CASO del autor, manual 3.5"),
        ("L15 a L15", 15, 15, 0,
         "P3  la segunda sucursal, la revista y la franquicia nacional: CASO del autor, manual 3.5"),
        ("L17 a L17", 17, 17, 0,
         "P4  la tension entre el empresario local y la economia de escala: DEFINICION del dilema, sin medios"),
        ("L19 a L19", 19, 19, 0,
         "P5  publicidad, contratacion, salarios y maquinaria: PREGUNTAS retoricas sin inventario de medios"),
        ("L21 a L21", 21, 21, 0,
         "P6  los huevos y los centros regionales de compra: CASO con su criterio en some kind of compromise"),
        ("L23 a L23", 23, 23, 0,
         "P7  el menu comun y la diferencia regional de gusto: CASO con discrecion sin medida"),
        ("L25 a L25", 25, 25, 0,
         "P8  el inmueble y los estandares que se fijan en Chicago: PREGUNTAS con some standards, adjetivo"),
        ("L27 a L27", 27, 27, 0,
         "P9  el mobiliario, la vajilla y los almacenes regionales: CASO con probably en el sitio del criterio"),
        ("L29 a L29", 29, 29, 0,
         "P10 donde se decide la ubicacion de una franquicia nueva: PREGUNTAS retoricas, ninguna zanjada"),
        ("L31 a L31", 31, 31, 0,
         "P11 la nostalgia del dueno y la plantilla corporativa que crece: POSTURA del autor"),
        ("L33 a L33", 33, 33, 0,
         "P12 el equipo de equipos: DEFINICION de cierre que abre la parte III, material de cierre"),
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
print("NODOS QUE MI FRONTERA DA EN LAS TRES UNIDADES DE HOY: %d" % total_nodos)
print("TECHO DE CANDIDATOS DE D.58 EN REGIMEN LIGERO       : %d" % TOPE)
print("DENTRO DEL TECHO DE CANDIDATOS                      : %s"
      % ("SI" if total_nodos <= TOPE else "NO"))
print("LA OTRA MITAD DEL TECHO, QUE ES LA QUE MUERDE: 90 min de reloj de aduana,")
print("que a 731,2 s por pasada (medida de la vuelta 52) dan 7,4 candidatos.")
