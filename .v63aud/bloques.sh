#!/usr/bin/env bash
# Cada bloque: la linea "$ comando" y debajo lo que el comando imprime, sangrado 4.
b() { echo "    \$ $1"; bash -c "$1" 2>&1 | sed 's/\r$//' | sed 's/^/    /'; echo; }
case "$1" in
estado)
b "git rev-parse --short HEAD; git rev-parse --abbrev-ref HEAD"
b "python forja.py gate 2>&1 | tail -3"
b "python forja.py guiones"
b "python forja.py resolutor"
b "tail -1 .v63aud/normal_tests.txt; grep 'total:' .v63aud/normal_tests.txt"
b "wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl"
b "ls cuarentena/grove_high_output/*.json | wc -l; ls cuarentena/_insertados/grove_high_output/"
b "git diff --stat 483ae30 HEAD -- dataset/ bitacora/ censos/ config/pares_mutuos.jsonl | wc -l"
;;
turno)
b "grep -n '2026-09-23 00:1[0-9].*extractor listo' docs/loop/loop.log"
b "python -c \"import json; d=json.load(open('docs/loop/ultimo_extractor.json',encoding='utf-8')); print(d['stop_reason'], d['terminal_reason'], d['num_turns']); print(d['result'])\""
b "cat .v63ext/insertar_01_construir_flujo.txt"
b "grep -c construir_flujo_produccion_paso_limitante dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl"
b "cat .v63aud/cerrojo.txt"
;;
reporte)
b "diff <(python .v63ext/fidelidad.py) .v63ext/fidelidad.txt && echo IDENTICA"
b "for id in \$(awk '{print \$1}' .v63ext/filas_previas_16.txt); do grep -E \"^\$id \" .v63rec/veredictos_de_aduana.txt; done | diff - .v63ext/filas_previas_16.txt && echo IDENTICAS"
b "for id in \$(awk '{print \$1}' .v63ext/filas_previas_16.txt); do git log -1 --format='%cs' 483ae30 -- cuarentena/grove_high_output/\$id.json; done | sort | uniq -c"
b "head -1 .v55ext/informe_de_lote.txt"
b "git show b63405c --stat --format= -- cuarentena/ | tail -1"
b "wc -l fuentes/grove_high_output/cap_02.md fuentes/grove_high_output/cap_03.md"
b "ls cuarentena/marquet_turn_the_ship/*.json | wc -l; ls cuarentena/gerber_emyth/*.json | wc -l"
;;
r5)
b "python .v63aud/pegado63.py"
;;
pasos)
b "python .v63aud/contar_fidelidad.py | tail -4"
b "cat .v63aud/conteo_pasos_normal.txt"
b "git show b63405c -- cuarentena/grove_high_output/equilibrar_capacidad_personal_inventario_plazo.json | grep -c '^-    \"Considera.*y apunta su coste:'"
;;
d005)
b "cat .v63aud/vecinos_d005.txt"
;;
credito)
b "python forja.py credito | sed -n '5,13p'"
b "python scripts/deuda.py --clase 64"
b "python forja.py tablero --puedo grove_high_output"
;;
coste)
b "grep -n '2026-09-23.*listo (USD' docs/loop/loop.log"
;;
esac
case "$1" in
cambio) b "cat .v63aud/cambio_423_462.txt" ;;
pasos_d1) b "git show b63405c -- cuarentena/grove_high_output/equilibrar_capacidad_personal_inventario_plazo.json | grep '^-    \"Considera'" ;;
esac
