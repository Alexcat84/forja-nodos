# -*- coding: utf-8 -*-
"""LOS SEIS PRIMEROS CANDIDATOS DE cap_13, ESCRITOS CONTRA SU LINEA (D.30)."""
import io
import json
import os

CARPETA = 'cuarentena/scott_radical_candor'
FUENTE = [{"clave": "scott_radical_candor", "fecha": "2026-09-13"}]
ORIGEN = ("UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_13.md, unidad Afterword, titulo "
          "textual Afterword to the Revised Edition: Rolling Out Radical Candor. ")


def escribe(d):
    ruta = os.path.join(CARPETA, d['id'] + '.json')
    with io.open(ruta, 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(d, ensure_ascii=False, indent=2, sort_keys=True))
        f.write(u'\n')
    return ruta


def nodo(ident, titulo, largo, otros, cond, entregable, pasos, resumen):
    return {
        "id": ident, "titulo": titulo, "dominio": "gestion_equipos", "estado": "vivo",
        "fuentes": FUENTE, "ids_alias": [], "nodos_previos": [], "nodos_siguientes": [],
        "denominaciones": {"nombre_largo": largo, "sigla": "",
                           "otros_idiomas": [{"idioma": "ingles", "termino": t} for t in otros]},
        "condiciones_activacion": cond, "entregable_esperado": entregable,
        "pasos_accionables": pasos, "resumen_teorico": ORIGEN + resumen,
    }


NODOS = []

NODOS.append(nodo(
    "mejorar_consciencia_propia_relacional_dos_practicas",
    ("Mejorar tu consciencia de ti mismo y tu consciencia de la relacion con las dos practicas que "
     "el texto desarrolla, porque en la franqueza radical el hilo comun siempre eres tu"),
    ("La cabeza de las dos practicas del epilogo: contar historias y los juegos de papeles, con las "
     "dos consciencias que mejoran"),
    ["YOU", "Improve using role plays and storytelling", "self-awareness", "relational awareness"],
    ("Cuando quieres practicar la franqueza radical y te das cuenta de que el hilo comun de todas "
     "las veces eres tu, y no sabes que hacer exactamente con eso."),
    ("Las dos consciencias distinguidas por su nombre y las dos practicas del texto elegidas y "
     "puestas en marcha, con tu impacto sobre los demas alineado con tus intenciones."),
    [
        "Parte del consejo del capitulo cinco que el texto trae aqui: mantente centrado, porque no puedes preocuparte por los demas si no cuidas de ti.",
        "Y parte de lo que el texto dice que es el hilo comun de todas las veces que se practica la franqueza radical: tu.",
        "Distingue las dos consciencias, porque el texto dice que de la primera se ha escrito mucho y de la segunda poco: la consciencia de ti mismo es la capacidad de reconocer tus propias fuerzas y tus propias debilidades.",
        "La consciencia de la relacion es el impacto que estas teniendo en los demas.",
        "Cuenta con lo que el texto avisa sobre por que no basta la primera: puedes tener toda la intencion de ser amable y util, pensar y sentir todo lo correcto, ser plenamente consciente de tus propios defectos, y aun asi decir algo destructivo de maneras que no podias predecir o de las que no eras consciente. O no soportar verlo y elegir no verlo.",
        "Cuenta tambien con lo que la consciencia de la relacion NO significa, porque el texto lo dice expresamente: no significa que lo que tengas que decir no moleste nunca al otro.",
        "Lo que si significa, y es lo que tienes que aprender: ver cuando has disgustado a alguien, y demostrar que te importa incluso cuando lo que tienes que decir sea duro de oir.",
        "Significa ademas que puedes y quieres ver el impacto que estas teniendo en el otro a corto y a largo plazo, y ajustar para que ese impacto sea positivo y no negativo.",
        "Y usa esa consciencia para bien, no solo para manipular al otro, que es la pregunta con la que el texto abre esta seccion.",
        "Cuenta con que las dos se pueden mejorar, y usa para ello las DOS practicas que el texto dice haber desarrollado: contar historias y los juegos de papeles.",
        "Haz la primera, contar historias, que el texto despliega bajo el rotulo cual es tu historia.",
        "Haz la segunda, el juego de papeles, que el texto despliega bajo el rotulo el triangulo de la critica.",
        "Y cuenta con lo que el texto dice de las dos: las han probado con gente de papeles y de centros de trabajo muy distintos por todo el mundo, y funcionaron bien en industrias y culturas diferentes.",
    ],
    ("Sale de las lineas 17 a 22 y 35 a 40. ES LA PIEZA 1 DE LA FRONTERA DE cap_13, que cierra en 12 "
     "piezas con su instrumento en .t1_v23/frontera_cap13.py. ES UNA SERIE D.37 Y LA CUENTA ESTA "
     "ESCRITA: la linea 39 dice We have developed TWO practices, storytelling and role plays, o sea "
     "que dice CUANTAS partes tiene Y LAS NOMBRA, que es la condicion literal de D.37. Las dos "
     "partes existen como candidato (contar_cuatro_historias_propias_ver_hueco_intencion y "
     "practicar_triangulo_critica_tres_papeles) y las dos aristas van declaradas en el reporte de la "
     "vuelta 23 con su paso citado, sin esperar a que ninguna senial las levante. POR QUE ES "
     "PROCEDIMIENTO Y NO UNA DEFINICION, con D.27 delante y sabiendo que es el caso en que mas facil "
     "seria equivocarse, porque las lineas 35 y 37 definen dos terminos: el libro no se queda en "
     "definir, pone su propio INVENTARIO DE MEDIOS (dos practicas nombradas y desarrolladas) y su "
     "inventario de OBJETOS A REVISAR (ver cuando has disgustado a alguien, ver el impacto a corto y "
     "a largo plazo, ajustar para que sea positivo). Distinguir las dos consciencias y elegir la "
     "practica deja fichero. EL CASO DEL CAPITALISTA DE RIESGO Y SU ASOCIADO (lineas 23 a 33) NO "
     "VIAJA A NINGUN PASO: es manual 3.5, y su doctrina (que un problema de arrogancia no es un "
     "problema de comunicacion, y que hace falta humildad antes de ver el impacto que tienes en los "
     "demas) esta escrita aparte en las lineas 35 y 37, que son las que viajan. RELECTURA DE "
     "FIDELIDAD D.30 EN EL ACTO, paso a paso contra su linea: 13 pasos, 13 TRANSCRIPCION, 0 PUENTE. "
     "P1 y P2 de la linea 21; P3 a P5 de la linea 35; P6 a P9 de la linea 37; P10 a P13 de la linea "
     "39. LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: cada cuanto se repiten las dos practicas, "
     "en que orden se hacen si no hay tiempo para las dos, y como se mide que tu consciencia de la "
     "relacion ha mejorado. El libro pone las practicas y no pone ninguna de las tres.")))

