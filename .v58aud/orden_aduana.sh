# LA PRUEBA DE QUE LOS SIETE INFORMES SON UNA SOLA CORRIDA POSTERIOR, Y NO SIETE ACTOS
echo "--- 1. poblacion del barrido que cada informe del extractor declara ---"
grep -H "poblacion del barrido" .v57ext/informe_*.txt
echo
echo "--- 2. la bandeja que esa poblacion supone, contada hoy ---"
for d in cuarentena/*/; do n=$(ls "$d"*.json 2>/dev/null | wc -l); echo "$d $n"; done
echo
echo "--- 3. mtime de cada candidato escrito en la vuelta 57 ---"
ls -la --time-style=full-iso cuarentena/grove_high_output/*.json | awk '{print $6, $7, $9}' | sort | tail -7
echo
echo "--- 4. mtime de cada informe guardado ---"
ls -la --time-style=full-iso .v57ext/informe_*.txt | awk '{print $6, $7, $9}' | sort
