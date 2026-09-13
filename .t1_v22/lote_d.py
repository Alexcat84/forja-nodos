# -*- coding: utf-8 -*-
"""LOTE D de cap_11: las piezas P13 a P16."""
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
        u"id": ident, u"titulo": titulo,
        u"denominaciones": {u"nombre_largo": largo,
                            u"otros_idiomas": [{u"idioma": u"ingles", u"termino": t} for t in otros],
                            u"sigla": u""},
        u"condiciones_activacion": activa, u"entregable_esperado": entrega,
        u"pasos_accionables": pasos, u"resumen_teorico": resumen, u"dominio": dominio,
        u"estado": u"vivo", u"fuentes": FUENTES, u"ids_alias": [],
        u"nodos_previos": [], u"nodos_siguientes": [],
    })


# --------------------------------------------------------------- P13, L235 a L249
nodo(
 u"montar_tablero_kanban_medir_actividades",
 u"Montar un tablero kanban de tres columnas para hacer visibles las actividades y los flujos de "
 u"trabajo, y medir la actividad y no solo el resultado",
 u"El tablero kanban con sus tres columnas y sus notas adhesivas de color por persona o equipo, y las "
 u"cinco cosas que el texto dice que consigue medir la actividad y ensenarla en publico",
 [u"KANBAN BOARDS", u"Make activity and workflows visible", u"To Do, In Progress, and Done"],
 u"Cuando no ves donde esta el cuello de botella de tu equipo, o cuando por los resultados solos no "
 u"puedes distinguir quien esta haciendo que las cosas pasen y quien va subido al carro.",
 u"Un tablero con las tareas de cada persona o equipo colocadas en las tres columnas y movidas por ellos "
 u"mismos, con el cuello de botella a la vista de todos y la actividad medida ademas del resultado.",
 [
  u"Monta el tablero en su forma mas simple, que es la que el texto describe: pon un tablero con tres "
  u"columnas, por hacer, en curso y hecho.",
  u"Compra un monton de notas adhesivas de colores distintos, y que los colores representen a las "
  u"distintas personas o equipos.",
  u"Haz que cada cual escriba sus tareas en su color de nota y las vaya moviendo entre por hacer, en "
  u"curso y hecho.",
  u"Usalo para lo que el texto dice que sirve al momento: ver rapidamente quien es el cuello de botella.",
  u"Distingue el tablero del cuadro de mando, porque el texto dice que no son lo mismo: el tablero se "
  u"centra en las actividades y en el trabajo en curso, y por eso da tiempo al equipo a detectar y "
  u"resolver problemas antes de que danien los resultados.",
  u"Cuenta con lo primero que consigue hacer visible el avance: da mas autonomia al equipo y no menos, "
  u"porque cuando todos ven donde estan los cuellos de botella los recursos fluyen solos hacia donde mas "
  u"falta hacen, sin que la direccion intervenga; y quien va adelantado se motiva para ir a ayudar a quien "
  u"se ha quedado atras, porque sabe que si esa tarea no sale, su propio trabajo no vale para nada o se "
  u"retrasa.",
  u"Cuenta con lo segundo: cuando un negocio va muy bien, por los resultados solos cuesta distinguir "
  u"quien va subido al carro y quien esta haciendo de verdad que las cosas pasen; y cuando la economia se "
  u"hunde por factores que nadie controla, si solo mides resultados no sabes quien esta achicando agua y "
  u"quien esta entrando en panico o empeorando las cosas.",
  u"Cuenta con lo tercero: medir actividades y visualizar flujos de trabajo os empuja a ti y a tu equipo "
  u"a entender de verdad como lo que haceis empuja o no empuja el exito.",
  u"Cuenta con lo cuarto: medir actividades crea mas respeto entre equipos, porque el texto dice que "
  u"sorprende lo rapido que un equipo da por hecho que otro esta sentado sin hacer nada y cuanto "
  u"resentimiento se acumula con eso; cuando se ve en un tablero lo que la gente hace, el respeto fluye "
  u"con bastante naturalidad.",
  u"Cuenta con lo quinto: medir actividades y ensenarlas publicamente tiende a llevar a evaluaciones y "
  u"ascensos que premian de forma mas consistente a los que mas rinden y son menos propensos a los sesgos "
  u"que nos acechan a todos, porque cuando queda claro para todos que es lo que empuja el exito es menos "
  u"probable que el sesgo se cuele en las decisiones de contratar, evaluar y ascender.",
 ],
 u"UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_11.md, unidad Cap. 8, Results. Sale de las lineas "
 u"235 a 249, bajo el rotulo KANBAN BOARDS. ES LA PIEZA P13 DE LA FRONTERA DE cap_11. "
 u"POR QUE ES PROCEDIMIENTO, con D.27 delante: la linea 239 pone el INVENTARIO DE MEDIOS literal y "
 u"completo, el tablero, las TRES columnas con su nombre, las notas adhesivas de colores y lo que cada "
 u"color representa, y el acto de moverlas. Transcribir eso no inventa nada. "
 u"kanban SE ESCRIBE TAL CUAL PORQUE ESTA EN LA LISTA BLANCA DE EXTRACTOR.md 15.1, entre los prestamos "
 u"asentados. No se traduce y no se caza. "
 u"EL ORIGEN HISTORICO DE LA LINEA 239 (el ingeniero industrial de Toyota que desarrollo el kanban como "
 u"sistema de programacion para la cadena de suministro) NO VIAJA A NINGUN PASO: es atribucion, no "
 u"procedimiento, y por principio 5 y 8 del manual una atribucion va en el campo atribuciones con autor, "
 u"fuente y fecha de corte. Aqui NO se escribe como atribucion porque el texto no da fecha de corte ni "
 u"cifra, y una atribucion sin eso es media cifra. Se deja dicho aqui y no se inventa el resto. "
 u"LOS DOS CASOS NOMBRADOS DE LAS LINEAS 245 Y 249 (el equipo de ventas que atendia llamadas en vez de "
 u"buscar clientes grandes, y el jefe de analisis que subio del puesto quince al primero) NO VIAJAN A "
 u"NINGUN PASO, ni sus cifras ni sus anios ni el nombre de sus empresas. Manual 3.5. Lo que viaja es la "
 u"doctrina que ilustran, y esa esta en las lineas 243, 245, 247 y 249. "
 u"POR QUE LOS CINCO cuenta con SI SON PASOS Y NO METAS SUELTAS: cada uno es lo que el texto dice que "
 u"pasa al hacerlo, escrito por el como another reason why, also y tends to. La restriccion 1 de D.27 "
 u"excluye que un inventario de fines SOSTENGA un nodo; aqui el nodo lo sostiene el inventario de medios "
 u"de la linea 239, y los cinco efectos entran detras como transcripcion. "
 u"RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 10 pasos, 10 TRANSCRIPCION, 0 PUENTE. P1 a P5 de la linea "
 u"239; P6 de la 241; P7 de la 243; P8 de la 245; P9 de la 247; P10 de la 249. "
 u"LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: cada cuanto se revisa el tablero, quien lo mantiene, "
 u"que actividades se miden y cuales no, y donde se cuelga.",
)

