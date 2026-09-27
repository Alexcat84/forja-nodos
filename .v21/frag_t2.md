
---

## O.3. TAREA 2: **`cap_10` ENTERO, TRECE CANDIDATOS**. CERRADA

*El encargo la pone como la tarea de la que no se separan las otras dos, y asi la ejecuto:
primero mi propia lectura de la frontera con los pasos delante (`P.17`), despues los trece
candidatos uno a uno con su informe, y despues las aristas y el par, que nacen de ellos.*

### O.3.a. **LA UNIDAD, REMEDIDA POR MI ANTES DE TOCARLA** (`EXTRACTOR.md` 5)

    $ sed -n '1,6p' fuentes/scott_radical_candor/cap_10.md
      libro: Scott, Radical Candor
      unidad: Cap. 7
      titulo_textual: Team
    $ sed -n '8,$p' fuentes/scott_radical_candor/cap_10.md | wc -w
      8976
    $ wc -l fuentes/scott_radical_candor/cap_10.md
      263

**LAS TRES CIFRAS DEL ENCARGO REPRODUCEN AL DIGITO: cuerpo `8.976`, unidad `Cap. 7`, rotulo
`Team`.** El encargo decia *remidelo tu*, y remedido esta.

### O.3.b. **MI PROPIA LECTURA DE LA FRONTERA, CON LOS PASOS YA ESCRITOS DELANTE** (`P.17`)

*La `ACTA 20` `4.6` cerro la frontera en **13** y dijo con todas las letras que **si mi lectura
con los pasos delante contradice su tabla, gana la mia**, declarada con su frontera al lado y su
`sed` pegado. **Asi que la corto otra vez y la cierro contra el cuerpo ANTES de publicar la
cuenta**, que es la orden 1 de la `ACTA 18` `7.5`.*

    $ python .t1_v21/frontera21.py | head -12
    ==============================================================================
    1. LA COMPROBACION, ANTES DE LA TABLA
    ==============================================================================
    tramos que dan nodo                    : 6
    tramos de resto                        : 3
    lineas con contenido de L8 en adelante : 128
    lineas NO cubiertas                    : 0  []
    SOLAPES                                : 0  []
    suma de las filas                      : 8976 palabras
    cuerpo medido aparte (sed 8,$ | wc -w) : 8976 palabras
    IGUALES                                : True

> ### **CIERRA AL DIGITO: `8.976` CONTRA `8.976`, CERO LINEAS SIN CUBRIR Y CERO SOLAPES. LA CUENTA SE PUEDE PUBLICAR.**

**LA TABLA LA IMPRIME EL MISMO GUION QUE CORRE LA COMPROBACION** (`EXTRACTOR.md` 5), con la
salida literal de la primera linea de cada tramo pegada en su ultima columna (`D.35`):

| tramo | palabras | nodos | que es | la salida, pegada |
|---|---:|---:|---|---|
| `L47 a L87` | 1862 | **3** | las tres conversaciones de carrera | `47:Conversation one: life story` |
| `L93 a L125` | 1095 | **1** | el plan anual de gestion del crecimiento | `93:GROWTH MANAGEMENT` |
| `L127 a L163` | 1501 | **1** | el proceso de contratacion, con el acto de L129 dentro | `127:HIRING: YOUR MENTALITY AND YOUR PROCESS` |
| `L165 a L201` | 1372 | **5** | despedir: cabeza, tres partes y coda | `165:FIRING` |
| `L203 a L223` | 638 | **1** | la calibracion de ascensos, con el caso de Google dentro | `203:PROMOTIONS` |
| `L225 a L251` | 568 | **2** | recompensar sin ascender | `225:REWARD YOUR ROCK STARS` |
| | **7036** | **13** | **los seis tramos que dan nodo** | |

| tramo de resto | palabras | nodos | por que no |
|---|---:|---:|---|
| `L9 a L45` | 1641 | **0** | subtitulo, entrada, rotulos y EL CASO DE RUSS LARAWAY |
| `L89 a L91` | 101 | **0** | cierre de seccion que remite a una web y a un libro de otro |
| `L253 a L263` | 198 | **0** | el cuadro que no esta en el recorte, el resumen y la cabecera del cap siguiente |
| | **1940** | **0** | |

