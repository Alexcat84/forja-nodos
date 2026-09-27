#!/bin/bash
# Censo de la vuelta 76 (COPIA de .v75ext/censo.sh con las dos rutas de Gerber, encargo TAREA 5, y el ls de insertados con 2>/dev/null,
# porque cuarentena/_insertados/gerber_emyth/ no existe mientras no entre ninguna): se corre al abrir y al cerrar.
echo "nodos en dataset/nodos.jsonl        : $(wc -l < dataset/nodos.jsonl)"
echo "veredictos en bitacora              : $(wc -l < bitacora/VEREDICTOS.jsonl)"
echo "pares mutuos                        : $(wc -l < config/pares_mutuos.jsonl)"
echo "bandeja cuarentena/gerber_emyth     : $(ls cuarentena/gerber_emyth/*.json | wc -l)"
echo "insertados de gerber_emyth          : $(ls cuarentena/_insertados/gerber_emyth/*.json 2>/dev/null | wc -l)"
echo "cerrojos en procesos/               : $(ls procesos/ | tr '\n' ' ')"
