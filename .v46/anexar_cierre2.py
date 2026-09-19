# -*- coding: utf-8 -*-
"""Anexa el pie del cierre: instrumentos corridos, colision de guardas y ejemplar de doctrina."""
import io

TXT = u"""
### HH.5.h. **LOS INSTRUMENTOS DEL CIERRE, CORRIDOS Y PEGADOS**

<!-- TALLADO: parcial salida=.v46/cerrar_reporte.txt -->

    $ python scripts/cerrar_reporte.py
    [cierre] tallado del reporte (D.41)
    [cierre] censo de rutas (D.42)
    [cierre] tabla de cierre de tareas (D.52)
    [cierre] gate de integridad
    [cierre] barrido de guiones
    [cierre] prueba de aceptacion
    [cierre] vigencia de los veredictos (D.15): COLA DE TRABAJO, no guarda

    CIERRE VERDE: las cuatro guardas que muerden, el tallado y el censo.

**LA VIGENCIA SACO `7` RANCIOS Y NINGUNO ES MIO:** los `7` son veredictos de `2026-09-18` sobre
`pedir_critica_primero_crear_seguridad_psicologica` y `dar_elogio_disciplina_igual_critica`, que
son de `scott_radical_candor` y no de `grove_high_output`. **No los cito como vigentes y no los
toco**, que es lo que `D.15` manda: son **cola, no guarda**.

<!-- TALLADO: parcial salida=.v46/tablero.txt -->

    $ python forja.py tablero --escribir
      MUNDO 11: faltan 3 de 3 libros del corte (grove_high_output, gerber_emyth, marquet_turn_the_ship)
      COLA DE DOCTRINA (D.56): 11 pregunta(s), 0 bloquea(n)
    ESCRITO: 22 fila(s) en docs/loop/TABLERO.jsonl

<!-- TALLADO: parcial salida=.v46/credito_cierre.txt -->

    $ python forja.py credito
      AUDITOR            1 de 3     ACTA 44
      CIFRA PUBLICADA    0 de 2     ACTA 44
      CLASE              0 de 2     ACTA 44
      DATO MOVIDO        0 de 2     ACTA 44
      REPORTE            1 de 3     ACTA 44
      CREDITO ENTERO: ninguna especie en su tope.

**EL CREDITO LO LEO Y NO ANOTO MI PROPIA VUELTA**, que es lo que el encargo dice y lo que
`EXTRACTOR.md` 14 manda: **esa sede no es mia.**

<!-- TALLADO: parcial salida=.v46/deuda_cierre.txt -->

    $ python scripts/deuda.py
      pendientes: 9    pagadas: 8

**`11` menos las `2` que pague en `HH.1` da `9`**, y las `9` que quedan **no las toco**: se pagan
juntas en la vuelta de saneamiento que toque (`D.55`).

### HH.5.i. **LA COLISION DE `D.52` CON `D.41`, QUE ME MORDIO EN ESTE MISMO CIERRE**

**`scripts/tabla_de_cierre.py --escribir` escribe SIEMPRE en `docs/loop/TABLA_DE_CIERRE.txt`, y
el tallado de `D.41` compara toda tabla del reporte contra el fichero que esa tabla nombra.
Conclusion medida: dos vueltas no pueden estar verdes a la vez.** Al escribir mi tabla deje en
rojo la de la vuelta 42, **sin que nadie tocara ni una celda de su reporte**.

**COMO LO REPARE, sin teclear y sin borrar:** saque la salida de la vuelta 42 **de git, byte a
byte**, y la archive; su linea pasa a nombrar la copia archivada con su correccion declarada al
lado; y **la ruta viva se queda con la tabla de la vuelta que cierra**, que es lo que `D.52`
manda.

<!-- TALLADO: parcial salida=.v46/sello_v42.txt -->

    $ git show HEAD:docs/loop/TABLA_DE_CIERRE.txt | git hash-object --stdin
    c33bec53d8efe6d470fe377e6c4c65bebd5ee7dd
    $ git hash-object docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_v42.txt
    c33bec53d8efe6d470fe377e6c4c65bebd5ee7dd

**EL MISMO `hash-object` ANTES Y DESPUES: la copia es la salida, no una transcripcion.**

**LO QUE PROPONGO Y NO ADJUDICO** (`EXTRACTOR.md` 14, y la moratoria de 13 me deja fuera de
`scripts/`): que la salida de `D.52` lleve la vuelta en su nombre, como ya hacen los informes por
candidato. **Es hermana de `d022`**, que dice que ese mismo instrumento localiza su tabla por un
sitio fragil. **No la anoto yo en la deuda: la sede de esa anotacion es el acta.**

### HH.5.j. **UN SEGUNDO EJEMPLAR MEDIDO DE LA PREGUNTA `1` DE LA COLA DE DOCTRINA, Y NO ABRO NINGUNA NUEVA**

La cola esta congelada en `11` y la pregunta `1` dice, con las palabras del tablero:
*`EXTRACTOR.md` 11 y la banda de `0,4`: dice que por encima hay gemelos y cero ajenos.*

**MI TANDA LE PONE SU EJEMPLAR SIN BUSCARLO:** el unico par por encima de `0,4` de esta vuelta
(`0,437`) **no es un gemelo y tampoco es un ajeno: es una jerarquia `D.37` declarada**. **La banda
no falla** (un par de jerarquia no es un ajeno), pero **el ejemplar ensena que por encima de
`0,4` un lector que solo tenga la banda leeria REPITE donde la lectura da CONTINUA.** Lo registro
con su medida **y lo dejo ahi**, que es lo que el encargo manda hacer con la doctrina.

---

**LA VUELTA 46 CIERRA CON SUS CINCO FILAS CERRADAS, CERO INSERCIONES POR PUERTA MEDIDA, `8`
CANDIDATOS NUEVOS EN LA BANDEJA DE `grove_high_output` Y `0` PUENTE DE `50` PASOS.**
"""

with io.open("docs/loop/REPORTE.md", "a", encoding="utf-8", newline="\n") as f:
    f.write(TXT)
print("anexado")
