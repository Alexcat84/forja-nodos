# ENCARGO DE LA VUELTA 40: **CERRAR LA SERIE `D.37` DE LOS CUATRO ELEMENTOS**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

*Linea **serial** (`extraccion-mundo-11`), la unica que inserta (`D.45`). Escrito al cerrar la
`ACTA 38`, que audita la vuelta 39 y **no abre ninguna parada**.*

> # **LIBRO DE ESTA VUELTA: `scott_radical_candor`**

> ## **LA VUELTA 39 SALIO LIMPIA DE TRES ESPECIES Y NO TE LO VOY A ESCONDER**
>
> | especie | de | a |
> |---|---:|---:|
> | **`REPORTE`** | `2 de 3` | **`0 de 3`** |
> | **`CIFRA PUBLICADA`** | `1 de 2` | **`0 de 2`** |
> | **`CLASE`** | `0 de 2` | **`0 de 2`** |
>
> **Las dos primeras las reinicia una tanda limpia por `D.38.1`, no el auditor.** Tu reporte
> **cerro**, escribio la linea literal con `N` igual a `3`, y sus diecinueve cifras de apertura y
> cierre me salen al digito. **Tus nueve discutibles se sostienen los nueve. Cero caidas dentro de
> tu marcado.**
>
> **Y HAY UNA CAIDA, Y NO ES DE LAS QUE TU MARCASTE:** `DATO MOVIDO` sube a `1 de 2`. Esta en la
> `TAREA 1.A` y es lo primero de tu turno.

> ## **EL TRAMO SUBE A CUATRO, Y VA CON SU ARITMETICA DELANTE**
>
> | techo | lo medido | que sale |
> |---|---|---:|
> | `PASOS INVENTADOS` (`AUDITOR_FORJA.md` 8.1) | **`0,00`** por ciento en tu tramo, contra el `2,97` del anterior y el tope de `10` | **sube un escalon** |
> | cerrar el reporte (`EXTRACTOR.md` 12.4) | **cerraste**, con la linea literal escrita | **no frena** |
> | **el reloj, que es el que avisa** | **`896` s de media por insercion**, contra los `483` con los que se dimensiono tu tramo | **manda elegir bien los cuatro** |
>
> **POR ESO LOS CUATRO SON ESTOS Y NO OTROS CUATRO:** los tres que le faltan a la serie `D.37` mas
> el nodo al que `L237` entrega. **Tres de los cuatro traen su arista ya escrita y en cola**, asi
> que se cablean solas al entrar; **y los pares mas probables del cuarto ya estan adjudicados** en
> las lineas `488` y `500` de la bitacora. **Ninguno abre vecindad que no este ya juzgada.**
>
> **Y LOS DOS MAS GORDOS NO ENTRAN HOY A PROPOSITO:** `dar_elogio` (`20` pasos) y `medir_critica`
> (`33` pasos) esperan a la vuelta 41 **con su arista `49` y su `51` ya en cola**. **No estires el
> tramo a seis.**

---

## TAREA 1, BLOQUEANTE. **LOS REGISTROS**

### 1.A. **DOS CARACTERES DE CONTROL `U+0008` DENTRO DE `dataset/nodos.jsonl`, Y ES LA CAIDA DE LA VUELTA**

    $ python -c "... repr del resumen_teorico de pedir_critica_primero_crear_seguridad_psicologica ..."
      "... y grep -o -iE '\x08ceo\x08' dataset/nodos.jsonl | wc -l d..."

**LA CIFRA ES CIERTA Y ESO VA PRIMERO:** sobre `e3950c6` y sus `321` nodos, `ceo` como palabra da
`0` y *consejero delegado* da `39`, comprobado por el auditor. **No hay cifra falsa y no es
`CIFRA PUBLICADA`.** Lo que hay es **dato corrompido**: el comando que ese campo publica como prueba
lleva **dos retrocesos donde tenia que llevar dos escapes**.

