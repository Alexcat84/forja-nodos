# -*- coding: utf-8 -*-
"""LOTE C de cap_11: las piezas P9 a P12."""
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


# ---------------------------------------------------------------- P9, L175 a L193
nodo(
 u"montar_reunion_gran_debate",
 u"Montar la reunion de gran debate, donde se debate y no se decide, con sus logisticas, sus normas y su "
 u"unico producto",
 u"La reunion reservada al debate y no a la decision: sus tres propositos escritos, quien la convoca "
 u"despues de la reunion de equipo, la norma de dejar los egos en la puerta y cambiar de papel a mitad, "
 u"y el resumen que es su unico producto",
 [u"BIG DEBATE MEETINGS", u"Lower the tension by making it clear that you are debating, not deciding."],
 u"Cuando tu equipo tiene delante un asunto importante con mucho desacuerdo y hace falta discutirlo sin "
 u"que nadie salga de ahi con una decision tomada.",
 u"El resumen cuidadoso de los hechos y los asuntos que salieron, una definicion mas clara de las "
 u"opciones que hay por delante, y una recomendacion de seguir debatiendo o de pasar a decidir, enviados "
 u"a todas las partes implicadas.",
 [
  u"Reserva estas reuniones para lo que el texto dice: debate, pero no decisiones, sobre los asuntos "
  u"mayores que tiene delante el equipo.",
  u"Cuenta con el primero de los tres propositos que el texto les pone: bajan la tension. Parte de la "
  u"friccion de muchas reuniones viene de que media sala cree que esta ahi para tomar una decision y la "
  u"otra media para debatir; los que querian decidir se enfurecen porque los que debaten no van hacia una "
  u"respuesta, y los que querian debatir se enfurecen porque los que deciden se niegan a pensarlo bien y "
  u"a mirar todos los angulos. Cuando todo el mundo sabe que la reunion acabara sin decision, esa fuente "
  u"de tension se elimina.",
  u"Cuenta con el segundo: te permiten frenar decisiones clave cuando conviene. Cuando un tema es "
  u"realmente importante y hay mucho desacuerdo, los equipos a veces se lanzan a decidir antes de haberlo "
  u"pensado bien o de tener suficiente informacion; meter ese tema en la agenda de debate obliga al "
  u"equipo a seguir peleandose con el, a desenterrar la informacion que falta, a buscar opinion experta o "
  u"simplemente a pensarlo mas hondo.",
  u"Cuenta con el tercero: alimentan una cultura de debate mas amplia. El debate deberia ocurrir "
  u"constantemente en un equipo que funciona, y tener estas reuniones con regularidad y buscarles temas "
  u"ayuda a construir el musculo y la tolerancia a la discusion y a la disension.",
  u"Y cuenta con lo que el texto anade sobre esa tercera: cuando toca un debate de los que se juegan la "
  u"empresa, es importante que las partes implicadas hayan participado antes en unos cuantos debates "
  u"abiertos; y tener debates, incluso discusiones, con regularidad tambien baja la tension, porque evita "
  u"las peleas explosivas. El texto lo apoya en el principio de la criticidad autoorganizada, que dice "
  u"que muchas correcciones pequenias crean estabilidad y una sola correccion enorme crea catastrofe.",
  u"Monta la logistica, que el texto dice que es bien simple: despues de tu reunion de equipo, manda el "
  u"tema, el duenio y los participantes del gran debate al equipo mas amplio, si eres jefe de jefes, y "
  u"tambien a la gente de otros equipos que trabaja con el tuyo.",
  u"Deja que los unicos obligados a participar en el debate sean los que identificaste en la reunion de "
  u"equipo.",
  u"Pero deja que cualquiera pueda asistir u observar la reunion de gran debate.",
  u"Haz que el duenio del debate nombre a alguien para tomar notas y mandarlas a todas las partes "
  u"implicadas.",
  u"Pon las normas, que el texto dice que tambien son sencillas: deja claro que todo el mundo tiene que "
  u"dejar los egos en la puerta de esta reunion.",
  u"Di cual es el objetivo del debate: trabajar juntos para dar con la mejor respuesta. No deberia haber "
  u"ni ganadores ni perdedores.",
  u"Pide a los participantes que se cambien los papeles a mitad de cada debate, que es la norma que el "
  u"texto recomienda: asi te aseguras de que se estan escuchando unos a otros, y les ayuda a mantenerse "
  u"centrados en dar con la mejor respuesta y a soltar sus egos y sus posiciones.",
  u"Y no dejes que salga de ahi ninguna otra cosa, porque el texto dice que el unico producto del debate "
  u"deberia ser un resumen cuidadoso de los hechos y los asuntos que emergieron, una definicion mas clara "
  u"de las opciones que hay por delante, y una recomendacion de seguir debatiendo o de pasar a una "
  u"decision.",
 ],
 u"UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_11.md, unidad Cap. 8, Results. Sale de las lineas "
 u"175 a 193, bajo el rotulo BIG DEBATE MEETINGS. ES LA PIEZA P9 DE LA FRONTERA DE cap_11. "
 u"POR QUE LOS TRES PROPOSITOS DE LA LINEA 179 NO SON TRES NODOS, y la cuenta esta escrita (They serve "
 u"three purposes), asi que esto hay que decirlo con la regla delante: la restriccion 1 de D.27 excluye "
 u"expresamente el inventario de METAS o de FINES, y purposes son fines. Nombrar adonde hay que llegar "
 u"sigue siendo nombrar. Por eso los tres entran como pasos de cuenta con y NO como partes de una serie "
 u"D.37. La cuenta escrita decide si la arista es D.37 o D.29, no si se corta (ACTA 20 seccion 4.1). "
 u"POR QUE ES PROCEDIMIENTO, con D.27 delante: las lineas 189, 191 y 193 ponen el inventario de MEDIOS y "
 u"de ETAPAS, nombrados uno a uno (quien manda que y a quien, quien esta obligado, quien puede asistir, "
 u"quien toma notas, la norma de los egos, la de cambiar de papel, y el producto unico). "
 u"EL PAR QUE DECLARO: montar_reunion_gran_debate contra montar_reunion_gran_decision, de las lineas 195 "
 u"a 203 del mismo capitulo. MI VEREDICTO ES CONTINUA CON ARISTA: el libro dice en la linea 199 que la "
 u"de decision tipicamente pero no siempre SIGUE a la de debate, y en la linea 201 que sus logisticas y "
 u"normas son LAS MISMAS que las de esta, asi que la de decision cuelga de esta y no la repite: aporta "
 u"el decisor, la finalidad de las decisiones y el poder de veto. Razon escrita en el reporte de la "
 u"vuelta 22. Y declaro tambien la arista con centrar_debate_ideas_fuera_egos, de cap_07, que es la "
 u"madre de la norma de los egos. "
 u"RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 13 pasos, 13 TRANSCRIPCION, 0 PUENTE. P1 y P2 de las lineas "
 u"179 y 181; P3 de la 183; P4 y P5 de la 185; P6 a P9 de la 189; P10 a P12 de la 191; P13 de la 193. "
 u"LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: cada cuanto se convoca, cuanto dura, quien elige al "
 u"duenio del debate, y que se hace si el debate no llega a producir su resumen.",
)

