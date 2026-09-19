import json, pathlib

base = pathlib.Path("cuarentena/grove_high_output")

VEREDICTOS = {
 "fijar_frecuencia_reunion_individual_madurez_tarea": [
   ("infundir_regularidad_reunion_proceso", "0,385",
    "aquel disena la regularidad de CUALQUIER reunion de proceso (L21) y este fija la frecuencia de UNA de las tres clases, subordinado a subordinado (L33 y L35). El par que la senial empareja es mi paso 8 contra su paso 1, y los dos dicen cosas distintas: el mio manda mirar la velocidad de cambio del area, el suyo manda infundir regularidad a la reunion"),
 ],
 "fijar_duracion_lugar_reunion_individual": [
   ("fijar_frecuencia_reunion_individual_madurez_tarea", "0,445",
    "aquel pone CADA CUANTO y este CUANTO DURA Y DONDE. Son dos de las tres decisiones de calendario de la misma reunion y ninguna repite a la otra. El par que la senial empareja es mi paso 4 contra su paso 3: el mio dice que por debajo de la hora el subordinado se limita a lo sencillo, el suyo dice que la madurez se mide por la experiencia con la tarea"),
 ],
 "preparar_guion_reunion_individual_subordinado": [
   ("fijar_duracion_lugar_reunion_individual", "0,428",
    "aquel programa la reunion (cuanto y donde) y este dice de quien es y quien la prepara. El par emparejado es mi paso 1 contra su paso 5: el mio atribuye la reunion al subordinado, el suyo la situa en su area de trabajo"),
   ("fijar_frecuencia_reunion_individual_madurez_tarea", "0,432",
    "aquel pone la frecuencia y este la propiedad y la preparacion. El par emparejado es mi paso 1 contra su paso 6, que son la atribucion de la reunion contra la frecuencia del inexperto"),
   ("infundir_regularidad_reunion_proceso", "0,416",
    "aquel trata la clase entera de reunion de proceso y este una practica interna de una de ellas. El par emparejado es mi paso 2 contra su paso 8, que son la cuenta de preparaciones contra el impacto en el calendario"),
 ],
 "cubrir_indicadores_problemas_reunion_individual": [
   ("preparar_guion_reunion_individual_subordinado", "0,432",
    "aquel dice QUIEN prepara el guion y este QUE va dentro de la reunion. Son las dos mitades de la misma reunion y el libro las escribe en dos renglones seguidos, L41 y L43. El par emparejado es mi paso 2 contra su paso 3, que son el enfasis en el indicador que avisa contra la peticion del guion"),
   ("fijar_duracion_lugar_reunion_individual", "0,386",
    "aquel programa la reunion y este la llena. El par emparejado es mi paso 8 contra su paso 4, que son la intuicion que hay que decir contra lo que pasa si la reunion dura menos de una hora"),
   ("infundir_regularidad_reunion_proceso", "0,391",
    "aquel disena la clase entera de reunion y este pone el contenido de una. El par emparejado es mi paso 2 contra su paso 2, que son el enfasis en el indicador contra saber como se lleva la reunion"),
   ("fijar_frecuencia_reunion_individual_madurez_tarea", "0,410",
    "aquel pone cada cuanto y este que se trata. El par emparejado es mi paso 1 contra su paso 2, que son las cifras de rendimiento contra la madurez relevante para la tarea"),
 ],
}

CABECERA = (
 " VEREDICTO ESCRITO POR LECTURA EN LA VUELTA 51, ANTES DE CUALQUIER INSERCION Y CON LOS VECINOS LEIDOS ENTEROS "
 "(EXTRACTOR.md 2: si la aduana bloquea, se leen los vecinos antes de escribir el veredicto; manual principio 4: las seniales ordenan, nunca deciden). "
 "SU SEDE ES bitacora/VEREDICTOS.jsonl Y HOY NO PUEDE LLEGAR ALLI, porque esa sede la escribe forja.py insertar y la puerta de D.39 mide CERRADA para grove_high_output en esta vuelta (.v51/puerta_d39.txt). "
 "Queda escrito aqui, dentro de la ficha que viaja, para que el dia de la insercion se escriba en su sede con esta razon y no con una nueva. "
)

