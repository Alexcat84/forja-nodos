"""Los veredictos por lectura de la tanda de la vuelta 52, escritos DENTRO de la ficha
que viaja porque su sede (bitacora/VEREDICTOS.jsonl) la cierra D.39 y hoy la puerta mide
CERRADA para grove_high_output.

APLICA d051 DESDE EL PRINCIPIO (TAREA 3.b del encargo): el veredicto NOMBRA SU INFORME y
NO se lleva el digito dentro como si fuera de hoy. Lo que queda escrito es la clase, el
vecino, la senial que lo levanto, la razon y el par emparejado. El digito vive en el
informe y solo alli.

Los pasos literalmente comunes NO se afirman: los cuenta este guion.
"""
import json, pathlib

BASE = pathlib.Path("cuarentena/grove_high_output")
GRAFO = pathlib.Path("dataset/nodos.jsonl")

# (vecino, senial que lo levanta segun el informe, razon leida)
VEREDICTOS = {
 "facilitar_expresion_subordinado_pregunta_mas": (".v52/aduana_c1.txt", [
   ("preparar_guion_reunion_individual_subordinado", "similitud de texto",
    "aquel dice DE QUIEN ES la reunion y QUIEN prepara el guion, y este dice QUE HACE EL SUPERVISOR dentro de ella. El par emparejado es mi paso 1 contra su paso 3, que son facilitar la expresion del subordinado contra pedirle que prepare un guion: uno es de dentro de la sesion y el otro de antes. El libro los escribe en dos renglones distintos, L41 y L45"),
   ("fijar_duracion_lugar_reunion_individual", "similitud de texto",
    "aquel programa la reunion (cuanto dura y donde) y este dice como se conduce. El par emparejado es mi paso 1 contra su paso 5, que son facilitar la expresion contra tenerla en el area de trabajo del subordinado. Son dos decisiones distintas sobre la misma reunion y ninguna repite a la otra"),
   ("fijar_frecuencia_reunion_individual_madurez_tarea", "similitud de texto",
    "aquel pone CADA CUANTO y este QUE PAPEL juega el supervisor cuando ya esta dentro. El par emparejado es mi paso 1 contra su paso 3, que son facilitar la expresion contra medir la madurez por la experiencia con la tarea"),
   ("cubrir_indicadores_problemas_reunion_individual", "similitud de texto",
    "aquel pone QUE ASUNTOS se cubren y este QUE HACE EL SUPERVISOR mientras se cubren. Es la pareja mas cercana de las cinco y aun asi no repite: aquella ficha ya declaro, en su propia relectura de fidelidad, que lo que el supervisor hace para sacar mas esta en L45, que es mi tramo. El par emparejado es mi paso 6 contra su paso 2, que son insistir con preguntas hasta el fondo contra poner el enfasis en el indicador que avisa"),
   ("infundir_regularidad_reunion_proceso", "similitud de texto",
    "aquel disena la clase entera de reunion de proceso y este conduce una sesion concreta de una de ellas. El par emparejado es mi paso 1 contra su paso 4, que son facilitar la expresion contra conseguir que los asistentes sepan que hay que conseguir en la reunion"),
 ]),
 "tomar_notas_copia_guion_reunion_individual": (".v52/aduana_c2.txt", [
   ("cubrir_indicadores_problemas_reunion_individual", "similitud de texto",
    "aquel dice QUE se habla y este QUE SE ESCRIBE mientras se habla. El par emparejado es mi paso 5 contra su paso 9, que son lo que simboliza escribirlo contra el criterio de que los asuntos sean los que preocupan al subordinado: uno es sobre el soporte y el otro sobre el contenido"),
   ("infundir_regularidad_reunion_proceso", "similitud de texto",
    "aquel disena la clase entera de reunion y este pone una pista mecanica de una de ellas. El par emparejado es mi paso 5 contra su paso 8, que son el compromiso que implica la nota contra el impacto minimo de una reunion programada en el resto del trabajo"),
   ("preparar_guion_reunion_individual_subordinado", "similitud de texto y familia de id",
    "ES EL UNICO PAR DE MI TANDA QUE LEVANTA LA SENIAL 2, y lo leo por eso antes que los otros tres. Los dos ids comparten las piezas guion y reunion_individual porque hablan DEL MISMO OBJETO EN DOS MOMENTOS: aquel dice quien prepara el guion y para que sirve, y este dice que se hace con el dentro de la sesion, que es tenerlo por duplicado y anotarlo. El par emparejado es mi paso 5 contra su paso 4, que son lo que simboliza escribirlo contra lo que el guion obliga a pensar de antemano. NO SON GEMELOS y la relacion que si existe esta declarada como arista por lectura dentro de las dos fichas"),
   ("facilitar_expresion_subordinado_pregunta_mas", "similitud de texto",
    "aquel pone el papel del supervisor y el principio de una pregunta mas, y este pone el soporte material de la sesion. El par emparejado es mi paso 6 contra su paso 6, que son el compromiso que implica la nota contra insistir con preguntas hasta llegar al fondo: los dos son el remate de su tramo y por eso se emparejan, pero uno cierra sobre el papel y el otro sobre la nota"),
 ]),
 "acumular_asuntos_importantes_fichero_espera": (".v52/aduana_c3.txt", [
   ("tomar_notas_copia_guion_reunion_individual", "similitud de texto",
    "los dos son pistas mecanicas del mismo tramo del libro y por eso se parecen, pero aquel trabaja DENTRO de la sesion (las dos copias del guion y las notas) y este ENTRE una sesion y la siguiente (el fichero de espera). El par emparejado es mi paso 1 contra su paso 1, que son usar un fichero compartido contra tener una copia del guion en cada lado: dos objetos distintos con la misma forma de reparto"),
   ("cubrir_indicadores_problemas_reunion_individual", "similitud de texto",
    "aquel dice QUE se cubre en la reunion y este COMO LLEGA a la reunion lo que no era urgente. El par emparejado es mi paso 2 contra su paso 3, que son acumular lo importante no urgente para la reunion siguiente contra cubrir lo importante ocurrido desde la anterior: son las dos caras del mismo intervalo entre reuniones, una por el lado de guardar y otra por el de tratar"),
   ("infundir_regularidad_reunion_proceso", "similitud de texto",
    "aquel trae el agrupamiento como principio de diseno de la reunion de proceso y este lo aplica a los asuntos que esperan. El par emparejado es mi paso 3 contra su paso 7, que son el principio de produccion del agrupamiento contra el sistema de control de produccion que toma forma en los calendarios. SON PARIENTES DE DOCTRINA Y NO GEMELOS, y la madre de verdad de mi paso 3 es agrupar_tareas_semejantes_aprovechar_preparacion, que ninguna senial levanto y que declaro por lectura"),
   ("facilitar_expresion_subordinado_pregunta_mas", "similitud de texto",
    "aquel conduce la conversacion y este gobierna la cola de asuntos que llega a ella. El par emparejado es mi paso 3 contra su paso 4, que son el principio del agrupamiento contra el principio de direccion didactica: dos principios con nombre propio del mismo libro, uno de produccion y otro de conversacion"),
 ]),
 "alentar_asuntos_corazon_vigilar_final_reunion": (".v52/aduana_c4.txt", [
   ("fijar_duracion_lugar_reunion_individual", "paso contra nodo",
    "ES EL UNICO PAR DE MI TANDA QUE LEVANTA LA SENIAL 3, LA QUE MAS CAZA, Y LO LEO EL PRIMERO POR ESO. Y lo que hay debajo no es duplicado: es LA MEJOR ARISTA DE LA TANDA. Aquel dice que por debajo de la hora el subordinado se limita a lo sencillo que se despacha deprisa, y este dice que el asunto grave llega cerca del final de la reunion. LOS DOS HABLAN DEL RELOJ DE LA MISMA REUNION y dicen cosas distintas y compatibles. El par emparejado es mi paso 1 contra su paso 3, que son alentar los asuntos de corazon a corazon contra hacer que la reunion dure una hora como minimo: el segundo es la condicion material del primero. Cero pasos comunes, y la relacion esta declarada como arista por lectura dentro de mi ficha"),
   ("tomar_notas_copia_guion_reunion_individual", "similitud de texto",
    "aquel pone el soporte de la sesion y este una clase de asunto que se trata en ella. El par emparejado es mi paso 5 contra su paso 2, que son preguntar si alguna frustracion le carcome contra hacer que los dos tomen notas sobre la copia del guion: no se tocan"),
   ("infundir_regularidad_reunion_proceso", "similitud de texto",
    "aquel disena la clase entera de reunion y este pone una clase de asunto de una de ellas. El par emparejado es mi paso 7 contra su paso 2, que son que el asunto grave llega cerca del final contra conseguir que los asistentes sepan como se lleva la reunion"),
   ("acumular_asuntos_importantes_fichero_espera", "similitud de texto",
    "aquel difiere lo importante no urgente hasta la reunion siguiente y este avisa de lo importante que llega tarde DENTRO de la reunion. El par emparejado es mi paso 7 contra su paso 3, que son el asunto que llega cerca del final contra el principio del agrupamiento. SON EL MISMO PROBLEMA DE MOMENTO VISTO POR DOS SITIOS y ninguno repite al otro: uno gobierna la cola de entrada y el otro el minuto de salida"),
   ("facilitar_expresion_subordinado_pregunta_mas", "similitud de texto",
    "aquel pone el papel del supervisor en general y este una clase concreta de asunto que ese papel saca. El par emparejado es mi paso 2 contra su paso 3, que son el foro perfecto para los problemas sutiles y profundos contra la frase de Drucker sobre hacer que el otro hable de sus problemas: se apoyan y no se repiten, y la arista esta declarada por lectura"),
 ]),
 "conducir_reunion_individual_telefono_distancia": (".v52/aduana_c5.txt", [
   ("tomar_notas_copia_guion_reunion_individual", "similitud de texto y paso contra nodo",
    "ES EL PAR MAS ALTO DE MI FICHA POR DOS SENIALES A LA VEZ, Y NO LO ESCONDO: mis pasos 2 y 3 repiten material que vive en aquel nodo, porque L55 vuelve a escribirlo entero para el caso del telefono. LO QUE ESTE NODO ANADE Y AQUEL NO TIENE: que el guion este en manos del supervisor ANTES de empezar, que al no verse las caras la toma de notas no puede funcionar igual, y el INTERCAMBIO de notas despues de la reunion, que aquel no escribe en ningun paso. El par emparejado es mi paso 3 contra su paso 2, que son las notas de las dos partes en los dos. NO ES GEMELO PORQUE SU CONDICION DE ACTIVACION ES OTRA: aquel vale para cualquier reunion individual y este solo cuando la organizacion esta repartida. El prestamo va declarado dentro de mi ficha, que es lo que d046 manda"),
   ("infundir_regularidad_reunion_proceso", "similitud de texto",
    "aquel disena la clase entera de reunion y este resuelve el caso en que no hay sala comun. El par emparejado es mi paso 5 contra su paso 1, que son intercambiar las notas despues contra infundir regularidad a la clase de reunion"),
   ("preguntar_conducir_reunion_individual", "familia de id",
    "ES EL UNICO VECINO DE OTRO LIBRO QUE UNA SENIAL LEVANTA EN TODA MI TANDA, Y LO LEVANTA LA SENIAL 2 CON LA 1 MUY POR DEBAJO DEL UMBRAL, que es el caso de libro de lo que D.19 mide: dos ids que comparten piezas y dos textos que no se parecen. Aquel, de zhuo_manager, trae tres grupos de preguntas para conducir la reunion, y este trae las condiciones materiales de celebrarla por telefono. El par emparejado es mi paso 4 contra su paso 7, que son que sin verse las caras la nota no funciona igual contra el grupo de preguntas de apoyar. SANO: no comparten ni un paso ni un libro, y lo que tienen en comun es la reunion sobre la que hablan"),
   ("acumular_asuntos_importantes_fichero_espera", "similitud de texto",
    "aquel gobierna lo que espera entre reuniones y este como se celebra una a distancia. El par emparejado es mi paso 5 contra su paso 3, que son el intercambio de notas despues de la reunion contra el principio del agrupamiento: los dos son mecanismos de traspaso, pero uno traspasa compromisos ya tomados y el otro asuntos todavia sin tratar"),
   ("alentar_asuntos_corazon_vigilar_final_reunion", "similitud de texto",
    "aquel abre la puerta a los asuntos de corazon a corazon y este describe el canal en que se celebra la reunion. El par emparejado es mi paso 5 contra su paso 1, que son intercambiar las notas contra alentar los asuntos de corazon a corazon. SON HERMANOS Y ADEMAS SE ROZAN EN ALGO QUE EL LIBRO NO DICE: si el asunto grave llega tarde y ademas es por telefono, ninguno de los dos tramos lo trata. LO DEJO ESCRITO COMO LECTURA Y NO COMO PASO, porque el libro no lo escribe y un paso mio ahi seria un puente"),
   ("facilitar_expresion_subordinado_pregunta_mas", "similitud de texto",
    "aquel pone el papel del supervisor y este el canal. El par emparejado es mi paso 3 contra su paso 2, que son hacer que las dos partes tomen notas contra estar en la reunion para aprender y orientar"),
 ]),
 "programar_reunion_individual_cadena": (".v52/aduana_c6.txt", [
   ("fijar_duracion_lugar_reunion_individual", "similitud de texto",
    "aquel pone CUANTO DURA Y DONDE y este CUANDO SE FIJA LA SIGUIENTE. Son dos piezas del calendario de la misma reunion y no comparten ni un paso. El par emparejado es mi paso 1 contra su paso 3, que son programar en cadena contra hacer que dure una hora como minimo"),
   ("alentar_asuntos_corazon_vigilar_final_reunion", "similitud de texto",
    "aquel pone una clase de asunto y este la manera de poner fecha. El par emparejado es mi paso 1 contra su paso 1, que son programar en cadena contra alentar los asuntos de corazon a corazon: se emparejan por ser la frase de apertura de su tramo, no por decir lo mismo"),
   ("infundir_regularidad_reunion_proceso", "similitud de texto",
    "PARECEN DECIR COSAS CONTRARIAS Y NO LAS DICEN, y por eso este veredicto es el que mas falta hacia: aquel manda infundir REGULARIDAD a la reunion de proceso y este manda NO usar un horario fijo. La regularidad de aquel es que la reunion se celebre siempre; la cadena de este es justo lo que impide que una fecha fija se lleve por delante una celebracion. El par emparejado es mi paso 3 contra su paso 8, que son tener en cuenta los demas compromisos y evitar cancelaciones contra que la reunion programada tenga el minimo impacto en el resto del trabajo: DICEN LO MISMO DESDE DOS SITIOS, y aun asi no son gemelos porque uno disena la clase de reunion y el otro pone fecha a una"),
   ("acumular_asuntos_importantes_fichero_espera", "similitud de texto",
    "aquel gobierna que espera a la reunion siguiente y este cuando se fija esa reunion siguiente. El par emparejado es mi paso 3 contra su paso 3, que son evitar cancelaciones contra el principio del agrupamiento: los dos apuntan al ahorro de tiempo de las dos partes y lo consiguen por vias distintas"),
   ("conducir_reunion_individual_telefono_distancia", "similitud de texto",
    "aquel pone el canal y este la fecha. El par emparejado es mi paso 4 contra su paso 4, que son el caso del horario fijo que se cae por las vacaciones contra que sin verse las caras la nota no funciona igual: cero relacion entre los dos, y se emparejan por ser los dos el paso de la salvedad de su tramo"),
   ("tomar_notas_copia_guion_reunion_individual", "similitud de texto",
    "aquel pone el soporte de la sesion y este su calendario. El par emparejado es mi paso 4 contra su paso 5, que son el horario fijo que se cae contra lo que simboliza escribirlo"),
   ("cubrir_indicadores_problemas_reunion_individual", "similitud de texto",
    "aquel pone el contenido y este la fecha. El par emparejado es mi paso 5 contra su paso 10, que son que en cadena eso se evita facilmente contra que las cuestiones que preocupan tardan en aflorar: los dos son la frase de cierre de su tramo"),
   ("facilitar_expresion_subordinado_pregunta_mas", "similitud de texto",
    "aquel pone el papel del supervisor dentro y este la fecha de la siguiente. El par emparejado es mi paso 1 contra su paso 2, que son programar en cadena contra estar en la reunion para aprender y orientar"),
   ("preguntar_conducir_reunion_individual", "familia de id",
    "SEGUNDO VECINO DE OTRO LIBRO LEVANTADO POR LA SENIAL 2 CON LA 1 MUY POR DEBAJO, igual que en el candidato 5. Aquel, de zhuo_manager, trae las preguntas con que se conduce la reunion y este dice cuando se fija la siguiente. El par emparejado es mi paso 3 contra su paso 7, que son tener en cuenta los demas compromisos contra el grupo de preguntas de apoyar. SANO: comparten la reunion de la que hablan y nada mas"),
   ("dirigir_reunion_individual_semanal", "familia de id",
    "ES EL VECINO DE LA FRONTERA DE d052, Y AQUI SI LO LEVANTA UNA SENIAL, aunque sea la 2 y con la 1 en la banda mas baja. LO DIGO ENTERO PORQUE NO ME FAVORECE CALLARLO: lo que la ACTA 50 mide en 50.5.b es que la senial no levanta el par de aquel nodo con cubrir_indicadores_problemas_reunion_individual, y ese par sigue sin levantarse; lo que este informe anade es que el mismo vecino aparece por otro lado. SANO, y la razon: aquel, de zhuo_manager, dirige la reunion semanal entera y este solo pone cuando se fija la siguiente. El par emparejado es mi paso 5 contra su paso 2. LA CONTRADICCION DE DOCTRINA QUE d052 DECLARA NO ESTA EN ESTE PAR: esta en el otro, y por eso la frontera se escribe alli y no aqui"),
 ]),
}

