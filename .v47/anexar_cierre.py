# -*- coding: utf-8 -*-
"""ANEXA LA SECCION II.4 AL REPORTE, con la tabla de cierre y el coste puestos en su sitio."""
import io

SCRATCH = ("C:/Users/AlexDesk/AppData/Local/Temp/claude/"
           "C--Users-AlexDesk-Documents-forja-nodos/"
           "b3c93959-cc33-4ce3-bcb2-dd8f08d97fa7/scratchpad/ii4.md")

TABLA = u"""| # | tarea | como cerro |
|---:|---|---|
| 1 | los registros de la `ACTA 45`: el `116`, las tres deudas nuevas y `d024` | **CERRADA**: la correccion del `116` escrita al lado del texto viejo con el instrumento de hoy (`115`), las tres deudas nombradas con su motivo de no pago, y `d024` dicha y no abierta |
| 2 | `cap_04` abierto: los ocho siguientes, cada uno por su aduana, cero inserciones | **CERRADA CORTA EN `6` candidatos de los `8` encargados**: `0` `CAERIA`, `9` pares de cola leidos par a par, la arista de `P27` escrita en las dos fichas, **cero inserciones**, y el corte declarado con su reloj |
| 3 | `PASOS INVENTADOS` de `cap_04` con su denominador y la fila de la vuelta 46 | **CERRADA**: `0` PUENTE de `45` pasos hoy, `0` de `50` en la vuelta 46, `0` de `95` en el capitulo, y los cinco sitios de tentacion nombrados |
| 4 | el cierre, con sus guardas, su tabla `D.52`, su estado y su coste | **CERRADA**: las cinco guardas en verde, la colision de `D.52` sellada por `hash-object`, el estado recomputado y el coste del turno contado de sus relojes |"""

texto = io.open(SCRATCH, encoding="utf-8").read()
coste = io.open(".v47/coste.txt", encoding="utf-8").read().split("\n")
# La tabla del coste es lo que va hasta la linea en blanco que sigue al total.
tabla_coste = []
for linea in coste:
    if linea.strip() == "" and tabla_coste:
        break
    tabla_coste.append(linea)
resto = [l for l in coste[len(tabla_coste):] if l.strip()]

texto = texto.replace(u"TABLA_AQUI", TABLA)
texto = texto.replace(u"COSTE_AQUI",
                      u"\n".join(tabla_coste) + u"\n\n    " + u"\n    ".join(resto))
texto = texto.replace(u"CIERRE_AQUI", u"CIERRE_PENDIENTE")

io.open("docs/loop/REPORTE.md", "a", encoding="utf-8", newline="\n").write(texto)
print("anexado")
