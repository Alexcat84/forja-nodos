# -*- coding: utf-8 -*-
import json, io

d = {
 "id": "decir_no_trabajo_excede_capacidad",
 "titulo": "Decir que no de salida al trabajo que excede tu capacidad, antes y no despues, usando tu propia idea del tiempo que cada cosa te lleva",
 "dominio": "gestion_equipos",
 "estado": "vivo",
 "ids_alias": [],
 "nodos_previos": [],
 "nodos_siguientes": [],
 "atribuciones": [],
 "fuentes": [{"clave": "grove_high_output", "fecha": "2026-09-19"}],
 "denominaciones": {
   "nombre_largo": "La segunda responsabilidad del calendario: el nivel de entrada que no se deja sobrecargar, el no explicito frente al no implicito, y el coste de abortar tarde",
   "sigla": "",
   "otros_idiomas": [
     {"idioma": "ingles", "termino": "say no at the outset"},
     {"idioma": "ingles", "termino": "capacity"},
     {"idioma": "ingles", "termino": "bottleneck"}
   ]
 },
 "condiciones_activacion": "Cuando te llega trabajo por encima de lo que puedes atender y lo aceptas porque no sabes medir tu propia capacidad.",
 "entregable_esperado": "El trabajo que excede tu capacidad rechazado de salida y de forma explicita, apoyado en tu propia idea del tiempo que cada cosa te lleva, y no abortado mas tarde cuando ya haya subido de etapa.",
 "pasos_accionables": [
   "Aplica aqui otro principio de produccion: la gente de fabricacion se fia de sus indicadores y no deja que el material empiece su recorrido por la fabrica si cree que ya esta operando a plena capacidad.",
   "Cuenta con el motivo: si lo dejaran, el material podria llegar hasta la mitad del recorrido y acumularse detras de un cuello de botella.",
   "Haz lo que hacen los jefes de fabrica: di que no de salida y evita que el nivel de entrada sobrecargue el sistema.",
   "Cuenta con que a otras clases de mando esto les resulta dificil de aplicar porque sus indicadores de capacidad no estan tan asentados ni son tan creibles.",
   "Preguntate cuanto tiempo necesitas para leer tu correo, para escribir tus informes o para reunirte con un colega: puede que no lo sepas con precision, pero seguro que tienes una idea del tiempo que hace falta.",
   "Explota esa idea tuya para programar tu trabajo.",
   "Acepta la segunda de las dos responsabilidades que el libro numera: di que no de salida al trabajo que este por encima de tu capacidad de atenderlo.",
   "Dilo antes y no despues, porque esperar a que algo alcance una etapa de mayor valor y abortarlo entonces por falta de capacidad significa perder mas dinero y mas tiempo.",
   "Cuenta con que puedes decir que no de forma explicita o de forma implicita, porque al no entregar acabas diciendo algo que equivale a un no.",
   "Recuerda ademas que tu tiempo es tu unico recurso finito, y que cuando dices que si a una cosa estas diciendo inevitablemente que no a otra."
 ],
 "resumen_teorico": (
  "UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_04.md, unidad Cap. 3, titulo textual Managerial Leverage. "
  "Sale de la PIEZA P34 de la frontera publicada en la vuelta 46 (HH.2.c), L273 a L285, 469 palabras. "
  "FRONTERA DENTRO DEL TRAMO, PUBLICADA ANTES DE CORTAR (EXTRACTOR.md 10), porque P34 da DOS nodos y esta ficha es el segundo: "
  "de este nodo son L277 (el no de salida, el nivel de entrada y los indicadores de capacidad), la cabecera de L279 (las dos responsabilidades), L283 (la responsabilidad 2) y L285 (por que antes y no despues, el no explicito o implicito, y el recurso finito). "
  "Del otro nodo, usar_calendario_herramienta_planificacion_produccion, son L273, L275, la misma cabecera de L279 y L281. "
  "Los dos nodos comparten SOLO la cabecera de L279, que es la frase que los numera, y ninguna otra linea: cero solapes de contenido. "
  "POR QUE ES PROCEDIMIENTO: el libro pone SU PROPIO INVENTARIO de lo que hay que mirar y de lo que hay que hacer, nombrado uno a uno (los indicadores de capacidad, el nivel de entrada, las tres actividades cuyo tiempo hay que estimar, el momento del no, y las dos formas del no), y ademas pone el CRITERIO de cuando decirlo, que es de salida y no cuando la cosa ya subio de etapa. "
  "Es inventario de OBJETOS DE TRABAJO y de ETAPAS, no de metas, y el criterio no es un adjetivo de adecuacion. "
  "DE DONDE SALE CADA PASO, uno a uno: paso 1 (L277: Another production principle can be applied here. Because manufacturing people trust their indicators, they will not allow material to begin its journey through the factory if they think it is already operating at capacity); "
  "paso 2 (L277: If they did, material might go halfway through and back up behind a bottleneck); "
  "paso 3 (L277: Instead, factory managers say no at the outset and keep the start level from overloading the system); "
  "paso 4 (L277: Other kinds of managers find this hard to apply because their indicators of capacity are not as well established or not as believable); "
  "paso 5 (L277: How much time do you need to read your mail, to write your reports, to meet with a colleague? You may not know precisely, but you surely have a feel for the time required); "
  "paso 6 (L277: And you should exploit that sense to schedule your work); "
  "paso 7 (L279 y L283: you must accept responsibility for two things... 2. You should say no at the outset to work beyond your capacity to handle); "
  "paso 8 (L285: It is important to say no earlier rather than later because we have learned that to wait until something reaches a higher value stage and then abort due to lack of capacity means losing more money and time); "
  "paso 9 (L285: You can obviously say no either explicitly or implicitly, because by not delivering you end up saying what amounts to no); "
  "paso 10 (L285: Remember too that your time is your one finite resource, and when you say yes to one thing you are inevitably saying no to another). "
  "RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 10 pasos, 10 TRANSCRIPCION, 0 PUENTE. "
  "DONDE ESTUVE A PUNTO DE ESCRIBIR UN PUENTE Y NO LO ESCRIBI: iba a escribir un paso que mandara MEDIR tu capacidad y anotarla, que es lo que el paralelo de fabrica pedia a gritos. "
  "El libro no lo manda: dice exactamente lo contrario, que los indicadores de capacidad de un mando no estan asentados y que lo que hay es una IDEA del tiempo que hace falta (you may not know precisely, but you surely have a feel). "
  "El paso 5 escribe esa idea y no una medicion, y el paso 6 manda explotarla tal cual. Un paso de medicion habria sido un inventario mio bajo un renglon que dice que la medicion no existe. "
  "LO QUE NO ESCRIBO Y POR ESO NO ESTA AQUI: NO escribo COMO se dice que no, ni a quien, ni con que formula, porque el tramo no lo pone; "
  "y NO traigo aqui la primera responsabilidad de L281, que es del nodo hermano. "
  "EL RECURSO FINITO NO ES UN PUENTE AUNQUE SUENE A OTRO TRAMO: el libro lo escribe en L285 dentro de este parrafo y cerrando este argumento. "
  "Que la misma idea aparezca antes en P15 (L175) como POSTURA no la convierte en material de alli: la frontera de la vuelta 46 dejo P15 en cero nodos precisamente porque alli no hay procedimiento, y dijo que su procedimiento vive en P32 y siguientes. Este es uno de esos. "
  "ARISTAS DECLARADAS POR LECTURA, para cablearlas el dia de la insercion y no hoy: "
  "(1) D.37, CABEZA subir_productividad_gerencial_tres_vias, paso 2 (sube el ritmo), que es la via de la que cuelgan los principios de produccion de este tramo. "
  "(2) D.29, HERMANO usar_calendario_herramienta_planificacion_produccion, que es la otra responsabilidad de la misma frase numerada de L279. Hermandad declarada y no jerarquia: el libro las numera 1 y 2 al mismo nivel. "
  "(3) D.29, PARIENTE equilibrar_capacidad_personal_inventario_plazo, de cap_02, donde la capacidad y el cuello de botella viven como objetos de fabrica. Este nodo los aplica al tiempo de un mando y NO repite sus pasos. "
  "TRADUCCION DECLARADA: say no at the outset, capacity y bottleneck viajan en denominaciones. "
  "DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO: los pasos 1 y 2 son el paralelo de fabrica, o sea un CASO de otro dominio, y un lector estricto dira que un caso no deberia poner pasos y que el nodo empieza en el 3. "
  "Los sostengo porque el paso 3 empieza literalmente con Instead, o sea que el libro escribe el acto del mando COMO CONTRASTE del paralelo, y sin el paralelo el paso 3 se queda sin el de salida que es toda su carga. Si caen, caen DENTRO de mi marcado. "
  "LAS ARISTAS HACIA NODOS QUE AUN NO EXISTEN VAN POR SU TRAMO Y NO POR UN ID INVENTADO DE ANTEMANO (encargo de la vuelta 48, 2.b): las tres de arriba apuntan a ids que ya viven en el dataset o en la bandeja, comprobado antes de escribirlas."
 )
}

io.open('cuarentena/grove_high_output/decir_no_trabajo_excede_capacidad.json', 'w', encoding='utf-8', newline='\n').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('escrito')
