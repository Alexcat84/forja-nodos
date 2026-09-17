# -*- coding: utf-8 -*-
"""LA TANDA DEL CAPITULO, CON SU ADUANA EN SECO LEIDA DE SU PROPIO FICHERO.

Cada fila se imprime de la salida guardada de `python forja.py informe <candidato>`
que se corrio EN EL MISMO ACTO de escribir ese candidato (EXTRACTOR.md 16). Nada
de esta tabla se teclea: el veredicto, la poblacion y los vecinos se leen del .txt.
"""
import io, json, os, re, sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

ORDEN = eval(io.open(".vm01/orden_tanda.txt", encoding="utf-8").read())
print("AVISO: CADA CELDA SALE DE .vm01/aduana/<fichero>.txt, la salida guardada del informe "
      "de ese candidato. El orden es el del libro y lo pone .vm01/orden_tanda.txt.")
print("")
print("| # | pieza | id | pasos | veredicto en seco | poblacion | vecinos | intentos |")
print("|---:|---|---|---:|---|---:|---:|---:|")
for numero, pieza, identificador, fichero, intentos in ORDEN:
    texto = io.open(os.path.join(".vm01", "aduana", fichero), encoding="utf-8").read()
    datos = json.load(io.open("cuarentena/marquet_turn_the_ship/%s.json" % identificador,
                              encoding="utf-8"))
    veredicto = re.search(r"\[(ENTRARIA|BLOQUEARIA|CAERIA)\]", texto).group(1)
    poblacion = re.search(r"poblacion del barrido\s*:\s*(\d+)", texto).group(1)
    vecinos = re.search(r"vecinos levantados en total\s*:\s*(\d+)", texto)
    print("| %d | `%s` | `%s` | **%d** | **%s** | %s | %s | %d |"
          % (numero, pieza, identificador, len(datos["pasos_accionables"]), veredicto,
             poblacion, vecinos.group(1) if vecinos else "0", intentos))
