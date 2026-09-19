import json, pathlib
d = {
 "id": "fijar_duracion_lugar_reunion_individual",
 "titulo": "Fijar cuanto dura la reunion individual y donde se tiene: una hora como minimo, y en el area de trabajo del subordinado o cerca de ella",
 "dominio": "gestion_equipos",
 "estado": "vivo",
 "ids_alias": [],
 "nodos_previos": [],
 "nodos_siguientes": [],
 "atribuciones": [
   {
     "cifra": "una reunion individual deberia durar una hora como minimo, y cualquier cosa menos que eso tiende a hacer que el subordinado se limite a las cosas sencillas que se despachan deprisa; una programada para durar solo quince minutos no sirve para sacar un problema grande",
     "autor": "Andrew S. Grove",
     "fuente": "grove_high_output",
     "fecha_corte": "1983, ano en que el autor escribio el libro segun cap_01 L13; la ficha canonica registra la edicion de 2015"
   }
 ],
 "fuentes": [{"clave": "grove_high_output", "fecha": "2026-09-19"}],
 "denominaciones": {
   "nombre_largo": "La duracion y el sitio de la reunion individual: la hora como minimo sostenida en el tiempo que pide un asunto espinoso, y el area de trabajo del subordinado como sitio, con las cuatro cosas que alli se aprenden mirando",
   "sigla": "",
   "otros_idiomas": [{"idioma": "ingles", "termino": "one-on-one"}]
 },
 "condiciones_activacion": "Cuando vas a programar la reunion individual con un subordinado y tienes que poner en el calendario cuanto va a durar y en que sitio se tiene.",
 "entregable_esperado": "La reunion individual programada con una duracion de una hora como minimo y situada en el area de trabajo del subordinado o cerca de ella, mas lo que hayas aprendido mirando ese sitio.",
 "pasos_accionables": [
   "Cuenta con que a cuanto tiene que durar no hay de verdad una respuesta, pero con que el subordinado tiene que sentir que hay tiempo suficiente para sacar los asuntos espinosos y meterse en ellos.",
   "Comprueba ese criterio poniendote en su sitio: si tuvieras un problema grande al que quisieras dar vueltas con tu supervisor, que es la persona cuyo interes profesional en el asunto solo va por detras del tuyo, no querrias sacarlo en una reunion programada para durar solo quince minutos.",
   "Haz que la reunion individual dure una hora como minimo.",
   "Cuenta con que cualquier cosa menos que eso tiende a hacer que el subordinado se limite a las cosas sencillas que se despachan deprisa.",
   "Ten la reunion en el area de trabajo del subordinado o cerca de ella siempre que se pueda, y no en la del supervisor ni en otro sitio.",
   "Aprovecha que un supervisor aprende mucho con solo ir al despacho de su subordinado.",
   "Mira si esta organizado o no.",
   "Mira si tiene que pasar tiempo una y otra vez buscando un documento que quiere.",
   "Mira si lo interrumpen todo el rato, o si no lo interrumpen nunca.",
   "Mira en general como se enfrenta el subordinado a su trabajo."
 ],
 "resumen_teorico": (
  "UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_05.md, unidad Cap. 4, titulo textual Meetings, The Medium of Managerial Work. "
  "Sale de la PIEZA P12 de la frontera de cap_05 publicada en la vuelta 50 (LL.4.b), L37 a L39, 195 palabras. "
  "LAS PALABRAS LAS RECOMPUTE YO EN LA VUELTA 51 ANTES DE CORTAR y reproducen la frontera al digito: 195, que es lo que LL.4.b publica (.v51/palabras_tramos.txt). "
  "LA FRONTERA DENTRO DEL NODO, ESCRITA ANTES DE CORTAR: el tramo son DOS renglones con una linea en blanco en medio (L38), y los dos son de este nodo. Los pasos 1 a 4 salen de L37 (CUANTO DURA) y los pasos 5 a 10 de L39 (DONDE SE TIENE). CERO frontera de libro (una sola fuente) y CERO prestamo de tramos vecinos. "
  "POR QUE SON UN SOLO NODO Y NO DOS, que es la pregunta que este tramo abre: la frontera de LL.4.b los da como una sola pieza, y los sostengo juntos porque las dos preguntas son la misma decision de calendario (cuanto y donde se programa la misma reunion) y porque el libro las escribe seguidas con la misma forma de pregunta y respuesta. SI EL AUDITOR LOS PARTE, lo que sale son dos nodos de 4 y de 6 pasos, y el corte va limpio entre el paso 4 y el paso 5, que es donde cambia el renglon. Lo dejo escrito aqui para que partirlo cueste una lectura y no una reextraccion. "
  "POR QUE ES PROCEDIMIENTO: el libro pone SU PROPIO INVENTARIO y ademas pone SU PROPIA CIFRA (EXTRACTOR.md 9.1). "
  "Nombra uno a uno: el criterio de duracion (enough time to broach and get into thorny issues), su contraste (fifteen minutes), la cifra (an hour at a minimum), lo que pasa por debajo (confine himself to simple things), el sitio elegido entre los tres que el mismo enumera (in or near the subordinate's work area, frente a the supervisor's office y somewhere else) y las CUATRO cosas que alli se miran, nombradas una a una. "
  "Y EL CRITERIO NO ES UN ADJETIVO DE ADECUACION: no dice una duracion razonable ni un sitio apropiado, da una cifra y elige un sitio entre tres. "
  "DE DONDE SALE CADA PASO, uno a uno: "
  "paso 1 (L37: How long should a one-on-one meeting last? There really is no answer to this, but the subordinate must feel that there is enough time to broach and get into thorny issues); "
  "paso 2 (L37: Look at it this way. If you had a big problem that you wanted to kick around with your supervisor, the person whose professional interest in the matter is second only to yours, would you want to bring it up in a meeting scheduled to last only fifteen minutes? You would not); "
  "paso 3 (L37: I feel that a one-on-one should last an hour at a minimum); "
  "paso 4 (L37: Anything less, in my experience, tends to make the subordinate confine himself to simple things that can be handled quickly); "
  "paso 5 (L39: Where should a one-on-one take place? In the supervisor's office, in the subordinate's office, or somewhere else? I think you should have the meeting in or near the subordinate's work area if possible); "
  "paso 6 (L39: A supervisor can learn a lot simply by going to his subordinate's office); "
  "paso 7 (L39: Is he organized or not?); "
  "paso 8 (L39: Does he repeatedly have to spend time looking for a document he wants?); "
  "paso 9 (L39: Does he get interrupted all the time? Never?); "
  "paso 10 (L39: And in general, how does the subordinate approach his work?). "
  "NOTA DE TRANSCRIPCION: en el paso 2 el original encierra la aposicion entre guiones largos. Los cito como comas porque el barrido de esta casa no admite guiones largos ni medios, y lo citado no cambia. "
  "RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 10 pasos, 10 TRANSCRIPCION, 0 PUENTE. "
  "DONDE ESTUVE A PUNTO DE ESCRIBIR UN PUENTE Y NO LO ESCRIBI, especie EL DESTINATARIO: iba a escribir que se HACE con lo que se aprende mirando el sitio (anotarlo, tratarlo en la propia reunion, llevarlo a la evaluacion). L39 pone las cuatro preguntas y NO dice que hacer con las respuestas: las deja como lo que el supervisor aprende. Los pasos 7 a 10 escriben MIRA y paran ahi. "
  "SEGUNDO SITIO DE TENTACION, especie EL PERIODO: iba a escribir un maximo de duracion, porque el libro da un minimo y el minimo pide su techo. El libro NO pone techo: dice an hour at a minimum y no dice hasta cuanto. Escribir un maximo seria cerrar un bucle que el libro deja abierto, que es la definicion de PUENTE del corolario de 9.1. "
  "TERCER SITIO DE TENTACION, especie EL RESPONSABLE: iba a escribir quien elige el sitio de los tres. L39 escribe I think you should have the meeting, o sea el propio mando que lee, y el paso 5 se queda en eso sin nombrar a nadie mas. "
  "LAS CIFRAS SON DEL AUTOR Y VIAJAN COMO TALES (manual principios 5 y 8): la hora como minimo, el contraste de los quince minutos y lo que pasa por debajo van en UNA sola atribucion, con autor, fuente y fecha de corte. Van juntas y no en tres porque el libro las escribe como un solo argumento de duracion, y partirlas fabricaria tres cifras donde el texto pone una escala. "
  "LO QUE NO ESCRIBO Y POR ESO NO ESTA AQUI: NO escribo que hacer si el area de trabajo del subordinado no permite hablar en privado, porque el libro no lo plantea; NO escribo con que frecuencia se tiene, que es la pieza P11 y su propio nodo; NO escribo que se trata dentro, que es la pieza P14 y su propio nodo. "
  "ARISTAS DECLARADAS POR LECTURA, para cablearlas el dia de la insercion y no hoy (D.39 mide la puerta CERRADA para este libro en esta vuelta): "
  "(1) D.29 hacia la CABEZA usar_tres_clases_reunion_proceso, el candidato 2 de esta misma tanda: este nodo es un MEDIO de la primera de las tres clases que aquella cabeza nombra. La etiqueta es D.29 y no D.37 por la razon escrita en la ficha de la cabeza. "
  "(2) D.29, PARIENTE POR CONTRASTE dirigir_reunion_individual_semanal, del grafo y de zhuo_manager, cuyo paso 2 fija no menos de treinta minutos. ESTE NODO FIJA UNA HORA COMO MINIMO. Los dos ponen un suelo de duracion para la misma reunion y ponen suelos DISTINTOS, asi que el dia que se cablee hay que leer los dos delante y declarar el contraste, no fundirlos. "
  "(3) D.29, PARIENTE fijar_frecuencia_reunion_individual_madurez_tarea, el candidato 3 de esta misma tanda: aquel pone CADA CUANTO y este CUANTO Y DONDE. Son las tres decisiones de calendario de la misma reunion y no comparten ni un paso. "
  "DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO: el paso 2 es un EXPERIMENTO MENTAL y no un acto, y ademas es largo. Lo sostengo porque es lo unico del tramo que da el mecanismo del criterio de duracion (por que hace falta tiempo bastante) y porque el libro lo escribe en imperativo (Look at it this way). Si cae, cae DENTRO de mi marcado. "
  "SEGUNDO DISCUTIBLE: tener este tramo por UN nodo y no por DOS, con el corte escrito arriba entre el paso 4 y el paso 5. Si el auditor lo parte, cae DENTRO de mi marcado y el arreglo es barato porque el corte ya esta dicho."
 )
}
p = pathlib.Path("cuarentena/grove_high_output/%s.json" % d["id"])
assert not p.exists(), "ya existe"
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("escrito", p, len(d["pasos_accionables"]), "pasos")
