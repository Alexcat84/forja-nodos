
---

## 5. **EL BARRIDO `D.38.4`, CORRIDO ENTERO POR MI HOY**: la seccion que mi apertura sellada no alcanzo

*`D.38.4`: el barrido del auditor se hace sobre **grafo mas bandejas**, descartando `_insertados` y
`_derivadas`. Lo corro con **el medidor de la casa** (`src.aduana.medir`) y **los umbrales que carga
la casa**, que es lo que `D.38.3` exige: cifra con instrumento al lado.*

    $ python .aud_v21/barrido_uno.py <cada uno de los trece>
      poblacion 299 = 203 grafo + 96 bandejas
      (descartados _insertados, _derivadas y el catalogo de control ensayo_referencia_163,
       que no tiene clave en la tabla canonica)

**`299` ES LA MISMA POBLACION QUE EL INFORME DE LA ADUANA PUBLICA EN LOS TRECE**, y ese es el punto
entero de `D.38.5`: **mi barrido y la maquina ya miden la misma poblacion, asi que las cifras son
comparables y una discrepancia seria de verdad.**

| candidato | pasos | **vecinos que MI barrido levanta** | **el informe de la aduana** | |
|---|---:|---|---|---|
| `admitir_pronto_mal_desempenio_cuatro_razones` | 9 | **2**: `sopesar_consejo_legal` `sim 0,374`; `trazar_plan_dieciocho` `sim 0,356` | 2, los mismos | **igual** |
| `armar_plan_anual_crecimiento_equipo` | 29 | **1**: `disenar_equipo_plan_anual` `fam 0,500` | 1, el mismo | **igual** |
| `calibrar_ascensos_evitar_politica` | 19 | **1**: `evitar_obsesion_ascenso_estatus` `fam 0,333` | 1, el mismo | **igual** |
| `calibrar_decision_despido_documentarla` | 13 | **1**: `sopesar_consejo_legal` `sim 0,362` | 1, el mismo | **igual** |
| `contactar_despedido_mes_despues` | 6 | **0** | 0 | **igual** |
| `conversar_historia_vida_descubrir_motivadores` | 15 | **0** | 0 | **igual** |
| `conversar_suenios_cruzar_habilidades` | 15 | **0** | 0 | **igual** |
| `evitar_obsesion_ascenso_estatus` | 10 | **1**: `calibrar_ascensos` `fam 0,333` | 1, el mismo | **igual** |
| `facilitar_despido_tres_cosas` | 11 | **0** | 0 | **igual** |
| `montar_proceso_contratacion_reducir_sesgo` | 32 | **0** | 0 | **igual** |
| `reconocer_excelencia_trayectoria_gradual` | 13 | **0** | 0 | **igual** |
| `sopesar_consejo_legal_despedir_humildad` | 8 | **2**: `calibrar_decision` `sim 0,367`; `admitir_pronto` `sim 0,365` | 2, los mismos | **igual** |
| `trazar_plan_dieciocho_meses_aprendizaje` | 14 | **1**: `calibrar_decision` `sim 0,371` | 1, el mismo | **igual** |
| | **194** | # **9 filas, 6 pares distintos** | **9 filas, 6 pares** | **REPRODUCE ENTERO** |

> ### **MI BARRIDO SOBRE LOS `299` NO LEVANTA NI UN VECINO QUE EL SUYO NO LEVANTARA, NI DEJA DE LEVANTAR NINGUNO.** `3.874` medidas, `7.118,6` segundos de instrumento. **El saldo de la aduana de la vuelta 21 queda verificado desde fuera, con otro guion y otro recorrido de la poblacion.**

### 5.1. **LO QUE EL BARRIDO ANADE, Y ES LO QUE UN INFORME NO IMPRIME: LOS QUE SE QUEDAN JUSTO DEBAJO**

*Mi guion imprime, ademas de los que pasan, **los cinco mas altos aunque no pasen**. Eso es lo que
convierte un barrido en una medida de `D.19` y no en una repeticion del informe.*

