# PARA ALEXIS. **EL BUCLE SE DETIENE EL 12 SEP 2026, Y LA CAUSA VUELVE A SER EL AUDITOR**

*Escrito por el auditor al cerrar la `ACTA 20` (`docs/loop/ACTA_AUDITOR.md`, la seccion que abre
con `# ACTA 20`, linea 18136). Condicion de parada: `AUDITOR_FORJA.md` 3, **CREDITO ROTO**.
`docs/loop/PROMPT_SIGUIENTE.md` queda **VACIO**, que es lo que esa misma seccion manda.*

---

## 1. EL MOTIVO, EN UNA FRASE Y CON SU COMANDO

**MI RACHA PROPIA LLEGA A 3 DE 3** (`D.38.2`: *`REMEDIO ROTO` y `CIFRA PUBLICADA PROPIA` acumulan
en la misma racha; tres seguidas paran`*), **y la tercera es un `REMEDIO ROTO`: escribi tres
guiones largos en el mensaje final de mi propia fase ciega, contra un remedio que dejo escrito el
auditor de la vuelta 19 exactamente para eso.**

**EL REMEDIO, `ACTA 19` `8.1`, literal:**

> *Y CERO GUIONES LARGOS Y CERO GUIONES MEDIOS EN MI MENSAJE FINAL, que es la otra mitad de la
> orden, porque el arnes lo escribe en `ultimo_auditor.json` despues de que mis comprobaciones
> hayan pasado.*

**LO QUE PASO, con la salida del arnes pegada:**

    [2026-09-12 17:07:27]   apertura ciega sellada: 37cb783e1c1a9a30ca7cc63b26b68957cbbda7ac
    [pre-commit] barrido de guiones
    BARRIDO DE GUIONES EN ROJO: 3 hallazgo(s)
      docs/loop/ultimo_apertura.json linea 1 columna 2933: guion largo (U+2014)
      docs/loop/ultimo_apertura.json linea 1 columna 3625: guion largo (U+2014)
      docs/loop/ultimo_apertura.json linea 1 columna 3903: guion largo (U+2014)
    [pre-commit] COMMIT ABORTADO

**Y NO ES UN ROJO DE ADORNO: tumbo dos de las cinco guardas.** Con esas tres lineas en el arbol,
`python forja.py guiones` sale en rojo y `python tests/test_aceptacion.py` **falla su prueba `E`**,
que exige el repo limpio antes de ensuciarlo. **Mi turno normal empezo con dos guardas rojas y las
dos eran mias.**

**TRES ACTAS SEGUIDAS CON CAIDA PROPIA, SIN NINGUNA TANDA LIMPIA EN MEDIO**, que es lo unico que
`D.38.1` admite para poner el contador a cero: `ACTA 18` **1 de 3**, `ACTA 19` **2 de 3**,
`ACTA 20` **3 de 3**.

> ### **LO QUE ESTA PARADA NO ES: NO ES UNA PARADA POR EL TRABAJO DEL EXTRACTOR.**
>
> **La vuelta 20 sale limpia de `CLASE` y limpia de `CIFRA PUBLICADA`**, y la `ACTA 20` lo verifica
> comando a comando: `cap_09` cerrado en **20 de 20** con **272 pasos**, los **95 pasos** nuevos
> cotejados uno a uno contra su linea con **0 puentes**, los **5 ids limpios** contra las seis
> reglas, y **las 39 filas de su frontera de `cap_10` remedidas por mi una a una: las 39 al
> digito**, con `8.976` contra `8.976`, cero lineas sin cubrir y cero solapes.
>
> **Su racha `REPORTE` se queda en 2 de 3 y NO sube**, con la unica cifra desfasada que encontre
> registrada y razonada en la `ACTA 20` `1.5`. **Si lees esa decision mia como blanda, la fila que
> tienes que mover es esa**, y entonces habria dos paradas en vez de una.

---

## 2. EL ESTADO EXACTO, MEDIDO HOY

| | |
|---|---|
| **rama** | `extraccion-mundo-11` (el bucle no funde ramas y no crea remotos) |
| **ultimo commit del extractor** | `dfeac69` (cierre de la vuelta 20 en `aef7324` mas dos precisiones) |
| **nodos en el grafo** | **203** (`wc -l dataset/nodos.jsonl`, y `forja.py gate` dice `nodos verificados: 203`) |
| **veredictos en la bitacora** | **148** (**79** `CONTINUA`, **69** `SANO`), sin mover en toda la vuelta |
| **candidatos en cuarentena del lote 4** | **83**, con **856 pasos**. **Ninguno en el grafo** |
| **pares mutuos** | sede vacia, solo la cabecera |
| **fase** | lote 4 (`scott_radical_candor`) **ABIERTO**, **10 de 15 unidades minadas** (`cap_00` a `cap_09`), **y ningun capitulo partido** |
| **cola de extraccion** | `cap_10` a `cap_14`, **36.656 palabras de cuerpo** |
| **las cinco guardas AL CERRAR MI TURNO** | `gate` **VERDE 203**, `guiones` **VERDE**, `rancios` **VERDE 148**, `resolutor` **203 vivos**, `tests/test_aceptacion.py` **90 pruebas, 0 fallos, 0 errores** |
| **rachas** | `CLASE` **0 de 2**, `CIFRA PUBLICADA` **0 de 2**, `REPORTE` **2 de 3**, **la del auditor 3 de 3** |
| **sello de la apertura ciega** | `37cb783e1c1a9a30ca7cc63b26b68957cbbda7ac`, **intacto** |
| **`PASOS INVENTADOS`** | `cap_09` **0,00 (0 de 272)**, lote 4 **0,58 (5 de 856)**, peor fila `cap_04` **6,25** contra tope **10**: **el freno no se dispara** |

### 2.1. **EL ARBOL QUEDA VERDE Y COMMITEADO. NO HAY TRABAJO BUENO SIN GUARDAR**

A diferencia de la parada de la `ACTA 17`, **aqui no hay nada a medio hacer**: la vuelta 20 cerro
su reporte, `cap_09` esta entero, y mi acta y este fichero estan commiteados. **Lo unico que tuve
que tocar para poder commitear fueron los tres guiones largos de mi propio mensaje en
`docs/loop/ultimo_apertura.json`**, sustituidos por el guion corto normal, con las tres
ocurrencias copiadas antes en la `ACTA 20` `1.2` y la correccion declarada en su `7.4`.

---

## 3. LO QUE SE NECESITA DE TI, Y SON TRES COSAS

### 3.1. **LA DECISION QUE SOLO ES TUYA: REINICIAR MI RACHA, O NO**

`5.4`: *la racha NO se reinicia sola. La reinicia una decision de Alexis escrita en
`docs/loop/paradas/`, y el acta lo dice citandola.* **Un auditor que pone su propia racha a cero se
esta absolviendo, y por eso no la toco.**

**Y TE DOY EL DATO QUE MAS IMPORTA PARA DECIDIR, aunque no me favorece:** es la **segunda** vez en
tres dias que el bucle se detiene por la racha del auditor (`ACTA 17`, 12 sep, y esta). **Aquella
vez reiniciaste la racha con una condicion mecanica puesta encima** (`D.40`, que el arnes entregue
los remedios heredados). **`D.40` funciono**: lei el acta anterior por su huella y declare la
herencia. **Lo que fallo hoy esta un escalon mas abajo: el arnes me entrego UN heredado, y el
remedio que rompi no estaba entre los entregados**, porque vive en la `8.1` del acta y no bajo el
titulo `TAREA BLOQUEANTE`. **Si vas a poner otra condicion mecanica, ese es el sitio exacto.**

### 3.2. **UNA PALABRA EN UNA TUPLA, QUE ES DOCTRINA YA ADJUDICADA Y CODIGO QUE NO ES MIO DE TOCAR**

**`ACTA 20` `4.7`: `docs/loop/ultimo_apertura.json` es artefacto de maquina a los efectos de
`D.33`**, igual que su gemelo `ultimo_auditor.json`, que si esta exento. La lista no lo nombra
porque el fichero **nacio despues** de `D.33`, con `D.34`:

    src/comun.py:243
    ARTEFACTOS_DE_MAQUINA = ("loop.log", "ultimo_extractor.json", "ultimo_auditor.json")

**No es maquinaria nueva** (moratoria, cosecha `7.F`): no anade guarda ni lector, **corrige el
alcance de una que ya existe**. Con esa palabra puesta, el mensaje final de la fase ciega deja de
poder tumbar dos guardas. **No lo he tocado yo porque `src/` no es sede del auditor**, y porque
**arreglarlo no borra mi caida**: el remedio dice que mi mensaje no lleve guiones largos, no que el
fichero este exento.

### 3.3. **LOS FICHEROS DE USAR Y TIRAR DEL ARBOL, QUE SIGUEN AHI Y CRECEN**

Repetido de la `ACTA 19` `7.6`, con lo mio anadido: `.t1_v20/` (16 guiones), `.aduana_v19/`,
`.aduana_v20/`, `.mut_v21/`, y mis `.censo_apertura_v21.py`, `.barrido_auditor_v21.py`,
`.frontera_auditor_v21.py`, `.cierre_cap09_v21.py`, `.verif_v21_auditor.py` con sus `.txt`.
**Ninguna regla manda retirarlos y `AUDITOR_FORJA.md` 3 te reserva borrar lo que ninguna regla
ordena borrar. No los borro y no fabrico una parada para poder borrarlos.** Los de `.aduana_*` **no
son andamio: son la prueba de cifras publicadas**, y retirarlos seria retirar evidencia.

---

## 4. COMO SE RETOMA, Y ESTA TODO MEDIDO PARA QUE NO HAGA FALTA REHACER NADA

**El trabajo de la vuelta siguiente esta decidido y no depende de la parada.** Si reinicias la
racha, el encargo se escribe con esto y nada mas:

| | |
|---|---|
| **la vuelta siguiente es `cap_10` ENTERO, y nada mas** | `cap_10` es `Cap. 7`, `Team`, **8.976 palabras de cuerpo** |
| **cuantos candidatos** | **13**, adjudicados en la `ACTA 20` `4.6` con la frontera cortada dos veces (la del extractor y la mia) y las cuatro discrepancias resueltas leyendo el texto. **13 cabe bajo el techo de 15 de `12.4`: no hay que partir el capitulo** |
| **la vara del corte, ya adjudicada** | **un nodo por cada par (condicion de activacion, entregable)**; la cuenta escrita del libro no corta, solo decide si la arista es `D.37` o `D.29` (`ACTA 20` `4.1`) |
| **la `D.37` viva que hay que cablear** | `L173` dice *three things* y sus tres partes **si daran nodo**: `P24` a `P25`, `P26` y `P27`, **tres aristas en la misma vuelta en que se escriban**. `P28` (*Follow up*) es **coda** y no entra en la serie |
| **el par que hay que mirar con lupa** | `L225` a `L251` de `cap_10` contra `reconocer_recompensar_gente_estable` de `cap_06` (12 pasos, en la bandeja). Mi lectura: **`CONTINUA` con arista, no `REPITE`**, y **la aduana no lo va a levantar sola** porque los dos extremos viven en cuarentena y `src/informe.py:113` carga la poblacion solo del grafo |
| **el volumen** | el tramo sigue en **tres capitulos** y el freno de `PASOS INVENTADOS` **no se dispara**, pero manda el techo de candidatos: **`cap_10` solo** |
| **la insercion** | **sigue cerrada**: `D.39` inserta un lote **CERRADO**, y quedan `cap_11` a `cap_14` sin minar. **Cero inserciones no es una vuelta perdida** |
| **la deuda de aristas** | **doce colas `D.29` vivas**, once desbloqueables con un solo acto (el cierre del lote 4), y **mas la `D.37` de `cap_10`** que se declara aparte porque sus nodos no existen todavia |
| **lo que sigue sin poder firmarse** | el **informe de lote de los 20 de `cap_09`** quedo lanzado y **no acabo**: `.aduana_v20/informe_lote_cap09_v2.txt` tiene **480 bytes, solo la cabecera**. Es la unica cifra del saldo que un informe de uno en uno no puede medir (`CHOCAN entre si dentro del lote`), y **ni el extractor ni yo hemos podido correrla dentro de un turno** a tres minutos por candidato |

**Y SI PREFIERES NO REINICIAR LA RACHA**, el estado tampoco se pierde: el grafo esta en 203 con el
gate verde, los 83 candidatos del lote 4 viajan en el repo (`D.25`), y `cap_00` a `cap_09` estan
enteros y sin partir.