# --------------------------------------------------------------- P14, L251 a L269
nodo(
 u"pasear_organizacion_hallar_problemas_pequenios",
 u"Pasear una hora a la semana por la organizacion para enterarte de los problemas pequenios antes de "
 u"que se vuelvan grandes",
 u"La hora semanal de pasear como manera de escuchar hondo cuando eres jefe de jefes y no puedes tener "
 u"reuniones a solas con cientos de personas, con las tres cosas para las que sirve enterarse de los "
 u"problemas pequenios",
 [u"WALK AROUND", u"Learn about small problems to prevent big ones",
  u"Management by walking around"],
 u"Cuando eres jefe de jefes y escuchar hondo en tu organizacion se te ha vuelto imposible: no puedes "
 u"tener reuniones a solas con cientos o miles de personas, y si pones horas de consulta te llegan los "
 u"mismos tres quejicas semana tras semana.",
 u"Una hora a la semana de paseo puesta en tu calendario, con problemas pequenios encontrados, alguno "
 u"arreglado por ti misma en el momento, y la gente con la que hablaste elegida entre la que llevabas "
 u"tiempo sin ver.",
 [
  u"Parte de la dificultad que el texto mide antes de dar el remedio: escuchar a quienes te reportan "
  u"directamente es relativamente sencillo aunque lleve tiempo y disciplina, pero si eres jefe de jefes "
  u"escuchar hondo en tu organizacion es mucho mas dificil, porque no puedes escuchar a todo el mundo ni "
  u"tener reuniones a solas con cientos o miles de personas, y las horas de consulta te traen a los "
  u"mismos tres quejicas semana tras semana.",
  u"Agenda una hora a la semana de tiempo para pasear.",
  u"Cuenta con que no es un invento nuevo: el texto lo llama una tecnica probada y contrastada, la "
  u"gestion paseando, y dice que no tiene ninguna complicacion hacerlo.",
  u"Fijate en las cosas en las que no te fijas cuando estas enterrado en el trabajo en tu mesa o "
  u"corriendo con la cabeza gacha de una reunion a la siguiente.",
  u"Preguntale a la gente que te llame la atencion, e idealmente a gente con la que hace tiempo que no "
  u"hablas, en que estan trabajando.",
  u"Encuentra algunos problemas pequenios y tratalos como el texto dice, como el universo dentro de un "
  u"grano de arena.",
  u"Cuenta con lo primero para lo que sirve ser consciente de esos problemas pequenios: te ayudan a "
  u"encontrar el diablo en los detalles. Demasiadas veces el jefe es el ultimo en enterarse de que algo "
  u"va mal, y el texto dice que la razon no suele ser que la gente esconda los problemas a proposito, "
  u"sino que solo quieren traerte las cosas importantes, y un problema puede ser mas importante de lo que "
  u"ellos creen.",
  u"Cuenta con lo segundo: ser consciente de los problemas pequenios y quiza incluso arremangarte y "
  u"arreglarlos tu misma es la mejor manera de matar la mentalidad del esto no es mi trabajo o, peor, la "
  u"del esto esta por debajo de mi. Si nada esta por debajo de tu atencion, los demas tambien prestaran "
  u"atencion a los detalles.",
  u"Cuenta con lo tercero: cuando demuestras que te importan las cosas pequenias que contribuyen a la "
  u"felicidad del cliente o a la calidad de vida de tu equipo, de repente a todo el mundo le importan "
  u"mas, y algunas de las cosas grandes empiezan a funcionar mejor tambien.",
 ],
 u"UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_11.md, unidad Cap. 8, Results. Sale de las lineas "
 u"251 a 269, bajo el rotulo WALK AROUND. ES LA PIEZA P14 DE LA FRONTERA DE cap_11. "
 u"POR QUE ES PROCEDIMIENTO, con D.27 delante: la linea 259 pone el acto con su periodo ESCRITO POR EL "
 u"LIBRO (Schedule an hour a week of walking-around time), y la linea 261 pone el inventario de actos "
 u"dentro del paseo, nombrados uno a uno (fijarse en lo que no se ve desde la mesa, preguntar a quien te "
 u"llame la atencion y mejor si hace tiempo que no hablas con esa persona, encontrar problemas "
 u"pequenios). La hora semanal NO es un puente del periodo: esta escrita, y por eso se transcribe. "
 u"EL CASO DEL CONSEJERO DELEGADO QUE PASEABA, Y EL DE LOS PLATOS SUCIOS DE LA COCINA DE LA LINEA 269, NO "
 u"VIAJAN A NINGUN PASO: manual 3.5, el caso no es la casa. Su nombre no aparece en ningun paso ni en el "
 u"entregable. Lo que viaja de ese caso es lo que ya esta en el paso 8, arremangarse y arreglar el "
 u"problema uno mismo, que el texto escribe como doctrina en la linea 265 y no solo dentro del caso. "
 u"POR QUE LOS TRES cuenta con NO SON UNA SERIE D.37: la linea 261 dice can be useful in several ways y "
 u"NO escribe cuanta, y ademas son fines, que la restriccion 1 de D.27 excluye. El libro los ordena con "
 u"First, Second, Third, pero enumerar sin decir cuantas es D.29 y no D.37 (EXTRACTOR.md 15.6). Aqui ni "
 u"siquiera hace falta arista: no existen como nodos aparte. "
 u"EL PAR QUE DECLARO: crear_cultura_escucha_equipo, de cap_07, es el paso LISTEN de la rueda, y pasear "
 u"es una herramienta suya para escuchar hondo. Arista D.29 declarada en el reporte de la vuelta 22. "
 u"RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 9 pasos, 9 TRANSCRIPCION, 0 PUENTE. P1 de la linea 255; P2 y "
 u"P3 de la 259; P4 a P6 de la 261; P7 de la 263; P8 de la 265; P9 de la 267. "
 u"LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: por donde se pasea, que dia, que se hace con el "
 u"problema pequenio que no puedes arreglar tu, y a quien se le cuenta lo que encontraste.",
)

