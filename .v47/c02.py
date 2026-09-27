# -*- coding: utf-8 -*-
import json, io

d = {
 "id": "delegar_tarea_base_comun_seguimiento",
 "titulo": "Delegar una tarea sobre una base comun de informacion, sin farsa y con su seguimiento, porque delegar sin seguimiento es abdicar",
 "dominio": "gestion_equipos",
 "estado": "vivo",
 "ids_alias": [],
 "nodos_previos": [],
 "nodos_siguientes": [],
 "atribuciones": [],
 "fuentes": [{"clave": "grove_high_output", "fecha": "2026-09-19"}],
 "denominaciones": {
   "nombre_largo": "La delegacion como palanca: la base comun que quien delega y quien recibe tienen que compartir, la decision consciente de que se retiene, y el seguimiento que separa la delegacion de la abdicacion",
   "sigla": "",
   "otros_idiomas": [
     {"idioma": "ingles", "termino": "delegation as leverage"},
     {"idioma": "ingles", "termino": "insincere delegation"},
     {"idioma": "ingles", "termino": "delegation without follow-through is abdication"}
   ]
 },
 "condiciones_activacion": "Cuando vas a pasar una tarea tuya a un subordinado y quieres que el resultado llegue sin tener que prescribirle cada actividad en detalle.",
 "entregable_esperado": "La tarea delegada sobre una base comun de informacion ya comprobada, con la decision consciente y dicha de que retienes y que sueltas, y con el seguimiento de la tarea delegada ya montado.",
 "pasos_accionables": [
   "Cuenta con que el tiempo de un mando tiene una jerarquia de valores, y con que por eso la delegacion es un aspecto esencial del mando.",
   "Antes de delegar, comprueba que quien delega y quien recibe comparten una base comun de informacion y un conjunto comun de ideas o nociones operativas sobre como abordar la resolucion de problemas, que es un requisito que muchas veces no se cumple.",
   "Cuenta con que, si las dos partes no comparten esa base comun relevante, quien recibe solo puede llegar a ser un delegado efectivo con instrucciones especificas, y eso, igual que en la intromision donde las actividades concretas se prescriben en detalle, produce palanca de mando baja.",
   "Revisa que tareas no quieres soltar en realidad: todos tenemos algunas que no queremos delegar simplemente porque nos gusta hacerlas y preferimos no soltarlas.",
   "Deja que eso pase solo si se apoya en una decision consciente de retener ciertas tareas que disfrutas haciendo aunque pudieras delegarlas si quisieras; sabe exactamente lo que estas haciendo y evita la farsa de la delegacion insincera, que produce una palanca de mando negativa inmensa.",
   "Antes de decidir si delegas las actividades que te son familiares o las que no, aplica el principio: delegar sin seguimiento es abdicar.",
   "Cuenta con que nunca puedes lavarte las manos de una tarea: aun despues de delegarla sigues siendo responsable de que se cumpla, y supervisar la tarea delegada es la unica via practica que tienes de asegurar un resultado.",
   "Separa el seguimiento de la intromision: supervisar no es entrometerse, sino comprobar que una actividad avanza en linea con lo que se espera de ella.",
   "Elige con esa vara que delegas: como es mas facil supervisar algo que te resulta familiar, si tienes eleccion delega aquellas actividades que mejor conoces.",
   "Cuenta de antemano con lo que el experimento del lapiz ensena: es muy probable que hacerlo asi vaya en contra de tu fibra emocional."
 ],
 "resumen_teorico": (
  "UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_04.md, unidad Cap. 3, titulo textual Managerial Leverage. "
  "Sale de la PIEZA P27 de la frontera publicada en la vuelta 46 (HH.2.c), L243 a L249, 347 palabras, y de ningun otro tramo. "
  "POR QUE ES PROCEDIMIENTO: el libro pone SU PROPIO INVENTARIO de lo que hay que comprobar antes y despues de delegar, nombrado pieza a pieza: la base comun de informacion, el conjunto comun de ideas operativas sobre como resolver problemas, la decision consciente sobre lo que se retiene, el seguimiento, y el criterio de que se delega. "
  "Es inventario de OBJETOS DE TRABAJO y no de metas, y el criterio no es un adjetivo de adecuacion: es la frase delegation without follow-through is abdication, que el propio libro llama principle. "
  "DE DONDE SALE CADA PASO, uno a uno: paso 1 (L245: Because managerial time has a hierarchy of values, delegation is an essential aspect of management); "
  "paso 2 (L245: The delegator and delegatee must share a common information base and a common set of operational ideas or notions on how to go about solving problems, a requirement that is frequently not met); "
  "paso 3 (L245: Unless both parties share the relevant common base, the delegatee can become an effective proxy only with specific instructions. As in meddling, where specific activities are prescribed in detail, this produces low managerial leverage); "
  "paso 4 (L247: We all have some things that we do not really want to delegate simply because we like doing them and would rather not let go); "
  "paso 5 (L247: this is not too bad so long as it is based on a conscious decision that you will hold on to certain tasks that you enjoy performing, even though you could, if you chose, delegate them. But be sure to know exactly what you are doing, and avoid the charade of insincere delegation, which can produce immense negative managerial leverage); "
  "paso 6 (L249: Given a choice, should you delegate activities that are familiar to you or those that are not? Before answering, consider the following principle: delegation without follow-through is abdication); "
  "paso 7 (L249: You can never wash your hands of a task. Even after you delegate it, you are still responsible for its accomplishment, and monitoring the delegated task is the only practical way for you to ensure a result); "
  "paso 8 (L249: Monitoring is not meddling, but means checking to make sure an activity is proceeding in line with expectations); "
  "paso 9 (L249: Because it is easier to monitor something with which you are familiar, if you have a choice you should delegate those activities you know best); "
  "paso 10 (L249: But recall the pencil experiment and understand before the fact that this will very likely go against your emotional grain). "
  "RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 10 pasos, 10 TRANSCRIPCION, 0 PUENTE. "
  "EL CASO ENTRA NOMBRADO Y NO PONE PASOS (manual 3.5): el experimento del lapiz, donde el supervisor ofrece el lapiz y no lo suelta, es el CASO del autor. "
  "Lo nombro en el paso 10 porque EL PROPIO LIBRO lo nombra ahi como recordatorio (recall the pencil experiment), y la doctrina que sostiene va escrita en los pasos 4 y 5 sin el dato del caso. "
  "LO QUE NO ESCRIBO Y POR ESO NO ESTA AQUI: NO escribo COMO se comprueba que la base comun existe, ni con que frecuencia se supervisa lo delegado, porque este tramo no pone ni prueba ni periodo para eso. "
  "El periodo y el detalle del seguimiento son de L253 a L255, que es la PIEZA P29, y tienen nodo propio en esta misma vuelta: supervisar_tarea_delegada_etapa_menor_valor. Escribirlos aqui seria extraer dos veces el mismo renglon. "
  "NO escribo la jerarquia de valores del tiempo del mando como procedimiento: el tramo la nombra y no la despliega, y NOMBRAR NO ES PROCEDIMENTAR. "
  "ARISTAS DECLARADAS POR LECTURA, para cablearlas el dia de la insercion y no hoy: "
  "(1) D.29, MADRE transmitir_objetivos_prioridades_preferencias, cuyo paso 5 dice en UNA linea que transmitir los objetivos y los modos preferidos es la llave de una delegacion que salga bien, y este hijo despliega esa delegacion en diez pasos que la madre no tiene. Esa madre ya declaro esta arista en su propia ficha en la vuelta 46, apuntando al nodo de L243 a L249 cuando el hijo aun no estaba escrito: hoy el hijo existe y se llama asi. "
  "(2) D.29, HIJO supervisar_tarea_delegada_etapa_menor_valor, porque el paso 7 de este nodo nombra el seguimiento de la tarea delegada en una linea y aquel lo despliega con su etapa, su frecuencia y su detalle. "
  "(3) D.29, HERMANO detectar_palanca_negativa_actividad_mando: los pasos 3 y 8 de este nodo se apoyan en la intromision, que aquel nodo define y prueba. La declaro como arista de lectura y no como gemelo: lo que aqui se delega no es lo que alli se detecta. "
  "TRADUCCION DECLARADA: delegation as leverage, insincere delegation y la frase delegation without follow-through is abdication viajan en denominaciones. "
  "DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO: el paso 1 es una razon y no un acto, y un lector estricto dira que sobra. "
  "Lo sostengo porque es la condicion que hace que el resto del nodo tenga sentido (si el tiempo del mando no tuviera jerarquia de valores, delegar no seria palanca), pero si cae, cae DENTRO de mi marcado."
 )
}

io.open('cuarentena/grove_high_output/delegar_tarea_base_comun_seguimiento.json', 'w', encoding='utf-8', newline='\n').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('escrito')
