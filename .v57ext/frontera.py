# -*- coding: utf-8 -*-
"""MI LECTURA DE LA FRONTERA DE cap_11, cap_12 Y cap_13, PUBLICADA ANTES DE MINAR NADA.

Mismo instrumento que la vuelta 56 corrio sobre cap_08, cap_09 y cap_10 (.v56ext/frontera.py),
que a su vez reusaba el de la vuelta 55 y el de la vuelta 53: NI UNA LINEA DE SU MAQUINARIA DE
MEDIR TOCADA (EXTRACTOR.md 13, la moratoria de maquinaria). Lo que cambia, y lo digo por su
nombre porque toco el bloque que imprime: LA TABLA DE TRAMOS es mi lectura de hoy sobre tres
capitulos nuevos, y en el bloque 3 (EL TECHO) retiro la linea "MAS LOS QUE YA ESPERAN EN
CUARENTENA DE cap_10", porque esa linea nombraba un candidato concreto que la vuelta 55 ya habia
escrito y que la 56 solo confirmaba; hoy no hay ningun candidato de cap_11, cap_12 o cap_13
escrito de antemano, asi que la linea no tiene a que candidato senalar y la dejo fuera en vez de
dejarla con un cero que nadie pidio. Es el unico cambio de las lineas que imprimen, y esta
declarado aqui para no repetir el aviso de ACTA 55 55.6.a (decir "ni una linea tocada" cuando si
se toco: aqui SI se toca, y esta es la razon).

LA PIEZA DE cap_13 SOBRE LA MADUREZ RELEVANTE PARA LA TAREA SE LEE EN CINCO TRAMOS NO
CONTIGUOS Y NO EN UNO SOLO: L19, L23, L25, L27 y L31 a L47 forman la misma pieza (la fila que
cierra la cuenta, en L31 a L47, es la que lleva el nodo), y L21 y L29, que caen en medio, quedan
FUERA de la pieza por ser CASO y analogia y no inventario propio; la razon de cada exclusion se
publica en la fila que la nombra, y la ficha del candidato repite la frontera dentro de si misma
como manda la seccion 10 de EXTRACTOR.md cuando un nodo se arma con tramos que no son un solo
bloque continuo de lineas.

CERO CONSTANTES TECLEADAS QUE EL FICHERO PUEDA DAR: la cabecera se localiza buscando el segundo
guion triple, las palabras y los caracteres se cuentan del fichero, y la cita de cada fila la
imprime el instrumento de la linea (D.35: la cita se pega, no se promete). Lo unico que pongo yo
son los TRAMOS, el rotulo de cada uno y los NODOS QUE PREVE, que son mi lectura y lo que el
auditor siguiente recomputa.
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
    texto = texto.replace(chr(0x2022), "*")
    texto = texto.replace(chr(0x2026), "...")
    return "".join(c for c in unicodedata.normalize("NFD", texto)
                   if unicodedata.category(c) != "Mn")


# MI LECTURA. La cuarta columna es cuantos nodos preve el tramo.
TRAMOS = {
    "cap_11": [
        ("L9 a L9", 9, 9, 0, "P1  rotulo: el numero 10, sin cuerpo que extraer"),
        ("L11 a L11", 11, 11, 0, "P2  titulo textual Modes of Control, sin cuerpo que extraer"),
        ("L13 a L13", 13, 13, 0, "P3  el ejemplo de comprar neumaticos por el mejor precio: CASO que abre el mercado libre, manual 3.5"),
        ("L15 a L15", 15, 15, 0, "P4  el ejemplo del semaforo en rojo: CASO que abre la obligacion contractual social, manual 3.5"),
        ("L17 a L17", 17, 17, 0, "P5  el ejemplo del accidente de trafico: CASO que abre los valores culturales, manual 3.5"),
        ("L19 a L19", 19, 19, 0, "P6  enunciado de los tres modos invisibles de control, con dos puntos que abre la lista de P7 a P9: DEFINICION, taxonomia sin pasos"),
        ("L21 a L21", 21, 21, 0, "P7  primer miembro de la lista: free-market forces, sin cuerpo propio"),
        ("L23 a L23", 23, 23, 0, "P8  segundo miembro de la lista: contractual obligations, sin cuerpo propio"),
        ("L25 a L25", 25, 25, 0, "P9  tercer miembro de la lista: cultural values, sin cuerpo propio"),
        ("L27 a L27", 27, 27, 0, "P10 rotulo Free-Market Forces, sin cuerpo que extraer"),
        ("L29 a L29", 29, 29, 0, "P11 definicion del modo de mercado libre y por que no necesita vigilancia: DEFINICION"),
        ("L31 a L31", 31, 31, 0, "P12 por que el mercado libre no sirve para todo: se necesita un precio claro: DEFINICION"),
        ("L33 a L33", 33, 33, 0, "P13 rotulo Contractual Obligations, sin cuerpo que extraer"),
        ("L35 a L35", 35, 35, 0, "P14 por que las transacciones entre empresas van por libre mercado y donde deja de servir: DEFINICION"),
        ("L37 a L37", 37, 37, 0, "P15 el dialogo con los ingenieros que funda el contrato: CASO, manual 3.5"),
        ("L39 a L39", 39, 39, 0, "P16 la naturaleza del control contractual y la autoridad generalizada que exige: DEFINICION"),
        ("L41 a L41", 41, 41, 0, "P17 el semaforo otra vez y el policia como sobrecoste del incumplimiento: DEFINICION con retorno al CASO de P4"),
        ("L43 a L43", 43, 43, 0, "P18 el sistema fiscal y la empresa electrica como ejemplos de obligacion contractual: CASO, manual 3.5, la resolucion es del relato y no un medio nombrado para transferir"),
        ("L45 a L45", 45, 45, 0, "P19 rotulo Cultural Values, sin cuerpo que extraer"),
        ("L47 a L47", 47, 47, 0, "P20 cuando el entorno cambia mas rapido de lo que las reglas pueden seguirle, y por que la confianza sustituye al contrato: DEFINICION"),
        ("L49 a L49", 49, 49, 0, "P21 rotulo The Role of Management, sin cuerpo que extraer"),
        ("L51 a L51", 51, 51, 0, "P22 el papel de la direccion en cada uno de los tres modos, contado en general y sin el criterio de activacion que P23 a P26 todavia no han dado: DEFINICION que ilustra la taxonomia de P6 a P9, no procedimiento propio todavia"),
        ("L53 a L53", 53, 53, 0, "P23 rotulo The Most Appropriate Mode of Control, sin cuerpo que extraer"),
        ("L55 a L55", 55, 55, 0, "P24 la tentacion de idealizar los valores culturales y por que no siempre son el modo mas eficiente: POSTURA"),
        ("L57 a L61", 57, 61, 1, "P25 EL FACTOR CUA (complejidad, incertidumbre y ambiguedad) Y EL CUADRO DE CUATRO CUADRANTES QUE CRUZA MOTIVACION CONTRA CUA PARA ELEGIR EL MODO: inventario propio del libro, manual 9.1, nodo propio"),
        ("L63 a L63", 63, 63, 1, "P26 aplicar el modelo a un empleado nuevo: puesto de bajo factor CUA que se complica a medida que gana experiencia compartida, con la promocion interna como razon: nodo propio, aplicacion generalizada y no un caso nombrado"),
        ("L65 a L65", 65, 65, 0, "P27 el caso del directivo senior contratado de fuera, con alta CUA y sin experiencia compartida: POSTURA sin procedimiento, el libro solo cruza los dedos"),
        ("L67 a L67", 67, 67, 0, "P28 rotulo Modes of Control at Work, sin cuerpo que extraer"),
        ("L69 a L69", 69, 69, 0, "P29 el dia de Bob visto por sus tres modos de control: CASO, manual 3.5"),
        ("L71 a L71", 71, 71, 0, "P30 el programa de formacion de Barbara y sus tres modos: CASO, manual 3.5"),
        ("L73 a L73", 73, 73, 0, "P31 el reparto de un mismo equipo de ventas entre varias divisiones: CASO, manual 3.5"),
        ("L75 a L75", 75, 75, 0, "P32 la queja de los gerentes de marketing de fabrica: CASO, manual 3.5"),
        ("L77 a L77", 77, 77, 0, "P33 como los propios departamentos de marketing fabricaron el problema con sus concursos: CASO, manual 3.5"),
        ("L79 a L79", 79, 79, 0, "P34 los vendedores que se quedaron sin producto que vender y no se fueron: CASO, manual 3.5"),
        ("L81 a L81", 81, 81, 0, "P35 rotulo de la parte IV, sin cuerpo que extraer"),
        ("L83 a L83", 83, 83, 0, "P36 titulo textual The Players del capitulo siguiente, arrastrado dentro de este fichero, sin cuerpo que extraer"),
    ],
    "cap_12": [
        ("L9 a L9", 9, 9, 0, "P1  rotulo: el numero 11, sin cuerpo que extraer"),
        ("L11 a L11", 11, 11, 0, "P2  titulo textual The Sports Analogy, sin cuerpo que extraer"),
        ("L13 a L13", 13, 13, 0, "P3  recordatorio de la frase clave del libro sobre el output del mando: POSTURA de enlace con capitulos previos"),
        ("L15 a L15", 15, 15, 0, "P4  la gestion como actividad de equipo limitada por sus miembros: POSTURA"),
        ("L17 a L17", 17, 17, 1, "P5  LA PRUEBA MENTAL PARA DISTINGUIR INCAPACIDAD DE DESMOTIVACION, SI LA VIDA DEPENDIERA DE HACER EL TRABAJO: inventario propio del libro de dos ramas, manual 9.1, nodo propio"),
        ("L19 a L19", 19, 19, 0, "P6  la tarea mas importante del mando y las dos vias, formacion y motivacion, con el foco del capitulo en la motivacion: DEFINICION"),
        ("L21 a L21", 21, 21, 0, "P7  pie de figura de las dos vias, formacion y motivacion, sin cuerpo que extraer"),
        ("L23 a L23", 23, 23, 0, "P8  la motivacion viene de dentro y el mando solo puede crear el entorno: POSTURA"),
        ("L25 a L25", 25, 25, 0, "P9  mejor motivacion es mejor desempeno y no un cambio de actitud sentido: DEFINICION"),
        ("L27 a L27", 27, 27, 0, "P10 la motivacion por miedo en la revolucion industrial: CASO historico, manual 3.5"),
        ("L29 a L29", 29, 29, 0, "P11 el auge del trabajador del conocimiento y por que el miedo deja de bastar: POSTURA historica"),
        ("L31 a L31", 31, 31, 0, "P12 la dependencia de la teoria de Maslow: POSTURA"),
        ("L33 a L33", 33, 33, 0, "P13 necesidad, impulso y motivacion, y que una necesidad satisfecha deja de motivar: DEFINICION"),
        ("L35 a L35", 35, 35, 0, "P14 pie de figura de la jerarquia de necesidades de Maslow, sin cuerpo que extraer"),
        ("L37 a L37", 37, 37, 0, "P15 rotulo Physiological Needs, sin cuerpo que extraer"),
        ("L39 a L39", 39, 39, 0, "P16 definicion de las necesidades fisiologicas y el miedo asociado: DEFINICION"),
        ("L41 a L41", 41, 41, 0, "P17 rotulo Security/Safety Needs, sin cuerpo que extraer"),
        ("L43 a L43", 43, 43, 0, "P18 definicion de las necesidades de seguridad con el ejemplo del seguro medico: DEFINICION con CASO, manual 3.5"),
        ("L45 a L45", 45, 45, 0, "P19 rotulo Social/Affiliation Needs, sin cuerpo que extraer"),
        ("L47 a L47", 47, 47, 0, "P20 definicion de las necesidades sociales, la compania de los semejantes: DEFINICION"),
        ("L49 a L49", 49, 49, 0, "P21 la amiga que vuelve a trabajar por la compania y no por el sueldo: CASO, manual 3.5"),
        ("L51 a L51", 51, 51, 0, "P22 el caso de Jim y sus companeros de piso de Intel: CASO, manual 3.5"),
        ("L53 a L53", 53, 53, 0, "P23 el caso de Chuck en Harvard Business School y el paso de la supervivencia a la afiliacion: CASO, manual 3.5"),
        ("L55 a L55", 55, 55, 0, "P24 el terremoto de la planta de California y la regresion a la necesidad fisiologica: CASO, manual 3.5"),
        ("L57 a L57", 57, 57, 0, "P25 las tres primeras necesidades traen al trabajo, la estima y la autorrealizacion hacen rendir: DEFINICION de enlace"),
        ("L59 a L59", 59, 59, 0, "P26 rotulo Esteem/Recognition Needs, sin cuerpo que extraer"),
        ("L61 a L61", 61, 61, 0, "P27 definicion de la necesidad de estima con la analogia de keeping up with the Joneses: DEFINICION con CASO, manual 3.5"),
        ("L63 a L63", 63, 63, 0, "P28 por que las fuentes anteriores se autolimitan, con el caso del nuevo vicepresidente: DEFINICION con CASO, manual 3.5"),
        ("L65 a L65", 65, 65, 0, "P29 rotulo Self-Actualization Needs, sin cuerpo que extraer"),
        ("L67 a L67", 67, 67, 0, "P30 definicion de la autorrealizacion segun Maslow con la referencia a Personal Best: DEFINICION"),
        ("L69 a L69", 69, 69, 0, "P31 competencia contra logro como las dos fuerzas internas, con el violinista y el monopatin: DEFINICION con CASO, manual 3.5"),
        ("L71 a L71", 71, 71, 0, "P32 el camino orientado al logro y el experimento de los aros: DEFINICION del experimento, sin inventario ejecutable"),
        ("L73 a L73", 73, 73, 0, "P33 los tres tipos que los investigadores clasificaron, apostadores, conservadores y triunfadores: inventario de TIPOS DE PERSONA, no de medios ni etapas, 9.1 restriccion 1 por analogia: es un inventario de como es la gente y no de que hacer"),
        ("L75 a L75", 75, 75, 1, "P34 FIJAR EL OBJETIVO DE UN SISTEMA DE DIRECCION POR OBJETIVOS EN EL PUNTO DE MITAD DE PROBABILIDAD DE EXITO CUANDO EL IMPULSO A ESTIRARSE NO ES ESPONTANEO: inventario propio del libro con su propia cifra, manual 9.1, nodo propio"),
        ("L77 a L77", 77, 77, 0, "P35 el entorno que valora el output contra el laboratorio centrado en el saber, con Intel como CASO nombrado: DEFINICION con CASO, manual 3.5"),
        ("L79 a L79", 79, 79, 0, "P36 rotulo Money and Task-Relevant Feedback, sin cuerpo que extraer"),
        ("L81 a L81", 81, 81, 0, "P37 el dinero en los niveles bajos de la jerarquia con el caso de la planta del Caribe: DEFINICION con CASO, manual 3.5"),
        ("L83 a L83", 83, 83, 0, "P38 el capitalista de riesgo que sigue trabajando tras el primer millon: CASO, manual 3.5"),
        ("L85 a L85", 85, 85, 1, "P39 LA PRUEBA SENCILLA PARA UBICAR A ALGUIEN EN LA JERARQUIA MOTIVACIONAL SEGUN COMO REACCIONA A UN AUMENTO DE SUELDO: inventario propio del libro de dos ramas, manual 9.1, nodo propio"),
        ("L87 a L87", 87, 87, 0, "P40 la necesidad de medidas de progreso una vez en autorrealizacion, con el violinista y el esgrimista hungaro: DEFINICION con CASO, manual 3.5"),
        ("L89 a L89", 89, 89, 0, "P41 los mecanismos de retroalimentacion en el trabajo, con la revision de desempeno nombrada y aplazada: POSTURA, su criterio es most appropriate measures, 9.1 restriccion 2, y el propio texto la remite a mas adelante"),
        ("L91 a L91", 91, 91, 0, "P42 rotulo Fear, sin cuerpo que extraer"),
        ("L93 a L93", 93, 93, 0, "P43 el miedo al fracaso en los niveles altos con el experimento del calambre en los aros: DEFINICION con CASO, manual 3.5"),
        ("L95 a L95", 95, 95, 0, "P44 el miedo en los niveles superiores viene de dentro y no de fuera: POSTURA"),
        ("L97 a L97", 97, 97, 0, "P45 rotulo interno The Sports Analogy que repite el titulo del capitulo, sin cuerpo que extraer"),
        ("L99 a L99", 99, 99, 0, "P46 recapitulacion del proposito del capitulo y el doble papel del mando, formar y llevar a la autorrealizacion: POSTURA de recapitulacion, sin inventario nuevo"),
        ("L101 a L101", 101, 101, 0, "P47 la pregunta retorica de por que alguien corre un maraton sin interes en su oficina: POSTURA"),
        ("L103 a L103", 103, 103, 0, "P48 la cita de Joe Frazier sobre por que boxea: CASO citado, manual 3.5"),
        ("L105 a L105", 105, 105, 0, "P49 imaginar la productividad si el trabajo tuviera las caracteristicas del deporte: POSTURA aspiracional"),
        ("L107 a L107", 107, 107, 0, "P50 el prejuicio cultural que admira el deporte y desprecia al workaholic: POSTURA"),
        ("L109 a L109", 109, 109, 0, "P51 el consejo de poner reglas del juego y maneras de medirse, resuelto en el caso del building czar de mantenimiento de Intel: CASO, manual 3.5, la solucion (marcador periodico de un gerente y comparacion entre edificios) es del relato y no un medio nombrado para transferir, igual que P18 de cap_11"),
        ("L111 a L111", 111, 111, 0, "P52 el columnista de periodico que pierde el gusto por el trabajo cuando fusionan los diarios: CASO, manual 3.5"),
        ("L113 a L113", 113, 113, 0, "P53 el deporte como leccion para tolerar el fracaso, con el 50 por ciento de partidos perdidos: POSTURA, cifra generica del deporte y no medicion propia del autor"),
        ("L115 a L115", 115, 115, 0, "P54 las tres caracteristicas del entrenador ideal, no toma credito, es duro, fue buen jugador: DEFINICION de un arquetipo, no inventario de medios porque la tercera caracteristica no es una accion que se pueda ejecutar hoy, 9.1 restriccion 1 por analogia"),
        ("L117 a L117", 117, 117, 0, "P55 el cierre: convertir el lugar de trabajo en un campo de juego hace ganadores consistentes: POSTURA de cierre"),
    ],
    "cap_13": [
        ("L9 a L9", 9, 9, 0, "P1  rotulo: el numero 12, sin cuerpo que extraer"),
        ("L11 a L11", 11, 11, 0, "P2  titulo textual Task-Relevant Maturity, sin cuerpo que extraer"),
        ("L13 a L13", 13, 13, 0, "P3  la pregunta de si existe un estilo de direccion optimo unico: POSTURA de apertura"),
        ("L15 a L15", 15, 15, 0, "P4  la historia del estilo de mando segun la teoria de motivacion de cada epoca, sin un estilo mejor probado: POSTURA historica"),
        ("L17 a L17", 17, 17, 0, "P5  la rotacion de mandos intermedios en Intel y la conclusion de que el alto rendimiento es de la pareja mando mas grupo: CASO del autor, manual 3.5"),
        ("L19 a L19", 19, 19, 0, "P6  parte 1 de 5 de la pieza compuesta que cierra en P12 (L31 a L47): la TRM definida por su nombre y sus componentes, y su especificidad a la tarea concreta"),
        ("L21 a L21", 21, 21, 0, "P7  el vendedor ascendido a jefe de planta cuya TRM cae en el puesto nuevo: CASO del autor, manual 3.5, EXCLUIDO de la pieza compuesta de P6 a P12 por ser narracion de un hecho con nombre de puesto concreto y no inventario"),
        ("L23 a L23", 23, 23, 0, "P8  parte 2 de 5 de la pieza compuesta: la TRM puede caer si el ritmo o el puesto cambian de golpe, con la analogia de conducir en carretera comarcal contra autopista"),
        ("L25 a L25", 25, 25, 0, "P9  parte 3 de 5 de la pieza compuesta: los tres estilos segun la TRM en prosa, mas la vigilancia constante y la frontera delegar contra abandonar"),
        ("L27 a L27", 27, 27, 0, "P10 parte 4 de 5 de la pieza compuesta: la advertencia de no juzgar el estilo estructurado como menos valioso, el criterio es la eficacia y no lo simpatico"),
        ("L29 a L29", 29, 29, 0, "P11 la analogia completa del padre y el hijo que madura: CASO ilustrativo, manual 3.5, EXCLUIDO de la pieza compuesta por ser analogia y no doctrina de la organizacion"),
        ("L31 a L47", 31, 47, 1, "P12 parte 5 de 5 y CIERRE DE LA PIEZA COMPUESTA que empezo en P6 (L19): LA TABLA DE LOS TRES NIVELES DE TRM CON SU ESTILO DE DIRECCION, inventario propio del libro de objetos de trabajo, manual 9.1, nodo propio; P6, P8, P9, P10 y esta fila son la misma pieza y P7 y P11 quedan fuera de ella por ser CASO y analogia"),
        ("L49 a L49", 49, 49, 0, "P13 si el entorno del hijo cambia de golpe el padre puede volver a un estilo anterior: continuacion de la analogia de P11, CASO ilustrativo, excluida"),
        ("L51 a L51", 51, 51, 0, "P14 por que la estructura no cambia de fondo al moverse de estructurada a comunicadora a monitora, dicho sobre la analogia padre-hijo: explicacion del mecanismo de la analogia, no doctrina propia de la organizacion, excluida"),
        ("L53 a L53", 53, 53, 0, "P15 si el padre o el supervisor transmitio pronto los valores operativos correctos, el hijo o el subordinado decidira como el: PRECONDICION de valores compartidos para que la progresion funcione, tangencial a la eleccion de estilo por TRM y no desarrollada como procedimiento propio en este tramo, PENDIENTE para una lectura futura"),
        ("L55 a L55", 55, 55, 0, "P16 sin esa comunidad de valores la organizacion se confunde, y el caso del asociado que dejo aprender por las malas al junior: DEFINICION con CASO, manual 3.5, misma familia de P15"),
        ("L57 a L57", 57, 57, 0, "P17 rotulo Management Style and Managerial Leverage, sin cuerpo que extraer"),
        ("L59 a L59", 59, 59, 0, "P18 subir la TRM da palanca de mando porque el estilo de alta TRM cuesta menos tiempo: POSTURA que repite consecuencias de P12 sin inventario nuevo"),
        ("L61 a L61", 61, 61, 0, "P19 la TRM depende del entorno concreto de trabajo, con el sargento como CASO que sigue en el renglon siguiente: POSTURA mas arranque de CASO, manual 3.5"),
        ("L63 a L63", 63, 63, 0, "P20 el estilo de comunicacion exige tiempo y hay que ganarselo, y ante el cambio subito se vuelve al modo estructurado: POSTURA que repite P12 sin inventario nuevo"),
        ("L65 a L65", 65, 65, 0, "P21 el mando estructurado no es el favorito de un directivo ilustrado y por eso se adopta tarde: POSTURA"),
        ("L67 a L67", 67, 67, 0, "P22 rotulo It's Not Easy to Be a Good Manager, sin cuerpo que extraer"),
        ("L69 a L69", 69, 69, 0, "P23 decidir la TRM no es facil y las preferencias personales priman sobre la eleccion logica: POSTURA"),
        ("L71 a L71", 71, 71, 0, "P24 LA CIFRA DEL AUTOR: EL 90 POR CIENTO DE LOS SUPERVISORES SE VIO A SI MISMO MAS COMUNICADOR O DELEGADOR DE LO QUE LO VIERON SUS SUBORDINADOS, medida por el propio autor: manual principios 5 y 8, entra como atribucion dentro del nodo de P12 y NO CUENTA AQUI COMO NODO PROPIO PARA NO DUPLICAR EL 1 DE P12"),
        ("L73 a L73", 73, 73, 0, "P25 el mando que esquia y bebe con su supervisor y confunde amistad social con estilo comunicador: CASO, manual 3.5"),
        ("L75 a L77", 75, 77, 1, "P26 LA PREGUNTA DE SI CONVIENE HACERSE AMIGO DE UN SUBORDINADO, RESUELTA CON LA PRUEBA DE IMAGINAR UNA REVISION DE DESEMPENO DIFICIL: inventario propio del libro de dos ramas mas sus pros y contras generales, manual 9.1, nodo propio"),
    ],
}

TOPE = 30    # el techo de candidatos de D.58 en regimen ligero, para contrastar, no para decidir

total_nodos = 0
nodos_por_unidad = {}
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
    nodos_por_unidad[unidad] = nodos

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
print("NODOS QUE MI FRONTERA DA EN LAS TRES UNIDADES DE HOY (cap_11+cap_12+cap_13): %d" % total_nodos)
print("  cap_11: %d   cap_12: %d   cap_13: %d"
      % (nodos_por_unidad["cap_11"], nodos_por_unidad["cap_12"], nodos_por_unidad["cap_13"]))
print("TECHO DE CANDIDATOS DE D.58 EN REGIMEN LIGERO                  : %d" % TOPE)
print("DENTRO DEL TECHO DE CANDIDATOS                                 : %s"
      % ("SI" if total_nodos <= TOPE else "NO"))
