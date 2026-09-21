# DECISION DEL FUNDADOR, 17 SEP 2026: **LA TABLA DE CIERRE SALE DE UN INSTRUMENTO**

*Archivo de `docs/loop/PARA_ALEXIS.md` de la linea serial, escrito por el auditor al
cerrar la `ACTA 34` sobre la vuelta 35. **La decision va arriba, literal. El cuerpo de la
parada va debajo sin tocar una coma.***

---

## LA DECISION, LITERAL

> SESION DE CHAT en forja-nodos. Commitea y pushea lo pendiente en la
> rama activa antes de tocar nada. DECISION DEL FUNDADOR (17 sep 2026)
> sobre la parada de la vuelta 35. Archivala en
> docs/loop/paradas/2026-09-17-la-tabla-de-cierre-DECISION.md con esto
> literal, aplicala y relanza el principal:
>
> 1. EXCEPCION EXPRESA A D.45, ACOTADA: la moratoria de maquinaria no
>    cubre la cura de una especie de credito con tres tandas medidas. Se
>    autoriza construir, SOLO en la linea serial, el remedio que el
>    auditor propuso: LA TABLA DE CIERRE DE TAREAS SALE DE UN
>    INSTRUMENTO, como ya salen las de apertura y estado, con su fichero
>    de salida declarado para que D.41 la vea. Limites de la excepcion:
>    toca unicamente scripts/ y el hook de la rama de insercion, NO toca
>    el banco, ni los protocolos, ni orquestador_forja.sh, ni nada que
>    grove edite; grove sigue intacto y su cosecha no debe conflictuar.
>    Caso positivo: la tabla de la vuelta 35 tal como quedo debe caer
>    nombrando la fila del 15 de 15; regenerada, pasa.
> 2. LA RACHA REPORTE DE LA LINEA SERIAL SE REINICIA, con la condicion de
>    que el remedio del punto 1 quede construido y corriendo en el hook
>    ANTES de abrir la vuelta 36. Y al banco, D.52: TODA TABLA DEL
>    REPORTE DECLARA SU INSTRUMENTO; una tabla sin instrumento declarado
>    no se publica, porque es precisamente la que ninguna guarda mira.
>    Las tres caidas de la racha son su ejemplar: las tres en la misma
>    tabla, y ninguna cazable por diseño.
> 3. LA EXENCION DEL CENSO, concedida y acotada: APERTURA_CIEGA.md queda
>    exento SOLO mientras la fase ciega esta abierta (se esta escribiendo:
>    es ruido, no dato), con el mismo tratamiento que los cuatro ficheros
>    que D.34.2 retira. Fuera de la fase ciega SIGUE siendo sede leida por
>    el censo y el tallado, como ya esta decidido: la exencion es de
>    momento, no de fichero.
> 4. PREGUNTA 7, decidida, porque es dato y no forma: UN PASO RETIRADO POR
>    DECLARACION SE RETIRA DEL CAMPO. Un nodo insertado cuyo
>    resumen_teorico declara retirado un paso que sigue literal en
>    pasos_accionables publica un puente a quien lee los pasos. Mide
>    primero cuantos nodos estan en ese caso y nombralos; despues
>    corrigelos en el campo con correccion declarada (el paso sale de
>    pasos_accionables y su retirada queda escrita con su cita), y deja
>    la regla en el banco para que un retiro futuro se aplique en el
>    mismo acto, no solo en la prosa. Es reparacion de dato: entra bajo
>    la misma excepcion del punto 1.
> 5. Escribe el PROMPT_SIGUIENTE de la vuelta 36 con cap_10 entero y sus
>    14 candidatos sin partir, tras el remedio y la reparacion. Relanza
>    el principal. Grove sigue vivo: no lo toques.

---

## LO QUE SE APLICO, Y DONDE QUEDO CADA COSA