| la vecindad | quien la vio | `similitud_texto` | umbral | |
|---|---|---:|---:|---|
| `armar_plan_anual` contra `calibrar_ascensos`, **el mismo procedimiento escrito dos veces por el libro** (`L119` contra `L213` mas `L217`) | **mi lectura ciega**, apertura `3.1` | **0,237** | 0,35 | **invisible** |
| `reconocer_excelencia` contra `reconocer_recompensar_gente_estable`, **el par que el fundador eligio a mano** | la lectura del fundador | **0,257** | 0,35 | **invisible** |
| `evitar_obsesion` contra `reconocer_excelencia`, **los dos nodos del mismo tramo** | la `ACTA 20` `4.3` | **0,343** y `0,348` | 0,35 | **invisible por 7 milesimas** |
| `trazar_plan_dieciocho` contra `calibrar_decision_despido`, **un plan de aprendizaje contra la documentacion de un despido** | la señal, sola | **0,371** | 0,35 | **LEVANTADA, y es ruido** |

> ### **LA FILA MAS DURA DE TODA ESTA ACTA ES ESA TABLA LEIDA DE ARRIBA ABAJO: LAS TRES VECINDADES QUE UNA LECTURA ENCONTRO ESTAN POR DEBAJO DEL UMBRAL, Y LA UNICA QUE LA SEÑAL LEVANTA SOLA ES LA QUE NINGUNA LECTURA DEFIENDE.**
>
> **`D.19` ya lo decia y `EXTRACTOR.md` 11 lo llama ruido por su nombre.** Lo que esta vuelta anade
> es **un tercer ejemplar, y esta vez es mio**: la vecindad que yo lei a ciegas como la mas fuerte
> del capitulo (el mismo acto escrito en `L119` y en `L217`) mide **`0,237`**, mas bajo que el par
> de la lupa. **No pido mover ningun umbral** (`5` de mi protocolo: los umbrales son mios para
> proponer y de Alexis para cambiar de raiz, y ninguna vuelta los mueve). **Lo que hago es dejar la
> vecindad declarada por lectura, con su cifra al lado, para que no dependa de una señal que no la
> ve.**

### 5.2. **LA VECINDAD QUE YO LEI Y QUE NADIE HABIA DECLARADO, ADJUDICADA**

**`armar_plan_anual_crecimiento_equipo` (`L119`) contra `calibrar_ascensos_evitar_politica` (`L213`
y `L217`).** El libro escribe **el mismo procedimiento sobre dos objetos distintos**: confiere con
tus iguales, exigelo si eres jefe de jefes, y si la discusion se alarga que se resuelva fuera y
vuelva con una recomendacion o contigo de arbitro.

**MI VEREDICTO ES `SANO`, Y NO `CONTINUA`.** Lo que queda fuera es procedimiento **en los dos
lados** y **los entregables no se tocan**: uno produce **planes de crecimiento escritos** (casillas,
mirada de fuera, tres a cinco puntos, equidad por nivel); el otro produce **ascensos calibrados**
(preparacion con recursos humanos, orden por nivel, dormir y desayunar, comprobacion en solitario).
**Ninguno despliega al otro: comparten un acto de mecanica de reunion y nada mas.**

**Y LO DIGO CONTRA MI PROPIA APERTURA, que la llamo *mas fuerte que la de la lupa*: es mas VISIBLE
al leer, no mas fuerte al adjudicar.** Con los dos ficheros abiertos y la vara delante, **es `SANO`
y la de la lupa es `CONTINUA`.** La cifra la traigo igual porque **una vecindad leida y descartada
tambien es trabajo de auditoria**, y porque su `0,237` es la medida que sostiene `5.1`.

---

## 6. LA MUESTRA PINEADA DE LOS `SANO` (`7`)

### 6.1. LA POBLACION EN SEDE ES **CERO**, y es una medida

    $ wc -l < bitacora/VEREDICTOS.jsonl      ->  148 al abrir y 148 al cerrar la vuelta 21

**La vuelta 21 no inserto nada, asi que no escribio ni un veredicto en sede.** `7` dice que no se
inventa una muestra donde no hay poblacion.

### 6.2. LO QUE RELEO EN SU LUGAR: **LOS SIETE `SANO` QUE LA VUELTA SI EMITIO**, Y LOS RELEO TODOS