CABECERA = (
 " VEREDICTO ESCRITO POR LECTURA EN LA VUELTA 52, ANTES DE CUALQUIER INSERCION Y CON LOS VECINOS LEIDOS ENTEROS "
 "(EXTRACTOR.md 2: si la aduana bloquea, se leen los vecinos antes de escribir el veredicto; manual principio 4: las seniales ordenan, nunca deciden). "
 "SU SEDE ES bitacora/VEREDICTOS.jsonl Y HOY NO PUEDE LLEGAR ALLI, porque esa sede la escribe forja.py insertar y la puerta de D.39 mide CERRADA para grove_high_output en esta vuelta (.v52/puerta_d39.txt). "
 "Queda escrito aqui, dentro de la ficha que viaja, para que el dia de la insercion se escriba en su sede con esta razon y no con una nueva. "
 "Y SE ESCRIBE YA SIN DIGITO DENTRO, QUE ES d051 APLICADA DESDE EL PRINCIPIO (TAREA 3.b): "
 "la senial que levanta cada vecino se nombra, pero SU NUMERO NO SE COPIA AQUI, porque este mismo bloque entra en el resumen_teorico del que la senial se calcula "
 "(src/aduana.py senal_similitud_texto sobre comun.texto_comparable) y un numero escrito dentro de su propia poblacion deja de reproducirse en cuanto se escribe. "
 "LA SEDE DEL DIGITO DE ESTA FICHA ES %s, que es el informe que la aduana imprimio en la pasada de esta ficha en la vuelta 52, con la poblacion de ese acto. "
 "Quien quiera la cifra la lee alli, donde si se puede recontar. "
)


