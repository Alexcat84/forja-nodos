import json, pathlib

base = pathlib.Path("cuarentena/grove_high_output")

D045 = (
 " CORRECCION DECLARADA DE LA VUELTA 51, SIN BORRAR LA LINEA VIEJA (manual principio 6, deuda d045, "
 "adjudicada por el auditor en la ACTA 49 y encargada en la TAREA 3.a de esta vuelta). "
 "DONDE LA ARISTA (1) DE MAS ARRIBA DICE D.37, CABEZA subir_productividad_gerencial_tres_vias, paso 2, TIENE QUE LEERSE D.29 CON LA MISMA CABEZA Y EL MISMO PASO. "
 "EL MOTIVO, y es de regla y no de gusto: D.37 ata la cabeza con las partes que LA CABEZA NOMBRA, y esa cabeza nombra TRES VIAS, que son el ritmo, la palanca y la mezcla. "
 "Este nodo NO es ninguna de las tres: es un MEDIO de la primera, o sea uno de los principios de produccion con los que se sube el ritmo. "
 "D.37 exige que la parte sea LA QUE ESE PASO NOMBRA, y el paso 2 de la cabeza nombra el ritmo, no la regularidad de los bloques iguales. "
 "LA RELACION NO CAMBIA NI SE BORRA: sigue habiendo arista, sigue siendo hacia la misma cabeza y sigue colgando del mismo paso 2. Lo que cambia es la ETIQUETA, y con ella lo que la arista promete: "
 "una D.37 promete que la cabeza enumera esta parte y la cuenta entre sus tres, y este nodo no sale de esa cuenta. Una D.29 promete una relacion declarada con razon escrita, que es lo que aqui hay. "
 "DE DONDE SALE LA CORRECCION, Y NO ES DE MI COSECHA: la misma relacion estaba etiquetada de dos maneras en la misma bandeja. "
 "La ficha de preparar_respuestas_estandar_interrupciones_repetidas (pieza P41) declaraba D.29 hacia esa misma cabeza y razonaba por que, y esta declaraba D.37. "
 "El auditor adjudico en la ACTA 49 que la buena es la de P41 y que esto no es caida de nadie, y esa es la que se aplica aqui. LA FICHA DE P41 NO SE TOCA, porque ya estaba bien. "
 "Y LO QUE ESTA CORRECCION DEJA DICHO PARA EL DIA DEL CABLEADO: las dos aristas se cablean juntas y las dos como D.29, para que la cabeza no reciba una parte de D.37 que su propio texto no cuenta."
)

D046 = (
 " CORRECCION DECLARADA DE LA VUELTA 51, SIN BORRAR LA LINEA VIEJA (manual principio 6, deuda d046, "
 "adjudicada por el auditor en la ACTA 49 y encargada en la TAREA 3.b de esta vuelta). "
 "DONDE ESTA FICHA AFIRMA MAS ARRIBA EL TRAMO ENTERO ES DE ESTE NODO: cero frontera interna y cero solapes con ningun otro candidato, TIENE QUE LEERSE ASI: "
 "el tramo entero es de este nodo y no solapa con ningun otro candidato, PERO EL PASO 1 TOMA PRESTADO SU REFERENTE DE L313, QUE ES LA PIEZA P40 Y DA CERO NODOS, Y ESE PRESTAMO SE DECLARA AQUI. "
 "QUE ES LO PRESTADO, exactamente: el paso 1 escribe porque hay formas mejores que esconderte, y L315, que es el tramo de este nodo, abre con There are better ways SIN DECIR mejores que que. "
 "Quien dice de que son mejores es L313: the idea mentioned most often was to create blocks of time for individual work by hiding physically, but this is a less than happy answer. "
 "O sea que el ESCONDERTE del paso 1 no esta en L315: esta en L313. "
 "POR QUE NO ES CAIDA, y lo adjudica el auditor y no yo: manual seccion 3.5 manda que el material de un tramo de cero entre NOMBRADO DENTRO del nodo de su doctrina, que es exactamente lo que este paso hace, "
 "y es el mismo criterio que el propio reporte aplica en LL.4.d a los cinco tramos de cero de cap_05. Un referente que se queda fuera convierte la frase del libro en una frase colgada. "
 "LO QUE SI FALTABA ERA DECIRLO, Y ES LO QUE ESTA LINEA HACE: la ficha afirmaba cero frontera interna y a la vez tomaba material de fuera del tramo, y las dos cosas no pueden estar escritas juntas sin explicacion. "
 "LA REGLA NUEVA QUE ME APLICO A PARTIR DE AQUI, y sale de esta misma deuda: si un paso resuelve su referente con un tramo vecino, SE DICE, aunque la regla lo autorice. Que algo este permitido no lo hace invisible. "
 "NI UN PASO, NI UNA ATRIBUCION, NI UN TITULO CAMBIAN CON ESTA CORRECCION: el paso 1 se queda como esta, porque el auditor adjudica que es correcto. Lo que cambia es que ahora el prestamo esta declarado."
)

for ident, texto, marca in (
    ("buscar_regularidad_bloques_iguales_trabajo_mando", D045, "deuda d045"),
    ("preparar_respuestas_estandar_interrupciones_repetidas", D046, "deuda d046"),
):
    p = base / ("%s.json" % ident)
    d = json.loads(p.read_text(encoding="utf-8"))
    assert "CORRECCION DECLARADA DE LA VUELTA 51" not in d["resumen_teorico"], ident
    antes = {"pasos": d["pasos_accionables"], "titulo": d["titulo"], "atribuciones": d.get("atribuciones")}
    d["resumen_teorico"] += texto
    despues = {"pasos": d["pasos_accionables"], "titulo": d["titulo"], "atribuciones": d.get("atribuciones")}
    assert antes == despues
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("correccion declarada en %-56s (%s): pasos, titulo y atribuciones INTACTOS" % (ident, marca))