*Seis salen de la cola de lectura que la aduana levanto (`O.6.5.a`) y uno lo declara la lectura
fuera de toda señal (`O.6.5.b`). **La muestra minima de `7` seria `max(3, 20 por ciento de 7) = 3`.
Releo los siete**, que es estrictamente mas que la muestra y ademas quita el sesgo de eleccion:
donde se relee todo no hay semilla que justificar.*

| # | par | señal, remedida por mi en `5` | **mi relectura, con los dos ficheros abiertos** | |
|---:|---|---|---|---|
| 1 | `admitir_pronto` contra `sopesar_consejo_legal` | `sim 0,374` / `0,365` | **hermanas de la serie `D.37` de `L173`**, la primera y la tercera. Una admite el bajo desempenio pronto con las cuatro razones de `L179`; la otra pesa el consejo legal con la pregunta de `L193`. **Comparten cabeza y ni un acto** | **SOSTENIDO** |
| 2 | `calibrar_decision` contra `sopesar_consejo_legal` | `sim 0,367` / `0,362` | **hermanas tambien**, la segunda y la tercera. Y la frontera es fina y la compruebo: `L191` abre con *Don't get too caught up in all the HR/legal advice, **though***, **y ese `though` es del libro**: son dos actos que el libro opone a proposito | **SOSTENIDO** |
| 3 | `trazar_plan_dieciocho` contra `calibrar_decision` | `sim 0,371` / `0,349` | **el molde `asegurate de que` y nada mas.** Un plan de aprendizaje de dieciocho meses contra la documentacion de un despido: **cero actos, cero entregables comunes**. Es el ejemplar de banda media como ruido | **SOSTENIDO** |
| 4 | `admitir_pronto` contra `trazar_plan_dieciocho` | `sim 0,356` / `0,340` | **lo mismo y con el mismo molde.** Y la asimetria (`0,356` en un sentido, `0,340` en el otro) **lo dice todo sobre lo que mide esa señal aqui** | **SOSTENIDO** |
| 5 | `calibrar_ascensos` contra `evitar_obsesion` | `fam 0,333` en los dos sentidos | **comparten la clave de familia porque los dos hablan de ascensos.** Uno calibra los ascensos entre iguales **antes** de aprobarlos; el otro decide que se anuncia **cuando ya hay** ascenso. **Dos secciones distintas del libro, dos entregables** | **SOSTENIDO** |
| 6 | `armar_plan_anual` contra `disenar_equipo_plan_anual` (**Zhuo, y vive EN EL GRAFO**) | `fam 0,500` | **el unico que cruza de libro y el unico cuyo vecino ya esta dentro, asi que es el que mas caro costaria fallar.** Lei los dos enteros: el de Zhuo es **plan de PLANTILLA** (organigrama futuro, analisis de huecos, lista de puestos abiertos); el de Scott es **plan de CRECIMIENTO** (nombres en casillas, planes de tres a cinco puntos, calibracion, equidad por nivel). **Cero actos compartidos, dos entregables sin interseccion** | **SOSTENIDO** |
| 7 | `evitar_obsesion` contra `reconocer_excelencia` (**declarado por lectura, sin señal**) | `sim 0,343` / `0,348`, **ninguna lo levanta** | **los dos nodos del tramo que la `ACTA 20` `4.3` partio.** Lo que los separa es la activacion: uno se dispara **cuando HAY ascenso**, el otro **precisamente cuando NO lo hay**. **Dos activaciones opuestas no son el mismo nodo** | **SOSTENIDO** |

> ### **SIETE RELEIDOS DE SIETE. `0` CAEN. TASA `0,00`, BANDA `[0 ; 40,96]` al 95 por ciento.**
> **Y digo lo que la banda dice y lo que no:** con siete casos, **una tasa real de hasta el 41 por
> ciento seria compatible con este resultado.** Cero de siete **no demuestra** que no se este
> dejando pasar nada. Lo unico que demuestra es que **en estos siete no hay nada que se me escape
> leyendo**.

