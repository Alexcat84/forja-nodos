# -*- coding: utf-8 -*-
import json, io

d = {
 "id": "buscar_regularidad_bloques_iguales_trabajo_mando",
 "titulo": "Buscar la regularidad en el trabajo de mando alisando la carga, abriendo ventanas en la caja negra, y usando los mismos bloques de tiempo para las actividades iguales",
 "dominio": "gestion_equipos",
 "estado": "vivo",
 "ids_alias": [],
 "nodos_previos": [],
 "nodos_siguientes": [],
 "atribuciones": [],
 "fuentes": [{"clave": "grove_high_output", "fecha": "2026-09-19"}],
 "denominaciones": {
   "nombre_largo": "El concepto de produccion de la regularidad aplicado al trabajo de mando: parar los parones y arranques, buscar la bomba de relojeria antes de que estalle, y coordinar los bloques de tiempo con los demas mandos",
   "sigla": "",
   "otros_idiomas": [
     {"idioma": "ingles", "termino": "regularity"},
     {"idioma": "ingles", "termino": "black box"},
     {"idioma": "ingles", "termino": "job shop"}
   ]
 },
 "condiciones_activacion": "Cuando tu jornada de mando se te llena de parones y arranques y las actividades iguales te caen en momentos distintos cada semana.",
 "entregable_esperado": "Una jornada de mando con la carga alisada y los mismos bloques de tiempo reservados para las actividades iguales, coordinados con los demas mandos, y las fuentes de problemas futuros de prioridad alta buscadas antes de que estallen.",
 "pasos_accionables": [
   "Aplica a tu trabajo de mando el siguiente concepto de produccion: ve hacia la regularidad.",
   "Alisa tu carga de trabajo todo lo que puedas, aunque no puedas controlar los habitos de los que te llegan, igual que una fabrica de desayunos iria mas eficiente si los clientes llegaran en un flujo estable y predecible en vez de entrar de uno en uno y de dos en dos.",
   "Haz que tu trabajo de mando tome las caracteristicas de una fabrica y no las de un taller a pedido.",
   "Impide en consecuencia, con todo lo que puedas, los pequenos parones y arranques de tu jornada, y tambien las interrupciones que traen las emergencias grandes.",
   "Busca siempre las fuentes de problemas futuros de prioridad alta abriendo ventanas en la caja negra de tu organizacion, aunque algunas de esas emergencias sean inevitables.",
   "Cuenta con lo que ganas al reconocer que tienes una bomba de relojeria entre manos: puedes atender el problema cuando tu quieras y no despues de que la bomba haya estallado.",
   "Coordina tu trabajo con el de los demas mandos, porque solo puedes ir hacia la regularidad si los otros van tambien.",
   "Usa, dicho de otro modo, los mismos bloques de tiempo para las actividades iguales.",
   "Toma el ejemplo que el libro da de Intel: las mananas de los lunes se apartaron en toda la empresa como el momento en que se reunen los grupos de planificacion, asi que quien pertenece a uno puede contar con el lunes para eso y queda libre de choques de agenda."
 ],
 "resumen_teorico": (
  "UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_04.md, unidad Cap. 3, titulo textual Managerial Leverage. "
  "Sale de la PIEZA P39 de la frontera publicada en la vuelta 46 (HH.2.c), L303 a L307, 242 palabras. "
  "EL TRAMO ENTERO ES DE ESTE NODO: cero frontera interna y cero solapes con ningun otro candidato. L303 es el rotulo de seccion (Interruptions, The Plague of Managerial Work) y no pone paso. "
  "POR QUE ES PROCEDIMIENTO: el libro pone SU PROPIO INVENTARIO de los medios, nombrados uno a uno (alisar la carga, dar al trabajo de mando las caracteristicas de una fabrica y no las de un taller a pedido, impedir los parones y arranques y las interrupciones de las emergencias grandes, abrir ventanas en la caja negra para buscar las fuentes de problemas futuros, coordinar con los demas mandos, y usar los mismos bloques de tiempo para las actividades iguales). "
  "Es inventario de MEDIOS y de OBJETOS DE TRABAJO y no de metas, y el criterio no es un adjetivo de adecuacion: el libro dice exactamente que se agrupa (las actividades iguales) y exactamente contra que (los mismos bloques de tiempo). "
  "DE DONDE SALE CADA PASO, uno a uno: paso 1 (L305: The next important production concept we can apply to managerial work is to strive toward regularity); "
  "paso 2 (L305: We could obviously run our breakfast factory more efficiently if customers arrived in a steady and predictable stream rather than dropping in by ones and twos. Though we cannot control our customers habits, we should try to smooth out our workload as much as possible); "
  "paso 3 (L305: As noted, we should try to make our managerial work take on the characteristics of a factory, not a job shop); "
  "paso 4 (L305: Accordingly, we should do everything we can to prevent little stops and starts in our day as well as interruptions brought on by big emergencies); "
  "paso 5 (L305: Even though some of the latter are unavoidable, we should always be looking for sources of future high-priority trouble by cutting windows into the black box of our organization); "
  "paso 6 (L305: Recognizing you have got a time bomb on your hands means you can address a problem when you want to, not after the bomb has gone off); "
  "paso 7 (L307: But because you must coordinate your work with that of other managers, you can only move toward regularity if others do too); "
  "paso 8 (L307: In other words, the same blocks of time must be used for like activities); "
  "paso 9 (L307: For example, at Intel Monday mornings have been set aside throughout the corporation as the time when planning groups meet. So anybody who belongs to one can count on Monday for that purpose and be free of scheduling conflicts). "
  "RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 9 pasos, 9 TRANSCRIPCION, 0 PUENTE. "
  "DONDE ESTUVE A PUNTO DE ESCRIBIR UN PUENTE Y NO LO ESCRIBI, especie EL PERIODO Y LA CIFRA: iba a escribir un paso que mandara reservar UN bloque semanal fijo, tomando la manana del lunes de Intel como la medida. "
  "El libro da el lunes como EJEMPLO de una empresa (For example, at Intel) y NO como periodo a seguir: la regla que escribe es que los mismos bloques se usen para las actividades iguales, sin decir cuantos, ni cuan largos, ni cada cuanto. "
  "Por eso el paso 8 escribe la regla sin cifra y el paso 9 escribe el ejemplo NOMBRADO COMO EJEMPLO, que es lo que manual 3.5 manda: el caso vive dentro de la doctrina y el entregable de la ficha no lleva ni un dato del caso. "
  "SEGUNDO SITIO DE TENTACION, especie EL INVENTARIO INVENTADO: iba a enumerar QUE ventanas se abren en la caja negra (indicadores, recorridos por el area, reuniones de uno a uno). El renglon dice cutting windows into the black box y no nombra ni una. La lista habria sido mia. "
  "LO QUE NO ESCRIBO Y POR ESO NO ESTA AQUI: NO escribo COMO se alisa la carga, ni CON QUIEN se coordina primero, ni QUE actividades son iguales entre si, porque el tramo no lo pone. "
  "Y NO TRAIGO AQUI NI LAS RESPUESTAS ESTANDAR (L315), NI EL AGRUPAR LAS INTERRUPCIONES EN LAS REUNIONES (L317), NI EL CARTEL Y LA HORA DE OFICINA ABIERTA (L321), que son P41, P42 y P44 de la frontera y tienen nodo propio en la vuelta 49. Ese es el corte del tramo de hoy. "
  "ARISTAS DECLARADAS POR LECTURA, para cablearlas el dia de la insercion y no hoy: "
  "(1) D.37, CABEZA subir_productividad_gerencial_tres_vias, paso 2 (sube el ritmo), que es la via de la que cuelgan los principios de produccion de este tramo del libro. "
  "(2) D.29, HERMANO agrupar_tareas_semejantes_aprovechar_preparacion, porque aquel agrupa las tareas semejantes para aprovechar la preparacion y este pone esos grupos SIEMPRE EN EL MISMO BLOQUE y los coordina con los demas mandos. Son la misma serie de principios de produccion y no comparten ni un paso: alli el objeto es la preparacion, aqui es la regularidad del bloque. "
  "(3) D.29, HERMANO usar_calendario_herramienta_planificacion_produccion, el candidato 1 de esta misma tanda, porque el calendario es la sede donde esos bloques iguales se colocan. "
  "(4) D.29, PARIENTE representar_actividad_caja_negra_ventanas, porque el paso 5 de este nodo manda abrir ventanas en la caja negra y quien despliega esa operacion es aquel nodo: este la NOMBRA y no repite sus pasos. "
  "LAS ARISTAS HACIA NODOS QUE AUN NO EXISTEN VAN POR SU TRAMO Y NO POR UN ID INVENTADO DE ANTEMANO (encargo de la vuelta 48, 2.b). Las cuatro de arriba apuntan a ids que ya viven en el dataset o en la bandeja, comprobado antes de escribirlas. "
  "TRADUCCION DECLARADA: regularity, black box y job shop viajan en denominaciones. "
  "DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO: el paso 9 es un CASO y no un acto, y un lector estricto dira que un ejemplo no pone paso y que el nodo termina en el 8. "
  "Lo sostengo porque es lo unico del tramo que ensena COMO se ve un bloque igual coordinado de verdad (un dia de la semana, para toda la empresa, para una clase de reunion), y porque manual 3.5 manda exactamente esto: que el caso entre nombrado dentro de la doctrina. Si cae, cae DENTRO de mi marcado. "
  "SEGUNDO DISCUTIBLE: el paso 6 es una CONSECUENCIA y no un acto, y ademas cierra el argumento del paso 5 en vez de anadir algo que hacer. Lo sostengo porque es lo unico que dice PARA QUE se abren las ventanas, y sin el el paso 5 queda en una busqueda sin destino."
 )
}

io.open('cuarentena/grove_high_output/buscar_regularidad_bloques_iguales_trabajo_mando.json', 'w', encoding='utf-8', newline='\n').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('escrito')
