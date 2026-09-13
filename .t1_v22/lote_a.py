# -*- coding: utf-8 -*-
"""LOTE A de cap_11: las piezas P1 a P4. Se escriben y pasan la aduana en el acto."""
import json
import io
import os
import sys

sys.path.insert(0, '.')
from src import reglas_id

DEST = 'cuarentena/scott_radical_candor'
FUENTES = [{u"clave": u"scott_radical_candor", u"fecha": u"2026-09-12"}]

CANDIDATOS = []


def nodo(ident, titulo, largo, otros, activa, entrega, pasos, resumen, dominio=u"gestion_equipos"):
    CANDIDATOS.append({
        u"id": ident,
        u"titulo": titulo,
        u"denominaciones": {u"nombre_largo": largo,
                            u"otros_idiomas": [{u"idioma": u"ingles", u"termino": t} for t in otros],
                            u"sigla": u""},
        u"condiciones_activacion": activa,
        u"entregable_esperado": entrega,
        u"pasos_accionables": pasos,
        u"resumen_teorico": resumen,
        u"dominio": dominio,
        u"estado": u"vivo",
        u"fuentes": FUENTES,
        u"ids_alias": [],
        u"nodos_previos": [],
        u"nodos_siguientes": [],
    })


# ----------------------------------------------------------------- P1, L15 a L35
nodo(
 u"decidir_quien_comunica_cada_cuanto",
 u"Decidir quien necesita comunicarse con quien y cada cuanto, minimizando el coste de cada reunion",
 u"La cabeza del capitulo de resultados: la responsabilidad de decidir el mapa de comunicacion del "
 u"equipo, el coste que toda reunion trae, las tres cosas que se minimizan, y las herramientas que el "
 u"texto enumera una a una",
 [u"Things you can do to get stuff done together-faster", u"Get Stuff Done wheel"],
 u"Cuando te toca decidir que reuniones hay en tu equipo, quien va a cada una y cada cuanto, y quieres "
 u"que la comunicacion fluya sin que las reuniones se coman el tiempo de todos.",
 u"El mapa de quien se comunica con quien y cada cuanto, con cada reunion puesta con su duracion, su "
 u"frecuencia y el minimo de personas a las que hace falta que asistan.",
 [
  u"Asume como una de tus responsabilidades mas importantes para que todo siga moviendose sin roces: "
  u"decidir quien necesita comunicarse con quien y con que frecuencia.",
  u"Cuenta con lo que eso significa en la practica, y el texto lo dice en dos palabras: reuniones.",
  u"Cuenta tambien con que toda reunion viene con un coste significativo, que el texto nombra: el tiempo.",
  u"Minimiza por eso las tres cosas que el texto nombra una a una: la duracion, la frecuencia y el "
  u"numero de personas a las que hace falta que asistan.",
  u"Empieza por la que el texto llama la mas importante de todas estas reuniones: la reunion a solas con "
  u"cada persona que te reporta directamente.",
  u"Y ten delante las herramientas que el texto enumera para sacar cosas adelante juntos, que son las "
  u"reuniones a solas, las reuniones de equipo, el tiempo para pensar, las reuniones de gran debate, las "
  u"reuniones de gran decision, las reuniones generales, las zonas libres de reuniones, los tableros "
  u"kanban, pasear por la organizacion y ser consciente de la cultura.",
 ],
 u"UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_11.md, unidad Cap. 8, Results. Sale de las lineas "
 u"15 a 35. ES LA PIEZA P1 DE LA FRONTERA DE cap_11 Y ES LA CABEZA DEL CAPITULO. "
 u"POR QUE ES PROCEDIMIENTO Y NO ENTRADA, con D.27 delante: la linea 15 pone un mandato (decide who "
 u"needs to communicate with whom and how frequently) Y SU PROPIO INVENTARIO DE OBJETOS A MINIMIZAR "
 u"nombrados uno a uno (the duration, frequency and number of people required to attend), y las lineas "
 u"17 a 35 ponen el inventario de MEDIOS del capitulo entero, diez herramientas nombradas una a una. "
 u"Escribir los pasos es transcribir esos dos inventarios. "
 u"POR QUE NO ES UNA SERIE D.37 SINO D.29: el libro NO escribe la cuenta en ningun sitio. Enumera las "
 u"diez sin decir cuantas son, y EXTRACTOR.md 15.6 dice que si el texto solo enumera sin decir cuantas "
 u"esto NO es D.37 sino D.29, y la arista se declara igual pero con razon escrita que la sostenga. Las "
 u"aristas van declaradas en docs/loop/REPORTE.md de la vuelta 22. "
 u"UNA DISCREPANCIA DEL PROPIO LIBRO QUE DECLARO EN VEZ DE ARREGLARLA: el indice de la linea 29 dice "
 u"Meeting-Free Zones y el rotulo de la seccion que le corresponde, en la linea 223, dice EXECUTION "
 u"TIME. Transcribo el indice tal como esta en la linea 29 y dejo dicho aqui que el rotulo de la seccion "
 u"es otro. No elijo por el libro. "
 u"RELECTURA DE FIDELIDAD D.30 EN EL ACTO, paso a paso contra su linea: 6 pasos, 6 TRANSCRIPCION, 0 "
 u"PUENTE. P1 a P5 de la linea 15; P6 de las lineas 17 a 35. "
 u"LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: cuanto es demasiada duracion, cada cuanto es "
 u"demasiada frecuencia, cuantas personas son demasiadas, y en que orden se montan las diez "
 u"herramientas. El libro pone el mandato de minimizar y NO pone el umbral, asi que cualquier cifra que "
 u"yo escribiera ahi la escribiria yo.",
)

