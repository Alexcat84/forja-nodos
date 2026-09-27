# DECISION DEL FUNDADOR, 22 SEP 2026: **LA RACHA DE `gerber_emyth` SE REINICIA CON CONDICION, Y LOS TRES DEFECTOS SE ARREGLAN AHORA**

*Archivo de la parada `G3` del frente `gerber_emyth`, escrita por su auditor al cerrar la
`ACTA G3`. **La decision va arriba, literal. El cuerpo va debajo sin tocar una coma.***

> ## **ESTE FICHERO ES EL QUE REINICIA LA RACHA.** `AUDITOR_FORJA.md` `5.4`: una racha la
> reinician **una tanda limpia** o **una decision escrita del fundador en
> `docs/loop/paradas/`**. Esta es la segunda. *Un auditor que pone su propia racha a cero
> se esta absolviendo*, y esta sesion tampoco puede hacerlo.

---

## LA DECISION, LITERAL

> SESION DE CHAT en forja-nodos. Commitea y pushea lo pendiente en la
> rama activa antes de tocar nada. DECISION DEL FUNDADOR (22 sep 2026)
> sobre la parada G3 del frente gerber. Archivala en docs/loop/paradas/
> 2026-09-22-gerber-g3-DECISION.md y aplicala:
>
> 1. LA RACHA REPORTE DE LA LINEA gerber_emyth SE REINICIA, con condicion:
>    la TAREA 1 de la vuelta 4 ejecuta d101 (cap_12: nacen los candidatos
>    de L51 y L63; L69 queda declarada no-nodo con su motivo) antes de
>    abrir cap_13. Regla nueva al banco, tu asignas el numero: LO
>    DECLARADO COMO DISCUTIBLE SE HACE O SE CIERRA EN LA MISMA VUELTA; un
>    "ahi nace otro candidato" publicado y no ejecutado es caida de
>    CIFRA, no de reporte.
> 2. El frente sigue en cuarentena, Sonnet extractor y Opus auditor,
>    regimen ligero: la cifra de 9,46 por turno se publica en el TABLERO
>    como la del regimen ligero de verdad, al lado de la de Grove.
> 3. LOS TRES DEFECTOS DE MAQUINARIA SON TUYOS Y SE ARREGLAN AHORA, con
>    el frente parado y antes de relanzarlo, en la rama de insercion y
>    luego llevados al worktree de gerber por fusion: (d097) la cadencia
>    de saneamiento D.58 gana su aritmetica en un frente: se cuenta desde
>    la primera vuelta del frente, no desde la 49 de la serial, y un
>    frente nace con su contador en cero; (d096) el tablero ve un
>    capitulo minado a cero como minado (con su firma), no como
>    pendiente; (d102) la fila del tablero se actualiza al cierre del
>    turno, no al arranque, para que no envejezca dentro del propio
>    turno. Cada uno con su caso positivo.
> 4. Escribe el PROMPT_SIGUIENTE de la vuelta 4 de gerber (TAREA 1 d101,
>    luego cap_13 en adelante en ligero) y relanza el frente con el
>    comando de gerber. La serial sigue parada hasta la insercion de la
>    semana que viene, como decidiste.

---

## LO QUE ESTA SESION APLICO, Y DONDE

| punto | donde vive aplicado |
|---|---|
| `1` el reinicio | linea `reinicio` en `docs/loop/CREDITO_gerber_emyth.jsonl`, con este fichero por cita |
| `1` la regla nueva | **`D.61`** en `docs/BANCO_DE_REGLAS.md` |
| `1` la condicion | `TAREA 1` del `PROMPT_SIGUIENTE.md` del worktree de gerber |
| `2` la cifra del ligero | `config/frentes.json` `coste_por_turno`, publicada por `forja.py tablero` |
| `3` los tres defectos | `scripts/deuda.py`, `src/tablero.py`, `config/frentes.json` y `orquestador_forja.sh`, con `7` pruebas |
| `4` el encargo y el relanzamiento | `PROMPT_SIGUIENTE.md` del worktree, y el comando de la seccion final |

---

## UNA NOTA SOBRE LA FECHA, Y SE DECLARA EN VEZ DE ELEGIRLA EN SILENCIO

**La decision se fecha el `22` sep y el reloj de esta maquina marca el `21`:**

    $ date '+%F %T'
    2026-09-21 10:41:*

**Se archiva con la fecha del fundador**, que es la que la decision lleva escrita y la que
el nombre del fichero pide. **Se deja anotado porque la aritmetica de `d097` cuenta
VUELTAS y no dias**, asi que la diferencia no toca ninguna cifra de este archivo; si
alguna vez una regla cuenta por calendario, este parrafo es donde mirar.

---

## LAS TRES CAIDAS QUE HICIERON LA RACHA, Y POR QUE `D.61` CAMBIA SU PRECIO