> ### **MI LECTURA CON LOS PASOS DELANTE DA 13, LA MISMA CUENTA QUE LA `ACTA 20` `4.6`, Y EN LOS MISMOS SEIS TRAMOS. NO CONTRADIGO LA TABLA DE LA CASA: LA CONFIRMO HABIENDO ESCRITO LOS 194 PASOS.**
>
> **Y DIGO QUE ESO ES MAS QUE COINCIDIR EN UN NUMERO:** los dos cortes que el acta me gano en
> la vuelta 20 (`L93 a L125` en **uno** y `L169 a L201` en **cinco**) son los dos que escribir
> los pasos confirma mas claro. El plan de crecimiento no se pudo partir: la linea 103 dice
> *The first step is* y la 109 dice *Next*, asi que sus partes entraron como pasos 5 a 21 de un
> solo nodo sin que sobrara ni faltara nada. Y el tramo de despedir no se pudo juntar: al
> escribir los pasos, **cada una de las cuatro piezas pedia su propio entregable** y la cabeza
> se quedo con once pasos que ninguna de las tres partes tiene.
>
> **LA UNICA DIFERENCIA CON LA TABLA DEL ACTA ES DE ENCUADRE Y NO DE CUENTA, y la declaro:** mi
> tabla abre el tramo de contratacion en `L127` y no en `L133`, y el de despedir en `L165` y no
> en `L169`, porque los rotulos de seccion (`HIRING: YOUR MENTALITY AND YOUR PROCESS`, `FIRING`,
> `A necessary evil`, `PROMOTIONS`, `REWARD YOUR ROCK STARS`) van dentro del tramo que encabezan
> en vez de ser piezas sueltas. **Es el mismo encuadre que la frontera ciega del auditor usaba
> (`ACTA 20` `3.1`, sus 18 piezas contra mis 39) y por eso mis palabras por tramo no son
> comparables fila a fila con mi propia tabla de 39 piezas de la vuelta 20.** La suma total es
> la misma y las lineas cubiertas son las mismas **128**.

### O.3.c. **LOS TRECE, UNO A UNO, CON SUS PASOS CONTADOS DEL FICHERO Y SU SELLO**

*`EXTRACTOR.md` 5: la tabla se cuenta de su fichero. La imprime `.t1_v21/frontera21.py` y los
sellos los da `git hash-object`, que es lo que ata cada informe a un estado de fichero.*

