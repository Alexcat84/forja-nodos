# PARA ALEXIS: **EL BUCLE SE DETIENE AL CERRAR LA VUELTA 53**, por dos condiciones y no por una

*Escrito por el auditor de la `ACTA 52`, linea **serial** (`extraccion-mundo-11`), el 19 sep 2026.
`docs/loop/PROMPT_SIGUIENTE.md` queda **VACIO**, que es lo que `AUDITOR_FORJA.md` `3` manda.*

> **LO PRIMERO, PORQUE ES LO QUE MAS FACIL SE CONFUNDE: LA VUELTA 53 HIZO BIEN SU TRABAJO.**
> Entrego sus cinco tareas, cerro `cap_06` entero en `8` de `8`, abrio `cap_07` por su cabeza, no
> inserto nada con la puerta cerrada, y **sus quince discutibles marcados se sostienen los quince**.
> **Lo que se detiene no es la vuelta: es el estado en el que el bucle queda.**

---

## 1. LOS DOS MOTIVOS, CADA UNO CON SU MEDIDA

### 1.A. **FALLO TECNICO REPETIDO** (`AUDITOR_FORJA.md` `3`)

> *hook, gate o **prueba de aceptacion en rojo dos vueltas seguidas por la misma causa sin regla que
> lo resuelva***

**Se cumple entera, y las cuatro mitades estan medidas:**

| | |
|---|---|
| **vuelta `52`** | `329` pruebas, `1` fallo. Verificado por la `ACTA 51` |
| **vuelta `53`** | `329` pruebas, `1` fallo. **Corrido por mi hoy** |
| **misma causa** | la **misma** prueba y la **misma** linea: `test_caso_negativo_el_encargo_que_declara_el_que_toca_pasa`, `tests/test_aceptacion.py` linea `4509` |
| **sin regla que lo resuelva** | **`D.55`** lo deja fuera de las cuatro guardas que bloquean, asi que ninguna vuelta esta **obligada** a pararse; **`D.45`** veda `tests/` y `scripts/` a toda sesion, asi que ninguna vuelta **puede** arreglarlo |

    $ python tests/test_aceptacion.py
    FAIL: test_caso_negativo_el_encargo_que_declara_el_que_toca_pasa
      (__main__.PruebaOrdenDePrioridad)
      File "tests\test_aceptacion.py", line 4509
      AssertionError: Lists differ: ["el encargo no dice de que vuelta es. D.58: ..."] != []
    Ran 329 tests in 118.148s
    FAILED (failures=1, skipped=1)

**LA AVERIA ES DE UNA LINEA Y ESTA DIAGNOSTICADA DESDE HACE DOS VUELTAS.** El commit `9ec9b3c` del
19 sep, que aplica `D.58`, dio a `scripts/guarda_tablero.py` la comprobacion de que el encargo
declare `ENCARGO DE LA VUELTA <n>`. **El fixture de esa prueba no se actualizo**: pasa un texto sin
titulo de vuelta y espera lista vacia. **La guarda esta bien; la prueba va por detras de ella.**

**Y NO LO DESCUBRO YO HOY: LA `ACTA 51` DEJO EL DISPARADOR ESCRITO DENTRO DE `d057`**, palabra por
palabra, antes de que la vuelta `53` empezara:

    AVISO: si la vuelta 53 cierra en rojo por la misma causa, se cumple la condicion de
    parada de AUDITOR_FORJA.md 3 (prueba de aceptacion en rojo dos vueltas seguidas).

**Cerro en rojo por la misma causa.**

### 1.B. **CREDITO ROTO** (`AUDITOR_FORJA.md` `3` y `5.4`)

> *`REPORTE` tres seguidas de la especie que acumula*

    $ python forja.py credito
      especie            racha      de donde sale
      AUDITOR            0 de 3     ACTA 52
      CIFRA PUBLICADA    1 de 2     ACTA 52
      CLASE              0 de 2     ACTA 52
      DATO MOVIDO        0 de 2     ACTA 52
      REPORTE            3 de 3     ACTA 52  TOPE

      CREDITO ROTO: REPORTE en su tope.

**Las tres son seguidas y ninguna tanda limpia se metio en medio** (`D.38.1`): `ACTA 50` la subio a
`1`, `ACTA 51` a `2`, `ACTA 52` a `3`.

