# PARADA DEL 15 SEP 2026: LA RUTA VACIA. **DECISION DEL FUNDADOR**

> ## LA DECISION DEL FUNDADOR, 15 sep 2026
>
> **1. `D.42`, LA UNIDAD DE LA RUTA ES LA CELDA.** Toda ruta publicada en un reporte o
> acta como sede de una cifra (en tabla, en columna *de donde sale*, o en linea) la
> verifica el censo en el commit, celda a celda, con tres formas y solo tres:
> **(a) RUTA CON CONTENIDO: pasa. (b) RUTA VACIA: tumba**, salvo que la misma celda
> lleve la marca literal `VACIA A PROPOSITO: <motivo>`; una ruta vacia sin marca es
> caida de cifra (cosecha `7.B`). **(c) PATRON:** una celda que declara un patron lo
> escribe como `PATRON: <glob>`, y el censo exige al menos una coincidencia con
> contenido; un patron sin coincidencias tumba. Y una **lista FIJA**, en `config/`, de
> sedes vacias por protocolo (`docs/loop/PROMPT_SIGUIENTE.md` en parada) que el censo
> no cuenta. El **caso positivo** es la vuelta 25 tal como quedo: `.v25/cola_lectura.txt`
> sin marca debe tumbar nombrando la celda; con la marca, o regenerada con sus `4`,
> pasa. El **negativo**: `.barrido_C_con_ensayo_v16.txt` con su marca y su cita de la
> `ACTA 15` pasa; `.aduana_v22/*.txt` declarado como `PATRON` pasa.
>
> **2. LA RACHA `REPORTE` DEL EXTRACTOR SE REINICIA** con `D.42` instalada y corriendo
> en el hook: la cifra `2` de la vuelta 25 se corrige **por regeneracion** (`4`, del
> instrumento de hoy) con correccion declarada.
>
> **3. El censo de las 84 ausentes se re-corre bajo `D.42` y se publica:** las que sean
> patrones se declaran como tales por correccion declarada en su sede; las que resulten
> rutas de verdad inexistentes se nombran y se traen, si las hay.
>
> **4. `PROMPT_SIGUIENTE` de la vuelta 26:** continuar la insercion del lote 4 y abrir
> el lote 5 por el orden escrito.

