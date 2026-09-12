# ENCARGO DE LA VUELTA 16: LOS REGISTROS, LA PUERTA QUE FALTA, DOS CORRECCIONES EN FRIO, Y `cap_05` A `cap_07`

*Escrito por el **auditor** al cerrar la **ACTA 15** (`docs/loop/ACTA_AUDITOR.md`, la
seccion que abre con `# ACTA 15`). Sede del auditor por `AUDITOR_FORJA.md` 5.6.*

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO QUE LA ACTA 15 DEJA DECIDIDO, EN CUATRO LINEAS

- **Tu vuelta 15 sale con CERO caidas en las tres especies, y es la segunda seguida.**
  Diez discutibles marcados y ninguno cayo. **Los dos unicos choques de clase de la
  vuelta los pierde tu auditor**, y estan adjudicados contra mi en `3.1` y `3.2`.
- **El lote 3 esta cerrado e insertado entero**: 136 candidatos, 1.107 pasos, 136 en el
  grafo, cero en la bandeja. **Lo verifique yo.**
- **El volumen se queda en CUATRO capitulos por vuelta.** `cap_04` midio **6,38 por
  ciento** de pasos inventados (3 de 47, banda 1,3 a 17,5) y el tope es 10: **el freno no
  se dispara.**
- **El lote 4 sigue ABIERTO y no se inserta nada de el** (`D.39`).

---

## TAREA 1: LOS REGISTROS. **VA PRIMERA Y NO ES UN TRAMITE**

**1.a. LEE LA `ACTA 15` ENTERA**, y en particular las seis adjudicaciones de su seccion
3. **Cinco te dan la razon y una corrige a tu auditor.** Recogelas en tu reporte como
recogidas, **sin reabrirlas** salvo que encuentres un hecho nuevo, y si lo encuentras
**lo traes con su medida y no lo resuelves copiando.**

**1.b. LAS SEIS ADJUDICACIONES, PARA QUE NO HAYA QUE BUSCARLAS:**

| # | adjudicacion | donde |
|---:|---|---|
| 1 | `cuidar_persona_completa_equipo` contra `respetar_cuidar_persona_cargo` es **`SANO`**. Tu lectura se sostiene y **mi `CONTINUA` ciego cae** | `ACTA 15` 3.1 |
| 2 | contra `gestionar_personas_equipo` tambien es **`SANO`**, y **la arista propuesta es la tuya**: el hijo es `desplegar_marco_franqueza_radical`, no media dimension | `3.2` |
| 3 | **`TRANSCRIPCION DE CASO` se admite como subrayado dentro de TRANSCRIPCION**, no como tercera clase, y **no mueve el numerador**. `D.30` sigue teniendo dos casillas | `3.3` |
| 4 | **una arista madre e hijo SI puede cruzar la frontera de libro**, citando `D.1` (*vale para TODO par*), `D.19`, `D.29` y el manual (la frontera de libro esta sobre las fuentes de un nodo, no sobre sus aristas). **Con tres condiciones y una de ellas te bloquea hoy** | `3.4` |
| 5 | **la atribucion de Fred Kofman CABE en `atribuciones`**: el campo `cifra` es cadena no vacia por esquema, y el censo ya registra **30 de sus 58 filas sin ninguna cifra numerica** | `3.5` |
| 6 | **`ORDEN_DE_LOTES.md` tiene hoy tres filas falsas y una seccion superada**, y **no es caida tuya**: eran ciertas al escribirse y nadie te encargo actualizarlas | `3.6` |

**1.c. CORRIGE `docs/loop/ORDEN_DE_LOTES.md`, POR CORRECCION DECLARADA Y SIN BORRAR UNA
PALABRA** (manual principio 6, y es como se corrigio cuatro veces antes en ese mismo
fichero). **Las cuatro, con su medida remedida por ti y su fecha:**

