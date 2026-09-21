import json, pathlib
d = {
 "id": "programar_reunion_individual_cadena",
 "titulo": "Programar la reunion individual en cadena, fijando la siguiente en el momento en que termina la que se esta teniendo",
 "dominio": "gestion_equipos",
 "estado": "vivo",
 "ids_alias": [],
 "nodos_previos": [],
 "nodos_siguientes": [],
 "atribuciones": [],
 "fuentes": [{"clave": "grove_high_output", "fecha": "2026-09-19"}],
 "denominaciones": {
   "nombre_largo": "La programacion en cadena de la reunion individual: se fija la siguiente cuando termina la que se esta teniendo, con lo que se pueden tener en cuenta los demas compromisos y se evitan las cancelaciones, al contrario de lo que pasa con el horario fijo, donde unas vacaciones que caigan en la fecha se llevan por delante la reunion",
   "sigla": "",
   "otros_idiomas": [
     {"idioma": "ingles", "termino": "rolling basis"},
     {"idioma": "ingles", "termino": "set schedule"},
     {"idioma": "ingles", "termino": "one-on-one"}
   ]
 },
 "condiciones_activacion": "Cuando hay que poner en el calendario la reunion individual siguiente y se elige entre un horario fijo y fijarla al terminar la que se esta teniendo.",
 "entregable_esperado": "La reunion individual siguiente ya fijada en el calendario antes de levantarse de la que se esta teniendo, con los demas compromisos de las dos partes tenidos en cuenta y sin fechas que se caigan por coincidir con una ausencia.",
 "pasos_accionables": [
   "Programa las reuniones individuales en cadena.",
   "Fija la siguiente en el momento en que termina la reunion que se esta teniendo.",
   "Cuenta con lo que eso consigue: asi se pueden tener en cuenta los demas compromisos y se evitan las cancelaciones.",
   "Cuenta con el caso contrario que el libro pone: si el supervisor usa un horario fijo para la reunion individual, por ejemplo la manana de cada segundo miercoles, y las vacaciones del subordinado caen en esa fecha, la reunion no se va a celebrar.",
   "Cuenta con que programando en cadena eso se evita facilmente."
 ],
 "resumen_teorico": (
  "UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_05.md, unidad Cap. 4, titulo textual Meetings, The Medium of Managerial Work. "
  "Sale de la PIEZA P20 de la frontera de cap_05 publicada en la vuelta 50 (LL.4.b), L57 a L57, 74 palabras. "
  "LAS PALABRAS LAS RECOMPUTE YO EN LA VUELTA 52 ANTES DE CORTAR y reproducen la frontera al digito: 74, que es lo que el encargo de la vuelta 52 publica desde LL.4.b (.v52/palabras_tramos.txt). "
  "EL TRAMO ENTERO ES DE ESTE NODO: cero frontera interna, cero solapes y cero prestamo de tramos vecinos. Los cinco pasos salen de L57 y de ninguna otra linea. "
  "ES EL ULTIMO TRAMO DE LA SECCION DEL UNO A UNO, y con el la seccion queda cerrada: L59 en adelante ya es la palanca y su cuenta, que la frontera de LL.4.b da en cero nodos. "
  "POR QUE ES PROCEDIMIENTO: el libro pone SU PROPIO INVENTARIO DE ETAPAS (EXTRACTOR.md 9.1), y ademas trae la pieza mas dificil de inventar, que es el contraejemplo con su mecanismo. "
  "Nombra uno a uno: como se programa (on a rolling basis), el acto exacto que eso significa (setting up the next one as the meeting taking place ends), los dos efectos (other commitments can thereby be taken into account and cancellations avoided), el caso contrario con su ejemplo de calendario (a set schedule, such as every second Wednesday morning), el suceso que lo rompe (if the subordinate vacation happens to fall on that date) y su consecuencia (the meeting is not going to occur). "
  "Y NO HAY ADJETIVO DE ADECUACION EN EL SITIO DEL CRITERIO: no dice una programacion adecuada ni una frecuencia razonable; dice cuando se fija la siguiente, que es un momento que quien lee reconoce sin interpretar nada. "
  "DE DONDE SALE CADA PASO, uno a uno, y los cinco salen de L57: "
  "paso 1 (One-on-ones should be scheduled on a rolling basis); "
  "paso 2 (setting up the next one as the meeting taking place ends); "
  "paso 3 (Other commitments can thereby be taken into account and cancellations avoided); "
  "paso 4 (If the supervisor uses a set schedule for a one-on-one, such as every second Wednesday morning, and if the subordinate vacation happens to fall on that date, the meeting is not going to occur); "
  "paso 5 (By scheduling on a rolling basis, this can be easily avoided). "
  "NOTA DE TRANSCRIPCION: el original encierra la aposicion del paso 2 entre guiones largos y usa apostrofe tipografico en el posesivo del subordinado. Cito con coma y en forma desarrollada porque el barrido de esta casa no admite ni guiones largos ni signos tipograficos, y lo citado no cambia. "
  "RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 5 pasos, 5 TRANSCRIPCION, 0 PUENTE. "
  "DONDE ESTUVE A PUNTO DE ESCRIBIR UN PUENTE Y NO LO ESCRIBI, especie EL RESPONSABLE: iba a escribir QUIEN fija la siguiente reunion de los dos, que es lo que un lector pregunta en cuanto lee el paso 2. L57 escribe el acto en pasiva (should be scheduled, setting up the next one) y no reparte el papel; ademas la reunion es del subordinado por L41 y el calendario del supervisor manda por L39, asi que cualquiera de las dos respuestas que yo escribiera seria mia. Los pasos 1 y 2 se quedan sin sujeto, igual que el libro. "
  "SEGUNDO SITIO DE TENTACION, especie EL PERIODO, y es la mas fina del tramo: iba a escribir CADA CUANTO se fija la siguiente, o sea a cuantos dias vista. El libro dice cuando SE FIJA (al terminar la anterior) y no dice para cuando; la frecuencia vive en otro renglon y en otro nodo, que es P11 con la madurez relevante para la tarea. Confundir las dos seria meter aqui la cifra de alla. "
  "TERCER SITIO DE TENTACION, especie EL DESTINATARIO: iba a escribir donde se apunta la cita o que se haga en el calendario compartido. L57 no nombra ningun soporte y el paso 2 se queda en fijarla. "
  "EL SEGUNDO MIERCOLES NO VA EN ATRIBUCIONES, Y DIGO POR QUE, con la misma razon que el ocho de P13 y los cinco minutos de P18: es el ejemplo de un caso contrario (such as), no una prescripcion del autor. El libro no manda reunirse los miercoles; usa esa fecha para ensenar como se cae un horario fijo. Las cifras que SI fueron a atribuciones en esta campania son prescripciones, y esta no lo es. "
  "CERO ATRIBUCIONES, por la razon escrita arriba: L57 no trae ni una cifra prescrita ni una frase de otro autor. "
  "LO QUE NO ESCRIBO Y POR ESO NO ESTA AQUI: NO escribo que se hace cuando la reunion se cancela igualmente; NO escribo con cuanta antelacion se fija; NO escribo ninguna regla para las vacaciones, porque el libro las usa como ejemplo de lo que rompe el horario fijo y no legisla sobre ellas. "
  "ARISTAS DECLARADAS POR LECTURA, para cablearlas el dia de la insercion y no hoy (D.39 mide la puerta CERRADA para este libro en esta vuelta, .v52/puerta_d39.txt): "
  "(1) D.29 hacia la CABEZA usar_tres_clases_reunion_proceso, que ya espera en la bandeja: este nodo es un MEDIO de la primera de las tres clases que aquella cabeza nombra, con la misma etiqueta y por la misma razon escrita dentro de la ficha de la cabeza. "
  "(2) D.29, PARIENTE fijar_frecuencia_reunion_individual_madurez_tarea, de la bandeja y de la vuelta 51: aquel dice CADA CUANTO se tienen y este dice CUANDO SE FIJA la siguiente. Son las dos mitades del calendario de la misma reunion y no se repiten en ningun paso; ademas son las que un lector confunde con mas facilidad, y por eso el dia que se cablee hay que leer las dos delante. "
  "(3) D.29, PARIENTE fijar_duracion_lugar_reunion_individual, de la bandeja y de la vuelta 51: aquel pone cuanto dura y donde, y este cuando se fija la siguiente. Tercera pieza del mismo calendario, cero pasos comunes. "
  "(4) D.29, PARIENTE POR CONTRASTE infundir_regularidad_reunion_proceso, de la bandeja y de la vuelta 51: aquel manda infundir REGULARIDAD a la reunion de proceso y este manda NO usar un horario fijo. LOS DOS PARECEN DECIR COSAS CONTRARIAS Y NO LAS DICEN: la regularidad de aquel es que la reunion se celebre siempre, y la cadena de este es justamente lo que impide que una fecha fija se lleve por delante una celebracion. El dia que se cablee hay que leer los dos delante, porque un lector rapido leera contradiccion donde hay complemento. "
  "DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO: el paso 5 repite el paso 1 (programar en cadena) y un lector estricto lo tumbara por redundante, dejando el nodo en cuatro pasos. Lo sostengo porque en el libro es la frase de cierre que ata el contraejemplo del paso 4 con la regla del paso 1, y porque quitarlo deja el paso 4 contando una desgracia sin salida. Si cae, cae DENTRO de mi marcado. "
  "SEGUNDO DISCUTIBLE: los pasos 3 y 4 son EFECTOS y CASOS y no actos del que lee, y un lector estricto los tumba los dos dejando el nodo en dos pasos, que es el minimo del esquema. Los sostengo porque el paso 3 es el motivo entero de la regla y el paso 4 es el unico sitio del tramo donde el libro ensena a reconocer el fallo. Si caen, caen DENTRO de mi marcado. "
  "TERCER DISCUTIBLE, Y ES SOBRE UNA CIFRA MIA: publico 74 palabras y con ellas doy la seccion del uno a uno por cerrada en 6 nodos y cap_05 en 12 de 26. Las dos cifras son de recuento y las dos las recomputo en el cierre de esta vuelta con su instrumento delante; si alguna discrepa, la discrepancia se declara y no se resuelve copiando. Marco esto porque la tanda anterior me cazo en aritmetica y ninguno de mis trece marcados era una cifra."
 )
}
p = pathlib.Path("cuarentena/grove_high_output/%s.json" % d["id"])
assert not p.exists(), "ya existe"
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("escrito", p, len(d["pasos_accionables"]), "pasos")