**LA CAUSA, Y NO ES TU PULSO:** la ficha se corrigio **en bandeja** con `.v39/corregir_cand1.py`,
porque `forja.py corregir` **solo actua sobre nodos ya insertados** y esta casa no tiene instrumento
para corregir un candidato en bandeja. Un script escribe `"\bceo\b"` en Python y al JSON llegan dos
caracteres de control. **De la bandeja paso al catalogo y a `cuarentena/_insertados/`.**

**LO QUE HACES, Y SOLO ESTO:**

1. **Una correccion declarada con `python forja.py corregir --nodo pedir_critica_primero_crear_seguridad_psicologica`**,
   que diga con todas sus letras que el comando publicado en la correccion anterior **viaja con dos
   caracteres de control** y que el comando que reproduce la cifra es
   `grep -o -iE "\bceo\b" dataset/nodos.jsonl | wc -l`. **Sin borrar nada**, que es como corrige
   esta casa.
2. **Pega el barrido de control despues**, sobre los valores decodificados de `dataset/nodos.jsonl`,
   `bitacora/VEREDICTOS.jsonl`, `config/pares_mutuos.jsonl`, `censos/` y `cuarentena/`. **Hoy el
   unico fichero con control es ese nodo, y su copia archivada.** Si sale otro, lo declaras.

> **NO RETIRES LOS CARACTERES Y NO ESCRIBAS UN INSTRUMENTO QUE LOS RETIRE.** La correccion por
> anexion no puede quitarlos y `7.F` de la cosecha veda la maquinaria nueva. **La pregunta de si se
> pueden retirar ya esta en la cola de doctrina como la `11`**, escrita en `config/frentes.json` por
> el auditor en su propia tanda. **No la dupliques y no la resuelvas.**

**Y CUENTA CON QUE ESTA CORRECCION VUELVE A DEJAR RANCIOS** los veredictos emitidos contra la huella
vieja de ese nodo. **Es `D.15`, cola de trabajo y no gate en rojo**, y se declara con su cifra al
cierre igual que hiciste con los `4` de la vuelta 39.

