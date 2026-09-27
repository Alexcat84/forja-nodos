#!/bin/sh
# Ficheros de cuarentena/dataset/bitacora MODIFICADOS (no nacidos) en esta vuelta.
git log --diff-filter=M --name-only --format='' 327d969..HEAD -- cuarentena/ dataset/ bitacora/ config/ censos/ | sort -u
echo "--- conteo de lineas de las sedes de dato, hoy ---"
wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
