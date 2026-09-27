#!/bin/bash
# Censo de la vuelta 79 (COPIA DE LA VUELTA 79 de .v78ext/censo.sh, encargo de la 79 TAREA 5, con este comentario cambiado y nada mas):
# se corre al abrir y al cerrar; ninguna linea de medida cambia.
echo "nodos en dataset/nodos.jsonl        : $(wc -l < dataset/nodos.jsonl)"
echo "veredictos en bitacora              : $(wc -l < bitacora/VEREDICTOS.jsonl)"
echo "pares mutuos                        : $(wc -l < config/pares_mutuos.jsonl)"
echo "bandeja cuarentena/marquet_turn_the_ship : $(ls cuarentena/marquet_turn_the_ship/*.json | wc -l)"
echo "insertados de marquet_turn_the_ship : $(ls cuarentena/_insertados/marquet_turn_the_ship/*.json 2>/dev/null | wc -l)"
echo "cerrojos en procesos/               : $(ls procesos/ | tr '\n' ' ')"
