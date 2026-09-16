# ENCARGO DE LA VUELTA 32: **LA CELDA TECLEADA DENTRO DEL INSTRUMENTO**, LA SEPTIMA ARISTA DE LA CABEZA, Y CERRAR `cap_11` EN INSERCION

*Escrito por el **auditor** al cerrar la **ACTA 30**, que audita la vuelta 31. Sede del auditor por
`AUDITOR_FORJA.md` 5.6.*

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## EL ESTADO CON EL QUE ABRES, MEDIDO POR MI HOY Y NO COPIADO

*Lo mido yo con mis comandos y lo publico para que tu apertura lo cuadre contra el suyo. Si tu
instrumento dice otra cosa, **gana el tuyo y declaras la discrepancia** (`EXTRACTOR.md` 5).*

| | |
|---|---:|
| hash al cerrar mi turno | `9a7c3ec` mas los commits de esta acta |
| nodos en `dataset/nodos.jsonl` | **267** |
| veredictos en `bitacora/VEREDICTOS.jsonl` | **391** |
| aristas del grafo, por los dos extremos | **102** y **102**, y **cero sin reciproco** |
| candidatos en bandeja, lote 4 (`cuarentena/scott_radical_candor`) | **78** |
| ya insertados y archivados, lote 4 | **64** |
| candidatos en bandeja, lote 5 (`cuarentena/marquet_turn_the_ship`) | **3** |
| lote 4 insertado sobre `142` | **45,07 por ciento** |
| pruebas de aceptacion | **200**, `0` fallos |
| tallado y censo de rutas | **VERDE** los dos: `61` tablas y `493` rutas |

**`PASOS INVENTADOS POR CAPITULO` de la vuelta 31, firmada por mi** (`ACTA 30` `8`): `cap_11`
**`0,00`** por ciento sobre **`142`** pasos. **El freno de fidelidad no se activa.** El que aprieta
sigue siendo el reloj de la aduana, **y esta vez lo cronometre yo: `192` segundos una corrida en
seco** (`ACTA 30` `1.4`), dentro de la banda de `109` a `321` que tu reporte publico.

**NO SE ABRE NINGUN LOTE** (`D.32`): el lote 4 esta **cerrado en extraccion desde la `ACTA 24`** y lo
que corre es **insercion**. **No hay condicion de apertura que medir porque no hay lote que cerrar.**

---

## TAREA 1. LOS REGISTROS DE LA `ACTA 30`

**Anexa al reporte la fila de registros** con lo que esta acta adjudica, **sin rehacer mis medidas**:

- **los `9` discutibles de `X.6`: SOSTENIDOS LOS NUEVE.** Cero caidas dentro del marcado.
- **`6` relecturas pineadas: las `6` se sostienen.** Tasa de caida de `CLASE` **`0,00`** por ciento,
  **banda al 95 por ciento de `0,00` a `39,03`**. La banda es ancha porque la poblacion era de seis,
  y eso es la cifra y no un defecto suyo.
- **las `3` propuestas: REGISTRADAS LAS TRES Y NINGUNA ENCARGADA** (moratoria de maquinaria,
  `AUDITOR_FORJA.md` 5.6). **Tu propuesta `1` la reforzaste bien y yo le puse mi cronometro al lado.**
- **tus tres caidas propias de `X.8.f`: las tres las cazaste tu y las tres las doy por buenas.**
- **mi unica caida cargada contra ti**: `REPORTE`, la fila `10` de la tabla de la cabeza de `cap_11`
  (`ACTA 30` `7.1`). **La racha `REPORTE` queda en `2 de 3`; `CLASE` y `CIFRA PUBLICADA` en `0 de 2`
  las dos. Mi racha propia vuelve a `0 de 3` por tanda limpia.**
- **y una caida que NO es tuya y que cazaste tu:** tu `DISCUTIBLE 7` tenia razon y **la atribucion
  mala era del auditor anterior** (`ACTA 30` `7.2`). **Queda registrada contra mi sede, no contra la
  tuya.**

---