| donde | lo que dice hoy | lo que el repo mide |
|---|---|---|
| fila del **lote 2** | *15 candidatos en `cuarentena/smart_who/`, SIN INSERTAR* | **la bandeja esta vacia** y `_insertados/smart_who/` tiene **59**, los 59 en el grafo |
| fila del **lote 3** | *Su INSERCION no [esta cerrada], y `MODO_INSERCION=cuarentena` sigue vigente* | **cerrado e insertado**: bandeja 0, archivados 136, los 136 en el grafo, y `MODO_INSERCION=insertar` desde `D.39` |
| fila del **lote 4** | *AL CIERRE DE LA VUELTA 14: 4 de 15 ficheros minados, 2 candidatos* | **5 de 15 minados** (`cap_00` a `cap_04`) y **8 candidatos** en la bandeja |
| seccion **Lo que este documento NO decide** | *cada insercion es una autorizacion del fundador que se pide con el informe delante* | **`D.39`, 11 sep 2026: la insercion de un lote cerrado ya no se pide.** `D.13` da la mas reciente |

**NO TOQUES NI EL ORDEN, NI LAS CLAVES, NI LA CUENTA DE CAPITULOS, NI LAS PALABRAS DE
ESA TABLA:** eso lo fija `D.24` y no lo elige el bucle. **Solo la columna de estado y la
seccion del final.** Y **remide antes de escribir**: que la cifra este aqui puesta no te
exime de comprobarla.

**1.d. RECOGE DOS CORRECCIONES MIAS, que van contra mi y no contra ti:**

1. **La frase *los 68 `[ENTRARIA]`* de mi `ACTA 13` y de mi parada es FALSA.** Lo cierto
   es **59 `[ENTRARIA]`, 9 `[BLOQUEARIA]`, 0 `[CAERIA]`**, y lo reproduje desde git sobre
   el grafo de 135 con los 9 pares al tercer decimal. **Tu discutible 1 tenia razon las
   dos veces que lo marcaste.**
2. **Mi apertura ciega decia que el censo de atribuciones registraba maximas sin cifra
   *de Brene Brown, Sutton, Batista y Buckingham*, como si fueran cuatro casos.** Son
   **30 de 58 filas**. Corregido en `3.5`.

---

## TAREA 2: LA PUERTA DE ENTRADA QUE FALTA, Y LAS DOS COLAS QUE NO SE PUEDEN ESCRIBIR TODAVIA

### 2.a. **LEE ESTE PAR Y, SI TU LECTURA LO SOSTIENE, ESCRIBE LA ARISTA**

*Sale de adjudicar tu discutible 8 (`ACTA 15` 2.7). **Tu argumento lo sostengo entero**:
una linea que nombra un trabajo apunta a su puerta de entrada, no a cada habitacion. **Lo
que te digo es que ese paso nombra cuatro trabajos y solo uno tiene su puerta cableada.***

    madre fijar_proceso_trabajo_equipo P7:
      Aprende a dominar los procesos que el libro nombra como importantes para un
      directivo: dirigir reuniones eficaces, blindarte contra los errores del pasado,
      planificar el maniana y cultivar una cultura sana.

    medido por mi:
      contrastar_cultura_actual_aspirada   nodos_previos: ['fijar_proceso_trabajo_equipo']
      fijar_resultado_excelente_reunion    nodos_previos: []   <- la cabeza de las cinco
                                           reuniones, viva, con sus cinco hijos y sin madre

**QUE HACER, EN ESTE ORDEN:**

1. **Lee los dos nodos enteros** y decide con la vara: **es `fijar_resultado_excelente_reunion`
   la puerta de entrada de *dirigir reuniones eficaces*, igual que el ejercicio de cultura
   lo era de *cultivar una cultura sana*?**
2. **Si si**: `python forja.py arista --madre fijar_proceso_trabajo_equipo --hijo
   fijar_resultado_excelente_reunion --paso 7 --razon "..."`, con la razon que `D.29`
   exige y **citando la linea del libro que la sostenga**, como hiciste con `cap_11.md`
   L79 para la de cultura.
3. **Si no**: escribelo con su razon y se acaba ahi. **Una arista que tu lectura no
   sostiene no se escribe porque su auditor la haya visto.**
4. **Y de los otros dos procesos que ese paso nombra** (*blindarte contra los errores del
   pasado* y *planificar el maniana*) **mide si tienen cabeza en el grafo y publica la
   medida**, en positivo o en negativo. **Yo no la he corrido y por eso no afirmo nada
   de ellos** (manual principio 7).

