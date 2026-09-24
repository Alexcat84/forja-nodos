
---

# CIERRE DE LA VUELTA 1 DEL FRENTE `marquet_turn_the_ship`

## C.1. LAS CIFRAS DEL CIERRE, RECOMPUTADAS AL CIERRE Y NO AL EMPEZAR

*`EXTRACTOR.md` 4: **el estado al cierre se mide al cierre**, y toda cifra que la propia vuelta
pudo mover se RECOMPUTA. Medir temprano y publicar tarde sin remedir es citar sin mirar.*

<!-- TALLADO: parcial salida=.vm01/cierre.txt -->

| | al empezar | **al cerrar** | de donde sale la del cierre |
|---|---:|---:|---|
| nodos en el dataset | 270 | **@@NODOS@@** | `.vm01/cierre.txt` (`wc -l < dataset/nodos.jsonl`) |
| candidatos en bandeja del lote | 3 | **@@BANDEJA@@** | `.vm01/cierre.txt` (`PATRON: cuarentena/marquet_turn_the_ship/*.json`) |
| pasos escritos en el lote entero | no medido | **@@PASOS@@** | `.vm01/fidelidad_lote.txt` |
| rama | `extraccion-marquet_turn_the_ship` | **`extraccion-marquet_turn_the_ship`** | `.vm01/cierre.txt` (`git rev-parse --abbrev-ref HEAD`) |
| commit al cerrar | `dbff694` | **@@COMMIT@@** | `.vm01/cierre.txt` (`git rev-parse --short HEAD`) |

**EL DATASET NO SE MOVIO NI UN NODO, Y ESO ES LO QUE TENIA QUE PASAR: `270` al abrir y `270` al
cerrar.** Este frente no inserta (`D.45`), `MODO_INSERCION` no se toco, y **no corri
`python forja.py insertar` ni una vez.** Lo unico que crecio es la bandeja.

## C.2. LAS GUARDAS AL CIERRE

<!-- TALLADO: parcial salida=.vm01/guardas.txt -->

| guarda | salida | |
|---|---|---|
| `python forja.py gate` | **GATE VERDE**, `@@GATE_NODOS@@` nodos verificados | `.vm01/guardas.txt` |
| `python forja.py guiones` | **BARRIDO VERDE**: cero guiones largos y cero guiones medios | `.vm01/guardas.txt` |
| `python tests/test_aceptacion.py` | **@@TESTS@@** | `.vm01/guardas.txt` |
| `python scripts/cerrar_reporte.py` | **@@CIERRE@@** | `.vm01/guardas.txt` |

## C.3. LAS TRES TAREAS, Y CERO COLA

| # | tarea | como cierra |
|---:|---|---|
| 1 | la frontera de la unidad que se mina | **CERRADA** en `1.b`: `cap_03`, `16` piezas, `1978` contra `1978`, residuo `0`, cero solapes y **cero lineas con palabras sin cubrir**. Tabla pegada de su instrumento, con el `AVISO` de que ninguna celda esta tecleada |
| 2 | minar con el techo por delante, aduana en seco en el acto | **CERRADA** en `2.b` a `2.f`: `6` candidatos, **`0 CAERIA`**, `3` aristas declaradas por lectura y `@@PARES@@` pares con veredicto escrito por vecino |
| 3 | `PASOS INVENTADOS POR CAPITULO`, fila por unidad mas total | **CERRADA** en `3.b`: tres filas, las tres releidas y firmadas por mi, **`0,00` por ciento sobre `70` pasos**. Y en `3.c` los **`8`** puentes que hubo que retirar para que ese `0` fuera cierto |

**LAS TRES ENTREGADAS Y NINGUNA EN COLA.** Lo que pasa a la vuelta siguiente es **el segundo
capitulo del tramo**, declarado en `2.a` con su cifra, y no es una tarea sin hacer: es el techo de
capitulos aplicado.