## TAREA 2, **BLOQUEANTE**: LA CELDA TECLEADA DENTRO DEL INSTRUMENTO, Y LA ARISTA QUE SE PERDIO POR ELLA

*Va antes de la primera insercion y es bloqueante **porque la racha `REPORTE` esta en su penultimo
escalon**, y `AUDITOR_FORJA.md` 5.5 dice que entonces el remedio **se encarga, no se declara**.*

### 2.a. **EL DEFECTO, MEDIDO** (`ACTA 30` `4.1` y `4.2`)

Tu tabla de `X.4.e` publica en su fila `10`:

    | 10 | Be Conscious of Culture | L35 | debatir_decidir_asuntos_cultura_evitar_delegar | en bandeja |

**Y el propio dato dice quien es quien, dos veces, una en cada fichero:**

    recorrer_rueda_conscientemente_cultura_equipo (EN EL GRAFO desde el 12 sep):
      "Sale de las lineas 271 a 299 y de las 307 a 333, BAJO EL ROTULO BE CONSCIOUS OF CULTURE"

    debatir_decidir_asuntos_cultura_evitar_delegar (en bandeja):
      "Sale de las lineas 301 a 305, bajo el rotulo Debate and decide explicitly,
       DENTRO DE LA SECCION BE CONSCIOUS OF CULTURE. ES LA PIEZA P16"

**El decimo rotulo es `recorrer_rueda_conscientemente_cultura_equipo`**, que ya vivia en el grafo;
`debatir_decidir` es **un rotulo interior suyo**. Con la celda caen `de ellos, con nodo dentro del
grafo hoy: 6` (**son `7`**), `de ellos, con su nodo todavia en bandeja: 3` (**son `2`**) y la
conclusion de `X.8.d` de que los tres que quedan cierran tres aristas de cabeza (**cierran dos**).

### 2.b. **POR QUE EL TALLADO NO LO VIO, QUE ES LO QUE HACE FALTA ARREGLAR**

    $ sed -n '15,16p' .v31/cabeza.py
    # LOS DIEZ ROTULOS EN EL ORDEN DE L17 A L35, con el nodo que los procedimenta.
    # El nodo lo pongo yo leyendo; lo que la maquina pone es si vive y si esta cableado.

**La tabla ERA la del instrumento y el tallado salio VERDE con razon.** Lo tecleado estaba **dentro**
del instrumento. **`D.41` cubre esto por extension natural de su propio motivo** (*la diferencia no
fue el cuidado: fue el metodo*), asi que **no es doctrina nueva y no es parada: es un remedio.**

### 2.c. **LO QUE HAY QUE HACER**

**Que el mapeo de rotulo a nodo se GENERE del dato**: cada `resumen_teorico` declara **su rango de
lineas y su rotulo**, y casar el rotulo del indice con el nodo cuyo rango lo contiene **es lo que la
maquina sabe hacer y el dedo no**. **No es maquinaria nueva:** es tu propio `.v31/cabeza.py` leyendo
el dato en vez de una constante, **y lo dice tu propio `X.4.a`**: *un instrumento que se equivoca lo
dice; una celda tecleada, no.*

- **si una constante tecleada es inevitable, el instrumento lo dice en su primera linea de salida**,
  como hace `herencia.py` con su `AVISO`;
- **republica la tabla de la cabeza entera con la fila `10` corregida**, y **corrige tambien los dos
  recuentos y la conclusion de `X.8.d`** por correccion declarada, **sin borrar el texto viejo**
  (`D.13`).

### 2.d. **Y CABLEA LA ARISTA QUE LA CELDA MALA ESCONDIO. LA CLASE LA PONGO YO Y TU LA EJECUTAS**

    madre : decidir_quien_comunica_cada_cuanto        paso 6, "y ser consciente de la cultura"
    hija  : recorrer_rueda_conscientemente_cultura_equipo    14 pasos, ya en el grafo

**Es `D.29` y no `D.37`**, por lo mismo que las otras seis: la lista de `L17` a `L35` **enumera sin
decir cuantas**. **La razon escrita que `D.29` cobra te la doy hecha, para que no la inventes:**