NODOS.append(nodo(
    "contar_cuatro_historias_propias_ver_hueco_intencion",
    ("Contar tus cuatro historias propias del marco de la franqueza radical para ver el hueco entre "
     "lo que pretendes y el impacto que tienes, y compartirlas con tu equipo"),
    ("Cual es tu historia: el ejercicio de taller de las cuatro historias, la de franqueza radical "
     "mas las tres de las otras tres casillas del marco"),
    ["Practice: What's your story?", "Radical Candor story", "Obnoxious Aggression",
     "Ruinous Empathy", "Manipulative Insincerity"],
    ("Cuando quieres desarrollar tu consciencia de ti mismo y tu consciencia de la relacion, y vas a "
     "hacer la primera de las dos practicas que el texto desarrolla."),
    ("Tus cuatro historias desenterradas y contadas a tu equipo, con el hueco entre tus intenciones "
     "y tu impacto puesto a la vista."),
    [
        "Parte de por que funciona, que es lo que el texto pone antes del ejercicio: contar historias es una gran manera de desarrollar a la vez la consciencia de ti mismo y la consciencia de la relacion.",
        "Piensa primero en tu historia de franqueza radical: acuerdate de alguna vez en que la estabas liando, alguien te lo dijo, y aunque lo que te dijo escociera un poco en el momento, te ayudo a la larga.",
        "Cuentala a tu equipo con lo que significa para ti, porque el texto dice que sera mil veces mas poderosa que la historia de la autora sobre cuando su jefa le dijo que decia um cada tres palabras en una presentacion.",
        "Cuenta con las dos cosas que haces a la vez al mostrar algo de vulnerabilidad contandola: una, demuestras consciencia de ti mismo y humildad; dos, ensenias que de verdad agradeces la critica. Eso hara mas facil que pidas critica, y cuanta mas pidas mas consciente de ti mismo te vuelves.",
        "Cuenta con para que sirven las otras tres, que el texto agrupa: tu historia de agresion odiosa, tu historia de insinceridad manipuladora y tu historia de empatia ruinosa te ayudaran a ti y a tu equipo a ver cuando te has caido de la meta de ser amable, o sea que trabajan la consciencia de la relacion.",
        "Piensa en tu historia de agresion odiosa: hubo alguna vez en que ofreciste una critica solo por ayudar y el otro te vivio como odiosamente agresivo? O una vez en que estabas dando una critica pero estabas muy enfadado y quiza tus intenciones no eran tan puras?",
        "Cava hondo ahi, que es lo que el texto pide: cual es el momento del que te encoges al mirar atras, preguntandote como pudiste comportarte de forma tan odiosa.",
        "Cuenta la tuya y no la del libro, y el texto da la razon: tu historia es por definicion mejor que la del correo grosero sobre los sitios desordenados que la autora mando al jefe de su jefe, porque es tuya.",
        "Cuenta con lo que esa historia consigue: te ayuda a entender el impacto que tienes en los demas, y ayuda a tu equipo a entenderte y a saber como hablarte para que puedan ensenarte cuando te estas portando como un cretino sin querer.",
        "Piensa despues en tu historia de empatia ruinosa: cuando dejaste de dar una critica solo por ser amable, y acabaste viendo sufrir a la persona por no haber corregido una mala conducta?",
        "No cuentes la historia de Bob del capitulo dos: cuenta la tuya, la vez en que intentabas ser amable y te diste cuenta de que habias sido cruel sin querer.",
        "Cuenta con lo que el texto dice que construye eso: el arrepentimiento que sientes al recordar el episodio y la vulnerabilidad que ensenias al contarlo levantan tu consciencia de la relacion.",
        "Y piensa por ultimo, y el texto avisa de que es la mas dificil de todas, en tu historia de insinceridad manipuladora: cuando no le dijiste a una persona un problema directamente y en cambio se lo contaste a otros? O le dijiste que su trabajo era bueno mientras lo socavabas por la espalda?",
        "Cuenta con que cuesta, que es lo que el texto reconoce: es muy dificil verse a uno mismo como alguien que apunialla por la espalda, pasivo agresivo o politico, y todos somos culpables de esas conductas de vez en cuando.",
        "Desempaqueta tus historias y compartelas con tu equipo, porque el texto dice que ahi es cuando la gente empieza a darse cuenta del hueco entre sus intenciones y el impacto que esta teniendo en los demas.",
        "Y cuenta con lo que el texto pone como remate: la consciencia es el primer paso hacia el cambio, y puedes hacer que tu impacto encaje con tus intenciones.",
        "Cuenta tambien con el limite que el texto pone justo despues: cada persona es distinta, asi que lo que a una le resulta util a otra puede resultarle insoportablemente doloroso. Tienes que ajustar como hablas para ser claro y amable con el otro sin sentirte un camaleon.",
    ],
    ("Sale de las lineas 41 a 58, bajo el rotulo Practice: What's your story? de la linea 41. ES LA "
     "PIEZA 2 DE LA FRONTERA DE cap_13. POR QUE ES PROCEDIMIENTO Y NO POSTURA, con D.27 delante y en "
     "uno de sus casos faciles: el libro pone su propio INVENTARIO DE OBJETOS DE TRABAJO, CUATRO "
     "historias nombradas una a una con su pregunta de arranque escrita (la de franqueza radical en "
     "la linea 45, la de agresion odiosa en la 49, la de empatia ruinosa en la 51 y la de "
     "insinceridad manipuladora en la 53), y ademas dice que es un ejercicio que hacen en sus "
     "talleres. Deja fichero: las cuatro historias escritas y contadas. ES PARTE DE LA SERIE D.37 "
     "que encabeza mejorar_consciencia_propia_relacional_dos_practicas, y la arista va declarada en "
     "el reporte de la vuelta 23. LA CUENTA DE CUATRO NO SE LA ATRIBUYO AL LIBRO A CIEGAS: el libro "
     "escribe THE NEXT THREE STORIES en la linea 47 y nombra la cuarta aparte en la 45, asi que el "
     "cuatro es la suma de una cuenta escrita mas una historia nombrada, y lo digo aqui en vez de "
     "dejarlo pasar. SU PAR CON contar_historias_propias_explicar_franqueza_radical (cap_12), Y LO "
     "DECLARO YO ANTES DE QUE LO LEVANTE NINGUNA SENIAL PORQUE EL PROPIO LIBRO LO DECLARA: la linea "
     "43 escribe There's a brief paragraph about this in the final Getting Started section, but we "
     "have been asked for more detail about how to do this and why it works. MI VEREDICTO ES "
     "CONTINUA CON ARISTA Y NO REPITE, con los dos lados medidos: aquel entrega la franqueza radical "
     "EXPLICADA a tu equipo y trae sus seis medios de explicarla (el libro, los videos, tus "
     "palabras, la historia del um, la de Bob, la vulnerabilidad); este entrega CUATRO historias "
     "desenterradas con su pregunta de arranque y las dos consciencias trabajadas, y ninguna de las "
     "cuatro esta en aquel. El acto compartido es uno solo, contar tu historia, y los dos lados "
     "tienen procedimiento fuera de el. LAS HISTORIAS DEL LIBRO VIAJAN COMO CONTRAEJEMPLO Y NO COMO "
     "CONTENIDO, que es manual 3.5: el texto dice expresamente que NO cuentes la del um, la del "
     "correo de los sitios desordenados ni la de Bob, sino la tuya. RELECTURA DE FIDELIDAD D.30 EN "
     "EL ACTO, paso a paso contra su linea: 17 pasos, 17 TRANSCRIPCION, 0 PUENTE. P1 de la linea 43; "
     "P2 a P4 de la linea 45; P5 de la linea 47; P6 a P9 de la linea 49; P10 a P12 de la linea 51; "
     "P13 y P14 de la linea 53; P15 y P16 de la linea 55; P17 de la linea 57. LO QUE EL TEXTO NO "
     "DICE Y POR ESO NO ESTA AQUI: en que reunion se comparten, en que orden se cuentan las cuatro, "
     "cuanto dura el ejercicio, y que se hace si alguien no encuentra una de las cuatro. El libro "
     "pone las cuatro historias y no pone ninguna de esas respuestas.")))