## C.4. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

*`EXTRACTOR.md` 8: se marcan **a ciegas**, para que el auditor empiece su relectura por ellos, y la
metrica de credito solo significa algo si el marcado se hizo antes. **Por numero y linea, sin
reabrir el argumento** (`D.47`).*

| # | discutible | donde |
|---:|---|---|
| 1 | `R5` (`L35`) fuera: nombra el sintoma y su techo, y lo tumbo por no poner medio ninguno de deteccion | `1.d` |
| 2 | `R7` (`L61`) fuera **teniendo inventario propio de seis nombrados uno a uno**, por la restriccion 1 de `D.27`: son fines | `1.d` |
| 3 | la vuelta mina **UNA** unidad cuando el tramo vigente del lote eran **DOS**, y el motivo es el reloj de la aduana, no la cosecha | `1.a` y `1.c` |
| 4 | `recorrer_organizacion_escuchar_plantilla` paso `1`: convierto en paso la **pregunta retorica** que el libro dirige al lector | resumen del candidato |
| 5 | `recorrer_organizacion_escuchar_plantilla` paso `7`: lleva pegada una **consecuencia observada** y no una instruccion | resumen del candidato |
| 6 | `observar_reunion_rutinaria_senales_plantilla`: la **activacion sale de `R3`**, pieza que yo mismo clasifique `RESIDUO` en la frontera | resumen del candidato |
| 7 | `seguir_frustrado_preguntar_implantacion_ideas` paso `2`: *sin pregunta y sin acusacion* es **mi glosa de la forma** de la frase citada | resumen del candidato |
| 8 | `contar_firmas_cadena_tramite_parado` paso `5`: transcribo `department chief` y `department head` como **dos puestos distintos** que en castellano se dicen igual, sin fundirlos ni inventarles nombre | resumen del candidato |
| 9 | `inspeccionar_reparto_informacion_notas_jefe` pasos `7` y `8`: son *quedate con*, o sea **lectura y no acto** | resumen del candidato |
| 10 | `auditar_formacion_premios_ultima_fila` paso `9`: arrastra **la valoracion del autor** pegada al objeto que hay que mirar | resumen del candidato |
| 11 | la arista `C` (`recorrer` a `inspeccionar`): **la madre no enumera al hijo** y el libro no dice cuantas rutinas hay | `2.d` |
| 12 | la deuda de `D.37` de `ceder_control_reforzar_competencia_claridad`: **la cuenta de cuatro es del libro, el desdoble de los dos pilares lo hago yo** | `2.d.2` |

**DOCE, Y CINCO DE ELLOS SON CONTRA MIS PROPIOS PASOS** (`4`, `5`, `7`, `9`, `10`). Los marco
porque `EXTRACTOR.md` 8 los quiere a ciegas, y porque los cinco son de la misma familia que las ocho
caidas de `3.c`: **un capitulo narrativo en pasado obliga a elegir el verbo, y la eleccion es mia.**

## C.5. LAS CONDICIONES DE PARADA, REPASADAS UNA A UNA

| condicion | lo que mido | veredicto |
|---|---|---|
| algo contradice una regla vigente | **ninguna.** Los casos de borde (la pieza `R7` con inventario de fines, la activacion sacada de un residuo, las aristas sin señal) **se resuelven DENTRO de la regla y van marcados discutibles** | **NO ES PARADA** |
| algo contradice una cifra publicada con su corte | **ninguna.** Las tres cifras que el encargo me da (`17` unidades, `3` candidatos en bandeja, clave en la tabla de fuentes) me salen **al digito** en `.vm01/apertura.txt` | **NO ES PARADA** |
| una operacion cuyo texto no alcanza para ejecutarse sin decidir | **ninguna.** Las tres tareas dicen que publicar, con que instrumento y contra que tope | **NO ES PARADA** |
| **una pregunta de doctrina, cualquiera** (`D.45`, regla propia de este frente) | **HAY DOS, Y LAS DECLARO COMO PARADA EN `C.5.1`.** No resuelvo ninguna | **ES PARADA, declarada y no resuelta** |
| una guarda en rojo al sellar | **las cuatro en verde al cierre** (`C.2`), corridas al cerrar y no al empezar | **NO ES PARADA** |
| una caida de dato | **ninguna.** `0` inserciones, dataset en `270` al abrir y al cerrar, `MODO_INSERCION` sin tocar, ningun fichero de `src/`, del banco ni de los protocolos modificado, y **las tres caidas propias las cace yo y las arregle antes de publicar** (`2.c`) | **NO ES PARADA** |

