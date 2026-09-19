# -*- coding: utf-8 -*-
"""d036 PAGADA: LAS OCHO CIFRAS DE FRONTERA, CORREGIDAS POR CORRECCION DECLARADA Y SIN BORRAR.

Manual principio 6: la correccion se escribe AL LADO del texto viejo y no lo borra. Aqui la
correccion se ANEXA al final del resumen_teorico de cada ficha, con la cifra vieja dentro de
la propia frase para que quien lea la correccion no tenga que ir a buscarla, y con el renglon
del instrumento pegado, que es lo que la sostiene (.v50/palabras_d036.txt).

NO INVENTA UNA TERCERA CIFRA: la buena es la que la frontera de HH.2.c publica, y
.v50/palabras_d036.py comprobo antes que mi recuento la reproduce en las ocho.

CERO PASADAS DE ADUANA POR ADJUDICACION DEL AUDITOR (encargo de la vuelta 50, TAREA 3.c).
"""
import io
import json
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

# LAS TRES COLUMNAS SE LEEN DEL FICHERO DEL INSTRUMENTO, NO SE TECLEAN AQUI.
FILAS = []
for l in io.open(".v50/palabras_d036.txt", encoding="utf-8"):
    m = re.match(r"(\S+)\s+(P\d+)\s+L(\d+) a L(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+la frontera manda", l)
    if m:
        FILAS.append((m.group(1), m.group(2), int(m.group(3)), int(m.group(4)),
                      int(m.group(5)), int(m.group(6)), int(m.group(7))))

if len(FILAS) != 8:
    raise SystemExit("PARADA: el instrumento no da las ocho filas en verde, da %d" % len(FILAS))

PLANTILLA = (
 " CORRECCION DECLARADA DE LA VUELTA 50, SIN BORRAR EL NUMERO VIEJO (manual principio 6, deuda d036, "
 "adjudicada en ACTA 48 seccion 48.5.a): donde esta ficha dice mas arriba que la PIEZA {pieza}, "
 "L{desde} a L{hasta}, tiene {dice} palabras, TIENE QUE LEERSE {bueno} palabras. La cifra buena es la "
 "que la frontera de HH.2.c publica para esta pieza, y no una tercera cifra mia: la recompute en la "
 "vuelta 50 con el mismo recuento de .v46/frontera.py linea 136 y me da {cuento}, identica a la de la "
 "frontera. EL RENGLON DEL INSTRUMENTO QUE LO SOSTIENE, pegado (.v50/palabras_d036.txt): "
 "{fid} {pieza} L{desde} a L{hasta} dice {dice} HH.2.c {bueno} cuento {cuento} la frontera manda. "
 "LO QUE ESTA CORRECCION NO TOCA: ni un paso, ni una atribucion, ni la frontera, que es precisamente "
 "la que sale bien. El numero viejo era un numero escrito a mano en la vuelta 46 que ni la frontera "
 "citada ni ningun recuento reproducen."
)

for fid, pieza, desde, hasta, dice, bueno, cuento in FILAS:
    ruta = "cuarentena/grove_high_output/%s.json" % fid
    ficha = json.load(io.open(ruta, encoding="utf-8"))
    if "deuda d036" in ficha["resumen_teorico"]:
        print("YA CORREGIDA, no la toco: %s" % fid)
        continue
    ficha["resumen_teorico"] = ficha["resumen_teorico"] + PLANTILLA.format(
        pieza=pieza, desde=desde, hasta=hasta, dice=dice, bueno=bueno,
        cuento=cuento, fid=fid)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(ficha, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("corregida %-46s %s  %d pasa a leerse %d" % (fid, pieza, dice, bueno))

print("")
print("fichas corregidas por correccion declarada: %d" % len(FILAS))
