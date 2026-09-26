#!/bin/bash
# Censo de la vuelta 75 (COPIA de .v74ext/censo.sh, encargo TAREA 5): se corre al abrir, antes y despues de cada tarea, y al cerrar.
echo "nodos en dataset/nodos.jsonl        : $(wc -l < dataset/nodos.jsonl)"
echo "veredictos en bitacora              : $(wc -l < bitacora/VEREDICTOS.jsonl)"
echo "pares mutuos                        : $(wc -l < config/pares_mutuos.jsonl)"
echo "bandeja cuarentena/grove_high_output: $(ls cuarentena/grove_high_output/*.json | wc -l)"
echo "insertados de grove_high_output     : $(ls cuarentena/_insertados/grove_high_output/*.json | wc -l)"
echo "cerrojos en procesos/               : $(ls procesos/ | tr '\n' ' ')"