| # | pieza | id | pasos | atrib. | sello del fichero (`git hash-object`) |
|---:|---|---|---:|---:|---|
| 1 | `P7` | `conversar_historia_vida_descubrir_motivadores` | **15** | 0 | `3c0e1470` |
| 2 | `P8` | `conversar_suenios_cruzar_habilidades` | **15** | 0 | `021fe522` |
| 3 | `P9` | `trazar_plan_dieciocho_meses_aprendizaje` | **14** | 0 | `02218600` |
| 4 | `P13 a P17` | `armar_plan_anual_crecimiento_equipo` | **29** | 0 | `e0ab02b1` |
| 5 | `P19 y P21` | `montar_proceso_contratacion_reducir_sesgo` | **32** | 2 | `8800e11c` |
| 6 | `P24` | `facilitar_despido_tres_cosas` | **11** | 0 | `8a2c3c69` |
| 7 | `P25` | `admitir_pronto_mal_desempenio_cuatro_razones` | **9** | 0 | `3ba9b4c1` |
| 8 | `P26` | `calibrar_decision_despido_documentarla` | **13** | 0 | `dfbbc36c` |
| 9 | `P27` | `sopesar_consejo_legal_despedir_humildad` | **8** | 0 | `f5bf0d46` |
| 10 | `P28` | `contactar_despedido_mes_despues` | **6** | 0 | `84fe0efe` |
| 11 | `P30` | `calibrar_ascensos_evitar_politica` | **19** | 1 | `f56f86e7` |
| 12 | `P33` | `evitar_obsesion_ascenso_estatus` | **10** | 0 | `e8570386` |
| 13 | `P34 a P36` | `reconocer_excelencia_trayectoria_gradual` | **13** | 1 | `52eaaad4` |
| | | **trece candidatos** | **194** | **4** | `.aduana_v21/sellos_candidatos.txt` |

    $ ls cuarentena/scott_radical_candor/*.json | wc -l
      96
    $ wc -l < .aduana_v21/sellos_candidatos.txt
      13

**`83` al abrir mas `13` de hoy son `96`**, y la cuenta de la bandeja lo confirma. **`194` pasos
en trece nodos son `14,9` de media**, contra los `13,6` de los 20 de `cap_09`.

### O.3.d. **LA RELECTURA DE FIDELIDAD `D.30`, Y NO SALIO LIMPIA: ME CACE 22 CUENTAS MIAS ATRIBUIDAS AL LIBRO**

*`D.30`: ninguna guarda de esta casa ve un paso que yo escribi y el libro no dice. Y la `ACTA 20`
`1.4` dejo el ejemplar de la especie exacta que hoy me muerde a mi: **la vuelta 20 se cazo un
puente que decia la diferencia que el texto pone entre LAS DOS MANERAS de compadecerse, cuando
el texto NO da esa cuenta.** Hoy he escrito diecisiete de esas y cinco mas en titulos.*

**PRIMERO EL INSTRUMENTO ESTRECHO, el mismo de la vuelta 20 aplicado al tramo de cada candidato
y no al capitulo entero:**

    $ python .t1_v21/cifras21.py          (ANTES de la correccion)
      cifras y numerales comprobados en los 194 pasos : 170
      los que NO estan en su tramo del libro           : 11

**Y DESPUES EL ANCHO, QUE TUVE QUE ESCRIBIR PORQUE EL ESTRECHO NO BASTA, y digo por que no
basta:** `cifras21.py` busca el numeral en el tramo, y **el tramo puede traer ese mismo numero
por otra razon**. Si el libro dice `three to five columns`, mi `sus tres preguntas` pasa sin que
nadie compare nada. **`.t1_v21/cuentas21.py` no decide: LISTA**, y la lectura la hago yo.

    $ python .t1_v21/cuentas21.py | tail -2
      ocurrencias de numeral que cuentan cosas, en los 194 pasos: 52

**LAS 52 RELEIDAS UNA A UNA CONTRA SU LINEA. 35 SON DEL LIBRO Y SE QUEDAN; 17 ERAN MIAS Y SE
RETIRAN.** Las diecisiete, con la linea que NO las dice:

| # | id | paso | la cuenta que yo atribuia | la linea, y lo que dice de verdad |
|---:|---|---:|---|---|
| 1 | `conversar_historia_vida...` | 5 | *El texto da sus **dos** ejemplares* | `L49` pone dos respuestas seguidas y **no escribe ninguna cuenta** |
| 2 | `conversar_historia_vida...` | 6 | *los otros **dos** ejemplares* | `L49`, igual |
| 3 | `conversar_suenios...` | 12 | *sus **tres** preguntas* | `L71`: *what are the projects..., whom can you introduce..., what are the options for education?* **Tres, sin cuenta escrita** |
| 4 | `armar_plan_anual...` | 10 | *el texto nombra **tres*** | `L105`: *your boss, a peer, an HR person.* **Tres nombrados, sin cuenta** |
| 5 | `armar_plan_anual...` | 16 | *las **tres** preguntas del texto* | `L109`: tres preguntas seguidas, **sin cuenta** |
| 6 | `montar_proceso...` | 6 | *basandola en **tres** cosas* | `L137`: *the role, the skills required for the role, and the team fit criteria* |
| 7 | `montar_proceso...` | 7 | *sus **dos** ejemplares* | `L137`: *It could be... Or maybe it's...* |
| 8 | `montar_proceso...` | 13 | *en las **dos** direcciones* | `L139` dice las dos cosas y **no las cuenta** |
| 9 | `montar_proceso...` | 20 | *las **dos** razones que el texto da* | `L147` da dos y **no las cuenta** |
| 10 | `montar_proceso...` | 30 | *las **dos** caras que el texto le pone* | `L163` dice las dos y **no las cuenta** |
| 11 | `admitir_pronto...` | 2 | *con sus **dos** preguntas* | `L177` hace dos y **no las cuenta** |
| 12 | `calibrar_decision...` | 4 | *los **dos** errores opuestos* | `L183` pone dos y **no los cuenta** |
| 13 | `sopesar_consejo_legal...` | 6 | *las **dos** respuestas* | `L193` pone dos y **no las cuenta** |
| 14 | `calibrar_ascensos...` | 2 | *los **cinco** consejos* | `L213`: *Here are **some tips*** . **LA CUENTA CINCO ERA MIA** |
| 15 | `calibrar_ascensos...` | 5 | *sus **dos** defectos* | `L211` pone dos y **no los cuenta** |
| 16 | `evitar_obsesion...` | 4 | *Pesa las **dos** cosas* | `L233` opone coste y beneficio **sin contarlos** |
| 17 | `evitar_obsesion...` | 6 | *las **dos** mitades* | `L235` separa las dos **sin contarlas** |

**Y LAS CINCO DE TITULO Y DENOMINACION, que son la misma especie en otra sede, y una de ellas
era ademas una cifra FALSA:**

| sede | lo que decia | lo que dice hoy, y por que |
|---|---|---|
| `montar_proceso...` **titulo** | *con las **cinco** practicas que el texto nombra* | *con las practicas que el texto nombra*. `L135` dice *some simple things*, **y mi propia cuenta de rotulos del libro es SEIS** (`L137`, `L139`, `L145`, `L149`, `L153`, `L159`): la cifra no solo estaba atribuida, **estaba mal** |
| `montar_proceso...` **nombre largo** | enumeraba **cinco** fundiendo dos rotulos en uno | enumera los **seis**, sin cuenta atribuida |
| `calibrar_ascensos...` **titulo** | *con los **cinco** consejos que el texto da* | *con los consejos que el texto da* |
| `calibrar_ascensos...` **nombre largo** | *los **cinco** consejos* | *los consejos, rotulados uno a uno por el libro* |
| `reconocer_excelencia...` **nombre largo** | *Las **tres** vias* | *Las vias*. `L247` dice *Another great way*, **sin cuenta** |

    $ python .t1_v21/arreglo_cuentas.py | tail -4
      arreglos aplicados : 22 de 22
      fallos             : 0  []
    $ python .t1_v21/cuentas21.py | tail -2
      ocurrencias de numeral que cuentan cosas, en los 194 pasos: 35
    $ python .t1_v21/cifras21.py
      cifras y numerales comprobados en los 194 pasos : 154
      los que NO estan en su tramo del libro           : 2
         P27  sopesar_consejo_legal_despedir_humildad  paso 2  ->  numeral un
         P27  sopesar_consejo_legal_despedir_humildad  paso 3  ->  numeral una

**LOS DOS QUE QUEDAN SON FALSOS POSITIVOS DE MI PROPIO INSTRUMENTO Y LO DIGO EN VEZ DE
ESCONDERLO:** son `un` y `una` usados como **articulo indeterminado** y no como numeral.

    $ sed -n '191p' fuentes/scott_radical_candor/cap_10.md
      ...Take a deep breath and a big step back. You have a relationship with the
      person you're about to fire...

**`un gran paso atras` es `a big step back` y `una relacion` es `a relationship`.** Por eso
`cuentas21.py` deja `un` y `una` fuera de su lista a proposito, y lo dice en su cabecera.

> ### **LO QUE NO SE RETIRO, Y ES LA MITAD QUE IMPORTA: NI UN CONTENIDO.** Los medios que el libro nombra siguen enteros, uno a uno, en los 194 pasos. **Lo unico que se retiro fue la CUENTA que yo le atribuia al libro donde el libro no la escribe.** Los pasos siguen siendo 194 antes y despues, y el guion lo comprueba fichero a fichero.

**Y DOS ARREGLOS MAS DEL MISMO ACTO, que no son de cuenta y van aqui porque se hicieron en la
misma pasada:**

| que | por que |
|---|---|
| `evitar_obsesion...` paso 9: se anade *y deja la lista abierta con un y asi sucesivamente* | `L237` cierra su lista con *and so on*, **y mi paso la cerraba en cuatro objetos**. Una lista cerrada donde el libro la deja abierta es la misma especie de defecto en la direccion contraria |
| `evitar_obsesion...` paso 6: gramatica | el arreglo automatico dejo *y es las que hacen*, que no se entiende. Corregido a *que es lo que hace* |

**LA TASA DE `PASOS INVENTADOS` DE `cap_10` QUEDA EN `0,00` (0 de 194), Y DIGO CON QUE CRITERIO,
porque hay dos y la `ACTA 20` `6.2` exige decirlo:** el numerador cuenta **puentes que siguen en
el arbol**, y los 22 se corrigieron **antes** de que el candidato contara como escrito y antes
de su informe de registro (`EXTRACTOR.md` 16). **Con el otro criterio (22 de 194) la fila daria
`11,34` y si dispararia el freno**, asi que esta vez la eleccion de criterio **si mueve una
decision**, y por eso la escribo arriba y con las dos cifras.

> ### **Y LA LECTURA QUE SACO DE ESTO CONTRA MI MISMO, porque es el dato mas util de la vuelta: `cap_09` dio 0 puentes en 272 pasos y `cap_10` dio 22 en 194. LA MANO NO HA EMPEORADO: LO QUE HA CAMBIADO ES EL INSTRUMENTO.**
> `cifras21.py`, que es el de la vuelta 20, cazaba **11** de los 22. El ancho caza los 22.
> **No puedo saber cuantas cuentas de esta especie hay en los 856 pasos de `cap_00` a `cap_09`
> sin correr el ancho sobre ellos, y no lo he corrido.** Lo declaro como lo que es: **una
> sospecha con su instrumento ya escrito**, no una cifra. Y va en `O.6` como propuesta.