NODOS.append(nodo(
    "practicar_triangulo_critica_tres_papeles",
    ("Practicar el triangulo de la critica en grupos de tres para ver el impacto real de tus "
     "palabras, con quien da, quien recibe y quien observa"),
    ("El triangulo de la critica: la version de juego de papeles de los autores, con sus tres "
     "papeles y el marco de dos por dos como cuaderno del observador"),
    ["Practice: The Feedback Triangle", "role play"],
    ("Cuando quieres ver el impacto que tus palabras tienen en el otro y elegir palabras mas amables "
     "y mas claras, y vas a hacer la segunda de las dos practicas que el texto desarrolla."),
    ("La conversacion ensayada en grupo de tres, con el recorrido del que da la critica dibujado "
     "sobre el marco de la franqueza radical por el observador, y el impacto real de sus palabras "
     "devuelto por quien la recibio."),
    [
        "Junta un grupo de tres.",
        "Describe una critica que sabes que deberias haber dado a alguien y no diste.",
        "Pon a un companiero a hacer de destinatario de esa critica.",
        "Pidele que exagere la respuesta defensiva, porque el texto dice que asi la experiencia es mas eficaz.",
        "Cuenta con la razon que el texto da de esa exageracion, que parece contradictoria y no lo es: animar a quien recibe la critica a ponerse dificil le lleva a acordarse de malos momentos de critica que ha vivido de verdad en su propia carrera, asi que ser dramatico produce paradojicamente interpretaciones que se sienten mas reales. Y ademas deja que quien da la critica practique los momentos mas duros.",
        "Pon al otro companiero a hacer de observador, y que siga como va la conversacion usando el marco de la franqueza radical.",
        "Ten delante los desplomes de conversacion que el texto dice ver todo el tiempo, porque son lo que el observador tiene que cazar: que quien da la critica empiece en franqueza radical y se retire a toda prisa a la empatia ruinosa cuando quien la recibe parece disgustado o incluso llora.",
        "O que empiece con intencion de ser radicalmente franco pero lo diga con tanta suavidad que acabe siendo ruinosamente empatico.",
        "O que, frustrado porque quien recibe la critica no se entera, se vuelva odiosamente agresivo.",
        "O que empiece radicalmente franco, quien recibe la critica se enfade y conteste con grosería, y entonces quien la da se enfade tambien y se vuelva seriamente odioso y agresivo.",
        "Dibuja esos recorridos sobre el marco de dos por dos de la franqueza radical, porque el texto dice que eso ofrece una especie de brujula que deja a los participantes con sensacion de poder hacer algo.",
        "Cuenta con lo que esa brujula consigue: cuando se paran un momento a ver el impacto que tienen en los demas, pueden usar esa informacion para devolver la conversacion al carril, en vez de quedarse solo a la defensiva o culpables. La consciencia de uno mismo no tiene por que ser flagelarse.",
        "Haz que el observador objetivo y tambien quien recibio la critica ayuden a su companiero ensenandole como aterrizo la critica: quiza demasiado agresiva, quiza no lo bastante clara.",
        "Cuenta con lo que eso mejora: la consciencia de la relacion de todos los participantes, que llegan a ver por los ojos del observador y por los de quien recibio la critica cual fue el impacto de sus palabras, al margen de su intencion.",
        "Y cuenta con la razon de fondo por la que el texto manda practicar: cuando aprendemos casi cualquier habilidad, matematicas, ventas, ingenieria, piano o deporte, practicamos para mejorar, pero en comunicacion no solemos tener esta clase de practica.",
    ],
    ("Sale de las lineas 59 a 72, bajo el rotulo Practice: The Feedback Triangle de la linea 59. ES "
     "LA PIEZA 3 DE LA FRONTERA DE cap_13. POR QUE ES PROCEDIMIENTO Y NO POSTURA, con D.27 delante y "
     "en su caso mas facil: el libro escribe Here's how it works y pone su propio INVENTARIO DE "
     "ETAPAS Y DE PAPELES, nombrados uno a uno (el grupo de tres, quien describe la critica, quien "
     "hace de destinatario, quien hace de observador, el marco como cuaderno), mas los cuatro "
     "desplomes que hay que cazar. Deja fichero: el recorrido dibujado sobre el marco. ES PARTE DE "
     "LA SERIE D.37 que encabeza mejorar_consciencia_propia_relacional_dos_practicas, y la arista va "
     "declarada en el reporte de la vuelta 23. EL TRES DEL ID NO ES UNA CUENTA QUE LE ATRIBUYA YO AL "
     "LIBRO: la linea 63 escribe Get together in a group of three, y los tres papeles estan "
     "nombrados uno a uno en las lineas 63, 65 y 69. RELECTURA DE FIDELIDAD D.30 EN EL ACTO, paso a "
     "paso contra su linea: 15 pasos, 15 TRANSCRIPCION, 0 PUENTE. P1 a P5 de la linea 63; P6 a P10 "
     "de la linea 65; P11 y P12 de la linea 67; P13 y P14 de la linea 69; P15 de la linea 71. "
     "LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: cuanto dura el ejercicio, cuantas rondas se "
     "hacen, si los tres rotan de papel, y que se hace con lo aprendido despues. El libro pone los "
     "papeles y las etapas y no pone ninguna de las cuatro.")))