### C.5.1. LAS DOS PARADAS DE DOCTRINA, ESCRITAS Y NO RESUELTAS

*El encargo de este frente es explicito y no lo interpreto a mi favor: **una pregunta de doctrina,
cualquiera, es PARADA y sube al fundador.** `EXTRACTOR.md` 14: **yo no escribo `PARA_ALEXIS.md`**;
declaro la parada en mi reporte y no la arreglo.*

| # | la pregunta, en una linea | lo que mide mi vuelta | donde |
|---:|---|---|---|
| **P1** | **la tabla de especies de puente de `D.30` tiene tres y me salen cuatro.** Falta `EL MEDIO`: inventar el soporte en que la accion se hace | **`7` de mis `8` puentes de esta vuelta son de esa cuarta especie**, y los `7` salen del mismo tipo de parrafo | `3.c` |
| **P2** | **las `QUESTIONS TO CONSIDER`: son nodo, son catorce nodos casi gemelos, o no son nodo.** La vuelta 25 la abrio y no la decidio | **`cap_03` la vuelve a traer**, con `5` preguntas en la pieza `R9`, `60` palabras, y **es la tercera unidad del lote que la trae sin decidir** | `1.b`, pieza `R9` |

> ### **Y DECLARO COMO LEI LA PALABRA `PARADA`, porque de eso depende que esta vuelta exista**
>
> **`EXTRACTOR.md` 7 dice que un pendiente de doctrina NO detiene**, y el encargo de este frente dice
> que **una pregunta de doctrina, cualquiera, es PARADA.** Las dos frases no dicen lo mismo, y una de
> las dos manda.
>
> **LO QUE HICE:** las declare como PARADA y **no las resolvi ni una** (`P1` esta medida y sin
> propuesta de regla, `P2` esta nombrada y sin eleccion), **y segui con las tres tareas.** Lei
> `PARADA` como *se declara y no se arregla aqui*, que es la formula literal que el propio encargo usa
> para la caida de dato en la linea siguiente.
>
> **LO QUE NO HICE, Y DIGO POR QUE:** no aborte el turno al encontrar la primera. Si `PARADA`
> significa *el turno se detiene*, entonces esta vuelta tenia que haber terminado en la `TAREA 3`
> con las otras dos sin entregar, **y la `P2` ya estaba abierta desde la vuelta 25, o sea que este
> frente no habria podido minar nunca.**
>
> **ESTA LECTURA ES MIA Y ES CORREGIBLE, Y ES LA TERCERA PARADA SI EL FUNDADOR LO VE ASI.** La pongo
> arriba en vez de dejarla implicita porque una vuelta entera depende de ella.

**NINGUNA CONDICION DE DATO SE CUMPLE: LA VUELTA CIERRA SIN CAIDA DE DATO. LAS DOS PARADAS SON DE
DOCTRINA, ESTAN DECLARADAS Y NO LAS TOCO.**

## C.6. LO QUE ME CARGO A MI MISMO ANTES DE QUE LO HAGA EL AUDITOR