> **`CONTINUA` por lectura.** El paso `6` de la madre nombra *ser consciente de la cultura* como una
> de las herramientas de la rueda, y la hija **despliega ese nombre en catorce pasos que la madre no
> tiene**: recorrer las etapas de la rueda sobre tu propia cultura, la prueba de contrastar tu
> conducta contra la cultura que empujas, y el correctivo de explicarla o corregirla. **La madre solo
> la nombra; la hija dice como se hace.**

**Los dos extremos viven en el grafo, asi que se cablea hoy y no queda en cola.** **Y LO COMPRUEBAS
POR LOS DOS EXTREMOS EN `dataset/nodos.jsonl`, no por la prosa de la salida.**

---

## TAREA 3. CERRAR `cap_11` EN INSERCION: LOS TRES QUE QUEDAN, CON SUS DOS ARISTAS DE CADUCIDAD

**Quedan `3` de los `14`**, y son los rotulos `8` y `9` de la cabeza mas la pieza `P16`:

| # | id | lineas | pasos |
|---:|---|---|---:|
| 12 | `montar_tablero_kanban_medir_actividades` | `L235` a `L249` | 10 |
| 13 | `pasear_organizacion_hallar_problemas_pequenios` | `L251` a `L269` | 9 |
| 14 | `debatir_decidir_asuntos_cultura_evitar_delegar` | `L301` a `L305` | 6 |

**3.a. LA RELECTURA DE FIDELIDAD `D.30` VA ANTES DE LA PRIMERA INSERCION**, y publicas
`PASOS INVENTADOS POR CAPITULO` con su fila de `cap_11`, que yo firmo.

**3.b. Y ESTA ES LA PARTE QUE NO SE PUEDE APLAZAR, CON FECHA DE CADUCIDAD.** Son **dos** aristas, y
las dos las adjudique yo en mi apertura sellada `4.2` y las repito en `ACTA 30` `4.4`:

> **EN EL ACTO EN QUE CADA UNO PASE LA PUERTA, DECLARAS SU ARISTA POR LECTURA:**
>
>     madre : decidir_quien_comunica_cada_cuanto   paso 6, "los tableros kanban"
>     hija  : montar_tablero_kanban_medir_actividades
>
>     madre : decidir_quien_comunica_cada_cuanto   paso 6, "pasear por la organizacion"
>     hija  : pasear_organizacion_hallar_problemas_pequenios
>
> **POR QUE NO PUEDEN ESPERAR, medido por mi HOY y no citado:** corri la aduana en seco sobre el
> kanban y da **`BLOQUEARIA` con `1` vecino, y el vecino NO es la cabeza**: es
> `repartir_notas_publicar_reparto_esperado`, por `paso_contra_nodo 0,607`. Sobre el paseo da **`0`
> vecinos, `ENTRARIA sin leer nada`**. **Ninguna senial va a poner a estos dos junto a su madre.**

**3.c. Y `debatir_decidir` NO LLEVA ARISTA DE CABEZA, y lo digo para que no se cablee por simetria:**
**no es uno de los diez rotulos del paso `6`.** Su madre por contenido es
`recorrer_rueda_conscientemente_cultura_equipo`, **pero quien lo nombra es el resumen de la madre y no
un paso suyo**, y `D.37` y `D.29` piden **citar el paso**. **Sin paso que lo nombre, no se declara.**

**3.d. SI LA INSERCION NO CABE, cierras donde llegues y lo declaras con su cifra**
(`EXTRACTOR.md` 12.4), **como hiciste bien en la vuelta 31**. Con tres candidatos a dos corridas de
aduana cada uno, mi cronometro dice que caben.

---

## TAREA 4. UN `resumen_teorico` QUE DICE LO CONTRARIO DEL GRAFO Y DE LA `ACTA 25`

*`ACTA 30` `4.3`. **No es caida tuya ni de esta tanda**: viene de la vuelta 22 y ninguna posterior la
toco. La cace recontando la cola de aristas.*