**LA TERCERA, LA DE HOY, EN UNA LINEA** (`ACTA 52` `52.6`): el reporte publica **`media por pasada
CON reloj: 517,7 s`** con **`11` pasadas en el numerador y `9` en el denominador**. Los `4659,0` s
incluyen la pasada perdida de `600` s, **que la celda de al lado marca como sin fichero de reloj**.
Sobre las `9` que su propia tabla cuenta la media es **`451,0`**; sobre los `10` ficheros que existen,
**`405,9`**; sobre las `11` lanzadas, **`423,5`**. De ahi sale un **`-29,2` por ciento** contra unos
`731,2` de la vuelta `52` que **si** son media por pasada (`4387,4` sobre `6,0`): la caida real por
pasada es **`-42,1`**. **Vive en TABLA** (la de `OO.5.d` y la fila `5` de la tabla de cierre `D.52`)
**y en CONCLUSION**, asi que acumula.

**LO QUE NO ES, Y LO DIGO PARA QUE LA DECISION SE TOME SOBRE LO QUE HAY:** `4659,0 / 9` **es la
cifra buena para presupuestar candidatos** y la direccion de su conclusion es correcta, **y ademas
se queda corta**. **Lo que cayo es la frase, no el uso.** Las tres caidas de la racha son de la misma
familia: **una frase sobre una cifra cierta que el propio instrumento desmiente dos lineas abajo.**

---

## 2. EL ESTADO EXACTO, MEDIDO HOY

| | |
|---|---|
| **rama** | `extraccion-mundo-11` |
| **hash auditado** | `33010e68b41650f26859a5659c7cabac6ce8059f` |
| **fase** | fin del turno del auditor de la vuelta `53`. **Acta escrita, encargo VACIO** |
| **nodos en el grafo** | **`346`** (`wc -l dataset/nodos.jsonl`) |
| **veredictos** | **`740`** (`wc -l bitacora/VEREDICTOS.jsonl`) |
| **pares mutuos** | **`1`** |
| **bandeja de `grove_high_output`** | **`65`** candidatos esperando, mas `1` ya insertado |
| **`gate`** | **VERDE**, `346` nodos verificados |
| **`guiones`** | **VERDE**, cero largos y cero medios |
| **resolutor** | `346` vivos, `0` deprecados, `0` alias |
| **fidelidad `D.30`** | **VERDE**, `0` PUENTE. Firmado por mi sobre los **`68`** pasos del lote, no solo sobre los `21` de su muestra |
| **prueba de aceptacion** | **ROJO**, `1` fallo de `329` (el de `1.A`) |
| **deuda** | **`20`** pendientes, **`18`** pagadas. Ultima vuelta de saneamiento: la `49` |
| **lote `7` en extraccion** | **ABIERTO**: `cap_01` a `cap_06` minados, `cap_07` abierto en `1` de `9`, `cap_08` con `0` nodos por frontera, y **`18` capitulos en total** |
| **puerta de `D.39`** | **CERRADA** para `grove_high_output`: no esta en `cerrados_en_extraccion` |

**NINGUNA DE LAS CUATRO GUARDAS DE DATO ESTA EN ROJO** (`D.55`): `gate` verde, el cerrojo y el censo
no decreciente dentro de `gate`, y la fidelidad `D.30` con `0` puentes. **El dato esta intacto: la
vuelta `53` no movio ni una linea de `dataset/`, `bitacora/`, `censos/`, `config/`, `esquema/`,
`src/`, `scripts/`, `tests/`, `hooks/` ni del banco**, comprobado con `git diff 55dbb5e..HEAD`.

---

## 3. LO QUE SE NECESITA DE TI, Y SON TRES COSAS

### 3.1. **LA DE UNA LINEA, Y ES LA QUE DESBLOQUEA EL BUCLE**

**Arreglar el fixture de `tests/test_aceptacion.py` linea `4509`**, poniendole al texto del encargo
su titulo `ENCARGO DE LA VUELTA <n>`, **o levantarle el veto de `D.45` a una vuelta para que lo
arregle ella.** Ninguna sesion del bucle puede tocarlo hoy, y esa es exactamente la razon por la que
esto llego hasta aqui.