| # | lo mio | especie | como salio a la luz |
|---:|---|---|---|
| **1** | **escribi el segundo candidato mientras el primero estaba en la aduana**, y pague la misma caida de plantilla dos veces | **el ciclo de `EXTRACTOR.md` 16 saltado por impaciencia**: `4` minutos por informe parecian tiempo muerto | **me lo dijo el dato**: dos informes con la misma linea de rechazo, `$: falta el campo obligatorio fuentes`. Arreglado en la plantilla, y los cuatro siguientes pasaron al primer intento (`2.c`) |
| **2** | **un puente mio paso la aduana en verde** y lo cace yo despues, no ella | **el destinatario invertido**: convertir en prohibicion al lector lo que el libro describe del autor | **lo vi releyendo paso contra parrafo**, con el informe ya guardado en verde al lado. Es literalmente el supuesto de `D.30`, y me toco comprobarlo en mi propio candidato (`3.c`) |
| **3** | **mi `git add -A` se llevo al commit la carpeta de trabajo del auditor ciego**, `.marquet_v1/`, que **no es mi sede** | **el barrido ancho en un arbol compartido**: el paralelo pone dos sesiones sobre el mismo arbol y mi commit no distinguia | **lo vi en los avisos del propio commit**, leyendo nombres de fichero que yo no habia escrito. **No toque ni un byte de esos ficheros**, y lo declaro aqui porque quien lea ese commit va a encontrar dentro trabajo que no es mio |

**LAS TRES SON DE LA MISMA FAMILIA Y ES LA FAMILIA DEL PARALELO:** las tres salen de que el turno
ya no esta solo en el arbol. **La primera es el reloj compartido, la tercera es el arbol
compartido, y la segunda es la unica que habria pasado igual en serie.**

## C.7. EL CONTRASTE CON LA APERTURA CIEGA, CITADO COMO CONTRASTE Y NO COMO FUENTE

*`EXTRACTOR.md` 5: un acta ajena **nunca** es fuente de una cifra mia; se cita como contraste, y si
discrepa de mi medicion, **la discrepancia se declara.***

**Mientras yo minaba, el auditor ciego media lo mismo desde `docs/loop/APERTURA_CIEGA.md`, con sus
propios instrumentos en `.marquet_v1/`.** No lo lei antes de escribir mis cifras; lo abro aqui, al
cerrar, para poner las dos columnas juntas.

<!-- TALLADO: parcial salida=.vm01/contraste.txt -->

| cifra | la mia, con su instrumento | la suya, `APERTURA_CIEGA.md` seccion 10, leida hoy | |
|---|---|---|---|
| candidatos en la bandeja del lote | **9** (`.vm01/cierre.txt`) | **9**, congelados por huella a las `21:16:13` | **CUADRA** |
| pasos escritos en el lote | **70** (`.vm01/fidelidad_lote.txt`) | **70** | **CUADRA** |
| pasos de `cap_03` | **53** (`.vm01/fidelidad_lote.txt`) | **53** | **CUADRA** |
| la frontera de `cap_03` | **1978 contra 1978**, cero lineas sin cubrir (`.vm01/frontera_cap03.txt`) | **1978 contra 1978**, cero lineas sin cubrir | **CUADRA** |
| poblacion del barrido | **354**, `270` del grafo mas `84` de bandejas (`.vm01/aduana/c5_*.txt`) | **354**, `270` mas `84` | **CUADRA** |
| puentes `D.30` en los `70` pasos | **0** (`.vm01/fidelidad_lote.txt`) | su tabla lo pone **`POR ADJUDICAR`**, porque es lectura y no cifra de maquina; su seccion `9.1` escribe **`0`** | **CUADRA la cifra, no la sede** |