### 6.3. `D.8` SOBRE LOS `SANO` QUE SI TIENEN SEDE

    $ python (recorro bitacora/VEREDICTOS.jsonl y cuento los SANO sin campo razon)
      veredictos en sede: 148   {'CONTINUA': 79, 'SANO': 69}
      SANO: 69   sin razon escrita: 0

**CERO `SANO` SIN RAZON ESCRITA EN LOS 69 DE LA SEDE.** Y los siete de esta vuelta llevan su razon
escrita en el reporte, que es hoy su unica sede posible.

---

## 7. `PASOS INVENTADOS POR CAPITULO` (`8`), **FIRMADA POR MI Y CON EL CRITERIO YA CORREGIDO** (`4.8`)

### 7.1. LO QUE VERIFIQUE ANTES DE FIRMARLA, PUNTO POR PUNTO DE `8.3`

1. **CONTE YO LOS PASOS** de los 96 candidatos con un instrumento mio y distinto del suyo (`1.3`):
   **las nueve filas, los trece de `cap_10` uno a uno y los dos totales reproducen al digito**, con
   la fila de residuo en `0` y su lista vacia.
2. **RELEI UNA MUESTRA DE LOS PASOS MARCADOS `TRANSCRIPCION` CONTRA SU PARRAFO**, que es el error
   que esta metrica invita a cometer. **Dos lecturas y las dos mias:**
   - en la fase ciega, **los `194` pasos uno a uno contra su linea**, mas **12 con semilla `2110`**;
   - hoy, **10 mas con semilla `1209`**, sorteados sobre los `194` y leidos contra su `sed`:

         montar_proceso 12 -> L139   admitir_pronto 5 -> L177   conversar_historia_vida 3 -> L49
         conversar_historia_vida 9 -> L53   facilitar_despido 3 -> L169
         conversar_historia_vida 7 -> L51   armar_plan_anual 24 -> L119
         montar_proceso 2 -> L129   armar_plan_anual 2 -> L99   conversar_historia_vida 15 -> L59

     **`10` de `10` `TRANSCRIPCION`, `0` puentes.** **El que estuvo a punto de caer y no cayo es
     `admitir_pronto` paso 5** (*quedate ahi hasta que todos los nombres esten en las casillas de
     bajo desempenio*), que parecia una orden que el libro no da: **`L177` la da, y con estas
     palabras**, *I force them to sit there until everyone has put names in the underperforming
     boxes.* **Lo leí entero antes de firmarlo.**
   - **`22` pasos de `194` leidos uno a uno entre las dos muestras, el `11,3` por ciento**, sobre
     los `194` ya leidos enteros en la fase ciega.
3. **EL REPORTE SI DESGLOSA POR CAPITULO** (`O.6.3`), asi que **no hay caida de `8.3` punto 3.**
4. **Y COMPROBE QUE LAS 22 CORRECCIONES SON REALES Y NO PERDIERON CONTENIDO** (`1.4`): abri los 17
   pasos y las 5 denominaciones; **ninguna cuenta atribuida queda**, los medios que el libro nombra
   siguen enteros, y los pasos siguen siendo `194` antes y despues.

### 7.2. **LA TABLA, CON EL NUMERADOR CORREGIDO POR `4.8`**