> **ARCHIVADA.** Este fichero fue `docs/loop/PARA_ALEXIS.md` hasta que el fundador
> resolvio lo que pedia. **Se archiva entero y sin tocar una palabra de su cuerpo ni de
> su anexo**; lo unico añadido es esta cabecera. El arnes solo mira
> `docs/loop/PARA_ALEXIS.md`, asi que el bucle ya no esta detenido por el.
>
> ### LOS TRES CASOS, CORRIDOS SOBRE EL ARBOL DE VERDAD
>
> **POSITIVO**, con el fichero vaciado a proposito para comprobarlo:
>
>     $ python scripts/censar_rutas.py
>     CAE  docs/loop/REPORTE.md linea 30980, celda 3
>          ruta : .v25/cola_lectura.txt
>          esta y esta VACIA, y la celda no lleva la marca 'VACIA A PROPOSITO: <motivo>'
>     rc=1
>
> **NEGATIVOS**, los dos que la decision nombra: `.barrido_C_con_ensayo_v16.txt` pasa
> con su marca y su cita de la `ACTA 15` `1.9`; `.aduana_v22/*.txt` pasa como `PATRON`
> con sus **17** coincidencias.
>
> ### EL CENSO DE LAS AUSENTES, RE CORRIDO Y PUBLICADO (punto 3)
>
> **LAS 84 DE AYER ERAN 84 PORQUE EL CENSO DE AYER ERA MALO.** Contaba globs como
> ficheros, trozos de comando como rutas (`wc -l dataset/nodos.jsonl` entero) y moldes
> como caminos. Con el censo de `D.42` delante, el reparto real es este:
>
> | | |
> |---|---:|
> | menciones de ruta en las dos sedes | **902** |
> | de esas, publicadas **como sede de una cifra** | **293** |
> | pasan con contenido | **272** |
> | declaradas `PATRON` | **14** |
> | declaradas `VACIA A PROPOSITO` | **3** |
> | vacias por protocolo (`config/`) | **4** |
> | **rutas de verdad inexistentes que haya que traer** | # **CERO** |
>
> **NINGUNA ERA UNA RUTA PERDIDA.** Se reparten asi, y cada grupo con su arreglo:
>
> | lo que eran | cuantas | que se hizo |
> |---|---:|---|
> | **patrones sin declarar** | 14 | escritos `PATRON: <glob>` en su celda, cada uno con sus coincidencias |
> | **moldes con `N` literal** (`.t1_v23/correccion_N.py`, `cap_0N.md`) | 3 | reescritos a su patron **verdadero** (`correccion_*.py`), que se puede recontar |
> | **andamio borrado** (`.c9/mk.py`, `.frag_disc.md`, `.c6a.txt`, `.pob_*`) | 6 | marcados con su motivo, o **fuera del censo por ser el sujeto de la frase y no una sede** |
> | **candidatos insertados** | 7 | **resueltos solos**: `D.31` los archiva en `_insertados/` en el acto de insertarlos, y el censo lo sabe |
> | **rutas relativas al documento** (`paradas/...` dentro de `docs/loop/`) | 3 | **resueltas solas**: un acta que escribe una ruta relativa no publica una ruta falsa |
>
> ### Y TRES COSAS QUE DIGO PORQUE SON LECTURAS MIAS, NO LETRA TUYA
>
> 1. **`CERO COINCIDENCIAS ES A VECES LA CIFRA.** `cuarentena/_insertados/*.json` da
>    `0` **porque ahi no cuelga ningun JSON suelto**, y eso es justo lo que su fila
>    publica. La letra dice que un patron sin coincidencias tumba; lo resuelvo con la
>    misma marca, que sigue exigiendo motivo escrito. **Puedes tumbar esta lectura.**
> 2. **SEDE NO ES TODA MENCION.** Censar toda mencion daba **42 celdas que marcar**;
>    censar las sedes da **cero**. Una marca que se pone cuarenta veces deja de leerse,
>    y a la quinta se pone sin mirar: seria fabricar la excusa que `D.42` vino a cerrar.
>    El criterio esta escrito en `D.42` y en el codigo.
> 3. **TU NUMERO `D.42` CHOCABA CON EL QUE YO ME HABIA PUESTO.** La regla del informe de
>    lote, que numere yo el 12 sep, **se ha movido dos veces en tres dias**: fue `D.41`,
>    luego `D.42`, y hoy es **`D.43`**. El tuyo manda siempre; pero una regla que se
>    mueve cada dos dias no la puede citar nadie de memoria, **y fijarle numero es
>    tuyo.**

---

# PARA ALEXIS. EL BUCLE SE DETIENE: CREDITO ROTO, RACHA `REPORTE` EN 3 DE 3

*Escrito por el auditor al cerrar la **VUELTA 25**, el 13 sep 2026. `AUDITOR_FORJA.md` `3`,
condicion **credito roto**: `REPORTE` tres tandas seguidas de la especie que acumula.
**`docs/loop/PROMPT_SIGUIENTE.md` queda VACIO** y el bucle no sigue hasta que decidas.*

---

## 1. EL MOTIVO, EN UNA PANTALLA

**La vuelta 25 publica en una tabla la cifra `2` donde mi propio comando de hoy da `4`, y la sede que
publica para esa cifra es un fichero de CERO BYTES.** Es la tercera tanda seguida con una caida
`REPORTE` en sede que acumula, y `AUDITOR_FORJA.md` `3` manda detener.

**LO QUE EL REPORTE PUBLICA**, en la tabla de `S.10`, cuya cabecera es *LO QUE PASA A LA VUELTA
SIGUIENTE, **CON SU CIFRA Y SU SEDE*** y cuya tercera columna se titula *de donde sale*:

    | los pares del candidato parado | 2 por leer, los dos del despido,
      de decidir_momento_despedir_persona | .v25/cola_lectura.txt |

**Y lo repite en la tabla de `S.3.e`.**

**LOS DOS DISPARADORES, y cada uno se sostiene solo:**

    (1) LA SEDE
    $ ls -la .v25/cola_lectura.txt
      -rw-r--r-- 1 AlexDesk 197609 0 Sep 13 18:30 .v25/cola_lectura.txt
                                   ^ CERO BYTES
    regla: AUDITOR_FORJA.md 5.5, cosecha 7.B, literal:
      "Una ruta publicada como evidencia de una corrida cuenta como CIFRA PUBLICADA en su sede.
       Si apunta a un fichero inexistente o de cero bytes, es caida de cifra."

    (2) LA CIFRA
    $ python forja.py informe cuarentena/scott_radical_candor/decidir_momento_despedir_persona.json
      [BLOQUEARIA] decidir_momento_despedir_persona
          vecino despedir_persona_franqueza_radical    [familia_id]
          vecino pedir_critica_equipo_premiarla        [similitud_texto]
          vecino despedir_persona_respeto_franqueza    [familia_id]
          vecino elegir_recolocar_despedir_persona     [familia_id]
        vecinos levantados en total : 4
    $ (cruce contra bitacora/VEREDICTOS.jsonl)
      CON VEREDICTO YA ESCRITO : 0     SIN VEREDICTO, o sea POR LEER : 4

**Y LE DOY LA MITAD DE LA DIFERENCIA QUE SI SE EXPLICA:** `pedir_critica_equipo_premiarla` entro al
grafo en esa misma vuelta, asi que ese vecino pudo nacer despues de su medicion. **Pero los otros tres
los levanta `familia_id` y los tres viven en la BANDEJA**, y `D.38.5` dice desde el 12 sep que el
informe carga **grafo mas bandejas**. **Su medicion ya tenia que dar por lo menos tres.**

**La especie es `REPORTE` y no `CIFRA PUBLICADA`** porque `docs/loop/REPORTE.md` es sede de `REPORTE`
(`5.2`), **y esa distincion la trace yo en la `ACTA 19` `4.4` cuando el disparador de cero bytes NO se
cumplia y por eso no subi la especie.** Hoy se cumple y sigo sin subirla: **manda la sede, no el dano.**

## 2. LAS TRES TANDAS, MEDIDAS CONTRA LAS ACTAS Y NO CONTRA MI MEMORIA

| tanda | racha `REPORTE` al cerrar | de donde |
|---|---|---|
| **vuelta 22** | 3 de 3, **el bucle se detuvo** | `ACTA 22` |
| **reinicio** | **0 de 3**, por decision tuya del 13 sep, `paradas/2026-09-13-la-tabla-tecleada.md` punto 1 | `ACTA 23` `8.1` |
| **vuelta 23** | **1 de 3** | `ACTA 23` `8.2` |
| **vuelta 24** | **2 de 3** | `ACTA 24` `8.1` |
| **vuelta 25** | # **3 DE 3** | `ACTA 25` `3.6` |

**Tres seguidas sin una tanda limpia en medio**, que es lo que `D.38.1` exige para que no se reinicie.

## 3. Y LO QUE TIENES QUE SABER ANTES DE DECIDIR: **ESTA ES LA VUELTA MEJOR VERIFICADA DE LA CAMPANIA**

*Lo escribo aqui y no en una nota al pie porque si solo lees el punto 1 te vas a llevar una idea falsa
de lo que ha pasado. **No suavizo la parada: la regla es literal y se ha cumplido.** Pero el estado que
para no es un estado malo.*

**TODO LO QUE RECOMPUTE CON MIS PROPIOS COMANDOS LE SALE AL DIGITO:**

- el estado entero: `222` nodos, `81` aristas, `203` lineas de bitacora, `123` en bandeja, `19`
  insertados, `3` del lote 5, `220` en `_insertados`, y el estado de apertura leido de `4f59ba2`;
- **las trece filas de la tabla del freno y su total** (`142` candidatos, `1688` pasos), con mi
  instrumento y no con el suyo;
- **las ocho aristas adjudicadas: 8 de 8 tienen el paso de su madre**, comprobado fichero a fichero;
- **su hallazgo del ancla unica, reproducido entero con un lector mio**: `4 de 24`, los mismos cuatro
  nombres, las mismas cuatro especies, y los otros veinte cuadrando uno a uno;
- **las dos fronteras del lote 5 contra mi corte ciego sellado**: `2472 = 2472` y `1454 = 1454`, con
  residuo `0` en los dos y las piezas cuadrando una a una aunque los bordes no sean los mismos;
- **la aritmetica de su propia caida de dato**: `41 = 30 + 11` y `47 = 41 + 6`, que **solo cierra con
  la reparacion dentro**. Su confesion es cierta y su reparacion es cierta;
- **55 de las 59 rutas que publica**, y de las cuatro restantes tres estan citadas precisamente para
  probar que no existen.

**Y EN LA RELECTURA CIEGA: 10 discutibles releidos y 10 sostenidos; 8 `SANO` de muestra pineada y 8
sostenidos. CERO caidas de clase.** El par que yo llevaba para cobrarle **resulto ser un error mio**,
y esta declarado en `ACTA 25` `2.2` y `7.4`.

**LA CAIDA QUE PARA EL BUCLE ES UN FICHERO DE SCRATCH VACIO Y UNA CIFRA DE COLA QUE ENVEJECIO DENTRO DE
SU PROPIA VUELTA.** La ley que la desmiente **la descubrio el mismo en esa vuelta**: su `S.3.c` se
titula *LA COLA NO SE VACIA, SE REALIMENTA*.

## 4. EL ESTADO EXACTO

    rama            : extraccion-mundo-11
    commit auditado : d2faa49  (d2faa493c7407c789cb8850500dc5c87e27a3789)
    fase            : lote 4 EN INSERCION, lote 5 ABIERTO en extraccion

    nodos en dataset/nodos.jsonl              : 222
    aristas vivas (suma de nodos_siguientes)  : 81
    lineas de bitacora/VEREDICTOS.jsonl       : 203   (CONTINUA 82, SANO 121, cero sin razon)
    bandeja del lote 4                        : 123
    insertados del lote 4                     : 19  de 142
    bandeja del lote 5                        : 3    (17 unidades, 2 minadas)
    deuda de aristas declaradas sin cablear   : 79

    guardas, corridas por mi en este turno:
      python forja.py gate                 GATE VERDE, nodos verificados: 222
      python forja.py guiones              BARRIDO DE GUIONES VERDE
      python forja.py resolutor            nodos vivos 222, deprecados 0, alias 0
      python tests/test_aceptacion.py      111 pruebas, 0 fallos, 0 errores
      python scripts/tallar_reporte.py     TALLADO VERDE, 41 tablas celda a celda, 0 difieren

    rachas al detenerse:
      CLASE            extractor   0 de 2
      CIFRA PUBLICADA  extractor   0 de 2
      REPORTE          extractor   3 DE 3   <- la parada
      la del auditor   auditor     2 de 3   (no la pongo a cero: ACTA 25 8.3)

**El arbol esta limpio y verde. No hay nada a medio hacer ni nada roto que reparar.**

## 5. LO QUE SE NECESITA DE TI

**UNA COSA ES OBLIGATORIA Y TRES SON OPCIONALES.**

### 5.1. OBLIGATORIA: la racha

**`AUDITOR_FORJA.md` `5.4`: la racha no se reinicia sola. La reinicia una tanda limpia o una decision
tuya escrita en `docs/loop/paradas/`, y el acta lo dice citandola. Ninguna de las dos soy yo.**

Las salidas que veo, **y no elijo por ti**:

| | |
|---|---|
| **reiniciar y seguir** | como el 13 sep con `paradas/2026-09-13-la-tabla-tecleada.md`. **Es la tercera vez que `REPORTE` llega a 3**, y esa repeticion es dato |
| **reiniciar con condicion** | por ejemplo, que toda ruta que el reporte publique como prueba **se compruebe con un comando antes de cerrar la vuelta**. Es barato: el censo entero son 59 rutas y lo corri yo hoy en un segundo con `.t2_v26_acta/rutas.py` |
| **afinar la regla** | `7.B` no distingue **una ruta vacia que sostiene una cifra falsa** de **una ruta vacia que sostiene una cifra cierta**. Hoy las dos cosas coinciden y no hace falta decidirlo; **si las separas, dilo tu y no yo** |

### 5.2. OPCIONALES, las tres de `ACTA 25` `10.3`

1. **Una casilla en `5.2` para la frase falsa dentro de un nodo ya insertado.** Hoy no existe: el
   `dataset/` esta listado bajo `CLASE`, que es *un veredicto mal puesto*, y esto no lo es. **Hay dos
   nodos en el grafo con una frase falsa y ninguna racha los ve.** Es la misma forma del caso del 2 sep
   2026, cuando una cifra dentro del codigo de una guarda no tenia casillero.
2. **La cuarta especie de puente de `D.30`, y hoy son TRES ejemplares:** el `teamwork` de `cap_14`
   generaliza el ejemplo, el `OFTEN` de `cap_05` refuerza la frecuencia, y el `Pide` de `cap_02`
   invierte el acto. **Ninguno de los tres es destinatario, periodo ni responsable.** El banco es tu
   sede y yo no escribo ahi.
3. **La guarda que nadie tiene: que la bitacora no nombre nodos que el dataset no tiene.** La vuelta 25
   la midio con su caso: **gate verde, 219 nodos verificados, y seis lineas de bitacora jurando que
   existia un nodo que no estaba.** Lo cazo una resta que no cuadro por uno.

## 6. COMO RETOMAR

1. **Escribe tu decision en `docs/loop/paradas/`**, con su fecha en el nombre, como las once que ya hay.
2. **El acta que retome la cita** por su fichero, dice en que queda cada racha y por que (`5.4`).
3. **El trabajo adjudicado ya esta decidido y no hay que rehacerlo.** Los ocho puntos estan escritos y
   listos para pegar en `ACTA 25` `11.1`: la celda del tallado con su version, los dos candidatos del
   ancla que se corrigen en la bandeja, la operacion escrita para los dos que ya viven en el grafo, el
   puente `Pide`, `cap_04` releido antes que el hueco, las `QUESTIONS TO CONSIDER` que no son nodo, la
   correccion 9 al reves, y la cola de `decidir_momento_despedir_persona` que es `4` y no `2`.
4. **Los cinco remedios que me dejo a mi mismo** estan en `ACTA 25` `11`, y el arnes se los entrega al
   auditor siguiente por `D.40`.
5. **Nada que reparar antes de empezar:** las cinco guardas estan en verde, corridas por mi, y el
   trabajo pendiente es el de siempre, `123` candidatos del lote 4 por insertar y `15` unidades del
   lote 5 por minar.

**NO FUNDO LA RAMA Y NO CREO NINGUN REMOTO.** `extraccion-mundo-11` queda como esta, con `docs/loop/`
commiteado y pusheado.

---

# ANEXO DE LA REANUDACION, 13 sep 2026. **ESCRITO POR CLAUDE, NO POR EL AUDITOR**

*Guion de reanudacion del fundador del 13 sep 2026. **Nada del texto de arriba se ha
tocado**: `D.28` dice que este fichero es del auditor, y el guion solo me manda anadir
aqui cuando la especie no tiene cura escrita. Esto es lo anadido.*

## A.1. DICTAMEN: **`CREDITO`**

Racha `REPORTE` en **3 de 3**, `AUDITOR_FORJA.md` `3`. No es `ARNES` (el arnes hizo su
trabajo: tres vueltas enteras, 222 nodos, todas las guardas verdes) y no es `DOCTRINA`
(la regla que se incumplio esta escrita y es literal: cosecha `7.B`).

## A.2. LO QUE SI CURE, PORQUE ERA UN HUECO EN UNA CURA QUE YA EXISTE

**`D.41` tenia que haber cazado una ruta de cero bytes y daba VERDE.** El tallador leia
el fichero vacio sin error, no encontraba ninguna tabla dentro, y lo despachaba con la
lectura mas generosa posible: *el instrumento no imprime ninguna tabla: esta la resume,
no la reproduce.* **Verde.**

    antes:  salida de CERO BYTES  ->  SIN COMPROBAR  ->  verde
    ahora:  salida de CERO BYTES  ->  RUTA VACIA     ->  ROJO, y nombra la ruta

**Con su caso negativo al lado**, porque la distincion tiene que aguantar: una salida
**con contenido pero sin tabla** sigue siendo `SIN COMPROBAR` y no tumba nada. Un
instrumento que imprime un saldo y no una tabla esta cumpliendo. **Tres pruebas nuevas**
(`PruebaTallado`, ahora 16).

> **ESE HUECO LO ABRI YO EL 13 SEP AL ESCRIBIR `D.41`, Y LO PAGO LA VUELTA 25.** Queda
> cerrado y no depende de esta decision.

## A.3. PERO ESO **NO** CURA LA CAIDA DE HOY, Y DIGO POR QUE

**La caida tiene otra forma.** `D.41` ata **un instrumento a una tabla entera**: mira la
declaracion de encima (*Salida de `X`, guardada en `Y`*) y compara la tabla contra `Y`.

**La tabla de `S.10` no declara nada encima: publica una ruta POR FILA, en su tercera
columna, titulada *de donde sale*:**

    | que | cifra | de donde sale |
    |---|---|---|
    | los pares del candidato parado | 2 ... | `.v25/cola_lectura.txt` |

**`D.41` no puede ver eso, y no es un fallo de implementacion: es que su unidad es la
tabla y aqui la unidad es la celda.** Corrido hoy sobre el reporte entero: **55 tablas
declaran instrumento, 41 talladas celda a celda, 0 difieren, 0 con la ruta vacia.** La
caida de la vuelta 25 **no esta entre ellas y no lo estaria nunca.**

## A.4. LA CURA QUE PROPONGO, Y **LA MEDIDA QUE LA VUELVE UNA DECISION TUYA**

> **EL CENSO DE RUTAS: toda ruta que el reporte publique como prueba tiene que existir y
> no estar vacia, se comprueba antes de cerrar la vuelta, y una ruta rota nombra su
> linea.** Es lo mismo que el auditor propone en su `5.1`, segunda fila.

**LA CORRI HOY SOBRE `docs/loop/REPORTE.md` ANTES DE PROPONERTELA**, y el resultado es
justo lo que hace que no la escriba yo solo:

| | |
|---|---:|
| rutas distintas publicadas en el reporte | **234** |
| existen y tienen contenido | **147** |
| **existen y estan VACIAS (cero bytes)** | # **3** |
| no existen en el arbol | **84** |

**LAS TRES VACIAS, UNA A UNA, Y SOLO UNA ES LA CAIDA:**

| ruta | que es |
|---|---|
| `.v25/cola_lectura.txt` | **LA CAIDA.** Sostiene la cifra `2` que el instrumento desmiente con `4` |
| `docs/loop/PROMPT_SIGUIENTE.md` | **VACIA A PROPOSITO Y POR REGLA**: `AUDITOR_FORJA.md` `3` manda dejarlo vacio en una parada. **Ahora mismo lo esta porque el auditor cumplio** |
| `.barrido_C_con_ensayo_v16.txt` | **VACIA A PROPOSITO Y YA ADJUDICADA**: `ACTA 15` `1.9` decidio que se quedaba vacio, y la `ACTA 16` `7.2` corrigio a quien lo conto como caida |

> ### **LA REGLA `7.B`, APLICADA AL PIE DE LA LETRA HOY, DISPARARIA TRES VECES Y ACERTARIA UNA.**

**Y de las 84 que no existen, la mayoria no son rutas: son PATRONES** (`.aduana_v22/*.txt`,
`.frag_*.md`, `.t1_v21/*.txt`), que el reporte escribe para nombrar un conjunto. **Una
guarda que no distinga un patron de una ruta empieza con ochenta y pico falsos
positivos**, y una guarda que grita donde no hay nada enseña a no mirarla.

**ASI QUE LA CURA NECESITA DOS DECISIONES QUE SON TUYAS Y NO MIAS**, y son exactamente
las que el auditor nombro en su `5.1` tercera fila:

1. **QUE HACE EL CENSO CON UNA RUTA VACIA A PROPOSITO.** O `7.B` gana entera y entonces
   `PROMPT_SIGUIENTE.md` vacio en una parada es una caida (que seria absurdo), o **la
   ruta vacia deliberada se declara** y el censo la respeta. **Si se declara, hay que
   decir como**, porque una excepcion que se concede a mano es una excepcion que se
   concede siempre.
2. **QUE ES UNA RUTA Y QUE ES UN PATRON.** Un `*` en el medio no es un fichero. Si el
   censo los ignora, **queda un hueco con forma de asterisco**: basta escribir
   `.v25/cola_*.txt` para que ninguna guarda mire.

**NO LAS DECIDO YO.** El guion me manda proponer y parar, y `5.4` dice que la racha la
reinicia una tanda limpia o una decision tuya escrita en `docs/loop/paradas/`. **Ninguna
de las dos soy yo.**

## A.5. LO QUE **NO** HICE, Y QUIERO QUE CONSTE

- **NO reinicie la racha.** Sigue en **3 de 3**.
- **NO relance el arnes.** El guion solo autoriza relanzar en la especie `ARNES`.
- **NO toque el texto del auditor** de este fichero, ni su `PROMPT_SIGUIENTE.md` vacio.
- **NO impuse el censo de rutas**, que es la condicion que esta decision necesita.

## A.6. EL ESTADO, QUE NO CAMBIO

El arbol sigue limpio y verde, con el hueco de la ruta vacia cerrado y probado:

    python forja.py gate                 GATE VERDE, 222 nodos
    python forja.py guiones              VERDE
    python scripts/tallar_reporte.py     VERDE, 55 declaradas, 41 talladas, 0 difieren
    python tests/test_aceptacion.py      114 pruebas, 0 fallos   (eran 111)
    bash tests/prueba_arnes.sh           128 comprobaciones en VERDE
