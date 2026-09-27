
## BC.5. **MIS DISCUTIBLES, MARCADOS ANTES DE INSERTAR NADA** (`EXTRACTOR.md` 8)

*Esta seccion se escribe y se commitea **antes** de la primera insercion, que es lo unico que hace que
el marcado signifique algo. Las dos adjudicaciones que el encargo me deja (`DISCUTIBLE 3` y la
direccion del cable de `P08`) van aqui decididas, no aplazadas.*

### BC.5.a. **LA DIRECCION DEL CABLE DE `P08`, QUE ES LA UNICA QUE EL ENCARGO NO ME DA HECHA**

**LOS DOS PASOS, LEIDOS DEL GRAFO Y NO DEL ENCARGO:**

<!-- TALLADO: parcial salida=.v38/pasos_madres.txt -->

    $ python .v38/pasos.py desplegar_plan_orden_operaciones_franqueza_radical desplegar_marco_franqueza_radical
    === desplegar_plan_orden_operaciones_franqueza_radical ===
      P08: Si quieres, copia el marco de la franqueza radical del capitulo dos y lleva ahi la cuenta de quien te dice que.
    === desplegar_marco_franqueza_radical ===
      P02: Recorta el marco del propio libro. El texto dice que hay una version mas grande en su pagina 297.
      P03: Haz fotocopias.
      P04: Ponlas en tu nevera, encima de tu mesa o en cualquier otro sitio, como recordatorio.
      P05: Comparte copias con tus colegas.

> # **MI DECISION: `desplegar_plan` ES LA MADRE Y `desplegar_marco` ES EL HIJO.** Cable
> `desplegar_plan_orden_operaciones_franqueza_radical > desplegar_marco_franqueza_radical`, paso `8`.

**LA RAZON, Y ES LA VARA MADRE APLICADA AL DERECHO:** *nombrar no es procedimentar*. `P08` dice **copia
el marco** y ahi se acaba; **los pasos `2` a `5` del otro nodo son literalmente como se copia** (recorta,
fotocopia, pega, reparte). **El que nombra es la madre, el que despliega es el hijo**, y aqui no hay
duda de cual es cual.

**LO QUE NO SOSTIENE LA DIRECCION CONTRARIA:** para que `desplegar_marco` fuera la madre, alguno de sus
nueve pasos tendria que **nombrar el plan del orden de operaciones**. **Ninguno lo hace**: sus nueve
pasos van del recorte, el reparto, el uso como brujula y las dos prohibiciones, y el plan de `cap_12` no
aparece en ninguno. **Una arista se cuelga de un paso que nombra al otro extremo, y aqui solo hay un
paso que nombre.**

