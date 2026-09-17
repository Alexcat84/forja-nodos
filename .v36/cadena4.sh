#!/bin/sh
# Cadena desde el candidato 5. El archivado D.31 va DENTRO de la misma funcion que
# corre la aduana, detras de su codigo de salida: es remedio mecanico, no memoria.
cd /c/Users/AlexDesk/Documents/forja-nodos
COMUN="--sin-preguntas --censo caso=no --censo marco_pais=no --censo vigencia=no --censo herramienta=no"
SERIE2P="serie=las tres cosas que facilitan un despido;papel=paso;cabeza=facilitar_despido_tres_cosas"
SERIE2C="serie=las tres cosas que facilitan un despido;papel=cabeza;nota=la cuenta esta escrita en la linea 173 del capitulo"

corre() {
  salida="$1"; shift
  id="$1"; shift
  { echo "\$ python forja.py insertar cuarentena/scott_radical_candor/$id.json [veredictos y censos]"
    python forja.py insertar "cuarentena/scott_radical_candor/$id.json" "$@"
    echo "CODIGO DE SALIDA: $?"
  } > ".v36/informes/$salida" 2>&1 < /dev/null
  if ! grep -q "CODIGO DE SALIDA: 0" ".v36/informes/$salida"; then
    echo "PARADA EN $id" >> .v36/informes/_cadena.txt
    exit 1
  fi
  git mv "cuarentena/scott_radical_candor/$id.json" "cuarentena/_insertados/scott_radical_candor/$id.json" >> ".v36/informes/$salida" 2>&1
  echo "  ARCHIVADO EN EL MISMO ACTO (D.31): cuarentena/_insertados/scott_radical_candor/$id.json" >> ".v36/informes/$salida"
  echo "OK $id  ($(wc -l < dataset/nodos.jsonl) nodos, bandeja $(ls cuarentena/scott_radical_candor/*.json | wc -l))" >> .v36/informes/_cadena.txt
}

echo "cadena 4 arrancada desde el candidato 5" >> .v36/informes/_cadena.txt

corre 05_plan_anual.txt armar_plan_anual_crecimiento_equipo \
 --veredicto "desplegar_tres_conversaciones_carrera|SANO|NO son el mismo trabajo y ninguno nombra al otro sin desplegarlo. La cabeza de las conversaciones de carrera se activa al desplegar la franqueza radical y entrega tres conversaciones tenidas; este se activa UNA VEZ AL ANIO (linea 99) y entrega un plan de crecimiento por persona con los nombres en sus casillas. Su paso 1 recuerda que las tres conversaciones ya ocurrieron, que es el encadenado de la linea 97, y recordar no es continuar." \
 --veredicto "desplegar_plan_orden_operaciones_franqueza_radical|CONTINUA|madre=desplegar_plan_orden_operaciones_franqueza_radical|ARISTA D.29: la madre NOMBRA el procedimiento en una linea y el hijo lo DESPLIEGA. El paso 32 de la madre es literalmente Planea el futuro de tu equipo, empieza a hacer un plan de gestion del crecimiento para cada persona de tu equipo, y ahi se acaba: no dice ni las casillas, ni la mirada de fuera, ni los tres a cinco puntos, ni la equidad entre niveles. El hijo pone las cuatro etapas en 29 pasos de las lineas 93 a 125. Es el par que la senial SI levanta, paso_contra_nodo 0.741, y es el mismo ejemplar de la linea 371 de la bitacora. La madre espera en la bandeja de cap_12, asi que la arista queda EN COLA." \
 --veredicto "disenar_equipo_plan_anual|SANO|EL familia_id MAS ALTO DEL TRAMO, 0.500, Y AUN ASI SON HERMANOS. Lo que comparten son las palabras plan, anual y equipo, y los dos libros son distintos. Lo que planifica el de Zhuo es A QUIEN CONTRATAR: organigrama a final de anio, huecos de habilidades y lista de puestos abiertos. Lo que planifica este es COMO CRECE LA GENTE QUE YA TIENES: nombres en casillas y un plan de tres a cinco puntos por persona. Ni el mismo objeto de trabajo ni el mismo entregable, y ninguno nombra al otro en una linea. Es la banda de familia leida como manda EXTRACTOR.md 11: la senial ordena, no decide." \
 --censo "serie=no" $COMUN

