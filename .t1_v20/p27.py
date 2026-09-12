# -*- coding: utf-8 -*-
import json, io
d = {
 "id": "conducir_reuniones_salto_nivel_diez_reglas",
 "titulo": "Conducir reuniones de salto de nivel con el equipo de cada persona a tu cargo, siguiendo las diez reglas generales que el texto da",
 "denominaciones": {
  "nombre_largo": "Las diez reglas generales para que una reunion de salto de nivel sirva a la cultura de guia y no se convierta en una sesion de quejas ni en un ataque al jefe del que se habla",
  "otros_idiomas": [
   {"idioma": "ingles", "termino": "SPEAKING TRUTH TO POWER"},
   {"idioma": "ingles", "termino": "skip level meetings"}
  ],
  "sigla": ""
 },
 "condiciones_activacion": "Cuando eres jefe de jefes y quieres saber que podrian hacer o dejar de hacer las personas a tu cargo para ser mejores jefes, sin que sus equipos tengan que criticarlas delante de ellas.",
 "entregable_esperado": "Las notas de la reunion compartidas con el jefe del que se hablo sin decir quien dijo que, y una o dos cosas concretas que ese jefe va a cambiar ya, comunicadas por el mismo a su equipo y revisadas despues.",
 "pasos_accionables": [
  "Reunete una vez al anio con las personas que trabajan para cada persona a tu cargo, sin esa persona en la sala, y preguntales que podria hacer o dejar de hacer para ser mejor jefe.",
  "Cuenta con el motivo por el que esto hace falta: la mayoria de la gente es muy reticente a criticar a su jefe, y los jefes, sobre todo los nuevos, buscaran consciente o inconscientemente reprimir la critica en vez de fomentarla.",
  "Ve con cuidado, porque estas reuniones pueden convertirse en sesiones de queja, y tiene que quedar claro que no das por supuesto que el jefe, que es tu persona a cargo, sea culpable, ni que no estes dispuesto a oir ninguna critica suya.",
  "Ten presente que la intencion de estas sesiones es apoyar a los jefes que te reportan y no socavarlos, y que parte de apoyarlos es saber cuando lo estan haciendo mal y ayudarlos a arreglarlo.",
  "Y cuida, por tu propia cordura y por la cultura, que estas reuniones no animen a la gente a venir corriendo a ti en vez de hablar directamente con su jefe.",
  "Explicalo, demuestralo y vuelve a explicarlo: dile a cada persona a tu cargo que tienes dos objetivos, ayudarla a ser mejor jefe y asegurarte de que la gente de su equipo se siente comoda dandole su opinion directamente.",
  "Demuestra que dices lo que dices: empieza pidiendole a tu propio jefe, o a alguien que tenga tiempo, que te haga a ti una reunion de salto de nivel, y si eres el consejero delegado pideselo a un entrenador, a un asesor o a un miembro del consejo.",
  "No tengas nunca una reunion de salto de nivel sin el consentimiento previo de la persona a tu cargo.",
  "Pide a los jefes que te reportan que le expliquen todo el asunto a sus equipos de antemano, porque es vital que todos entiendan que la reunion contigo es en apoyo de su jefe y no un ataque contra el.",
  "Al empezar la reunion, repite que el objetivo es que el jefe mejore, y recuerdales que la meta es crear una cultura donde todos se sientan siempre comodos dando guia, y sobre todo critica, directamente a sus jefes, y que esta reunion es un paso hacia eso y no un sustituto de eso.",
  "Y mas importante todavia, no tengas reuniones de salto de nivel con los equipos de algunas de las personas a tu cargo y no con los de otras: tiene que quedar claro que es un proceso rutinario que se hace con cualquiera que tenga gente a su cargo.",
  "Cuenta con lo que pasa si solo las haces cuando hay problemas en un equipo: se convierten en un castigo en vez de en una herramienta bienvenida para ayudar a la gente a desarrollar sus habilidades de gestion.",
  "Asegurate de que la reunion es sin atribucion: que todos entiendan que, aunque el objetivo sea que la gente acabe comoda dando su opinion directamente al jefe, en esta reunion todo lo importante se le contara a su jefe, pero no quien lo dijo.",
  "Toma notas y proyectalas: proyecta las notas que tomas durante la reunion y avisa de que las vas a compartir con el jefe.",
  "Anima a la gente a decirlo si encuentra las notas inexactas, y cuando alguien hable, cambia las notas y comprueba dos veces que estan bien antes de seguir.",
  "Toma las notas tu mismo en vez de pedirle a otro que las tome, por lo que el texto dice que consigue: primero demuestra que estas escuchando y atento, y segundo es una manera excelente de descubrir cuando has entendido algo mal.",
  "Arranca la conversacion contando con que la primera de estas reuniones suele ser incomodisima y que vas a tener que trabajar duro para ganarte la confianza de todos los de la sala.",
  "Empieza por el elogio, que es lo mas facil para que la gente hable, preguntando que esta haciendo bien tu jefe; luego que podria estar haciendo mejor; y luego que es lo que de verdad es un asco.",
  "A medida que salgan problemas, intenta que la gente piense en soluciones, para que no degenere en una sesion de quejas.",
  "Y si te llegan muchas quejas, recuerdate que eso es bueno y no malo: solo estas fracasando si todo es dulzura y luz.",
  "Prioriza los asuntos: cuando la cosa fluya, recuerdale a la gente que casi siempre se plantean muchos mas problemas de los que se van a arreglar, y que la meta es mejorar las cosas, porque dejarlas perfectas no es realista.",
  "Empuja a los de la sala a decidir cuales son los asuntos mas importantes y a priorizar esos.",
  "Comparte las notas justo despues de la reunion: cuando queden unos ocho minutos, pide a todos que miren las notas recordandoles que vas a compartir el documento con su jefe en un momento.",
  "Cuenta con lo que el texto dice que consigue esa inmediatez: enfoca la conversacion, hace a la gente responsable de sus sugerencias, hace que la conversacion se sienta menos a espaldas de la persona, te ahorra los pasos siguientes que se quedan rondando en la cabeza o simplemente no se hacen, y alivia la ansiedad de la persona evaluada, que quiere saber lo que se dijo ya mismo.",
  "Asegurate de que tus personas a cargo hacen y comunican cambios: cuando hayan leido las notas, trabaja con cada una para sacar una o dos cosas concretas que pueda cambiar inmediatamente.",
  "No dejes que sea algo grande y vago como mejorar mis relaciones: mucho mejor algo mas pequenio pero mas tangible, como discrepar en persona y no por correo.",
  "Anima a cada persona a tu cargo a mandar un correo a su equipo explicando que ha aprendido y que va a hacer distinto a partir de ahora, con copia a ti, y a volver sobre ello en la siguiente reunion de equipo para ver si la gente cree que ha ido lo bastante lejos.",
  "Revisa esos cambios en un seguimiento de la reunion de salto de nivel y anima al equipo a decirte si han marcado alguna diferencia o no, porque cuanto mas visible sea el cambio, mejor.",
  "Si la gente cree que no se hizo ningun cambio, o que la reunion no sirvio de nada, tomatelo muy en serio, y en casos extremos quita al jefe en cuestion del equipo, devolviendolo a un puesto sin gente a cargo, poniendolo al frente de otro equipo o despidiendolo.",
  "Ten estas reuniones una vez al anio para cada persona a tu cargo, y si diriges jefes, insiste en que hagan lo mismo, que es lo que hace que el proceso escale.",
  "Cuenta con el problema que el texto nombra por su nombre: cuando empiezan a ir bien todo el mundo las quiere todo el tiempo, y se llega a la proliferacion de saltos de nivel, que consumen mucha energia y atencion y pueden acabar quemandote si tienes que hacer demasiadas."
 ],
 "resumen_teorico": "UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_09.md, unidad Cap. 6, Guidance. Sale de las lineas 383 a 413, bajo el rotulo SPEAKING TRUTH TO POWER. ES LA PIEZA P27 DE LA FRONTERA DE cap_09, UNA DE LAS CINCO QUE LA VUELTA 19 DEJO SIN ESCRIBIR, Y LA PIEZA MAS PROCEDIMENTAL DEL CAPITULO con 1419 palabras remedidas por mi. POR QUE ES PROCEDIMIENTO Y NO POSTURA, con D.27 delante: la linea 391 cierra con here are a few rules of thumb I learned for conducting them y detras van DIEZ consejos rotulados uno a uno, en las lineas 393, 395, 397, 401, 403, 405, 407, 409, 411 y 413. Es inventario de MEDIOS y de ETAPAS del propio libro, no de metas. LA CUENTA NO ESTA ESCRITA: la linea 391 dice a few rules of thumb sin decir cuantas, asi que esto NO es D.37 y no cablea ninguna serie por la cuenta. Los diez los cuento yo de los rotulos y lo digo asi en vez de atribuirle al libro una cuenta que no da. LA LINEA 399 NO ES UN UNDECIMO CONSEJO: empieza con More importantly y continua el rotulo Never have a skip level meeting without prior consent de la 397, sin rotulo propio, asi que sus dos pasos cuelgan de ese mismo consejo. Es el mismo criterio de corte que aplico en P24 con las lineas 349 y 351. RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 31 pasos, 31 TRANSCRIPCION, 0 PUENTE. P1 de la linea 385; P2 de la 389; P3, P4 y P5 de la 391; P6 de la 393; P7 de la 395; P8, P9 y P10 de la 397; P11 y P12 de la 399; P13 de la 401; P14, P15 y P16 de la 403; P17, P18, P19 y P20 de la 405; P21 y P22 de la 407; P23 y P24 de la 409; P25, P26, P27, P28 y P29 de la 411; P30 y P31 de la 413. LOS DOS PERIODOS SON DEL LIBRO Y NO MIOS, que es lo que los salva de ser puentes de la especie el periodo: la una vez al anio esta en la linea 385 y repetida en la 413, y los ocho minutos en la 409. EL DESTINATARIO TAMBIEN ES DEL LIBRO: la copia a ti del correo del jefe a su equipo esta escrita en la linea 411, asi que no es puente de la especie el destinatario. LA LINEA 387, sobre que la organizacion plana es un mito y la jerarquia un hecho inescapable, NO ENTRA COMO PASO: es la razon de la seccion y no un acto, y escribirla como paso habria sido convertir una postura en procedimiento. LA ATRIBUCION DE ROXANE WALES VA A SU SEDE y no a un paso, por el principio 5. LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI: como se decide a quien invitar de un equipo grande, ni que hacer si la persona a tu cargo niega el consentimiento que la linea 397 exige, ni cuanto se espera entre la reunion y su seguimiento.",
 "dominio": "gestion_equipos",
 "estado": "vivo",
 "fuentes": [{"clave": "scott_radical_candor", "fecha": "2026-09-12"}],
 "ids_alias": [],
 "nodos_previos": [],
 "nodos_siguientes": [],
 "atribuciones": [
  {"cifra": "que una de las cosas mas importantes que puede hacer un jefe de jefes para fomentar una cultura de guia es tener reuniones de salto de nivel, y que basta con que ocurran una vez al anio para que sean eficaces",
   "autor": "Roxane Wales, que trabajo primero en la NASA y despues en Aprendizaje y Desarrollo en Google, citada por Kim Scott",
   "fuente": "scott_radical_candor",
   "fecha_corte": "no consta fecha en el texto: el libro dice once told me sin datar la conversacion ni dar obra, asi que la atribucion queda sin fecha de corte y se dice"},
  {"cifra": "que el proceso sale a unas siete u ocho horas al anio si tienes cinco personas a tu cargo, contando una hora por cada salto de nivel y media hora por cada seguimiento",
   "autor": "Kim Scott, sobre el coste en tiempo de su propia recomendacion",
   "fuente": "scott_radical_candor",
   "fecha_corte": "no consta fecha en el texto: la unidad da la cuenta sin datarla y sin decir sobre cuantos casos la midio, asi que la cifra queda sin banda y sin fecha de corte y se dice"}
 ]
}
io.open('cuarentena/scott_radical_candor/%s.json' % d['id'], 'w', encoding='utf-8').write(
    json.dumps(d, ensure_ascii=False, indent=1))
print("escrito:", d['id'], len(d['pasos_accionables']), "pasos")
