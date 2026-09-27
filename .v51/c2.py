import json, pathlib
d = {
 "id": "usar_tres_clases_reunion_proceso",
 "titulo": "Usar las tres clases de reunion de proceso que el libro cuenta y nombra: el uno a uno, la reunion de personal y la revision de operaciones",
 "dominio": "gestion_equipos",
 "estado": "vivo",
 "ids_alias": [],
 "nodos_previos": [],
 "nodos_siguientes": [],
 "atribuciones": [],
 "fuentes": [{"clave": "grove_high_output", "fecha": "2026-09-19"}],
 "denominaciones": {
   "nombre_largo": "La cabeza de serie de las reuniones de proceso: las tres clases que el autor dice usar, contadas y nombradas una a una, cada una con su propio despliegue mas adelante en el capitulo",
   "sigla": "",
   "otros_idiomas": [
     {"idioma": "ingles", "termino": "process-oriented meetings"},
     {"idioma": "ingles", "termino": "one-on-one"},
     {"idioma": "ingles", "termino": "staff meeting"},
     {"idioma": "ingles", "termino": "operation review"}
   ]
 },
 "condiciones_activacion": "Cuando vas a montar las reuniones de proceso de tu organizacion y necesitas saber cuantas clases hay y cuales son, antes de entrar en como se lleva cada una.",
 "entregable_esperado": "Las tres clases de reunion de proceso identificadas por su nombre, para poder ir despues a la que toque.",
 "pasos_accionables": [
   "Cuenta con que las reuniones de proceso que se usan son de tres clases, y con que el libro las nombra una a una.",
   "Primera clase: el uno a uno.",
   "Segunda clase: la reunion de personal.",
   "Tercera clase: la revision de operaciones."
 ],
 "resumen_teorico": (
  "UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_05.md, unidad Cap. 4, titulo textual Meetings, The Medium of Managerial Work. "
  "Sale de la PIEZA P7 de la frontera de cap_05 publicada en la vuelta 50 (LL.4.b), L23 a L23, 18 palabras. "
  "LAS PALABRAS LAS RECOMPUTE YO EN LA VUELTA 51 ANTES DE CORTAR y reproducen la frontera al digito: 18, que es lo que LL.4.b publica (.v51/palabras_tramos.txt). "
  "EL TRAMO ENTERO ES DE ESTE NODO: cero frontera interna, cero solapes y cero prestamo de tramos vecinos. Los cuatro pasos salen de L23 y de ninguna otra linea. "
  "ES UNA CABEZA DE SERIE, Y ENTRA COMO TAL (EXTRACTOR.md 9, manual seccion 3.4, y D.37): el texto DICE CUANTAS partes tiene (three kinds) y LAS NOMBRA una a una (the one-on-one, the staff meeting, and the operation review). La cuenta es condicion y esta escrita, no deducida. "
  "LA CITA ENTERA DEL TRAMO, que cabe en una linea: At Intel we use three kinds of process-oriented meetings: the one-on-one, the staff meeting, and the operation review. "
  "DE DONDE SALE CADA PASO, uno a uno, y los cuatro salen de L23: paso 1 (At Intel we use three kinds of process-oriented meetings); paso 2 (the one-on-one); paso 3 (the staff meeting); paso 4 (and the operation review). "
  "RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 4 pasos, 4 TRANSCRIPCION, 0 PUENTE. "
  "Y AQUI LA RELECTURA IMPORTA MAS QUE EN NINGUN OTRO NODO DE ESTA TANDA, porque este es el tramo MAS POBRE que toco: 18 palabras, la cifra mas baja de los seis. EXTRACTOR.md 15.4 dice que un parrafo pobre no produce un nodo pobre sino un nodo INVENTADO, y que el parrafo mas pobre del lote 1 dio 83 por ciento de puentes. Por eso este nodo se queda en los cuatro pasos que el renglon escribe y ni uno mas. "
  "DONDE ESTUVE A PUNTO DE ESCRIBIR UN PUENTE Y NO LO ESCRIBI, y son tres sitios, todos de la misma especie: EL CONTENIDO DE CADA CLASE. Iba a escribir que el uno a uno es entre un supervisor y un subordinado, que la reunion de personal es del supervisor con todos sus subordinados juntos, y que la revision de operaciones es para los que no se tratan a diario. LAS TRES COSAS SON CIERTAS Y NINGUNA ESTA EN L23: la primera esta en L27, la segunda en L69 y la tercera en L87, que son las piezas P9, P25 y P30, tramos distintos y nodos distintos. Un paso que trae material de otro tramo sin declararlo es exactamente la deuda d046, y no la repito el dia que la pago. "
  "CUARTO SITIO DE TENTACION, especie EL PERIODO: iba a escribir que las tres se tienen con regularidad. Lo dice L17 (Such meetings take place on a regularly scheduled basis), que es la pieza P4 y da cero nodos, y L21, que es el candidato 1 de esta misma tanda. NO esta en L23 y no lo escribo aqui. "
  "EL AT INTEL NO LO CONVIERTO EN ATRIBUCION NI EN DATO DEL CASO: el renglon dice donde se usan esas tres clases, y manual 3.5 manda que el caso entre nombrado dentro de la doctrina y no que su dato viaje en el entregable. El paso 1 escribe las reuniones de proceso que se usan y no mete el nombre de la empresa en el entregable. CERO ATRIBUCIONES: no hay en L23 ni cifra con banda ni frase de otro autor. "
  "ARISTAS DECLARADAS POR LECTURA, para cablearlas el dia de la insercion y no hoy (D.39 mide la puerta CERRADA para este libro en esta vuelta): "
  "(1) D.29 hacia infundir_regularidad_reunion_proceso, el candidato 1 de esta misma tanda: aquel dice QUE hay que infundirle a toda reunion de proceso, esta dice CUALES son. El libro las pone seguidas, L21 y L23. "
  "(2) D.29 hacia los cuatro nodos del uno a uno de esta misma tanda (fijar_frecuencia_uno_a_uno_madurez_tarea, fijar_duracion_lugar_uno_a_uno, preparar_guion_uno_a_uno_subordinado y cubrir_asuntos_uno_a_uno_indicadores_problema_potencial), y mas adelante hacia los de la reunion de personal y los de la revision de operaciones. "
  "Y POR QUE D.29 Y NO D.37, QUE ES LO QUE PARECERIA, con la razon escrita porque aqui si hay algo que argumentar: D.37 ata la cabeza con las partes que la cabeza NOMBRA, y esta cabeza nombra TRES CLASES DE REUNION, no cuatro maneras de llevar una de ellas. Los cuatro nodos de esta tanda son MEDIOS de la primera clase, igual que los dos nodos de la deuda d045 son medios de la primera de las tres vias de su cabeza. Es la misma figura y le aplico la misma etiqueta, que es la que el auditor firmo en la ACTA 49 al adjudicar d045 y que el encargo de esta vuelta me manda aplicar en su TAREA 3.a. "
  "Y LO QUE ESO DEJA ABIERTO, dicho en vez de escondido: si alguna vez existe un nodo que SEA el uno a uno entero, ese si seria parte de D.37 de esta cabeza. Hoy no existe, porque P9, que es el tramo donde el libro define el uno a uno, da CERO nodos por ser definicion mas caso (LL.4.b y LL.4.d). "
  "DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO: un lector estricto puede decir que esta cabeza no es un procedimiento sino una ENUMERACION, y que EXTRACTOR.md 9 tumba lo que solo nombra. Lo sostengo por dos motivos escritos y no por preferencia: manual 3.4 autoriza expresamente un nodo por paso MAS UNA CABEZA para la serie numerada, y la ACTA 49 adjudica que la cabeza de serie de este capitulo es P7. Si cae, cae DENTRO de mi marcado, y lo que caeria conmigo seria la figura entera de la cabeza de serie, no este renglon. "
  "SEGUNDO DISCUTIBLE: la etiqueta D.29 de la arista (2) en vez de D.37. La razon esta escrita arriba y es la aplicacion directa de la adjudicacion de d045. Si el auditor lee que una cabeza de serie tiene que atar D.37 a algo si o si, esto cae, y cae DENTRO de mi marcado."
 )
}
p = pathlib.Path("cuarentena/grove_high_output/%s.json" % d["id"])
assert not p.exists(), "ya existe"
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("escrito", p, len(d["pasos_accionables"]), "pasos")
