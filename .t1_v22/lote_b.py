# -*- coding: utf-8 -*-
"""LOTE B de cap_11: las piezas P5 a P8."""
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


# ---------------------------------------------------------------- P5, L115 a L127
nodo(
 u"leer_seniales_fallo_jefe_reunion_solas",
 u"Leer en tus reuniones a solas las cinco seniales que el texto da de que estas fallando como jefe",
 u"Las cinco seniales tempranas que una reunion a solas da al jefe: cancelaciones, actualizaciones que "
 u"podrian ir por correo, solo buenas noticias, ninguna critica hacia ti, y ninguna agenda",
 [u"Signs you'll get from 1:1s that you're failing as a boss"],
 u"Cuando quieres las seniales tempranas de que estas fallando como jefe, y las buscas donde el texto "
 u"dice que aparecen primero: en tus propias reuniones a solas.",
 u"Las seniales presentes en tus reuniones a solas identificadas una a una con lo que el texto dice que "
 u"significan, y la accion que el texto encarga para las que la llevan.",
 [
  u"Parte de para quien vale cada cosa: la reunion a solas vale a quien te reporta para compartir su "
  u"pensamiento contigo y decidir en que direccion sigue su trabajo, y te vale a ti porque es ahi donde "
  u"te llegan las primeras seniales de aviso de que estas fallando como jefe.",
  u"Mira si hay cancelaciones: si la gente que te reporta cancela las reuniones a solas demasiado a "
  u"menudo, es senial de que vuestra asociacion no les resulta fructifera, o de que la estas usando de "
  u"forma inapropiada para soltar la critica que llevabas acumulando.",
  u"Mira si lo que te dan son solo actualizaciones: si la gente se limita a darte cosas que podrian "
  u"habersete mandado por correo, animales a usar ese tiempo de forma mas constructiva.",
  u"Mira si solo oyes buenas noticias: si es asi, es senial de que la gente no se siente comoda "
  u"trayendote sus problemas, o de que cree que no vas a hacer nada con ellos.",
  u"Mira si nunca te critican: si nunca te critican, no eres lo bastante bueno consiguiendo guia de tu "
  u"equipo. Acuerdate de esa frase, que puedo hacer o dejar de hacer que te facilitaria esto.",
  u"Mira si llegan sin agenda: si vienen sistematicamente sin temas que tratar, puede significar que "
  u"estan desbordados, que no entienden para que es esta reunion, o que no la estan tomando en serio.",
 ],
 u"UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_11.md, unidad Cap. 8, Results. Sale de las lineas "
 u"115 a 127, bajo el rotulo Signs you'll get from 1:1s that you're failing as a boss, dentro de la "
 u"seccion 1:1 CONVERSATIONS. ES LA PIEZA P5 DE LA FRONTERA DE cap_11. "
 u"POR QUE ES PROCEDIMIENTO Y NO UNA ADVERTENCIA, con D.27 delante y sabiendo que este es el caso en que "
 u"mas facil seria equivocarse: el libro NO pone un mandato general con un adjetivo de adecuacion; pone "
 u"su propio INVENTARIO DE OBJETOS A REVISAR, cinco seniales nombradas una a una con su rotulo propio en "
 u"las lineas 119 a 127 (Cancellations, Updates, Good news only, No criticism, No agenda), cada una con "
 u"su lectura escrita. Mirar los cinco objetos de una lista que el libro escribe es un procedimiento, y "
 u"deja fichero: las que estan y las que no. "
 u"Y EL LIBRO NO ESCRIBE LA CUENTA: dice some sure signals, no cinco, asi que ni el id ni el titulo del "
 u"fichero le atribuyen un numero al libro. El cinco del titulo de esta ficha es mio y sale de contar "
 u"las lineas 119 a 127, y lo digo aqui en vez de dejarlo pasar. "
 u"LA UNICA ACCION ENCARGADA QUE EL TEXTO DA ES LA DE LA SEGUNDA SENIAL (encourage them to use the time "
 u"more constructively) y la del recordatorio de la cuarta (Remember that phrase). Las otras tres solo "
 u"traen su lectura, y por eso sus pasos solo traen su lectura: completar las tres que faltan seria "
 u"exactamente el puente que D.30 llama el destinatario. "
 u"RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 6 pasos, 6 TRANSCRIPCION, 0 PUENTE. P1 de la linea 117; P2 de "
 u"la 119; P3 de la 121; P4 de la 123; P5 de la 125; P6 de la 127. "
 u"LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: cuantas cancelaciones son demasiadas, cada cuanto se "
 u"revisan las cinco seniales, y que se hace cuando aparece alguna de las tres que no traen accion.",
)

