# ENCARGO DE LA VUELTA 27: **LA COLA QUE SE PERDIO DOS VECES**, SEGUIR INSERTANDO EL LOTE 4, Y ABRIR EL LOTE 5

*Escrito por el **auditor** al cerrar la **ACTA 26** y reescrito con la decision del
fundador del 16 sep 2026, archivada en
`docs/loop/paradas/2026-09-16-la-frase-y-el-instrumento-DECISION.md`. Sede del auditor
por `AUDITOR_FORJA.md` 5.6.*

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO QUE LA DECISION DEJA RESUELTO, EN CINCO LINEAS

- **LA PARADA SE DISOLVIO POR LETRA, NO POR INDULTO.** `LIMPIA` significa **sin caidas de
  la especie que esa racha acumula**, y la `ACTA 25` no tuvo ninguna: **la racha del
  auditor recomputa a `1 de 3`.** El detalle esta en la parada archivada.
- **TU VUELTA 26 SALIO LIMPIA** de `CLASE` y de `CIFRA PUBLICADA`, con tus siete cifras de
  cierre y tus `35` pares al digito y **los nueve discutibles sostenidos**. `REPORTE`
  sigue en **1 de 3**.
- **`D.38.5` YA LLEGO A `src/aduana.py`**, que es donde se decide. **La aduana mide ahora
  grafo mas bandejas tambien al insertar**, asi que **espera mas bloqueos que antes** y no
  es que tus candidatos hayan empeorado: es cola que antes se aplazaba.
- **`D.40` SE ENSANCHA:** un `NO APLICA` sobre un heredado **lleva la salida del
  instrumento pegada debajo**. Es del auditor, pero te lo digo porque el arnes se detiene.
- **`D.38.3` SE ENSANCHA:** **la frase es la del instrumento**, y toda conclusion sobre
  contenido va en linea aparte marcada `LECTURA`. **Te aplica a ti tambien.**

---

## TAREA 1: **LOS OCHO PUNTOS DE LA `ACTA 25` QUE NO LLEGARON AL ENCARGO DE LA 26**

*Punto 4 de la decision. **Esto se perdio una vez y el remedio de la fase ciega lo cazo
con un `grep`**: siete de los ocho no estaban en el encargo que la vuelta 26 recibio, y de
los dos que el `grep` daba por presentes, **ninguno lo estaba de verdad**. Van aqui
enteros, y ninguno es opcional.*

| # | que hay que hacer | de donde sale |
|---:|---|---|
| **1** | **la celda del tallado dice contra QUE VERSION se corrio** | `ACTA 25` `11.1` |
| **2** | **los dos candidatos del ancla unica que se corrigen EN LA BANDEJA** | `ACTA 25`, hallazgo del ancla (`4 de 24`) |
| **3** | **la operacion escrita para los DOS que ya viven en el grafo** con la frase falsa dentro | `ACTA 25`, y `5.2` no tiene casilla para esto: **por eso va escrito** |
| **4** | **el puente `Pide`** de `cap_02`, que invierte el acto | `ACTA 25`, cuarta especie de `D.30` |
| **5** | **`cap_04` releido antes que el hueco** | `ACTA 25` |
| **6** | **las `QUESTIONS TO CONSIDER` no son nodo**, adjudicado por exclusion con tres reglas | `ACTA 26` `2.x` lo repite |
| **7** | **la correccion 9 al reves**, que lleva cinco vueltas con los papeles cambiados | `ACTA 26` |
| **8** | **la cola de `decidir_momento_despedir_persona` es `4` y no `2`** | ya regenerada el 15 sep en `.v25/cola_lectura.txt` |

> **Y EL REMEDIO QUE LO CAZO SIGUE VIVO:** antes de cerrar tu turno, **busca con `grep` en
> este fichero cada cosa que el acta encargue.** Es un comando, no la memoria, y ya fallo
> una vez sin que nadie lo viera.

---

## TAREA 2: **LAS TRES ARISTAS ADJUDICADAS, Y UNA ES LA PRIMERA ENTRE LIBROS**

*Punto 3 de la decision, literal: **la primera arista entre libros NO ES CEREMONIA.** Esta
adjudicada y vencida, **se declara como cualquier arista, con su razon.** La firma del
fundador es para la doctrina, no para las aristas; **una arista que espera un estreno es
una arista que falta.***

**2.a. LA PRIMERA ENTRE DOS LIBROS DE ESTA CASA** (`ACTA 26` `2.3`), con los dos extremos
ya en el grafo desde la vuelta 26:

    python forja.py arista --madre despedir_persona_respeto_franqueza \
                           --hijo  despedir_persona_franqueza_radical --paso 8 \
                           --razon "D.29 por lectura: el paso 8 de la madre NOMBRA (ayuda a tu
                           persona a cargo a ponerse en el mejor camino posible hacia su capitulo
                           siguiente) y el hijo lo PROCEDIMENTA en sus pasos 5, 6 y 8. El libro lo
                           escribe literal en cap_06 L299: Can I help by making an introduction?
                           Admisible entre libros por ACTA 15 3.4, que ninguna parada retira."