def main():
    grafo = {}
    for linea in GRAFO.read_text(encoding="utf-8").splitlines():
        if linea.strip():
            n = json.loads(linea)
            grafo[n["id"]] = n

    total_pares = 0
    filas = []
    for idc, (informe, lista) in VEREDICTOS.items():
        p = BASE / ("%s.json" % idc)
        d = json.loads(p.read_text(encoding="utf-8"))
        viejo = d["resumen_teorico"]
        assert "VEREDICTO ESCRITO POR LECTURA EN LA VUELTA 52" not in viejo, "ya escrito: %s" % idc
        trozos = [CABECERA % informe]
        comunes_ficha = 0
        for vecino, senial, razon in lista:
            pv = BASE / ("%s.json" % vecino)
            if pv.exists():
                dv = json.loads(pv.read_text(encoding="utf-8"))
                sede = "bandeja"
            else:
                dv = grafo[vecino]
                sede = "grafo"
            comunes = len(set(d["pasos_accionables"]) & set(dv["pasos_accionables"]))
            comunes_ficha += comunes
            trozos.append(
                " VEREDICTO SANO sobre el vecino %s (%s), levantado por %s: son HERMANOS. RAZON: %s. "
                "PASOS LITERALMENTE COMUNES ENTRE LOS DOS, CONTADOS POR .v52/veredictos.py Y NO AFIRMADOS: %d."
                % (vecino, sede, senial, razon, comunes))
            total_pares += 1
        d["resumen_teorico"] = viejo + "".join(trozos)

        a = json.loads(p.read_text(encoding="utf-8"))
        assert d["resumen_teorico"].startswith(viejo)
        assert a["pasos_accionables"] == d["pasos_accionables"]
        assert a["titulo"] == d["titulo"]
        assert a.get("atribuciones") == d.get("atribuciones")
        p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        filas.append((idc, len(lista), comunes_ficha, informe))

    print("    %-48s %7s %9s  %s" % ("candidato", "pares", "comunes", "sede del digito"))
    for idc, n, c, inf in filas:
        print("    %-48s %7d %9d  %s" % (idc[:48], n, c, inf))
    print()
    print("    PARES DE COLA DE LA TANDA, veredictados uno a uno : %d" % total_pares)
    print("    PASOS LITERALMENTE COMUNES en los %d pares        : %d" % (total_pares, sum(f[2] for f in filas)))
    print("    DIGITOS DE SENIAL ESCRITOS DENTRO DE LAS FICHAS   : 0   (d051 aplicada desde el principio)")
    print("    ASERCION: pasos, titulo y atribuciones identicos, y el texto viejo es PREFIJO del nuevo en las 6.")


if __name__ == "__main__":
    main()