# ------------------------------------------ P15, L271 a L299 mas L307 a L333
nodo(
 u"recorrer_rueda_conscientemente_cultura_equipo",
 u"Recorrer conscientemente los pasos de la rueda de hacer cosas sobre tu propia cultura, mirando la "
 u"conducta y no el caracter",
 u"La cultura del equipo trabajada por los pasos de la rueda de hacer cosas: bajo el microscopio, "
 u"aclarando lo que comunicas aunque creas que no dices nada, persuadiendo por los detalles pequenios, "
 u"ejecutando con actos pequenios, aprendiendo de lo que pasa y escuchando hasta que ya no vaya de ti",
 [u"BE CONSCIOUS OF CULTURE",
  u"Everyone is watching you, but that doesn't mean it's all about you",
  u"People are listening. Like it or not, you're under the microscope",
  u"Clarify. Be vigilant about clarifying what you are communicating",
  u"Persuade. Pay attention to the small things",
  u"Execute: Action should reflect your culture"],
 u"Cuando notas que la cultura de tu equipo refleja tu personalidad mas de lo que tu habrias elegido, y "
 u"quieres influir en ella a sabiendas en vez de dejar que pase.",
 u"Los pasos de la rueda de hacer cosas recorridos a sabiendas sobre tu propia cultura, con tus propias "
 u"conductas revisadas contra la cultura que dices querer y con lo que aprendiste de lo que salio mal "
 u"convertido en un cambio.",
 [
  u"Parte de lo que el texto mide: la cultura de un equipo tiene un impacto enorme en sus resultados, y "
  u"la personalidad de quien dirige tiene un impacto enorme en la cultura del equipo. Quien eres tu como "
  u"ser humano impacta enormemente en la cultura de tu equipo.",
  u"Y parte tambien de la salida que el texto da, que es la que evita que eso te paralice: no va solo de "
  u"ti. Igual que en tus evaluaciones de otros, centrate en la conducta y no en el caracter, en los actos "
  u"y no en las esencias.",
  u"Pide guia con regularidad y de verdad, porque el texto dice que asi las cualidades tuyas mas "
  u"flagrantes saldran inevitablemente a la luz.",
  u"E influye en tu cultura recorriendo a sabiendas los pasos de la rueda de hacer cosas, que es lo que "
  u"el texto dice que hace el resto del trabajo.",
  u"Escucha contando con que estas bajo el microscopio: cuando te vuelves jefe la gente te escucha de una "
  u"forma intensa que no habias vivido antes, y atribuye significado, a veces acertado y a veces no, a lo "
  u"que dices, a la ropa que llevas y al coche que conduces.",
  u"Cuenta con lo que el texto dice que pasa a menudo: dices o haces algo esperando que se lo tomen a la "
  u"ligera, y en realidad te has movido mucho mas alla en el eje de desafiar directamente de lo que "
  u"pretendias.",
  u"Aclara lo que estas comunicando, y se vigilante con ello incluso cuando crees que no estas diciendo "
  u"nada, dado el nivel de escrutinio bajo el que estas.",
  u"Comprueba para eso si tus propias conductas cuadran con la cultura que estas empujando, que es la "
  u"prueba que el texto pone con su propio ejemplo: una manera de aparcar descuidada cuadraba con la "
  u"cultura de pedir perdon y no permiso que ella empujaba, y si hubiera estado creando una cultura de "
  u"medir dos veces y cortar una, habria tenido al menos que dar una explicacion de su manera de aparcar "
  u"y probablemente habria tenido que corregirla.",
  u"Persuade prestando atencion a las cosas pequenias, porque el texto dice que eso puede tener un gran "
  u"impacto en persuadir a la gente de que tu cultura merece entenderse y adaptarse a ella.",
  u"Cuenta con que el entorno de la oficina es parte de marcar el tono y la cultura, y con que no hace "
  u"falta un presupuesto grande: aunque no puedas permitirte esa clase de dispendios, si puedes "
  u"asegurarte de que el cafe de la cocina sea el que a la gente le gusta beber, y de ofrecer tambien "
  u"unas bolsitas de te verde.",
  u"Elige a sabiendas el entorno que quieres, porque el texto dice que las elecciones pequenias que hagas "
  u"persuadiran a la gente de actuar de acuerdo con la cultura que quieres construir con tu equipo: un "
  u"entorno ordenado y bien iluminado, o un entorno frenetico con las cosas por todas partes.",
  u"Ejecuta contando con que un acto pequenio tuyo puede impactar la cultura de tu equipo incluso cuando "
  u"tu ya no estes, que es lo que el texto dice que le sorprendio.",
  u"Aprende de lo que pasa: cuando eres el jefe y pasa algo, es tu responsabilidad aprender de ello y "
  u"hacer un cambio; si no lo haces, creas una cultura que no aprende de sus errores.",
  u"Y escucha hasta el final de la rueda, con la senial que el texto da para saber que lo has conseguido: "
  u"una cultura fuerte se replica sola, y sabras que has tenido exito cuando de verdad ya no vaya de ti.",
 ],
 u"UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_11.md, unidad Cap. 8, Results. Sale de las lineas "
 u"271 a 299 y de las lineas 307 a 333, bajo el rotulo BE CONSCIOUS OF CULTURE y sus rotulos interiores. "
 u"ES LA PIEZA P15 DE LA FRONTERA DE cap_11, Y SU TRAMO ES NO CONTIGUO: entre sus dos mitades viven las "
 u"lineas 301 a 305, que son el rotulo Debate and decide explicitly y salen en su propio nodo, "
 u"debatir_decidir_asuntos_cultura_evitar_delegar. Lo digo aqui para que la frontera se pueda comprobar. "
 u"POR QUE ES PROCEDIMIENTO Y NO POSTURA, Y ES DONDE MAS CERCA HE ESTADO DE ESCRIBIR UNA POSTURA EN TODO "
 u"EL CAPITULO, con D.27 delante: lo que lo sostiene NO son las lineas 275 a 279, que son diagnostico, "
 u"sino que el libro pone SU PROPIO INVENTARIO DE ETAPAS, los pasos de la rueda de hacer cosas nombrados "
 u"uno a uno como rotulos (escuchar en la linea 283, aclarar en la 295, persuadir en la 307, ejecutar en "
 u"la 315, aprender en la 321 y escuchar otra vez en la 327), y la linea 281 escribe el mandato de "
 u"recorrerlos (simply by moving consciously through the steps of the GSD wheel) mas dos actos propios "
 u"(focus on behavior rather than on character; if you are regularly and genuinely soliciting feedback). "
 u"ETAPAS es una de las tres cosas que la restriccion 1 de D.27 admite. "
 u"LOS SEIS CASOS DE ESTA SECCION NO VIAJAN A NINGUN PASO Y LOS NOMBRO PARA QUE SE PUEDA COMPROBAR: el "
 u"fundador que temia que la empresa reflejara su caracter (linea 277), el oro comprado por un comentario "
 u"de pasillo (287), el cuero de los autobuses (289), la camisa blanca (291), la carpeta de papeleo del "
 u"primer dia (309), el sofa movido (319) y la sala informal que hubo que quitar (325). Manual 3.5. Lo "
 u"que viaja es la doctrina que cada uno ilustra, y esa esta en las lineas 281, 285, 293, 297, 311, 313, "
 u"317, 323 y 329. EL UNICO CASO CUYA MECANICA SI VIAJA ES EL DE APARCAR (linea 299), y viaja porque el "
 u"texto lo escribe como prueba y no como anecdota: comprobar si tu conducta cuadra con la cultura que "
 u"empujas, y si no cuadra explicarla o corregirla. El paso 8 lo dice sin el nombre de la empresa. "
 u"LA SENIAL BARATA DE MANUAL 3.5 SALE LIMPIA: el entregable no lleva ni un dato de ninguno de los siete "
 u"casos. "
 u"EL PAR QUE DECLARO YO ANTES DE QUE LO LEVANTE NADIE: recorrer_rueda_hacer_cosas_equipo, que sale de "
 u"cap_07 lineas 65 a 77 y tiene 12 pasos, es la MADRE de este nodo. MI VEREDICTO ES CONTINUA CON "
 u"ARISTA: la madre recorre la rueda sobre LAS DECISIONES del equipo y entrega una vuelta entera de la "
 u"rueda dada; este la recorre sobre TU PROPIA CULTURA y entrega tus conductas revisadas contra la "
 u"cultura que dices querer. Comparten los nombres de las etapas y ni un acto: la madre no tiene la "
 u"prueba de la conducta propia, ni el cafe, ni el entorno, ni la senial de que ya no vaya de ti. Razon "
 u"escrita en el reporte de la vuelta 22. "
 u"RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 14 pasos, 14 TRANSCRIPCION, 0 PUENTE. P1 de las lineas 275 y "
 u"277; P2 a P4 de la 281; P5 de la 285; P6 de la 293; P7 de la 297; P8 de la 299; P9 de la 311; P10 de "
 u"la 311; P11 de la 313; P12 de la 317; P13 de la 323; P14 de la 329. "
 u"LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: cada cuanto se hace este recorrido, quien lo hace "
 u"contigo, como se mide si la cultura ha cambiado, y que se hace cuando la conducta propia que no cuadra "
 u"es una que no quieres cambiar.",
)