# ----------------------------------------------------------------- P2, L37 a L65
nodo(
 u"montar_reuniones_solas_mentalidad_frecuencia",
 u"Montar tus reuniones a solas con cada persona a tu cargo: la mentalidad, la frecuencia, presentarte "
 u"siempre y la agenda puesta por quien te reporta",
 u"Las cuatro cosas que el texto pone para sacar el maximo de las reuniones a solas: la mentalidad de "
 u"comida o cafe en vez de reunion, la frecuencia atada al cuello de botella del jefe, no cancelarlas "
 u"nunca, y la agenda en manos de quien te reporta",
 [u"1:1 CONVERSATIONS", u"Employees set the agenda, you listen and help them clarify",
  u"Mind-set", u"Frequency", u"Show up!", u"Your direct report's agenda, not yours"],
 u"Cuando vas a montar o a arreglar las reuniones a solas con las personas que te reportan "
 u"directamente, y quieres que salga de ellas lo que el texto dice que son: tu mejor oportunidad de "
 u"escuchar de verdad.",
 u"Las reuniones a solas puestas con su frecuencia, no canceladas, con la agenda puesta por quien te "
 u"reporta, y con la direccion en la que esa persona quiere ir y lo que se lo bloquea entendidos por ti.",
 [
  u"Trata las reuniones a solas como tus reuniones de obligado cumplimiento: el texto dice que son tu "
  u"mejor oportunidad de escuchar, escuchar de verdad, a la gente de tu equipo, para asegurarte de que "
  u"entiendes su punto de vista sobre lo que funciona y lo que no.",
  u"Usalas tambien para llegar a conocer a las personas a tu cargo, que es como subes en la dimension de "
  u"importarte personalmente del marco de la franqueza radical.",
  u"No las uses para soltar toda la critica que llevas guardada: el texto dice que eso va en las "
  u"conversaciones improvisadas de dos a tres minutos que ya estas teniendo.",
  u"Ten claro cual es el proposito, que el texto escribe entero: escuchar y aclarar, o sea entender hacia "
  u"que direccion quiere ir cada persona que trabaja para ti y que se lo esta bloqueando.",
  u"Cambia primero tu mentalidad, porque el texto dice que es lo que mas decide como salen: deja de "
  u"pensar en ellas como reuniones y tratalas como si estuvieras comiendo o tomando un cafe con alguien a "
  u"quien tienes ganas de conocer mejor.",
  u"Si programarlas sobre una comida ayuda, hazlas comidas periodicas.",
  u"Si a ti y a la persona os gusta andar y hay un buen sitio para pasear cerca de la oficina, hazlas "
  u"paseando.",
  u"Ajusta la hora a tu energia: si eres de maniana, ponlas por la maniana; si eres de los que se "
  u"desinflan a las dos de la tarde, no las pongas a las dos de la tarde.",
  u"Pero no seas un cretino con eso, que es como el texto lo dice: si a ti te gusta levantarte a las "
  u"cinco e ir al gimnasio, no esperes que la gente que trabaja para ti quede alli contigo.",
  u"Pon la frecuencia contando tu propio limite, porque el texto dice que las reuniones a solas deben ser "
  u"el cuello de botella natural que decide cuantas personas puede tener a su cargo un jefe: el suyo son "
  u"cincuenta minutos a la semana con cada persona y no mas de unas cinco horas de reuniones a solas en "
  u"el calendario, porque escuchar es trabajo duro y no hay capacidad infinita para ello.",
  u"Si la gente esta en remoto, ten esas conversaciones por videoconferencia y complementalas con "
  u"comprobaciones rapidas mas frecuentes.",
  u"Si tienes diez personas a tu cargo, pasa las reuniones a solas a veinticinco minutos a la semana.",
  u"Si tienes veinte y no hay nada que puedas hacer al respecto, ponlas de veinticinco minutos cada dos "
  u"semanas con cada persona.",
  u"Y mira ademas si puedes crear oportunidades de liderazgo para la gente que trabaja para ti y reducir "
  u"el numero de personas que te reportan.",
  u"Para evitar que las reuniones se multipliquen, usa el tiempo de la reunion a solas para tener las "
  u"conversaciones de carrera y, si toca, para hacer las evaluaciones formales de desempenio.",
  u"Presentate: el texto dice que es probablemente el consejo mas importante de todos para las reuniones "
  u"a solas.",
  u"Cuenta con la cuenta que el texto hace, para que no te pille: entre viajes, las veces que "
  u"inevitablemente caeras enfermo y alguna vacacion, cancelaras al menos dos o tres de cada trece "
  u"programadas; y si ademas reservas algunas para las especiales, te quedan siete u ocho normales por "
  u"trimestre, o tres o cuatro si tienes mas de diez personas y las haces cada dos semanas.",
  u"Asi que no canceles tus reuniones a solas, se incendie lo que se incendie en tu dia.",
  u"Deja que la agenda la ponga y la posea la persona que te reporta, y no tu: el texto dice que asi son "
  u"mas productivas, porque te dejan escuchar lo que a ellos les importa.",
  u"Pon aun asi las expectativas basicas sobre la agenda y sobre como llega: si quieres una agenda "
  u"estructurada dilo, si la quieres por adelantado dilo, y si no la vas a mirar por adelantado ponlo "
  u"claro tambien.",
  u"Di tambien si te vale que lleguen con unos puntos apuntados en una servilleta o si prefieres que la "
  u"lleven en un documento compartido al que se pueda volver despues.",
  u"Y haz tu propio trabajo, que el texto define en una linea: pedir cuentas a quien llega sin preparar, "
  u"o decidir que de vez en cuando esta bien tener una reunion a solas sin agenda.",
 ],
 u"UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_11.md, unidad Cap. 8, Results. Sale de las lineas "
 u"37 a 65, bajo el rotulo 1:1 CONVERSATIONS y sus cuatro rotulos interiores Mind-set, Frequency, Show "
 u"up! y Your direct report's agenda, not yours. ES LA PIEZA P2 DE LA FRONTERA DE cap_11. "
 u"POR QUE LOS CUATRO ROTULOS VAN EN UN SOLO NODO Y NO EN CUATRO, con la vara de la ACTA 20 seccion 4.1 "
 u"y la confirmacion de la ACTA 21 seccion 4.2 delante: la linea 45 los encadena ella misma con una sola "
 u"frase (Here are a few things you can do to make sure you and each of your reports are getting the "
 u"most out of these 1:1 meetings), y los cuatro comparten UNA condicion de activacion (vas a montar tus "
 u"reuniones a solas) y UN entregable (las reuniones puestas y no canceladas, con su agenda). Es la "
 u"misma forma que armar_plan_anual_crecimiento_equipo en cap_10. "
 u"Y EL LIBRO NO ESCRIBE LA CUENTA: dice a few things, no cuatro, asi que ni el titulo ni el id llevan "
 u"numero y esto NO es una serie D.37. "
 u"EL CASO DE SHERYL SANDBERG, DE LA LINEA 43, NO VIAJA A NINGUN PASO: es el ejemplar de un problema "
 u"resuelto en una reunion a solas (viajar a diez ciudades contra quedarse embarazada, resuelto trayendo "
 u"al equipo en vez de yendo). Lo que SI viaja de la linea 43 es su primera frase, que es doctrina y no "
 u"caso: el proposito de una reunion a solas es escuchar y aclarar. Manual 3.5. "
 u"RELECTURA DE FIDELIDAD D.30 EN EL ACTO, paso a paso contra su linea: 22 pasos, 22 TRANSCRIPCION, 0 "
 u"PUENTE. P1 a P3 de la linea 41; P4 de la linea 43; P5 a P9 de la linea 49; P10 y P11 de la linea 53; "
 u"P12 a P14 de la linea 55; P15 de la linea 57; P16 a P18 de la linea 61; P19 a P22 de la linea 65. "
 u"LAS CIFRAS QUE LLEVAN LOS PASOS SON TODAS DEL LIBRO Y LAS COMPROBE UNA A UNA, que es la especie que "
 u"mi propia vuelta 21 se cazo 22 veces: cincuenta minutos, cinco horas, cinco personas, veinticinco "
 u"minutos, diez personas, veinte personas, dos o tres de cada trece, siete u ocho por trimestre y tres "
 u"o cuatro por trimestre estan todas escritas en las lineas 53, 55 y 61. "
 u"LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: como se recupera una reunion a solas cancelada, que "
 u"se hace si quien te reporta no quiere poner agenda nunca, y cada cuanto se revisa si la frecuencia "
 u"elegida sigue valiendo.",
)

