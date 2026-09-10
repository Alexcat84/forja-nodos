# ENCARGO DE LA VUELTA 6. Lote 2, `smart_who`: Cap. 4 (`Select`) y Cap. 5 (`Sell`)

*Escrito por el **auditor** el 10 sep 2026 al cerrar el ACTA 5, que es su sede
(`AUDITOR_FORJA.md` 5.6). El ACTA 5 verifico la vuelta 5, **adjudico los cinco
discutibles y las cinco propuestas, los cinco discutibles SOSTENIDOS**, y **no hubo
parada**.*

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO PRIMERO, Y NO ES UNA TAREA: **TU MATERIAL SE NOMBRA POR LINEA, NO POR FICHERO**

**EL ACTA 5 ADJUDICO TU DISCUTIBLE 1 A TU FAVOR: LA UNIDAD ES EL CAPITULO Y NO EL
FICHERO** (manual 3.4, `D.13`, y el propio encargo anterior). **Acertaste, y
acertaste tambien en no parar.**

**Y ESO TIENE UNA CONSECUENCIA QUE TE AFECTA HOY:** `cap_04.md` quedo commiteado
como cerrado y **de el solo se mino L9 a L29**. Si esta vuelta empezara por
`cap_05.md`, **el Cap. 4 entero se perderia**. Por eso el encargo no nombra
ficheros. **Nombra rangos, y los midio el auditor:**

| unidad | donde vive EXACTAMENTE | palabras | bloques |
|---|---|---:|---:|
| **Cap. 4, `Select: The Four Interviews for Spotting A Players`** | **`cap_04.md` L31 a L321** mas **`cap_05.md` L9 a L361** | **12.989** | **323** |
| **Cap. 5, `Sell: The Top Five Ways to Seal the Deal`** | **`cap_05.md` L363 a L365** mas **`cap_06.md` L9 a L455** | **11.370** | |

**LAS DOS PIEZAS QUE EL AUDITOR YA ABRIO Y QUE TE AHORRAN LA BUSQUEDA:**

    cap_04.md L31  "Steve Kerr, the chief learning officer for Goldman Sachs..."
                                                      <- ABRE el Cap. 4
    cap_04.md L321 "CONDUCTING AN EFFECTIVE WHO INTERVIEW"
                                                      <- el fichero MUERE en un titulo
    cap_05.md L9   "To put the Who Interview into practice, divide a person's
                    career story into the equivalent of chapters..."
                                                      <- CONTINUA ese mismo titulo
    cap_05.md L339 "Now it is time to take the final step: selling the person on
                    actually joining your team."      <- CIERRA el Cap. 4
    cap_05.md L343 a L355  "HOW TO SELECT AN A PLAYER", recuadro de SEIS puntos.
                            ENTERO, no partido. Verificado por el auditor
    cap_05.md L359 y L361  las dos notas al pie del Cap. 4
    cap_05.md L363 "Most managers fail to sell a candidate."
                                                      <- ABRE el Cap. 5

**Si tu lectura del corte discrepa de esta tabla, MANDA TU MEDIDA y declara la
discrepancia**, como hiciste en A.4. **Esa fue la mejor pagina de la vuelta 5.**

---

## LAS COMPROBACIONES DE APERTURA, AHORA CON CUATRO LINEAS

**Una condicion medida es la que mediste tu.** Antes de leer una linea de libro, y
**su resultado va en el reporte como su propia fila, antes de la TAREA 1**:

    ls fuentes/smart_who/                          cap_01.md a cap_07.md
    python -c "import json,io; print('smart_who' in json.load(io.open('fuentes/FUENTES_CANONICAS.json',encoding='utf-8')))"
    head -8 fuentes/smart_who/cap_05.md            cabecera: unidad y titulo_textual
    grep -n '[^[:space:]]' fuentes/smart_who/cap_05.md | tail -1     <-- LA CUARTA, NUEVA

**LA CUARTA LINEA ES TU PROPUESTA C.5.3, ADJUDICADA A FAVOR** (ACTA 5, 3.8): *la
cabecera dice donde empieza el fichero, y el desajuste vive en la ultima linea.*
**Y se arregla con una linea de encargo, no con una guarda** (moratoria de
maquinaria). **Corre las cuatro sobre `cap_05.md` y sobre `cap_06.md`.**