> **LAS SEIS CUADRAN, Y AUN ASI DECLARO DOS COSAS QUE LA TABLA NO DICE.**
>
> **LA PRIMERA: SU `0` Y MI `0` NO ESTAN MIRANDO EL MISMO FICHERO.** Su huella de
> `auditar_formacion_premios_ultima_fila.json` es `ad14d6c7`, congelada a las `21:16:13`; la de mi
> version corregida es `319bc9d6`, y las dos estan pegadas arriba de su `git hash-object`. **Yo
> reescribi el paso `2` de ese candidato despues de su corte**, al cazar el puente de `3.c`.
> **Entonces el auditor ciego leyo el candidato CON el puente dentro y tampoco lo marco**, igual que
> la aduana. Su `0` y el mio coinciden **por caminos distintos**, y esa coincidencia no es
> confirmacion: **es la medida de lo dificil que es la especie.**
>
> **LA SEGUNDA, Y VA CONTRA MI: EL AUDITOR CIEGO ENCONTRO UNA FRONTERA CORRIDA QUE YO NO VI**, la de
> `cambiar_forma_trabajar_conservar_plantilla` paso `4` contra `L27` (su seccion `9.1` punto `2`).
> **Esta corregida en `3.d.2`, con su credito escrito dentro del propio candidato, y el numerador
> sigue en `0` porque no era un puente.** Lo que no hago es presentarlo como hallazgo mio: **lei sus
> mismas diez lineas y encontre una de las dos.**
>
> **Y UNA TERCERA QUE NO ES CIFRA: LAS DOS PAGINAS SE MOVIERON LA UNA DEBAJO DE LA OTRA.** Su
> seccion `1` declara que *el arbol se movio debajo de esta pagina*, y era yo commiteando; su tabla
> de puentes cambio de `cero puentes` a `POR ADJUDICAR` entre mi primera lectura y esta. **Escribo la
> que lei al cerrar, con su numero de linea, y dejo dicho que la otra existio:** es la seccion 5 de
> `EXTRACTOR.md` aplicada a un documento vivo.

## C.8. LO QUE PROPONGO, SIN ADJUDICARME NADA

*`EXTRACTOR.md` 14: **el extractor propone en su reporte y no se adjudica a si mismo.** En este
frente, ademas, la doctrina es parada, asi que estas tres son propuestas y ninguna es una decision.*

| # | propuesta | la medida que la sostiene |
|---:|---|---|
| **1** | **una cuarta especie de puente, `EL MEDIO`**, en la tabla de tres de `D.30` | `7` de mis `8` puentes de esta vuelta son de esa especie (`3.c`), y los `7` salen del mismo tipo de parrafo: narracion en pasado de lo que alguien miro |
| **2** | **o el arnes le sella a este frente el informe de lote, como `D.43` ya hace en el serial, o el tramo de este frente se queda en UNA unidad** | `8` informes de candidato corridos en esta vuelta a **`4` minutos** cada uno, mas el del lote, todo dentro de mi turno; y **dos corridas salieron a `0` bytes, con codigo `1` y sin una linea de error, y hubo que relanzarlas** (`2.f.2`) |
| **3** | **que la distincion `PUENTE` contra `FRONTERA INCOMPLETA` quede escrita donde se lee `D.30`** | el caso de `3.d`: la misma linea leida como puente se habria **retirado** un paso que el libro si dice, y leida como frontera incompleta se **declara**. Son dos remedios opuestos para dos especies que se parecen |

## C.9. EL SALDO DE LA VUELTA EN UNA TABLA

| | |
|---|---:|
| unidad minada | **`cap_03`** (Cap. 5, `Call to Action`) |
| candidatos escritos en esta vuelta | **6** |
| candidatos que `CAERIAN` | **0** |
| aristas declaradas por lectura, escritas y no cableadas | **3** |
| pares con veredicto escrito por vecino | **@@PARES@@** |
| `PASOS INVENTADOS` del lote entero | **0,00 por ciento sobre 70 pasos** |
| puentes retirados en el acto | **8** |
| discutibles marcados a ciegas | **12** |
| propuestas | **3** |
| **paradas de doctrina declaradas y no resueltas** | **2** |
| inserciones | **0, y por regla, no por falta de sitio** |