# --------------------------------------------------------------- P10, L195 a L203
nodo(
 u"montar_reunion_gran_decision",
 u"Montar la reunion de gran decision, con su decisor nombrado, sus decisiones finales y tu poder de "
 u"veto usado con cuentagotas",
 u"La reunion que sigue al gran debate: sus dos papeles escritos, el decisor nombrado en la reunion de "
 u"equipo, las mismas logisticas y normas que la de debate, y la advertencia de que una decision "
 u"apelable es un debate y no una decision",
 [u"BIG DECISION MEETINGS",
  u"Push decisions into the facts, pull facts into the decisions, and keep egos at bay"],
 u"Cuando hay que tomar una decision importante y quieres que quede claro que se esta decidiendo y no "
 u"debatiendo, normalmente despues de una reunion de gran debate.",
 u"Un resumen cuidadoso de la reunion repartido a todas las partes implicadas, con la decision tomada y "
 u"final, y tu veto puesto antes de que salgan las notas si es que lo pusiste.",
 [
  u"Convocala normalmente despues de una reunion de gran debate, aunque el texto aclara que no siempre "
  u"es asi.",
  u"Cuenta con el primero de los dos papeles que el texto le da, que llama el obvio: tomar decisiones "
  u"importantes.",
  u"Cuenta con el segundo, que llama mas sutil: cuesta saber cuando dejar de debatir y empezar a decidir, "
  u"y el texto dice que no ha encontrado ningun principio absoluto que responda a eso; el acto simple de "
  u"ser explicito y consciente de cuando decides y cuando debates es lo que mas ayuda a saber cuando hace "
  u"falta de verdad tomar una decision. El texto dice que esa es la razon principal por la que recomienda "
  u"dos reuniones separadas.",
  u"Ponle las mismas logisticas y las mismas normas que a la reunion de gran debate.",
  u"Haz que dirija la reunion el decisor, que es a quien habras nombrado en tu reunion de equipo.",
  u"Deja que los unicos obligados a asistir sean los identificados en la reunion de equipo, y que "
  u"cualquiera pueda asistir.",
  u"Haz que se tomen notas y que se pongan a disposicion de todas las partes implicadas.",
  u"Egos en la puerta, y ni ganadores ni perdedores.",
  u"Saca de ahi el producto que el texto le pone: un resumen cuidadoso de la reunion repartido a todas "
  u"las partes implicadas.",
  u"Y asegurate de que las decisiones son finales, porque el texto dice que si no siempre se apelaran y "
  u"entonces seran debates y no decisiones.",
  u"Acata tu las decisiones tomadas en estas reuniones igual que todos los demas.",
  u"Si sabes que es un tema sobre el que tienes opiniones fuertes, o vas tu a la reunion, o le dices al "
  u"decisor que tienes poder de veto.",
  u"Si tienes poder de veto, haz que el decisor te mande la decision para que la apruebes o la rechaces "
  u"antes de que las notas salgan mas ampliamente.",
  u"Y usa ese poder con cuentagotas, porque el texto dice que si no las reuniones se volveran "
  u"irrelevantes.",
 ],
 u"UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_11.md, unidad Cap. 8, Results. Sale de las lineas "
 u"195 a 203, bajo el rotulo BIG DECISION MEETINGS. ES LA PIEZA P10 DE LA FRONTERA DE cap_11. "
 u"POR QUE ES NODO PROPIO Y NO UN PASO DE montar_reunion_gran_debate, sabiendo que la linea 201 dice que "
 u"sus logisticas y normas SON LAS MISMAS: porque su par es otro y su producto es otro. Aquel se activa "
 u"cuando hay que discutir sin decidir y entrega una recomendacion; este se activa cuando hay que "
 u"decidir y entrega una decision final. Y trae procedimiento propio que el otro no tiene: el decisor "
 u"nombrado, la finalidad de la decision, y el poder de veto con su regla de uso. "
 u"LOS PASOS 4 A 8 REPITEN A PROPOSITO LO QUE LA LINEA 201 DICE QUE SE REPITE, y lo declaro en vez de "
 u"esconderlo: el libro escribe the logistics and norms of these meetings are the same, y despues las "
 u"vuelve a listar el mismo. Transcribo su repeticion porque es suya. Si el auditor lee que eso es un "
 u"gemelo de los pasos 6 a 12 del nodo de debate, la salida es fundir los dos nodos, no retirar los "
 u"pasos: va marcado como discutible en el reporte de la vuelta 22. "
 u"LA CUENTA DE LA LINEA 199 (They serve two important roles) ES DE PAPELES, o sea de fines, que la "
 u"restriccion 1 de D.27 excluye. No es una serie D.37. "
 u"RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 14 pasos, 14 TRANSCRIPCION, 0 PUENTE. P1 a P3 de la linea "
 u"199; P4 a P10 de la 201; P11 a P14 de la 203. "
 u"LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: como se elige al decisor, cuanto dura la reunion, "
 u"cuantas veces es demasiadas para usar el veto, y que se hace si el decisor y tu no estais de acuerdo "
 u"y no quieres vetar.",
)