| punto | donde vive ahora |
|---|---|
| **1. la tabla sale de un instrumento** | **`scripts/tabla_de_cierre.py`**, y su fichero de salida es `docs/loop/TABLA_DE_CIERRE.txt`, declarado en el reporte con su marca de tallado |
| **corriendo en el hook** | dentro de **`scripts/cerrar_reporte.py`**, que es lo que el hook llama. **`hooks/pre-commit` NO se toco**: un fichero que esta sesion no mueve es un fichero que la cosecha de `grove` no puede encontrar en conflicto |
| **2. la racha reiniciada** | suceso `reinicio` en `docs/loop/CREDITO_serial.jsonl` **con la condicion cumplida citada dentro**, porque el remedio ya corre |
| **`D.52` del fundador** | en el banco, con las tres caidas en su tabla y la excepcion a `D.45` razonada |
| **3. la exencion de momento** | `censar_rutas.fase_ciega_abierta()` y `EXENTAS_EN_FASE_CIEGA`. **Se mide por AUSENCIA de `REPORTE.md`**, que es lo que el arnes retira: la fase ciega **es** esa ausencia, medida donde no se puede fingir |
| **4. el paso retirado** | **`scripts/retirar_paso.py`** y **`D.54`** en el banco. Medido primero, aplicado despues |
| **5. el encargo** | `docs/loop/PROMPT_SIGUIENTE.md`, vuelta 36, con `cap_10` entero |

### El caso positivo que pediste por su nombre, corrido contra el reporte de verdad

    $ python scripts/tabla_de_cierre.py
      SIN COMPROBAR  1  ninguna afirmacion de la forma 'N de M del capitulo' con su cap_NN
      SIN COMPROBAR  2  ninguna afirmacion de la forma 'N de M del capitulo' con su cap_NN
      DIFIERE        3  la celda publica '15 de 15 del capitulo' y cap_09 son 20 de 20
                        en el grafo (272 pasos)

    TABLA DE CIERRE EN ROJO: 1 fila(s) publican una cifra que el dato no da.

**Y regenerada, pasa:** `CUADRA  3  cap_09 son 20 en el grafo, y la celda dice 20`.

### El punto 4, medido antes de tocar nada

    $ python .v36/pasos_retirados.py
    poblacion: dataset/nodos.jsonl, 302 nodos, SIN filtrar
    nodos con una retirada declarada y el paso todavia en el campo : 1

      practicar_franqueza_radical_jefe_propio
         paso 13 de 17, y el resumen dice: P13 DE ESTE NODO LLEVA UN PUENTE, Y AQUI QUEDA RETIRADO

**UNO, y es el que el auditor nombro.** Aplicado: el paso sale del campo (`17` a `16`),
**su texto literal queda escrito dentro del nodo** y la retirada lleva su cita. Despues:
`encontradas: 0`.

> **Y EL MEDIDOR TENIA UN DEFECTO QUE SE VIO AL APLICARLO:** despues de retirar el paso
> **seguia acusando al mismo nodo**, porque el resumen sigue diciendo que el `P13` esta
> retirado y el nodo sigue teniendo trece pasos o mas. **Un medidor que no sabe decir
> cuando ya se hizo no mide: acusa siempre.** Ahora mira la marca que la propia retirada
> escribe.

### Una renumeracion mia, declarada

**`D.52` era mia de esta manana** (*`dataset/` es el catalogo y nada mas*), porque aquella
decision no venia numerada. **El fundador asigno `D.52` por la tarde a la tabla de cierre,
y el numero del fundador manda sobre el mio**, igual que paso con `D.45` y `D.46` el 16
sep. **Mi regla pasa a `D.53`**, el contenido no cambia.

**LO QUE NO SE REESCRIBE, Y SE DICE:** las actas, el reporte y la parada ya archivada
siguen diciendo `D.52` donde esa regla era `D.52`. **Son registro de lo que se escribio
cuando se escribio.** Lo que si se actualizo es lo que esta sesion mantiene: `src/`,
`scripts/`, `config/` y las pruebas.

### Las guardas al aplicar esto

    gate       302 nodos, VERDE          pruebas   294, 0 fallos
    guiones    VERDE                     tallado   VERDE
    censo      VERDE                     credito   ENTERO, ninguna especie en su tope
    tabla de cierre  VERDE

---

# EL CUERPO DE LA PARADA, SIN TOCAR

# PARA ALEXIS: **EL BUCLE PARA POR CREDITO ROTO.** `REPORTE` llega a `3 de 3` en la vuelta 35 de la linea `serial`

*Escrito por el auditor al cerrar la `ACTA 34`. `docs/loop/PROMPT_SIGUIENTE.md` queda
**VACIO** por `AUDITOR_FORJA.md` 3. El bucle no funde ramas y no crea remotos: esto es una
peticion, no una accion.*

---

## 1. EL MOTIVO, CON SU CONDICION LITERAL

`AUDITOR_FORJA.md` 3, quinta condicion de parada:

> **Credito roto (seccion 5): CLASE o CIFRA PUBLICADA dos tandas seguidas, o REPORTE tres
> seguidas de la especie que acumula.**

Y el instrumento de la casa, corrido al cerrar el acta:

    $ python forja.py credito
    CREDITO DE LA LINEA 'serial' (D.48)
      tandas: 34, en 149 suceso(s) de especie

      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA 34
      CIFRA PUBLICADA    0 de 2     ACTA 34
      CLASE              0 de 2     ACTA 34
      DATO MOVIDO        0 de 2     ACTA 34
      REPORTE            3 de 3     ACTA 34  TOPE

      CREDITO ROTO: REPORTE en su tope.

### 1.1. LAS TRES TANDAS SEGUIDAS, SIN NINGUNA LIMPIA EN MEDIO

| tanda | vuelta | la caida que acumulo | sede |
|---|---:|---|---|
| `ACTA 32` | `33` | `13` vecindades levantadas donde se levantaron `11` | conclusion de `Z.3.a` |
| `ACTA 33` | `34` | `0` PUENTE de `181` donde la relectura da `1` | dos TABLAS y la conclusion de `AA.5.b` |
| **`ACTA 34`** | **`35`** | **`15` de `15` del capitulo donde `cap_09` son `20` de `20`** | **TABLA de `AB.5.f` y conclusion de `AB.4.a`** |

### 1.2. LA CAIDA DE ESTA VUELTA, EN TRES LINEAS Y CON SU MEDICION

El reporte cierra la `TAREA 3` diciendo **`15` de `15` del capitulo, contando los `10` que
entraron en la vuelta 34**. Las dos mitades son falsas y se miden por caminos distintos:

    nodos del grafo que citan scott_radical_candor/cap_09.md : 20   (272 pasos)
    candidatos archivados que citan cap_09                   : 20
    candidatos en bandeja que citan cap_09                   : 0
    nodos que entraron en la vuelta 34 (7 mas 4 mas 4)       : 15, los quince de cap_09

**El capitulo son `20` de `20` y la vuelta 34 metio `15`, no `10`.** La `ACTA 33` ya lo
publicaba en su propio titulo (*`cap_09` insertado `15` de `20`*). **La vuelta 34 escribio
`15 de 15 DEL TRAMO`, que era cierto; la 35 lo reescribio como `DEL CAPITULO`.**

**LO QUE ESTA CAIDA NO ES, Y CONVIENE QUE SE LEA ANTES DE DECIDIR:** no movio ni un dato.
Los `5` nodos de la vuelta entraron bien, con el gate verde, la arista `D.29` cableada en
los dos sentidos, la bandeja de `cap_09` vacia y cero nodos desaparecidos. **Lo que esta mal
es lo que el reporte dice del trabajo, no el trabajo.**

## 2. EL ESTADO EXACTO

| pieza | valor | de donde sale |
|---|---|---|
| rama | `extraccion-mundo-11` | `git rev-parse --abbrev-ref HEAD` |
| hash al escribir esto | `0ff87d0a55838d8d8105fde99cacf5a89fbc94a2` | `git rev-parse HEAD` |
| fase | **auditor de la vuelta 35 de la linea `serial`, cerrada** | `docs/loop/loop.log` |
| nodos en el grafo | **`302`**, gate verde con `13` guardas | `python forja.py gate` |
| veredictos | **`427`**, de ellos `14` no consumadas | `bitacora/VEREDICTOS.jsonl` |
| aristas | **`109`** por los dos extremos | `dataset/nodos.jsonl` |
| libro de la linea | `scott_radical_candor`, lote `4`, **`CERRADO EN EXTRACCION`** | `python forja.py tablero` |
| bandeja del lote 4 | **`43`**: `cap_10` `14`, `cap_12` `2`, `cap_13` `12`, `cap_14` `15` | `cuarentena/scott_radical_candor/` |
| insertado del lote 4 | **`99`** de `142`, el `69,7` por ciento | `cuarentena/_insertados/scott_radical_candor/` |
| guardas | `gate`, `guiones`, `resolutor` y la suite de `274` pruebas, **todas verdes** | corridas por el auditor en esta vuelta |
| otros frentes | `grove_high_output` `EN CURSO` en su rama; `gerber_emyth` y `marquet_turn_the_ship` `PAUSADOS` | `python forja.py tablero` |

**NADA DEL DATO ESTA EN ROJO. LO QUE ESTA EN SU TOPE ES UNA RACHA DE DICTADO.**

## 3. LO QUE SE NECESITA DE TI

