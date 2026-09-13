# -*- coding: utf-8 -*-
"""LOS SEIS ULTIMOS CANDIDATOS DE cap_13, ESCRITOS CONTRA SU LINEA (D.30)."""
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
    "abrazar_incomodidad_silencio_contar_seis",
    ("Abrazar la incomodidad del silencio despues de pedir critica, aguantandolo mientras cuentas "
     "hasta seis en tu cabeza"),
    ("Abraza la incomodidad, puesto en acto: el silencio que sigue a tu pregunta y la practica de "
     "contar hasta seis"),
    ["EMBRACE THE DISCOMFORT", "Practice: Count to six in your head"],
    ("Cuando has pedido critica a alguien y se hace el silencio, y te tienta rellenarlo o dejar a la "
     "otra persona salir del apuro."),
    ("El silencio aguantado hasta el final, con la respuesta del otro salida de el, o con el "
     "compromiso escrito de volver a preguntarle."),
    [
        "Parte de lo que le haces al otro cuando le pides critica, que es lo que el texto pone primero: le metes en una situacion incomoda.",
        "No seas ruinosamente empatico y no le dejes salir del apuro.",
        "Dale tiempo y espacio para formular su respuesta.",
        "Cuenta con que a menudo la gente se queda callada despues de que preguntes, y resiste la tentacion de rellenar el silencio.",
        "Aguantalo aunque sea incomodo para ti y para el otro, porque el texto dice que tu trabajo es soportarlo e incluso abrazarlo.",
        "Cuenta con lo que el texto ha medido en sus talleres: parece facil, y hace falta una disciplina enorme.",
        "Practicalo asi: hazle tu pregunta a un companiero amistoso y cuenta hasta seis.",
        "No te permitas decir nada, por incomodo que te sientas o por incomodo que parezca el otro.",
        "Cuenta con lo que esa cuenta te da: buena parte de poner la franqueza radical en practica es ser capaz de atravesar la incomodidad social, y este truco te saca la cabeza de la incomodidad.",
        "Fijate en cuantos segundos aguanta tu companiero el silencio antes de saltar a decir algo, porque el texto dice que la mayoria no aguanta hasta seis y dice algo. Puede que no sea profundo, pero es un principio.",
        "Y si aun asi se quedan callados, diles que les vas a dar mas tiempo pero que vas a volver a ellos porque de verdad quieres su critica.",
        "Y no te olvides de volver a preguntar: no les dejes salir del apuro, ni te dejes salir a ti.",
    ],
    ("Sale de las lineas 187 a 198, bajo el rotulo EMBRACE THE DISCOMFORT de la linea 187. ES LA "
     "PIEZA 7 DE LA FRONTERA DE cap_13, y es el segundo de los cuatro elementos de pedir critica que "
     "la linea 113 enumera. POR QUE ES PROCEDIMIENTO Y NO UNA POSTURA, con D.27 delante: el propio "
     "libro dice en la linea 189 que muchos participantes le han dicho que no sabian como poner en "
     "accion el consejo de abrazar la incomodidad, y entonces pone su INVENTARIO DE ETAPAS (no le "
     "dejes salir, dale tiempo, resiste el silencio, cuenta hasta seis, vuelve a preguntar) y un "
     "ejercicio con su cuenta escrita. Deja fichero: la respuesta salida del silencio, o el "
     "compromiso de volver. EL SEIS DEL ID ES DEL LIBRO Y NO MIO: la linea 193 escribe Count to six "
     "in your head y la 195 lo repite. SU ARISTA CON pedir_critica_primero_crear_seguridad_"
     "psicologica va declarada en el reporte de la vuelta 23 con su paso 17 citado, que es el que "
     "enumera los cuatro elementos. SU PAR CON abrazar_incomodidad_arrancar_critica_equipo (cap_09), "
     "leido antes de que lo levante ninguna senial y porque su id se parece tanto que seria "
     "negligente no mirarlo: aquel entrega la primera critica arrancada a un equipo que no critica; "
     "este entrega UN SILENCIO CONCRETO aguantado con una cuenta hasta seis, que aquel no tiene. "
     "Comparten el acto de no dejar salir del apuro y los dos tienen procedimiento fuera de el. VA "
     "MARCADO COMO DISCUTIBLE EN EL REPORTE. RELECTURA DE FIDELIDAD D.30 EN EL ACTO, paso a paso "
     "contra su linea: 12 pasos, 12 TRANSCRIPCION, 0 PUENTE. P1 a P6 de la linea 191; P7 a P10 de la "
     "linea 195; P11 y P12 de la linea 197. LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: cuanto "
     "se espera antes de volver a preguntar, y cuantas veces se insiste. El libro pone la cuenta "
     "hasta seis y no pone ninguna de las dos.")))

