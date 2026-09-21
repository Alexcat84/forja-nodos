# -*- coding: utf-8 -*-
import json, io

d = {
 "id": "supervisar_decision_delegada_preguntas_concretas",
 "titulo": "Supervisar una decision delegada por su proceso de reflexion: preguntas bastante concretas en la reunion de revision",
 "dominio": "gestion_equipos",
 "estado": "vivo",
 "ids_alias": [],
 "nodos_previos": [],
 "nodos_siguientes": [],
 "atribuciones": [],
 "fuentes": [{"clave": "grove_high_output", "fecha": "2026-09-19"}],
 "denominaciones": {
   "nombre_largo": "Como se supervisa lo que no es una tarea sino una decision: mirando el proceso de decision del subordinado en vez de rehacer su reflexion",
   "sigla": "",
   "otros_idiomas": [
     {"idioma": "ingles", "termino": "monitoring their decision-making process"},
     {"idioma": "ingles", "termino": "review meeting"}
   ]
 },
 "condiciones_activacion": "Cuando lo que has delegado en un subordinado no es una tarea sino un tipo de decision, y tienes que aprobarla sin volver a hacer tu mismo toda la reflexion que el ya hizo.",
 "entregable_esperado": "La decision delegada aprobada o no aprobada segun lo bien que el subordinado responda en la reunion de revision a preguntas bastante concretas sobre su peticion, y sin que tu hayas tenido que recorrer su reflexion entera.",
 "pasos_accionables": [
   "Cuenta con que hay tipos de decision que los mandos delegan con frecuencia en sus subordinados.",
   "Supervisa esa delegacion por su proceso de decision, que es la mejor manera de hacerla.",
   "Pide al subordinado que piense el asunto entero con cuidado antes de presentarte su peticion de aprobacion.",
   "Para supervisar lo buena que es su reflexion, hazle preguntas bastante concretas sobre su peticion durante una reunion de revision.",
   "Si las responde de forma convincente, aprueba lo que pide.",
   "Cuenta con que esta tecnica te permite averiguar lo buena que es la reflexion sin tener que recorrerla tu mismo."
 ],
 "resumen_teorico": (
  "UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_04.md, unidad Cap. 3, titulo textual Managerial Leverage. "
  "Sale de la PIEZA P30 de la frontera publicada en la vuelta 46 (HH.2.c), L257 a L257, 106 palabras, y de ningun otro tramo. "
  "POR QUE ES PROCEDIMIENTO: el libro no solo nombra la respuesta, la despliega en sus etapas con sus dos preguntas encadenadas escritas a proposito (How is this best done? By monitoring their decision-making process. How do you do that?) y pone el inventario de lo que hay que hacer: pedir la reflexion previa, hacer preguntas concretas, la reunion de revision, y la regla de aprobacion. "
  "Es inventario de ETAPAS DE TRABAJO y no de metas, y el criterio de aprobacion que da (si responde de forma convincente) es del libro y no mio. "
  "DE DONDE SALE CADA PASO, uno a uno, y los seis salen de L257: paso 1 (Making certain types of decisions is something managers frequently delegate to subordinates); "
  "paso 2 (How is this best done? By monitoring their decision-making process); "
  "paso 3 (We ask a subordinate to think through the entire matter carefully before presenting a request for approval); "
  "paso 4 (And to monitor how good his thinking is, we ask him quite specific questions about his request during a review meeting); "
  "paso 5 (If he answers them convincingly, we will approve what he wants); "
  "paso 6 (This technique allows us to find out how good the thinking is without having to go through it ourselves). "
  "RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 6 pasos, 6 TRANSCRIPCION, 0 PUENTE. "
  "EL CASO ENTRA NOMBRADO Y SIN SU DATO (manual 3.5): el caso es la aprobacion de una compra de equipo de capital en Intel, y el nodo NO se lo lleva. "
  "Ni el entregable ni ningun paso dicen equipo de capital ni Intel: la senial barata de que un caso se hizo la casa es que el entregable lleve un dato del caso, y aqui el entregable dice la decision delegada. "
  "LO QUE NO ESCRIBO Y POR ESO NO ESTA AQUI: NO escribo CUALES son las preguntas concretas, porque el libro dice quite specific questions y no las enumera. "
  "Escribir una lista de preguntas seria la especie mas cara de EXTRACTOR.md 15.4, un inventario inventado bajo un adjetivo del libro. "
  "NO escribo tampoco que tipos de decision se delegan: el libro dice certain types y no los nombra. "
  "ARISTAS DECLARADAS POR LECTURA, para cablearlas el dia de la insercion y no hoy: "
  "(1) D.29, MADRE delegar_tarea_base_comun_seguimiento, cuyo paso 7 manda supervisar lo delegado en una linea y este nodo lo despliega para el caso de una decision. "
  "(2) D.29, HERMANO supervisar_tarea_delegada_etapa_menor_valor: mismo seguimiento, objeto distinto (una decision, no una tarea), y el libro los separa en dos tramos consecutivos. "
  "DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO, y es el mismo reparo que la vuelta 46 se marco a si misma en dos nodos (HH.5.f discutibles 3 y 4): LOS PASOS 3, 4 Y 5 SALEN DEL CASO. "
  "El libro los escribe dentro de Let us examine what Intel goes through, y un lector estricto dira que un caso no deberia poner pasos, y que este nodo se queda en los pasos 1, 2 y 6, que es una definicion y no un procedimiento. "
  "Lo sostengo porque el libro presenta el caso como la RESPUESTA a su propia pregunta How do you do that?, o sea como el despliegue del procedimiento y no como una ilustracion posterior, y porque los tres pasos estan escritos en presente generico (we ask, we ask him, we will approve) y no en pasado narrativo. "
  "Si cae, cae DENTRO de mi marcado, y el nodo entero cae con el: sin esos tres pasos no queda procedimiento."
 )
}

io.open('cuarentena/grove_high_output/supervisar_decision_delegada_preguntas_concretas.json', 'w', encoding='utf-8', newline='\n').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('escrito')
