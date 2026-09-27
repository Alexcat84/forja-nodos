# -*- coding: utf-8 -*-
"""TAREA 1.B de la vuelta 39: las dos cifras del candidato 1, arregladas EN BANDEJA.

Por anexion y sin borrar el texto viejo, que es como corrige esta casa. El
candidato todavia no ha entrado, asi que esto se hace antes de que su
`resumen_teorico` sea CIFRA PUBLICADA en sede duradera.
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA = os.path.join(RAIZ, "cuarentena", "scott_radical_candor",
                    "pedir_critica_primero_crear_seguridad_psicologica.json")

ANEXO = (
    " CORRECCION DECLARADA 18 sep 2026, vuelta 39, TAREA 1.B del encargo, hecha EN BANDEJA"
    " y antes de la primera insercion, sobre DOS cifras de este mismo campo que no se"
    " sostienen contra su instrumento. LA PRIMERA: la correccion del paso 15 dice 36"
    " apariciones en dataset/nodos.jsonl contra 1 de ceo, y SON 39 CONTRA 0."
    " grep -o -i 'consejero delegado' dataset/nodos.jsonl | wc -l da 39, y"
    " grep -o -iE '\bceo\b' dataset/nodos.jsonl | wc -l da 0, corridos hoy sobre los 321"
    " nodos del arbol e3950c6. LA GRAFIA QUE ESA CIFRA SOSTIENE NO CAMBIA: consejero"
    " delegado sigue siendo la de la casa y el paso 15 no se toca; lo que estaba mal era"
    " el numero citado para justificarla, y hoy lo sostiene con mas holgura que entonces."
    " LA SEGUNDA: la frase 17 pasos, 17 TRANSCRIPCION, 0 PUENTE es de ANTES de la"
    " relectura, y se lee como si fuera el resultado de ella. Dice lo contrario que las"
    " frases que van debajo, que cuentan DOS defectos. Lo que hubo fue esto, en orden:"
    " la relectura de la vuelta 38 encontro DOS PUENTE, en los pasos 6 y 15, y los dos se"
    " reescribieron contra sus lineas; la cuenta 17 de 17 vale para el nodo YA CORREGIDO y"
    " no para el que se releyo. LA RELECTURA D.30 DE LA VUELTA 39, corrida hoy y entera"
    " otra vez antes de insertar, da 17 pasos, 17 TRANSCRIPCION, 0 PUENTE, con los 17 de"
    " la clase que el encargo manda releer entera (persona, cuenta, escalon o adjetivo de"
    " sentimiento): los 17 de este candidato caen en ella y los 17 se releyeron contra su"
    " linea completa. Y SE AFINA UNA CITA que estaba corta: el paso 17 sale de la linea"
    " 113 Y de la 237, no solo de la 113. La 113 escribe each of the four tips for"
    " soliciting criticism, que es de donde sale la cuenta, y la 237 es la que NOMBRA los"
    " cuatro uno a uno, coming up with a go-to question, embracing the discomfort,"
    " listening with the intent to understand, and making listening tangible by rewarding"
    " the candor, que es de donde salen los cuatro nombres del paso. El paso no cambia:"
    " cambia su cita, que estaba incompleta."
)

with io.open(RUTA, encoding="utf-8") as f:
    d = json.load(f)

if "vuelta 39, TAREA 1.B" in d["resumen_teorico"]:
    raise SystemExit("YA ESTABA ANEXADO: no toco nada.")
antes = len(d["resumen_teorico"])
d["resumen_teorico"] = d["resumen_teorico"] + ANEXO
with io.open(RUTA, "w", encoding="utf-8", newline="\n") as f:
    json.dump(d, f, ensure_ascii=False, indent=2, sort_keys=True)
    f.write(u"\n")
print("resumen_teorico: %d caracteres antes, %d despues, %d aniadidos, 0 borrados"
      % (antes, len(d["resumen_teorico"]), len(d["resumen_teorico"]) - antes))
