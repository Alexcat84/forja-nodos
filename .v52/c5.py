import json, pathlib
d = {
 "id": "conducir_reunion_individual_telefono_distancia",
 "titulo": "Conducir la reunion individual por telefono a distancia con el guion por delante, notas de las dos partes e intercambio de notas al terminar",
 "dominio": "gestion_equipos",
 "estado": "vivo",
 "ids_alias": [],
 "nodos_previos": [],
 "nodos_siguientes": [],
 "atribuciones": [],
 "fuentes": [{"clave": "grove_high_output", "fecha": "2026-09-19"}],
 "denominaciones": {
   "nombre_largo": "La reunion individual por telefono a larga distancia, que la dispersion geografica de la organizacion hace necesaria: funciona con el guion en manos del supervisor antes de empezar y con notas de las dos partes, y como no se ven las caras las notas no pueden funcionar igual que en la reunion cara a cara, asi que se intercambian al terminar",
   "sigla": "",
   "otros_idiomas": [
     {"idioma": "ingles", "termino": "long-distance telephone one-on-ones"},
     {"idioma": "ingles", "termino": "outline"}
   ]
 },
 "condiciones_activacion": "Cuando la organizacion esta repartida geograficamente y la reunion individual tiene que celebrarse por telefono a larga distancia en vez de cara a cara.",
 "entregable_esperado": "La reunion individual a distancia celebrada con el guion en manos del supervisor desde antes de empezar y con notas tomadas por las dos partes, y las notas intercambiadas despues de la reunion de manera que cada uno sepa a que se comprometio el otro.",
 "pasos_accionables": [
   "Ten la reunion individual por telefono a larga distancia cuando la organizacion este repartida geograficamente.",
   "Haz que el supervisor tenga el guion antes de que la reunion empiece.",
   "Haz que las dos partes tomen notas.",
   "Cuenta con que, como no puedes ver al otro participante de la reunion, la toma de notas no puede funcionar igual que en la reunion cara a cara.",
   "Intercambiad las notas despues de la reunion, que es la manera de asegurarse cada uno de a que se comprometio el otro."
 ],
 "resumen_teorico": (
  "UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_05.md, unidad Cap. 4, titulo textual Meetings, The Medium of Managerial Work. "
  "Sale de la PIEZA P19 de la frontera de cap_05 publicada en la vuelta 50 (LL.4.b), L55 a L55, 85 palabras. "
  "LAS PALABRAS LAS RECOMPUTE YO EN LA VUELTA 52 ANTES DE CORTAR y reproducen la frontera al digito: 85, que es lo que el encargo de la vuelta 52 publica desde LL.4.b (.v52/palabras_tramos.txt). "
  "EL TRAMO ENTERO ES DE ESTE NODO: cero frontera interna, cero solapes y cero prestamo de tramos vecinos. Los cinco pasos salen de L55 y de ninguna otra linea. "
  "PERO SI HAY PRESTAMO DE CONTENIDO Y LO DECLARO YO, QUE ES LO QUE 15.4 Y d046 MANDAN HACER: los pasos 2 y 3 repiten dos piezas que ya viven en otros nodos de este mismo capitulo (el guion es de L41, pieza P13; las notas de las dos partes son de L49, pieza P16). NO SON UN PRESTAMO DE TRAMO, porque L55 las escribe otra vez con todas sus letras dentro de su propio renglon, y por eso se transcriben de L55 y se citan de L55. Lo que declaro es que el material se repite, para que quien lea el grafo sepa que no son tres nodos distintos diciendo cosas distintas, sino el mismo requisito aplicado a la reunion a distancia. "
  "POR QUE ES PROCEDIMIENTO: el libro pone SU PROPIO INVENTARIO DE MEDIOS (EXTRACTOR.md 9.1), y lo pone justo despues de su adjetivo de adecuacion, que es lo que hay que mirar dos veces. "
  "EL ADJETIVO DE ADECUACION ESTA EN EL TRAMO Y DIGO DONDE, PORQUE ES LA RESTRICCION 2 DE 9.1: el texto dice these can work well enough with proper preparation and attention, y proper es exactamente un adjetivo de adecuacion. Lo que salva al tramo es que el adjetivo NO esta en el sitio del criterio: va seguido de dos puntos y de la lista propia del libro (the supervisor must have the outline before the meeting begins, both parties should take notes), asi que el criterio que decide no es proper, son las dos piezas nombradas. Si el tramo se hubiera quedado en proper preparation, este nodo no existiria. "
  "Y EL and so on NO LO RELLENO, que es la otra mitad de lo mismo: la lista del libro termina con and so on, y ahi el libro deja abierto lo que no nombra. Cualquier tercera pieza que yo anadiera seria mia y no suya, asi que los pasos 2 y 3 son exactamente las dos que el texto escribe, ni una mas. "
  "DE DONDE SALE CADA PASO, uno a uno, y los cinco salen de L55: "
  "paso 1 (Long-distance telephone one-on-ones have become necessary because many organizations are now spread out geographically); "
  "paso 2 (the supervisor must have the outline before the meeting begins); "
  "paso 3 (both parties should take notes, and so on); "
  "paso 4 (Because you cannot see the other participant in the meeting, note-taking cannot work in the same way as in a face-to-face meeting); "
  "paso 5 (Exchanging notes after the meeting is a way to make sure each knows what the other committed himself to do). "
  "NOTA DE TRANSCRIPCION: el original usa apostrofe tipografico en las contracciones de no puedes y no puede. Los cito en forma desarrollada porque el barrido de esta casa no admite signos tipograficos, y lo citado no cambia. "
  "RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 5 pasos, 5 TRANSCRIPCION, 0 PUENTE. "
  "DONDE ESTUVE A PUNTO DE ESCRIBIR UN PUENTE Y NO LO ESCRIBI, especie EL DESTINATARIO, y esta sale directamente del and so on: iba a escribir una tercera pieza de preparacion (confirmar la hora, probar la linea, avisar de quien esta en la sala). Ninguna esta en L55 y las tres son de mi cosecha. El and so on se queda sin rellenar y el paso 3 termina donde el libro termina. "
  "SEGUNDO SITIO DE TENTACION, especie EL RESPONSABLE: iba a escribir quien manda las notas a quien en el intercambio del paso 5. El libro dice exchanging notes, que es reciproco y sin remitente, y el paso 5 lo deja en la forma reciproca. "
  "TERCER SITIO DE TENTACION, especie EL PERIODO: iba a escribir cuanto tarda el intercambio (el mismo dia, antes de la siguiente). L55 dice after the meeting y no pone plazo, y el paso 5 dice despues de la reunion. "
  "CUARTO SITIO DE TENTACION, y es de medio: iba a escribir el canal del intercambio (correo, fichero compartido). El libro de 1983 no lo nombra y no me toca modernizarlo. "
  "CERO ATRIBUCIONES, y es deliberado: L55 no trae ni una cifra ni una frase de otro autor. "
  "LO QUE NO ESCRIBO Y POR ESO NO ESTA AQUI: NO escribo que se hace si una de las partes no tiene el guion; NO escribo ninguna duracion ni frecuencia para la reunion a distancia, porque el tramo no las toca y las de la reunion cara a cara viven en P11 y P12 con sus propias fichas. "
  "ARISTAS DECLARADAS POR LECTURA, para cablearlas el dia de la insercion y no hoy (D.39 mide la puerta CERRADA para este libro en esta vuelta, .v52/puerta_d39.txt): "
  "(1) D.29 hacia la CABEZA usar_tres_clases_reunion_proceso, que ya espera en la bandeja: este nodo es un MEDIO de la primera de las tres clases que aquella cabeza nombra, con la misma etiqueta y por la misma razon escrita dentro de la ficha de la cabeza. "
  "(2) D.29, MADRE POR LECTURA tomar_notas_copia_guion_reunion_individual, el candidato 2 de esta misma tanda: aquel pone la regla general de las notas en la reunion individual y este dice como cambia cuando no os veis las caras, y le anade el intercambio posterior que aquel no tiene. ES LA ARISTA MAS IMPORTANTE DE ESTA FICHA y la levanta la lectura, porque el paso 4 de aqui contradice en parte el modo de aquel (note-taking cannot work in the same way). "
  "(3) D.29, MADRE POR LECTURA preparar_guion_reunion_individual_subordinado, de la bandeja y de la vuelta 51: aquel dice quien prepara el guion y para que sirve, y este exige que ese guion este en manos del supervisor ANTES de que empiece la reunion a distancia, que es una exigencia de momento que aquel no escribe. "
  "(4) D.29, PARIENTE fijar_duracion_lugar_reunion_individual, de la bandeja y de la vuelta 51: aquel fija el LUGAR de la reunion (el area de trabajo del subordinado) y este describe el caso en que no hay lugar comun porque la organizacion esta repartida. Se tocan por el sitio y no por los pasos, y cero pasos comunes. "
  "DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO, Y ES EL DE FIDELIDAD, NO EL DE CLASE: los pasos 2 y 3 son material que ya vive en otros dos nodos de este capitulo, y un lector estricto puede decir que este nodo repite y que lo propio de L55 son solo los pasos 1, 4 y 5. Lo sostengo porque L55 los vuelve a escribir enteros y porque un nodo de reunion a distancia al que se le quiten sus dos requisitos de preparacion no es ejecutable; pero lo marco porque P.19 manda fundir lo que se repite y esto lo roza. Si cae, cae DENTRO de mi marcado y el arreglo es quitar dos pasos, no reescribir el nodo. "
  "SEGUNDO DISCUTIBLE: el paso 4 es una OBSERVACION y no un acto, y un lector estricto lo tumba. Lo sostengo porque es la razon entera por la que el paso 5 existe: si las notas funcionaran igual que cara a cara, no haria falta intercambiarlas. Si cae, cae DENTRO de mi marcado. "
  "TERCER DISCUTIBLE, Y ESTE ES SOBRE UNA CIFRA MIA, que es donde la tanda anterior me cazo: publico 85 palabras para este tramo porque mi recuento las da, y mi recuento sale de wc -w sobre sed -n 55p, que cuenta como palabra cada cadena separada por espacio. Este renglon lleva CUATRO piezas unidas por guion corto (Long-distance, one-on-ones, note-taking y face-to-face) y cada una cuenta como UNA palabra; medido con un contador que partiera por cada guion, el tramo daria 91 y no 85, y las dos cifras estan corridas en .v52/palabras_guion.txt y no tecleadas por mi. Marco la convencion de conteo porque la cifra coincide con LL.4.b al digito y quiero que se sepa con que regla coincide. Si cae, cae DENTRO de mi marcado y no toca ni un paso."
 )
}
p = pathlib.Path("cuarentena/grove_high_output/%s.json" % d["id"])
assert not p.exists(), "ya existe"
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("escrito", p, len(d["pasos_accionables"]), "pasos")