| unidad | rotulo | cuerpo | candidatos | numerador | denominador | **tasa** | quien la firma |
|---|---|---:|---:|---:|---:|---:|---|
| `cap_00` | `Copyright Page` | 218 | 0 | 0 | 0 | **sin definir** | denominador **mio** |
| `cap_01` | `Preface` | 2.846 | 1 | **0** | **9** | **0,00** | denominador **mio**; numerador **sin medir con el instrumento ancho** |
| `cap_02` | `Introduction` | 3.908 | 0 | 0 | 0 | **sin definir** | denominador **mio** |
| `cap_03` | `How to Use This Book` | 627 | 1 | **0** | **7** | **0,00** | denominador **mio**; numerador **sin medir con el ancho** |
| `cap_04` | `Cap. 1` | 6.263 | 6 | **3** | **48** | **6,25** | denominador **mio**; **numerador heredado, lo cito y no lo firmo** |
| `cap_05` | `Cap. 2` | 8.756 | 8 | **2** | **76** | **2,63** | denominador **mio**; numerador heredado |
| `cap_06` | `Cap. 3` | 11.587 | 10 | **0** | **117** | **0,00** | denominador **mio**; numerador **sin medir con el ancho** |
| `cap_07` | `Cap. 4` | 13.678 | 25 | **0** | **225** | **0,00** | denominador **mio**; numerador **sin medir con el ancho** |
| `cap_08` | `Cap. 5` | 6.140 | 12 | **0** | **102** | **0,00** | denominador **mio**; numerador **sin medir con el ancho** |
| `cap_09` | `Cap. 6` | 17.482 | 20 | # **1** | **272** | # **0,37** | **corregido por `4.8`**: el puente que la vuelta 20 cazo y corrigio **cuenta**. La cifra `1` la cito de su reporte, **el criterio lo firmo yo** |
| **`cap_10`** | **`Cap. 7`** | **8.976** | **13** | # **17** | **194** | # **8,76** | # **NUMERADOR Y DENOMINADOR LOS FIRMO YO** |
| | **lote 4 hasta `cap_10`** | **80.481** | **96** | **23** | **1050** | **2,19** | **INCOMPLETO, y lo digo: siete filas no se han medido con el instrumento ancho** |

**COMO SALE EL `17` DE `cap_10`, Y POR QUE NO ES `22` NI `0`:**

| | |
|---|---|
| el reporte retiro **22** cuentas atribuidas | `O.3.d` |
| de esas 22, **5 vivian en `titulo` y en `denominaciones.nombre_largo`**, que **no son pasos** | comprobado por mi abriendo los tres ficheros (`1.4`) |
| **el denominador de esta metrica son los PASOS** (`8`) | asi que las 5 no entran |
| **quedan `17`** | **`17 / 194 = 8,76` por ciento** |

> ### **LA CIFRA DEL PROPIO REPORTE (`22 de 194 = 11,34`) TIENE EL NUMERADOR FUERA DEL ALCANCE DE SU DENOMINADOR, Y LA DIFERENCIA NO ES COSMETICA: `11,34` PASA EL TOPE DE `10` Y `8,76` NO.**
>
> **Y LA FRONTERA LA DIGO ENTERA EN VEZ DE ESCONDERLA:** hay un decimoctavo candidato a puente, el
> **paso 9 de `evitar_obsesion`**, que **cerraba en cuatro objetos una lista que `L237` deja abierta
> con `and so on`**. El reporte lo declara aparte por no ser de cuenta. **Con el dentro serian `18
> de 194 = 9,28`, que sigue por debajo del tope de `10`.** **Publico las dos y el freno no se
> dispara con ninguna.**

### 7.3. **LA ESCALADA, DECIDIDA SOBRE LA PEOR FILA** (`8.2`)

    PEOR UNIDAD (la que decide): cap_10 con 8,76 contra tope 10     (antes era cap_04 con 6,25)

| lo que `8.1` pregunta | la cifra de hoy | la salida |
|---|---|---|
| **sube por encima del 10 por ciento?** | **NO**: `8,76`, o `9,28` con el decimoctavo dentro | **el tramo NO baja un escalon** |
| **se mantiene o baja respecto al anterior?** | **NO, sube** de `0,37` (`cap_09`) a `8,76` | **no se gana un capitulo mas** |
| | | # **EL TRAMO SE QUEDA EN TRES CAPITULOS** |

> ### **Y LA LECTURA QUE SACO DE LA FILA, QUE ES PARA LO QUE ESTA LA METRICA: `cap_10` NO ES PEOR PORQUE LA MANO HAYA EMPEORADO. ES PEOR PORQUE EL INSTRUMENTO QUE LA MIDE SE ENSANCHO EN ESTA MISMA VUELTA.**
> El estrecho (`cifras21.py`, el de la vuelta 20) cazaba **11** de las 22; el ancho
> (`cuentas21.py`, escrito hoy) caza las **22**. **Las siete filas que hoy marco `sin medir con el
> ancho` se midieron todas con el estrecho**, y por eso el total del lote (`2,19`) **es un suelo y
> no una medida**. La tarea que lo cierra va encargada, y es la `PROPUESTA 1` del propio extractor.
