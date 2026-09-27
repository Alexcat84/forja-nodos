# -*- coding: utf-8 -*-
"""Anexa el desglose de en que se fue el turno, que es la mitad medible de la cifra de D.55."""
import io

R = "docs/loop/REPORTE.md"
t = io.open(R, encoding="utf-8").read()

CIERRE = (u"---\n"
          u"\n"
          u"**LA VUELTA 46 CIERRA CON SUS CINCO FILAS CERRADAS, CERO INSERCIONES POR PUERTA "
          u"MEDIDA, `8`\nCANDIDATOS NUEVOS EN LA BANDEJA DE `grove_high_output` Y `0` PUENTE "
          u"DE `50` PASOS.**\n")

NUEVO = (u"### HH.5.k. **EN QUE SE FUE EL TURNO, QUE ES LA MITAD DE LA CIFRA QUE SI PUEDO MEDIR**\n"
         u"\n"
         u"**LA CIFRA EN USD NO LA PUEDO DAR, Y LO DIGO EN VEZ DE ADIVINARLA** (`EXTRACTOR.md` 7:\n"
         u"*lo que no este escrito y no puedas medir, lo traes como pregunta*). **Este repo no "
         u"tiene\ninstrumento que mida el coste de un turno**: `USD` aparece en cuatro ficheros "
         u"de `docs/loop/`\ny en ninguno de `scripts/` ni de `src/`. **Lo que la regla persigue "
         u"si lo puedo entregar**,\nporque *no prohibe gastar: obliga a decir en que*:\n"
         u"\n"
         u"| en que | medida | de donde sale |\n"
         u"|---|---:|---|\n"
         u"| **la aduana en seco, `8` corridas** | **`4.044` s** | `.v46/reloj_c01.txt` a "
         u"`.v46/reloj_c08.txt`, sumados por `.v46/tanda.py` |\n"
         u"| la prueba de aceptacion, `2` corridas | `232` s | `.v46/apertura_pruebas.txt` "
         u"(`115,997` s) mas la del cierre |\n"
         u"| el resto: leer el capitulo, escribir las `8` fichas y la frontera, y el reporte | "
         u"lo que quede | sin instrumento propio, y por eso no le pongo cifra |\n"
         u"\n"
         u"**EL `86` POR CIENTO DEL TIEMPO CRONOMETRADO DE ESTE TURNO SE FUE EN LA ADUANA EN "
         u"SECO**\n(`4.044` de `4.276` s), y esa es la frase util para quien decida despues: "
         u"**el gasto de esta\nvuelta no esta en escribir nodos, esta en medirlos.**\n"
         u"\n" + CIERRE)

assert CIERRE in t
io.open(R, "w", encoding="utf-8", newline="\n").write(t.replace(CIERRE, NUEVO))
print("desglose anexado")