**El auditor las midio hoy y las cuatro estan en verde.** `cap_05.md` declara
`unidad: Cap. 4`, `titulo_textual: Select: The Four Interviews for Spotting A
Players`, y su ultima linea es `Imagine putting all of that work into finding Mr.
or Ms. Right...`. **Si tu las mides en rojo, manda tu medida y paras.**

---

## EL ESTADO CONTRA EL QUE ABRES, MEDIDO POR EL AUDITOR EN `6c396ed`

| medida | cifra |
|---|---:|
| nodos vivos en el dataset | **8** (clave `estado`, valor `vivo`) |
| pasos vigentes en el grafo | **43** |
| aristas declaradas | **2 relaciones**, 4 extremos |
| veredictos en bitacora | **2**, los dos CONTINUA, los dos con razon escrita |
| **candidatos en `cuarentena/smart_who/`** | **17**, **los 17 ENTRARIAN**, **cero insertados** |
| **pasos en la bandeja de cuarentena** | **100** |
| fuentes canonicas registradas / en uso | **13** / **2** |
| capitulos del lote 2 leidos | **4 de 7**. Quedan **28.263 palabras** |
| **pares que levantarian sobre los 17** | **38 de 272**: 34 por familia, 10 por paso contra nodo, **0 por similitud** |

**Mide tu la apertura igual, antes de la primera operacion, y si discrepas manda tu
medicion y declara la discrepancia.**

---

## TAREA 1. LOS REGISTROS DEL ACTA 5

*Va primero porque un registro que no se escribe en la vuelta siguiente se pierde.
**No toca ningun dato del grafo, no pide maquinaria, y NADA de esta tarea escribe
en sede ajena.** El encargo anterior te mando escribir en `docs/BANCO_DE_REGLAS.md`
y eso fue **una caida del auditor**, declarada en el ACTA 5 seccion 4.2. **No se
repite: las tres entradas del banco van a Alexis por mano del auditor.***

### 1.a. LA CORRECCION DECLARADA, sin borrar el texto viejo

Anotala **al lado** de la tabla de la seccion 3.e del `REPORTE.md` de la vuelta 5,
sin tocarle una palabra a la fila original:

> **CORRECCION DECLARADA (auditor, ACTA 5 seccion 4.1, 10 sep 2026).** La tabla de
> 3.e publica **`L391`** como la linea del cuarto puente. **La cita *"One company we
> know was so overwhelmed... asked its researchers to screen candidates a little
> more thoroughly"* esta en `cap_03.md` L393**, verificada por el auditor con
> `grep -n "overwhelmed"` y `sed -n '393p'`. `L391` existe y dice otra cosa (*"The
> downside with researchers is that they won't qualify candidates as thoroughly as
> you might like..."*). **Las otras tres citas de la tabla (L313, L343, L383)
> reproducen exactas, el ejemplar es real, y la especie que sostiene queda
> ADJUDICADA como QUINTA especie de `D.30`.**

### 1.b. LAS TRES ARISTAS PENDIENTES, en bloque propio y titulado

**`D.29`: una arista que solo vive en la prosa de un reporte se pierde.** Van en un
bloque propio de tu reporte, esta vuelta y todas las que sigan:

1. **`aplicar_metodo_ghsmart_contratacion` es CABEZA y espera CUATRO hijos.** Tienes
   **dos entregados** (`crear_tarjeta_puntuacion_puesto` y
   `abastecer_flujo_candidatos`). **Esta vuelta le trae el TERCERO (Select) y, si
   cabe, el CUARTO (Sell).** No se cablea: **una arista se cablea contra ids que ya
   viven** y la cabeza sigue en cuarentena.
2. **`detectar_metodos_vudu_contratacion` va antes por L53, y NO SE CABLEA NUNCA.**
   Adjudicado: la arista es de despliegue, no de calendario.
3. **El Cap. 3 usa la tarjeta de puntuacion del Cap. 2 en dos de sus seis puntos**
   (`contratar_reclutadores_externos` la construye, `pedir_referencias_empleados`
   mete un resultado en ella). **Ninguna señal las levanta.** Sin cablear.

**Y lo mismo que hiciste en la vuelta 5: los hijos de esta vuelta se escriben con la
cabeza nombrada en su prosa o en sus `condiciones_activacion`**, para que el dia de
la insercion la arista se cablee por lectura.

### 1.c. LA QUINTA ESPECIE DE `D.30`, YA ADJUDICADA, PARA QUE LA USES AL ESCRIBIR

**No la registras tu en ningun sitio: la registra Alexis, y el auditor ya se la
enruto.** Lo que si haces es **buscarla expresamente**, porque el Cap. 4 va a estar
lleno de entrevistas contadas por quien las hizo:

> **EL CASO ASCENDIDO A DOCTRINA.** El libro cuenta lo que alguien **HIZO** y el
> paso lo escribe como lo que **TU** tienes que hacer. **No falta nada y no se cierra
> nada: el contenido esta entero en el parrafo y lo que cambia es el sujeto del
> verbo.**
>
> **SU DETECTOR NO ES LA AUSENCIA, ES EL EJECUTOR** (manual 4, `EXTRACTOR.md` 9):
> *la prueba de que una linea es procedimiento es que EXISTE QUIEN LO EJECUTA.*
>
> **Y SU FRONTERA, que es tu propia linea de 3.f y quedo SOSTENIDA:** si el libro
> **manda el acto** y despues enumera los **medios**, los medios son inventario y se
> transcriben **aunque los ilustre quien los usa**; si el libro **no manda nada** y
> solo cuenta lo que alguien hizo, es **caso** y se retira.

---

## TAREA 2. EL Cap. 4 ENTERO, `Select` (`cap_04.md` L31 a L321 mas `cap_05.md` L9 a L361)

**LA UNIDAD ATOMICA ES EL CAPITULO.** Frontera del Cap. 4, candidatos del Cap. 4,
relectura de fidelidad del Cap. 4, informe, **commit del Cap. 4**. Y solo entonces
el Cap. 5. **Nunca los dos juntos.**

**1. LA FRONTERA, PUBLICADA ANTES DE CORTAR.** Que hay dentro, que es procedimiento
y que no, con la prueba del inventario (`D.27`) y sus tres restricciones, y el
saldo. **Con la columna de linea y diciendo de que fichero es cada tramo**, que este
capitulo vive en dos.

**2. LOS CANDIDATOS, CON EL CICLO DE CINCO PASOS**, sin cambiar ni el orden ni una
pieza:

    1. escribes el candidato en cuarentena/smart_who/<id_propuesto>.json
    2. RELECTURA DE FIDELIDAD, con el parrafo delante:
         marcas cada paso como TRANSCRIPCION o como PUENTE
         cada PUENTE se retira o se reescribe, citando el parrafo que NO lo dice
    3. python forja.py informe cuarentena/smart_who/<id>.json
    4. si CAERIA, lo corriges y vuelves al 3
    5. solo entonces cuenta como escrito

**EL PASO 2 VA ANTES QUE EL 3 Y NO ES INTERCAMBIABLE.** La aduana no tiene el libro
delante.

**3. EL INFORME Y EL COMMIT:** `python forja.py informe --carpeta cuarentena/smart_who`,
pegas el saldo entero, y commiteas el capitulo con los JSON dentro. **El mensaje
dice el capitulo CON SU RANGO DE LINEA y cuantos candidatos**, como hiciste en
`3dd9dec` y `0a94d12`.

### LO QUE ESTE CAPITULO TIENE DE ESPECIAL, y conviene saberlo antes

**ES EL TERCER HIJO DE LA CABEZA.** Select es el paso 3 de los cuatro que
`aplicar_metodo_ghsmart_contratacion` comprime. **Ese nodo es la UNICA compresion
permitida de esa numeracion.**

**SU RECUADRO NUMERADO ESTA ENTERO EN UN SITIO, y por primera vez en el lote:**
`HOW TO SELECT AN A PLAYER`, `cap_05.md` L343 a L355, **seis puntos**. **No hay
serie partida esta vez.**

**Y AQUI ES DONDE LA QUINTA ESPECIE SE JUEGA DE VERDAD.** El Cap. 3 triplico la tasa
del Cap. 2 **no por ser mas pobre sino por tener el caso entretejido con el
mandato** (ACTA 5, 7.3). Un capitulo sobre **entrevistas** va a venir lleno de
*"un consultor nuestro hizo"*, *"un cliente nos conto"*, *"Michael Haugen dedico los
primeros diez minutos a"*. **Cuando leas una frase en tercera persona que suene a
instruccion, pregunta quien la ejecuta.**

**UN AVISO DE GUION, MEDIDO POR EL AUDITOR, QUE VALE UNA VUELTA SI NO SE DICE:**
`cap_05.md` tiene **9 guiones medios**, y uno cae **dentro del material del Cap. 4**:
la nota al pie de **L359** (`p22` guion medio `28`). **Si la transcribes tal cual,
el hook aborta el commit.** Convierte, no copies.

---

## TAREA 3. EL Cap. 5 ENTERO, `Sell` (`cap_05.md` L363 a L365 mas `cap_06.md` L9 a L455)

**Las mismas tres partes, enteras y por separado**, y **solo si el Cap. 4 quedo
cerrado con su commit dentro.**

**EL AVISO DE TRAMO, CON SU CIFRA DELANTE Y NO COMO ADORNO:**

    Cap. 4   12.989 palabras       mas del DOBLE que el Cap. 2 (6.286)
    Cap. 5   11.370 palabras
    la vuelta 24.359 palabras      mas del DOBLE que las 11.181 de la vuelta 5

**La vuelta 5 saco 15 candidatos de 11.181 palabras y eso es EXACTAMENTE el techo
del tramo** (`EXTRACTOR.md` 12.4: entre cinco y quince).

> **SI EL Cap. 4 SOLO YA LLENA EL TRAMO, EL Cap. 5 NO SE EMPIEZA. Eso no es un
> fallo: es el tramo funcionando**, y esta escrito antes de que ocurra para que no
> haya que justificarlo despues.
>
> **Y SI EL Cap. 4 SE COME LA VUELTA, LO CIERRAS ENTERO Y PARAS AHI.** Reporte
> parcial, nunca vacio, diciendo donde te quedaste. **Un capitulo cerrado vale mas
> que dos a medias**, y la razon es que **la cifra que esta vuelta existe para medir
> es POR CAPITULO**.

**Y LA ADJUDICACION 8 DEL ACTA 4, VIGENTE: el disparador NO se lee en los dos
sentidos.** Que la vuelta 5 cupiera **no autoriza a subir el tramo**.

---

## TAREA 4. LAS CUATRO MEDIDAS DEL CIERRE, DESGLOSADAS POR CAPITULO

**Las dos primeras con una fila por capitulo**, y todas **recomputadas al cierre**:

| medida | como la das |
|---|---|
| **candidatos por mil palabras** | una fila por capitulo, mas el total. **Denominador por CAPITULO**, que es el honesto, y si das tambien el de fichero **dilo al lado**, como hiciste en 4.a |
| **pasos inventados sobre pasos escritos** | **una fila por capitulo.** Es la cifra de la regla de volumen. Si un capitulo escribe cero pasos, la fila dice *sin denominador*, **no cero por ciento**. Denominador: **pasos ESCRITOS**, y el puente corregido **se cuenta**, lo retires o lo reescribas |
| **veredictos escritos** | del lote |
| **cuanto tardo y si el tramo fue el correcto** | de la vuelta, diciendo si el segundo capitulo cupo. **Y da tus dos marcas propias**: el auditor las cruza con `loop.log`, que mide el turno entero y no lo mismo que tu |

**LA TABLA DE MARCADO VA EN TU REPORTE**, paso a paso y con el parrafo citado en
cada puente, no dentro del JSON.

**LA SERIE QUE LLEVAS, para que la fila nueva se lea contra ella:**

    lote 1               36 pasos   13 puentes   36,11 por ciento
    lote 2, cap_02       16 pasos    1 puente     6,25
    lote 2, Cap. 2       35 pasos    1 puente     2,86
    lote 2, Cap. 3       53 pasos    4 puentes    7,55
    lote 2 acumulado    104 pasos    6 puentes    5,77

---

## LO QUE ESTA VUELTA TIENE QUE DEJAR MEDIDO

1. **La tasa de puentes de un capitulo NARRADO EN PRIMERA PERSONA DEL PLURAL.** El
   Cap. 2 (2,86) tenia los casos aparte; el Cap. 3 (7,55) los tenia entretejidos.
   **El Cap. 4 va a ser el mas denso en caso de los tres**: es el capitulo del
   metodo donde los autores cuentan sus propias entrevistas. **Esa fila es la que de
   verdad prueba la lectura de 7.3.**
2. **Si la quinta especie, ya nombrada ANTES de escribir, baja la cifra.** El Cap. 3
   la descubrio a posteriori. **Este la lleva en la cabeza desde el primer paso.**
   Si baja, la casa ha medido que **nombrar una especie la previene**; si no baja,
   ha medido que no. **Las dos respuestas valen y las dos hay que decirlas.**
3. **Si un capitulo de 12.989 palabras cabe en una vuelta.** La vuelta 5 contesto
   por 11.181. **Esta lo lleva un 16 por ciento mas lejos.**
4. **Cuantos vecinos levanta la aduana con TRES series hermanas en la bandeja.** Al
   cierre de la vuelta 5 eran **38 de 272**. Con los hijos del Cap. 4 dentro, **lo
   mides con `src.aduana.medir` y lo das con su tabla**, como en 3.i. **Y si vuelves
   a encontrar un par que solo ve la señal 3, dilo: llevas cuatro y son el ejemplar
   vivo de por que se paga la cola falsa.**

---

## LO QUE EL AUDITOR TE PIDE QUE NO REPITAS, y es una escalada, no un consejo

**CINCO VUELTAS SEGUIDAS FALLANDO EN LO QUE RODEA AL DATO, Y NI UNA EN EL DATO:**

| vuelta | donde cayo |
|---|---|
| 1 | la lectura |
| 2 | la aritmetica de acompañamiento |
| 3 | el recuento de acompañamiento |
| 4 | una señal medida antes de una correccion y publicada despues |
| **5** | **un puntero de linea: `L391` publicado donde la cita esta en `L393`** |

**LA BUENA NOTICIA PRIMERO, porque te la ganaste:** el remedio de la vuelta 4
(*remedir al cierre lo que la propia vuelta pudo mover*) **lo aplicaste y funciono**.
Tu 3.i remidio los vecinos sobre los 17, cazo tu propia generalizacion de 2.h y la
corrigio sin borrar la vieja. **Eso es exactamente lo que se te pidio y lo hiciste
dentro de la misma vuelta.**

**EL REMEDIO DE ESTA ES SU GEMELO, PARA LAS CITAS:**

> **UNA CITA DE LINEA SE REABRE ANTES DE PUBLICARSE.** No se escribe de memoria ni
> se arrastra de un borrador: **antes de teclear `L<n>` en el reporte, se corre
> `sed -n '<n>p'` sobre el fichero y se mira que la frase esta ahi.** `EXTRACTOR.md`
> 4 se titula *la cita lleva su linea* justamente porque **la linea ES la prueba**;
> una linea que no entrega su prueba es una ruta rota (cosecha 7.B).

**Esto es una linea de disciplina, no un programa. NO escribas una guarda para
esto** (moratoria de maquinaria, `EXTRACTOR.md` 13).

**Y EL AVISO DE CREDITO, CON SU CIFRA, QUE ES LO QUE LO VUELVE ACCIONABLE:**

    CLASE                  0 de 2 tandas seguidas
    CIFRA PUBLICADA        0 de 2 tandas seguidas
    REPORTE que acumula    1 de 3 tandas seguidas   <-- esta vuelta lo puso en 1

**Una cifra falsa en TABLA, CABECERA o CONCLUSION en la vuelta 6 y en la 7 para el
bucle.** En prosa de acompañamiento o en lista de rutas, no acumula. **La diferencia
esta en donde la pones, asi que ponla donde puedas defenderla.**

---

## UNA LINEA DE CRITERIO QUE EL ACTA 5 DEJA ESCRITA, y que sale de tus dos capitulos

**En el Cap. 2 recortaste por prudencia tres particulares de un caso** (las razones
de Washington de L61) **y en el Cap. 3 conservaste uno** (los 5.000 dolares de
L357). **Las dos decisiones quedaron SOSTENIDAS**, pero el criterio no estaba
dicho. **Lo dice el auditor ahora:**

> **UN PARTICULAR DE UN CASO ENTRA EN UN PASO SOLO SI (a) EL LIBRO LO MANDA FUERA
> DEL CASO, Y (b) EL PASO LO ATRIBUYE EN SU PROPIO TEXTO.** Si falta cualquiera de
> las dos, se va al `resumen_teorico` con su dueño delante.

**No es doctrina nueva:** es el manual 3.5 (*el caso no es la casa*, y un dato del
caso dentro de la doctrina es la señal barata de que el caso se metio donde no era)
mas `D.30`.

---

## LAS PARADAS

**Paras, lo declaras en TU REPORTE y te detienes si:**

- **alguna de las cuatro comprobaciones de apertura falla.** **Manda tu medida, no
  este parrafo**;
- una regla de la casa te obliga a algo que rompe otra regla de la casa **y no hay
  arbitro escrito**. *(Si lo hay, como en tu 1.b de la vuelta 5, no es parada: se
  cita el arbitro y se sigue. Lo hiciste bien.)*;
- necesitas mover un umbral, una regla de id, el esquema, **la prueba del inventario
  (`D.27`)**, **`D.30`** o la vara de continua contra repite. **Ninguna vuelta mueve
  nada de eso.** *(Y en particular: si una lectura te pide meter el antipatron
  dentro de `D.27`, eso es ensanchar la prueba y es parada. El ACTA 5 lo dejo como
  ejemplar medido, no como pendiente.)*;
- **el MATERIAL DE LA VUELTA no da ni un procedimiento.** **La parada es por VUELTA,
  no por capitulo.** Un capitulo de cero es un resultado medido y se publica con su
  frontera entera. **Si los DOS capitulos dan cero, ahi si paras.**

**TU NO ESCRIBES `docs/loop/PARA_ALEXIS.md`** (`D.28`). Eso lo hace el auditor, y
solo el. **Y un encargo asigna trabajo, NO MUEVE UNA SEDE:** si alguna linea de este
encargo te mandara escribir en `dataset/`, `bitacora/`, `censos/`, `config/` o
`docs/BANCO_DE_REGLAS.md`, **no lo hagas, tallalo y proponlo**, exactamente como
hiciste en la vuelta 5. **Tenias razon y quedo adjudicado.**

**NO paras por:** que un candidato caiga en la aduana (lo corriges y pegas la
salida), que un capitulo de pocos nodos (se dice con su razon), que el tramo no se
llene, ni porque la relectura de fidelidad te obligue a retirar pasos que acabas de
escribir. **Eso ultimo es la regla funcionando antes de que el dato entre, y en la
vuelta 5 funciono cinco veces.**

**NO INSERTAS NADA.** El arnes arranca en `MODO_INSERCION=cuarentena` y **la
insercion es una autorizacion del fundador, no un default** (`D.26`). Los 17
candidatos siguen esperando, y **eso no bloquea esta vuelta** (`D.32`).

**Y NO FABRICAS MAQUINARIA** (`EXTRACTOR.md` 13). Ni arneses, ni guardas, ni
lectores. **En particular: no propongas una guarda que automatice la relectura de
fidelidad** (el texto fuente no esta en el repo y una guarda sin el libro no puede
juzgar fidelidad al libro, `D.30`), **ni una que compruebe la ultima linea del
fichero** (es una linea de encargo y ya esta puesta arriba).

---

**MARCA TUS DISCUTIBLES ANTES DE SABER SI ACIERTAS**, ordenados por lo que
costarian si fallas. **Los cinco de la vuelta 5 se sostuvieron los cinco, y el
primero cambio el encargo de hoy.** Una duda marcada a tiempo vale mas que un
acierto callado.

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice
una regla vigente, paras y lo traes. No adivines.**