### 2.b. LAS DOS COLAS QUE SE DECLARAN Y NO SE ESCRIBEN, cada una en su bloque titulado (`D.29`)

| cola | por que no se escribe todavia | cuando |
|---|---|---|
| **la serie de las TRES RESPONSABILIDADES**: `revisar_ciclo_responsabilidades_relaciones` paso 3 nombra las tres, y las tres son las cabezas de `cap_05`, `cap_06` y `cap_07` | los hijos no existen: los tres capitulos no estan minados, **y el propio candidato sigue en cuarentena** | el dia que el lote 4 cierre y entre. Va bajo **`D.29`** y no `D.37`: el paso nombra y no cuenta |
| **la primera arista entre dos libros**: `gestionar_personas_equipo` paso 2 a `desplegar_marco_franqueza_radical` | **adjudicada admisible** (`3.4`), pero `D.29` exige que el hijo ya viva, y esta en cuarentena de un lote ABIERTO | idem. **No la estrenes antes** |

**LAS DOS VIVEN EN UN BLOQUE PROPIO Y TITULADO DE TU REPORTE cada vuelta hasta que se
puedan escribir**, que es lo que `D.29` manda para que una arista no se pierda en la
prosa.

---

## TAREA 3: LOS DOS ARREGLOS EN FRIO DE LA BANDEJA, QUE HOY CUESTAN LO QUE LEER

*Los dos candidatos siguen en `cuarentena/scott_radical_candor/`, o sea que tocarlos hoy
no mueve el grafo. **Los dos vuelven a pasar por la aduana despues**, uno por vez.*

**3.a. `delimitar_franqueza_radical_cinco_noes`: LE FALTA UN IMPERATIVO DEL LIBRO.**

    $ sed -n '149p' fuentes/scott_radical_candor/cap_04.md
    ... But ultimately, if it's not possible to be Radically Candid with your boss and
    your peers, I'd recommend finding a different kind of work environment if at all
    possible.

**Tus pasos 5 y 6 llevan el microcosmos y la cautela, y esa recomendacion no esta en
ningun paso.** **No es un puente: es lo contrario**, inventario del libro que el nodo no
recogio. **Ninguna regla te obliga a la exhaustividad**, asi que decide tu con la linea
delante: **o entra como paso, o escribes por que no entra.** Las dos salidas valen; la
que no vale es no mirarlo.

**3.b. `cuidar_persona_completa_equipo`: LA ATRIBUCION DE FRED KOFMAN.**

    $ sed -n '113p' fuentes/scott_radical_candor/cap_04.md
    Fred Kofman, my coach at Google, had a mantra that contradicted the "just professional"
    approach ...: "Bring your whole self to work." ...

**Tu paso 8 usa la formula y el candidato no lleva campo `atribuciones`.** El campo **cabe**
(`3.5`) y es **opcional por esquema**, asi que **no te lo impongo: lo encargo leido.** Si
entra, con sus cuatro subcampos y `fecha_corte` que diga lo que el texto da (el libro lo
presenta como *my coach at Google*, sin anio ni obra). Si no entra, **con su razon
escrita.**

**AL CERRAR LA TAREA 3:** los dos por la aduana en seco, **uno por vez**, con su informe
pegado, **y el informe del lote 4 entero recontado** (hoy: 8 candidatos, 7 `[ENTRARIA]`,
1 `[BLOQUEARIA]`, 0 `[CAERIA]`, 3 vecinos).

---

## TAREA 4: EL LOTE 4, `scott_radical_candor`. **`cap_05` A `cap_07`, Y `cap_08` SI CABE**

**EL VOLUMEN VIGENTE SON CUATRO CAPITULOS POR VUELTA** (decision del fundador 5.8, y el
freno **no** se dispara: peor capitulo 6,38 contra un tope de 10). **Y el tramo pendiente
del encargo anterior son exactamente tres**, asi que el orden es este y no otro:

| orden | fichero | unidad | palabras de cuerpo, medidas por mi |
|---:|---|---|---:|
| 1 | `cap_05.md` | `Cap. 2`, `Get, Give, and Encourage Guidance` | **8.756** |
| 2 | `cap_06.md` | `Cap. 3`, `Understand What Motivates Each Person on Your Team` | **11.587** |
| 3 | `cap_07.md` | `Cap. 4`, `Drive Results Collaboratively` | **13.678** |
| 4, solo si los tres cierran enteros y el turno aguanta | `cap_08.md` | `Cap. 5` | **6.140** |
| | | **los tres del tramo** | **34.021** |

> **LA MEDIDA QUE TU TRAJISTE Y QUE YO FIRMO: el ritmo sostenido del lote 3 fue de
> 14.008 palabras por vuelta** (70.041 en cinco vueltas, remedido por mi). **Los tres que
> te encargo son 2,43 veces ese ritmo.**
>
> **ASI QUE LA REGLA DE CORTE ES LA MISMA Y LA REPITO: cierras los que quepan ENTEROS y
> lo dices con su cifra.** Un capitulo cerrado vale mas que dos a medias y **la unidad
> atomica sigue siendo el capitulo.** Que no quepan los tres **no es un fallo tuyo ni una
> excusa: es la medida que decide el volumen del lote 5**, y esta vez ya hay una vuelta
> de datos para compararla.

**EL RESTO, COMO SIEMPRE, Y NADA DE ESTO ES OPCIONAL:**

1. **La frontera publicada ANTES de cortar**, pieza a pieza, con su `sed` pegado
   (`D.35`), y **lo que no extraes declarado uno a uno con su motivo.**
2. **La relectura de fidelidad `D.30` DENTRO del acto de escribir**, paso a paso contra
   su linea, con la marca de cada paso. **Y si usas `TRANSCRIPCION DE CASO`, va con el
   caso nombrado dentro del propio paso**, que es la condicion con la que la admiti.
3. **Un commit por capitulo.**
4. **Las cuatro medidas POR CAPITULO**, no por vuelta. **Y la de pasos inventados con su
   numerador y su denominador separados**, que es lo que me deja firmarla.
5. **Cada candidato por la aduana en el acto en que se escribe** (`EXTRACTOR.md` 16), y
   **cuidado con la regla 3 de ids**: te cazo dos veces en `cap_04` con locuciones
   adverbiales (`tras desafiar`, `hacia arriba`). **Tu propia propuesta de ejemplar esta
   recogida y sigue su curso; mientras no este resuelta, mirala dos veces.**
6. **Los candidatos del lote 4 SE QUEDAN EN CUARENTENA**, los 8 de hoy y los que
   escribas. **El lote 4 esta abierto y `D.39` solo abre la insercion de un lote
   CERRADO.** Meter uno seria caida de dato.

---

## SON CUATRO TAREAS Y EL TOPE SON CINCO

**No hay cola por tope.** Si algo se queda fuera, que sea por volumen de capitulo y con
su cifra al lado.

## LAS PARADAS

**Paras, lo declaras en TU REPORTE y te detienes si:**

- una regla de la casa te obliga a algo que rompe otra regla de la casa;
- necesitas mover un umbral, el esquema, `D.27`, `D.30`, `D.37` o la vara de continua
  contra repite;
- la TAREA 1 encuentra que una de mis seis adjudicaciones contradice una regla escrita
  **que yo no cite**;
- una lectura de `cap_05` a `cap_07` te pide fundir un nodo que ya vive en el grafo.

**TU NO ESCRIBES `docs/loop/PARA_ALEXIS.md`** (`D.28`).

**NO paras por:** que la aduana levante muchos vecinos con 203 nodos (eso es la aduana
funcionando), que los tres capitulos no quepan (se dice con su cifra), que haya lecturas
`SANO` sin sede (se cuentan y se traen: hoy son **19** con los dos ids vivos y **11**
esperando a su candidato), ni porque las dos colas de la TAREA 2 sigan sin poder
escribirse.

**Y NO FABRIQUES MAQUINARIA** (`EXTRACTOR.md` 13 y la moratoria de `5.6`). En particular:
**no inventes una sede para los `SANO` sin vecino** y **no estrenes la arista entre dos
libros antes de que su hijo viva en el grafo.**

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una
regla vigente, paras y lo traes. No adivines.**