# -------------------------------------------- P6, L129 a L145 mas L159 a L163
nodo(
 u"conducir_reunion_equipo_agenda_tres_bloques",
 u"Conducir la reunion semanal de equipo con la agenda de tres bloques del texto: aprender, escuchar y "
 u"aclarar, sin debatir ni decidir dentro",
 u"La reunion de equipo con sus tres goles escritos, su agenda de veinte, quince y treinta minutos, el "
 u"cuadro de mando de unos pocos numeros, y la regla de identificar las decisiones sin tomarlas",
 [u"STAFF MEETINGS", u"Review metrics, study hall updates, and identify (but do not make) key decisions",
  u"Learn: review key metrics", u"Listen: put updates in a shared document",
  u"Clarify: identify key decisions & debates"],
 u"Cuando conduces la reunion semanal con las personas que te reportan y quieres que sirva para algo, en "
 u"vez de que la temas tu, la vean como perdida de tiempo los que van, y se sientan excluidos los que no.",
 u"La reunion semanal corrida con sus tres bloques y sus tiempos, el cuadro de mando revisado, y las una "
 u"o dos decisiones y el debate mas importante de la semana identificados con su duenio, sin haberlos "
 u"decidido ni debatido dentro.",
 [
  u"Cuenta con lo que el texto mide antes de darte la agenda: bien llevada, una reunion de equipo te "
  u"ahorra tiempo porque te avisa de los problemas, comparte las actualizaciones con eficiencia y os deja "
  u"a todos de acuerdo sobre cuales son las prioridades compartidas de la semana.",
  u"Ponle los tres goles que el texto escribe: repasar como han ido las cosas la semana anterior, dejar "
  u"que la gente comparta actualizaciones importantes, y forzar al equipo a aclarar cuales son las "
  u"decisiones y los debates mas importantes de la semana que viene.",
  u"Y para ahi: el texto dice que eso es todo, y que esta no es la reunion donde se debate ni donde se "
  u"decide.",
  u"Haz tu trabajo, que el texto define en tres actos: establecer una agenda constante, insistir en que "
  u"la gente se cinia a ella, y cortar a quien se alarga demasiado o se va por las ramas.",
  u"Monta la agenda con los tres bloques y sus tiempos: aprender, repasar los indicadores clave, veinte "
  u"minutos.",
  u"Escuchar, poner las actualizaciones en un documento compartido, quince minutos.",
  u"Aclarar, identificar las decisiones y los debates clave, treinta minutos.",
  u"En el bloque de aprender, pregunta que fue bien esa semana y por que, y que fue mal y por que.",
  u"Monta para eso un cuadro de mando de indicadores clave, y el texto aclara que no significa un sistema "
  u"sofisticadisimo montado por un departamento de informatica: significa una hoja de calculo con unos "
  u"pocos numeros.",
  u"Elige esos numeros con la pregunta que el texto da: cuales son las actividades y los resultados mas "
  u"importantes que ves cada semana y que te dicen si vas camino de lograr tus objetivos.",
  u"Disenia tu misma el cuadro de mando: el texto dice que no necesitas que te lo haga una infraestructura "
  u"corporativa.",
  u"Idealmente que se actualice solo; y si eso no es posible, asegurate de que cada persona que trabaja "
  u"para ti actualice su parte la noche anterior a la reunion.",
  u"Si hace falta, compruebalo tu y dales la lata hasta que metan sus actualizaciones.",
  u"Si puedes, pon el cuadro de mando en un sitio donde lo vea el equipo entero.",
  u"Y haz publicas casi siempre las notas de esa conversacion.",
  u"En el bloque de aclarar, pregunta cuales son la una o dos decisiones mas importantes y el unico "
  u"debate mas importante que tu equipo tiene que abordar esa semana.",
  u"Si tu equipo es de menos de unas veinte personas, probablemente puedas limitarte a listarlos y "
  u"decidir o debatir sobre la marcha.",
  u"Si tu equipo es mas grande que unas veinte personas, ponte mas formal: pon esos temas en las agendas "
  u"de reuniones separadas de gran decision y de gran debate, e identifica duenios para cada uno.",
  u"Cuenta con que eso parece multiplicar reuniones y con lo que el texto responde: en realidad es la "
  u"manera de sacarte a ti de reuniones y de que esten presentes los que quieren estar en esos debates y "
  u"decisiones.",
  u"Y deja que los duenios del debate y de la decision no sean ni tu ni la gente que te reporta, porque "
  u"esas reuniones separadas son la manera de delegar debates y decisiones, y delegarlos los empuja hacia "
  u"los hechos y evita el pensamiento jerarquico.",
  u"Comunica al equipo mas amplio la agenda de esas dos reuniones, y deja que asista libremente quien "
  u"quiera.",
  u"Cuenta con lo que el texto dice que pasa entonces: al principio seran probablemente demasiado "
  u"grandes, pero muy pronto la gente ira solo si de verdad quiere o necesita estar, porque odia mas "
  u"asistir a reuniones que no le incumben que quedarse fuera de decisiones que si.",
 ],
 u"UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_11.md, unidad Cap. 8, Results. Sale de las lineas "
 u"129 a 145 y de las lineas 159 a 163, bajo el rotulo STAFF MEETINGS. ES LA PIEZA P6 DE LA FRONTERA DE "
 u"cap_11, Y SU TRAMO ES NO CONTIGUO: entre sus dos mitades viven las lineas 147 a 157, que son el "
 u"mecanismo de los apuntes de sala de estudio y salen en su propio nodo, "
 u"escribir_apuntes_sala_estudio_equipo. Lo digo aqui para que la frontera se pueda comprobar. "
 u"POR QUE LOS TRES BLOQUES VAN EN UN SOLO NODO Y NO EN TRES: comparten UNA activacion (conduces la "
 u"reunion semanal) y UN entregable (la reunion corrida con sus tres bloques), y el libro los encadena "
 u"el mismo en la linea 137 con una sola frase (Here's the agenda that I've found to be most effective). "
 u"Es la vara de la ACTA 20 seccion 4.1 confirmada por la ACTA 21 seccion 4.2. "
 u"LA CUENTA QUE EL LIBRO SI ESCRIBE, y por eso el id la lleva: la linea 135 dice An effective staff "
 u"meeting has three goals. PERO ES UNA CUENTA DE GOLES, NO DE PARTES, y por eso esto NO es una serie "
 u"D.37: EXTRACTOR.md 15.6 pide que la cuenta sea de las PARTES que existen como nodos, y aqui los tres "
 u"goles son fines, que la restriccion 1 de D.27 excluye expresamente. Los tres bloques de la agenda son "
 u"pasos de este nodo y no nodos hermanos. "
 u"EL PAR QUE DECLARO YO ANTES DE QUE LO LEVANTE NADIE: el paso 6 de este nodo nombra en una linea poner "
 u"las actualizaciones en un documento compartido, y escribir_apuntes_sala_estudio_equipo lo despliega "
 u"en su mecanismo entero. CONTINUA CON ARISTA, declarada en docs/loop/REPORTE.md de la vuelta 22 con su "
 u"paso citado. Y lo mismo con los pasos 18 y 20, que nombran las reuniones de gran debate y de gran "
 u"decision, desplegadas en montar_reunion_gran_debate y montar_reunion_gran_decision. "
 u"RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 22 pasos, 22 TRANSCRIPCION, 0 PUENTE. P1 de la linea 133; P2 "
 u"a P4 de la 135; P5 a P7 de las 139, 141 y 143; P8 a P15 de la 145; P16 y P17 de la 159; P18 a P20 de "
 u"la 161; P21 y P22 de la 163. "
 u"LAS CIFRAS SON TODAS DEL LIBRO: veinte minutos, quince minutos, treinta minutos, veinte personas y "
 u"una o dos decisiones y un debate estan escritas en las lineas 139, 141, 143, 159 y 161. "
 u"LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: cuanto dura la reunion entera, quien la convoca, que "
 u"se hace si un bloque se pasa de su tiempo, y cada cuanto se revisa el cuadro de mando en si.",
)

