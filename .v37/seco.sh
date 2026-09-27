#!/bin/sh
# Informe EN SECO, uno por vez y en el orden del libro (EXTRACTOR.md 12.2 y 12.3).
# Cero inserciones: es la cola de vecinos que D.43 NO me quito cuando es de un
# candidato suelto, y esta corrida no trae cola sellada del arnes.
cd /c/Users/AlexDesk/Documents/forja-nodos
i=0
for id in \
  contar_historias_propias_explicar_franqueza_radical \
  mejorar_consciencia_propia_relacional_dos_practicas \
  contar_cuatro_historias_propias_ver_hueco_intencion \
  practicar_triangulo_critica_tres_papeles \
  pedir_critica_primero_crear_seguridad_psicologica \
  elegir_pregunta_recurrente_pedir_critica \
  resolver_dudas_frecuentes_pedir_critica \
  abrazar_incomodidad_silencio_contar_seis \
  escuchar_entender_critica_dominar_defensa \
  premiar_franqueza_hacer_escucha_tangible \
  integrar_peticion_critica_rutina_existente \
  dar_elogio_disciplina_igual_critica \
  medir_critica_respuesta_oyente_brujula
do
  i=$((i+1))
  { echo "\$ python forja.py informe cuarentena/scott_radical_candor/$id.json"
    python forja.py informe "cuarentena/scott_radical_candor/$id.json"
    echo "CODIGO DE SALIDA: $?"
  } > ".v37/informes/seco_$(printf %02d $i)_$id.txt" 2>&1 < /dev/null
  echo "seco $i $id" >> .v37/informes/_seco.txt
done
echo "CADENA EN SECO COMPLETA" >> .v37/informes/_seco.txt
