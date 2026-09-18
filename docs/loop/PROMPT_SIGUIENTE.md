# ENCARGO DE LA VUELTA 41: **CERRAR LA SERIE `D.37`, Y PAGAR LA DEUDA DE ARISTAS DE LA VUELTA 24**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

*Linea **serial** (`extraccion-mundo-11`), la unica que inserta (`D.45`). Escrito al cerrar la
`ACTA 39`, que audita la vuelta 40 y **no abre ninguna parada**.*

> # **LIBRO DE ESTA VUELTA: scott_radical_candor**

    $ python forja.py tablero --puedo scott_radical_candor
      LINEA 'serial', LIBRO 'scott_radical_candor': SI
        'scott_radical_candor' ya es de esta linea ('serial'): continuarlo es lo que toca.

---

## **LO QUE PASO EN TU VUELTA, SIN ADORNO Y SIN CASTIGO DE MAS**

**Entregaste cinco de tus seis piezas y las cinco me salen al digito.** Los `4` controles en sus dos
posiciones y sus dos sedes, los tres cortes del `ceo` (`321/0/39`, `324/4/43`, `324/9/45`), el
denominador `12` y `212`, la cola `16/11/5/0`, la medicion campo a campo del nodo rancio. **Tus NUEVE
discutibles se sostienen los NUEVE.** Y **tu `0` `PUENTE` de `58` lo relei yo entero y lo FIRMO**, que
es la fila que decide el volumen.

**Y no entro ni un nodo.** `0` de `4`.

| especie | de | a |
|---|---:|---:|
| **`REPORTE`** | `0 de 3` | # **`1 de 3`** |
| `CLASE` | `0 de 2` | `0 de 2` |
| `CIFRA PUBLICADA` | `0 de 2` | `0 de 2` |
| `DATO MOVIDO` | `1 de 2` | **`0 de 2`**, por `D.38.1` y no por indulto mio |
| `AUDITOR` | `1 de 3` | # **`2 de 3`**, **y es MIA**, no tuya |

### **LA CAUSA ESTA MEDIDA Y ES DE UNA LINEA, ASI QUE NO LA VOY A DISFRAZAR**

    $ cat .v40/informes/_cadena.txt
      07:06:08 arranca cadena 1
      cadena 1 arrancada (candidato 1 de 4)
      PARADA EN abrazar_incomodidad_silencio_contar_seis
    $ tail -1 .v40/informes/i01_abrazar_incomodidad.txt
      CODIGO DE SALIDA: 2
    $ grep "^BLOQUEADO" .v40/informes/i01_abrazar_incomodidad.txt
      BLOQUEADO: faltan veredictos para escuchar_entender_critica_dominar_defensa,
                 premiar_franqueza_hacer_escucha_tangible,
                 contar_historias_propias_explicar_franqueza_radical
    $ grep -c -- "--veredicto" .v40/cadena_1.sh
      4

**Tu guion traia los `4` veredictos declarados por LECTURA y ninguno de los `3` que levanta la SEÑAL.**
La aduana los pidio, el codigo de salida fue `2`, y **eso ocurrio a las `07:12`, cuando tu turno ya
habia cerrado a las `07:10:55`**. El encargo anterior decia, en negrita, *NO TERMINES TU TURNO CON UNA
CADENA TODAVIA CORRIENDO*, y la vuelta 39 lo habia comprobado con su `tail` pegado.

> **LO QUE NO TE CARGO, Y LO DIGO PARA QUE NO LO ARRASTRES:** la guarda que te paro **funciono**. Dos de
> esos tres vecinos estan en bandeja y los mide la aduana desde `D.38.5`. **No perdiste la vuelta por
> una regla injusta: la perdiste por no correr `forja.py informe` antes de escribir el guion, y por no
> mirar el resultado antes de irte.** Las dos cosas son la `TAREA 2`.

---

## TAREA 1, BLOQUEANTE. **LOS REGISTROS**

### 1.A. **UN VEREDICTO MAL PUESTO DE LA VUELTA 39, Y LA DEUDA DE ARISTAS QUE ARRASTRA DESDE LA 24**

**ADJUDICADO EN LA `ACTA 39` `4.2`, CON MI CASO ESCRITO Y LA VARA APLICADA DELANTE.** Esto es lo unico
de esta vuelta que toca un veredicto ya escrito, y por eso va primero.

    linea 498  SANO  elegir_pregunta_recurrente_pedir_critica
                     contra abrazar_incomodidad_arrancar_critica_equipo

**MI CASO, EN TRES LINEAS:** el `P07` de la madre dice *ten una pregunta de cabecera*, da la de Fred
Kofman y aniade *si esas palabras no te salen solas, busca las que si*. **Nombra el trabajo y lo deja
sin hacer.** El hijo lo hace en `24` pasos, **y su propio `P07` CORRIGE esa misma pregunta de Kofman**.
Eso es `NOMBRAR NO ES PROCEDIMENTAR` (`P.5.1`) con la direccion escrita. **La razon de la `498` compara
entregable contra entregable, que es la pregunta al reves** (`AUDITOR_FORJA.md` 6.1, *se pregunta que
aniade el HIJO a la MADRE, nunca al reves*).

**Y NO ES LECTURA NUEVA: es la arista `54` de la `ACTA 24`, adjudicada y SOSTENIDA hace dieciseis
vueltas**, junto con la `55`, la `56` y la `57`, que son las de tus tres candidatos de hoy.

| # | madre | hijo | `--paso` | especie | estado hoy |
|---:|---|---|---:|---|---|
| `54` | `abrazar_incomodidad_arrancar_critica_equipo` | `elegir_pregunta_recurrente_pedir_critica` | **7** | `D.29` | **en el grafo, SIN cable, y con un `SANO` encima** |
| `55` | `abrazar_incomodidad_arrancar_critica_equipo` | `abrazar_incomodidad_silencio_contar_seis` | **8** | `D.29` | el hijo entra hoy |
| `56` | `abrazar_incomodidad_arrancar_critica_equipo` | `escuchar_entender_critica_dominar_defensa` | **12** | `D.29` | el hijo entra hoy |
| `57` | `abrazar_incomodidad_arrancar_critica_equipo` | `premiar_franqueza_hacer_escucha_tangible` | **14** | `D.29` | el hijo entra hoy |

**LO QUE HACES:**

1. **Relee el par de la `498` contra el grafo, con los pasos de los dos delante.** Si mi lectura se
   sostiene, **corrigela por correccion declarada y sin borrar**:

       python forja.py anotar --linea 498 --anade "CORRECCION DECLARADA ..." --razon "..."

   y **cablea la arista `54`** con `python forja.py arista --madre abrazar_incomodidad_arrancar_critica_equipo
   --hijo elegir_pregunta_recurrente_pedir_critica --paso 7 --razon "..."`.
2. **Si al leerlos discrepas, NO la corrijas: escribe tu caso y marcalo discutible.** `AUDITOR_FORJA.md`
   1.3 dice que la discrepancia va a relectura conjunta y que **tu decides con la vara contra el grafo**.
   Yo pongo la evidencia; **no cierro esto a martillazos.**
3. **Las `55`, `56` y `57` van en el acto en que cada hijo entre**, con su razon escrita, **como `D.29` y
   NO como `D.37`**.

> ### **Y AQUI VA UNA CORRECCION DE MI PROPIA SEDE, PORQUE LA CAIDA ES MIA**
>
> **Mi apertura sellada de esta vuelta escribio que `abrazar_incomodidad_arrancar_critica_equipo` es
> cabeza de serie `D.37` porque *dice seis y las nombra*. Lo lei de su `TITULO`, que es un campo de esta
> casa, no del libro.** `cap_09` **no escribe la cuenta en ningun sitio**, y la `ACTA 24` ya lo adjudico:
> *sin cuenta no hay `D.37`*.
>
> **ESO ES `CIFRA PUBLICADA PROPIA` Y LA CARGO YO: `AUDITOR` sube a `2 de 3`.** Lo escribo aqui, y no
> solo en mi acta, **porque si mi encargo te dijera `D.37` estarias tecleando mi error dentro de
> `dataset/`.** Las cuatro son `D.29` y su razon la sostiene tu lectura, no una cuenta escrita.

### 1.B. **LO ADJUDICADO EN LA `ACTA 39`, RECOGIDO Y NO REABIERTO**

| | lo adjudicado |
|---|---|
| **tus NUEVE discutibles se sostienen los nueve** | los tres cortes del `ceo`, el verbo *medido* del `P06`, *la directora de Spanx* (`15.1` es regla de **id**, no de prosa de paso), el Rick Hanson sin `atribuciones` (ese campo es para **cifras** de autor, no para metaforas), la `L111` de `integrar_peticion`, los dos ejercicios en un nodo, la omision del ejemplo de `L229`, el `SANO` de `integrar_peticion`, y los dos rancios declarados por medicion. **Cero caidas dentro de tu marcado** |
| **la fila de `PASOS INVENTADOS` de tu tramo la FIRMO yo** | **`0` de `58`, `0,00` por ciento: FIRMADA.** `cap_13` entero, `4` de `212`, `1,89` por ciento, **sigue siendo SUELO** y no la firmo: `154` de esos pasos no los he releido |
| **la fidelidad `D.30` de tus tres candidatos YA ESTA HECHA** | **no la vuelvas a correr.** Son `45` de esos `58` pasos, releidos dos veces contra sus lineas, por ti y por mi. **`D.47`, modo austero: lo que el registro ya dice no se repite** |
| **tu puntero de `DC.2.d` decia `DC.5.d` donde los discutibles estan en `DC.5.e`** | **registrado con su nombre y NO acumula**: es prosa de acompanamiento, no tabla ni conclusion (`5.2`). **No lo arregles hacia atras, solo no lo repitas** |
| **el rojo de la suite en la fase ciega NO es tuyo y no es parada** | lo cubre *la exencion es de MOMENTO y no de fichero*. **Sube al fundador, y `D.45` prohibe que lo arregles tu** |

---

## TAREA 2, BLOQUEANTE. **EL METODO DE LA CADENA, ARREGLADO POR MECANICA Y NO POR PROPOSITO**

**ES LA TAREA QUE COSTO LA VUELTA 40 ENTERA, y por eso va antes que la extraccion.**

1. **CORRE `python forja.py informe` SOBRE CADA CANDIDATO ANTES DE ESCRIBIR SU GUION**, y **pega su
   salida**. Cada `vecino` de su cola de lectura es **un `--veredicto` obligatorio**, lo levante la
   senial o lo traigas tu. Hoy, sobre el arbol de la vuelta 40, salen asi:

       abrazar_incomodidad : 3 vecinos   escuchar_entender 0.449 | premiar_franqueza 0.353 | contar_historias 0.376
       escuchar_entender   : 4 vecinos   cambiar_forma_trabajar 0.634 | contar_historias 0.393 | abrazar_incomodidad 0.446 | premiar_franqueza 0.363
       premiar_franqueza   : 1 vecino    escuchar_entender 0.375

   **Y VUELVE A CORRERLO PARA EL `2` Y EL `3` DESPUES DE QUE ENTRE EL ANTERIOR**, porque el primero que
   entra cambia lo que el segundo mide (`EXTRACTOR.md` 12.3) **y porque dos de esos vecinos pasan hoy de
   bandeja a grafo.** La cifra de arriba es de **antes** de la primera insercion: no la copies como si
   fuera la de despues.

2. **CUENTA LOS VEREDICTOS CONTRA LOS VECINOS ANTES DE LANZAR**, y que el guion se niegue solo si no
   cuadran. **Una linea de `grep -c` contra el numero de vecinos del informe.**

3. **TU TURNO NO TERMINA HASTA QUE EL REGISTRO DE LA CADENA DIGA QUE ACABO.** Pega el `tail` de tu
   fichero de cadenas como ultima cosa que haces. **Si la cadena sigue viva, esperas; si murio, lo
   dices y escribes en que candidato.** La vuelta 39 lo hizo y le salio bien; la 40 no y perdio cuatro
   inserciones ya preparadas.

> **NO ES MAQUINARIA NUEVA Y POR ESO TE LA PUEDO PEDIR** (`7.F` de la cosecha, `EXTRACTOR.md` 13): los
> tres puntos son **un comando que ya existe**, **un `grep -c`** y **un `tail`**. No escribas un arnes,
> no escribas una guarda, no escribas un lector.

---

## TAREA 3. **`cap_13`, LOS TRES QUE CIERRAN LA SERIE, UNO POR VEZ Y EN EL ORDEN DEL LIBRO**

**EL TRAMO BAJA DE `4` A `3`, y lo baja `EXTRACTOR.md` 12.4**: *si una vuelta no cierra su reporte, la
siguiente baja el tramo*. **Tu `0,00` de `PASOS INVENTADOS` decia subir; el freno manda sobre el.**

| # | candidato | rotulo y linea | pasos | lo que ya tiene escrito |
|---:|---|---|---:|---|
| `1` | `abrazar_incomodidad_silencio_contar_seis` | `EMBRACE THE DISCOMFORT`, `L187` | 12 | arista `D.37` en cola (linea `489`) **mas la `55` de `D.29`**; rancio `484` que anotar |
| `2` | `escuchar_entender_critica_dominar_defensa` | `LISTEN WITH THE INTENT TO UNDERSTAND`, `L199` | 13 | arista `D.37` en cola (linea `492`) **mas la `56`**; rancio `485` que anotar |
| `3` | `premiar_franqueza_hacer_escucha_tangible` | `MAKE LISTENING TANGIBLE`, `L215` | 20 | arista `D.37` en cola (linea `495`) **mas la `57`**. **Con el cierra la serie** |

### 3.A. **CON EL `3` SE CIERRA LA SERIE `D.37`, Y ESO SE ESCRIBE CON SU CIFRA**

`L113` escribe *each of the four tips for soliciting criticism offered in the book* y `L237` los nombra
uno a uno. `elegir_pregunta` entro en la vuelta 39 y es el primero. **Cuando entren estos tres, las
cuatro partes estan en el grafo con sus cuatro aristas `D.37` desde la cabeza de `cap_13`.** Escribe esa
frase con la cifra al lado: **una serie a medias es el estado fragil y el reporte tiene que decir cuando
deja de estarlo.**

**Y NO CONFUNDAS LAS DOS FAMILIAS DE ARISTA, que es justo donde yo me cai:**

| desde | especie | que la sostiene |
|---|---|---|
| `pedir_critica_primero_crear_seguridad_psicologica` (`cap_13`) | **`D.37`** | **la cuenta escrita**: `L113` dice *four* |
| `abrazar_incomodidad_arrancar_critica_equipo` (`cap_09`) | **`D.29`** | **tu lectura, con razon escrita**: `cap_09` no escribe ninguna cuenta |

### 3.B. **LOS TRES QUE NO ENTRAN, PARA QUE NO SE PIERDAN**

`integrar_peticion_critica_rutina_existente` (`13` pasos, `SANO` ya razonado en las lineas `488` y `500`
y en dos aperturas selladas), `dar_elogio_disciplina_igual_critica` (`20` pasos, arista `49`, linea
`490`) y `medir_critica_respuesta_oyente_brujula` (`33` pasos, arista `51`, linea `494`) **siguen en
bandeja con su arista en cola.** **No los toques y no los declares cerrados.** `cap_13` **queda con `3`**.

---

## TAREA 4. **EL CIERRE, Y LA LINEA LITERAL ES LA MITAD DE ESTA TAREA**

**La seccion de la insercion se abre ANTES de que entre el primer candidato y crece una fila cada vez
que uno entra**, en su propio commit. **Eso lo hiciste bien en la vuelta 40 y no hay nada que cambiar.**

**LO QUE FALTO, Y ES LO QUE `REPORTE` CARGA:**

> *la vuelta cierra en el candidato `N` de `3`; los que quedaban pasan a la vuelta siguiente.*

**ESCRIBELA SEA CUAL SEA `N`, INCLUIDO `0` Y INCLUIDO `3`.** Cerrar completo y decirlo cuesta una linea;
**no decirlo costo la racha dos veces antes de la tuya y una vez en la tuya.**

**El prefijo lo eliges tu, con la salida pegada, igual que la vuelta 40** (`grep -oE "^## [A-Z]{2}\."
docs/loop/REPORTE.md | sort -u`). **La seccion es la `.6`.**

---

## EL CIERRE: LAS CUATRO COSAS QUE NO SE NEGOCIAN

1. **Gate, barrido de guiones y prueba de aceptacion EN VERDE**, con su salida pegada. Hoy abren en
   `324`, cero y `294 / 0 / 0`.
2. **Las cifras del cierre recomputadas al cierre** y no copiadas de tu apertura: nodos, veredictos,
   aristas, bandeja por capitulo, insertados y archivados.
3. **La cola de aristas recontada entera**, por `arista_corregida` cuando la linea la traiga. **Hoy abre
   en `16 / 11 / 5 / 0` y la cifra que tiene que salir `0` es la ultima.** Al cerrar, con tus tres
   dentro, deben quedar **`14` cableadas y `2` esperando** (`490` y `494`), y **`0`** con los dos
   extremos dentro y sin cable.
4. **Tus discutibles marcados ANTES de saber si aciertas**, y la fila de `PASOS INVENTADOS` **de tu
   tramo y con su denominador dicho**. Si tu tramo son los tres ya releidos, **dilo y no la infles**:
   una fila repetida no es una fila nueva.

**Y COMMITEA Y PUSHEA `docs/loop/`.**

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.**
