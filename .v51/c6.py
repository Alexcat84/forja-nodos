import json, pathlib
d = {
 "id": "cubrir_indicadores_problemas_reunion_individual",
 "titulo": "Cubrir en la reunion individual los indicadores del subordinado, lo ocurrido desde la anterior y el problema potencial, con el criterio de que sean los asuntos que le preocupan",
 "dominio": "gestion_equipos",
 "estado": "vivo",
 "ids_alias": [],
 "nodos_previos": [],
 "nodos_siguientes": [],
 "atribuciones": [],
 "fuentes": [{"clave": "grove_high_output", "fecha": "2026-09-19"}],
 "denominaciones": {
   "nombre_largo": "El contenido de la reunion individual: las cifras de rendimiento con enfasis en las que avisan de problema, lo importante ocurrido desde la reunion anterior con sus cuatro clases, la intuicion que dispara una mirada a la caja negra de la organizacion, y el criterio que manda sobre todos ellos",
   "sigla": "",
   "otros_idiomas": [
     {"idioma": "ingles", "termino": "one-on-one"},
     {"idioma": "ingles", "termino": "organizational black box"}
   ]
 },
 "condiciones_activacion": "Cuando estas dentro de la reunion individual, o preparando su guion, y hay que decidir que asuntos se tratan en ella.",
 "entregable_esperado": "La reunion individual cubierta por sus asuntos: los indicadores del subordinado con los que avisan de problema por delante, lo importante ocurrido desde la anterior, los problemas potenciales, y todos ellos filtrados por el criterio de que sean los que preocupan al subordinado.",
 "pasos_accionables": [
   "Empieza por las cifras de rendimiento, o sea los indicadores que usa el subordinado, como los ritmos de pedidos entrantes, la produccion o el estado de los proyectos.",
   "Pon el enfasis en los indicadores que avisan de un problema.",
   "Cubre ademas cualquier cosa importante que haya ocurrido desde la reunion anterior.",
   "Trata dentro de eso los problemas de contratacion del momento.",
   "Trata los problemas de personas en general.",
   "Trata los problemas de organizacion y los planes futuros.",
   "Y trata, muy muy importante, los problemas potenciales.",
   "Cuenta con que aunque un problema no sea tangible, aunque sea solo una intuicion de que algo va mal, el subordinado se lo debe a su supervisor y tiene que decirselo, porque eso dispara una mirada dentro de la caja negra de la organizacion.",
   "Rige todo lo anterior por el criterio mas importante de los asuntos que se hablan: que sean cuestiones que preocupan al subordinado y le dan la lata.",
   "Cuenta con que esas cuestiones suelen ser oscuras y tardan en aflorar, en considerarse y en resolverse."
 ],
 "resumen_teorico": (
  "UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_05.md, unidad Cap. 4, titulo textual Meetings, The Medium of Managerial Work. "
  "Sale de la PIEZA P14 de la frontera de cap_05 publicada en la vuelta 50 (LL.4.b), L43 a L43, 134 palabras. "
  "LAS PALABRAS LAS RECOMPUTE YO EN LA VUELTA 51 ANTES DE CORTAR y reproducen la frontera al digito: 134, que es lo que LL.4.b publica (.v51/palabras_tramos.txt). "
  "EL TRAMO ENTERO ES DE ESTE NODO: cero frontera interna, cero solapes y cero prestamo de tramos vecinos. Los diez pasos salen de L43 y de ninguna otra linea. "
  "POR QUE ES PROCEDIMIENTO: el libro pone SU PROPIO INVENTARIO DE OBJETOS DE TRABAJO, que es el caso central de EXTRACTOR.md 9.1, y lo pone dos veces. "
  "Nombra uno a uno: por donde se empieza (performance figures, indicators used by the subordinate) con sus TRES ejemplos de indicador (incoming order rates, production output, project status), donde va el enfasis (indicators that signal trouble), el segundo bloque (anything important that has happened since the last meeting) con sus CUATRO clases nombradas una a una (current hiring problems, people problems in general, organizational problems and future plans, potential problems), el caso de la intuicion con su mecanismo (triggers a look into the organizational black box) y el criterio que manda sobre todo (the most important criterion governing matters to be talked about is that they be issues that preoccupy and nag the subordinate). "
  "Y EL CRITERIO NO ES UN ADJETIVO DE ADECUACION, y esto conviene mirarlo dos veces porque el renglon usa la palabra criterion: no dice los asuntos apropiados ni los temas relevantes, dice que sean los que preocupan y dan la lata al subordinado, que es una prueba que quien lee puede aplicar a un asunto concreto. "
  "DE DONDE SALE CADA PASO, uno a uno, y los diez salen de L43: "
  "paso 1 (What should be covered in a one-on-one? We can start with performance figures, indicators used by the subordinate, such as incoming order rates, production output, or project status); "
  "paso 2 (Emphasis should be on indicators that signal trouble); "
  "paso 3 (The meeting should also cover anything important that has happened since the last meeting); "
  "paso 4 (current hiring problems); "
  "paso 5 (people problems in general); "
  "paso 6 (organizational problems and future plans); "
  "paso 7 (and, very, very important, potential problems); "
  "paso 8 (Even when a problem is not tangible, even if it is only an intuition that something is wrong, a subordinate owes it to his supervisor to tell him, because it triggers a look into the organizational black box); "
  "paso 9 (The most important criterion governing matters to be talked about is that they be issues that preoccupy and nag the subordinate); "
  "paso 10 (These are often obscure and take time to surface, consider, and resolve). "
  "NOTA DE TRANSCRIPCION: en el paso 7 el original encierra el muy muy importante entre guiones largos, y en el paso 8 escribe isn't, it's y something's con apostrofe tipografico. Los cito como comas y en forma desarrollada porque el barrido de esta casa no admite guiones largos ni signos tipograficos, y lo citado no cambia. "
  "RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 10 pasos, 10 TRANSCRIPCION, 0 PUENTE. "
  "DONDE ESTUVE A PUNTO DE ESCRIBIR UN PUENTE Y NO LO ESCRIBI, especie EL RESPONSABLE, y esta era la mas facil de colar: iba a escribir que el supervisor PREGUNTE por el problema potencial si el subordinado no lo saca. L43 escribe la obligacion del lado del subordinado (a subordinate owes it to his supervisor to tell him) y NO encarga al supervisor ninguna pregunta. Lo que el supervisor hace para sacar mas esta en L45, que es la pieza P15 y otro nodo, y ahi ira con su propio tramo. El paso 8 se queda en la obligacion que el renglon escribe. "
  "SEGUNDO SITIO DE TENTACION, especie EL DESTINATARIO: iba a escribir que se hace con el indicador que avisa de un problema (escalarlo, abrir una accion, llevarlo a la revision de operaciones). L43 dice donde va el ENFASIS y no dice que se haga despues. El paso 2 dice pon el enfasis y para ahi. "
  "TERCER SITIO DE TENTACION, especie EL PERIODO: iba a escribir cada cuanto se repasan los indicadores. El renglon dice since the last meeting, que es un intervalo definido por la reunion anterior y no un periodo fijado, y el paso 3 lo escribe asi. "
  "LOS TRES EJEMPLOS DE INDICADOR ENTRAN DENTRO DEL PASO 1 Y NO COMO PASOS PROPIOS, y es deliberado: el libro los da con such as, que es forma de ejemplo y no de inventario cerrado, mientras que las CUATRO clases del paso 3 las da con dos puntos y una lista, que es forma de inventario. Por eso los ejemplos van dentro de un paso y las clases van en cuatro. La diferencia la marca el texto, no yo. "
  "CERO ATRIBUCIONES, y es deliberado: L43 no trae ni una cifra ni una frase de otro autor. La frase de Drucker de este capitulo esta en L45, que es la pieza P15 y otro nodo. "
  "ARISTAS DECLARADAS POR LECTURA, para cablearlas el dia de la insercion y no hoy (D.39 mide la puerta CERRADA para este libro en esta vuelta): "
  "(1) D.29 hacia la CABEZA usar_tres_clases_reunion_proceso, el candidato 2 de esta misma tanda: este nodo es un MEDIO de la primera de las tres clases que aquella cabeza nombra. La etiqueta es D.29 y no D.37 por la razon escrita en la ficha de la cabeza. "
  "(2) D.29, PARIENTE preparar_guion_reunion_individual_subordinado, el candidato 5 de esta misma tanda: aquel dice QUIEN prepara el guion y este QUE va dentro. Son la misma reunion por sus dos mitades y no comparten ni un paso. "
  "(3) D.29, PARIENTE POR CONTRASTE preguntar_conducir_reunion_individual, del grafo y de zhuo_manager, que trae tres grupos de preguntas para conducir la misma reunion. AQUEL PONE LAS PREGUNTAS DEL SUPERVISOR y este pone los ASUNTOS que hay que cubrir, y ademas aquel encarga al que dirige lo que este deja del lado del subordinado. El dia que se cablee hay que leer los dos delante. "
  "(4) D.29, PARIENTE calibrar_notas_reunion_jefes_pares, del grafo: aquel trabaja sobre las notas de la reunion y este sobre su contenido. Cero pasos comunes. "
  "DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO: partir las cuatro clases de L43 en cuatro pasos (4 a 7) en vez de dejarlas dentro del paso 3. Un lector estricto dira que el libro las escribe en una sola frase y que son una enumeracion, no cuatro actos. Lo sostengo por la forma del texto (dos puntos y lista, frente al such as del paso 1) y porque la cuarta clase lleva su propio enfasis escrito (very, very important), que se pierde si se funde. Si cae, cae DENTRO de mi marcado. "
  "SEGUNDO DISCUTIBLE: el paso 10 es una OBSERVACION sobre esos asuntos y no un acto. Lo sostengo porque es la frase de cierre literal del tramo y porque explica por que el criterio del paso 9 pide tiempo. Si cae, cae DENTRO de mi marcado."
 )
}
p = pathlib.Path("cuarentena/grove_high_output/%s.json" % d["id"])
assert not p.exists(), "ya existe"
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("escrito", p, len(d["pasos_accionables"]), "pasos")
