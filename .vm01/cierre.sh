#!/bin/sh
# LAS CIFRAS DEL CIERRE, MEDIDAS AL CIERRE (EXTRACTOR.md 4). Cero celdas tecleadas.
echo '$ wc -l < dataset/nodos.jsonl'
wc -l < dataset/nodos.jsonl
echo '$ ls cuarentena/marquet_turn_the_ship/*.json | wc -l'
ls cuarentena/marquet_turn_the_ship/*.json | wc -l
echo '$ git rev-parse --abbrev-ref HEAD'
git rev-parse --abbrev-ref HEAD
echo '$ git rev-parse --short HEAD'
git rev-parse --short HEAD
echo '$ grep -c "" docs/loop/REPORTE.md   (lineas del reporte al cerrar)'
grep -c "" docs/loop/REPORTE.md
echo '$ ls .vm01/aduana/*.txt | wc -l   (informes de aduana guardados en esta vuelta)'
ls .vm01/aduana/*.txt | wc -l
echo '$ grep -lc "INFORME DE LA ADUANA" .vm01/aduana/*.txt | wc -l   (los que traen salida de verdad)'
grep -l "INFORME DE LA ADUANA" .vm01/aduana/*.txt | wc -l
echo '$ grep -c "" .vm01/informe_lote.txt   (lineas del informe del lote entero)'
grep -c "" .vm01/informe_lote.txt