# --------------------------------------------------------------- P16, L301 a L305
nodo(
 u"debatir_decidir_asuntos_cultura_evitar_delegar",
 u"Debatir y decidir tu misma los asuntos de cultura que te tienta delegar a recursos humanos, para que "
 u"no los decidan sin tu influencia humanizadora ni se queden sin decidir",
 u"Los asuntos de cultura que el texto nombra uno a uno como los que se delegan por no gastar neuronas "
 u"en ellos, con los dos sitios adonde va la cultura si se delegan o si nadie los decide",
 [u"Debate and decide explicitly. Don't let things that pervert your culture just happen"],
 u"Cuando tienes delante uno de esos asuntos de cultura en los que preferirias no gastar neuronas y te "
 u"tienta pasarselo a recursos humanos o simplemente dejarlo pasar.",
 u"Esos asuntos debatidos y decididos explicitamente por ti, con tu influencia humanizadora dentro, en "
 u"vez de decididos por recursos humanos y los abogados laborales o dejados sin decidir.",
 [
  u"Reconoce la tentacion por su nombre, que es lo que el texto hace: hay una serie de debates y "
  u"decisiones que vas a estar tentado de delegar a recursos humanos, y suelen ser cosas en las que "
  u"preferirias no gastar tus neuronas.",
  u"Ten delante los asuntos que el texto nombra uno a uno, porque son el inventario de lo que se delega: "
  u"si a la fiesta se le va a llamar fiesta navidenia o fiesta de las fiestas, si va a haber arbol o no, "
  u"si va a haber candelabro de las siete velas, si se va a servir alcohol en la fiesta, que se hace "
  u"cuando llegas un lunes por la maniana y te encuentras ropa interior sobre la mesa de la sala de "
  u"reuniones, y que se hace con que una persona del equipo le haya dado a otra una patada en el trasero "
  u"de las de broma, de las que os dabais entre amigos en el colegio, y la que la recibio este indignada.",
  u"Pregunta por cada uno la pregunta que el texto pone al final de esa lista: quien va a decidir como se "
  u"maneja esto.",
  u"Cuenta con lo que pasa si lo delegas, que el texto dice sin rodeos: las decisiones que acaben tomando "
  u"recursos humanos y los abogados laborales sin tu influencia humanizadora empujaran tu cultura en la "
  u"direccion de que la ley es un asno.",
  u"Y cuenta con lo que pasa si no lo decide nadie: acabas en territorio de El senior de las moscas.",
  u"Y decide sabiendo que ninguna de esas dos es la cultura que quieres, que es como el texto cierra.",
 ],
 u"UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_11.md, unidad Cap. 8, Results. Sale de las lineas "
 u"301 a 305, bajo el rotulo Debate and decide explicitly. Don't let things that pervert your culture "
 u"just happen, dentro de la seccion BE CONSCIOUS OF CULTURE. ES LA PIEZA P16 DE LA FRONTERA DE cap_11. "
 u"POR QUE ES NODO PROPIO Y NO UN PASO DE recorrer_rueda_conscientemente_cultura_equipo, y es el corte "
 u"mas discutible del capitulo y va marcado como tal en el reporte de la vuelta 22: su par es otro. "
 u"Aquel se activa cuando quieres influir en tu cultura a sabiendas y entrega tus conductas revisadas; "
 u"este se activa en el momento concreto en que te tienta delegar un asunto, y entrega ese asunto "
 u"decidido por ti. Y el libro le da aqui algo que no le da a ninguna otra etapa de esa seccion: SU "
 u"PROPIO INVENTARIO DE OBJETOS DE TRABAJO, seis asuntos nombrados uno a uno en la linea 303, que es "
 u"exactamente la cara positiva de D.27. "
 u"SI EL AUDITOR LEE QUE ESTO ES UN PASO Y NO UN NODO, la salida es fundirlo dentro de "
 u"recorrer_rueda_conscientemente_cultura_equipo como un paso mas entre su paso 8 y su paso 9, y "
 u"entonces cap_11 cierra en 15 piezas y no en 16, justo en el techo. Lo digo con las dos cuentas "
 u"hechas para no tener que elegir la que me conviene. "
 u"LAS DOS REFERENCIAS CULTURALES DE LAS LINEAS 303 Y 305 (el candelabro de las siete velas y la novela "
 u"de la isla) SE TRANSCRIBEN POR LO QUE SON, un objeto de una fiesta y el nombre de un libro, y no se "
 u"convierten en otra cosa. "
 u"RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 6 pasos, 6 TRANSCRIPCION, 0 PUENTE. P1 a P3 de la linea 303; "
 u"P4 a P6 de la linea 305. "
 u"LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: como se decide cada uno de los seis asuntos, con "
 u"quien se debaten, en que reunion, y que se hace cuando recursos humanos ya lo decidio antes de que "
 u"llegaras. El libro pone el inventario y el mandato de decidir, y NO pone ninguna de las respuestas: "
 u"escribirlas seria escribirlas yo.",
)

for d in CANDIDATOS:
    fallos = reglas_id.validar(d['id'])
    ruta = os.path.join(DEST, d['id'] + '.json')
    print('%-50s reglas_id: %-18s pasos: %2d  %s'
          % (d['id'], fallos or 'OK', len(d['pasos_accionables']),
             'YA EXISTIA' if os.path.exists(ruta) else 'nuevo'))
    if fallos:
        raise SystemExit('EL ID NO PASA LAS REGLAS. No se escribe nada.')
    with io.open(ruta, 'w', encoding='utf-8') as f:
        f.write(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True))
        f.write(u'\n')
print('')
print('escritos %d candidatos' % len(CANDIDATOS))
