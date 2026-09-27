#!/bin/sh
# HEREDADO 3 punto 4: cada encargo de la ACTA 25 (11.1) buscado con grep en
# docs/loop/PROMPT_SIGUIENTE.md. Es la comprobacion que la propia ACTA 25 dice
# que "ya fallo una vez sin que nadie la viera".
P=docs/loop/PROMPT_SIGUIENTE.md
buscar() {
  n=$(grep -c -i -- "$2" "$P")
  if [ "$n" -gt 0 ]; then e="ESTA   "; else e="NO ESTA"; fi
  printf '%-3s %s  grep -c -i "%s" -> %s\n' "$1" "$e" "$2" "$n"
}
echo "fichero: $P   ($(wc -l < $P) lineas)"
echo
buscar 1 "tallado"
buscar 2 "despedir_persona_franqueza_radical"
buscar 2b "reconocer_recompensar_gente_estable"
buscar 3 "resumen_teorico"
buscar 4 "cambiar_forma_trabajar_conservar_plantilla"
buscar 5 "cap_04"
buscar 6 "QUESTIONS TO CONSIDER"
buscar 7 "recorrer_rueda"
buscar 8 "decidir_momento_despedir_persona"
