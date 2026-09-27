# -*- coding: utf-8 -*-
"""EL CANDIDATO 1 DE LA VUELTA 50, PIEZA P41 DE cap_04 (L315 a L315, 92 palabras)."""
import io
import json

resumen = (
 "UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_04.md, unidad Cap. 3, titulo textual Managerial Leverage. "
 "Sale de la PIEZA P41 de la frontera publicada en la vuelta 46 (HH.2.c), L315 a L315, 92 palabras. "
 "LAS 92 PALABRAS SON LAS QUE LA FRONTERA PUBLICA Y NO UNA CIFRA MIA: las recompute en la vuelta 50 con el mismo "
 "recuento de .v46/frontera.py linea 136 y me dan 92, identicas, antes de escribir esta ficha. "
 "EL TRAMO ENTERO ES DE ESTE NODO: cero frontera interna y cero solapes con ningun otro candidato. "
 "L315 es una sola linea de prosa corrida y no lleva rotulo. "
 "POR QUE ES PROCEDIMIENTO: el libro pone SU PROPIO INVENTARIO de los medios, nombrados uno a uno (aplicar el concepto "
 "de produccion del producto estandar, fijar que clase de interrupciones estas recibiendo, preparar respuestas estandar "
 "para las que mas aparecen, bajar con ellas el tiempo gastado en atender interrupciones, y tenerlas disponibles para "
 "delegar buena parte del trabajo en personal con menos experiencia). Es inventario de MEDIOS y de OBJETOS DE TRABAJO y "
 "no de metas, y el criterio no es un adjetivo de adecuacion: el libro dice exactamente que se prepara (respuestas "
 "estandar) y exactamente para que interrupciones (las que salen a la superficie una y otra vez). "
 "DE DONDE SALE CADA PASO, uno a uno: "
 "paso 1 (L315: There are better ways. Let's apply a production concept. Manufacturers turn out standard products); "
 "paso 2 (L315: By analogy, if you can pin down what kind of interruptions you're getting); "
 "paso 3 (L315: you can prepare standard responses for those that pop up most often); "
 "paso 4 (L315: Customers don't come up with totally new questions and problems day in and day out, and because the "
 "same ones tend to surface repeatedly); "
 "paso 5 (L315: a manager can reduce time spent handling interruptions using standard responses); "
 "paso 6 (L315: Having them available also means that a manager can delegate much of the job to less experienced personnel). "
 "RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 6 pasos, 6 TRANSCRIPCION, 0 PUENTE. "
 "DONDE ESTUVE A PUNTO DE ESCRIBIR UN PUENTE Y NO LO ESCRIBI, especie EL INVENTARIO INVENTADO: iba a escribir un paso "
 "que mandara CLASIFICAR las interrupciones en categorias y llevar un registro de su frecuencia para saber cuales son "
 "las mas frecuentes. El renglon dice pin down what kind of interruptions you're getting y no nombra ni un metodo, ni "
 "un registro, ni una categoria. El metodo habria sido mio, asi que el paso 2 escribe el acto que el libro escribe y "
 "para ahi. "
 "SEGUNDO SITIO DE TENTACION, especie EL RESPONSABLE Y EL PERIODO: iba a escribir cada cuanto se revisan esas "
 "respuestas estandar y quien las mantiene. El renglon no pone ni periodo ni responsable: dice Having them available, y "
 "nada mas. "
 "LO QUE NO ESCRIBO Y POR ESO NO ESTA AQUI: NO escribo COMO se redacta una respuesta estandar, ni DONDE se guardan, ni "
 "CUANTAS clases de interrupcion hay, porque el tramo no lo pone. Y NO TRAIGO AQUI NI EL AGRUPAR LAS INTERRUPCIONES EN "
 "LAS REUNIONES REGULARES (L317), NI EL BANCO DE INDICADORES (L319), NI EL CARTEL Y LA HORA DE OFICINA ABIERTA (L321), "
 "que son P42, P43 y P44 de la frontera: los dos primeros tienen nodo propio en esta misma vuelta y P43 no tiene nodo "
 "por P.19, porque su objeto ya vive entero en archivar_indicadores_resolver_problemas de cap_03. Ese es el corte del "
 "tramo de hoy. "
 "ARISTAS DECLARADAS POR LECTURA, para cablearlas el dia de la insercion y no hoy: "
 "(1) D.29, MADRE subir_productividad_gerencial_tres_vias, cuyo paso 2 manda subir el ritmo con el que ejecutas tus "
 "actividades: este nodo es uno de los principios de produccion que el libro pone bajo el rotulo Increasing Managerial "
 "Activity Rate: Speeding Up the Line (L259), y por eso despliega en 6 pasos lo que aquel paso nombra en una linea. LA "
 "DECLARO D.29 Y NO D.37, Y LO RAZONO CONTRA MI PROPIO INTERES: la cabeza dice TRES vias y las nombra (el ritmo, la "
 "palanca y la mezcla), asi que sus partes de D.37 son esas tres y este nodo no es ninguna de las tres, sino un medio de "
 "la primera. D.37 exige que la parte sea LA QUE ESE PASO NOMBRA, y el paso 2 nombra el ritmo y no las respuestas "
 "estandar. "
 "(2) D.29, HERMANO buscar_regularidad_bloques_iguales_trabajo_mando, porque los dos salen de la misma seccion de "
 "interrupciones (Interruptions, The Plague of Managerial Work, L303) y no comparten ni un paso: alli el objeto es la "
 "regularidad del bloque de tiempo, aqui es la respuesta preparada de antemano. "
 "(3) D.29, HERMANO el nodo que sale de L317, que agrupa las interrupciones de los subordinados en las reuniones "
 "regulares: es el segundo remedio del mismo parrafo y ataca la MISMA interrupcion por otro sitio, el CUANDO se atiende "
 "en vez del QUE se responde. "
 "(4) D.29, HERMANO el nodo que sale de L321, el cartel en la puerta y la hora de oficina abierta: es el tercer remedio "
 "de la misma seccion. "
 "LAS DOS ULTIMAS VAN POR SU TRAMO Y NO POR UN ID, porque cuando escribo esta ficha esos dos nodos no existen todavia en "
 "ninguna sede, y un id inventado de antemano deja la arista colgada sin que ninguna guarda lo cante (leccion de JJ.2.b). "
 "Las dos primeras apuntan a ids que ya viven en la bandeja, comprobado antes de escribirlas. "
 "TRADUCCION DECLARADA: standard products, standard responses e interruptions viajan en denominaciones. "
 "DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO: el paso 4 es una CONSTATACION y no un acto, y un lector estricto dira "
 "que un nodo no manda contar con algo. Lo sostengo porque es la premisa sin la cual el paso 3 no tiene criterio: el "
 "libro pone ahi POR QUE las respuestas estandar funcionan (las mismas preguntas vuelven), y sin esa linea el paso 3 "
 "manda preparar respuestas para las mas frecuentes sin decir por que existen las mas frecuentes. Si cae, cae DENTRO de "
 "mi marcado. "
 "SEGUNDO DISCUTIBLE: declaro la arista 1 como D.29 y la ficha de P39 de la vuelta 48 declara esa MISMA relacion con "
 "esta MISMA cabeza como D.37. Un lector estricto dira que dos fichas del mismo capitulo no pueden etiquetar distinto la "
 "misma arista. Lo sostengo porque D.37 pide que la parte sea la que el paso nombra y el paso 2 nombra el ritmo, no el "
 "principio de produccion; y lo dejo dicho aqui en vez de callarlo, porque la diferencia se ve al leer las dos fichas "
 "juntas. NO TOCO la ficha de P39: no es mi encargo de hoy y no abro doctrina (D.56)."
)

