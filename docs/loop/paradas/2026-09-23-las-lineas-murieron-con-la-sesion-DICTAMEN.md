# DICTAMEN, 23 SEP 2026: **LAS DOS LINEAS MURIERON CON LA SESION QUE LAS LANZO**

*Especie **ARNES**. Lo escribe la sesion de chat por el mandato del fundador del `22` sep
(`2026-09-22-tu-lanzas-MANDATO.md`, punto `2.a`): arreglarlo con caso positivo y negativo,
dictamen aqui, y relanzar. **No hay racha que reiniciar ni decision del fundador que pedir.**
Lo detecto el fundador a las `06:05`: *me parecio que estaba detenido*. Lo estaba.*

---

> ## **CORRECCION DECLARADA, 23 SEP A LAS 08:00: LA CAUSA DE LA PRIMERA MUERTE NO FUE LA SESION**
>
> ~~las mato el cierre de esa sesion~~ **Las mato un REINICIO DE WINDOWS UPDATE** a las
> `00:29:59` (`KB5124010`), medido en el visor de eventos por la decision del fundador del `24`
> sep: `MoUsoCoreWorker.exe` inicio el reinicio, el sistema se apago a las `00:31:35`, y
> `TrustedInstaller` lo reinicio otra vez a las `00:32:52`. **La sesion murio de lo mismo.** La
> segunda muerte, la de WMI, coincide con **otro actor de git en la carpeta** (un `fetch` de las
> cinco ramas a las `06:30:38`). Dictamen entero en
> `2026-09-24-una-carpeta-un-actor-DECISION.md`. **El lanzador vigente es la tarea programada
> con la ventana oculta** (`PARALELO.md` `7.a`), y **ningun lanzador sobrevive a un reinicio.**

## 1. LO QUE PASO

Las dos lineas se lanzaron el `23` sep a las `00:03:25` con `nohup ... &` desde el shell de
la sesion de chat. **Las dos murieron sin escribir `PARA_ALEXIS.md`**, porque no pararon:
**las mato el cierre de esa sesion**, que se llevo su arbol de procesos entero. `nohup` no
protege de eso en Windows.

| linea | donde murio | la ultima linea de su log |
|---|---|---|
| **serial** | **en plena fase ciega** de la vuelta `63` | `00:18:08  y solo eso: remedios con su motivo, sin cifras ni conclusiones (D.52)` |
| **marquet** | **a mitad del turno de su extractor** (vuelta `5`) | `00:03:27  VUELTA 1 : EXTRACTOR (claude-sonnet-5, esfuerzo defecto)` |

## 2. LO QUE SE COMPROBO ANTES DE TOCAR NADA, Y NO SE PERDIO NADA

    $ python forja.py gate
    GATE VERDE.  nodos verificados: 346
    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl
    346 / 740
    $ git status --short dataset/ bitacora/ censos/
    (vacio)

**CERO NODOS PERDIDOS, CERO VEREDICTOS MOVIDOS.** Grove sigue con `91` en bandeja y `1` en
`_insertados/`, como al lanzar.

### 2.a. **El refugio de la fase ciega estaba entero**

La fase ciega aparta cuatro ficheros a un directorio temporal y los devuelve al cerrar.
**No llego a cerrar**, asi que faltaban del arbol, **entre ellos el reporte de la vuelta
`63`, que solo existia alli**. Estaban intactos en `/tmp/tmp.Pz22BHgNbX`:

    CREDITO_serial.jsonl    IDENTICO a HEAD
    ultimo_auditor.json     IDENTICO a HEAD
    REPORTE.md              el de la vuelta 63, mas nuevo que el del indice
    ultimo_extractor.json   el del turno del extractor

**Se devolvieron los cuatro**, que es exactamente lo que el arnes habria hecho.

### 2.b. **La fase ciega interrumpida se ANULA**

Una fase ciega sin sello no es una fase ciega: el sello prueba que la clasificacion se
escribio antes de ver el reporte (`D.34.2`, `D.46`). `APERTURA_CIEGA.md` y
`ultimo_apertura.json` vuelven a su version commiteada, y la evidencia del ciego se archiva
en `docs/loop/archivo/interrumpidas/2026-09-23-v63-fase-ciega/` **sin reutilizarse**.

### 2.c. **El trabajo del extractor de la `63` se conserva**

Seis correcciones de fidelidad **declaradas y hechas antes de insertar**, en `cap_02` y
`cap_03`, y su reporte, **que abre con las tareas en `PENDIENTE` y dice que, si la vuelta se
corta, lo que siga pendiente es hasta donde se llego**. Es trabajo bueno y lo audita el
auditor de la `63`, desde una fase ciega nueva.

### 2.d. **El cerrojo del dataset quedo echado por un proceso muerto, y se cura solo**

    procesos/nodos.jsonl.679b2259.cerrojo   {"pid": 14980, "desde": 00:13:40}
    $ tasklist //FI "PID eq 14980"
    INFO: No tasks are running which match the specified criteria.

**No se toca a mano.** `src/cerrojo.py` rompe un cerrojo cuyo dueno no se puede probar vivo
cuando pasa de `TOPE_DE_HUERFANO` (`15` min), **y lo declara**. El proximo `insertar` lo hara.

---

## 3. LOS DOS DEFECTOS, Y SON DOS

### 3.a. **EL LANZAMIENTO. Mio.**