NODOS.append(nodo(
    "escuchar_entender_critica_dominar_defensa",
    ("Escuchar la critica con intencion de entender y no de responder, dominando tu propia defensa "
     "con la practica de escuchar tres minutos sin interrumpir"),
    ("Escucha con intencion de entender, no de responder: que hacer con la respuesta de pelea, huida "
     "o bloqueo, y el ejercicio de los tres minutos"),
    ["LISTEN WITH THE INTENT TO UNDERSTAND, NOT TO REPLY", "Practice: Listening"],
    ("Cuando estas recibiendo una critica y notas que te estas poniendo a la defensiva, aunque la "
     "hayas pedido tu."),
    ("La critica escuchada entera sin respuesta defensiva, con tu propio recurso de proceso "
     "identificado y el ejercicio de los tres minutos hecho con alguien."),
    [
        "Parte de lo que el texto reconoce que pasa: recibir critica puede disparar en nosotros la respuesta de pelea, huida o bloqueo, incluso cuando la hemos pedido.",
        "Cuenta con que no solo cuesta la critica injusta: la critica justa, sobre todo cuando toca algo que ya no nos gusta de nosotros mismos, tambien cuesta.",
        "Averigua que te ayuda a ti a procesar lo que oyes sin caer en una respuesta defensiva, que es lo que el texto encarga: un ejercicio de respiracion puede ayudar, y tambien dar un trago largo de una botella de agua.",
        "Y sobre todo practica con otros, que es lo que el texto pone por encima de lo demas.",
        "Practicalo asi: busca una pareja con quien practicar, sea companiero de trabajo, amigo o familiar.",
        "Que una persona hable durante tres minutos.",
        "Despues cambiad los papeles y escucha a la otra persona hablar, sin interrumpir.",
        "Podeis hablar de lo que querais: cualquier cosa que os importe de verdad, del trabajo o de fuera de el.",
        "Si eres tu quien escucha, dale a quien habla el regalo de tu atencion completa.",
        "Puedes asentir, o decir ya veo o entiendo, pero este no es el momento de preguntas.",
        "Ni de que relaciones su historia con algo que te importe a ti, como tu historia favorita de las vacaciones en Hawai.",
        "Ni de darle a quien habla ese consejo que le va a cambiar la vida para siempre: tu trabajo no es dar consejo, es escuchar.",
        "Y cuenta con lo que el texto ha medido haciendo esto: companieros que llevaban mas de diez anios en el mismo equipo aprendieron mas unos de otros en tres minutos que en una decada trabajando juntos. Escuchar, escuchar de verdad, es increiblemente eficiente.",
    ],
    ("Sale de las lineas 199 a 214, bajo el rotulo LISTEN WITH THE INTENT TO UNDERSTAND, NOT TO "
     "REPLY de la linea 199. ES LA PIEZA 8 DE LA FRONTERA DE cap_13, y es el tercero de los cuatro "
     "elementos de pedir critica que la linea 113 enumera. POR QUE ES PROCEDIMIENTO Y NO UNA FRASE "
     "DE CARTEL, con D.27 delante: el propio libro dice en la linea 201 que esta es otra linea muy "
     "tuiteada del libro que a muchos no les ayudo a aprender a manejar su defensa, y entonces pone "
     "su INVENTARIO DE MEDIOS (el ejercicio de respiracion, el trago de agua, practicar con otros) y "
     "un ejercicio con sus etapas y su cuenta de minutos. Deja fichero: la critica escuchada entera. "
     "SU ARISTA CON pedir_critica_primero_crear_seguridad_psicologica va declarada en el reporte de "
     "la vuelta 23 con su paso 17 citado. SU PAR CON crear_cultura_escucha_equipo Y CON "
     "escuchar_callado_equipo_tranquilizar_incomodo (cap_07), leido antes de que lo levante ninguna "
     "senial: aquellos entregan una cultura de escucha en el equipo y un estilo de escucha callada; "
     "este entrega TU PROPIA DEFENSA DOMINADA mientras te critican a ti, que es otro entregable y "
     "otra condicion de activacion. Comparten la palabra escuchar y ni un acto. Va marcado como "
     "discutible en el reporte. LA HISTORIA DE KIM Y SU HIJA, QUE ESTA EN LA LINEA 95 Y NO AQUI, ES "
     "EL EJEMPLAR DE ESTA DOCTRINA y por eso no la repito: manual 3.5, el caso vive en su tramo de "
     "resto. RELECTURA DE FIDELIDAD D.30 EN EL ACTO, paso a paso contra su linea: 13 pasos, 13 "
     "TRANSCRIPCION, 0 PUENTE. P1 y P2 de la linea 203; P3 y P4 de la linea 205; P5 a P8 de la linea "
     "209; P9 a P12 de la linea 211; P13 de la linea 213. LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA "
     "AQUI: cada cuanto se repite el ejercicio de los tres minutos, y que se hace cuando el ejercicio "
     "de respiracion no basta. El libro pone los medios y no pone ninguna de las dos.")))