ficha = {
  "id": "preparar_respuestas_estandar_interrupciones_repetidas",
  "titulo": "Preparar respuestas estandar para las clases de interrupcion que se repiten, y tenerlas disponibles para delegar buena parte del trabajo en personal con menos experiencia",
  "dominio": "gestion_equipos",
  "estado": "vivo",
  "ids_alias": [],
  "nodos_previos": [],
  "nodos_siguientes": [],
  "atribuciones": [],
  "fuentes": [{"clave": "grove_high_output", "fecha": "2026-09-19"}],
  "denominaciones": {
    "nombre_largo": "El concepto de produccion del producto estandar aplicado a las interrupciones del trabajo de mando: fijar que clase de interrupcion te llega, preparar de antemano la respuesta de las que mas se repiten, y delegarlas",
    "sigla": "",
    "otros_idiomas": [
      {"idioma": "ingles", "termino": "standard products"},
      {"idioma": "ingles", "termino": "standard responses"},
      {"idioma": "ingles", "termino": "interruptions"}
    ]
  },
  "condiciones_activacion": "Cuando las mismas preguntas y los mismos problemas te llegan como interrupcion una y otra vez, y cada vez los atiendes desde cero.",
  "entregable_esperado": "Un juego de respuestas estandar preparadas para las clases de interrupcion que mas aparecen, disponibles y por eso delegables en personal con menos experiencia.",
  "pasos_accionables": [
    "Aplica a las interrupciones que te llegan el siguiente concepto de produccion, porque hay formas mejores que esconderte: los fabricantes sacan productos estandar.",
    "Fija por esa analogia que clase de interrupciones estas recibiendo.",
    "Prepara respuestas estandar para las que aparecen mas a menudo.",
    "Cuenta con lo que hace que eso funcione: los clientes no salen con preguntas y problemas totalmente nuevos un dia tras otro, y las mismas tienden a aflorar una y otra vez.",
    "Reduce con esas respuestas estandar el tiempo que gastas atendiendo interrupciones.",
    "Ten esas respuestas disponibles, porque tenerlas a mano es ademas lo que te deja delegar buena parte de ese trabajo en personal con menos experiencia."
  ],
  "resumen_teorico": resumen
}

RUTA = "cuarentena/grove_high_output/preparar_respuestas_estandar_interrupciones_repetidas.json"
with io.open(RUTA, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(ficha, fh, ensure_ascii=False, indent=2)
    fh.write("\n")

texto = io.open(RUTA, encoding="utf-8").read()
print("escrito %s" % RUTA)
print("pasos: %d" % len(ficha["pasos_accionables"]))
print("guion largo dentro: %s   guion medio dentro: %s"
      % (chr(0x2014) in texto, chr(0x2013) in texto))
