# HEREDADO 3 punto 4 de la ACTA 25, aplicado a mi: cada punto encargado se busca
# CON UN COMANDO en el encargo de hoy, no con la memoria.
for t in "version" "ancla" "operacion escrita" "puente" "cap_04" "QUESTIONS TO CONSIDER" "correccion 9" "cola de"; do
  printf "%-26s -> %s coincidencia(s)\n" "$t" "$(grep -c -i "$t" docs/loop/PROMPT_SIGUIENTE.md)"
done