| tanda | la caida | que es | con `D.61` |
|---|---|---|---|
| `G1` | cito una seccion `G1.10.e` que no existe | errata de celda | sigue siendo `REPORTE` |
| `G2` | *los dos discutibles* donde su `G2.7` tiene `3` | errata de celda | sigue siendo `REPORTE` |
| `G3` | **`cap_12` da al menos `3` candidatos y publico `1`** | **trabajo anunciado y no hecho** | **`CIFRA PUBLICADA`** |

**El propio auditor separo las tres antes de que nadie se lo pidiera**, y lo escribio con
estas palabras: *lo digo asi para que la decision no se tome sobre una racha que parece de
erratas.* **`D.61` convierte esa distincion en mecanica**, para que la proxima vez no
dependa de que un auditor tenga el buen juicio de senialarla.

---

## LO QUE SE VERIFICO ANTES DE REINICIAR NADA

    $ python forja.py credito                 (en el worktree de gerber)
      REPORTE            3 de 3     ACTA G3  TOPE
      CREDITO ROTO: REPORTE en su tope.
    $ python forja.py credito --revisar
      REPLAY VERDE en la linea 'gerber_emyth': las 10 tanda(s) vigilables suman lo que declaran.

    $ python forja.py gate
      GATE VERDE.  nodos verificados: 346
    $ python forja.py guiones
      BARRIDO DE GUIONES VERDE
    $ python tests/test_aceptacion.py
      total: 343 pruebas, 0 fallos, 0 errores

**Las cuatro guardas de dato de `D.55` en VERDE, cero inserciones en el frente entero, y el
grafo donde estaba.** La racha se reinicia sobre un frente sano.

---

## EL CUERPO DE LA PARADA, SIN TOCAR UNA COMA

# PARA ALEXIS: **EL FRENTE `gerber_emyth` PARA POR CREDITO ROTO**

*Escrito el 21 sep 2026 por el auditor del bucle al cerrar la `ACTA G3`, sobre el commit `4f2d2af`
de la rama `extraccion-gerber_emyth`, worktree `C:/Users/AlexDesk/Documents/forja-gerber_emyth`.*

> ## **MOTIVO: `REPORTE` llega a `3 de 3`, su tope, en tres tandas seguidas sin una limpia en medio.**
> **`AUDITOR_FORJA.md` seccion `3` (credito roto) y `5.4`. Lo dice el instrumento antes que yo.**

    $ python forja.py credito
    CREDITO DE LA LINEA 'gerber_emyth' (D.48)
      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA G3
      CIFRA PUBLICADA    0 de 2     ACTA G3
      CLASE              0 de 2     ACTA G3
      DATO MOVIDO        0 de 2     ACTA G3
      REPORTE            3 de 3     ACTA G3  TOPE

      CREDITO ROTO: REPORTE en su tope.
    $ python forja.py credito --revisar
    REPLAY VERDE en la linea 'gerber_emyth': las 10 tanda(s) vigilables suman lo que declaran.

**`docs/loop/PROMPT_SIGUIENTE.md` queda VACIO a proposito**, que es lo que la seccion `3` manda.

---

## 1. LAS TRES TANDAS QUE HACEN LA RACHA, Y NO PESAN LO MISMO

| tanda | la caida de `REPORTE` | sede | quien la levanto |
|---|---|---|---|
| **`G1`** | cito una seccion `G1.10.e` que no existe en el documento | celda de tabla | el propio auditor de la `G1`, contra si mismo, en su parada del `17` sep |
| **`G2`** | *los dos discutibles* donde su `G2.7` tiene `3`, y su propio `G2.8.c` ya decia `3` | celda de tabla | `ACTA G2` `3.1` |
| **`G3`** | **`cap_12` da al menos `3` candidatos y publico `1`** | **CABECERA y cuatro TABLAS** | `ACTA G3` `4.1` |

**LAS DOS PRIMERAS SON CIFRAS MAL TECLEADAS. LA TERCERA ES TRABAJO QUE NO SE HIZO**, y lo digo asi
para que la decision no se tome sobre una racha que parece de erratas:

- `cap_12` `L51` (el saludo nuevo, con las palabras exactas y sus dos ramas) y `cap_12` `L63` (el
  test de seis semanas del traje azul, con sus dos etapas y sus ocho prendas nombradas una a una)
  **son inventario propio del libro en imperativo al lector** y pasan `EXTRACTOR.md` `9.1`;
- **el extractor lo marco como discutible `1` antes de saber si acertaba**, nombro el bloque del
  traje azul en particular y escribio la consecuencia exacta: *ahi nace otro candidato*;
- **lo adjudique con la vara escrita y con un ejemplar de esta misma casa y este mismo libro
  delante** (`unificar_color_forma_vestuario_modelo`, nacido en la vuelta `1` de este frente de un
  pasaje de la misma forma). **No hubo que mover la vara**, y por eso esto no es parada de doctrina.

**Y el resto de la vuelta `3` es buena, y lo mido:** las `19` filas de sus tres fronteras me salen
al digito, su informe de aduana me sale **identico byte a byte**, su muestra de fidelidad tambien,
sus `6` pasos son `6` TRANSCRIPCION y `0` PUENTE, su vecino `SANO` se lo firmo, y **el remedio
heredado que llevaba dos vueltas sin cumplirse (`d095`) esta pagado entero, con sus `4` celdas
tachadas y la comprobacion de secciones en `0`.**

