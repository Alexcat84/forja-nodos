#!/bin/sh
cd /c/Users/AlexDesk/Documents/forja-nodos
COMUN='--censo caso=no --censo marco_pais=no --censo vigencia=no --censo herramienta=no'
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
  echo "OK $id  ($(wc -l < dataset/nodos.jsonl) nodos)" >> .v36/informes/_cadena.txt
}

corre 05_plan_anual.txt armar_plan_anual_crecimiento_equipo \
 --veredicto "desplegar_tres_conversaciones_carrera|SANO|NO son el mismo trabajo y ninguno nombra al otro sin desplegarlo. La cabeza de las conversaciones de carrera se activa al desplegar la franqueza radical y entrega tres conversaciones tenidas; este se activa UNA VEZ AL ANIO (linea 99) y entrega un plan de crecimiento por persona con los nombres en sus casillas. Su paso 1 recuerda que las tres conversaciones ya ocurrieron, que es el encadenado de la linea 97, y recordar no es continuar." \
 --censo "serie=no" $COMUN

corre 06_contratacion.txt montar_proceso_contratacion_reducir_sesgo \
 --veredicto "armar_plan_anual_crecimiento_equipo|SANO|COMPARTEN EL VOCABULARIO DE LAS CASILLAS Y NO EL TRABAJO. El plan anual reparte a la gente que YA esta en tu equipo entre estrellas de rock y superestrellas para escribirle a cada una su plan de crecimiento; este monta el proceso por el que entra gente que aun no esta, y su unica frase de proporcion (linea 129, si tienes demasiadas superestrellas contrata una estrella de rock) es criterio de contratacion, no de crecimiento." \
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
 --censo "$SERIE2P" $COMUN

corre 10_sopesar.txt sopesar_consejo_legal_despedir_humildad \
 --veredicto "facilitar_despido_tres_cosas|CONTINUA|madre=facilitar_despido_tres_cosas|ARISTA D.37: la cabeza escribe la cuenta en la linea 173 y su paso 11 nombra las tres. Este hijo es la TERCERA y la despliega en 8 pasos que la cabeza no tiene: la pregunta que le da la vuelta al consejo legal de la linea 193 (cual es el riesgo de NO hacerlo) y el recordatorio de la linea 195 de que lo que es malo es el puesto y no la persona." \
 --veredicto "calibrar_decision_despido_documentarla|SANO|HERMANOS de la misma serie de tres. El segundo manda pedir consejo a jefe, iguales y recursos humanos; el tercero dice que no te quedes atrapada en ese consejo. Son la ida y la vuelta de la misma seccion del libro y ninguno despliega al otro: los dos cuelgan de la cabeza de la linea 173." \
 --censo "$SERIE2P" $COMUN

corre 11_contactar.txt contactar_despedido_mes_despues \
 --veredicto "facilitar_despido_tres_cosas|SANO|ES LA CODA Y NO LA CUARTA PARTE, y esa es exactamente la figura que D.37 manda juzgar SANO. La linea 173 escribe TRES y esta seccion es la cuarta bajo el mismo rotulo FIRING; su condicion de activacion es otra (cuando hace un mes que despediste, no cuando vas a despedir) y su entregable es otro. Una cabeza de tres y un vecino que no es ninguna de las tres son hermanos." \
 --censo "serie=no" $COMUN

corre 12_ascensos.txt calibrar_ascensos_evitar_politica \
 --veredicto "armar_plan_anual_crecimiento_equipo|SANO|LAS DOS CALIBRAN CON LOS IGUALES Y NO CALIBRAN LO MISMO. El plan anual compara notas de crecimiento para no ser correctora blanda ni dura (linea 117); este calibra ASCENSOS antes de que se aprueben (linea 213) y trae su propia reunion con sus consejos de las lineas 215 a 223. Ninguno nombra el procedimiento del otro en una linea." \
 --censo "serie=no" $COMUN

corre 13_obsesion.txt evitar_obsesion_ascenso_estatus \
 --veredicto "calibrar_ascensos_evitar_politica|SANO|UNO DECIDE EL ASCENSO Y EL OTRO DECIDE SI SE ANUNCIA. El de la calibracion se activa cuando se acerca el ciclo y entrega los ascensos calibrados; este se activa cuando vas a anunciarlos o a elogiar en publico y entrega el correo de celebracion NO enviado (linea 231). Son consecutivos en el libro y ninguno despliega al otro." \
 --censo "serie=no" $COMUN

corre 14_reconocer.txt reconocer_excelencia_trayectoria_gradual \
 --veredicto "evitar_obsesion_ascenso_estatus|SANO|SON LOS DOS NODOS DEL TRAMO L225 A L251 Y LOS PARTE LA ACTIVACION, no el rotulo, que es lo que la ACTA 20 seccion 4.3 adjudico. El primero se activa cuando vas a anunciar un ascenso; este se activa cuando tienes a alguien excelente en trayectoria gradual al que NO vas a ascender, y entrega el agradecimiento, el papel de referente y la presentacion publica de las lineas 243 a 251. El elogio en publico aparece en los dos y en cada uno hace otra cosa." \
 --censo "serie=no" $COMUN