corre 06_contratacion.txt montar_proceso_contratacion_reducir_sesgo \
 --veredicto "armar_plan_anual_crecimiento_equipo|SANO|COMPARTEN EL VOCABULARIO DE LAS CASILLAS Y NO EL TRABAJO. El plan anual reparte a la gente que YA esta en tu equipo entre estrellas de rock y superestrellas para escribirle a cada una su plan de crecimiento; este monta el proceso por el que entra gente que aun no esta, y su unica frase de proporcion (linea 129, si tienes demasiadas superestrellas contrata una estrella de rock) es criterio de contratacion, no de crecimiento." \
 --veredicto "disenar_equipo_plan_anual|SANO|UNO DICE A CUANTA GENTE Y CON QUE PERFIL, EL OTRO DICE COMO SE ELIGE. El de Zhuo entrega el organigrama futuro, los huecos y la lista de puestos abiertos, y su paso 11 usa ese plan como marco para evaluar candidatos SIN decir como se evalua. Este pone el como: descripcion del puesto escrita por quien contrata, filtro previo a ciegas, comite de cuatro, entrevistas informales, apuntes en el momento y reunion presencial con sesgo hacia el no, de las lineas 133 a 163. NO declaro CONTINUA porque la linea del de Zhuo no nombra este procedimiento: nombra el marco de su propio plan, que es otra cosa, y declarar la arista pediria una lectura que el texto no sostiene." \
 --censo "serie=no" $COMUN

corre 07_despido_cabeza.txt facilitar_despido_tres_cosas \
 --veredicto "armar_plan_anual_crecimiento_equipo|CONTINUA|madre=armar_plan_anual_crecimiento_equipo|ARISTA D.29 DECLARADA POR LECTURA: la madre NOMBRA el procedimiento en una linea y el hijo lo DESPLIEGA. El paso 17 de la madre sale de la linea 111 (At some point, you have to initiate the process of firing these people) y ahi se acaba: la madre no dice ni una de las tres cosas. El hijo pone los dos errores opuestos de las empresas, la premisa de que despedir es duro y debe serlo, y la cuenta de tres de la linea 173 con sus tres partes nombradas. Ninguna senial la levanta, y D.19 ya midio que no la va a levantar." \
 --censo "$SERIE2C" $COMUN

corre 08_admitir.txt admitir_pronto_mal_desempenio_cuatro_razones \
 --veredicto "facilitar_despido_tres_cosas|CONTINUA|madre=facilitar_despido_tres_cosas|ARISTA D.37: la cabeza escribe la cuenta en la linea 173 (But if you do three things) y su paso 11 nombra las tres. Este hijo es la PRIMERA y la despliega en 9 pasos que la cabeza no tiene: el ejercicio de las casillas de la linea 177 y las cuatro razones numeradas de la linea 179, que la cabeza ni menciona." \
 --veredicto "armar_plan_anual_crecimiento_equipo|SANO|LAS DOS CASILLAS SON LAS MISMAS Y EL TRABAJO NO. El plan anual pone nombres en las casillas para escribir planes de crecimiento y se activa una vez al anio; este usa el mismo ejercicio como PRUEBA de la resistencia a nombrar a quien rinde por debajo, y se activa cuando alguien EMPIEZA a rendir por debajo. Ni una de las cuatro razones de la linea 179 esta en el plan anual." \
 --censo "$SERIE2P" $COMUN

corre 09_calibrar_despido.txt calibrar_decision_despido_documentarla \
 --veredicto "facilitar_despido_tres_cosas|CONTINUA|madre=facilitar_despido_tres_cosas|ARISTA D.37: la cabeza escribe la cuenta en la linea 173 y su paso 11 nombra las tres. Este hijo es la SEGUNDA y la despliega en 13 pasos que la cabeza no tiene: los tres sitios donde se pide ayuda de la linea 183, la regla de que no basta pedir consejo sino que hay que conseguir que editen lo que escribes, y el mecanismo de fallo del plan de mejora de la linea 185." \
 --veredicto "admitir_pronto_mal_desempenio_cuatro_razones|SANO|HERMANOS de la misma serie de tres, con la cabeza por madre. Uno admite el bajo desempenio pronto y el otro decide el despido sin tomarlo solo: se encadenan en el tiempo y ninguno nombra el procedimiento del otro en una linea. D.37 manda SANO para el vecino que no es la cabeza." \
 --veredicto "trazar_plan_dieciocho_meses_aprendizaje|SANO|EL MISMO PAR QUE YA JUZGUE AL INSERTAR trazar_plan, ahora por el otro lado. similitud_texto lo levanta por el paso 12 contra el paso 12, y los dos empiezan por asegurate de que, que es una formula que escribi yo. Uno exige elementos de accion en la lista de aprendizaje de la linea 81 y el otro exige que alguien con experiencia edite los documentos del despido de la linea 187: ni el mismo objeto ni la misma activacion." \
 --censo "$SERIE2P" $COMUN