# ----------------------------------------------------------------- P3, L67 a L97
nodo(
 u"preguntar_seguimiento_hallar_huecos",
 u"Preguntar en la reunion a solas las preguntas de seguimiento que ensenian los huecos entre lo que la "
 u"persona hace, lo que cree que deberia hacer y lo que quiere hacer",
 u"El repertorio literal de preguntas de seguimiento de la reunion a solas, con las tres que abren, las "
 u"seis del trabajo que se quiere y no se quiere, las tres de los equipos de los que dependes, y la nota "
 u"del texto sobre para que sirve la ultima",
 [u"Some good follow-up questions"],
 u"Cuando estas dentro de una reunion a solas y quieres ensenar que escuchas, que te importa y que "
 u"quieres ayudar, y ademas sacar los huecos entre lo que la persona hace, lo que cree que deberia hacer "
 u"y lo que quiere hacer.",
 u"Los huecos de esa persona identificados con sus palabras, y el asunto de otro equipo planteado por "
 u"ella misma a ese equipo en vez de resuelto por ti.",
 [
  u"Haz estas preguntas de seguimiento con el doble proposito que el texto les pone: ensenar no solo que "
  u"estas escuchando sino que te importa y quieres ayudar, e identificar los huecos entre lo que la gente "
  u"hace, lo que cree que deberia hacer y lo que quiere hacer.",
  u"Pregunta: por que?",
  u"Pregunta: como puedo ayudar?",
  u"Pregunta: que puedo hacer, o dejar de hacer, que te facilitaria esto?",
  u"Pregunta: que es lo que te desvela por la noche?",
  u"Pregunta: en que estas trabajando en lo que no quieres trabajar?",
  u"Pregunta: no quieres trabajar en ello porque no te interesa o porque crees que no es importante?",
  u"Pregunta: que puedes hacer para dejar de trabajar en ello?",
  u"Pregunta: en que no estas trabajando en lo que si quieres trabajar?",
  u"Pregunta: por que no estas trabajando en ello?",
  u"Pregunta: que puedes hacer para empezar a trabajar en ello?",
  u"Pregunta: como te sientes respecto a las prioridades de los equipos de los que dependes?",
  u"Pregunta: en que estan trabajando ellos que parezca poco importante o incluso contraproducente?",
  u"Pregunta: que es lo que no estan haciendo y a ti te gustaria que hicieran?",
  u"Pregunta: has hablado directamente con esos otros equipos de lo que te preocupa? Y si no, por que no?",
  u"Y ten presente lo que el texto marca como nota importante sobre esa ultima: el objetivo aqui es "
  u"animar a la gente a plantear el asunto directamente entre ellos, no resolverles el problema tu.",
 ],
 u"UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_11.md, unidad Cap. 8, Results. Sale de las lineas "
 u"67 a 97, bajo el rotulo Some good follow-up questions, dentro de la seccion 1:1 CONVERSATIONS. ES LA "
 u"PIEZA P3 DE LA FRONTERA DE cap_11. "
 u"POR QUE ES PROCEDIMIENTO Y NO POSTURA, con D.27 delante y en su caso mas facil: el libro pone su "
 u"inventario ENTERO Y LITERAL, catorce preguntas escritas una a una entre las lineas 71 y 97, mas su "
 u"proposito escrito en la linea 69 y su nota de uso en la 97. Escribir los pasos aqui es transcribir, y "
 u"no se inventa nada. "
 u"POR QUE ES NODO PROPIO Y NO PARTE DE montar_reuniones_solas_mentalidad_frecuencia: su par es otro. "
 u"Aquel se dispara cuando vas a MONTAR las reuniones y entrega las reuniones puestas; este se dispara "
 u"cuando ya estas DENTRO de una y entrega los huecos identificados. La linea 69 escribe ese entregable "
 u"con sus propias palabras (to identify the gaps between what people are doing, what they think they "
 u"ought to be doing, and what they want to be doing). "
 u"LAS PREGUNTAS VAN EN CASTELLANO Y EN SU ORDEN, y la unica que lleva coletilla es la ultima, porque el "
 u"propio texto le cuelga una nota que empieza con Important note. "
 u"EL REENVIO DE LA LINEA 97 A Prevent Backstabbing DEL CAPITULO SEIS NO SE TRANSCRIBE COMO PASO: es un "
 u"remite a otro sitio del libro, que EXTRACTOR.md 9 llama el caso literal de nombrar el procedimiento "
 u"de otro. Ese procedimiento ya vive en la bandeja como impedir_punialadas_espalda_equipo, y la arista "
 u"va declarada en docs/loop/REPORTE.md de la vuelta 22. "
 u"RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 16 pasos, 16 TRANSCRIPCION, 0 PUENTE. P1 de la linea 69; P2 a "
 u"P15 de las lineas 71 a 97, una por linea; P16 de la linea 97. "
 u"LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: cuantas de las catorce se hacen en una misma reunion, "
 u"en que orden, y que se hace con el hueco una vez identificado. El libro da las preguntas y no da el "
 u"despues.",
)

