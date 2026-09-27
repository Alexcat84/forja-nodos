#!/bin/sh
# anclas.sh: fija con grep -n, SOBRE EL FICHERO CRUDO, la primera y la ultima linea
# de cada bloque que el auditor adjudica a un candidato.
# PRIMERA LINEA OBLIGADA (REMEDIO 4 de la ACTA 30): SI lleva constantes tecleadas.
# Son las frases ancla, y las teclea el auditor porque las ha leido; el dato no las
# puede casar solo (el candidato esta en castellano y el libro en ingles, y por eso
# casar.py deja cuatro candidatos SIN CASAR). Lo que NO teclea es ningun numero de
# linea: los pone grep.
F=fuentes/gerber_emyth
g() { printf '%-46s ' "$2"; grep -n "$3" "$F/$1.md" | head -1 | cut -d: -f1; }
g cap_04 "cap_04 abre  hacer_trabajo_futuro"      "An Entrepreneur does the work of envisioning"
g cap_04 "cap_04 cierra hacer_trabajo_futuro"     "I call it Future Work"
g cap_07 "cap_07 abre  dictar_ritmo"              "dictate your business"
g cap_07 "cap_07 cierra dictar_ritmo"             "any plan is better than no plan"
g cap_08 "cap_08 abre  construir_empresa"         "Tom Watson, the founder of IBM"
g cap_08 "cap_08 cierra construir_empresa"        "we built one"
g cap_08 "cap_08 abre  trazar_modelo"             "fulfills the perceived needs of a specific segment"
g cap_08 "cap_08 cierra trazar_modelo"            "no business can succeed"
g cap_11 "cap_11 abre  fingir_prototipo"          "for 5,000 more just like it"
g cap_11 "cap_11 cierra fingir_prototipo"         "each of these rules in turn"
g cap_11 "cap_11 abre  dar_valor"                 "^What is value"
g cap_11 "cap_11 cierra dar_valor"                "simple word of thanks to your banker"
g cap_11 "cap_11 abre  operar_modelo"             "^Yes, I said lowest possible level of skill"
g cap_11 "cap_11 cierra operar_modelo"            "necessary correlate"
g cap_11 "cap_11 abre  documentar_trabajo"        "^Documentation says"
g cap_11 "cap_11 cierra documentar_trabajo"       "would not be a model without one"
g cap_11 "cap_11 abre  unificar_color"            "Marketing studies tell us"
g cap_11 "cap_11 cierra unificar_color"           "as carefully as any box of cereal"
g cap_11 "cap_11 abre  interrogar_negocio"        "Go to work on your business rather than in it"
g cap_11 "cap_11 cierra interrogar_negocio"       "you do not know the answers\|know the answers"
g cap_11 "cap_11 regla 3, enunciada en la lista"          "place of impeccable order"
g cap_11 "cap_11 regla 5, enunciada en la lista"          "uniformly predictable service"
g cap_11 "cap_11 regla 1, primera declarativa"  "^Value can be a word said at the door"
g cap_11 "cap_11 regla 1, ultima declarativa"   "^Value can be a simple word of thanks"
g cap_11 "cap_11 regla 4, su encabezado"        "^4. All Work in the Model"
g cap_10 "cap_10 las preguntas que NO son el nodo" "How do you build yours"
