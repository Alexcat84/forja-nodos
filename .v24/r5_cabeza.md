
---

## R.5. TAREA 4: **`cap_14` ENTERO**, la ultima unidad sin minar del lote 4. CERRADA

### R.5.a. EL ROTULO Y EL VOLUMEN, **REMEDIDOS POR MI** (`EXTRACTOR.md` 5)

*El auditor me da el rotulo y la cuenta ya medidos, y ademas registra que su encargo anterior los
tenia mal. **Los remido igual: una cifra de mi encargo no es fuente de una cifra mia.***

Salida de los tres comandos, guardada en `.v24/rotulo_cap14.txt`:

    $ sed -n "1,7p" fuentes/scott_radical_candor/cap_14.md
    ---
    libro: Scott, Radical Candor
    edicion: Fully Revised & Updated Edition, St. Martin's Press, First Edition October 2019
    unidad: Bonus Chapter
    titulo_textual: Bonus Chapter: A Radically Candid Performance Review
    fidelidad: verbatim
    ---
    $ sed -n "8,$p" fuentes/scott_radical_candor/cap_14.md | wc -w
    7638
    $ wc -l fuentes/scott_radical_candor/cap_14.md
    243 fuentes/scott_radical_candor/cap_14.md

**LOS TRES CUADRAN AL DIGITO CON LOS DEL ENCARGO.** El rotulo es
`Bonus Chapter: A Radically Candid Performance Review`, la unidad es `Bonus Chapter`, el cuerpo son
**7.638** palabras y el fichero **243** lineas. **La caida del rotulo del encargo anterior queda
registrada con el nombre de quien la firmo y no la reabro.**

### R.5.b. **EL PAR MAS CARO DE FALLAR, LEIDO ENTERO ANTES DE CORTAR** (`EXTRACTOR.md` 2)

*El encargo me manda leer `entregar_evaluacion_formal_desempenio_nueve_consejos` ENTERO antes de
cortar `cap_14`, no despues de que la aduana me bloquee. **Lo lei entero, sus 22 pasos, y va aqui su
lectura con la conclusion delante.***

**EL GEMELO DECLARADO Y SU MEDIDA, impresa de su fichero:**

| | |
|---|---|
| id | `entregar_evaluacion_formal_desempenio_nueve_consejos` |
| unidad | `cap_11` |
| pasos | **22** |
| condicion de activacion | *Cuando tu empresa tiene un proceso formal de evaluacion de desempenio y te toca dar la de alguien de tu equipo.* |
| entregable | *Una evaluacion dada sin sorpresas, contrastada con mas de un juicio, escrita, con la mitad del tiempo puesta en el plan que la propia persona propone, y con sus revisiones marcadas en el calendario.* |

> ## **VEREDICTO DEL PAR `cap_14` CONTRA `entregar_evaluacion_formal_desempenio_nueve_consejos`: `SANO`. NO SON GEMELOS Y LA RAZON ES EL SUJETO.**
>
> **El nodo de `cap_11` tiene por sujeto UN JEFE que entrega UNA evaluacion a UNA persona**, y su
> procedimiento entero son actos de esa conversacion: no des sorpresas, pide primero que te evaluen
> a ti, escribela, decide cuando la entregas, reserva cincuenta minutos, parte el tiempo en
> diagnostico y plan, no traigas tu el plan, deja la nota y la paga para el final.
>
> **`cap_14` tiene por sujeto UN EQUIPO DE GESTION DEL DESEMPENIO que disenia EL SISTEMA de una
> empresa**, y su procedimiento entero son decisiones de disenio: si hay nota, cuantas, como se
> llaman, que reparto se espera, si se fuerza la curva, como se calibra, cada cuanto, si es de
> trescientos sesenta grados, si es transparente, si es ligero.
>
> **LA PRUEBA MAS BARATA DE QUE NO SE PISAN:** el nodo de `cap_11` **presupone** el sistema (*cuando
> tu empresa TIENE un proceso formal*) y `cap_14` **lo construye**. Y no hay ni un paso repetido: la
> unica frontera que se tocan es la palabra evaluacion.
>
> **Y LO DIGO ANTES DE QUE LA ADUANA OPINE, que es la orden:** ninguno de los 15 informes de esta
> tanda levanto a `entregar_evaluacion_formal_desempenio_nueve_consejos` como vecino de ningun
> candidato de `cap_14`. **La lectura y la senial coinciden, y la lectura iba primero.**

### R.5.c. LA FRONTERA DE `cap_14`, **PUBLICADA ANTES DE CORTAR Y CERRADA CONTRA EL CUERPO AL DIGITO**

Salida de `python .v24/frontera_cap14.py`, guardada en `.v24/salida_frontera_cap14.txt`:
