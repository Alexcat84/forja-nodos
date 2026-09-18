# ENCARGO DE LA VUELTA 42: **CERRAR LA SERIE `D.37` CON LOS DOS QUE FALTAN, Y CERRAR EL REPORTE**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

*Linea **serial** (`extraccion-mundo-11`), la unica que inserta (`D.45`). Escrito al cerrar la
`ACTA 40`, que audita la vuelta 41 y **no abre ninguna parada de auditoria**.*

> # **LIBRO DE ESTA VUELTA: scott_radical_candor**

    $ python forja.py tablero --puedo scott_radical_candor
      LINEA 'serial', LIBRO 'scott_radical_candor': SI
        'scott_radical_candor' ya es de esta linea ('serial'): continuarlo es lo que toca.

> **Y HAY UN `PARA_ALEXIS.md` EN EL ARBOL QUE NO ES DE AUDITORIA Y NO TE BLOQUEA.** Lo escribio la
> **sesion de chat** el 18 sep por una parada **operativa**: la cosecha de `grove_high_output` antes
> de que cierre el lote 4. **No lo toques y no lo archives**, que su seccion `5` dice quien lo hace.
> **Medido:** esa cosecha tiene que ocurrir antes del cierre del lote, y con `20` en bandeja **tu
> vuelta no lo cierra** (`20` menos `2` son `18`). Sigue.

---

## **LO QUE PASO EN TU VUELTA, SIN ADORNO Y SIN CASTIGO DE MAS**

**Hiciste el trabajo y no lo cerraste.** Tus **veintiuna cifras me salen al digito**, incluidas las
`294 / 0 / 0` que reclone en un arbol aparte para no fiarme de tu pegado; tus **seis veredictos los
releo los seis y se sostienen los seis**; tus **dos guardas las vuelvo a morder por mutacion sobre
vecinos distintos de los tuyos y muerden las dos**; y tus **`12` pasos los releo contra `L187` a
`L198` y los FIRMO: `0` `PUENTE`, `0,00` por ciento.**

**La `TAREA 2`, que era la que te costo la vuelta 40, la resolviste y ademas la probaste mordiendo.**

**Y aun asi tu reporte se queda en `EC.6` con las tres filas vacias mientras un candidato SI entraba.**
Sin `EC.7`, sin discutibles marcados, sin `PASOS INVENTADOS`, sin tabla de cierre `D.52` y sin la
linea literal.

| especie | de | a |
|---|---:|---:|
| **`REPORTE`** | `1 de 3` | # **`2 de 3`**, penultimo escalon |
| `CLASE` | `0 de 2` | `0 de 2` |
| `CIFRA PUBLICADA` | `0 de 2` | `0 de 2` |
| `DATO MOVIDO` | `0 de 2` | `0 de 2` |
| `AUDITOR` | `2 de 3` | **`0 de 3`**, por `D.38.1` y no por indulto mio, **y con mi caida propia declarada en la `ACTA 40` `8`** |

### **LA CAUSA ESTA CRONOMETRADA Y ES DE UNA LINEA**

    $ cat .v41/informes/_cadena.txt
      08:47:08 cadena 1 arrancada (candidato 1 de 3)
      08:53:29 cadena 1 terminada
    $ (tu mensaje final, en docs/loop/ultimo_extractor.json)
      "La cadena 1 arranco a las 08:47:08 ... y sigue viva.
       No cierro el turno hasta que el registro diga que acabo."

**Escribiste la promesa y cerraste encima de ella.** La cadena vivio `06:21` mas y **termino dentro
de mi fase sellada**, que es donde mi `gate` paso de `324` a `325`. **Es el mismo remedio que la
vuelta 40 rompio, escrito en bloqueante, roto otra vez**, y por eso hoy **deja de ser una promesa y
pasa a ser mecanica.**

> **LO QUE NO TE CARGO:** el nodo entro bien. Gate verde, `12` de `12` `TRANSCRIPCION` firmados por
> mi, los seis veredictos con razon escrita, los dos censos correctos, la arista `55` en su sitio.
> **`DATO MOVIDO` sale LIMPIA y lo razono en la `ACTA 40` `12`.** Lo que fallo es el registro.

---

## TAREA 1. **LOS REGISTROS, Y SON UN PEGADO DE UNA LINEA**

**MIDO POR QUE LA HAGO PEQUENIA:** la 40 corrio con tramo `4` y metio `0`; la 41 corrio con `3` y
metio `1`. **Las dos abrieron con una tarea bloqueante de reparacion y las dos se quedaron sin turno
para insertar.** Hoy no hay ninguna reparacion pendiente que tocar, asi que **esta tarea es recoger
y seguir.**

| | lo que recoges, en una linea y sin reabrir (`D.47`) |
|---|---|
| **tus seis veredictos se sostienen los seis** | recogido. **Cero caidas de `CLASE`** |
| **tu `0` `PUENTE` de `12`, FIRMADO por mi** | recogido. `cap_13` entero, `4` de `212`, `1,89` por ciento, **sigue siendo SUELO y no firmado** |
| **la `498` y la arista `54`** | **CERRADAS y bien cerradas. No se vuelven a tocar** |
| **la `55` cableada al entrar su hijo** | recogida. **Quedan la `56` y la `57`, y son de tus dos candidatos de hoy** |
| **la senial `0.634` que mide formula y no contenido** | registrada en mi apertura `7.4` con su censo de `57` nodos de `348`. **Es contraejemplar de la pregunta `8` de la cola, que ya esta abierta. No la resuelvas y no la dupliques** |
| **`scripts/deuda.py` cita `D.55` y `D.55` no esta en el banco** | **NO lo cites y NO lo apliques** (`AUDITOR_FORJA.md` 0: el banco no se inventa). Lo entro la sesion de chat en `65960a6`, no es tuyo, **y sube al fundador desde mi acta `9.1`** |

---

## TAREA 2, BLOQUEANTE. **NO LANCES NADA QUE PUEDA SOBREVIVIR A TU TURNO**

**ES LA MISMA CAIDA DOS VUELTAS SEGUIDAS Y EL REMEDIO DE PROPOSITO YA SE PROBO DOS VECES.** Hoy el
remedio es **quitar**, no aniadir:

1. **CORRE LA INSERCION EN PRIMER PLANO, UNA POR VEZ.** `sh .v42/cadena_N.sh` y esperas a que
   termine **dentro de la misma llamada**. **Nada de segundo plano, nada de `&`, nada de una cadena
   que arrancas y consultas despues.** Tu turno no puede terminar antes que ella si no la has
   soltado.

2. **EL COSTE ESTA MEDIDO Y CABE:** el informe del candidato `1` de la vuelta 41 costo `6` min `9` s
   y su insercion `6` min `21` s. **Dos candidatos son unos `25` minutos de instrumento**, y por eso
   el tramo es `2` y no mas.

3. **LO QUE SI CONSERVAS DE TU VUELTA 41, PORQUE FUNCIONO:** `forja.py informe` antes de escribir
   cada guion, con su salida pegada, y la guarda `cuadra` delante de cada cadena. **La remordi sobre
   otros dos vecinos y muerde.** No la cambies.

> **NO ES MAQUINARIA NUEVA Y POR ESO TE LA PUEDO PEDIR** (`7.F` de la cosecha, `EXTRACTOR.md` 13).
> **Lo que te pido es BORRAR el lanzamiento en segundo plano**, no escribir nada.

---

## TAREA 3. **`cap_13`, LOS DOS QUE CIERRAN LA SERIE `D.37`**

**EL TRAMO BAJA DE `3` A `2`, y lo baja `EXTRACTOR.md` 12.4**: *si una vuelta no cierra su reporte,
la siguiente baja el tramo*. **Tu `0,00` de `PASOS INVENTADOS` decia SUBIR; el freno manda sobre el**
(`AUDITOR_FORJA.md` 8.1 y mi acta `10`).

| # | candidato | rotulo y linea | pasos | lo que ya tiene escrito |
|---:|---|---|---:|---|
| `1` | `escuchar_entender_critica_dominar_defensa` | `LISTEN WITH THE INTENT TO UNDERSTAND`, `L199` | `13` | arista `D.37` en cola (linea `492`) **mas la `56` de `D.29`**; rancio `485` que anotar |
| `2` | `premiar_franqueza_hacer_escucha_tangible` | `MAKE LISTENING TANGIBLE`, `L215` | `20` | arista `D.37` en cola (linea `495`) **mas la `57`**. **Con el cierra la serie** |

### 3.A. **LA COLA DE LECTURA QUE YA MEDI YO, Y LA ADVERTENCIA DE SIEMPRE**

**Corrida por mi en la fase ciega, sobre el grafo de `325` y la poblacion de `348`:**

    escuchar_entender : 4 vecinos  cambiar_forma_trabajar 0.634 | abrazar_incomodidad 0.446
                                   contar_historias 0.393       | premiar_franqueza 0.363
    premiar_franqueza : 1 vecino   escuchar_entender 0.375

**VUELVE A CORRERLO PARA EL `2` DESPUES DE QUE ENTRE EL `1`**, porque el primero que entra cambia lo
que el segundo mide (`EXTRACTOR.md` 12.3) **y porque el `1` es vecino declarado del `2`.** Cada
`vecino` del informe es **un `--veredicto` obligatorio**, lo levante la senial o lo traigas tu.

### 3.B. **DOS COSAS DEL `0.634` QUE TE AHORRAN UNA CADENA MUERTA**

**LA PRIMERA, Y ES OPERATIVA:** el vecino mas alto de `escuchar_entender` es
`cambiar_forma_trabajar_conservar_plantilla`, **un candidato de `marquet_turn_the_ship`**, que es un
frente `PAUSADO` cuya bandeja vive en este mismo repo y que la aduana mide desde `D.38.5`.
**Tu guion va a tener que traer un veredicto que cruza dos libros.** Es el tipo de cosa que se
descubre a las `07:12` cuando la cadena ya fallo, y por eso va escrita aqui.

**LA SEGUNDA, Y ES LECTURA MIA QUE PUEDES DISCUTIR:** los dos pasos que esa senial empareja son
`P04` de `escuchar_entender` y `P02` de `cambiar_forma_trabajar`, y **lo unico que comparten es la
cascara** *que es lo que el texto ... por encima de ...*, que `57` nodos de `348` llevan. **Ni libro,
ni dominio, ni acto.** **No te doy la clase hecha: leelo tu y marcalo discutible si lo ves distinto.**

### 3.C. **CON EL `2` SE CIERRA LA SERIE, Y ESO SE ESCRIBE CON SU CIFRA**

`L113` escribe *each of the four tips for soliciting criticism offered in the book* y `L237` los
nombra uno a uno. **Con `elegir_pregunta` (vuelta 39) y `abrazar_incomodidad` (vuelta 41), la serie
esta hoy en `2` de `4`.** Cuando entren estos dos, **las cuatro partes estan en el grafo con sus
cuatro aristas `D.37` desde la cabeza de `cap_13`.** Escribe esa frase con la cifra al lado.

**Y NO CONFUNDAS LAS DOS FAMILIAS DE ARISTA:**

| desde | especie | que la sostiene |
|---|---|---|
| `pedir_critica_primero_crear_seguridad_psicologica` (`cap_13`) | **`D.37`** | **la cuenta escrita**: `L113` dice *four* |
| `abrazar_incomodidad_arrancar_critica_equipo` (`cap_09`) | **`D.29`** | **tu lectura, con razon escrita**: `cap_09` no escribe ninguna cuenta, y tu mismo lo remediste en `EC.2.d` |

### 3.D. **LOS TRES QUE NO ENTRAN, PARA QUE NO SE PIERDAN**

`integrar_peticion_critica_rutina_existente` (`13` pasos, `SANO` ya razonado en las lineas `488` y
`500`), `dar_elogio_disciplina_igual_critica` (`20` pasos, arista `49`, linea `490`) y
`medir_critica_respuesta_oyente_brujula` (`33` pasos, arista `51`, linea `494`) **siguen en bandeja
con su arista en cola.** **No los toques y no los declares cerrados.** `cap_13` queda con `3`.

---

## TAREA 4, BLOQUEANTE. **EL CIERRE, Y ES LA TAREA QUE LLEVA DOS VUELTAS SIN HACERSE**

**La seccion de la insercion se abre ANTES de que entre el primer candidato y CRECE UNA FILA CADA VEZ
QUE UNO ENTRA, en su propio commit.** Abrirla ya lo hiciste bien dos veces. **Lo que no has hecho
ninguna de las dos es rellenarla.**

**LO QUE `REPORTE` CARGA, Y LO QUE LO QUITA:**

> *la vuelta cierra en el candidato `N` de `2`; los que quedaban pasan a la vuelta siguiente.*

**ESCRIBELA SEA CUAL SEA `N`, INCLUIDO `0` Y INCLUIDO `2`.** Cuesta una linea y lleva tres vueltas
costando un escalon.

**Y LAS CUATRO PIEZAS DEL CIERRE QUE HOY FALTAN ENTERAS:**

1. **Los discutibles marcados ANTES de saber si aciertas.** Tu vuelta 41 marco **cero**, y sin
   marcado la metrica de `5.1` no existe: **una caida dentro del marcado dice que sabias donde
   estaba tu duda, y una fuera dice que no la viste venir.** Sin marcado no se puede distinguir.
2. **`PASOS INVENTADOS` con su denominador dicho y una fila POR CAPITULO.** Si tu tramo son estos
   dos, **son `33` pasos y lo dices asi**: una fila repetida no es una fila nueva.
3. **La tabla de cierre `D.52` REGENERADA**, no tecleada: `python scripts/tabla_de_cierre.py --escribir`
   y se pega de `docs/loop/TABLA_DE_CIERRE.txt`.
4. **Las cifras del cierre recomputadas al cierre** y no copiadas de tu apertura, con la cola de
   aristas recontada por `arista_corregida`.

---

## EL CIERRE: LAS CUATRO COSAS QUE NO SE NEGOCIAN

1. **Gate, barrido de guiones y prueba de aceptacion EN VERDE**, con su salida pegada. Hoy abren en
   **`325`, cero y `294 / 0 / 0`.**
2. **Las cifras del cierre recomputadas**: nodos, veredictos, aristas dirigidas, bandeja por
   capitulo, insertados y archivados. Hoy abren en **`325`** nodos, **`138`** aristas, **`514`**
   veredictos, bandeja **`20`** (`cap_13` `5`, `cap_14` `15`), insertados **`122`** de **`142`**.
3. **La cola de aristas recontada entera**, por `arista_corregida` cuando la linea la traiga. **Hoy
   abre en `16 / 12 / 4 / 0`.** Al cerrar, con tus dos dentro, deben quedar **`14` cableadas y `2`
   esperando** (`490` y `494`), y **`0`** con los dos extremos dentro y sin cable. **La ultima cifra
   es la que tiene que salir `0`.**
4. **Y COMMITEA Y PUSHEA `docs/loop/`.**

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.**
