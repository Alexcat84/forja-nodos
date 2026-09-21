# -*- coding: utf-8 -*-
"""MI LECTURA DE LA FRONTERA DE cap_14, cap_15 Y cap_16, PUBLICADA ANTES DE MINAR NADA.

Mismo instrumento que la vuelta 57 corrio sobre cap_11, cap_12 y cap_13 (.v57ext/frontera.py),
que a su vez reusaba el de las vueltas 56, 55 y 53: NI UNA LINEA DE SU MAQUINARIA DE MEDIR
TOCADA (EXTRACTOR.md 13, la moratoria de maquinaria). Lo que cambia, y lo digo por su nombre
porque toco el bloque que imprime, es LA TABLA DE TRAMOS: es mi lectura de hoy sobre tres
capitulos nuevos. No retiro ninguna linea del bloque 3 (EL TECHO) de la vuelta 57 porque no
nombraba ningun candidato concreto que ya no aplique hoy.

CADA FILA ES, POR DEFECTO, UNA SOLA LINEA DE CONTENIDO DEL FICHERO FUENTE** (el mismo patron que
uso la vuelta 57 para la mayoria de sus filas de cap_11 y cap_12). Solo agrupo varias lineas de
contenido en una misma fila cuando forman una sola pieza que el propio libro presenta como una
unidad (una lista de items, una tabla, un parrafo que se numera a si mismo). Cuando una pieza
tarda mas de un parrafo en cerrarse, sigo el mismo patron que la vuelta 57 uso en el TRM de
cap_13 (L31 a L47): cada parte se declara en su propia fila con 0 nodos y la fila que CIERRA la
pieza lleva el 1, citando cuales filas son la misma pieza y cuales quedan fuera por ser CASO,
taxonomia distinta o pie de figura.

LA REPETICION INTERNA (P.19, 14 ago 2026): en cap_15, las cuatro categorias de informacion de
entrevista (L57) reparten las mismas nueve preguntas ya extraidas en L39 a L55 (L61 a L87). El
objeto ya esta en casa: esa fila NO genera nodo propio, se declara como repeticion y se funde en
la lectura de la pieza de L39 a L55 en vez de fabricar su gemelo.

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
    "cap_14": [
        ("L9 a L9", 9, 9, 0, "P1  rotulo: el numero 13, sin cuerpo que extraer"),
        ("L11 a L11", 11, 11, 0, "P2  titulo textual Performance Appraisal: Manager as Judge and Jury, sin cuerpo que extraer"),
        ("L13 a L13", 13, 13, 0, "P3  rotulo Why Bother?, sin cuerpo que extraer"),
        ("L15 a L15", 15, 15, 0, "P4  la pregunta que el autor planteo a un grupo de mandos intermedios sobre por que existen las revisiones: POSTURA de apertura"),
        ("L17 a L31", 17, 31, 0, "P5  las ocho respuestas del grupo sobre para que sirve la revision: CASO, encuesta de practicantes y no inventario propio del libro, manual 3.5"),
        ("L33 a L33", 33, 33, 0, "P6  la segunda pregunta del autor sobre como se siente el supervisor al dar la revision: POSTURA de transicion"),
        ("L35 a L49", 35, 49, 0, "P7  las ocho respuestas del grupo sobre los sentimientos al dar una revision: CASO, encuesta de practicantes, manual 3.5"),
        ("L51 a L51", 51, 51, 0, "P8  la tercera pregunta del autor sobre que fallaba en las revisiones que ellos mismos recibieron: POSTURA de transicion"),
        ("L53 a L65", 53, 65, 0, "P9  las siete respuestas del grupo sobre los defectos de las revisiones recibidas: CASO, encuesta de practicantes, manual 3.5"),
        ("L67 a L67", 67, 67, 0, "P10 conclusion de que dar revisiones es dificil y los mandos no lo hacen especialmente bien: POSTURA"),
        ("L69 a L69", 69, 69, 0, "P11 la revision es la forma mas importante de feedback relevante a la tarea y una de las actividades de mayor palanca del mando: POSTURA"),
        ("L71 a L71", 71, 71, 0, "P12 el proposito fundamental de la revision es mejorar el desempeno del subordinado, dividido en nivel de habilidad y motivacion: DEFINICION"),
        ("L73 a L73", 73, 73, 0, "P13 la revision como el acto mas formal de liderazgo institucionalizado, el mando como juez y jurado: DEFINICION"),
        ("L75 a L75", 75, 75, 0, "P14 la responsabilidad del supervisor y la anecdota hungara sobre la palabra argument: CASO, manual 3.5"),
        ("L77 a L77", 77, 77, 0, "P15 las revisiones de desempeno no son solo para grandes organizaciones: POSTURA"),
        ("L79 a L79", 79, 79, 0, "P16 los dos aspectos de la revision, evaluar y entregar, son igual de dificiles: DEFINICION de transicion"),
        ("L81 a L81", 81, 81, 0, "P17 rotulo Assessing Performance, sin cuerpo que extraer"),
        ("L83 a L83", 83, 83, 0, "P18 evaluar el desempeno de profesionales de forma objetiva es dificil, el supervisor camina en la cuerda floja entre objetividad y juicio: POSTURA"),
        ("L85 a L85", 85, 85, 0, "P19 para facilitar la evaluacion el supervisor debe aclarar de antemano que espera del subordinado: POSTURA"),
        ("L87 a L87", 87, 87, 0, "P20 la caja negra gerencial, medidas de salida y medidas internas, sin formula estricta de ponderacion entre ambas: DEFINICION, el propio texto no fija criterio y varia caso a caso, 9.1 restriccion 2"),
        ("L89 a L89", 89, 89, 0, "P21 el compromiso entre desempeno orientado a largo y a corto plazo, con la idea de valor presente: DEFINICION"),
        ("L91 a L91", 91, 91, 0, "P22 el factor tiempo entre actividad y resultado, y la historia del gerente cuya organizacion tuvo un año superior: CASO, manual 3.5"),
        ("L93 a L93", 93, 93, 0, "P23 continuacion de la historia, el año siguiente la organizacion se desploma: CASO, manual 3.5"),
        ("L95 a L95", 95, 95, 0, "P24 el desfase de tiempo tambien opera al reves, la historia de la planta de produccion de Intel: CASO, manual 3.5"),
        ("L97 a L97", 97, 97, 0, "P25 al revisar a un gerente hay que juzgar su desempeno y el de su grupo a la vez: POSTURA"),
        ("L99 a L99", 99, 99, 0, "P26 la trampa del potencial y la historia del gerente general que no se aprueba: CASO, manual 3.5"),
        ("L101 a L101", 101, 101, 0, "P27 la decision de ascender esta ligada a la revision y comunica valores a la organizacion: POSTURA"),
        ("L103 a L103", 103, 103, 0, "P28 es dificil evaluar el desempeno pero tambien hay que intentar mejorarlo con retrospectiva: POSTURA"),
        ("L105 a L105", 105, 105, 0, "P29 rotulo Delivering the Assessment, sin cuerpo que extraer"),
        ("L107 a L107", 107, 107, 0, "P30 cabeza de pieza compuesta que cierra en P36 (L119): anuncio de las tres L a tener en cuenta al entregar la revision, Level, Listen y Leave yourself out"),
        ("L109 a L109", 109, 109, 0, "P31 parte 1 de 3 de la pieza: Level, ser totalmente franco tanto al elogiar como al criticar"),
        ("L111 a L111", 111, 111, 0, "P32 parte 2 de 3, primer tramo: Listen, el significado especial de escuchar y el recorrido de un pensamiento de un cerebro a otro"),
        ("L113 a L113", 113, 113, 0, "P33 parte 2 de 3, segundo tramo: como asegurarse de ser oido, observar al subordinado y no parar hasta estar seguro de que el mensaje llego"),
        ("L115 a L115", 115, 115, 0, "P34 parte 2 de 3, cierre del tramo Listen: usar toda la capacidad sensorial para verificar que el mensaje se interpreta bien"),
        ("L117 a L117", 117, 117, 0, "P35 el profesor de aula que sabe si le entienden y ajusta su explicacion: CASO ilustrativo de la escucha, manual 3.5, EXCLUIDO de la pieza compuesta"),
        ("L119 a L119", 119, 119, 1, "P36 parte 3 de 3 y CIERRE DE LA PIEZA COMPUESTA que empezo en P30 (L107): Leave yourself out, dejar fuera las propias inseguridades y controlar las emociones propias durante la entrega; P30, P31, P32, P33 y P34 son la misma pieza y P35 queda fuera por ser CASO ilustrativo, inventario propio del libro de tres ramas, manual 9.1, nodo propio"),
        ("L121 a L121", 121, 121, 0, "P37 anuncio de que existen tres tipos de revision de desempeno: DEFINICION de transicion, taxonomia sin pasos propios"),
        ("L123 a L123", 123, 123, 0, "P38 rotulo On the One Hand...On the Other Hand..., sin cuerpo que extraer"),
        ("L125 a L125", 125, 125, 0, "P39 la mayoria de las revisiones caen en esta categoria mixta, con sus problemas tipicos: DEFINICION"),
        ("L127 a L127", 127, 127, 0, "P40 el subordinado solo puede absorber un numero finito de mensajes: POSTURA"),
        ("L129 a L129", 129, 129, 0, "P41 parte 1 de 2 de la pieza que cierra en P42 (L131): el metodo de la hoja de trabajo, reunir el material (informes de avance, objetivos trimestrales, notas de reuniones individuales) y anotarlo todo sin editar en una hoja en blanco"),
        ("L131 a L131", 131, 131, 1, "P42 parte 2 de 2 y CIERRE DE LA PIEZA que empezo en P41 (L129): buscar relaciones entre lo anotado, nombrarlas mensajes, y descartar los mensajes que el subordinado no podria retener; P41 y esta fila son la misma pieza, inventario propio del libro de pasos, manual 9.1, nodo propio"),
        ("L133 a L157", 133, 157, 0, "P43 el ejemplo relleno de la hoja de trabajo con sus positivos, negativos y tres mensajes numerados: CASO, el entregable del caso lleva datos del caso, manual 3.5, EXCLUIDO como nodo propio"),
        ("L159 a L159", 159, 159, 0, "P44 las sorpresas en una revision, si aparecen hay que entregarlas igual: POSTURA"),
        ("L161 a L161", 161, 161, 0, "P45 remite a la figura de una revision mixta anotada, sin cuerpo propio que transcribir"),
        ("L163 a L163", 163, 163, 0, "P46 rotulo The Blast, sin cuerpo que extraer"),
        ("L165 a L165", 165, 165, 0, "P47 introduccion al problema grave de desempeno que puede acabar en despido: POSTURA de apertura"),
        ("L167 a L167", 167, 167, 0, "P48 parte 1 de 3 de la pieza que cierra en P54 (L179): las etapas por las que pasa el subordinado ante un problema grave, ignorar, negar y culpar a otros, con la evidencia como palanca contra las dos primeras"),
        ("L169 a L169", 169, 169, 0, "P49 pie de figura de las etapas de resolucion de problemas, sin cuerpo propio que transcribir"),
        ("L171 a L171", 171, 171, 0, "P50 parte 2 de 3 de la pieza: es tarea del revisor llevar al subordinado por todas las etapas hasta que asuma responsabilidad, llevando la cuenta de en que etapa esta"),
        ("L173 a L173", 173, 173, 0, "P51 los tres desenlaces posibles de la revision dificil: DEFINICION, taxonomia distinta de la pieza de etapas, no forma parte de ella"),
        ("L175 a L175", 175, 175, 0, "P52 cualquier desenlace con compromiso de accion es aceptable: POSTURA, criterio de la taxonomia de P51"),
        ("L177 a L177", 177, 177, 0, "P53 la anecdota de Andy, no me vas a convencer nunca: CASO, manual 3.5"),
        ("L179 a L179", 179, 179, 1, "P54 parte 3 de 3 y CIERRE DE LA PIEZA que empezo en P48 (L167): si el subordinado no avanza mas alla de culpar a otros, el mando asume el papel formal de jefe, da la instruccion explicita y vigila el cumplimiento del compromiso; P48 y P50 y esta fila son la misma pieza y P49, P51, P52 y P53 quedan fuera por ser pie de figura, taxonomia distinta y CASO, inventario propio del libro de etapas, manual 9.1, nodo propio"),
        ("L181 a L181", 181, 181, 0, "P55 la historia de la resena reescrita sin acuerdo del subordinado: CASO, manual 3.5"),
        ("L183 a L183", 183, 183, 0, "P56 rotulo Reviewing the Ace, sin cuerpo que extraer"),
        ("L185 a L185", 185, 185, 0, "P57 el ejercicio con veinte mandos intermedios analizando sus propias revisiones: CASO con POSTURA de apertura"),
        ("L187 a L187", 187, 187, 0, "P58 el grupo de triunfadores recibio revisiones retrospectivas sin apenas guia de mejora: POSTURA, hallazgo del propio ejercicio"),
        ("L189 a L189", 189, 189, 0, "P59 conviene invertir mas en mejorar a las estrellas, actividad de alta palanca: POSTURA"),
        ("L191 a L191", 191, 191, 0, "P60 a todos cuesta decir cosas criticas pero siempre hay margen de mejora: POSTURA"),
        ("L193 a L193", 193, 193, 0, "P61 rotulo Other Thoughts and Practices, sin cuerpo que extraer"),
        ("L195 a L195", 195, 195, 0, "P62 si conviene pedir una autorevision previa al subordinado: POSTURA"),
        ("L197 a L197", 197, 197, 0, "P63 si conviene que el subordinado evalue al supervisor, con estatus solo consultivo: POSTURA"),
        ("L199 a L199", 199, 199, 0, "P64 los pros y contras de entregar la resena escrita antes, durante o despues de la conversacion: POSTURA"),
        ("L201 a L201", 201, 201, 0, "P65 la recomendacion de entregar la resena escrita antes de la reunion cara a cara para que el subordinado la digiera: POSTURA, preferencia unica sin pasos adicionales que desplegar"),
        ("L203 a L203", 203, 203, 0, "P66 cierre del capitulo, la revision es una de las tareas mas dificiles del mando: POSTURA de cierre"),
    ],
    "cap_15": [
        ("L9 a L9", 9, 9, 0, "P1  rotulo: el numero 14, sin cuerpo que extraer"),
        ("L11 a L11", 11, 11, 0, "P2  titulo textual Two Difficult Tasks, sin cuerpo que extraer"),
        ("L13 a L13", 13, 13, 0, "P3  las dos tareas emocionalmente cargadas del mando, entrevistar y retener a quien quiere irse: POSTURA de apertura"),
        ("L15 a L15", 15, 15, 0, "P4  rotulo Interviewing, sin cuerpo que extraer"),
        ("L17 a L25", 17, 25, 0, "P5  los cuatro propositos de la entrevista, seleccionar, educar, determinar encaje y vender el puesto: inventario del libro pero de FINES y no de medios ni etapas, 9.1 restriccion 1, no cuenta como nodo"),
        ("L27 a L27", 27, 27, 0, "P6  los medios disponibles, una hora de entrevista y comprobar referencias del candidato: POSTURA"),
        ("L29 a L29", 29, 29, 0, "P7  la comprobacion de referencias no exime de aprovechar la entrevista misma: POSTURA"),
        ("L31 a L31", 31, 31, 0, "P8  rotulo CONDUCTING THE INTERVIEW, sin cuerpo que extraer"),
        ("L33 a L33", 33, 33, 0, "P9  el candidato debe hablar el 80 por ciento del tiempo, escucha activa e interrupcion si se desvia: POSTURA, tecnica en prosa continua sin inventario propio nombrado"),
        ("L35 a L35", 35, 35, 0, "P10 dirigir la conversacion hacia temas familiares a ambos: POSTURA"),
        ("L37 a L37", 37, 37, 0, "P11 cabeza de la pieza que cierra en P12 (L55): un grupo de mandos aporto las mejores preguntas para una entrevista"),
        ("L39 a L55", 39, 55, 1, "P12 CIERRE DE LA PIEZA que empezo en P11 (L37): las nueve preguntas literales aportadas por el grupo de mandos, listas para usar en la entrevista; inventario propio del libro de objetos de trabajo, manual 9.1, nodo propio"),
        ("L57 a L57", 57, 57, 0, "P13 la informacion buscada cae en cuatro categorias nombradas por el propio texto, tecnico, que hizo con el saber, discrepancias y valores operativos: DEFINICION que anuncia una clasificacion"),
        ("L59 a L87", 59, 87, 0, "P14 el reparto de las mismas nueve preguntas de P12 bajo las cuatro categorias de P13: repite el mismo objeto ya capturado en P12 dentro del propio candidato, P.19, no genera nodo propio y se funde en la lectura de la pieza ya extraida"),
        ("L89 a L89", 89, 89, 0, "P15 el proposito ultimo de entrevistar es juzgar el potencial, en tension con la trampa del potencial de la revision de desempeno: POSTURA"),
        ("L91 a L91", 91, 91, 0, "P16 la autoevaluacion del candidato como via de respuestas directas: POSTURA, tecnica sin inventario propio nombrado"),
        ("L93 a L93", 93, 93, 0, "P17 la historia del candidato de Harvard y el coste del wafer: CASO, manual 3.5"),
        ("L95 a L95", 95, 95, 0, "P18 dejar que el candidato pregunte revela sus capacidades, con la historia de la memoria anual marcada: POSTURA con CASO, manual 3.5"),
        ("L97 a L97", 97, 97, 0, "P19 comprobar referencias busca la misma informacion, y el vinculo personal ayuda a que se abran: POSTURA"),
        ("L99 a L99", 99, 99, 0, "P20 conviene una segunda entrevista tras comprobar referencias: POSTURA"),
        ("L101 a L101", 101, 101, 0, "P21 la historia de la silla de tres patas del almirante Rickover y la preferencia por una entrevista franca: CASO, manual 3.5"),
        ("L103 a L103", 103, 103, 0, "P22 la historia del ejecutivo cuidadosamente entrevistado que resulto un desastre, no hay garantias: CASO, manual 3.5"),
        ("L105 a L105", 105, 105, 0, "P23 rotulo I Quit!, sin cuerpo que extraer"),
        ("L107 a L107", 107, 107, 0, "P24 lo que mas teme el mando, un subordinado valioso que decide irse: POSTURA de apertura"),
        ("L109 a L109", 109, 109, 0, "P25 el primer aviso ocurre de pasada y la reaccion inicial del mando es crucial: POSTURA, escenario que activa la pieza de L111"),
        ("L111 a L111", 111, 111, 1, "P26 la respuesta al primer momento del anuncio, en siete pasos dentro del mismo parrafo: dejar lo que se esta haciendo, sentarlo y preguntar por que se va, dejarlo hablar sin discutir, hacer mas preguntas cuando termine, no discutir ni sermonear ni entrar en panico, pedir tiempo para el siguiente encuentro, y cumplir lo que se prometa; inventario propio del libro de pasos, manual 9.1, nodo propio"),
        ("L113 a L113", 113, 113, 0, "P27 parte 1 de 5 de la pieza que cierra en P31 (L121): llevar el problema al propio jefe y hacerlo participar de la solucion"),
        ("L115 a L115", 115, 115, 0, "P28 parte 2 de 5: perseguir cada via para retener al subordinado, incluida la transferencia, y asumir el papel de gestor de esa solucion hasta que se resuelva"),
        ("L117 a L117", 117, 117, 0, "P29 parte 3 de 5: volver al subordinado con una solucion que atienda sus razones reales"),
        ("L119 a L119", 119, 119, 0, "P30 parte 4 de 5: hacerlo sentirse comodo con el nuevo arreglo, aclarando que no fue un chantaje"),
        ("L121 a L121", 121, 121, 1, "P31 parte 5 de 5 y CIERRE DE LA PIEZA que empezo en P27 (L113): si ya acepto otro empleo, hacerle ver que su compromiso con los companeros con quienes trabaja a diario pesa mas que uno con un conocido nuevo, y conseguir que rechace la otra oferta; P27, P28, P29, P30 y esta fila son la misma pieza, inventario propio del libro de pasos, manual 9.1, nodo propio"),
        ("L123 a L123", 123, 123, 0, "P32 cierre del capitulo, lo que esta en juego es el bien de la empresa y la moral de otros empleados destacados: POSTURA de cierre"),
    ],
    "cap_16": [
        ("L9 a L9", 9, 9, 0, "P1  rotulo: el numero 15, sin cuerpo que extraer"),
        ("L11 a L11", 11, 11, 0, "P2  titulo textual Compensation as Task-Relevant Feedback, sin cuerpo que extraer"),
        ("L13 a L13", 13, 13, 0, "P3  el dinero en los distintos niveles de la jerarquia de Maslow, remite a la prueba sencilla ya descrita en el capitulo 11: POSTURA que reusa un nodo previo del propio libro, sin cuerpo nuevo que procedimentar"),
        ("L15 a L15", 15, 15, 0, "P4  la utilidad marginal decreciente del dinero segun el nivel de compensacion y la sensibilidad del supervisor ante necesidades distintas: POSTURA"),
        ("L17 a L17", 17, 17, 0, "P5  el proposito de usar el dinero como feedback relevante a la tarea, dificultado porque el mando intermedio no se paga por pieza: DEFINICION de transicion"),
        ("L19 a L19", 19, 19, 0, "P6  el bono de desempeno como porcentaje creciente segun el nivel de compensacion, 50 por ciento en la alta direccion y 10 a 25 por ciento en mandos intermedios: POSTURA prescriptiva del autor, no una cifra medida con fecha de corte, principios 5 y 8 no aplican por no ser medicion"),
        ("L21 a L21", 21, 21, 0, "P7  los asuntos a sopesar al diseñar un esquema de bono, planteados como preguntas abiertas y no como medios nombrados: POSTURA, 9.1 restriccion 2 por el criterio abierto de que sopesar"),
        ("L23 a L23", 23, 23, 0, "P8  el ejemplo de un esquema de bono de tres factores: CASO ilustrativo explicito, ningun esquema da exactamente lo que se busca, manual 3.5, EXCLUIDO como nodo propio"),
        ("L25 a L25", 25, 25, 0, "P9  las dos formas puras de administrar el salario base, por antiguedad y por merito: DEFINICION"),
        ("L27 a L27", 27, 27, 0, "P10 la mayoria de empresas usa un compromiso entre las dos formas puras: DEFINICION de transicion"),
        ("L29 a L29", 29, 29, 0, "P11 el salario por antiguedad pura en grandes empresas japonesas, sindicatos y docentes: DEFINICION con CASO, manual 3.5"),
        ("L31 a L31", 31, 31, 0, "P12 el salario por merito puro es impractico, es dificil ignorar la experiencia: POSTURA"),
        ("L33 a L33", 33, 33, 0, "P13 la facilidad de administrar el esquema por antiguedad frente al esfuerzo del esquema por merito: POSTURA"),
        ("L35 a L35", 35, 35, 0, "P14 el merito exige comparacion competitiva entre personas, con la analogia deportiva: POSTURA"),
        ("L37 a L37", 37, 37, 0, "P15 los ascensos comunican el sistema de valores a la organizacion y deben basarse en desempeno: DEFINICION"),
        ("L39 a L39", 39, 39, 0, "P16 referencia al Principio de Peter, un ascenso continuo hasta el nivel de incompetencia: DEFINICION, concepto de otro autor y no inventario propio del libro"),
        ("L41 a L41", 41, 41, 0, "P17 la ilustracion que sigue a alguien por sus ascensos entre el punto A y el punto B: DEFINICION que remite a una figura"),
        ("L43 a L43", 43, 43, 0, "P18 pie de figura, el que logra alterna entre cumple y supera los requisitos: sin cuerpo propio que transcribir"),
        ("L45 a L45", 45, 45, 0, "P19 la alternativa de no ofrecer mas reto en el punto B atrofia el desempeno: POSTURA"),
        ("L47 a L47", 47, 47, 0, "P20 los dos tipos de desempeno que cumple los requisitos, el que no compite y el que compite: DEFINICION"),
        ("L49 a L49", 49, 49, 1, "P21 la solucion de reciclar al ascendido mas alla de su capacidad, en cuatro pasos dentro del mismo parrafo: la direccion reconoce su propio error de juicio en vez de forzar la salida del empleado, lo coloca de vuelta en un puesto que sepa desempeñar, lo apoya frente a la vergüenza, y hace el reciclaje abiertamente; inventario propio del libro de pasos, manual 9.1, nodo propio"),
        ("L51 a L51", 51, 51, 0, "P22 cierre del capitulo, la responsabilidad de dar calificaciones honestas y compensacion basada en merito: POSTURA de cierre"),
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
print("NODOS QUE MI FRONTERA DA EN LAS TRES UNIDADES DE HOY (cap_14+cap_15+cap_16): %d" % total_nodos)
print("  cap_14: %d   cap_15: %d   cap_16: %d"
      % (nodos_por_unidad["cap_14"], nodos_por_unidad["cap_15"], nodos_por_unidad["cap_16"]))
print("TECHO DE CANDIDATOS DE D.58 EN REGIMEN LIGERO                  : %d" % TOPE)
print("DENTRO DEL TECHO DE CANDIDATOS                                 : %s"
      % ("SI" if total_nodos <= TOPE else "NO"))
