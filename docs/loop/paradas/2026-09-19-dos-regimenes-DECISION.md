# DECISION DEL FUNDADOR, 19 SEP 2026: **DOS REGIMENES**

*Aplicada **sin parar el arnes**, que era la condicion. No archiva ninguna parada: el bucle
estaba corriendo la vuelta 52 mientras esto se escribia, y sigue.*

---

## LA DECISION, LITERAL

> SESION DE CHAT en forja-nodos. Commitea y pushea lo pendiente en la
> rama activa antes de tocar nada. DECISION DEL FUNDADOR (19 sep 2026):
> DOS REGIMENES. Archivala en docs/loop/paradas/2026-09-19-dos-regimenes
> -DECISION.md y aplicala en la vuelta siguiente sin parar el arnes:
>
> 1. REGIMEN DE EXTRACCION (MODO_INSERCION=cuarentena), ligero, porque
>    nada toca el grafo: el extractor mina TRES capitulos por vuelta con
>    techo de 30 candidatos; corre tallado y censo (baratos); y la
>    relectura de fidelidad D.30 se hace POR MUESTRA: uno de cada tres
>    capitulos entero, y en los otros dos una muestra fija de 15 pasos
>    con semilla escrita. El auditor de extraccion verifica la frontera
>    al digito, coteja la muestra, publica pasos inventados por capitulo
>    y escribe un acta corta; SIN fase ciega, sin sello ni testigo (no
>    hay cifra sobre el grafo que proteger). Si la muestra de un capitulo
>    pasa del 10 por ciento de pasos inventados, ese capitulo se relee
>    entero antes de seguir. Objetivo medido: turno bajo 5 USD.
> 2. REGIMEN DE INSERCION (MODO_INSERCION=insertar), completo, sin quitar
>    nada: es donde el dato existe y donde cada guarda se paga sola. La
>    relectura de fidelidad de un lote se hace ENTERA en su vuelta de
>    insercion, sobre los candidatos que entran, no antes: asi ningun
>    paso entra al grafo sin haber sido leido contra su libro una vez.
> 3. LA CADENCIA DE SANEAMIENTO SE HACE CUMPLIR POR EL ARNES: la vuelta
>    49 debio ser de saneamiento y no lo fue. deuda.py gana la
>    comprobacion en la apertura: si desde la ultima vuelta de saneamiento
>    han pasado cinco, la vuelta que abre ES de saneamiento y el encargo
>    no puede decir otra cosa. La proxima es la 53.
> 4. ALCANCE, con la cifra delante: Grove se termina y se inserta, y el
>    mundo 11 puede declararse COMPLETO con esos cinco libros si el
>    fundador lo decide al cerrar Grove. Gerber y Marquet siguen pausados
>    con sus 19 candidatos; se relevan solo si el coste medido del
>    regimen ligero lo permite, y eso se decide con la cifra de Grove
>    delante, no ahora.
> 5. Escribe el PROMPT_SIGUIENTE de la siguiente vuelta de extraccion en
>    el regimen ligero, con su muestra y su semilla.

---

## UNA CORRECCION AL DATO DE LA DECISION, Y VA A FAVOR DEL BUCLE

