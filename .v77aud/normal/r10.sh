# ACTA 76, R10: las salidas pegadas en docs/loop/PROMPT_SIGUIENTE.md, vueltas a correr DESPUES de mi ultima escritura en
# docs/loop/CREDITO_serial.jsonl (DEUDA.jsonl no lo toco), y comparadas con lo pegado, bloque a bloque. Solo lee.
E=docs/loop/PROMPT_SIGUIENTE.md
blk() { awk -v a="$1" 'index($0, a)==1 {p=1; next} p && /^    \$ /{exit} p && !/^    /{exit} p' $E | sed 's/^    //'; }
grep "rc=" .v76ext/barrido.log | sed "s/.*segundos=//" | sort -n | sed -n "1p;\$p" > /tmp/r10a; grep -E "^(INICIO|TODOS)" .v76ext/barrido.log >> /tmp/r10a
diff --strip-trailing-cr /tmp/r10a <(blk '    $ grep "rc=" .v76ext/barrido.log') && echo "reloj del barrido de la 76: IDENTICO al pegado"
python scripts/deuda.py --clase 78 | diff --strip-trailing-cr - <(blk '    $ python scripts/deuda.py --clase 78') && echo "clase 78: IDENTICA a la pegada"
python forja.py tablero --puedo marquet_turn_the_ship | diff --strip-trailing-cr - <(blk '    $ python forja.py tablero --puedo') && echo "tablero --puedo: IDENTICO al pegado"
grep '"id": "d150"' docs/loop/DEUDA.jsonl | grep -o '"que": "[^"]*"' | diff --strip-trailing-cr - <(awk 'index($0, "       $ grep")==1 {p=1; next} p && /^       /{print substr($0,8); next} p{exit}' $E) && echo "texto de d150: IDENTICO al pegado"
ls -l --time-style=full-iso docs/loop/CREDITO_serial.jsonl docs/loop/DEUDA.jsonl docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, substr($7,1,8), $9}'
date "+ahora: %Y-%m-%d %H:%M:%S"