corre 10_sopesar.txt sopesar_consejo_legal_despedir_humildad \
 --veredicto "facilitar_despido_tres_cosas|CONTINUA|madre=facilitar_despido_tres_cosas|ARISTA D.37: la cabeza escribe la cuenta en la linea 173 y su paso 11 nombra las tres. Este hijo es la TERCERA y la despliega en 8 pasos que la cabeza no tiene: la pregunta que le da la vuelta al consejo legal de la linea 193 (cual es el riesgo de NO hacerlo) y el recordatorio de la linea 195 de que lo que es malo es el puesto y no la persona." \
 --veredicto "calibrar_decision_despido_documentarla|SANO|HERMANOS de la misma serie de tres. El segundo manda pedir consejo a jefe, iguales y recursos humanos; el tercero dice que no te quedes atrapada en ese consejo. Son la ida y la vuelta de la misma seccion del libro y ninguno despliega al otro: los dos cuelgan de la cabeza de la linea 173." \
 --veredicto "admitir_pronto_mal_desempenio_cuatro_razones|SANO|HERMANOS de la misma serie de tres, con la cabeza por madre. Uno admite pronto el bajo desempenio y este despide con humildad una vez tomada la decision: ni el mismo momento ni el mismo objeto, y ninguno nombra el procedimiento del otro." \
 --censo "$SERIE2P" $COMUN

corre 11_contactar.txt contactar_despedido_mes_despues \
 --veredicto "facilitar_despido_tres_cosas|SANO|ES LA CODA Y NO LA CUARTA PARTE, y esa es exactamente la figura que D.37 manda juzgar SANO. La linea 173 escribe TRES y esta seccion es la cuarta bajo el mismo rotulo FIRING; su condicion de activacion es otra (cuando hace un mes que despediste, no cuando vas a despedir) y su entregable es otro. Una cabeza de tres y un vecino que no es ninguna de las tres son hermanos." \
 --veredicto "sopesar_consejo_legal_despedir_humildad|SANO|EL DE ANTES ES EL DESPIDO Y ESTE ES LO QUE VIENE DESPUES. La tercera parte de la serie se activa cuando vas a despedir y entrega el despido dado con humildad; esta coda se activa un mes despues y entrega el contacto hecho o el silencio respetado. Ninguna nombra el procedimiento de la otra." \
 --censo "serie=no" $COMUN

corre 12_ascensos.txt calibrar_ascensos_evitar_politica \
 --veredicto "armar_plan_anual_crecimiento_equipo|SANO|LAS DOS CALIBRAN CON LOS IGUALES Y NO CALIBRAN LO MISMO. El plan anual compara notas de crecimiento para no ser correctora blanda ni dura (linea 117); este calibra ASCENSOS antes de que se aprueben (linea 213) y trae su propia reunion con sus consejos de las lineas 215 a 223. Ninguno nombra el procedimiento del otro en una linea." \
 --censo "serie=no" $COMUN

corre 13_obsesion.txt evitar_obsesion_ascenso_estatus \
 --veredicto "calibrar_ascensos_evitar_politica|SANO|UNO DECIDE EL ASCENSO Y EL OTRO DECIDE SI SE ANUNCIA. El de la calibracion se activa cuando se acerca el ciclo y entrega los ascensos calibrados; este se activa cuando vas a anunciarlos o a elogiar en publico y entrega el correo de celebracion NO enviado (linea 231). Son consecutivos en el libro y ninguno despliega al otro." \
 --veredicto "desplegar_plan_orden_operaciones_franqueza_radical|CONTINUA|madre=desplegar_plan_orden_operaciones_franqueza_radical|ARISTA D.29: el paso 33 de la madre dice Asegurate de que no estas creando una cultura obsesionada con el ascenso, y dedica un pensamiento extra a como estas recompensando a tus superestrellas, y ahi se acaba. El hijo pone el como en 10 pasos de las lineas 229 a 237: el correo que no se manda, el cambio de papel que si se anuncia porque no todo cambio de papel es un ascenso, y el elogio apuntado al trabajo y no al estatus. La madre espera en la bandeja de cap_12, asi que la arista queda EN COLA." \
 --censo "serie=no" $COMUN

corre 14_reconocer.txt reconocer_excelencia_trayectoria_gradual \
 --veredicto "evitar_obsesion_ascenso_estatus|SANO|SON LOS DOS NODOS DEL TRAMO L225 A L251 Y LOS PARTE LA ACTIVACION, no el rotulo, que es lo que la ACTA 20 seccion 4.3 adjudico. El primero se activa cuando vas a anunciar un ascenso; este se activa cuando tienes a alguien excelente en trayectoria gradual al que NO vas a ascender, y entrega el agradecimiento, el papel de referente y la presentacion publica de las lineas 243 a 251. El elogio en publico aparece en los dos y en cada uno hace otra cosa." \
 --censo "serie=no" $COMUN

echo "CADENA COMPLETA: los 14 de cap_10" >> .v36/informes/_cadena.txt