NODOS.append(nodo(
    "pedir_critica_primero_crear_seguridad_psicologica",
    ("Pedir critica tu antes que nada, que es el primer paso del orden de operaciones, porque es lo "
     "que mas deprisa crea la seguridad psicologica del equipo"),
    ("El orden de operaciones de la franqueza radical, sus cinco pasos numerados, y la razon medida "
     "de por que pedir critica va el primero"),
    ["SOLICIT CRITICISM FIRST", "order of operations", "psychological safety"],
    ("Cuando vas a empezar a practicar la franqueza radical con tu equipo y tienes que decidir por "
     "que punto empiezas."),
    ("El orden de operaciones recorrido desde su primer paso, con la critica pedida por ti y "
     "respondida bien, que es lo que el texto dice que crea antes que nada la seguridad "
     "psicologica."),
    [
        "Ten delante el orden de operaciones que el texto llama importante, con sus cinco pasos numerados: uno, pide critica.",
        "Dos, da elogio.",
        "Tres, da critica.",
        "Cuatro, mide la critica y ajusta.",
        "Cinco, fomenta el elogio y la critica entre los demas.",
        "Empieza por el primero y no por otro, y el texto explica por que hace falta decirlo: como las dos historias mas repetidas del libro eran las de una jefa dando critica, muchos lectores se quedaron con la impresion de que la franqueza radical va sobre todo de jefes criticando a empleados, y nada podria estar mas lejos de la verdad.",
        "Cuenta con cual es la meta de pedir critica, que el texto pone doble: no solo ayudarte a ser mas consciente de ti mismo, sino crear un ambiente en el que todos los empleados sientan bastante seguridad psicologica como para darse critica radicalmente franca entre ellos.",
        "Ten delante la definicion de la que el texto parte, la de Amy Edmondson de la escuela de negocios de Harvard: la seguridad psicologica es una creencia compartida de que el equipo es seguro para asumir riesgos interpersonales.",
        "Y cuenta con lo que su investigacion ensenia: en los centros de trabajo psicologicamente seguros la gente sabe que puede recibir critica de desempenio que diga que no esta cumpliendo las expectativas, y aun asi se siente dispuesta y capaz de asumir los riesgos interpersonales que la franqueza trae.",
        "Cuenta con la afirmacion que el texto hace de ahi, que es la que ordena el paso: no hay nada que un lider pueda hacer que cree mas deprisa las condiciones de la seguridad psicologica que pedir critica el mismo y responder bien a ella.",
        "Y ten delante por que la seguridad psicologica importa tanto en el trabajo, con la medicion que el texto cita: un grupo de operaciones de personas de Google hizo durante dos anios mas de doscientas entrevistas, analizando mas de doscientos cincuenta atributos de mas de ciento ochenta equipos activos.",
        "Cuenta con lo que encontraron: quien estaba en el equipo importaba menos que como interactuaban entre ellos, como estructuraban su trabajo y como veian sus contribuciones.",
        "Y con las cinco dinamicas clave de los equipos con exito que nombraron: seguridad psicologica, fiabilidad, estructura y claridad, sentido, e impacto. La seguridad psicologica era con mucho la mas importante de las cinco, porque es el cimiento de las otras cuatro.",
        "Haz las tres cosas que el texto dice que arrancan el circulo virtuoso: pide critica, responde a ella de forma constructiva, y premiala. Eso empieza a normalizar la critica como una fuerza positiva.",
        "Cuenta con lo que eso desencadena hacia abajo: cuando quien manda pide critica y premia a quien se la da, manda una senial a los jefes intermedios de que deberian hacer lo mismo, y segun la gente de todos los niveles se da cuenta de que dar critica honesta es seguro e incluso se fomenta, se produce un circulo virtuoso.",
        "Y con lo que ese circulo produce: equipos que funcionan a un nivel notablemente alto, porque la gente innova mas cuando tiene menos miedo a asumir riesgos y aprende de los errores en vez de esconderlos y repetirlos.",
        "Y cuando ya tengas claro por que pruebas que aguantas antes de repartir, pasa a los cuatro elementos con los que el texto despliega como se pide critica: dar con una pregunta recurrente, abrazar la incomodidad, escuchar con intencion de entender, y hacer tangible la escucha premiando la franqueza.",
    ],
    ("Sale de las lineas 73 a 86, 105 a 110 y 113 a 114, bajo el rotulo SOLICIT CRITICISM FIRST de la "
     "linea 73. ES LA PIEZA 4 DE LA FRONTERA DE cap_13. POR QUE ES PROCEDIMIENTO Y NO POSTURA, con "
     "D.27 delante: el libro pone su propio INVENTARIO DE ETAPAS, cinco pasos NUMERADOS por el "
     "propio texto en las lineas 77 a 85, y ademas pone el inventario de los cuatro elementos del "
     "primero en la linea 113. SU PAR CON empezar_cultura_franqueza_radical (cap_05), Y LO DECLARO "
     "YO ANTES DE QUE LO LEVANTE NINGUNA SENIAL PORQUE EL PROPIO LIBRO LO DECLARA: la linea 87 "
     "escribe The first edition describes this order of operations. MI VEREDICTO ES CONTINUA CON "
     "ARISTA Y NO REPITE, con los dos lados medidos: aquel sale de cap_05, tiene el orden en prosa "
     "(pide antes de dar, elogia antes de criticar, entiende la frontera peligrosa) y NO tiene ni la "
     "numeracion, ni los pasos cuatro y cinco, ni una sola razon medida; este trae la lista numerada "
     "entera, la definicion de Edmondson, la medicion de Google con sus cinco dinamicas y el circulo "
     "virtuoso. VA MARCADO COMO DISCUTIBLE EN EL REPORTE, porque es donde mas cerca estoy de un "
     "REPITE en todo el capitulo. Y ES UNA SERIE D.29 Y NO D.37: el texto NUMERA los cinco pasos "
     "pero NO escribe la palabra cinco, y D.37 pide que el texto diga CUANTAS partes tiene. Por eso "
     "ni el id ni el titulo llevan la cifra y las aristas a los cinco pasos van con razon escrita. "
     "LA HISTORIA DE KIM Y SU HIJA (lineas 87 a 103) NO VIAJA A NINGUN PASO: es manual 3.5, el "
     "ejemplar de pedir critica, y el propio texto dice que la escribe porque al libro le faltaba "
     "una historia memorable de un jefe pidiendo critica. Su doctrina (escuchar con intencion de "
     "entender, pedir aclaracion en vez de responder a la defensiva) viaja en la pieza 8, que es "
     "donde el libro la desarrolla. EL HABITO REGULAR DE LA LINEA 111 NO VIAJA AQUI Y DIGO DONDE VA: "
     "a integrar_peticion_critica_rutina_existente, que es la pieza 10, porque es el mismo objeto "
     "que la linea 239 y P.19 manda fundirlo en un solo procedimiento en vez de mandarlo a nodo "
     "propio. RELECTURA DE FIDELIDAD D.30 EN EL ACTO, paso a paso contra su linea: 17 pasos, 17 "
     "TRANSCRIPCION, 0 PUENTE. P1 a P5 de las lineas 75 a 85; P6 de la linea 89; P7 a P10 de la "
     "linea 105; P11 a P13 de la linea 107; P14 a P16 de la linea 109; P17 de la linea 113. LAS "
     "CIFRAS DE LA LINEA 107 SON DEL LIBRO Y LAS COMPROBE UNA A UNA: dos anios, mas de doscientas "
     "entrevistas, mas de doscientos cincuenta atributos, mas de ciento ochenta equipos y cinco "
     "dinamicas. LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: cuanto se tarda en pasar del paso "
     "uno al dos, quien decide que el equipo ya tiene seguridad psicologica, y como se mide. El "
     "libro pone el orden y la razon y no pone ninguna de las tres.")))

