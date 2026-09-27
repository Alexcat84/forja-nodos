# Fase ciega de la 80 (R10, ACTA 78 78.11 y 78.13): lo que de R10 se puede medir hoy sobre el encargo de la 80 sin
# CREDITO_serial.jsonl (el arnes lo retiro en esta fase). (1) La salida de la ACTA 78 78.13, tal como la guardo, y las
# horas del fichero de credito (de la lista del arnes no: la leo del fichero guardado), del encargo y de esa salida.
# (2) Los tres bloques del encargo que miden ficheros que nadie escribio despues (los relojes, el orden y las aristas
# esperadas con sus lineas), vueltos a correr hoy y comparados. Los otros dos (la clase 80 y el tablero --puedo) miden
# DEUDA.jsonl y el tablero, que la vuelta 80 movio al pagar y al insertar: hoy ya no son comparables, y se dice.
# Copia de .v79aud/normal/r10.sh con esos cambios. Solo lee.
E=docs/loop/PROMPT_SIGUIENTE.md
blk() { awk -v a="$1" 'index($0, a)==1 {p=1; next} p && /^    \$ /{exit} p && !/^    /{exit} p' $E | sed 's/^    //'; }
echo "(1) la salida de la ACTA 78 78.13, guardada:"; sed 's/^/    /' .v79aud/normal/r10.txt
ls -l --time-style=full-iso $E .v79aud/normal/r10.txt | awk '{print "    " $6, substr($7,1,8), $9}'
echo "(2) los bloques comparables, hoy:"
{ tail -1 .v77ext/relojes.txt; tail -1 .v75ext/relojes.txt; } | diff --strip-trailing-cr -Z - <(blk '    $ tail -1 .v77ext/relojes.txt') && echo "    relojes: IDENTICOS a los pegados"
sed -n '2,21p' .v78ext/orden.txt | cut -c1-80 | sed 's/[[:space:]]*$//' | diff --strip-trailing-cr -Z - <(blk "    \$ sed -n '2,21p'") && echo "    orden: IDENTICO al pegado"
{ sed -n '/^ARISTAS ESPERADAS/,$p' .v78ext/orden.txt; grep -v '^#' .v78ext/veredictos_listos.txt | grep -c '|'; } | diff --strip-trailing-cr -Z - <(blk "    \$ sed -n '/^ARISTAS") && echo "    aristas esperadas y lineas: IDENTICAS a las pegadas"