**Y LO QUE ESTE CABLE NO RESUELVE, que lo digo yo antes de que me lo pregunten:** `P08` tiene **dos
mitades**, *copia el marco* y *lleva ahi la cuenta de quien te dice que*. **El cable cuelga de la
primera.** La segunda es la que choca con `P08` del hijo (*No escribas nombres en las casillas`), y esa
contradiccion **sube a la cola de doctrina en `BC.7` y no la resuelve esta arista.**

### BC.5.b. **`DISCUTIBLE 3`, QUE ES MIO Y LO ADJUDICO: LA ARISTA `50` SI SE CABLEA**

*La vuelta 37 lo marco al reves (*la arista `50` no se cablea, y las `49`, `51` y `52` si*) y **no llego
a escribir su razon**: su turno cerro en el `2` de `14`. **Asi que no heredo un argumento, heredo una
casilla vacia**, y la lleno yo.*

**LOS CUATRO HIJOS DEL ORDEN DE OPERACIONES, CONTRA EL GRAFO DE HOY** y no contra la tabla de la vuelta
23:

<!-- TALLADO: parcial salida=.v38/cuatro_hijos.txt -->

    $ python .v38/cuatro_hijos.py
    LOS CUATRO HIJOS DEL ORDEN DE OPERACIONES, contra el grafo de hoy
      arista 49  dar_elogio_disciplina_igual_critica                 en la BANDEJA
      arista 50  criticar_trabajo_evitar_desanimo                    DENTRO del grafo
      arista 51  medir_critica_respuesta_oyente_brujula              en la BANDEJA
      arista 52  fomentar_guia_reciproca_companieros                 DENTRO del grafo

> # **ADJUDICO QUE LA `50` SE CABLEA**, y con ella la `52`. **Las `49` y la `51` van A COLA**, porque
> sus hijos siguen en la bandeja y esta vuelta no los mete.

**LA RAZON QUE DECIDE ES LA DE LA `ACTA 36` `3.6`, aplicada contra mi mismo:** *una vara no puede dar
dos respuestas a la misma figura dentro de la misma vuelta*. Los cinco pasos del orden son **la misma
figura cinco veces**: un paso que nombra la etapa por su rotulo y un hijo que la despliega. **Si cablear
`Cinco, fomenta el elogio y la critica entre los demas` a `fomentar_guia_reciproca_companieros` esta
bien, cablear `Tres, da critica` a `criticar_trabajo_evitar_desanimo` esta bien**, y no se me ocurre
ninguna diferencia entre los dos casos que no sea que uno me da mas reparo que el otro.

**Y EL REPARO TIENE NOMBRE, ASI QUE LO ESCRIBO:** `criticar_trabajo_evitar_desanimo` **ya tiene madre**,
`empezar_cultura_franqueza_radical`, que es la version en prosa del **mismo** orden de operaciones en
`cap_05`. **Le estoy dando una segunda madre que dice lo mismo que la primera.** Lo hago igual por dos
cosas: **la `ACTA 36` `3.7` sostuvo una TERCERA madre** para `abrazar_incomodidad_silencio_contar_seis`,
asi que en esta casa un hijo con varias madres no es defecto; y **`L87` dice expresamente que las dos
listas son la misma** (*The first edition describes this order of operations*), o sea que la duplicidad
**esta en el libro**, no la invento yo.

### BC.5.c. **LA TABLA DE LOS DISCUTIBLES, ANTES DE SABER**

| # | lo que decido | por donde puede caerse |
|---:|---|---|
| **1** | la arista de `P08` va **`desplegar_plan` > `desplegar_marco`** (`BC.5.a`) | el encargo me da la fila con `desplegar_marco` en la **columna de madre**, asi que si el auditor la leyo al reves, la leyo al reves a proposito y yo me aparto de su casilla |
| **2** | **`DISCUTIBLE 3` CAE: la arista `50` SI se cablea** (`BC.5.b`) | me aparto de lo que la vuelta 37 marco, **al alza**, y le doy a un hijo que ya tiene madre una segunda madre que dice lo mismo. Si sobra una arista en esta vuelta, es esta |
| **3** | los dos defectos de `pedir_critica_primero` `P06` y `P15` son **`PUENTE`** y los cuento en la fila | es la vara que la `ACTA 36` fijo al tumbar mi `DISCUTIBLE 1`. Si el auditor la lee mas estrecha, `cap_13` baja de `2` a `0` y mi fila estaba inflada |
| **4** | la tilde de *grosería* **NO es `D.30`** y no la cuento como `PUENTE` | es un defecto real que ninguna guarda ve, y si el auditor decide que todo lo que la relectura caza cuenta, `cap_13` sube de `2` a `3` de `101` |
| **5** | `pedir_critica_primero_crear_seguridad_psicologica` entra como **nodo propio y no `REPITE`** de `empezar_cultura_franqueza_radical` (heredado, `ACTA 36` `3.5`) | es el par mas caro de fallar del capitulo, y ahora si hay dato que releer: **el veredicto se escribe en esta vuelta**, no en la anterior |
| **6** | `P06` reescrito pone la causa como **ausencia** (*al libro le faltaba una historia de una jefa pidiendo*) y no como presencia | es mi lectura de `L89`, y si el auditor lee que las dos mitades dicen lo mismo, mi correccion movio un paso que no hacia falta mover |

**Y UNA COSA QUE NO ES DISCUTIBLE SINO AVISO DE ALCANCE:** el encargo pide **seis** y `cap_13` tiene
**doce** en bandeja. **La vuelta cierra el capitulo a la mitad a proposito** y los otros seis no se
tocan. Si cierro en menos de seis, lo digo con su cifra en `BC.6`.