# ---------------------------------------------------------------- P7, L147 a L157
nodo(
 u"escribir_apuntes_sala_estudio_equipo",
 u"Escribir y leer los apuntes de la semana dentro de la propia reunion, como sala de estudio, en vez de "
 u"contarlos en voz alta o dejarlos a que cada cual los ponga por su cuenta",
 u"El mecanismo de los apuntes de sala de estudio: cinco a siete minutos para escribir tres a cinco "
 u"cosas, cinco a siete para leer los de los demas, sin conversaciones laterales, en documento "
 u"compartido, y publicos si eres jefe de jefes",
 [u"study hall", u"snippets", u"Listen: put updates in a shared document during a study hall"],
 u"Cuando quieres que todo el mundo sepa en que anda todo el mundo para poder senialar solapes y motivos "
 u"de preocupacion, y ni te vale una reunion de horas ni te funciona que cada cual escriba sus apuntes "
 u"por su cuenta.",
 u"Los apuntes de la semana de cada persona escritos y leidos dentro de la reunion, con las preguntas de "
 u"seguimiento fuera de ella, en un documento compartido y publicos al equipo mas amplio si eres jefe de "
 u"jefes.",
 [
  u"Parte del problema que el texto pone: mantener a todos al tanto de lo que hacen los demas, para que "
  u"puedan senialar zonas de preocupacion o de solape, sin gastar muchisimo tiempo en ello.",
  u"Distingue las actualizaciones de los indicadores clave, porque el texto dice que no son lo mismo: "
  u"las actualizaciones son cosas que nunca entrarian en el cuadro de mando, del tipo necesitamos cambiar "
  u"los objetivos de este proyecto, estoy pensando en reorganizar, empiezo a pensar que tengo que "
  u"despedir a fulano, o me tienen que operar el mes que viene y estare fuera tres semanas.",
  u"No lo resuelvas con una reunion de equipo de varias horas para compartir esa clase de informacion, "
  u"porque el texto dice que casi todo el mundo odia las reuniones largas.",
  u"Y cuenta tambien con lo que le pasa al otro extremo, el documento publico donde cada cual apunta por "
  u"su cuenta lo que hizo y lo que hara: en teoria es facil de usar y evita reuniones interminables, pero "
  u"en la practica mucha gente se resiste enormemente a escribir sus apuntes, y cuando algunos no los "
  u"hacen el sistema entero se viene abajo.",
  u"Haz por eso lo que el texto dice que le funciono mucho mejor: hacer sitio para que lo hagais todos "
  u"dentro de la reunion de equipo.",
  u"Haz que cada persona se tome de cinco a siete minutos para escribir las tres a cinco cosas que ella o "
  u"su equipo hicieron esa semana y que los demas necesitan saber.",
  u"Y de cinco a siete minutos mas para leer las actualizaciones de todos los demas.",
  u"No permitas conversaciones laterales: exige que las preguntas de seguimiento se traten despues de la "
  u"reunion.",
  u"Cuenta con lo que el texto dice que se juega en esa regla simple: ahorra cantidades enormes de tiempo "
  u"perdido, y si no la pones, la mayor parte de la reunion seran dos o tres personas hablando mientras "
  u"el resto mira sin interes.",
  u"Hazlo en un documento compartido que varias personas puedan editar a la vez, y el texto nombra los "
  u"sitios donde vale hacerlo.",
  u"Si tu equipo no tiene portatiles ni telefonos, usa papel y boligrafo: cada cual apunta sus notas en "
  u"un papel y luego hacedlos circular.",
  u"Si eres jefe de jefes, haz publicos esos apuntes al equipo mas amplio.",
  u"Y cuenta con lo que eso implica, que el texto dice a continuacion: entonces la gente no puede meter "
  u"ahi cosas que hay que mantener confidenciales, como los problemas de desempenio de una persona o "
  u"ajustes de salario que se estan contemplando.",
  u"Si te hace falta, ten un documento de apuntes confidenciales para tu equipo, pero asegurate de que no "
  u"haya demasiadas cosas ahi: la mayoria de lo que tratais deberia compartirse con el equipo mas amplio.",
 ],
 u"UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_11.md, unidad Cap. 8, Results. Sale de las lineas "
 u"147 a 157, dentro de la seccion STAFF MEETINGS y del bloque Listen de su agenda. ES LA PIEZA P7 DE LA "
 u"FRONTERA DE cap_11. "
 u"POR QUE ES NODO PROPIO Y NO UN PASO DE conducir_reunion_equipo_agenda_tres_bloques: su par es otro y "
 u"se puede montar sin la reunion de equipo del otro nodo. Este se dispara cuando quieres que todos sepan "
 u"en que anda todo el mundo y entrega los apuntes escritos y leidos; aquel se dispara cuando conduces la "
 u"reunion semanal y entrega la reunion corrida con sus tres bloques. La madre lo nombra en una linea (su "
 u"paso 6) y este lo despliega en catorce: es la forma de CONTINUA CON ARISTA que EXTRACTOR.md 15.6 "
 u"describe, declarada en el reporte de la vuelta 22 con su paso citado. "
 u"POR QUE ES PROCEDIMIENTO, con D.27 delante: la linea 153 pone el mecanismo entero con sus tiempos y "
 u"su regla (five to seven minutes, three to five things, five to seven minutes to read, don't allow "
 u"side conversations), y las lineas 155 y 157 ponen el medio y la regla de publicidad. Es inventario de "
 u"MEDIOS y de ETAPAS, no de metas. "
 u"LA PALABRA snippets NO SE TRADUCE COMO PRESTAMO SINO COMO apuntes, porque no esta en la lista blanca "
 u"de EXTRACTOR.md 15.1 y tiene equivalente corriente en castellano. El termino ingles va en "
 u"denominaciones. "
 u"LOS NOMBRES DE PRODUCTO DE LA LINEA 155 NO SE TRANSCRIBEN UNO A UNO EN EL PASO 10, y digo por que: "
 u"son marcas de tres proveedores concretos y lo que el libro pide es la propiedad (un documento "
 u"compartido editable por varias personas a la vez), que si esta transcrita. El paso dice que el texto "
 u"los nombra. "
 u"RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 14 pasos, 14 TRANSCRIPCION, 0 PUENTE. P1 y P2 de la linea "
 u"147; P3 de la 149; P4 de la 151; P5 de la 151; P6 a P9 de la 153; P10 y P11 de la 155; P12 a P14 de "
 u"la 157. "
 u"LAS CIFRAS SON TODAS DEL LIBRO: cinco a siete minutos, tres a cinco cosas y tres semanas estan "
 u"escritas en las lineas 147 y 153. "
 u"LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: que se hace con quien aun asi no escribe sus apuntes "
 u"dentro de la reunion, quien revisa el documento confidencial, y cuanto es demasiadas cosas en el.",
)

