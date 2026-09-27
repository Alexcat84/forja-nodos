#!/bin/sh
# Cadena desde el candidato 8. Mismo arnes: la aduana y el archivado D.31 en la
# misma funcion, y --sin-preguntas para que un vecino no previsto imprima su cola
# entera y devuelva BLOQUEO en vez de reventar contra un input() sin terminal.
cd /c/Users/AlexDesk/Documents/forja-nodos
COMUN="--sin-preguntas --censo caso=no --censo marco_pais=no --censo vigencia=no --censo herramienta=no"
SERIE2P="serie=las tres cosas que facilitan un despido;papel=paso;cabeza=facilitar_despido_tres_cosas"

# LA MISMA CAIDA TRES VECES, Y LA MISMA RAZON: la senial 1 de este tramo la levanta
# una formula imperativa MIA (que es lo que el texto dice, asegurate de que, no te
# quedes), no material del libro. Cada par va leido y juzgado uno a uno igual.
FORMULA="LA SEMEJANZA ES MIA, NO DEL LIBRO, y es el tercer par del tramo con la misma causa. similitud_texto la levanta en la banda de 0.35 a 0.38, por debajo del 0.4 que EXTRACTOR.md 11 llama gemelos seguros, y el detalle senala pasos que comparten una formula imperativa que escribi yo en los dos sitios. Lo que dicen los dos pasos no se toca."

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

echo "cadena 5 arrancada desde el candidato 8" >> .v36/informes/_cadena.txt

corre 08_admitir.txt admitir_pronto_mal_desempenio_cuatro_razones \
 --veredicto "facilitar_despido_tres_cosas|CONTINUA|madre=facilitar_despido_tres_cosas|ARISTA D.37: la cabeza escribe la cuenta en la linea 173 (But if you do three things) y su paso 11 nombra las tres. Este hijo es la PRIMERA y la despliega en 9 pasos que la cabeza no tiene: el ejercicio de las casillas de la linea 177 y las cuatro razones numeradas de la linea 179, que la cabeza ni menciona." \
 --veredicto "armar_plan_anual_crecimiento_equipo|SANO|LAS DOS CASILLAS SON LAS MISMAS Y EL TRABAJO NO. El plan anual pone nombres en las casillas para escribir planes de crecimiento y se activa una vez al anio; este usa el mismo ejercicio como PRUEBA de la resistencia a nombrar a quien rinde por debajo, y se activa cuando alguien EMPIEZA a rendir por debajo. Ni una de las cuatro razones de la linea 179 esta en el plan anual." \
 --veredicto "trazar_plan_dieciocho_meses_aprendizaje|SANO|$FORMULA Aqui la senial da 0.356 y senala mi paso 5 contra su paso 12: los dos acaban en que es lo que el texto dice. Uno manda no pasar a otra cosa hasta que todos los nombres esten en las casillas de bajo desempenio (linea 177) y el otro manda meter elementos de accion en la lista de aprendizaje (linea 81). Ni el mismo objeto ni la misma activacion, y ninguno nombra al otro." \
 --veredicto "sopesar_consejo_legal_despedir_humildad|SANO|DOS COSAS A LA VEZ, y las dos dan SANO. Son HERMANOS de la misma serie de tres de la linea 173, con la cabeza por madre, y D.37 manda SANO para el vecino que no es la cabeza. Y ademas $FORMULA Aqui da 0.374 sobre mi paso 5 contra su paso 1, y lo que comparten es empezar por una negacion y cerrar con que es lo que el texto dice." \
 --censo "$SERIE2P" $COMUN

corre 09_calibrar_despido.txt calibrar_decision_despido_documentarla \
 --veredicto "facilitar_despido_tres_cosas|CONTINUA|madre=facilitar_despido_tres_cosas|ARISTA D.37: la cabeza escribe la cuenta en la linea 173 y su paso 11 nombra las tres. Este hijo es la SEGUNDA y la despliega en 13 pasos que la cabeza no tiene: los tres sitios donde se pide ayuda de la linea 183, la regla de que no basta pedir consejo sino que hay que conseguir que editen lo que escribes, y el mecanismo de fallo del plan de mejora de la linea 185." \
 --veredicto "admitir_pronto_mal_desempenio_cuatro_razones|SANO|HERMANOS de la misma serie de tres, con la cabeza por madre. Uno admite el bajo desempenio pronto y el otro decide el despido sin tomarlo solo: se encadenan en el tiempo y ninguno nombra el procedimiento del otro en una linea. D.37 manda SANO para el vecino que no es la cabeza." \
 --veredicto "trazar_plan_dieciocho_meses_aprendizaje|SANO|EL MISMO PAR QUE YA JUZGUE AL INSERTAR trazar_plan, ahora por el otro lado. similitud_texto lo levanta por el paso 12 contra el paso 12, y los dos empiezan por asegurate de que, que es una formula que escribi yo. Uno exige elementos de accion en la lista de aprendizaje de la linea 81 y el otro exige que alguien con experiencia edite los documentos del despido de la linea 187: ni el mismo objeto ni la misma activacion." \
 --veredicto "sopesar_consejo_legal_despedir_humildad|SANO|HERMANOS de la misma serie de tres. Este manda pedir consejo a jefe, iguales y recursos humanos (linea 183); el tercero dice que no te quedes atrapada en ese consejo (linea 191). Son la ida y la vuelta de la misma seccion del libro y ninguno despliega al otro: los dos cuelgan de la cabeza de la linea 173." \
 --censo "$SERIE2P" $COMUN

corre 10_sopesar.txt sopesar_consejo_legal_despedir_humildad \
 --veredicto "facilitar_despido_tres_cosas|CONTINUA|madre=facilitar_despido_tres_cosas|ARISTA D.37: la cabeza escribe la cuenta en la linea 173 y su paso 11 nombra las tres. Este hijo es la TERCERA y la despliega en 8 pasos que la cabeza no tiene: la pregunta que le da la vuelta al consejo legal de la linea 193 (cual es el riesgo de NO hacerlo) y el recordatorio de la linea 195 de que lo que es malo es el puesto y no la persona." \
 --veredicto "calibrar_decision_despido_documentarla|SANO|HERMANOS de la misma serie de tres. El segundo manda pedir consejo a jefe, iguales y recursos humanos; este dice que no te quedes atrapada en ese consejo. Son la ida y la vuelta de la misma seccion del libro y ninguno despliega al otro: los dos cuelgan de la cabeza de la linea 173." \
 --veredicto "admitir_pronto_mal_desempenio_cuatro_razones|SANO|HERMANOS de la misma serie de tres, con la cabeza por madre, y el par ya lo juzgue por el otro lado al insertar admitir_pronto. Uno admite pronto el bajo desempenio y este despide con humildad una vez tomada la decision: ni el mismo momento ni el mismo objeto." \
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
