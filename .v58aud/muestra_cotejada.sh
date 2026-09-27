# D.58: QUIEN AUDITA VUELVE A CORRER EL INSTRUMENTO CON LA MISMA SEMILLA
python scripts/muestra_fidelidad.py --libro grove_high_output --capitulos cap_11,cap_12,cap_13 --semilla v57 > .v58aud/muestra_v57.txt 2>&1
echo "--- diff contra el fichero que el reporte cita como su salida (.v57ext/muestra.txt) ---"
diff .v58aud/muestra_v57.txt .v57ext/muestra.txt && echo "IDENTICO, linea a linea"
echo
echo "--- diff contra el BLOQUE QUE EL REPORTE PEGA en XX.4 ---"
echo "(el reporte pega una version RESUMIDA: mira las lineas de abajo)"
sed -n '/--- cap_11: 15 paso/,/cap_13: ENTERO/p' .v58aud/muestra_v57.txt | head -4