---

## 2. EL ESTADO EXACTO, MEDIDO HOY Y NO RECORDADO

    $ git rev-parse --short HEAD ; git rev-parse --abbrev-ref HEAD
    4f2d2af
    extraccion-gerber_emyth
    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
    $ ls cuarentena/gerber_emyth/*.json | wc -l
    11
    $ git diff --name-only 07aa6f2..HEAD -- dataset/ bitacora/ censos/ config/pares_mutuos.jsonl
    (vacio)

| pieza | cifra | nota |
|---|---:|---|
| fase | **EXTRACCION en cuarentena** | `MODO_INSERCION=cuarentena`. **CERO inserciones en el frente entero** |
| nodos en el grafo | **346** | sin mover desde que el frente se reanudo |
| veredictos escritos | **740** | `bitacora/` intacta |
| candidatos en bandeja de `gerber_emyth` | **11**, con **95** pasos | `0` insertados |
| unidades del libro | **22** | mas la unidad apartada del `cap. 17` |
| unidades CERRADAS | **8** | `cap_04` a `cap_11` |
| unidades ABIERTAS | **1** | **`cap_12`**: le faltan al menos `2` candidatos (`d101`) |
| unidades SIN TOCAR | **13** | `cap_01` a `cap_03`, y `cap_13` a `cap_22` |
| guardas | **las seis en VERDE** | `gate` `346` con `13` guardas, `guiones`, `343` pruebas con `0` fallos, `resolutor`, tallado `165` tablas, censo `943` rutas |
| deuda de la linea | **36** pendientes, **32** pagadas | `docs/loop/DEUDA.jsonl` |

**NO HAY AVERIA.** Las cuatro guardas de dato que `D.55` deja bloquear estan verdes. **Lo que para
el frente no es un fallo tecnico: es la metrica de credito llegando a su tope.**

---

## 3. LO QUE NECESITO DE TI, en dos lineas

1. **Di si la racha de `REPORTE` de la linea `gerber_emyth` se reinicia, y escribelo en
   `docs/loop/paradas/`.** `5.4` es explicita: la racha no se reinicia sola, la reinician **una
   tanda limpia** o **una decision escrita tuya**, y **un auditor que pone la racha a cero se esta
   absolviendo**. Yo no puedo hacerlo, ni siquiera viendo que dos de las tres caidas son erratas de
   celda. **Si decides que siga, el bucle arranca la vuelta `4` sin mas.**
2. **Di si el frente sigue en `MODO_INSERCION=cuarentena`.** La bandeja tiene `11` candidatos con
   `95` pasos esperando, y **la cosecha de un lote es tuya** (`D.32`, `D.39`). Si la respuesta es
   que siga en cuarentena, no hace falta que lo digas dos veces: es lo que ya hace.

**LO QUE NO TE PIDO, porque el bucle no lo hace:** ningun merge, ningun remoto, ningun umbral
movido. **El bucle no funde ramas y el bucle no crea remotos.**

---

## 4. COMO SE RETOMA, cuando decidas

1. **La vuelta `4` abre cerrando `cap_12`**, que es lo unico que esta a medias:
   **`d101`** en `docs/loop/DEUDA.jsonl` trae la pieza (`R3`), los dos bloques (`L51` y `L63`), y
   **el tercero que NO es nodo (`L69`) tambien escrito**, para que no se cosechen tres donde hay
   dos. La clase de `R3` en `docs/loop/REPORTE.md` linea `57859` **se corrige declarando y sin
   borrar**, como se corrigieron las cuatro celdas de `d095`.
2. **Despues, el orden del libro:** el siguiente sin tocar es `cap_13` (`364` palabras, el mas corto
   del libro), y luego `cap_14` en adelante. `cap_01` a `cap_03` siguen en `d094`, que **no es
   blocante**.
3. **Los tres punteros medidos que no se pueden perder**, todos en `docs/loop/DEUDA.jsonl`:
   `d098` (`D.37`, `cap_05` `L29`), `d104` (`D.37`, `cap_12` `L21`) y `d099` (donde nace el nodo de
   la delegacion, si nace: `cap_18` `L345` a `L349`).
4. **Y tres defectos de maquinaria medidos y NO tocados**, porque `D.45` veda `src/` y el arnes
   desde un frente: `d096` y `d102` (el tablero no puede ver un capitulo minado a cero, y su fila
   envejece dentro del propio turno) y `d097` (**la cadencia de saneamiento de `D.58` no tiene
   aritmetica en un frente**: la cuenta sale negativa y un frente no puede recibir una vuelta de
   saneamiento por ese camino, nunca).

---

*Todo lo que sostiene este fichero esta en `docs/loop/ACTA_AUDITOR.md`, `ACTA G3`, con el comando
pegado encima de cada cifra. Mis ficheros de trabajo de ese turno estan en `.g3aud/`.*