# ---------------------------------------------------------------- P8, L165 a L173
nodo(
 u"bloquear_tiempo_pensar_calendario",
 u"Bloquear tiempo para pensar en tu calendario y mantener ese tiempo sagrado",
 u"El tiempo para pensar como bloque del calendario que no se mueve por nadie, con el enfado explicito "
 u"ante quien intenta agendar encima y el encargo de que el equipo entero haga lo mismo",
 [u"THINK TIME", u"Block time to think, and hold that time sacred"],
 u"Cuando entre las reuniones a solas, la de equipo, las de gran debate y gran decision y lo que va "
 u"surgiendo no te queda un momento tranquilo para aclarar tu propio pensamiento ni para ayudar a "
 u"aclarar el de los tuyos.",
 u"El tiempo para pensar bloqueado en tu calendario y mantenido, con tu equipo avisado de que ahi no se "
 u"agenda y animado a bloquear el suyo.",
 [
  u"Reconoce primero a que te enfrentas, que es lo que el texto describe: acabas de anadir al calendario "
  u"las reuniones a solas y la de equipo, probablemente tendras que ir a alguna de gran debate y de gran "
  u"decision, y ademas la gente querra hablarte de esto o de aquello y surgiran asuntos urgentes que "
  u"tendras que atender.",
  u"Cuenta con lo que el texto dice que pasa si no haces nada: apenas tendras tiempo de ir al banio o de "
  u"coger agua, no digamos de comer, seras un tiranizado por tu calendario, y el unico momento tranquilo "
  u"para pensar que tendras sera en casa, de noche, cuando de verdad deberias estar durmiendo.",
  u"Agenda entonces algo de tiempo para pensar, y manten ese tiempo sagrado.",
  u"Hazle saber a la gente que no pueden agendar nada encima de el, nunca.",
  u"Enfadate de verdad, y en serio, si lo intentan.",
  u"Y anima a todos los de tu equipo a hacer lo mismo.",
 ],
 u"UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_11.md, unidad Cap. 8, Results. Sale de las lineas "
 u"165 a 173, bajo el rotulo THINK TIME. ES LA PIEZA P8 DE LA FRONTERA DE cap_11 y es la mas fina del "
 u"capitulo, con 311 palabras de cuerpo. "
 u"POR QUE ES PROCEDIMIENTO Y NO POSTURA, con D.27 delante y sabiendo que un parrafo pobre produce un "
 u"nodo inventado (D.30): la linea 173 pone CUATRO imperativos propios del libro, uno detras de otro, "
 u"dirigidos al lector (schedule in some think time, hold that think time sacred, let people know that "
 u"they cannot ever schedule over it, get really seriously angry if they try, encourage everyone on your "
 u"team to do the same). No hace falta ningun inventario indirecto: el libro escribe los pasos. "
 u"EL CASO DEL CONSEJERO DELEGADO QUE BLOQUEABA DOS HORAS DIARIAS Y NO SE LAS MOVIO NI AL PRESIDENTE DE "
 u"UN PAIS, Y EL DEL DIRECTIVO QUE ENCONTRO A SU CONSEJERO DELEGADO MIRANDO AL CIELO, NO VIAJAN A NINGUN "
 u"PASO, y es a proposito: manual 3.5. Las DOS HORAS son del caso, no de la doctrina, y por eso este "
 u"nodo NO pone ninguna cantidad de tiempo. El texto dice some think time y eso es lo que dice el paso "
 u"3. Escribir aqui dos horas seria exactamente el puente que D.30 llama el periodo. "
 u"RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 6 pasos, 6 TRANSCRIPCION, 0 PUENTE. P1 y P2 de la linea 169; "
 u"P3 a P6 de la linea 173. "
 u"EL PAR QUE DECLARO: bloquear_tiempo_pensar_calendario contra "
 u"pelear_proliferacion_reuniones_bloquear_ejecucion, que sale de las lineas 223 a 233 del mismo "
 u"capitulo. Son dos bloques distintos del calendario para dos cosas distintas, y el propio libro los "
 u"distingue en la linea 233 (For the same reason I blocked off think-time in calendar, I ALSO found it "
 u"necessary to block off time to be alone and execute). MI VEREDICTO ES SANO: comparten el medio "
 u"(bloquear calendario) y no comparten ni el entregable ni la activacion. Razon escrita en el reporte "
 u"de la vuelta 22. "
 u"LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: cuanto tiempo para pensar, a que hora, cada cuanto, y "
 u"que se hace cuando el que agenda encima es tu propio jefe. Las cuatro son las especies de puente que "
 u"D.30 nombra y las cuatro se quedan fuera.",
)

for d in CANDIDATOS:
    fallos = reglas_id.validar(d['id'])
    ruta = os.path.join(DEST, d['id'] + '.json')
    print('%-48s reglas_id: %-22s pasos: %2d  %s'
          % (d['id'], fallos or 'OK', len(d['pasos_accionables']),
             'YA EXISTIA' if os.path.exists(ruta) else 'nuevo'))
    if fallos:
        raise SystemExit('EL ID NO PASA LAS REGLAS. No se escribe nada.')
    with io.open(ruta, 'w', encoding='utf-8') as f:
        f.write(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True))
        f.write(u'\n')
print('')
print('escritos %d candidatos' % len(CANDIDATOS))