NODOS.append(nodo(
    "elegir_pregunta_recurrente_pedir_critica",
    ("Elegir tus preguntas recurrentes para pedir critica, con los cuatro atributos que el texto da "
     "y la prueba de campo con un companiero de confianza"),
    ("La pregunta recurrente que de verdad te imaginas haciendo: sus cuatro atributos, las preguntas "
     "de ejemplo de los talleres y su ensayo"),
    ["A GO-TO QUESTION YOU CAN ACTUALLY IMAGINE ASKING", "go-to question"],
    ("Cuando vas a pedir critica a tu equipo y no sabes que pregunta hacer, o la que haces no saca "
     "nada."),
    ("Tres o cuatro preguntas recurrentes tuyas escritas y probadas con un companiero de confianza, "
     "evaluadas por si sacaron critica util y por si sonaron naturales."),
    [
        "Parte de la pregunta que el texto descarta y de por que: si preguntas tienes alguna critica para mi, la respuesta sera casi seguro que no, todo va bien.",
        "Pide la critica de una forma que sea autentica y que ademas tenga en cuenta las necesidades del otro, que es lo que el texto pide para sacar una respuesta con sustancia.",
        "No busques la pregunta correcta, porque el texto dice que no existe: dadas las permutaciones y combinaciones infinitas posibles en la ecuacion de tu y ellos, no hay una sola pregunta correcta.",
        "Ten tres o cuatro preguntas recurrentes, que es lo que el texto dice que a muchos participantes de sus talleres les resulta util, para poder adaptarte a distintas personas de tu equipo y a distintas situaciones.",
        "Comprueba el primer atributo, que sea sincera: la gente tiene detectores de tonteria bien afinados, y si suenas a que estas repitiendo como un loro algo que leiste en un libro, aunque sea un gran libro, no vas a sonar sincero.",
        "Comprueba el segundo, que no se pueda contestar con un si o un no: el texto avisa con el ejemplar de preguntarle a un crio que tal el dia, que saca poco mas que un si o un no, frente a cuentame lo mejor y lo peor de tu dia, que saca mas.",
        "Corrige por eso la pregunta que la primera edicion recomendaba, que es una correccion que el propio texto hace: preguntar hay algo que pudiera hacer o dejar de hacer que te facilitara trabajar conmigo le da una salida facil a quien teme el conflicto, que puede decir simplemente que no, y esa es justo la gente a la que hay que animar. Pregunta en cambio que podria hacer o dejar de hacer.",
        "Y si no se les ocurre nada, animales a pensar un poco mas, avisales de que se lo vas a volver a preguntar la semana que viene, y no te olvides de volver a preguntar.",
        "Comprueba el tercero, si la quieres concreta o abierta: hay gente que se siente segura contestando una pregunta abierta, y para quien no, una pregunta concreta puede funcionar mejor.",
        "Ten delante el ejemplar de pregunta concreta que el texto escribe: me preocupa que a veces interrumpa a la gente antes de que haya podido expresarse del todo. Cuando me has visto hacerlo? Me lo seniallaras si me ves hacerlo la semana que viene?",
        "Cuenta con que tampoco aqui hay una talla unica, asi que mira que saca critica y que saca silencio. Y que el silencio no te eche para atras: sigue intentandolo hasta que saques algo.",
        "Comprueba el cuarto, la frecuencia: si solo pides critica una vez cada seis meses, en las respuestas tendras un sesgo de lo reciente, porque te contaran algo de hace una semana habiendose olvidado de algo mucho mas importante de hace tres meses, y ademas puede que ya sea tarde para arreglar aquello.",
        "Pide critica a menudo, porque el texto dice que eso sube la probabilidad de que la critica sea accionable, y ademas construye fondo de aguante: si solo sales a correr una vez cada seis meses cada carrera duele mucho, y si lo haces a diario la echas de menos cuando no vas.",
        "Ten delante las preguntas que el texto recoge de participantes de sus talleres, y fijate en que el tono varia mucho de persona a persona: en la ultima semana, cuando habrias preferido que me metiera mas o menos en tu trabajo?",
        "Dime por que estoy equivocado aqui.",
        "Que podria haber hecho distinto esta semana para hacerte mas facil tu trabajo?",
        "Como podria apoyar mejor tu desarrollo profesional ahora mismo?",
        "Que he hecho en la ultima semana que haya hecho dificil trabajar conmigo?",
        "Cual es un punto ciego mio que hayas notado?",
        "Lo mas importante que puedes hacer por los dos es decirme cuando la he liado.",
        "Siento que no lo hice todo lo bien que podia en esa reunion, pero no estoy seguro de que hice mal. Puedes ayudarme a averiguarlo?",
        "De verdad estoy intentando hacer mejor esto. Se que en teoria es un problema, pero no siempre soy consciente en el momento. Puedes ayudarme seniallandomelo cuando lo veas?",
        "Y prueba las tuyas antes de soltarlas en tu equipo, que es el ejercicio que el texto pone: piensa unas cuantas preguntas recurrentes, ve a un companiero de confianza y hazle una o dos.",
        "Evalua a partir de sus respuestas dos cosas: si produjo critica util, y si sono natural, es decir, como algo que de verdad dirias tu.",
    ],
    ("Sale de las lineas 115 a 120 y 129 a 166, bajo el rotulo A GO-TO QUESTION YOU CAN ACTUALLY "
     "IMAGINE ASKING de la linea 115. ES LA PIEZA 5 DE LA FRONTERA DE cap_13. POR QUE ES "
     "PROCEDIMIENTO Y NO POSTURA, con D.27 delante y en su caso mas facil: el libro escribe Here are "
     "some attributes of good go-to questions y pone su propio INVENTARIO, cuatro atributos "
     "nombrados uno a uno con su rotulo propio en las lineas 131 a 137 (Sincere; Don't ask questions "
     "that can be answered with a yes or a no; Specific vs open-ended; Frequency), mas NUEVE "
     "preguntas literales en las lineas 141 a 157 y un ejercicio de prueba en la 161. Escribir los "
     "pasos aqui es transcribir. EL NUEVE DE LAS PREGUNTAS ES MI CUENTA Y NO DEL LIBRO, que dice a "
     "few great questions, y por eso ni el id ni el titulo llevan cifra. LA HISTORIA DE JASON Y ANN "
     "(lineas 121 a 127) NO VIAJA A NINGUN PASO: es manual 3.5, y lo unico que deja de doctrina es "
     "su pregunta recurrente, que ya viaja literal en el paso 14 porque la linea 141 la repite fuera "
     "del caso. SU PAR CON exigir_critica_jefe_reticente Y CON pedir_critica_equipo_premiarla "
     "(cap_09), leido antes de que lo levante ninguna senial: aquellos entregan la critica arrancada "
     "a un equipo que no la da y la critica premiada; este entrega TRES O CUATRO PREGUNTAS ESCRITAS "
     "Y PROBADAS con sus cuatro atributos, que es un objeto que ninguno de los dos tiene. El acto "
     "compartido es pedir critica, y los tres tienen procedimiento fuera de el. Va marcado como "
     "discutible en el reporte. RELECTURA DE FIDELIDAD D.30 EN EL ACTO, paso a paso contra su linea: "
     "24 pasos, 24 TRANSCRIPCION, 0 PUENTE. P1 a P4 de la linea 119; P5 de la linea 131; P6 a P8 de "
     "la linea 133; P9 a P11 de la linea 135; P12 y P13 de la linea 137; P14 a P22 de las lineas 141 "
     "a 157, una por linea; P23 y P24 de las lineas 161 a 165. LO QUE EL TEXTO NO DICE Y POR ESO NO "
     "ESTA AQUI: cuantas preguntas son demasiadas, como se elige cual toca con cual persona, y que "
     "se hace con la pregunta que no saca nada dos veces seguidas. El libro pone los atributos y los "
     "ejemplares y no pone ninguna de las tres.")))

