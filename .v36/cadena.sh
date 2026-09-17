#!/bin/sh
cd /c/Users/AlexDesk/Documents/forja-nodos
COMUN='--censo caso=no --censo marco_pais=no --censo vigencia=no --censo herramienta=no'
SERIE1="serie=las tres conversaciones de carrera;papel=paso;cabeza=desplegar_tres_conversaciones_carrera"
SERIE2="serie=las tres cosas que facilitan un despido;papel=paso;cabeza=facilitar_despido_tres_cosas"

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

echo "cadena arrancada" > .v36/informes/_cadena.txt

corre 02_historia.txt conversar_historia_vida_descubrir_motivadores \
 --veredicto "desplegar_tres_conversaciones_carrera|CONTINUA|madre=desplegar_tres_conversaciones_carrera|ARISTA D.37: la cabeza escribe la cuenta y nombra las partes (linea 43, a succession of three forty-five-minute conversations) y su paso 9 la transcribe. Este hijo es la PRIMERA de las tres y la despliega en 15 pasos que la cabeza no tiene: la apertura literal de la linea 49, los momentos de cambio, los cuatro motivadores ejemplares y el limite de no presionar de la linea 53. La cabeza no da ni uno de esos pasos." \
 --censo "$SERIE1" $COMUN

corre 03_suenios.txt conversar_suenios_cruzar_habilidades \
 --veredicto "desplegar_tres_conversaciones_carrera|CONTINUA|madre=desplegar_tres_conversaciones_carrera|ARISTA D.37: la cabeza escribe la cuenta y nombra las tres partes en la linea 43. Este hijo es la SEGUNDA y la despliega en 15 pasos que la cabeza no tiene: la pregunta de arranque literal de la linea 69, los tres a cinco suenios, el cuadro de columnas y filas de la linea 71 y la comprobacion contra los valores de la linea 73." \
 --veredicto "conversar_historia_vida_descubrir_motivadores|SANO|HERMANOS, no madre e hijo: las dos son partes de la misma serie de tres y su madre es la cabeza, no la otra. La primera saca motivadores de la historia de vida (linea 49) y la segunda saca suenios y los cruza con habilidades (lineas 69 a 71). D.37 lo dice literal: un vecino que no es la cabeza ni ninguna de las otras partes es hermano, y su veredicto es SANO." \
 --censo "$SERIE1" $COMUN

corre 04_dieciocho.txt trazar_plan_dieciocho_meses_aprendizaje \
 --veredicto "desplegar_tres_conversaciones_carrera|CONTINUA|madre=desplegar_tres_conversaciones_carrera|ARISTA D.37: la cabeza escribe la cuenta y nombra las tres partes en la linea 43. Este hijo es la TERCERA y la despliega en 14 pasos que la cabeza no tiene: las cuatro preguntas literales de la linea 79, el horizonte de seis a dieciocho meses y la lista de la linea 81 con quien hace que y para cuando." \
 --veredicto "conversar_suenios_cruzar_habilidades|SANO|HERMANOS de la misma serie de tres, con la cabeza por madre. La segunda conversacion produce los suenios y el cuadro de habilidades; la tercera convierte eso en lo que hay que aprender y en la lista de la linea 81. Se encadenan en el tiempo, que es lo que la cabeza ordena, y encadenarse no es continuarse: ninguna de las dos nombra a la otra en una linea sin desplegarla." \
 --veredicto "conversar_historia_vida_descubrir_motivadores|SANO|HERMANOS de la misma serie de tres, con la cabeza por madre. La primera saca motivadores de la historia de vida y la tercera traza el plan de aprendizaje: ni comparten objeto de trabajo ni una nombra el procedimiento de la otra." \
 --censo "$SERIE1" $COMUN
