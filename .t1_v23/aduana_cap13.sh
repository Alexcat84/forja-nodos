#!/bin/sh
cd /c/Users/AlexDesk/Documents/forja-nodos
for id in mejorar_consciencia_propia_relacional_dos_practicas \
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
          medir_critica_respuesta_oyente_brujula ; do
  python forja.py informe "cuarentena/scott_radical_candor/$id.json" > ".aduana_v23/$id.txt" 2>&1
  echo "HECHO $id"
done
echo "ADUANA DE cap_13 TERMINADA"
