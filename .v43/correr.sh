# UNA CORRIDA DE LA ADUANA, CON SU RELOJ Y SU CODIGO ESCRITOS AL LADO.
# El arnes mata una llamada en primer plano a los 10 minutos y estas corridas
# pasan de ahi, asi que se lanzan aqui y se esperan bloqueado hasta leer el
# codigo. Nada avanza mientras tanto.
salida="$1"; shift
inicio=$(date +%s)
date '+%H:%M:%S' > "$salida.reloj"
"$@" > "$salida" 2>&1
codigo=$?
fin=$(date +%s)
date '+%H:%M:%S' >> "$salida.reloj"
printf 'CODIGO=%d\nSEGUNDOS=%d\n' "$codigo" "$((fin-inicio))" >> "$salida.reloj"