Lanzar con `nohup` desde el shell de la sesion ata la linea a la sesion. **Se lanza ahora
con `scripts/lanzar_linea.ps1`**, que crea el proceso **a traves de WMI**
(`Win32_Process.Create`): su padre es el servicio `WmiPrvSE`, no el shell que lo pide, y
**sobrevive a la sesion**. Comprobado antes de usarlo:

    padre: WmiPrvSE
    /c/Users/AlexDesk/AppData/Roaming/npm/claude
    2.1.280 (Claude Code)
    TEMP=/tmp

**Y UNA TRAMPA QUE SALIO AL PROBARLO:** `bash.exe` a secas resuelve en Windows a
`C:\WINDOWS\system32\bash.exe`, **que es el de WSL** y corre en otro sistema de ficheros. El
script usa el Git Bash por su ruta: `C:\Program Files\Git\usr\bin\bash.exe`.

> ### **CORRECCION DECLARADA DEL MISMO DIA, 06:30: EL LANZADOR POR WMI TAMPOCO SIRVIO**
>
> ~~Se lanza ahora con `scripts/lanzar_linea.ps1`, que crea el proceso a traves de WMI [...] y
> sobrevive a la sesion.~~ **Relanzadas asi a las `06:25`, las dos murieron a los `90`
> segundos**, la serial otra vez en plena fase ciega. **La causa: WMI crea cada proceso con su
> PROPIA VENTANA DE CONSOLA**, vacia porque la salida va al log. El fundador las vio abrirse
> vacias y lo pregunto: *se abrieron dos ventanas del terminal de windows, pero estaban vacias,
> sin proceso alguno*. **Esas ventanas eran las lineas.** Mi prueba duro `20` segundos y no
> llego a verlo. **El refugio volvio a estar entero** (`/tmp/tmp.KAjV0caXLi`, los cuatro
> identicos a `HEAD`) y se restauro desde git: gate VERDE, `346`.
>
> **EL LANZADOR BUENO, probado con un trabajo de `150` segundos antes de usarlo:** una **tarea
> programada** de Windows (`forja_linea_<nombre>`) que corre `wscript` con un `.vbs` que arranca
> el Git Bash **con la ventana oculta y sin esperarlo**. Sin ventana que cerrar, y lanzado por el
> servicio del programador, no por esta sesion. **Y el pid que se vigila es el del bash
> envoltorio en el espacio de Git Bash** (`<log>.pid`, con `kill -0`): los pids de Windows no
> sirven, porque Git Bash cambia de proceso de Windows en cada `exec`, y eso fue lo que hizo
> creer al vigia que la serial habia muerto antes de que muriera de verdad.
>
>     06:32:31  relanzadas las dos por tarea programada
>     06:35:26  serial VIVO, marquet VIVO: pasada la marca de los 90 segundos

### 3.b. **UNA INSERCION SOBREVIVIO A SU TURNO. Del arnes.**

El extractor de la `63` **lanzo su primera `forja.py insertar` en segundo plano** a las
`00:13:40` y cerro su turno a las `00:18:07` con esta frase:

> *Both background jobs are still running; I'll pick up as soon as the insertion 1 result lands.*

**No la recogio nadie.** El arnes abrio la fase ciega encima, y la insercion murio **con su
fichero de salida en la cabecera y el cerrojo echado**. Salio bien por suerte: murio antes de
tocar `nodos.jsonl`. **Una insercion cortada DESPUES de escribir es la que perdio un nodo y
dio nacimiento a `D.44`.**

**Y es la tercera vez que esta casa ve un proceso sobrevivir a su turno**: el informe de lote
que `D.43` saco del turno fue la primera, y el auditor ciego de esta misma vuelta hizo lo
mismo con `16` informes, que quedaron en `0` bytes.

**EL ARREGLO, en las dos puntas:**

1. **EN EL ORIGEN**, el mandato de insercion del arnes: *CADA `python forja.py insertar` SE
   CORRE EN PRIMER PLANO Y ESPERAS A QUE VUELVA: NUNCA la lances en segundo plano, y NUNCA
   termines tu turno con una insercion en vuelo.*
2. **EN LA GUARDA**, entre el turno del extractor y la fase ciega: si el cerrojo sigue echado,
   el arnes **lo dice**; si su dueno vive, **lo espera** hasta `ESPERA_INSERCION`; y si no se
   suelta, **comprueba el grafo**. Gate verde: se dice y se sigue. **Gate rojo: se para con
   `PARA_ALEXIS`**, porque eso ya es un dato en rojo tras una insercion cortada.

**SUS CASOS, en el banco del arnes:**

| escenario | que prueba | |
|---|---|---|
| `20` | cerrojo echado por un proceso MUERTO: lo dice, lo da por interrumpido, gate verde, sigue al auditor | positivo |
| `20b` | cerrojo echado por un proceso VIVO que lo suelta: lo espera y lo ve terminar | positivo |
| `20c` | sin cerrojo no hay aviso, y en `cuarentena` no se mira siquiera | negativo |

    RESULTADO: 171 comprobaciones en VERDE, 0 en ROJO
    total: 374 pruebas, 0 fallos, 0 errores

---

## 4. EL RELANZAMIENTO

**Las dos lineas se relanzan con `scripts/lanzar_linea.ps1`**, con los comandos del fundador
intactos en sus variables. **La serial arrancara por el AUDITOR**: su reporte de la `63` es
mas nuevo que su acta, y el arnes lo mide solo (`ROL INICIAL POR MEDICION`). **Marquet**
retoma su vuelta `5` con un aviso al principio del encargo: **los tres candidatos que dejo su
turno muerto son un borrador**, y los adopta con su aduana guardada o los retira con motivo.