| | |
|---|---|
| **lo que el grafo tiene** | `recorrer_rueda_conscientemente_cultura_equipo` **es la madre** y `recorrer_rueda_hacer_cosas_equipo` el hijo |
| **lo que la bitacora adjudico**, linea `265`, citando `ACTA 25` `3.3` | lo mismo |
| **lo que su `resumen_teorico` sigue diciendo** | *`recorrer_rueda_hacer_cosas_equipo` ... **es la MADRE de este nodo*** |

**LA DIRECCION ESTA BIEN PUESTA EN EL DATO Y BIEN ADJUDICADA EN LA BITACORA. Lo que quedo sin corregir
es la frase.** `D.13`: entre dos textos fechados que chocan **gana el mas reciente y el perdedor se
corrige sin borrarse**. **La via existe y no hay que construirla:**

    python forja.py corregir --nodo recorrer_rueda_conscientemente_cultura_equipo \
                             --anade "CORRECCION DECLARADA ..." --razon R

---

## TAREA 5. LA COLA ENTERA, RECONTADA FILA A FILA CONTRA EL DATO

| lo que queda | cifra que yo mido hoy | que la cierra |
|---|---:|---|
| la arista de la cabeza al decimo rotulo | **1** | **`TAREA 2.d`**, cableable hoy |
| aristas en cola escritas en la bitacora | **4** escritas, **3** cableadas, **1** abierta (linea `371`) | que entre la MADRE `desplegar_plan_orden_operaciones_franqueza_radical`, en bandeja |
| las dos aristas con fecha de caducidad de `TAREA 3.b` | **2** | declararlas **en el acto** de la insercion |
| el `resumen_teorico` de `recorrer_rueda_conscientemente` | **1** | **`TAREA 4`** |
| **huecos de transcripcion** | **2** ejemplares y **2** especies | **CORREGIDA POR MI** (`ACTA 30` `2.3`): `L153` es un **paso que falta**; `escribir_apuntes` paso `10` es un **paso que remite y no transcribe**, y es **el unico de los `2.156` del grafo**. **La frase *con un solo ejemplar no se construye* ya no vale.** Sigue **SIN VIA**: `forja.py corregir` escribe el resumen, no un paso. **NO construyas la via** (moratoria) |
| las entradillas de `LISTEN`, `CLARIFY` y `DEBATE` de `cap_07` sin nodo | **3** de **7** | **NADA: adjudicado consecuencia buena** (`ACTA 29` `5`). Registro, no deuda |
| `L221` de `cap_07`, *turn on that rock tumbler* | **1** tramo | **NO se toca**: `cap_07` cerrado en insercion |
| `cap_04` releido, candidatos y pasos | **6** y **48** | sigue sin caber, **y van tres vueltas**. Si tampoco cabe, **lo declaras otra vez con su motivo** |
| la frontera por capitulo con las `QUESTIONS TO CONSIDER` | **14** de **17** | la vuelta que mine un capitulo del lote 5 |
| las `8` lineas `SIN HUELLA` de `D.15` | **8**, **las 8 declaradas** | **CERRADA**, y lo corri hoy |
| `censos/series_y_cabezas.md` | **0** filas con **267** nodos | **propuesta registrada y NO encargada.** Moratoria |
| bandeja del lote 4 | **78** | la insercion |
| de esa bandeja, lo que queda de `cap_11` | **3** | **`TAREA 3`** |
| lote 5 | **3** | **NO TOCAR** (`D.39`) |

**Y RECUENTALA TU CONTRA EL DATO, no contra esta tabla.** Si una cifra mia no te sale, **gana la tuya
y declaras la discrepancia.**

---

**Son CINCO tareas y el tope son cinco** (`EXTRACTOR.md` 1.3). **La `TAREA 2` es BLOQUEANTE y va antes
de la insercion**: la racha `REPORTE` esta en `2 de 3`, y lo que la subio fue **una celda tecleada
dentro de un instrumento que el tallado no puede ver**. **Mientras ese metodo siga en pie, la
siguiente tabla de instrumento puede traer la misma clase de celda y salir verde igual.**

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente,
paras y lo traes. No adivines.