1. **DECIDIR SOBRE LA RACHA `REPORTE`.** Solo tu la reinicias, y la decision se escribe en
   `docs/loop/paradas/` para que el acta siguiente la cite (`AUDITOR_FORJA.md` 5.4). Un
   auditor que se la pone a cero se esta absolviendo, asi que **yo no la toco**. Si decides
   reiniciarla, la linea de `reinicio` del registro se escribe con
   `python forja.py credito --anotar` citando ese fichero.
2. **SI QUIERES, PONER EL REMEDIO DELANTE.** Las tres caidas de esta racha son la misma
   figura: **una cifra tecleada en una TABLA que no declara instrumento**, en el cierre del
   reporte. El tallado `D.41` no las ve por diseño, porque compara tablas contra su fichero
   de salida y estas no lo declaran. **El remedio natural es de arnes y no de doctrina:**
   que la tabla de cierre de tareas del reporte salga de un instrumento como ya salen las
   de apertura y cierre de estado. **No lo encargo yo:** `D.45` dice que mientras corran
   frentes en paralelo ninguna sesion toca `src/`, el banco, el arnes ni los protocolos.
3. **LA PREGUNTA DE DOCTRINA NUMERO `7`, QUE NO BLOQUEA PERO NO TIENE CASILLERO** (`ACTA 34`
   3.3): el `P13` de `practicar_franqueza_radical_jefe_propio` quedo **retirado por
   declaracion** dentro del `resumen_teorico`, y **su texto sigue literal en
   `pasos_accionables`**, porque ningun instrumento de la casa reescribe un paso de un nodo
   ya insertado. Quien lea los pasos se lleva el puente; quien lea el resumen se entera de
   que esta retirado. **La guarda `deprecado_en_superficie` es sobre aristas, no sobre esto.**
4. **UNA PROPUESTA DE ARNES, PEQUEÑA Y MEDIDA** (`ACTA 34` 5.3): al censo de rutas `D.42` le
   falta la exencion de `docs/loop/APERTURA_CIEGA.md` en la fase ciega. Mientras el auditor
   no ha escrito su apertura, cualquier acta que la cite como sede pone el censo en rojo, y
   con el la prueba de aceptacion que corre el hook entero. **Se cura sola en cuanto la
   apertura se escribe**, asi que es ruido y no dato, y `config/sedes_vacias.json` dice que
   esa lista la escribe el fundador.

5. **UNA PRUEBA EN ROJO QUE LA PROPIA PARADA FABRICA, Y LA DIGO YO** (`ACTA 34` 11.2). La
   suite estaba en `274` de `274`; **al vaciar `docs/loop/PROMPT_SIGUIENTE.md`, que es lo
   que `AUDITOR_FORJA.md` 3 manda, cae `test_el_encargo_vivo_del_repo_declara_su_libro`**,
   porque `D.49` exige que el encargo vivo declare su libro. **Las dos reglas piden lo mismo
   en efecto** (un encargo sin libro no abre la vuelta siguiente, que es lo que una parada
   quiere), **y lo que falta es que el rojo diga parada en vez de descuido**:
   `config/sedes_vacias.json` ya exime esa ruta citando la seccion `3`, y la guarda del
   tablero todavia no sabe que un encargo vacio **con `docs/loop/PARA_ALEXIS.md` al lado**
   es una parada. Es arnes, `D.45` me prohibe tocarlo, y **no lo toco**. El hook de commit
   no corre la suite, asi que el arbol commitea verde.

## 4. COMO RETOMAR

1. Archiva este fichero en `docs/loop/paradas/2026-09-17-<nombre>.md` con tu decision
   arriba, que es como se archiva en esta casa.
2. Si reinicias la racha, escribe la linea de `reinicio` en `docs/loop/CREDITO_serial.jsonl`
   citando ese fichero, y comprueba con `python forja.py credito` y
   `python forja.py credito --citas`.
3. **EL TRABAJO QUE ESPERA, Y CABE EN UNA VUELTA:** `cap_10` entero, sus `14` candidatos,
   que el propio encargo anterior dejo declarado que **no se parten**, mas la remision de
   `cap_08.md` `L95` al capitulo siete, que espera a que `cap_10` entre. La linea sigue
   siendo `serial`, el libro sigue siendo `scott_radical_candor` y el tablero da **SI** a
   que esta linea lo continue.
4. Vuelve a lanzar el arnes. **Sin tu decision escrita, la vuelta siguiente abriria con la
   racha en su tope y volveria a parar en el mismo sitio.**

---

**NI FUSIONO NI CREO NADA:** el lote 4 no cierra con esta vuelta, asi que `D.32` no abre
lote nuevo y `D.50` no releva a mitad. Lo que la vuelta 35 cierra es **un capitulo**.