> **LA VUELTA 49 SI FUE DE SANEAMIENTO.** Lo dice el registro, y lo escribio el auditor.

    {"tipo": "saneamiento", "vuelta": 49,
     "cita": "PROMPT_SIGUIENTE.md de la ACTA 47, que titula la vuelta 49 VUELTA DE
              SANEAMIENTO (D.55) LA QUINTA DESDE LA 44, y REPORTE.md KK.5.h, que la
              declara con esas palabras. La declaracion faltaba en el registro y la
              escribe el auditor en la ACTA 48 seccion 48.5.c."}

Y pago deuda ese dia: **`3` en la 49**, mas `2` en la 50 y `3` en la 51. **`16` pagadas en
total.**

**LO QUE SI PASO, Y ES MAS SUTIL:** la vuelta 49 **corrio como saneamiento y no lo anoto en
el registro**, asi que durante un dia `deuda.py` decia *ultima vuelta de saneamiento:
ninguna todavia*. **El auditor lo detecto solo** y escribio la declaracion que faltaba,
citando donde constaba.

**EL PUNTO 3 SE APLICA IGUAL Y HACIA FALTA**, porque el defecto que describe existia: **la
cadencia dependia de que alguien se acordara de anotarla**. Lo unico que cambia es la
cuenta: **la proxima de saneamiento es la `54`, no la `53`.**

---

## LO QUE SE APLICO

| punto | donde quedo |
|---|---|
| **1 y 2, los dos regimenes** | **`D.58`** en el banco, y **en los dos protocolos**: `EXTRACTOR.md` seccion `15` y `AUDITOR_FORJA.md` antes de `5.1`. **Ahi es donde tienen que vivir**, porque un encargo lo reescribe el auditor de la vuelta siguiente y un protocolo no |
| **la muestra con semilla** | **`scripts/muestra_fidelidad.py`**. Reparte uno entero y dos de `15` pasos, **con `sha1` y sin `random`**: el mismo texto da la misma lista en cualquier maquina |
| **3, la cadencia** | **`scripts/guarda_tablero.py`**, que es lo que el arnes ya llama al abrir. **`orquestador_forja.sh` NO se toco** |
| **5, el encargo** | `docs/loop/PROMPT_SIGUIENTE.md`, vuelta 53, con su semilla `v53` |

### POR QUE LA CADENCIA ENTRA POR LA GUARDA Y NO POR EL ARNES

**Dos motivos, y los dos importan.** El arnes estaba **corriendo** mientras esto se
escribia, y **bash lee su script a trozos mientras lo ejecuta**: editarlo lo corrompe a
mitad. Y un fichero que esta sesion no mueve **es un fichero que no puede chocar en una
cosecha**.

**Caso positivo:** con la ultima de saneamiento en la `49`, un encargo de la `54` que
declare `EXTRACCION` **no abre**, y la guarda nombra la cuenta. **Negativo:** ese mismo
encargo declarando `SANEAMIENTO` pasa.

### UN ROTULO MIO QUE ESTA DECISION VOLVIO FALSO, Y LO CORREGI

`deuda.clase_de_vuelta()` devolvia **`INSERCION`** para toda vuelta que no fuera de
saneamiento. **Con tres clases, eso es falso en toda vuelta de extraccion.** Ahora devuelve
**`LIBRE`**, que no es una clase: **es la ausencia de obligacion.** Las otras dos las elige
el encargo segun el libro, y **decirlas ahi seria publicar un rotulo que ese instrumento no
mide.**

### LO QUE NO PUEDE TOMAR EFECTO SIN UN RELANZAMIENTO, Y LO DIGO

**`MODO_INSERCION` y la fase ciega son del arnes**, y el arnes se lanzo con
`MODO_INSERCION=insertar`. Mientras esa corrida viva:

- **la fase ciega, el sello y el testigo van a seguir corriendo** en cada vuelta, aunque
  `D.58` los quite del regimen ligero;
- **funcionalmente ya estas en extraccion**, porque `D.39` no deja insertar un lote abierto
  y el extractor lo mide en cada vuelta.

**El ahorro entero del regimen ligero llega en el proximo relanzamiento**, con
`MODO_INSERCION=cuarentena`. **No mato un turno vivo para adelantarlo**, que es lo que la
decision pedia al decir *sin parar el arnes*.

### Las guardas al aplicar esto

    gate       346 nodos, VERDE        pruebas   329, 1 fallo ambiental
    guiones    VERDE                   tablero   VERDE
    censo      VERDE

**El fallo es `test_e_guion_largo_rompe_el_hook`, que exige el arbol limpio antes de
ensuciarlo**, y el extractor esta escribiendo. Con el arbol quieto pasa.