NODOS.append(nodo(
    "premiar_franqueza_hacer_escucha_tangible",
    ("Premiar la franqueza de quien te critica haciendo tangible tu escucha, con la lista de las "
     "criticas recibidas y lo que has hecho con ellas contado en publico"),
    ("Haz tangible la escucha: premia la franqueza, ensenia tu trabajo, y premia tambien la critica "
     "con la que no estas de acuerdo"),
    ["MAKE LISTENING TANGIBLE: REWARD THE CANDOR", "Practice: Make Listening Tangible",
     "Practice: Reward criticism you disagree with"],
    ("Cuando alguien te ha dado una critica y quieres que vuelva a darsela, o cuando quieres que tu "
     "equipo vea que la critica que te dan sirve para algo."),
    ("El problema criticado arreglado deprisa o explicado por que no puedes, y la critica recibida "
     "contada en publico con lo que aprendiste y lo que vas a hacer con ella."),
    [
        "Parte de lo que hace quien te critica, que es de donde el texto saca el encargo: esta asumiendo un riesgo, y tu trabajo es asegurarte de que se le premia por asumirlo, o no lo volvera a hacer.",
        "Premia la critica valiosa de la mejor manera que el texto ha encontrado: arregla el problema deprisa, o explica claramente por que no puedes y busca una solucion de rodeo.",
        "Cuenta con el sesgo contra el que juegas, que el texto llama sesgo de negatividad: aunque respondas bien a la critica nueve de cada diez veces, la que recordaran es la vez que respondiste a la defensiva.",
        "Ten delante la frase con que el texto lo resume, de Rick Hanson, autor de Resilient: el cerebro es como el velcro para las experiencias negativas y como el teflon para las positivas.",
        "Por eso haz que se note cuando premias la franqueza, y el texto pone su ejemplar: la directora de Spanx, Sara Blakely, puso la cancion Oops! I Did It Again mientras describia a toda la empresa un patron de errores que habia cometido.",
        "Celebra tus propios fallos, y ensenia que la unica manera de que mejores es que la gente te los seniale.",
        "Habla en publico de la critica util que has recibido y de como has intentado resolverla, porque eso senializa que para ti la critica es un regalo y no una patada en la espinilla.",
        "Practicalo asi: haz una lista de las tres o cuatro veces que unos companieros te han ofrecido alguna critica recientemente.",
        "Si no se te ocurre nada, no significa que seas perfecto: significa o que no estas oyendo lo que te dicen, o que no se sienten comodos compartiendo su critica.",
        "Y si no tienes nada en la lista, vete de pesca. Y pesca critica, no elogio.",
        "En una reunion de equipo o en una reunion de pie, comparte alguna critica que hayas recibido en la ultima semana, lo que aprendiste de ella, tu agradecimiento por ella, y que piensas hacer al respecto.",
        "Pide ayuda al equipo mientras intentas cambiar tu conducta o resolver el problema que te plantearon.",
        "Deja claro que agradeces mas critica en esas mismas areas, y recibela con gusto si te llega.",
        "Cuenta con las dos cosas buenas que el texto dice que pasan cuando dedicas un rato a ensenar que estas haciendo con la critica que te han dado: una, haces tangible tu escucha, porque a menudo los lideres trabajan duro para resolver una critica y se olvidan de compartir ese esfuerzo con el equipo. Ensenia tu trabajo.",
        "Y dos, te enteras de si has arreglado el problema: a veces descubriras que te has pasado, o que no has llegado, y en cualquiera de los dos casos tienes ocasion de calibrar tu respuesta.",
        "Y practica tambien con la critica con la que no estas de acuerdo: piensa en alguna que hayas recibido hace poco y con la que basicamente no estabas de acuerdo, e intenta encontrar algun elemento de ella con el que si puedas estar de acuerdo.",
        "Comparte con la persona esa zona de acuerdo, para demostrar que la escuchaste y que estas abierto a la critica.",
        "Despues hazle saber que hay elementos de lo que dijo con los que no estas de acuerdo, y preguntale si esta dispuesta a tener una conversacion mas larga.",
        "Si lo esta, articula lo mas claramente que puedas por que no estas de acuerdo, o por que cambiar tu conducta daria peores resultados.",
        "Y cuenta con lo que el texto senialla como lo peor que puedes hacerle a una relacion: fingir que escuchas mientras descartas en silencio lo que te dicen, porque eso hace que la gente se sienta invisible e ignorada. Un desacuerdo respetuoso puede fortalecer una relacion, e ignorar a una persona casi nunca lo hace.",
    ],
    ("Sale de las lineas 215 a 234, bajo el rotulo MAKE LISTENING TANGIBLE: REWARD THE CANDOR de la "
     "linea 215. ES LA PIEZA 9 DE LA FRONTERA DE cap_13, y es el cuarto de los cuatro elementos de "
     "pedir critica que la linea 113 enumera. POR QUE ES PROCEDIMIENTO Y NO POSTURA, con D.27 "
     "delante: el libro pone su propio INVENTARIO DE ETAPAS Y DE OBJETOS, con DOS ejercicios "
     "rotulados (Practice: Make Listening Tangible en la linea 223 y Practice: Reward criticism you "
     "disagree with en la 231) y sus etapas escritas una a una. Deja fichero: la lista de tres o "
     "cuatro criticas y lo contado en la reunion. POR QUE LOS DOS EJERCICIOS VAN EN UN SOLO NODO Y "
     "NO EN DOS, con la vara de la ACTA 20 seccion 4.1 delante: comparten UNA condicion de "
     "activacion (alguien te ha criticado y quieres que vuelva a hacerlo) y UN entregable (la "
     "escucha hecha tangible), y el segundo es el caso dificil del primero, no otro procedimiento. "
     "SU ARISTA CON pedir_critica_primero_crear_seguridad_psicologica va declarada en el reporte de "
     "la vuelta 23 con su paso 17 citado. SU PAR CON pedir_critica_equipo_premiarla (cap_09), leido "
     "antes de que lo levante ninguna senial porque es el par mas caro de fallar de todo el "
     "capitulo: aquel entrega la critica pedida y premiada en el acto de la conversacion; este "
     "entrega LA LISTA DE LAS TRES O CUATRO CRITICAS RECIENTES y lo que hiciste con ellas contado en "
     "publico en una reunion de equipo, con el sesgo de negatividad, la pesca cuando la lista esta "
     "vacia y el protocolo de la critica con la que no estas de acuerdo, que aquel no tiene. Va "
     "marcado como discutible en el reporte. RELECTURA DE FIDELIDAD D.30 EN EL ACTO, paso a paso "
     "contra su linea: 20 pasos, 20 TRANSCRIPCION, 0 PUENTE. P1 y P2 de la linea 217; P3 y P4 de la "
     "linea 219; P5 a P7 de la linea 221; P8 a P10 de la linea 225; P11 a P13 de la linea 227; P14 y "
     "P15 de la linea 229; P16 a P20 de la linea 233. LOS NOMBRES PROPIOS QUE VIAJAN: Rick Hanson "
     "con su libro y Sara Blakely con su empresa y su cancion, porque el libro los nombra y son el "
     "ejemplar de manual 3.5. LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: cada cuanto se cuenta "
     "en publico, cuanto se espera para arreglar el problema, y que se hace si el equipo no se cree "
     "el gesto. El libro pone los dos ejercicios y no pone ninguna de las tres.")))