# --------------------------------------------------------------- P11, L205 a L221
nodo(
 u"montar_reunion_general_presentaciones_preguntas",
 u"Montar la reunion general del equipo entero con sus dos partes: las presentaciones que persuaden y "
 u"las preguntas abiertas que dejan oir el disenso",
 u"La reunion general como herramienta de traerse a todos: cuando hace falta segun el tamanio del "
 u"equipo, sus dos partes, quien hace cada una, y por que las respuestas persuaden mas que las "
 u"presentaciones",
 [u"ALL-HANDS MEETINGS", u"Bring others along"],
 u"Cuando tu equipo ha crecido lo bastante como para que las decisiones que se toman empiecen a parecer "
 u"misteriosas o incluso turbias a quien no estuvo cerca del proceso.",
 u"La reunion general celebrada con sus dos partes, con las iniciativas presentadas por el equipo que "
 u"las lleva y con el disenso oido y respondido de frente por quien dirige.",
 [
  u"Mira primero si te hace falta, con el corte que el texto da: si tienes un equipo de diez personas o "
  u"menos, probablemente no necesitas una reunion aparte para asegurarte de que todo el mundo esta "
  u"persuadido de que se han tomado las decisiones correctas.",
  u"Pero segun tu equipo se hace mas grande, empieza a pensar como te traes a todos contigo, porque el "
  u"texto dice que es chocante lo rapido que las decisiones que toman algunos empiezan a parecerles "
  u"misteriosas o incluso turbias a quienes no estuvieron cerca del proceso.",
  u"Si tu equipo es de cien personas o mas, monta una reunion general con regularidad, que el texto dice "
  u"que ayuda de verdad a conseguir respaldo amplio para las decisiones que se toman y tambien a enterarte "
  u"del disenso.",
  u"Montala con las dos partes que el texto dice que suelen incluir: presentaciones para persuadir a la "
  u"gente de que la empresa esta tomando buenas decisiones y va en la direccion correcta, y un turno de "
  u"preguntas y respuestas llevado de manera que quien dirige pueda oir el disenso y responderlo de "
  u"frente.",
  u"Cuenta con lo que el texto dice que pasa cuando se lleva bien: las respuestas que dan los que "
  u"dirigen a esas preguntas, que a menudo son bastante incomodas, suelen persuadir mas que las "
  u"presentaciones.",
  u"Centra las presentaciones en una o dos iniciativas que sean especialmente emocionantes e importantes.",
  u"Usalas para las dos cosas que el texto les pone: informar a todos de las prioridades mas amplias y "
  u"conseguir su respaldo.",
  u"Y haz que las presente el equipo que esta trabajando en la iniciativa, no tu: el texto dice que esa "
  u"practica construia el musculo de persuadir en toda la empresa, y que a la gente normalmente le "
  u"encantaba presentar en esas reuniones. Si tu equipo quiere el escenario, dale el escenario.",
  u"Deja el turno de preguntas en manos de quien dirige la empresa o la fundo, porque es a ellos a "
  u"quienes les toca responder esas preguntas a menudo desagradables, desafiantes o incomodas, y porque "
  u"es asi como se enteran de lo que la gente piensa de verdad.",
  u"Cuida como se responden esas preguntas, porque el texto dice que es enormemente importante para "
  u"persuadir a mucha gente a la vez de que se estan tomando las decisiones correctas de la manera "
  u"correcta.",
  u"Y responde como el texto dice que respondian los dos fundadores que pone de ejemplo: aceptando toda "
  u"clase de preguntas semana tras semana, sin ese tono sobrepreparado y sobremensajeado en el que caen a "
  u"veces los que dirigen, con respuestas espontaneas, humanas y del todo autenticas, y volviendo a la "
  u"reunion siguiente a recibir otra vez preguntas duras e incomodas.",
 ],
 u"UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_11.md, unidad Cap. 8, Results. Sale de las lineas "
 u"205 a 221, bajo el rotulo ALL-HANDS MEETINGS. ES LA PIEZA P11 DE LA FRONTERA DE cap_11. "
 u"POR QUE ES PROCEDIMIENTO, con D.27 delante: la linea 209 pone los DOS cortes de tamanio con su cifra "
 u"(diez o menos, cien o mas), la linea 213 pone las DOS partes nombradas, y las lineas 217 y 219 ponen "
 u"quien hace cada una y con que proposito. Es inventario de etapas y de objetos, no un adjetivo de "
 u"adecuacion. "
 u"LOS NOMBRES DE LAS REUNIONES GENERALES DE CUATRO EMPRESAS, DE LA LINEA 211, NO VIAJAN A NINGUN PASO, "
 u"y tampoco el caso de la reunion siguiente a una adquisicion de la linea 215: son casos, manual 3.5. "
 u"LOS NOMBRES DE LOS DOS FUNDADORES DE LA LINEA 221 NO SE ESCRIBEN EN EL PASO 11, y digo por que lo "
 u"hago asi: lo que el texto pone ahi como doctrina es COMO se responde (espontaneo, humano, autentico, "
 u"sin tono sobrepreparado, volviendo la semana siguiente), y eso es lo que viaja. El paso los nombra "
 u"como los dos fundadores que el texto pone de ejemplo, sin traer el dato del caso al entregable. La "
 u"senial barata de manual 3.5 sale limpia: el entregable no lleva ni un nombre propio. "
 u"RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 11 pasos, 11 TRANSCRIPCION, 0 PUENTE. P1 a P3 de la linea "
 u"209; P4 y P5 de la 213; P6 a P8 de la 217; P9 y P10 de la 219; P11 de la 221. "
 u"EL PAR QUE DECLARO: persuadir_emocion_oyente_no_propia y compartir_logica_mostrar_razonamiento, de "
 u"cap_07, son el paso PERSUADE de la rueda y esta reunion es una herramienta suya. Arista D.29 "
 u"declarada en el reporte de la vuelta 22. "
 u"LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: cada cuanto se celebra, cuanto dura, como se "
 u"recogen las preguntas, y que se hace con el disenso una vez oido.",
)

