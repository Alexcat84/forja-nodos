#!/bin/sh
# Los tres ultimos de cap_10.
cd /c/Users/AlexDesk/Documents/forja-nodos
COMUN="--sin-preguntas --censo caso=no --censo marco_pais=no --censo vigencia=no --censo herramienta=no"

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

echo "cadena 6 arrancada desde el candidato 12" >> .v36/informes/_cadena.txt

corre 12_ascensos.txt calibrar_ascensos_evitar_politica \
 --veredicto "armar_plan_anual_crecimiento_equipo|SANO|LAS DOS CALIBRAN CON LOS IGUALES Y NO CALIBRAN LO MISMO. El plan anual compara notas de crecimiento para no ser correctora blanda ni dura (linea 117); este calibra ASCENSOS antes de que se aprueben (linea 213) y trae su propia reunion con sus consejos de las lineas 215 a 223. Ninguno nombra el procedimiento del otro en una linea." \
 --veredicto "bloquear_tiempo_pensar_calendario|SANO|LA SENIAL MAS ALTA DE TODO EL TRAMO, paso_contra_nodo 0.911, Y ES UN FALSO POSITIVO DE LONGITUD. El detalle lo dice entero: mi paso 14 contra su paso 6, y los dos son la misma frase corta y generica. El mio es Y anima a todo tu equipo a hacer lo mismo, transcripcion de la linea 219 de cap_10 (Encourage your whole team to do the same), dicha del dia de la reunion de calibracion de ascensos. El suyo es Y anima a todos los de tu equipo a hacer lo mismo, dicho de bloquear tiempo para pensar en el calendario, de cap_11. Dos pasos cortos que coinciden casi palabra por palabra NO hacen dos procedimientos iguales: ni el mismo objeto de trabajo, ni la misma activacion, ni la misma seccion del libro, y ninguno de los dos nodos nombra al otro. La senial ordena, no decide (manual principio 4)." \
 --veredicto "evitar_obsesion_ascenso_estatus|SANO|COMPARTEN LA PALABRA ASCENSO Y NADA MAS, y por eso familia_id da 0.333. Este decide QUIEN asciende y como se conduce la reunion de calibracion sin que la politica la arruine (lineas 205 a 223); el otro decide si el ascenso SE ANUNCIA y que se elogia en publico (lineas 229 a 237). Son secciones consecutivas del libro con activacion y entregable distintos, y ninguno despliega al otro." \
 --censo "serie=no" $COMUN

corre 13_obsesion.txt evitar_obsesion_ascenso_estatus \
 --veredicto "calibrar_ascensos_evitar_politica|SANO|EL MISMO PAR QUE YA JUZGUE POR EL OTRO LADO al insertar calibrar_ascensos. Uno decide el ascenso y este decide si se anuncia: el de la calibracion se activa cuando se acerca el ciclo y entrega los ascensos calibrados; este se activa cuando vas a anunciarlos o a elogiar en publico y entrega el correo de celebracion NO enviado (linea 231). Son consecutivos en el libro y ninguno despliega al otro." \
 --veredicto "desplegar_plan_orden_operaciones_franqueza_radical|CONTINUA|madre=desplegar_plan_orden_operaciones_franqueza_radical|ARISTA D.29: el paso 33 de la madre dice Asegurate de que no estas creando una cultura obsesionada con el ascenso, y dedica un pensamiento extra a como estas recompensando a tus superestrellas, y ahi se acaba. El hijo pone el como en 10 pasos de las lineas 229 a 237: el correo que no se manda, el cambio de papel que si se anuncia porque no todo cambio de papel es un ascenso, y el elogio apuntado al trabajo y no al estatus. La madre espera en la bandeja de cap_12, asi que la arista queda EN COLA." \
 --censo "serie=no" $COMUN

corre 14_reconocer.txt reconocer_excelencia_trayectoria_gradual \
 --veredicto "evitar_obsesion_ascenso_estatus|SANO|SON LOS DOS NODOS DEL TRAMO L225 A L251 Y LOS PARTE LA ACTIVACION, no el rotulo, que es lo que la ACTA 20 seccion 4.3 adjudico. El primero se activa cuando vas a anunciar un ascenso; este se activa cuando tienes a alguien excelente en trayectoria gradual al que NO vas a ascender, y entrega el agradecimiento, el papel de referente y la presentacion publica de las lineas 243 a 251. El elogio en publico aparece en los dos y en cada uno hace otra cosa." \
 --veredicto "calibrar_ascensos_evitar_politica|SANO|UNO ASCIENDE Y ESTE RECONOCE SIN ASCENDER, que es literalmente su condicion de activacion. El de la calibracion entrega los ascensos calibrados entre iguales; este se activa cuando NO vas a ascender a alguien excelente en trayectoria gradual y entrega el agradecimiento en persona y por escrito, el papel de experto de referencia y la presentacion publica. Comparten la palabra ascenso por oposicion, no por materia." \
 --censo "serie=no" $COMUN

echo "CADENA COMPLETA: los 14 de cap_10" >> .v36/informes/_cadena.txt
