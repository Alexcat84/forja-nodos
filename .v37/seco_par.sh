#!/bin/sh
# El informe EN SECO es de SOLO LECTURA: no escribe nada y la poblacion no se
# mueve mientras corre, asi que los candidatos que faltan se pueden medir a la
# vez. LA INSERCION NO: esa sigue siendo uno por vez, porque el primero que
# entra cambia lo que el segundo mide (EXTRACTOR.md 12.3).
cd /c/Users/AlexDesk/Documents/forja-nodos
uno() {
  n="$1"; id="$2"
  { echo "\$ python forja.py informe cuarentena/scott_radical_candor/$id.json"
    python forja.py informe "cuarentena/scott_radical_candor/$id.json"
    echo "CODIGO DE SALIDA: $?"
  } > ".v37/informes/seco_${n}_${id}.txt" 2>&1 < /dev/null
  echo "seco $n $id" >> .v37/informes/_seco.txt
}
uno 00 desplegar_plan_orden_operaciones_franqueza_radical &
uno 03 contar_cuatro_historias_propias_ver_hueco_intencion &
uno 04 practicar_triangulo_critica_tres_papeles &
uno 05 pedir_critica_primero_crear_seguridad_psicologica &
uno 06 elegir_pregunta_recurrente_pedir_critica &
uno 07 resolver_dudas_frecuentes_pedir_critica &
uno 08 abrazar_incomodidad_silencio_contar_seis &
uno 09 escuchar_entender_critica_dominar_defensa &
uno 10 premiar_franqueza_hacer_escucha_tangible &
uno 11 integrar_peticion_critica_rutina_existente &
uno 12 dar_elogio_disciplina_igual_critica &
uno 13 medir_critica_respuesta_oyente_brujula &
wait
echo "CADENA EN SECO COMPLETA" >> .v37/informes/_seco.txt