**LA GUARDA NO SE TOCA: esta bien y muerde donde debe.** Lo que va por detras es la prueba.

### 3.2. **LA RACHA DE `REPORTE`, QUE SOLO TU PUEDES REINICIAR** (`5.4`)

> *La reinicia una decision de Alexis escrita en `docs/loop/paradas/`, y el acta lo dice citandola.
> Un auditor que pone su propia racha a cero se esta absolviendo.*

**No la toco.** Si decides reiniciarla, va escrita en `docs/loop/paradas/` y la primera acta que
retome la cita. **Si decides no reiniciarla, tambien sirve**: una tanda limpia la pone a cero sola
(`D.38.1`), y para eso hace falta que el bucle vuelva a correr, que es lo que `3.1` desbloquea.

**MI LECTURA, Y LA DOY PORQUE ME LA VAS A PEDIR:** las tres caidas son de dictado y **ninguna movio
un dato**. La produccion de las tres vueltas fue buena y se la verifique al digito a las tres. **Pero
la racha no es mia de reiniciar**, y el patron que mide es real: tres veces seguidas **una frase que
el instrumento de al lado desmiente**.

### 3.3. **UNA DECISION DE ALCANCE, Y LA TRAIGO PORQUE ES LA QUE MAS TRABAJO DESBLOQUEA**

**`d058`, abierta ayer, mide algo que se va a cobrar el dia de la insercion:** el `resumen_teorico`
es **del `70,3` al `83,1` por ciento** del texto que la senial `1` compara, asi que **los candidatos
se parecen entre si por el formulario de la ficha y no por el procedimiento del libro.** Lo remido
yo en la `ACTA 52` `52.7` y **la medida es cierta**.

**La propuesta de `d058` es medir si `texto_comparable` puede dejar fuera el `resumen_teorico`, o
comparar pasos contra pasos.** Eso toca `src/`, que `D.45` veda. **No propongo mover ningun umbral**,
que es tuyo de raiz. **Lo que pido es que decidas si esa medicion se autoriza antes de la insercion o
despues**, porque los `65` candidatos de la bandeja entran con la senial tal como esta.

---

## 4. COMO SE RETOMA

1. **Arreglar el fixture de `3.1`** (o levantar el veto), y comprobar que `python tests/test_aceptacion.py` da `329` pruebas y `0` fallos.
2. **Escribir en `docs/loop/paradas/` la decision sobre la racha de `REPORTE`** (`3.2`), reinicie o no.
3. **El auditor que retome escribe el encargo de la vuelta `54` en `docs/loop/PROMPT_SIGUIENTE.md`**, citando esa decision. **Y la `54` ES de saneamiento**: el instrumento lo dice solo (`ultima vuelta de saneamiento: 49`, `scripts/deuda.py`), y `D.58` deja que lo compruebe el codigo y no la memoria de nadie.
4. **El trabajo que queda en el lote `7`, ya medido y sin adivinar**: `cap_07` en `1` de `9` con su frontera publicada tramo a tramo en `OO.2.b` del reporte, `cap_08` cerrado en `0` nodos, y `cap_09` a `cap_18` sin abrir.

### **Y TRES COSAS QUE DEJO APUNTADAS PARA QUIEN RETOME, PORQUE SE PIERDEN SI NO SE ESCRIBEN**

- **`ACTA 52` `52.5`: tres fronteras contra el grafo declaradas por lectura y que ninguna senial levanta**, la mas apretada `decidir_nivel_competente_inferior` contra `repartir_decision_cercanos_hechos`, que **mandan lo contrario sobre la misma palanca**. **Se cablean el dia de la insercion.**
- **`d056`**: los `17` veredictos de la vuelta `53` se midieron contra poblaciones de `406` a `414`, **ninguno contra el lote entero**. La cola se recorre entera el dia de la insercion.
- **`conducir_etapas_modelo_ideal_decision`** es la ficha mas grande del lote (`12` pasos) y **la maquina la dejaria entrar sin leer nada**, con `0` vecinos incluso sobre la poblacion completa de `414`. **Es la que entra a ciegas.**

---

> **EL BUCLE NO FUNDE RAMAS Y EL BUCLE NO CREA REMOTOS.** Esto no pide merge y no pide publicar:
> **pide una linea de fixture y una decision escrita.**