NODOS.append(nodo(
    "resolver_dudas_frecuentes_pedir_critica",
    ("Resolver las dudas frecuentes que aparecen al empezar a pedir critica, con la respuesta que el "
     "texto da a cada una"),
    ("Las preguntas frecuentes del epilogo sobre pedir critica: la pregunta que se queda rancia, la "
     "critica que no puedes arreglar, el jefe joven con gente mayor y el miedo a empezar"),
    ["FAQ"],
    ("Cuando ya estas pidiendo critica y te tropiezas con una de las dudas que el texto recoge de "
     "sus talleres."),
    ("Cada duda resuelta con la respuesta del texto y con la accion concreta que esa respuesta "
     "encarga."),
    [
        "Si tu pregunta recurrente se te esta quedando rancia y te preguntas si tienes que usar la misma cada semana, parte de lo que el texto dice en general: la consistencia, tanto en cuando pides critica como en la pregunta que usas, tiende a hacer que la gente se sienta mas comoda dandotela, porque forma parte de una rutina esperada.",
        "Pero introduce alguna variacion si quieres, y sobre todo si tu pregunta no esta sacando respuestas.",
        "Y no dejes que el hecho de no estar recibiendo buena critica sea una excusa para dejar de pedirla: si lo que haces no funciona prueba algo nuevo, y pregunta por que no funciona. Di, con tus palabras, se que no soy perfecto y que probablemente hago mil cosas mal cada dia. Por que no me lo dice nadie?",
        "Si la respuesta que recibes va de algo que no puedes arreglar, reconoce primero que no sabes como arreglarlo.",
        "Pregunta si pueden ayudarte a resolver el problema.",
        "Si ninguno de los dos tiene una solucion a mano, retate a ti mismo: es de verdad algo que no puedes arreglar?",
        "Di que vas a necesitar algo de tiempo para pensarlo y que volveras a ellos.",
        "Y si acabas sin saber como resolver el problema, explica por que no puedes resolverlo.",
        "Si eres un jefe nuevo trabajando con gente bastante mayor que tu y temes parecer debil pidiendo critica, haz lo que el texto llama una de las cosas mas eficaces que puedes hacer con cualquier persona a tu cargo, y especialmente con las mayores: pedirles que compartan su sabiduria y su experiencia.",
        "Cuenta con la razon que el texto da: es tentador para los empleados mayores despachar a los jefes jovenes como sabelotodos arrogantes. Demuestrales que se equivocan.",
        "Si lo que te para es el miedo a recibir critica, empieza por donde el texto dice que empieces, y parte de que eso es normal: nadie quiere de verdad oir criticas.",
        "Centrate en que solo puedes arreglar los problemas que conoces, y en que si la persona se preocupa lo bastante como para hacerte ver un problema quiza tambien te ayude a arreglarlo.",
        "Si tiendes al perfeccionismo, recuerdate que eres humano y que vas a cometer errores, y que de hecho asi es como se mejora.",
        "Y trabaja la mentalidad del todavia no que el texto toma de Carol Dweck: en un instituto de Chicago los alumnos que no aprobaban un curso recibian la nota todavia no, y eso es fantastico, porque con un suspenso piensas que no eres nada y no estas en ninguna parte, y con un todavia no entiendes que estas en una curva de aprendizaje, lo que te da un camino hacia el futuro.",
        "Cierra con lo que el texto pone de remate: puede que hayas tenido unas cuantas erratas en una presentacion importante, o que te hayas enrollado en una reunion y la gente sintiera que ocupabas demasiado aire. No significa que seas un desastre: significa que eres humano.",
    ],
    ("Sale de las lineas 167 a 186, bajo el rotulo FAQ de la linea 167. ES LA PIEZA 6 DE LA FRONTERA "
     "DE cap_13. POR QUE ES PROCEDIMIENTO Y NO UN CONJUNTO DE POSTURAS, con D.27 delante: el libro "
     "pone su propio INVENTARIO DE OBJETOS, cuatro dudas nombradas una a una y escritas como "
     "pregunta en las lineas 169, 173, 177 y 181, y cada respuesta trae actos encargados y no solo "
     "opinion (reconoce que no sabes arreglarlo, pregunta si pueden ayudarte, di que volveras, "
     "pideles que compartan su sabiduria). Deja fichero: la duda resuelta y el acto hecho. TIENE "
     "PRECEDENTE DE FORMA EN ESTA MISMA BANDEJA: resolver_dudas_frecuentes_reuniones_salto_nivel "
     "sale de cap_09 con la misma figura, un bloque de preguntas frecuentes que el libro contesta "
     "una a una, y esta casa ya lo trato como nodo. SU PAR CON ESE NODO ES SANO: comparten la forma "
     "y ni un objeto, porque aquel contesta dudas de las reuniones de salto de nivel y este de pedir "
     "critica. Y NO ES UNA SERIE D.37: el texto no escribe cuantas dudas recoge, asi que ni el id ni "
     "el titulo llevan cifra. RELECTURA DE FIDELIDAD D.30 EN EL ACTO, paso a paso contra su linea: "
     "15 pasos, 15 TRANSCRIPCION, 0 PUENTE. P1 a P3 de la linea 171; P4 a P8 de la linea 175; P9 y "
     "P10 de la linea 179; P11 a P14 de la linea 183; P15 de la linea 185. LA CITA DE CAROL DWECK "
     "VIAJA CON SU AUTORA NOMBRADA porque el libro la nombra y sin el nombre el paso no se puede "
     "buscar, que es manual 3.5. LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: cuanto tiempo es "
     "razonable pedir para pensar una critica que no sabes arreglar, y que se hace si la persona "
     "mayor sigue despachandote. El libro pone las cuatro dudas y no pone esas dos respuestas.")))

for d in NODOS:
    r = escribe(d)
    print('escrito %s  (%d pasos)' % (r, len(d['pasos_accionables'])))
