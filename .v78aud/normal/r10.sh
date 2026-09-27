# ACTA 77, R10: las salidas pegadas en docs/loop/PROMPT_SIGUIENTE.md, vueltas a correr DESPUES de mi ultima escritura en
# docs/loop/CREDITO_serial.jsonl y docs/loop/DEUDA.jsonl, y comparadas con lo pegado, bloque a bloque. Copia de .v77aud/normal/r10.sh
# con los tres bloques del encargo de la 79. El -Z es porque el generador del encargo quita el espacio del final de linea. Solo lee.
E=docs/loop/PROMPT_SIGUIENTE.md
blk() { awk -v a="$1" 'index($0, a)==1 {p=1; next} p && /^    \$ /{exit} p && !/^    /{exit} p' $E | sed 's/^    //'; }
python scripts/deuda.py --clase 79 | diff --strip-trailing-cr -Z - <(blk '    $ python scripts/deuda.py --clase 79') && echo "clase 79: IDENTICA a la pegada"
python forja.py tablero --puedo marquet_turn_the_ship | diff --strip-trailing-cr -Z - <(blk '    $ python forja.py tablero --puedo') && echo "tablero --puedo: IDENTICO al pegado"
python scripts/deuda.py | grep -E "^  (d098|d099|d104|d135|d150|d180|d183) " | diff --strip-trailing-cr -Z - <(blk '    $ python scripts/deuda.py | grep') && echo "las siete deudas: IDENTICAS a las pegadas"
ls -l --time-style=full-iso docs/loop/CREDITO_serial.jsonl docs/loop/DEUDA.jsonl docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, substr($7,1,8), $9}'
date "+ahora: %Y-%m-%d %H:%M:%S"
