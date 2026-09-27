#!/bin/bash
# Censo de la vuelta 78 (COPIA DE LA VUELTA 78 de .v77ext/censo.sh con las dos rutas cambiadas a Marquet, encargo TAREA 5, y nada mas; la de
# la 77 era copia de la de la 76, que era COPIA de .v75ext/censo.sh con las dos rutas de Gerber y el ls de insertados con 2>/dev/null,
# porque cuarentena/_insertados/<libro>/ no existe mientras no entre ninguna): se corre al abrir y al cerrar.
echo "nodos en dataset/nodos.jsonl        : $(wc -l < dataset/nodos.jsonl)"
echo "veredictos en bitacora              : $(wc -l < bitacora/VEREDICTOS.jsonl)"
echo "pares mutuos                        : $(wc -l < config/pares_mutuos.jsonl)"
echo "bandeja cuarentena/marquet_turn_the_ship : $(ls cuarentena/marquet_turn_the_ship/*.json | wc -l)"
echo "insertados de marquet_turn_the_ship : $(ls cuarentena/_insertados/marquet_turn_the_ship/*.json 2>/dev/null | wc -l)"
echo "cerrojos en procesos/               : $(ls procesos/ | tr '\n' ' ')"