# --------------------------------------------------------------- P12, L223 a L233
nodo(
 u"pelear_proliferacion_reuniones_bloquear_ejecucion",
 u"Pelear la proliferacion de reuniones bloqueando en tu calendario el tiempo de estar a solas y "
 u"ejecutar, despues de descartar los tres remedios que el texto dice que no cuajan",
 u"La pelea contra la multiplicacion de reuniones: los tres remedios probados que nunca se sostienen, y "
 u"el que el texto dice que si funciona, que es combatir fuego con fuego bloqueando calendario",
 [u"EXECUTION TIME", u"Fight meeting proliferation", u"Meeting-Free Zones"],
 u"Cuando la rueda de sacar cosas adelante ha empezado a parecer la rueda de las reuniones del infierno, "
 u"y la multiplicacion de reuniones amenaza con dejar a tu equipo y a ti sin capacidad de ejecutar.",
 u"Tiempo bloqueado en tu calendario para estar a solas y ejecutar, y tu equipo animado a bloquear el "
 u"suyo, con los tres remedios que no cuajan descartados y dicho por que.",
 [
  u"Reconoce el sintoma que el texto nombra: si no tienes cuidado, la multiplicacion de reuniones puede "
  u"de verdad frenar en seco tu capacidad de ejecutar, tanto como persona como equipo.",
  u"Asume que ser implacable en asegurarte de que tu equipo tiene tiempo para ejecutar es una de las "
  u"cosas mas importantes que puedes hacer como jefe.",
  u"No pruebes el primer remedio que el texto descarta, quitar las sillas de las salas de reunion: el "
  u"texto reconoce que en teoria acorta las reuniones porque casi nadie aguanta de pie mas de una hora, "
  u"que hay investigacion que dice que la gente es mas creativa de pie que sentada, que hay quien dice "
  u"que estar sentado es el nuevo fumar, y que ademas te ahorras el mobiliario, y aun asi dice que nunca "
  u"funciona de verdad y que no conoce ninguna empresa que se haya mantenido en ello.",
  u"No pruebes el segundo, declarar un dia de la semana sin reuniones: el texto cuenta que distintos "
  u"equipos lo intentaron y ninguno fue capaz de sostenerlo.",
  u"Ni el tercero, ponerse el objetivo de terminar antes de tiempo una cuarta parte de tus reuniones: el "
  u"texto dice que le encanto la idea y que no cree que quien se la puso llegara nunca a cumplirla.",
  u"Haz en cambio lo que el texto dice que es la solucion mas eficaz: combatir fuego con fuego.",
  u"Bloquea en tu calendario tiempo para estar a solas y ejecutar, por la misma razon por la que "
  u"bloqueaste el tiempo para pensar.",
  u"Y anima a los demas a hacer lo mismo, porque el texto dice que eso les ayudo a decir que no a mas "
  u"reuniones innecesarias.",
 ],
 u"UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_11.md, unidad Cap. 8, Results. Sale de las lineas "
 u"223 a 233, bajo el rotulo EXECUTION TIME y su subtitulo Fight meeting proliferation. ES LA PIEZA P12 "
 u"DE LA FRONTERA DE cap_11. En el indice del capitulo, linea 29, esta misma herramienta aparece con "
 u"otro nombre, Meeting-Free Zones, y lo declaro en vez de elegir por el libro. "
 u"POR QUE ES PROCEDIMIENTO Y NO POSTURA, con D.27 delante: el libro pone su propio INVENTARIO DE MEDIOS "
 u"con su veredicto escrito, tres remedios nombrados uno a uno en las lineas 229 y 231 con la razon "
 u"medida de por que no cuajan, y el cuarto en la linea 233 con lo que consigue. Descartar por su nombre "
 u"tres remedios que el lector iba a probar es procedimiento, y deja fichero. "
 u"EL PAR QUE DECLARO YO ANTES DE QUE LO LEVANTE NADIE, y es el mas dificil del capitulo: "
 u"reservar_calendario_tiempo_ejecutar, que sale de cap_07 lineas 385 a 387 bajo el rotulo Block time to "
 u"execute, es la MADRE de este nodo y tiene 4 pasos. MI VEREDICTO ES CONTINUA CON ARISTA Y NO REPITE, "
 u"con los dos lados medidos: la madre trae lo que este no tiene (que ejecutar es tarea solitaria, y el "
 u"sesgo de usar el calendario sobre todo para tareas colaborativas, que es su diagnostico entero), y "
 u"este trae lo que la madre no tiene (los TRES remedios descartados con su razon, y el encargo de "
 u"animar a los demas para que puedan decir que no). El acto compartido es uno solo, bloquear "
 u"calendario, y los dos lados tienen procedimiento fuera de el, asi que la vara de manual 4 no tiene "
 u"bascula. Va marcado como discutible en el reporte de la vuelta 22, porque es donde mas cerca estoy de "
 u"un REPITE en todo el capitulo. "
 u"Y EL OTRO PAR, CON bloquear_tiempo_pensar_calendario DEL MISMO CAPITULO: SANO. El propio libro los "
 u"distingue en la linea 233 (For the same reason I blocked off think-time in calendar, I ALSO found it "
 u"necessary to block off time to be alone and execute): son dos bloques distintos para dos cosas "
 u"distintas, uno para pensar y otro para ejecutar. "
 u"RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 8 pasos, 8 TRANSCRIPCION, 0 PUENTE. P1 y P2 de la linea 227; "
 u"P3 de la 229; P4 y P5 de la 231; P6 a P8 de la 233. "
 u"LA CUARTA PARTE DEL PASO 5 ES LA CIFRA DEL LIBRO (25 percent, linea 231) ESCRITA EN LETRA, y el "
 u"nombre del ingeniero que se la puso se queda en el caso, manual 3.5. "
 u"LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: cuanto tiempo se bloquea para ejecutar, cada cuanto, "
 u"y como se mide si la proliferacion de reuniones ha bajado.",
)

for d in CANDIDATOS:
    fallos = reglas_id.validar(d['id'])
    ruta = os.path.join(DEST, d['id'] + '.json')
    print('%-52s reglas_id: %-18s pasos: %2d  %s'
          % (d['id'], fallos or 'OK', len(d['pasos_accionables']),
             'YA EXISTIA' if os.path.exists(ruta) else 'nuevo'))
    if fallos:
        raise SystemExit('EL ID NO PASA LAS REGLAS. No se escribe nada.')
    with io.open(ruta, 'w', encoding='utf-8') as f:
        f.write(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True))
        f.write(u'\n')
print('')
print('escritos %d candidatos' % len(CANDIDATOS))
