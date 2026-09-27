# -*- coding: utf-8 -*-
"""LA CIFRA 4 DE LA MEDICION DEL 21 SEP, QUE EL EXTRACTOR NO PODIA MEDIR DESDE DENTRO DE SU TURNO.

Las cifras salen de docs/loop/loop.log, que es donde el arnes las escribe, y los
cocientes los calcula este instrumento (D.59): ninguno va tecleado.
"""
import io
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

LINEA = re.compile(r"^\[([\d\- :]+)\] (extractor|auditor ciego|auditor) listo "
                   r"\(USD ([\d.]+)\), (\d+)s")

turnos = []
for l in io.open("docs/loop/loop.log", encoding="utf-8", errors="replace"):
    m = LINEA.match(l.strip())
    if m:
        turnos.append((m.group(1), m.group(2), float(m.group(3)), int(m.group(4))))

extractores = [t for t in turnos if t[1] == "extractor"][-5:]
print("LOS CINCO ULTIMOS TURNOS DE EXTRACTOR, leidos de docs/loop/loop.log")
print("  cerrado              USD        seg")
for t in extractores:
    print("  %-19s %9.4f %6d" % (t[0], t[2], t[3]))
print("")

v57 = [t for t in turnos if t[1] == "extractor"][-1]
v56 = [t for t in turnos if t[1] == "extractor"][-2]
v55 = [t for t in turnos if t[1] == "extractor"][-3]
v54 = [t for t in turnos if t[1] == "extractor"][-4]

print("EL UMBRAL ESCRITO DEL FUNDADOR (21 sep, punto 3): 'el turno baja a la mitad'")
print("  turno de Sonnet MINANDO      (v57) : %9.4f USD en %5d s" % (v57[2], v57[3]))
print("  turno de Opus   MINANDO      (v55) : %9.4f USD en %5d s" % (v55[2], v55[3]))
print("  turno de Opus   MINANDO      (v54) : %9.4f USD en %5d s" % (v54[2], v54[3]))
print("  turno de Sonnet SIN COSECHA  (v56) : %9.4f USD en %5d s" % (v56[2], v56[3]))
print("")
media_opus = (v54[2] + v55[2]) / 2.0
print("  media de los dos turnos de Opus     : %9.4f USD" % media_opus)
print("  LA MITAD, que es lo que el umbral pide: %8.4f USD" % (media_opus / 2.0))
print("")
print("  v57 contra v55 (Sonnet contra Opus, los dos minando) : %.4f veces" % (v57[2] / v55[2]))
print("  v57 contra la media de Opus                          : %.4f veces" % (v57[2] / media_opus))
print("  v57 contra v56 (Sonnet minando contra Sonnet sin cosecha) : %.4f veces" % (v57[2] / v56[2]))
print("")
print("  EL UMBRAL 'BAJA A LA MITAD' SE CUMPLE: %s"
      % ("SI" if v57[2] <= media_opus / 2.0 else "NO"))
print("")
print("NORMALIZADO, LAS TRES MANERAS, Y NINGUNA SE ESCONDE")
print("  USD por candidato escrito   v57 (7 candidatos) : %.4f" % (v57[2] / 7))
print("  USD por candidato escrito   v55 (9 candidatos) : %.4f" % (v55[2] / 9))
print("  USD por palabra de cuerpo   v57 (9277 palabras): %.6f" % (v57[2] / 9277))
print("  USD por palabra de cuerpo   v55 (5502 palabras de cap_09 mas cap_10): %.6f"
      % (v55[2] / 5502))
print("")
print("  objetivo escrito de D.58 en regimen ligero: turno bajo 5 USD")
print("  v57 contra ese objetivo                   : %.2f veces" % (v57[2] / 5.0))
print("  umbral de declaracion de D.56             : 10 USD. v57 lo PASA: %s"
      % ("SI" if v57[2] > 10 else "NO"))