NODOS.append(nodo(
    "integrar_peticion_critica_rutina_existente",
    ("Integrar la peticion de critica en la rutina que ya tienes, al final de tus reuniones a solas, "
     "para que deje de depender de tu acordarte"),
    ("Metelo en tu horario existente: el habito regular de pedir critica, por que verlo una vez no "
     "basta, y donde encaja"),
    ["BUILD IT INTO YOUR EXISTING SCHEDULE",
     "Practice: add soliciting feedback to the end of your 1:1 agenda"],
    ("Cuando ya has practicado los cuatro elementos de pedir critica por separado y quieres "
     "juntarlos y convertir la peticion en un habito."),
    ("La peticion de critica metida al final de tus reuniones a solas ya programadas, anunciada al "
     "equipo con la pregunta que vas a hacer."),
    [
        "Parte de por que no basta con hacerlo una vez, que es lo que el texto pone: ver al jefe pedir critica una vez no es suficiente, porque el miedo a ofender al poderoso no muere facil.",
        "Cuenta con la consecuencia que el texto saca de ahi: solo podemos estar seguros de que un jefe quiere critica si tiene la costumbre de pedirla con regularidad.",
        "Asi que busca la manera de meterla en una practica regular para que ocurra automaticamente.",
        "Cuenta con lo que eso consigue, que el texto describe entero: cuando un jefe aparta tiempo cada semana para reuniones a solas y pide critica al final de cada una, los empleados llegan a esperarlo como lo normal. Establecer una rutina regular les senializa que vas a pedir critica, y les vuelve mas atentos en general a que podrias hacer mejor o cambiar para que ellos sean mas eficaces.",
        "Aprovecha ademas el otro gran momento que el texto nombra: cuando la gente esta de verdad enfadada contigo. El instinto es evitar a quien esta enfadado, y ese es justo el momento en que es mas probable que oigas la verdad sin barniz.",
        "Junta ahora los cuatro elementos que has practicado por separado, que es lo que el texto ordena aqui: dar con una pregunta recurrente, abrazar la incomodidad, escuchar con intencion de entender, y hacer tangible la escucha premiando la franqueza.",
        "Para construir el habito, minimiza el esfuerzo, que es la regla que el texto da: eso significa meterlo en las rutinas que ya tienes.",
        "Ponlo en el sitio ideal que el texto nombra: al final de tus reuniones a solas ya programadas con la gente del equipo.",
        "No tiene por que ser una reunion a solas, porque el texto reconoce que distinta gente tiene distintos enfoques de esas reuniones. Pero si tienes que pedir critica a menudo, para que sea como cepillarse los dientes y usar el hilo dental y no como una limpieza anual que temes.",
        "Y pidela en privado, que es lo que el texto dice que es mejor: hace la situacion menos amenazante para el otro, y ademas baja la amenaza a tu ego y sube tus posibilidades de mantener la compostura y la curiosidad.",
        "Cuenta con lo que te vas a encontrar las primeras veces: el texto dice que las primeras veinte o asi te va a parecer un acto antinatural, y que tu trabajo es empujar a traves de la incomodidad.",
        "Practicalo asi: hazle saber a tu equipo que piensas pedir critica en vuestras proximas reuniones a solas.",
        "Y como extra, comparteles la pregunta que piensas hacer, porque el texto dice que sobre todo al principio de normalizar esta conducta es importante darles tiempo para pensar en conductas tuyas que de verdad les importen.",
    ],
    ("Sale de las lineas 111 a 112 y 235 a 246, bajo el rotulo BUILD IT INTO YOUR EXISTING SCHEDULE "
     "de la linea 235. ES LA PIEZA 10 DE LA FRONTERA DE cap_13. POR QUE SE LLEVA LA LINEA 111, QUE "
     "ESTA A CIENTO VEINTICUATRO LINEAS DE DISTANCIA Y DENTRO DE OTRA SECCION: porque es EL MISMO "
     "OBJETO que la linea 239 (meter la peticion de critica al final de la reunion a solas para que "
     "se vuelva rutina), y P.19 manda fundir el objeto repetido en un solo procedimiento en vez de "
     "mandarlo a nodo propio y fabricar el gemelo de su propio donante. LA FRONTERA LO DECLARA COMO "
     "TRAMO NO CONTIGUO y lo publica antes de cortar, que es EXTRACTOR.md 10. POR QUE ES "
     "PROCEDIMIENTO Y NO POSTURA, con D.27 delante: el libro pone su propio INVENTARIO DE ETAPAS Y "
     "DE SITIOS (la rutina existente, el final de la reunion a solas, en privado, el momento del "
     "enfado) mas un ejercicio rotulado con sus dos actos. Deja fichero: la peticion metida en la "
     "agenda y anunciada. SU ARISTA CON pedir_critica_primero_crear_seguridad_psicologica va "
     "declarada en el reporte de la vuelta 23 con su paso 17 citado, porque su paso 6 junta "
     "expresamente los cuatro elementos que aquel enumera. SU PAR CON "
     "montar_reuniones_solas_mentalidad_frecuencia (cap_11) ES SANO Y LO DIGO CON LOS DOS LADOS "
     "MEDIDOS: aquel entrega las reuniones a solas montadas y no canceladas con su agenda, y en sus "
     "22 pasos no hay ni uno que meta la peticion de critica al final; este entrega la peticion de "
     "critica metida en esa reunion. Son procedimientos vecinos con entregables distintos, ninguno "
     "despliega al otro. RELECTURA DE FIDELIDAD D.30 EN EL ACTO, paso a paso contra su linea: 13 "
     "pasos, 13 TRANSCRIPCION, 0 PUENTE. P1 a P5 de la linea 111; P6 de la linea 237; P7 a P10 de la "
     "linea 239; P11 de la linea 241; P12 y P13 de la linea 245. LO QUE EL TEXTO NO DICE Y POR ESO "
     "NO ESTA AQUI: que se hace si no tienes reuniones a solas, cuanto tiempo del final se reserva, "
     "y que pasa cuando la reunion se queda sin tiempo. El libro pone el sitio y no pone ninguna de "
     "las tres.")))

