# -*- coding: utf-8 -*-
"""MI LECTURA DE LA FRONTERA DE cap_17 Y cap_18, PUBLICADA ANTES DE MINAR NADA.

Mismo instrumento que las vueltas 57 y 58 corrieron (.v57ext/frontera.py, .v58ext/frontera.py),
que a su vez reusaba el de las vueltas 56, 55 y 53: NI UNA LINEA DE SU MAQUINARIA DE MEDIR
TOCADA (EXTRACTOR.md 13, la moratoria de maquinaria). Lo que cambia es LA TABLA DE TRAMOS: es mi
lectura de hoy sobre los dos ultimos capitulos de grove_high_output.

CADA FILA ES, POR DEFECTO, UNA SOLA LINEA DE CONTENIDO DEL FICHERO FUENTE (mismo patron que las
tres vueltas anteriores). Cuando una pieza tarda mas de una linea en cerrarse, cada parte se
declara en su propia fila con 0 nodos y la fila que CIERRA la pieza lleva el 1, citando cuales
filas son la misma pieza.

cap_18 es el capitulo de cierre del libro (One More Thing...), una lista de asignaciones con
puntaje. CADA ITEM ES UNA SOLA LINEA QUE NOMBRA UNA TAREA YA DESPLEGADA EN OTRO CAPITULO DEL
PROPIO LIBRO (la vara de EXTRACTOR.md 9, NOMBRAR NO ES PROCEDIMENTAR): ninguna linea trae su
propio inventario de pasos, y la mayoria remite por su propio contenido a un procedimiento que
esta lote ya tiene en cuarentena o que un lote anterior ya inserto. Por eso cap_18 da 0 nodos, y
la tabla deja escrita al lado la referencia que sostiene cada lectura.

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
    "cap_17": [
        ("L9 a L9", 9, 9, 0, "P1  rotulo: el numero 16, sin cuerpo que extraer"),
        ("L11 a L11", 11, 11, 0, "P2  titulo textual Why Training Is the Boss's Job, sin cuerpo que extraer"),
        ("L13 a L13", 13, 13, 0, "P3  la anecdota del restaurante y la empleada nueva del telefono sin instruir: CASO de apertura, manual 3.5"),
        ("L15 a L15", 15, 15, 0, "P4  la anecdota del implantador de iones en Intel y el millon de dolares perdido por falta de entrenamiento: CASO, manual 3.5"),
        ("L17 a L17", 17, 17, 0, "P5  la importancia del entrenamiento se vuelve obvia tras estos problemas: POSTURA de transicion"),
        ("L19 a L19", 19, 19, 0, "P6  la cuestion de quien debe entrenar, y la creencia del autor de que debe ser el propio mando: POSTURA"),
        ("L21 a L21", 21, 21, 0, "P7  la definicion basica de que produce un mando, la salida de su organizacion: DEFINICION"),
        ("L23 a L23", 23, 23, 0, "P8  las dos vias para subir el desempeno individual, motivacion y capacidad: DEFINICION, taxonomia de dos sin pasos propios"),
        ("L25 a L25", 25, 25, 0, "P9  el ejemplo numerico de la palanca del entrenamiento, doce horas de preparacion por doscientas horas ganadas: CASO ilustrativo con numeros propios del ejemplo, manual 3.5"),
        ("L27 a L27", 27, 27, 0, "P10 el entrenamiento tiene que atender lo que el estudiante necesita, con la salvedad de los cursos enlatados externos: POSTURA"),
        ("L29 a L29", 29, 29, 0, "P11 la anecdota de los consultores externos y el curso de desarrollo de carrera desalineado con la practica de Intel: CASO, manual 3.5"),
        ("L31 a L31", 31, 31, 0, "P12 el entrenamiento tiene que ser un proceso continuo y no un evento aislado: POSTURA"),
        ("L33 a L33", 33, 33, 0, "P13 quien tiene que entrenar es el propio mando, en cascada por todos los niveles de supervision: POSTURA"),
        ("L35 a L35", 35, 35, 0, "P14 el mando tiene que ser el instructor porque debe representar un modelo de rol creible, un delegado no puede asumir ese papel: POSTURA"),
        ("L37 a L37", 37, 37, 0, "P15 la cifra propia de Intel, entre el dos y el cuatro por ciento del tiempo del empleado en el aula: ATRIBUCION de la propia empresa del autor, sin fecha de corte externa que verificar, principio 8 no aplica a una practica interna sin cita de tercero"),
        ("L39 a L39", 39, 39, 0, "P16 el catalogo universitario de Intel con mas de cincuenta clases, y el ejemplo del curso del implantador de iones: CASO, manual 3.5"),
        ("L41 a L41", 41, 41, 0, "P17 el propio repertorio de cursos del autor, resenas de desempeno, reuniones productivas e introduccion a Intel: CASO en primera persona, manual 3.5"),
        ("L43 a L43", 43, 43, 0, "P18 la distincion entre dos tareas de entrenamiento, ensenar habilidades a nuevos miembros y ensenar ideas nuevas a los miembros actuales: DEFINICION, taxonomia de dos sin pasos propios"),
        ("L45 a L45", 45, 45, 0, "P19 la magnitud de la tarea de entrenar nuevos empleados, con el ejemplo numerico del diez por ciento de rotacion mas diez por ciento de crecimiento: CASO ilustrativo con numeros propios, manual 3.5"),
        ("L47 a L47", 47, 47, 0, "P20 la magnitud aun mayor de ensenar ideas nuevas a todo el departamento, con el ejemplo del coste de un millon de dolares: CASO ilustrativo con numeros propios, manual 3.5"),
        ("L49 a L51", 49, 51, 1, "P21 parte 1 de 1 y CIERRE DE LA PIEZA de planificacion: hacer una lista sin limitar su alcance de en que deberian entrenarse los subordinados, preguntar a la propia gente que necesita, tomar inventario de los mando maestros y materiales disponibles, y asignar prioridades entre esos items; inventario propio del libro de pasos, manual 9.1, nodo propio"),
        ("L53 a L59", 53, 59, 1, "P22 parte 1 de 1 y CIERRE DE LA PIEZA de desarrollo del primer curso: empezar sin ambicion desarrollando un curso corto de tres a cuatro clases sobre el tema mas urgente, fijar un calendario con plazos y comprometerse con el, crear un esquema del curso entero, desarrollar solo la primera clase y dictarla, desarrollar la segunda clase despues de haber dado la primera, tratar la primera vez como un desechable y ensenarsela a los subordinados mas informados para perfeccionarla con su critica, y preguntarse si se podra cubrir a toda la organizacion uno mismo o si hace falta preparar a otros instructores con el primer set de clases; inventario propio del libro de pasos, manual 9.1, nodo propio"),
        ("L61 a L61", 61, 61, 1, "P23 parte 1 de 1 y pieza de una sola linea que cierra en si misma: pedir criticas anonimas a los alumnos tras dar el curso, usar un formulario con calificaciones numericas y preguntas abiertas, estudiar las respuestas sabiendo que nunca se complacera a todos, y tener como objetivo ultimo satisfacerse uno mismo de que se esta logrando el proposito; inventario propio del libro de pasos, manual 9.1, nodo propio"),
        ("L63 a L63", 63, 63, 0, "P24 anuncio de que la primera vez que se ensena se descubren unas cuantas cosas: DEFINICION de transicion que anuncia la lista de P25 a P27"),
        ("L65 a L65", 65, 65, 0, "P25 parte 1 de 3 de la lista que cierra en P27 (L69): el entrenamiento es trabajo duro, se descubre cuanto no se sabe: POSTURA reflexiva, no es paso a ejecutar"),
        ("L67 a L67", 67, 67, 0, "P26 parte 2 de 3: quien mas aprende del curso es quien lo da: POSTURA reflexiva"),
        ("L69 a L69", 69, 69, 0, "P27 parte 3 de 3 y CIERRE de la lista que empezo en P25 (L65): el proceso de entrenar resulta exaltante y produce calidez al ver a un subordinado practicar lo ensenado: POSTURA reflexiva de cierre, taxonomia de tres observaciones sobre la experiencia y no un inventario de medios o etapas del procedimiento, 9.1 restriccion 1, ninguna de las tres lineas es paso ejecutable"),
    ],
    "cap_18": [
        ("L9 a L9", 9, 9, 0, "P1  rotulo One More Thing..., sin cuerpo que extraer"),
        ("L11 a L11", 11, 11, 0, "P2  postura de apertura, invito a elegir asignaciones y hacerlas con honestidad: POSTURA"),
        ("L13 a L13", 13, 13, 0, "P3  postura, cien puntos de asignaciones hacen a un mejor mando: POSTURA"),
        ("L15 a L15", 15, 15, 0, "P4  rotulo Production, sin cuerpo que extraer"),
        ("L17 a L17", 17, 17, 0, "P5  rotulo Points, encabezado de columna sin cuerpo que extraer"),
        ("L19 a L19", 19, 19, 0, "P6  item 1: identificar las operaciones de proceso, montaje y prueba en el propio trabajo, una sola linea sin pasos propios que la libro despliegue, nombra el procedimiento ya extraido en clasificar_trabajo_proceso_montaje_prueba (cuarentena grove_high_output), EXTRACTOR.md 9 nombrar no es procedimentar"),
        ("L21 a L21", 21, 21, 0, "P7  puntaje del item 1: 10, sin cuerpo que extraer"),
        ("L23 a L23", 23, 23, 0, "P8  item 2: identificar el paso limitante de un proyecto y mapear el flujo alrededor, una sola linea que nombra el procedimiento ya extraido en rehacer_flujo_paso_limitante_capacidad y construir_flujo_produccion_paso_limitante (cuarentena grove_high_output), nombrar no es procedimentar"),
        ("L25 a L25", 25, 25, 0, "P9  puntaje del item 2: 10, sin cuerpo que extraer"),
        ("L27 a L27", 27, 27, 0, "P10 item 3: definir los lugares de inspeccion de recepcion, en proceso y final, decidir si son de vigilancia o de barrera, identificar cuando relajarlas a un esquema variable, una sola linea que nombra los procedimientos ya extraidos en elegir_inspeccion_barrera_monitorizacion, preferir_inspeccion_proceso_prueba_destructiva y variar_frecuencia_inspeccion_nivel_calidad (cuarentena grove_high_output), nombrar no es procedimentar"),
        ("L29 a L29", 29, 29, 0, "P11 puntaje del item 3: 10, sin cuerpo que extraer"),
        ("L31 a L31", 31, 31, 0, "P12 item 4: identificar media docena de indicadores nuevos que midan cantidad y calidad de la salida, una sola linea que nombra el procedimiento ya extraido en elegir_cinco_indicadores_diarios_fabrica y emparejar_indicadores_efecto_contraefecto (cuarentena grove_high_output), nombrar no es procedimentar"),
        ("L33 a L33", 33, 33, 0, "P13 puntaje del item 4: 10, sin cuerpo que extraer"),
        ("L35 a L35", 35, 35, 0, "P14 item 5: instalar esos indicadores como rutina y establecer su revision regular en las reuniones de equipo, una sola linea sin pasos propios, tema ya cubierto por archivar_indicadores_resolver_problemas y cubrir_indicadores_problemas_reunion_individual (cuarentena grove_high_output), nombrar no es procedimentar"),
        ("L37 a L37", 37, 37, 0, "P15 puntaje del item 5: 20, sin cuerpo que extraer"),
        ("L39 a L39", 39, 39, 0, "P16 item 6: identificar la estrategia mas importante, describir la demanda del entorno que la motivo y el estado o impulso actual, una sola linea que nombra los procedimientos ya extraidos en examinar_demanda_entorno_dos_marcos_temporales, planificar_tres_pasos_demanda_estado_brecha y cerrar_brecha_dos_preguntas_estrategia (cuarentena grove_high_output), nombrar no es procedimentar"),
        ("L41 a L41", 41, 41, 0, "P17 puntaje del item 6: 20, sin cuerpo que extraer"),
        ("L43 a L43", 43, 43, 0, "P18 rotulo Leverage, sin cuerpo que extraer"),
        ("L45 a L45", 45, 45, 0, "P19 item 7: hacer simplificacion del trabajo en la tarea mas tediosa, eliminar al menos el treinta por ciento de los pasos, una sola linea que nombra literalmente el procedimiento ya extraido en simplificar_trabajo_reducir_numero_pasos (cuarentena grove_high_output), nombrar no es procedimentar"),
        ("L47 a L47", 47, 47, 0, "P20 puntaje del item 7: 10, sin cuerpo que extraer"),
        ("L49 a L49", 49, 49, 0, "P21 item 8: definir la propia salida y listar sus elementos por orden de importancia, una sola linea sin pasos propios que el libro despliegue aqui, tema ya cubierto en el capitulo de la produccion como salida gerencial de unidades anteriores del propio libro (cap_01 a cap_09, ya insertadas en dataset), nombrar no es procedimentar"),
        ("L51 a L51", 51, 51, 0, "P22 puntaje del item 8: 10, sin cuerpo que extraer"),
        ("L53 a L53", 53, 53, 0, "P23 item 9: analizar el sistema de recoleccion de informacion, balanceado entre titulares, articulos y revistas semanales, con redundancia, una sola linea que nombra el procedimiento ya extraido en reunir_informacion_gerencial_vias_variadas y escalonar_fuentes_informacion_gerencial (cuarentena grove_high_output), nombrar no es procedimentar"),
        ("L55 a L55", 55, 55, 0, "P24 puntaje del item 9: 10, sin cuerpo que extraer"),
        ("L57 a L57", 57, 57, 0, "P25 item 10: hacer una gira y listar las transacciones en que se participo, una sola linea que nombra el procedimiento ya extraido en programar_visita_area_observar_despachar (cuarentena grove_high_output), nombrar no es procedimentar"),
        ("L59 a L59", 59, 59, 0, "P26 puntaje del item 10: 10, sin cuerpo que extraer"),
        ("L61 a L61", 61, 61, 0, "P27 item 11: crear una excusa mensual para una gira, una sola linea que remite al mismo procedimiento de la gira de P25 (programar_visita_area_observar_despachar), repeticion del mismo objeto, P.19"),
        ("L63 a L63", 63, 63, 0, "P28 puntaje del item 11: 10, sin cuerpo que extraer"),
        ("L65 a L65", 65, 65, 0, "P29 item 12: describir como se vigilara el proximo proyecto delegado, una sola linea que nombra el procedimiento ya extraido en supervisar_tarea_delegada_etapa_menor_valor y supervisar_decision_delegada_preguntas_concretas (cuarentena grove_high_output), nombrar no es procedimentar"),
        ("L67 a L67", 67, 67, 0, "P30 puntaje del item 12: 10, sin cuerpo que extraer"),
        ("L69 a L69", 69, 69, 0, "P31 item 13: generar un inventario de proyectos discrecionales, una sola linea que nombra literalmente el procedimiento ya extraido en llevar_inventario_proyectos_discrecionales (cuarentena grove_high_output), nombrar no es procedimentar"),
        ("L71 a L71", 71, 71, 0, "P32 puntaje del item 13: 10, sin cuerpo que extraer"),
        ("L73 a L73", 73, 73, 0, "P33 item 14: hacer una reunion individual programada con cada subordinado, explicarsela antes y hacer que se preparen, una sola linea que nombra los procedimientos ya extraidos en fijar_duracion_lugar_reunion_individual y preparar_guion_reunion_individual_subordinado (cuarentena grove_high_output), nombrar no es procedimentar"),
        ("L75 a L75", 75, 75, 0, "P34 puntaje del item 14: 20, sin cuerpo que extraer"),
        ("L77 a L77", 77, 77, 0, "P35 item 15: clasificar las actividades de la ultima semana por palanca y generar un plan para hacer mas de la categoria alta, una sola linea que nombra los procedimientos ya extraidos en buscar_actividad_alta_palanca_tres_vias, detectar_palanca_negativa_actividad_mando y elegir_momento_actividad_palanca_maxima (cuarentena grove_high_output), nombrar no es procedimentar"),
        ("L79 a L79", 79, 79, 0, "P36 puntaje del item 15: 10, sin cuerpo que extraer"),
        ("L81 a L81", 81, 81, 0, "P37 item 16: pronosticar la demanda de tiempo de la proxima semana, clasificar las reuniones y reducir las de mision si pasan del veinticinco por ciento, una sola linea que nombra el procedimiento ya extraido en usar_tres_clases_reunion_proceso (cuarentena grove_high_output), nombrar no es procedimentar"),
        ("L83 a L83", 83, 83, 0, "P38 puntaje del item 16: 10, sin cuerpo que extraer"),
        ("L85 a L85", 85, 85, 0, "P39 item 17: definir los tres objetivos mas importantes de la organizacion para los proximos tres meses, respaldados con resultados clave, una sola linea sin pasos propios que el libro despliegue aqui, tema ya cubierto en fijar_periodo_direccion_objetivos_retroalimentacion, fijar_meta_direccion_objetivos_mitad_probabilidad y contestar_dos_preguntas_direccion_objetivos (cuarentena grove_high_output), nombrar no es procedimentar"),
        ("L87 a L87", 87, 87, 0, "P40 puntaje del item 17: 20, sin cuerpo que extraer"),
        ("L89 a L89", 89, 89, 0, "P41 item 18: hacer que los subordinados hagan lo mismo tras discutir el conjunto generado arriba, una sola linea que remite al mismo procedimiento de objetivos de P39, repeticion del mismo objeto, P.19"),
        ("L91 a L91", 91, 91, 0, "P42 puntaje del item 18: 20, sin cuerpo que extraer"),
        ("L93 a L93", 93, 93, 0, "P43 item 19: generar un inventario de decisiones pendientes y estructurar tres usando el enfoque de las seis preguntas, una sola linea que nombra literalmente el procedimiento ya extraido en zanjar_seis_preguntas_decision_adelantado y conducir_etapas_modelo_ideal_decision (cuarentena grove_high_output), nombrar no es procedimentar"),
        ("L95 a L95", 95, 95, 0, "P44 puntaje del item 19: 10, sin cuerpo que extraer"),
        ("L97 a L97", 97, 97, 0, "P45 item 20: evaluar el propio estado motivacional segun la jerarquia de Maslow y hacer lo mismo con cada subordinado, una sola linea que remite a la jerarquia de Maslow ya tratada en diagnosticar_nivel_motivacion_reaccion_aumento_salario y diagnosticar_capacidad_motivacion_prueba_vida (cuarentena grove_high_output), nombrar no es procedimentar"),
        ("L99 a L99", 99, 99, 0, "P46 puntaje del item 20: 10, sin cuerpo que extraer"),
        ("L101 a L101", 101, 101, 0, "P47 item 21: dar a los subordinados una pista de carreras, un conjunto de indicadores de desempeno para cada uno, una sola linea sin pasos propios que el libro despliegue aqui, tema de indicadores ya cubierto en elegir_cinco_indicadores_diarios_fabrica y emparejar_indicadores_efecto_contraefecto (cuarentena grove_high_output), nombrar no es procedimentar"),
        ("L103 a L103", 103, 103, 0, "P48 puntaje del item 21: 20, sin cuerpo que extraer"),
        ("L105 a L105", 105, 105, 0, "P49 item 22: listar las formas de retroalimentacion relevante a la tarea que reciben los subordinados, una sola linea sin pasos propios, tema de la retroalimentacion relevante a la tarea que titula el propio cap_16 del libro (compensation as task relevant feedback, ya en cuarentena grove_high_output), nombrar no es procedimentar"),
        ("L107 a L107", 107, 107, 0, "P50 puntaje del item 22: 10, sin cuerpo que extraer"),
        ("L109 a L109", 109, 109, 0, "P51 item 23: clasificar la madurez relevante a la tarea de cada subordinado y evaluar el estilo de direccion apropiado, una sola linea que nombra literalmente el procedimiento ya extraido en elegir_estilo_direccion_madurez_relevante_tarea (cuarentena grove_high_output), nombrar no es procedimentar"),
        ("L111 a L111", 111, 111, 0, "P52 puntaje del item 23: 10, sin cuerpo que extraer"),
        ("L113 a L113", 113, 113, 0, "P53 item 24: evaluar la ultima revision de desempeno recibida y las que se dieron, como medio de retroalimentacion relevante a la tarea, una sola linea sin pasos propios, tema ya cubierto en entregar_evaluacion_desempeno_tres_claves (cuarentena grove_high_output), nombrar no es procedimentar"),
        ("L115 a L115", 115, 115, 0, "P54 puntaje del item 24: 20, sin cuerpo que extraer"),
        ("L117 a L117", 117, 117, 0, "P55 item 25: rehacer una de esas revisiones como debio hacerse, una sola linea que remite al mismo procedimiento de revision de desempeno de P53, repeticion del mismo objeto, P.19"),
        ("L119 a L119", 119, 119, 0, "P56 puntaje del item 25: 10, sin cuerpo que extraer"),
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
print("NODOS QUE MI FRONTERA DA EN LOS DOS CAPITULOS DE HOY (cap_17+cap_18): %d" % total_nodos)
print("  cap_17: %d   cap_18: %d" % (nodos_por_unidad["cap_17"], nodos_por_unidad["cap_18"]))
print("TECHO DE CANDIDATOS DE D.58 EN REGIMEN LIGERO                  : %d" % TOPE)
print("DENTRO DEL TECHO DE CANDIDATOS                                 : %s"
      % ("SI" if total_nodos <= TOPE else "NO"))