**2.b y 2.c. LAS DOS QUE LA LECTURA CIEGA LEVANTO Y NINGUNA SEÑAL VE**, con los dos
extremos ya dentro (`APERTURA_CIEGA.md` `4.3` y `4.4`):

- **`decidir_momento_despedir_persona > despedir_persona_franqueza_radical`**: el
  **entregable** del primero es la **condicion de activacion** del segundo, escrito con
  esas palabras en los dos ficheros, y **los cuatro campos de arista de los dos estan
  vacios.**
- **`aprender_resultados_vencer_dos_presiones > cambiar_posicion_hechos_explicar_cambio`**:
  **`D.37` en su forma fuerte**, la madre nombra *las dos enormes presiones* y el libro
  imprime los dos rotulos (`cap_07` `L403` *Pressure to be consistent*, y *Burnout*). **La
  segunda mitad vence cuando entre `cuidarse_agotamiento_centro_rueda`**, que sigue en la
  bandeja.

---

## TAREA 3: **SEGUIR INSERTANDO EL LOTE 4**

| | |
|---|---:|
| candidatos en bandeja | **111** de 142 |
| ya insertados y archivados | **31** |
| nodos en el grafo | **234** |
| veredictos en bitacora | **240** |

**DONDE SE PARO:** dentro de `cap_07`, en `centrar_debate_ideas_fuera_egos`.

> ### **Y LA CABEZA DE LA RUEDA VA POR DELANTE DE SUS PARTES**
>
> **`recorrer_rueda_hacer_cosas_equipo` se inserta ANTES que sus partes** (propuesta `2`
> del extractor en `T.6`, adjudicada): sus tres partes estan en la bandeja, y **si entran
> antes que la cabeza, sus aristas `D.37` no las va a poder cablear la aduana.**

**LO QUE CAMBIO DEBAJO DE TI, y es la razon de que veas mas bloqueos:** `D.38.5` ya corre
en `src/aduana.py`. **La aduana mide grafo mas bandejas tambien al insertar**, y publica la
poblacion con su reparto. **Los cinco pares que la `ACTA 26` midio como aplazados ya no se
aplazan: se bloquean y se leen.**

---

## TAREA 4: **ABRIR EL LOTE 5 POR SU ORDEN, SI LA INSERCION DEJA SITIO**

| | |
|---|---:|
| lote 5 | `marquet_turn_the_ship` |
| unidades | **17**, de ellas **2 minadas** |
| candidatos en bandeja | **3** |

**EL ORDEN LO FIJA `docs/loop/ORDEN_DE_LOTES.md` y no lo elige la vuelta** (`D.24`). **El
tramo se queda en TRES** y no sube (`ACTA 26` `4.4`), y **el techo de candidatos por vuelta
sigue mandando sobre el de capitulos**: si un capitulo lo pasa, **la vuelta cierra ahi y lo
declaras con su cifra.**

---

## LO QUE MANDA EN COMO ESCRIBES, Y HOY HAY DOS COSAS NUEVAS

**`D.41`:** toda tabla que presentes como salida de un instrumento **se anexa desde su
fichero**, y el hook la compara celda a celda.

**`D.42`:** toda ruta que publiques como sede de una cifra **tiene que sostenerla**, con
sus tres formas y solo tres.

> ### **Y DESDE HOY, `D.38.3` ENSANCHADA: LA FRASE ES LA DEL INSTRUMENTO**
>
> **La linea que acompania a una cifra dice lo que el instrumento MIDIO.** Toda conclusion
> sobre **contenido** va en **linea aparte marcada `LECTURA`**, con lo que la sostiene.
>
>     campo cap_NN presente en resumen_teorico : 33 de 234
>     $ grep -lc "cap_[0-9]" ...   ->  33
>     LECTURA: la costumbre de nombrar la unidad empieza en cap_07, y por eso los
>     anteriores no la traen.
>
> **Contar campos y publicar una frase sobre contenido es caida de cifra**, y le paso al
> auditor en la vuelta 26 con la cifra bien contada y la frase falsa.

**Al cerrar la vuelta:** `python scripts/cerrar_reporte.py`, que corre el tallado en
estricto, el censo de rutas y las cinco guardas.

## SON CUATRO TAREAS Y EL TOPE SON CINCO

**La TAREA 1 va primera y no se solapa**, porque ya se perdio una vez. **Si la insercion se
come la vuelta, la vuelta se cierra ahi y lo declaras con su cifra**: abrir el lote 5 con
el 4 a medio insertar no adelanta nada.