NODOS.append(nodo(
    "dar_elogio_disciplina_igual_critica",
    ("Dar elogio con la misma disciplina que pones en la critica, comprobando los hechos antes y "
     "diciendolo concreto, porque el elogio es el acelerador y la critica el freno"),
    ("El elogio con disciplina: el acelerador y el freno, por que el elogio vago patrocina, y el "
     "ejercicio de dar un elogio concreto a un companiero"),
    ["PRAISE: FOCUS ON THE GOOD STUFF. REALLY.",
     "APPLY THE SAME DISCIPLINE TO PRAISE THAT YOU DO TO CRITICISM", "Praise Practice"],
    ("Cuando acabas de hacer el trabajo duro de pedir critica y te tienta pasar directamente a dar "
     "la tuya, o cuando vas a elogiar a alguien y no has comprobado los hechos."),
    ("El elogio dado primero y concreto, con los hechos comprobados antes, sin comparaciones odiosas "
     "y sin un gran trabajo vacio."),
    [
        "Parte de la imagen con la que el texto ordena las dos: cuando diriges un equipo, la critica es tu freno y el elogio es tu acelerador. Si quieres ir a algun sitio tienes que usar el acelerador mas que el freno, y si no usas nunca el freno te estrellas y no llegas a ninguna parte. Y te sentiras mas seguro pisando el acelerador si sabes que los frenos funcionan.",
        "Cuenta con la razon por la que la gente se resiste a elogiar, que el texto nombra sin rodeos: es mucho mas facil parecer listo criticando. Y la meta de la guia es ayudar a los demas a tener exito, no demostrar lo listo que eres tu.",
        "No uses el elogio como arma, que es el otro mal uso que el texto nombra: decir que fulano es estupendo, que os pasa al resto de perdedores, tira a quien tuvo exito debajo de un autobus lleno de companieros que ahora le guardan rencor, y no vas a conseguir que el exito se repita.",
        "Haz que tu elogio sea concreto y sincero, y que inspire a los demas en vez de hacer comparaciones odiosas.",
        "Pon disciplina de verdad en el foco sobre el elogio, y cuenta con por que cuesta: despues del trabajo duro y doloroso de pedir critica, apetece dar algo de la tuya, y probablemente llevas un tiempo guardandote alguna.",
        "Cuenta con el aviso que el texto te da justo ahi: muy a menudo lo que te molesta lleva molestandote tanto tiempo que es todo lo que puedes ver o sentir, y has dejado de notar todo lo que te gusta de trabajar con esa persona. Si solo ves lo negativo, probablemente no estas en la mentalidad correcta para dar critica.",
        "Asi que centrate en lo bueno y elogia primero.",
        "Cuenta ademas con lo que el elogio consigue y la critica no: ayuda a la gente a centrarse en sus fuerzas y a hacer mas del trabajo que disfruta y menos del que odia.",
        "Cuenta con la excepcion que el texto deja escrita: a veces tienes que asegurarte de que una persona llega a un nivel de competencia en el que un defecto no se vuelve fatal.",
        "Pero cuenta con donde esta el rendimiento: sacas mas partido centrandote en las fuerzas que en las debilidades, maximizando lo de arriba en vez de minimizando lo de abajo.",
        "Y cuenta con lo que el elogio hace que lo vuelve practico y no solo agradable: revela lo que funciona y lo hace usable y repetible, ensenia como una fuerza puede llevar al exito y como se puede construir un exito sobre otro, demuestra que te importa personalmente, y desafia directamente, porque anima a la gente a seguir haciendo mas de lo que esta bien.",
        "Hazte la pregunta que el texto hace en sus talleres, tomada de Karen Sipprell: cuanto tiempo dedicas a asegurarte de que tienes los hechos claros antes de dar elogio a alguien de tu equipo? Y cuenta con que la respuesta tipica es ninguno.",
        "Cuenta con lo que pasa cuando eres vago con el elogio: es igual de probable que dejes a la persona sintiendose patrocinada, y en cualquier caso la positividad vaga tiene muy poco impacto a largo plazo. Un gran trabajo vacio puede sonar condescendiente y desmoralizar, que es justo lo contrario del efecto que buscabas.",
        "Da elogio concreto, porque el texto dice que ayuda a la persona y al equipo a entender como es el exito, y le da a los miembros ambiciosos del equipo un modelo que seguir.",
        "Y aplicale al elogio las mismas pautas que a la critica, que el texto repite aqui: hazlo con humildad, con utilidad y de inmediato; elogia en publico y critica en privado; y no des guia sobre atributos de personalidad.",
        "Practicalo asi: emparejate con un companiero y compartid un elogio concreto cada uno.",
        "Cuenta con lo que el texto ha medido de ese ejercicio: la gente sale sintiendose vista, conectada e inspirada, y dicen cosas como llevo anios haciendo esto y no sabia que nadie se hubiera dado cuenta, lo que lleva a mas implicacion cuando vuelven a la oficina.",
        "Cuenta con que no cuesta tanto como parece: no es dificil encontrar cosas que elogiarse unos a otros, incluso con alguien que acabas de conocer en un taller. Se vuelve mas facil centrarse en lo bueno cuando pones la intencion de hacerlo, te da curiosidad, y despues dices algo de verdad concreto.",
        "Ten delante los dos ejemplares que el texto escribe de ese elogio concreto: gracias por hacer esa pregunta sobre llegar tarde a las reuniones, no sabia si ibamos a tratarlo y ayudo a mover la conversacion. Y gracias por escucharme cuando hablaba de mi hija, de verdad necesitaba hablar de ello.",
        "Y cuenta con para que sirve ademas del proposito principal: el proposito primero del elogio es ensenar hacia donde vamos y como es lo bueno, y este ejercicio corto es ademas una via rapida y facil de construir la habilidad de dar voz a lo que aprecias.",
    ],
    ("Sale de las lineas 247 a 252 y 267 a 288, bajo los rotulos PRAISE: FOCUS ON THE GOOD STUFF. "
     "REALLY. de la linea 247 y APPLY THE SAME DISCIPLINE TO PRAISE THAT YOU DO TO CRITICISM de la "
     "275. ES LA PIEZA 11 DE LA FRONTERA DE cap_13. POR QUE LOS DOS ROTULOS VAN EN UN SOLO NODO Y NO "
     "EN DOS, con la vara de la ACTA 20 seccion 4.1 delante: comparten UNA condicion de activacion "
     "(vas a dar elogio y te tienta pasar a la critica o quedarte en lo vago) y UN entregable (el "
     "elogio dado primero y concreto), y el segundo rotulo es la disciplina del primero, no otro "
     "procedimiento. POR QUE ES PROCEDIMIENTO Y NO POSTURA, con D.27 delante: el libro pone su "
     "propio INVENTARIO DE OBJETOS A COMPROBAR (los hechos antes de elogiar, la concrecion frente a "
     "la vaguedad, la comparacion odiosa, los tres pares de pautas de la linea 279) y un ejercicio "
     "rotulado con sus dos ejemplares literales. Deja fichero: el elogio dado y lo que dijo. LA "
     "HISTORIA DE JASON Y DAVE (lineas 253 a 266) NO VIAJA A NINGUN PASO: es manual 3.5, y su "
     "doctrina (que si no hubiera elogiado a Dave, Dave habria seguido preocupado por haberle pisado "
     "el terreno) esta escrita fuera del caso en las lineas 267 y 273. SU PAR CON "
     "elogiar_trabajo_especifico_contexto Y CON equilibrar_elogio_critica_equipo (cap_05 y cap_09), "
     "leido antes de que lo levante ninguna senial porque son los dos pares mas caros de fallar de "
     "esta pieza: MI VEREDICTO ES CONTINUA CON ARISTA en los dos casos y NO REPITE, con los lados "
     "medidos. Aquellos entregan el elogio concreto con su contexto y el balance de elogio y critica "
     "del equipo; este trae lo que ninguno de los dos tiene, que es LA PREGUNTA DE KAREN SIPPRELL "
     "sobre comprobar los hechos antes de elogiar, la imagen del acelerador y el freno, el elogio "
     "usado como arma, y el ejercicio de pareja con sus dos ejemplares. VA MARCADO COMO DISCUTIBLE "
     "EN EL REPORTE, y es el corte mas discutible del capitulo. RELECTURA DE FIDELIDAD D.30 EN EL "
     "ACTO, paso a paso contra su linea: 20 pasos, 20 TRANSCRIPCION, 0 PUENTE. P1 de la linea 251; "
     "P2 de la linea 267; P3 y P4 de la linea 269; P5 a P7 de la linea 271; P8 a P11 de la linea "
     "273; P12 de la linea 277; P13 a P15 de la linea 279; P16 y P17 de la linea 283; P18 a P20 de "
     "las lineas 285 y 287. LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: cuanto elogio por cada "
     "critica, cada cuanto se hace el ejercicio de pareja, y como se comprueban los hechos antes de "
     "elogiar. El libro hace la pregunta de los hechos y NO da el metodo de contestarla, y "
     "escribirlo seria escribirlo yo.")))