# ----------------------------------------------------------------- P4, L99 a L113
nodo(
 u"nutrir_ideas_nuevas_reunion_solas",
 u"Nutrir en la reunion a solas las ideas nuevas, que son fragiles, empujando a quien la trae a "
 u"explicarla mas claro y para quien la tiene que oir",
 u"Las seis preguntas literales con que se empuja una idea nueva a ser mas clara dentro de la reunion a "
 u"solas, con la reunion tratada como sitio seguro antes del empujon del debate",
 [u"Encourage new ideas in the 1:1.", u"new ideas are fragile"],
 u"Cuando alguien de tu equipo trae una idea nueva a su reunion a solas contigo y todavia no esta clara "
 u"ni lista para llevarla al equipo mas amplio.",
 u"La idea explicada con la claridad suficiente para llevarla al equipo mas amplio, y explicada de la "
 u"manera que entiende cada persona a la que hay que comunicarsela.",
 [
  u"Ten en la cabeza, antes de entrar a una reunion a solas, la frase de Jony Ive que el texto cita: las "
  u"ideas nuevas son fragiles.",
  u"Trata esa reunion como un sitio seguro donde la gente pueda nutrir ideas nuevas antes de someterlas "
  u"al empujon y el revolcon del debate.",
  u"Ayudales con las dos cosas que el texto nombra: a aclarar lo que ellos mismos piensan de la idea, y a "
  u"aclarar su comprension de las personas a las que tienen que comunicarsela.",
  u"Cuenta con que la misma idea puede necesitar describirse de una manera para un ingeniero y de otra "
  u"para un comercial.",
  u"Pregunta: que necesitas para desarrollar mas esa idea, de manera que este lista para discutirla con "
  u"el equipo mas amplio? Como puedo ayudarte?",
  u"Pregunta: creo que tienes algo entre manos, pero todavia no me queda claro. Puedes intentar "
  u"explicarmelo otra vez?",
  u"Pregunta: vamos a pelearnos un poco mas con esto, te parece?",
  u"Pregunta: entiendo lo que quieres decir, pero no creo que los demas lo entiendan. Como puedes "
  u"explicarlo para que a ellos les resulte mas facil de entender?",
  u"Pregunta: no creo que fulano vaya a entender esto. Puedes explicarlo otra vez para que quede mas "
  u"claro especificamente para el?",
  u"Pregunta: el problema es de verdad que ellos son demasiado tontos para entenderlo, o es que tu no lo "
  u"estas explicando con la claridad suficiente?",
 ],
 u"UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_11.md, unidad Cap. 8, Results. Sale de las lineas "
 u"99 a 113, bajo el rotulo Encourage new ideas in the 1:1, dentro de la seccion 1:1 CONVERSATIONS. ES "
 u"LA PIEZA P4 DE LA FRONTERA DE cap_11. "
 u"POR QUE ES PROCEDIMIENTO, con D.27 delante: la linea 101 pone el proposito y las lineas 103 a 113 "
 u"ponen SEIS preguntas literales, una por linea, que son medios nombrados uno a uno. "
 u"EL PAR QUE HAY QUE DECLARAR, Y LO DECLARO YO ANTES DE QUE LO LEVANTE NADIE: "
 u"crear_espacio_seguro_madurar_ideas_nuevas, que sale de cap_07 lineas 177 a 195, es la MADRE de este "
 u"nodo, y sus pasos 12, 13 y 14 dicen ya trata tus reuniones semanales a solas como ese sitio seguro. "
 u"MI VEREDICTO ES CONTINUA CON ARISTA Y NO REPITE, y la razon va con los dos lados medidos: la madre "
 u"trae procedimiento que este no tiene (no pidas tres soluciones y una recomendacion, la tecnica del "
 u"plussing de Pixar, la reunion previa donde las ideas se afilan, y la advertencia de que una lluvia de "
 u"ideas no es una conversacion sin negativas), y este trae procedimiento que la madre no tiene (las "
 u"SEIS preguntas literales, la cita de Jony Ive, y la regla de describir la idea distinto para un "
 u"ingeniero y para un comercial). Los dos lados tienen procedimiento fuera del solape, y la vara de "
 u"manual 4 no tiene bascula: CONTINUA. Va marcado como discutible en el reporte de la vuelta 22. "
 u"RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 10 pasos, 10 TRANSCRIPCION, 0 PUENTE. P1 a P4 de la linea "
 u"101; P5 a P10 de las lineas 103 a 113, una por linea. "
 u"LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: cuando se da una idea por lista para el equipo mas "
 u"amplio, quien decide que ya esta clara, y que se hace si despues de las seis preguntas sigue sin "
 u"estarlo.",
)

# ------------------------------------------------------------------- ESCRITURA
for d in CANDIDATOS:
    fallos = reglas_id.validar(d['id'])
    ruta = os.path.join(DEST, d['id'] + '.json')
    print('%-48s reglas_id: %-28s pasos: %2d  %s'
          % (d['id'], fallos or 'OK', len(d['pasos_accionables']),
             'YA EXISTIA' if os.path.exists(ruta) else 'nuevo'))
    if fallos:
        raise SystemExit('EL ID NO PASA LAS REGLAS. No se escribe nada.')
    with io.open(ruta, 'w', encoding='utf-8') as f:
        f.write(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True))
        f.write(u'\n')
print('')
print('escritos %d candidatos en %s' % (len(CANDIDATOS), DEST))
