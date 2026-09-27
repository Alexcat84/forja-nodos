# ACTA 78, R10: las salidas pegadas en docs/loop/PROMPT_SIGUIENTE.md, vueltas a correr DESPUES de mi ultima escritura en
# docs/loop/CREDITO_serial.jsonl (en DEUDA.jsonl no escribo) y comparadas con lo pegado, bloque a bloque. Copia de .v78aud/normal/r10.sh
# con los bloques del encargo de la 80. El -Z es porque el generador quita el espacio del final de linea. Solo lee.
E=docs/loop/PROMPT_SIGUIENTE.md
blk() { awk -v a="$1" 'index($0, a)==1 {p=1; next} p && /^    \$ /{exit} p && !/^    /{exit} p' $E | sed 's/^    //'; }
python scripts/deuda.py --clase 80 | diff --strip-trailing-cr -Z - <(blk '    $ python scripts/deuda.py --clase 80') && echo "clase 80: IDENTICA a la pegada"
python forja.py tablero --puedo marquet_turn_the_ship | diff --strip-trailing-cr -Z - <(blk '    $ python forja.py tablero --puedo') && echo "tablero --puedo: IDENTICO al pegado"
{ tail -1 .v77ext/relojes.txt; tail -1 .v75ext/relojes.txt; } | diff --strip-trailing-cr -Z - <(blk '    $ tail -1 .v77ext/relojes.txt') && echo "relojes: IDENTICOS a los pegados"
sed -n '2,21p' .v78ext/orden.txt | cut -c1-80 | sed 's/[[:space:]]*$//' | diff --strip-trailing-cr -Z - <(blk "    \$ sed -n '2,21p'") && echo "orden: IDENTICO al pegado"
{ sed -n '/^ARISTAS ESPERADAS/,$p' .v78ext/orden.txt; grep -v '^#' .v78ext/veredictos_listos.txt | grep -c '|'; } | diff --strip-trailing-cr -Z - <(blk "    \$ sed -n '/^ARISTAS") && echo "aristas esperadas y lineas: IDENTICAS a las pegadas"
ls -l --time-style=full-iso docs/loop/CREDITO_serial.jsonl docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, substr($7,1,8), $9}'
date "+ahora: %Y-%m-%d %H:%M:%S"