NODOS.append(nodo(
    "medir_critica_respuesta_oyente_brujula",
    ("Medir tu critica en la respuesta de quien la oye, usando el marco de la franqueza radical como "
     "brujula para decidir si toca importarte mas o desafiar mas claro"),
    ("Medir la critica: la franqueza radical se mide en el oido del otro y no en tu boca, y que "
     "hacer ante la tristeza, ante el enfado y ante quien no te oye"),
    ["GAUGE CRITICISM", "listen-challenge-commit", "It's not mean, it's clear"],
    ("Cuando estas dando una critica y tienes delante la respuesta del otro, y tienes que decidir "
     "que hacer con ella."),
    ("La critica ajustada sobre la marcha segun la respuesta del oyente, con la emocion nombrada si "
     "la hubo y con la conversacion devuelta al carril."),
    [
        "Parte de la frase que el texto trae aqui para ponerla en accion: la franqueza radical no se mide en tu boca, sino en el oido de la otra persona.",
        "No busques las palabras magicas, porque el texto dice que no existen: no hay palabras que sirvan a la vez de bisturi y de anestesia emocional.",
        "Cuenta con los dos casos que salen de ahi: a veces la franqueza radical escuece un poco, y cuando escuece tu trabajo es que te importe personalmente. Mas a menudo no escuece porque no se ha oido, y entonces tu trabajo es desafiar directamente.",
        "Usa el marco de la franqueza radical como una brujula para medir tu critica y llevar la conversacion a un sitio mejor.",
        "Presta mucha atencion a la respuesta del otro a lo que has dicho, y decide si necesita que le ensenies que te importa personalmente, o que seas mas directo y mas claro en tu desafio.",
        "Cuenta con la regla que el texto pone por encima: la manera en que escuchas importa mas que la manera en que hablas.",
        "Cuando ofrezcas franqueza compasiva, empieza suave y despues mide la respuesta del otro: escucha lo que dice, observa su lenguaje corporal, mirale a los ojos, y preguntate como parece que se siente y si te ha oido.",
        "Y no lo hagas desde el telefono ni desde el ordenador, porque el texto dice que asi no se puede hacer.",
        "Si la persona con la que hablas parece triste, esa es tu senial para pararte un momento y ensenar que te importa personalmente.",
        "Cuenta con que eso cuesta, y con por que: ante alguien que parece disgustado, nuestra inclinacion natural es retirarnos de lo que estabamos diciendo, o sea movernos en la direccion equivocada del eje de desafiar directamente. Y este es justo el momento de ensenar que te importa.",
        "Usa el marco como brujula para no caer en la trampa de la empatia ruinosa, que es lo que el texto dice que te recuerda: puedes ir en la direccion correcta del eje de importarte personalmente sin ir en la direccion equivocada del de desafiar directamente.",
        "Si lo que recibes es una respuesta enfadada, esa es tu senial para atender a las emociones que hay en la sala y ensenar que te importa personalmente.",
        "Cuenta con que eso tambien cuesta: cuando el otro esta enfadado es natural enfadarse uno, y el texto dice que nada te baja mas deprisa en el eje de importarte personalmente que el enfado.",
        "Nombra la emocion que estas viendo, que es la via que el texto da para ensenar que te importa ante emociones negativas: parece que te he disgustado, o que te he cabreado, o que te he frustrado. No era lo que queria hacer. Estoy intentando ayudarte. Como puedo decir esto de una manera mejor?",
        "No uses ese guion literal: usa tus propias palabras.",
        "Cuenta con lo que nombrar la emocion consigue y con lo que hace lo contrario: a menudo nombrarla ayuda a la persona a sentirse vista, y nuestra tendencia ante las emociones negativas es fingir que no estan pasando, lo que hace que el otro se sienta invisible o invalidado.",
        "Se humilde al nombrar la emocion, porque puedes estar entendiendola mal: el texto pone su propio ejemplar, que si la autora empieza a llorar es probablemente porque esta furiosa y no triste.",
        "Y hagas lo que hagas, no juzgues la emocion ni le digas a la persona que no deberia sentirla. Quita no te lo tomes como algo personal de tu vocabulario.",
        "Y cuando todo lo demas falle, usa la respuesta simple que el texto da para las emociones negativas: como puedo ayudar?",
        "Si en cambio la persona sencillamente no te oye, porque esta a la defensiva, o ajena, o irremediablemente optimista, o sobrada, o distraida, esa es tu senial para moverte a la derecha en el eje de desafiar directamente.",
        "Cuenta con que ser extremadamente claro puede sentirse duro y con que la mayoria de la gente se resiste con razon a ser dura, y usa ahi el lema que el texto da: no es cruel, es claro.",
        "Centrate en el largo plazo, que es lo que el texto dice que ayuda en esos momentos: si esta persona esta cometiendo un error que le va a hacer danio con el tiempo, la unica manera de que lo arregle es que sea consciente de el, aunque esa consciencia duela un poco en el momento.",
        "Si ves que se esta cerrando, cuenta con que a veces es porque no esta de acuerdo con lo que dices y no quiere decirlo: tu primera meta es que te diga si esta en desacuerdo, y por que.",
        "Cuenta con el riesgo que eso trae: puede que venga hacia ti agresivamente y te diga por que eres una persona terrible, catalogando todos tus defectos. Si pasa, reconoce que no eres perfecto y di que te gustaria hablar de esos problemas en otra conversacion, pero que ahora mismo quieres hablar del asunto que teniais entre manos.",
        "Usa el lema que el texto da para dar critica, escuchar, desafiar y comprometer, y no te saltes el paso de en medio: no pases demasiado deprisa a pedir un compromiso de cambio sin darle la oportunidad de desafiarte. La meta es animar a la persona a meterse en la conversacion, a escuchar y a participar, incluso cuando eso signifique estar en desacuerdo con tu critica, y especialmente cuando lo este.",
        "Y si aun asi no te oye, prueba a preguntar: solo para asegurarme de que estamos en la misma pagina, puedes decirme que acabas de oir?",
        "O di lo que estas sintiendo: no siento que se me este oyendo.",
        "O prueba con: puedo ser mucho mas directo contigo?",
        "Y no llames la atencion sobre las consecuencias de no cumplir con la critica antes de haberle dado a la persona la oportunidad de estar en desacuerdo con ella, que es el error que el texto dice que se comete a menudo: muchos van demasiado deprisa a tu puesto esta en riesgo si no arreglas esto. Puede que sea verdad, pero si la persona no esta de acuerdo con la critica eso se siente como una consecuencia injusta.",
        "Cuenta con lo que esa prisa rompe: estas intentando enganchar el deseo interno de la persona de mejorar y crecer en su carrera, e ir demasiado deprisa a los castigos externos puede danar esa motivacion interna, porque si ya estoy de salida o me han condenado sin juicio, para que voy a intentar arreglarlo.",
        "Y cuenta con la excepcion que el texto deja escrita: si el problema va a llevar a que la persona entre en un plan de mejora de desempenio o a que la despidan de forma inminente, cuanto antes se lo digas mejor.",
        "Lleva ademas varios ejemplares concretos del problema que intentas hacerle ver, que es lo otro que el texto dice que ayuda.",
        "Y si te interrumpen con excusas despues del primero, di algo como: antes de meternos muy a fondo en esto, quiero compartir contigo varios ejemplos mas para que veas el patron que estoy viendo. Cuando termine escuchare tu punto de vista, te lo prometo. Estoy abierto a oir que me equivoco. Y si resulta que tengo razon, estoy aqui para ayudarte a arreglarlo. Y como siempre, usa tus palabras y no las del libro.",
    ],
    ("Sale de las lineas 289 a 322, bajo el rotulo GAUGE CRITICISM de la linea 289. ES LA PIEZA 12 DE "
     "LA FRONTERA DE cap_13. POR QUE ES PROCEDIMIENTO Y NO POSTURA, con D.27 delante: el propio "
     "libro dice en la linea 291 que la frase de medir la critica en el oido del otro era otra linea "
     "muy tuiteada del libro pero que en sus talleres quedo claro que no se explicaba sola, y "
     "entonces pone su propio INVENTARIO DE OBJETOS A OBSERVAR (lo que dice, su lenguaje corporal, "
     "su mirada) y su inventario de TRES RESPUESTAS con lo que hay que hacer con cada una (tristeza "
     "en la linea 299, enfado en la 303, no oirte en la 309), mas los guiones literales de las "
     "lineas 305, 315 y 321. Deja fichero: la critica ajustada y la emocion nombrada. Y NO ES UNA "
     "SERIE D.37: el texto no escribe cuantas respuestas hay, asi que ni el id ni el titulo llevan "
     "cifra. SU PAR CON ajustar_franqueza_oido_oyente Y CON manejar_enfado_persona_desafiada "
     "(cap_05 y cap_06), leido antes de que lo levante ninguna senial: MI VEREDICTO ES CONTINUA CON "
     "ARISTA en los dos y no REPITE, con los lados medidos. Aquellos entregan la franqueza ajustada "
     "al oido de cada persona y el enfado de una persona desafiada manejado; este entrega LA "
     "CONVERSACION AJUSTADA SOBRE LA MARCHA con el marco usado como brujula, con las tres respuestas "
     "nombradas una a una, el lema de escuchar, desafiar y comprometer, y el error de las "
     "consecuencias prematuras, que ninguno de los dos tiene. VA MARCADO COMO DISCUTIBLE EN EL "
     "REPORTE. LA CIFRA Y EL NOMBRE QUE NO VIAJAN: los actores contratados para los juegos de "
     "papeles de la linea 301 son el caso de la autora y no un encargo al lector, asi que se quedan "
     "en el caso, manual 3.5. RELECTURA DE FIDELIDAD D.30 EN EL ACTO, paso a paso contra su linea: "
     "32 pasos, 32 TRANSCRIPCION, 0 PUENTE. P1 de la linea 291; P2 y P3 de la linea 293; P4 y P5 de "
     "la linea 295; P6 a P8 de la linea 297; P9 y P10 de la linea 299; P11 de la linea 301; P12 y "
     "P13 de la linea 303; P14 a P16 de la linea 305; P17 a P19 de la linea 307; P20 y P21 de la "
     "linea 309; P22 de la linea 311; P23 a P25 de la linea 313; P26 a P28 de la linea 315; P29 a "
     "P31 de la linea 319; P32 de la linea 321. LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: "
     "cuantos ejemplares son varios, cuanto se espera antes de volver a la critica, y que se hace si "
     "la persona nombra una emocion distinta de la que ves. El libro pone las tres respuestas y no "
     "pone ninguna de las tres.")))

for d in NODOS:
    r = escribe(d)
    print('escrito %s  (%d pasos)' % (r, len(d['pasos_accionables'])))
