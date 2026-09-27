
---

# TAREA 1. EL REMEDIO DE `M6.9.a`: LA FRONTERA SE PEGA ENTERA, FILA POR PIEZA

**La caida que corrijo (`M6.3`, `M6.8.a`):** la `ACTA M6` encontro que las cuatro tablas de frontera de la
vuelta `5` no eran las brutas de `.v5m/frontera/`, sino un resumen agrupado tecleado encima, marcado
`TALLADO: parcial`, con `12` cifras de palabras que no eran la suma de sus piezas y ninguna columna que
sumara el cuerpo que su propia fila final declaraba. La marca `parcial` es legitima por si sola
(`scripts/tallar_reporte.py` linea `461` la despacha como `CITA` sin reproducirla), y por eso la maquina no
la caza: **la caida era del contenido, no de la marca.**

**EL REMEDIO, TAL COMO LO ESCRIBE `D.41` Y LO ORDENA `M6.9.a`, aplicado en las dos frontera de esta vuelta**
(seccion `2.a` y `2.b` de la `TAREA 2`):

1. **Cada tabla de frontera se genera con un instrumento propio de esta vuelta**
   (`.v6m/frontera/generar_frontera.py`), que cuenta lineas y palabras del fichero fuente, **nunca a mano**.
   Su salida se guarda en `.v6m/frontera/cap_16_bruta.txt` y `.v6m/frontera/cap_17_bruta.txt`.
2. **La tabla se pega en este reporte tal como el fichero la escribe**, pieza por pieza (`R1`, `R2`, ...,
   sin agrupar rangos), bajo `<!-- TALLADO: salida=.v6m/frontera/cap_NN_bruta.txt -->` **sin la palabra
   `parcial`**, para que `scripts/tallar_reporte.py` la reproduzca celda a celda en vez de citarla.
3. **Ningun resumen agrupado va en el sitio de la tabla.** Si hace falta una lectura de conjunto, va aparte
   y marcada `LECTURA` (asi se hace en `2.a` y `2.b`, despues de la tabla, no en su lugar).
4. **La frase *coincide al digito* solo se escribe debajo de una tabla que el tallado haya reproducido**, y
   aqui se escribe con `scripts/cerrar_reporte.py` corrido al cierre (`C.1`) como la comprobacion que lo
   sostiene, no como promesa.

**No es doctrina nueva:** `D.41` ya existia: *la tabla que dice ser de instrumento se anexa, no se teclea*.
Lo que esta vuelta cambia es la ejecucion, no la regla (moratoria de maquinaria, `EXTRACTOR.md` `13`).