### 1.B. **LA CORRECCION DE LA VUELTA 39 DEJO DOS RANCIOS QUE HOY TE TOCAN A TI**

    $ python forja.py rancios | grep "practicar_triangulo" | cut -c1-118
      [RANCIO] veredicto practicar_triangulo_critica_tres_papeles contra abrazar_incomodidad_silencio_contar_seis (linea 4
      [RANCIO] veredicto practicar_triangulo_critica_tres_papeles contra escuchar_entender_critica_dominar_defensa (linea 
      [RANCIO] veredicto practicar_triangulo_critica_tres_papeles contra mejorar_consciencia_propia_relacional_dos_practic
      [RANCIO] veredicto practicar_triangulo_critica_tres_papeles contra practicar_triangulo_critica_tres_papeles (linea 4

**Las lineas `484` y `485` son pares de DOS de tus cuatro candidatos de hoy.** Cuando cada uno entre,
**relee ese par contra el texto nuevo de `practicar_triangulo` y vuelve a emitirlo, o declara por
escrito por que el `SANO` se sostiene sin releerlo.** Las dos cosas valen; **la que no vale es
insertar encima de un veredicto rancio sin decir nada.**

### 1.C. **LAS ADJUDICACIONES DE LA `ACTA 38`, RECOGIDAS Y NO REABIERTAS**

| | lo adjudicado |
|---|---|
| **tus NUEVE discutibles se sostienen los nueve** | el prefijo `CC`, la reparacion sin minimo, el `0` `PUENTE`, el `P22` con la `X` de `L157`, el `P11` con `L183`, los ordinales de `L129`, el titulo del candidato `2`, el campo de `6.741` caracteres y el `SANO` de `integrar_peticion`. **Cero caidas dentro de tu marcado** |
| **la fila de `PASOS INVENTADOS` la firma el auditor** | **tu tramo, `0` de `56`, `0,00` por ciento: FIRMADA.** `cap_13` entero, `4` de `212`, `1,89` por ciento, **sigue siendo SUELO** y el auditor no la firma: `156` de esos pasos no los ha releido el |
| **el `P11` del candidato `3` NO es `PUENTE`** | `L181` pregunta *Where should I start?* y `L183` **si contesta**. Es prosa circular, no contenido inventado. **Tu `0` aguanta** |
| **el prefijo `BC.6` del encargo anterior era MIO y estaba mal** | tu `grep` tenia razon. **Esta vuelta el encargo ya no te dicta prefijo** (`TAREA 4`) |
| **mi propuesta de arista entre `resolver_dudas` y `elegir_pregunta`: RETIRADA** | tu razon de la linea `505` la gano. **El `SANO` se queda solo, sin cable** |
| **lo que ya esta hecho y no repitas** | el auditor subio la pregunta `11` a `config/frentes.json` y **volco `docs/loop/TABLERO.jsonl`**. **No lo vuelvas a volcar salvo que cambies su sede** |

---

## TAREA 2, BLOQUEANTE. **LA FIDELIDAD `D.30` DE LOS CUATRO, ANTES DE LA PRIMERA INSERCION**

`EXTRACTOR.md` 15.4. **Son `58` pasos** (`12` mas `13` mas `20` mas `13`) y van releidos **contra su
linea del libro**, no contra el grafo.

**LA CLASE QUE SE RELEE ENTERA SIGUE SIENDO LA MISMA:** cuando un paso nombre **una persona, una
cuenta, un escalon o un adjetivo de sentimiento**, lee la linea completa antes de marcarlo
`TRANSCRIPCION`. **Declara cuantos releiste por ese motivo, aunque sean cero.**

> **Y UNA ADVERTENCIA QUE SALE DE TU PROPIO REPORTE, NO DE LA MIA:** tu `0` de `56` de la vuelta 39
> lo explicaste tu mismo, y tenias razon: **los tres venian ya releidos**. **Estos cuatro NO.**
> `premiar_franqueza` trae `20` pasos y `abrazar_incomodidad` cuenta hasta seis en voz alta.
> **Un `0` aqui valdria mucho mas que el de la vuelta pasada, y por eso no lo des por hecho.**

**Publica la fila con su denominador dicho:** `cap_13` entero son `12` candidatos y `212` pasos.
**Tu tramo son `4` de esos `12` y `58` de esos `212`.** La fila del capitulo **no la firmes** si no
has releido sus `212`.

---

## TAREA 3. **`cap_13`, CUATRO CANDIDATOS EN EL ORDEN DEL LIBRO, UNO POR VEZ**

| # | candidato | linea | pasos | lo que ya tiene escrito |
|---:|---|---|---:|---|
| `1` | `abrazar_incomodidad_silencio_contar_seis` | `L187`, rotulo `EMBRACE THE DISCOMFORT` | 12 | **arista `D.37` en cola, linea `489`**: se cablea sola al entrar |
| `2` | `escuchar_entender_critica_dominar_defensa` | `L199`, rotulo `LISTEN WITH THE INTENT TO UNDERSTAND` | 13 | **arista `D.37` en cola, linea `492`** |
| `3` | `premiar_franqueza_hacer_escucha_tangible` | `L215`, rotulo `MAKE LISTENING TANGIBLE` | 20 | **arista `D.37` en cola, linea `495`** |
| `4` | `integrar_peticion_critica_rutina_existente` | `L235`, rotulo `BUILD IT INTO YOUR EXISTING SCHEDULE` | 13 | **`SANO` ya escrito contra la cabeza (`488`) y contra `elegir_pregunta` (`500`)** |

### 3.A. **CON EL `3` SE CIERRA LA SERIE `D.37` DE LOS CUATRO ELEMENTOS, Y ESO SE DICE EN EL REPORTE**

`L113` escribe *each of the four tips for soliciting criticism* y `L237` los nombra uno a uno.
`elegir_pregunta` entro en la vuelta 39 y es el primero. **Cuando entren estos tres, las cuatro
partes de la serie estan en el grafo con sus cuatro aristas cableadas desde la cabeza.** **Escribe
esa frase con la cifra al lado**, porque una serie `D.37` a medias es el estado fragil y el reporte
tiene que decir cuando deja de estarlo.

### 3.B. **EL CUARTO NO ES PARTE DE LA SERIE, Y SU VEREDICTO YA ESTA RAZONADO DOS VECES**

`integrar_peticion_critica_rutina_existente` es lo que `L237` manda hacer **DESPUES** de practicar
los cuatro. **`D.37`, apartado *lo que NO autoriza*: un nodo del mismo dominio que no es ninguna de
las cuatro es hermano, y su veredicto es `SANO`.** Tu lo escribiste asi en la linea `488` y el
auditor lo adjudico igual por separado en su apertura sellada. **No lo pelees otra vez: escribelo y
sigue.** Si al leer sus `13` pasos discrepas, **lo dices y lo marcas discutible.**

### 3.C. **Y LOS DOS QUE NO ENTRAN, PARA QUE NO SE PIERDAN**

`dar_elogio_disciplina_igual_critica` (arista `49`, linea `490`) y
`medir_critica_respuesta_oyente_brujula` (arista `51`, linea `494`) **siguen en bandeja con su arista
en cola**. **No los toques y no los declares cerrados.** `cap_13` queda con `2`.

---

## TAREA 4. **EL CIERRE SIGUE SIN IR AL FINAL, Y EL PREFIJO LO ELIGES TU**

**LO QUE FUNCIONO EN LA VUELTA 39 SE REPITE ENTERO:** la seccion de la insercion se abre **ANTES de
que entre el primer candidato**, con la fidelidad y los discutibles dentro, y **crece una fila cada
vez que uno entra**, en su propio commit y con el candidato ya dentro. **Si el reloj te corta en el
`2`, lo que falta es una linea y no una seccion.**

> ### **EL PREFIJO NO TE LO DICTO YO, Y ESTO ES UNA CORRECCION DE MI SEDE**
>
> El encargo de la vuelta 39 escribio *abre `BC.6`* cuando `BC` era el prefijo de la vuelta 38. **Lo
> cazaste tu y tenias razon.** Asi que esta vez el encargo nombra **el papel y el numero, no las
> letras**:
>
>     $ grep -oE "^## [A-Z]{2}\." docs/loop/REPORTE.md | sort -u
>
> **Abre la seccion `.6` con el prefijo que te toque segun esa salida**, y **pega la salida al lado**
> igual que hiciste. **Lo que el encargo compra es la seccion abierta antes de la primera insercion,
> no un par de letras.**

**Y LA LINEA QUE CIERRA, LITERAL, SEA CUAL SEA LA CIFRA:**

> *la vuelta cierra en el candidato `N` de `4`; los que quedaban pasan a la vuelta siguiente.*

**Escribela aunque `N` sea `4`.** Cerrar completo y decirlo cuesta una linea.

**NO TERMINES TU TURNO CON UNA CADENA TODAVIA CORRIENDO.** La vuelta 39 lo comprobo en vez de
prometerlo, con su `tail` del registro de cadenas pegado. **Hazlo igual.**

---

## EL CIERRE: LAS CUATRO COSAS QUE NO SE NEGOCIAN

1. **Gate, barrido de guiones y prueba de aceptacion EN VERDE**, con su salida pegada.
2. **Las cifras del cierre recomputadas al cierre** y no copiadas de tu apertura: nodos, veredictos,
   aristas, bandeja por capitulo, insertados y archivados.
3. **La cola de aristas recontada entera**, con la cifra de las que tienen los dos extremos dentro y
   siguen sin cable. **Hoy sale `0`. Que siga saliendo `0`.** Y cuentala **por `arista_corregida`
   cuando la linea la traiga**: contada por el campo `arista` a secas salen `12` auto aristas viejas
   que ya estan corregidas al lado, y ese `12` no es deuda.
4. **Tus discutibles marcados ANTES de saber si aciertas**, y la fila de `PASOS INVENTADOS` con su
   denominador dicho, **de tu tramo y no del capitulo**.

**Y COMMITEA Y PUSHEA `docs/loop/`.**

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.**
