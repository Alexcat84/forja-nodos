# ACTA 79: R10 sobre PARA_ALEXIS.md. Vuelve a correr sus ordenes con el mismo generador y compara con lo escrito, y da las horas de
# la ultima anotacion del credito, de PARA_ALEXIS.md y de ahora.
N=.v80aud/normal
python $N/generar.py $N/para_alexis_plantilla.md $N/para_alexis_r10.md > /dev/null
diff docs/loop/PARA_ALEXIS.md $N/para_alexis_r10.md > /dev/null && echo "PARA_ALEXIS.md: IDENTICO al volver a correr sus ordenes" || echo "PARA_ALEXIS.md: DISTINTO"
ls -l --time-style=+"%Y-%m-%d %H:%M:%S" docs/loop/CREDITO_serial.jsonl docs/loop/PARA_ALEXIS.md docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, $7, $5, $8}'
echo "ahora: $(date '+%Y-%m-%d %H:%M:%S')"
