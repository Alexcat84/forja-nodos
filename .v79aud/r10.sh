# Fase ciega de la 79 (R10, ACTA 77 77.11 y 77.13): lo que de R10 se puede medir hoy sobre el encargo de la 79 sin
# CREDITO_serial.jsonl (el arnes lo retiro en esta fase). (1) La salida de la ACTA 77 77.13, tal como la guardo.
# (2) Mi ultima escritura en DEUDA.jsonl (la linea de d183, que anote al cerrar) contra la hora del encargo, leida de su
# campo 'anotada' y no de la hora del fichero, que despues movio el extractor. (3) El bloque del tablero --puedo del
# encargo, vuelto a correr hoy y comparado (los otros dos bloques miden DEUDA.jsonl, que el extractor escribio despues:
# hoy ya no son comparables). Copia de .v78aud/normal/r10.sh con esos cambios. Solo lee.
E=docs/loop/PROMPT_SIGUIENTE.md
blk() { awk -v a="$1" 'index($0, a)==1 {p=1; next} p && /^    \$ /{exit} p && !/^    /{exit} p' $E | sed 's/^    //'; }
echo "(1) la salida de la ACTA 77 77.13:"; sed 's/^/    /' .v78aud/normal/r10.txt
echo "(2) mi ultima linea en DEUDA.jsonl y la hora del encargo:"
python -c "
import json, io
u = [json.loads(l) for l in io.open('docs/loop/DEUDA.jsonl', encoding='utf-8') if json.loads(l).get('anotada')]
u.sort(key=lambda d: d['anotada'])
print('    ultima deuda anotada: %s %s (vuelta %s)' % (u[-1]['id'], u[-1]['anotada'], u[-1]['vuelta']))
"
ls -l --time-style=full-iso $E | awk '{print "    encargo escrito:", $6, substr($7,1,8)}'
echo "(3) el bloque del tablero, hoy:"
python forja.py tablero --puedo marquet_turn_the_ship | diff --strip-trailing-cr -Z - <(blk '    $ python forja.py tablero --puedo') && echo "    tablero --puedo: IDENTICO al pegado en el encargo"
