import json, pathlib
d = {
 "id": "infundir_regularidad_reunion_proceso",
 "titulo": "Infundir regularidad a la reunion de proceso, para poder agrupar en tanda las tareas de mando semejantes y pronosticar el tiempo que piden",
 "dominio": "gestion_equipos",
 "estado": "vivo",
 "ids_alias": [],
 "nodos_previos": [],
 "nodos_siguientes": [],
 "atribuciones": [],
 "fuentes": [{"clave": "grove_high_output", "fecha": "2026-09-19"}],
 "denominaciones": {
   "nombre_largo": "La regularidad de la reunion de proceso: que los asistentes sepan como se lleva, que asuntos se tratan y que hay que conseguir, para agrupar transacciones en tanda y dejar que tome forma un sistema de control de produccion registrado en los calendarios",
   "sigla": "",
   "otros_idiomas": [
     {"idioma": "ingles", "termino": "process-oriented meeting"},
     {"idioma": "ingles", "termino": "batch"},
     {"idioma": "ingles", "termino": "production control"}
   ]
 },
 "condiciones_activacion": "Cuando llevas una reunion de las que se repiten en un calendario fijo y quieres sacarle el maximo, en vez de dejar que cada convocatoria se organice sola.",
 "entregable_esperado": "Una reunion de proceso con su regularidad puesta: sus asistentes sabiendo las tres cosas que el libro nombra, sus transacciones agrupadas en tanda, y un sistema de control de produccion tomando forma en los calendarios.",
 "pasos_accionables": [
   "Apunta a infundir regularidad a esta clase de reunion, que es la manera de sacarle el maximo.",
   "Consigue que los que asisten sepan como se lleva la reunion.",
   "Consigue que sepan que clases de asuntos de fondo se tratan en ella.",
   "Consigue que sepan que es lo que hay que conseguir en ella.",
   "Disenala de forma que te deje agrupar transacciones en tanda, o sea usar el mismo tiempo y esfuerzo de preparacion de produccion para atender muchas tareas de mando semejantes.",
   "Aprovecha que, dada esa regularidad, tu y los demas asistentes podeis empezar a pronosticar el tiempo que piden las clases de trabajo que hay que hacer.",
   "Deja que de ahi tome forma un sistema de control de produccion, registrado en los distintos calendarios.",
   "Cuenta con lo que ese sistema consigue: que una reunion programada tenga el minimo impacto en las otras cosas que la gente esta haciendo."
 ],
 "resumen_teorico": (
  "UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_05.md, unidad Cap. 4, titulo textual Meetings, The Medium of Managerial Work. "
  "Sale de la PIEZA P6 de la frontera de cap_05 publicada en la vuelta 50 (LL.4.b), L21 a L21, 124 palabras. "
  "LAS PALABRAS LAS RECOMPUTE YO EN LA VUELTA 51 ANTES DE CORTAR y reproducen la frontera al digito: sed sobre la linea 21 mas wc -w da 124, que es lo que LL.4.b publica (.v51/palabras_tramos.txt). "
  "EL TRAMO ENTERO ES DE ESTE NODO: cero frontera interna, cero solapes y cero prestamo de tramos vecinos. Los ocho pasos salen de L21 y de ninguna otra linea. "
  "POR QUE ES PROCEDIMIENTO: el libro pone SU PROPIO INVENTARIO de MEDIOS, que es la cara positiva de la vara de EXTRACTOR.md 9.1. "
  "Nombra uno a uno: las TRES cosas que los asistentes tienen que saber (how the meeting is run, what kinds of substantive matters are discussed, what is to be accomplished), el medio de diseno (allow a manager to batch transactions, to use the same production set-up time and effort), lo que la regularidad habilita (begin to forecast the time required) y el artefacto que toma forma (a production control system, as recorded on various calendars). "
  "Y EL CRITERIO NO ES UN ADJETIVO DE ADECUACION: no dice una reunion apropiada ni con la regularidad razonable, dice QUE tienen que saber y QUE tiene que permitir el diseno. "
  "DE DONDE SALE CADA PASO, uno a uno, y los ocho salen de L21: "
  "paso 1 (To make the most of this kind of meeting, we should aim to infuse it with regularity); "
  "paso 2 (In other words, the people attending should know how the meeting is run); "
  "paso 3 (what kinds of substantive matters are discussed); "
  "paso 4 (and what is to be accomplished); "
  "paso 5 (It should be designed to allow a manager to batch transactions, to use the same production set-up time and effort to take care of many similar managerial tasks); "
  "paso 6 (Moreover, given the regularity, you and the others attending can begin to forecast the time required for the kinds of work to be done); "
  "paso 7 (Hence, a production control system, as recorded on various calendars, can take shape); "
  "paso 8 (which means that a scheduled meeting will have minimum impact on other things people are doing). "
  "NOTA DE TRANSCRIPCION: el original escribe batch, production y production control entre comillas tipograficas. Las cito sin ellas porque el barrido de esta casa no admite signos tipograficos, y la palabra citada no cambia. "
  "RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 8 pasos, 8 TRANSCRIPCION, 0 PUENTE. "
  "DONDE ESTUVE A PUNTO DE ESCRIBIR UN PUENTE Y NO LO ESCRIBI, especie EL PERIODO: iba a escribir cada cuanto se convoca esta reunion, porque todo el tramo habla de regularidad y de calendario. L21 NO da ni un periodo: dice regularly scheduled en L17, que es otro tramo y otro nodo, y aqui solo dice infuse it with regularity. El periodo de cada clase de reunion lo da el libro mas adelante y por su tramo, y ahi ira. "
  "SEGUNDO SITIO DE TENTACION, especie EL RESPONSABLE: iba a escribir quien comunica a los asistentes las tres cosas que tienen que saber. L21 escribe the people attending should know, en pasiva y sin nombrar a nadie que se lo diga. Los pasos 2, 3 y 4 escriben CONSIGUE QUE SEPAN y paran ahi, sin repartir el encargo. "
  "TERCER SITIO DE TENTACION, especie EL DESTINATARIO: iba a escribir a que calendario concreto se lleva el sistema de control de produccion. El libro dice various calendars, en plural y sin nombrar ninguno, asi que el paso 7 dice los distintos calendarios y no elige. "
  "LO QUE NO ESCRIBO Y POR ESO NO ESTA AQUI: NO escribo COMO se agrupa una transaccion en tanda, porque este tramo lo nombra y no lo despliega; NO escribo que hacer si los asistentes NO saben las tres cosas; NO escribo ninguna cifra de tiempo, porque en este tramo no hay ni una. "
  "CERO ATRIBUCIONES, y es deliberado: L21 no trae ni una cifra ni una frase de otro autor. Las de Drucker y Whyte estan en L13, que es la pieza P2 y da cero nodos. "
  "ARISTAS DECLARADAS POR LECTURA, para cablearlas el dia de la insercion y no hoy (D.39 mide la puerta CERRADA para este libro en esta vuelta): "
  "(1) D.29, PARIENTE agrupar_interrupciones_subordinados_reuniones_regulares, que vive en esta misma bandeja y sale de cap_04. Aquel nodo manda agrupar en tanda las interrupciones de los subordinados y atenderlas en las reuniones regulares; este dice COMO se le pone a esa reunion la regularidad de la que aquel depende. Comparten el principio de la tanda y no comparten ni un paso: aquel trabaja sobre las interrupciones, este sobre el diseno de la reunion. Es D.29 y no D.37 porque ninguno de los dos textos dice cuantas partes tiene el otro. "
  "(2) D.29, PARIENTE POR CONTINUIDAD hacia la CABEZA de las tres clases de reunion de proceso, que es el candidato 2 de esta misma tanda (elegir_clase_reunion_proceso_tres_clases): aquella cabeza dice CUALES son las tres reuniones de proceso y esta dice QUE hay que infundirles a todas. El orden del libro las pone seguidas, L21 y L23. "
  "(3) D.29, PARIENTE auditar_calendario_reuniones_semana, que ya vive en el grafo y viene de otro libro: aquel mira el calendario ya hecho para quitar reuniones, este disena la reunion para que el calendario se pueda pronosticar. Cero pasos comunes y direccion contraria. "
  "DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO: el paso 8 es una CONSECUENCIA y no un acto, igual que el paso 11 de dimensionar_numero_subordinados_medio_dia_semanal, y por el mismo motivo lo sostengo: es la frase de cierre literal del tramo y es lo unico que dice PARA QUE sirve el sistema del paso 7. Si cae, cae DENTRO de mi marcado."
 )
}
p = pathlib.Path("cuarentena/grove_high_output/%s.json" % d["id"])
assert not p.exists(), "ya existe"
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("escrito", p, len(d["pasos_accionables"]), "pasos")