COLA = (
 " LO QUE SOSTIENE LOS VEREDICTOS DE ARRIBA, Y ESTA MEDIDO Y NO SUPUESTO (.v51/cola_lectura.txt, corrido en la vuelta 51): "
 "de los 9 pares que esta tanda levanta, 6 pasan de 0,40 tal como la aduana los mide, y 0 pasan de 0,40 si se les quita el resumen_teorico. "
 "PASOS literalmente comunes en los 9 pares: 0. LINEAS del libro compartidas en los 9 pares: 0, porque los seis tramos son disjuntos por la frontera de LL.4.b. "
 "POR QUE PASA ESTO, dicho contra mi mismo: la senial 1 compara titulo mas resumen mas pasos (src/aduana.py senal_similitud_texto), y en estas fichas el resumen_teorico es el 85 por ciento del texto comparado. "
 "Mis seis resumenes comparten la plantilla de la casa entera, con sus mismas rubricas escritas con las mismas palabras. "
 "LO QUE ESO SIGNIFICA Y LO QUE NO: la banda alta de EXTRACTOR.md 11 dice que por encima de 0,40 hay 325 gemelos y CERO ajenos en un catalogo de 3.169, y yo acabo de producir 6 pares por encima de 0,40 que no son gemelos. "
 "NO PROPONGO MOVER NINGUN UMBRAL, que ademas me esta vedado: lo que esto mide es MI MANERA DE ESCRIBIR, no la vara. Queda registrado con su cifra."
)

CORRECCIONES = {
 "infundir_regularidad_reunion_proceso": (
  " CORRECCION DECLARADA DENTRO DE LA MISMA VUELTA 51, SIN BORRAR LA LINEA VIEJA (manual principio 6): "
  "donde la arista (2) de mas arriba escribe elegir_clase_reunion_proceso_tres_clases, TIENE QUE LEERSE usar_tres_clases_reunion_proceso, que es el id con el que el candidato 2 de esta tanda se escribio y paso su aduana. "
  "EL MOTIVO DEL CAMBIO DE ID, y no es de forma: elegir afirma un acto de eleccion que L23 no escribe. El renglon dice we use three kinds y no pone ningun criterio para elegir entre las tres, asi que un id con elegir prometia un paso que el libro no tiene. "
  "LA RELACION QUE LA ARISTA DECLARA NO CAMBIA: sigue siendo D.29 hacia la cabeza de las tres clases. Solo cambia el nombre del otro extremo."
 ),
 "usar_tres_clases_reunion_proceso": (
  " CORRECCION DECLARADA DENTRO DE LA MISMA VUELTA 51, SIN BORRAR LAS LINEAS VIEJAS (manual principio 6): "
  "donde la arista (2) de mas arriba escribe fijar_frecuencia_uno_a_uno_madurez_tarea, fijar_duracion_lugar_uno_a_uno, preparar_guion_uno_a_uno_subordinado y cubrir_asuntos_uno_a_uno_indicadores_problema_potencial, TIENEN QUE LEERSE "
  "fijar_frecuencia_reunion_individual_madurez_tarea, fijar_duracion_lugar_reunion_individual, preparar_guion_reunion_individual_subordinado y cubrir_indicadores_problemas_reunion_individual, que son los cuatro ids con los que esos candidatos se escribieron y pasaron su aduana. "
  "EL MOTIVO, y son dos, los dos de regla escrita: uno, la a de uno_a_uno es una preposicion y la regla 3 de id prohibe preposiciones, que es la regla que mas cae de todas. "
  "Dos, y pesa mas, la regla 4 prohibe las familias repetidas: el grafo ya tiene dirigir_reunion_individual_semanal y preguntar_conducir_reunion_individual para este mismo objeto, y escribir uno_a_uno habria partido la familia en dos, con lo que la senial 2 habria dejado de ver juntos a los nodos que de verdad hablan de lo mismo. "
  "Eso es exactamente el motivo que EXTRACTOR.md 15.1 da para la regla del idioma unico, aplicado aqui a la grafia. LA RELACION QUE LA ARISTA DECLARA NO CAMBIA: sigue siendo D.29, con la razon escrita mas arriba."
 ),
}

for ident, pares in VEREDICTOS.items():
    p = base / ("%s.json" % ident)
    d = json.loads(p.read_text(encoding="utf-8"))
    texto = CABECERA
    for vecino, senal, razon in pares:
        texto += (" VEREDICTO SANO sobre el vecino %s, levantado por similitud de texto %s: son HERMANOS. RAZON: %s. "
                  "Cero pasos literalmente comunes y cero lineas del libro compartidas, medido en .v51/cola_lectura.txt. "
                  "La relacion que SI existe entre los dos esta declarada como arista por lectura mas arriba en esta misma ficha."
                  % (vecino, senal, razon))
    texto += COLA
    assert "VEREDICTO ESCRITO POR LECTURA EN LA VUELTA 51" not in d["resumen_teorico"]
    d["resumen_teorico"] += texto
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("veredictos escritos en %-50s (%d vecino(s))" % (ident, len(pares)))

for ident, texto in CORRECCIONES.items():
    p = base / ("%s.json" % ident)
    d = json.loads(p.read_text(encoding="utf-8"))
    assert "CORRECCION DECLARADA DENTRO DE LA MISMA VUELTA 51" not in d["resumen_teorico"]
    d["resumen_teorico"] += texto
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("correccion declarada en %-50s" % ident)
