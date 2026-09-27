
---

# ACTA 50. VUELTA 51, lote 7 (`grove_high_output`), `cap_05`: **LA TANDA ES BUENA, SUS TRES PAGOS DE DEUDA CIERRAN, Y SU ARITMETICA SE CAE EN UNA CELDA**. Le verifico al digito las **cinco guardas**, los **cinco relojes**, los **seis informes de aduana** con sus **nueve pares de cola** al milesimo, el estado (`346`, `740`, `1`, `50`), el **tallado `240 / 130 / 110`** con su base `234 / 129 / 105` **reconstruida commit a commit**, el **censo `808`** con su base `803` **reconstruida igual**, el **sello `hash-object` de `D.52`** y **`PASOS INVENTADOS` contado por mi de las `51` fichas del libro sin mirar su instrumento**: me da `1/7`, `7/50`, `15/121`, `22/156`, `6/49` y `383`, su tabla entera. **FIRMO su `0` PUENTE de `49` pasos**, leidos por mi a ciegas contra `L21`, `L23`, `L33`, `L35`, `L37`, `L39`, `L41` y `L43`; **las dos guardas que declara mordiendo las vuelvo a morder por mutacion y muerden las dos**; y sus **tres pagos de deuda** (`d044`, `d045`, `d046`) los compruebo por prefijo y por clave: las tres fichas **anaden y no borran** y **solo `resumen_teorico` cambia**. **De sus TRECE discutibles marcados se sostienen los TRECE.** Y aun asi: **su tabla del techo publica `29,5` min donde su propia celda escribe `1728,2` s, que son `28,80`**, y eso vive en TABLA, asi que **`REPORTE` sube de `0 de 3` a `1 de 3`**. Sus otras dos caidas son **de PROSA y NO acumulan**: **`72` rancios donde el instrumento escribe `RANCIO 71`** (el `grep -c` se cuenta a si mismo la linea de resumen), y **`MM.4.a` dice `ocho` fichas y su propio parentesis enumera nueve**, que es lo que `git` da. `CIFRA PUBLICADA` sale **LIMPIA** y **baja de `1 de 2` a `0 de 2`** por la tanda limpia de `5.4` y `D.38.1`, no por indulto mio; `CLASE` y `DATO MOVIDO` salen **LIMPIAS** con su motivo medido: `740` contra `740` y `git diff` vacio sobre `dataset/`, `bitacora/`, `censos/`, `config/`, `esquema/`, `src/`, `scripts/`, `tests/`, `hooks/` y el banco. **Y DESENTIERRO DOS COSAS QUE NO SON CAIDA DE NADIE Y SE COBRAN EL DIA DE LA INSERCION**: los **nueve digitos de senial que las fichas llevan escritos dentro no se reproducen ni uno**, porque el bloque `VEREDICTO` que los escribe entra en el texto del que la senial se calcula (`6705` y `7217` caracteres de corte medidos, que son exactamente donde ese bloque empieza), **tercera generacion de `d038`**; y **hay una frontera real que ninguna maquina de esta casa va a levantar**, `cubrir_indicadores_problemas_reunion_individual` contra `dirigir_reunion_individual_semanal` del grafo, que **mandan cosas contrarias sobre con que se empieza la misma reunion** y miden `0,1125` contra un umbral de `0,35`, **mientras dos pares de hermanos miden `0,55`**. Las dos van **encargadas** y no solo agendadas. **Y MI PROPIA TANDA SALE LIMPIA**: remido una a una las cifras de mi pagina sellada sin que se mueva ninguna, y mi `HEREDADO 1` lo compruebo corriendo su instrumento **sobre la pagina ya sellada**, que devuelve las dos cabeceras identicas a las que la pagina publica. **`AUDITOR` se queda en `0 de 3`.** Ninguna condicion de parada se cumple: **no escribo `PARA_ALEXIS.md`**, y el encargo de la vuelta `52` sale de esta sede.

*Modo austero (`D.47`): no repito lo que el `loop.log`, el reporte o las actas anteriores ya dicen.*

## 50.1. LO QUE VERIFIQUE, CON MIS PROPIOS COMANDOS

El commit del extractor es `b04ac62`. **Mi `HEAD` al auditar es `3579674`**, que es el commit del arnes que sella mi apertura ciega y **no toca ni un fichero de dato**.

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python tests/test_aceptacion.py
      total: 318 pruebas, 0 fallos, 0 errores

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl

    $ for d in cuarentena/*/; do echo $d $(ls $d*.json | wc -l); done
    cuarentena/_derivadas/ 2            cuarentena/ensayo_referencia_163/ 163
    cuarentena/grove_high_output/ 50    cuarentena/marquet_turn_the_ship/ 3
    cuarentena/onu_consumidor/ 0        cuarentena/scott_radical_candor/ 0
    cuarentena/smart_who/ 0             cuarentena/zhuo_manager/ 0

Esas salidas miden las cuatro guardas de la casa corridas por mi en esta vuelta, las tres cuentas de estado que el encargo fijo por adelantado, y el reparto de las bandejas libro a libro.

`LECTURA`: **las cuatro cifras que el encargo predijo salen las cuatro** (`346`, `740`, `1`, `50`), y **las cuatro guardas verdes a la primera**. Y el reparto de bandejas contesta a la cifra de poblacion del informe sin que haya que creersela: `50` de `grove` mas `3` de `marquet` son `53`, y `346` mas `53` son los `399` con que cierra la sexta pasada.

### 50.1.a. Las cifras que solo se pueden comprobar recomputandolas

| lo que el reporte publica | donde | lo que me da a mi, con mi comando | |
|---|---|---|---|
| `8`, `4`, `10`, `10`, `7`, `10` pasos y `49` de tanda | `MM.2.c` | `.v51aud/03_pasos_cap05.py` sobre `pasos_accionables`, corrido en mi fase ciega: los seis y el `49` | **sale** |
| `124`, `18`, `187`, `195`, `145`, `134` palabras | `MM.2.a` | `sed` mas `wc -w` sobre `cap_05.md`, corrido en mi fase ciega: las seis al digito, y coinciden con las filas de `.v50/frontera_cap_05.txt` y con lo que las seis fichas declaran en su cabecera | **salen** |
| las `8` citas de linea con su `sed` | `MM.2.b` | `sed -n '21p;23p;33p;35p;37p;39p;41p;43p'`: las ocho reproducen | **salen** |
| relojes `253,2`, `374,4`, `339,8`, `317,1`, `350,7`, y el sexto sin medir | `MM.4.f` | leidos por mi de `.v51/reloj_c1.txt` a `.v51/reloj_c6.txt`: el `c1` dice literalmente `RELOJ:  s` | **salen** |
| suma `1635,2`, media `327,0` sobre `5`, contraste `461,3`, variacion `-29,1` por ciento | `MM.4.f` | recomputados por mi: `1635,2`; `1635,2/5` da `327,04`; `327,0/461,3` da `-29,1` por ciento | **salen** |
| poblaciones `394` a `399` y vecinos `0`, `0`, `1`, `1`, `3`, `4` | `MM.2.c` | leidos por mi de los seis `.v51/aduana_c*.txt`: las seis poblaciones y los seis recuentos | **salen** |
| los `9` pares de cola con sus nueve digitos | `MM.2.e` | contados por mi de los seis informes: `1` mas `1` mas `3` mas `4` dan `9`, y los nueve digitos son los suyos | **salen** |
| `6` de `9` por encima de `0,40` y `0` de `9` sin el `resumen_teorico` | `MM.2.e` | `.v51/cola_lectura.py` corrido por mi hoy: `6` y `0` | **salen** |
| `13` sitios de tentacion en `6` fichas | `MM.2.g` | filas de su tabla contadas por mi: `3` de `P6` y `2` de cada uno de los otros cinco dan `13` | **sale** |
| `0 CAERIA` y `0` choques en los seis | `MM.2.c` | los seis informes: `CAERIAN por una guarda : 0` y `CHOCAN entre si dentro del lote : 0` | **salen**, y digo lo que valen en `50.5.e` |
| `1/7`, `7/50`, `15/121`, `22/156`, `6/49` y `51/383` | `MM.4.e` | **conteo mio propio, por otro camino que el suyo**: `.v51aud/43_pasos_sin_doble.py` recorre bandeja mas `_insertados` mas grafo, deduplica el unico id que vive en los dos, y saca el capitulo del fichero fuente. **La tabla entera** | **sale** |
| tallado `240 / 130 / 110` y base `234 / 129 / 105` | `MM.4.k` | `scripts/tallar_reporte.py` hoy da `240 / 130 / 110`; reconstruido sobre el arbol de `3061fc2` da `234` declaradas, `128` talladas mas `1` que DIFIERE, o sea las `129` comprobables, y `105` PARCIAL | **salen las seis** |
| censo `803` a `808` | `MM.4.k` | reconstruido sobre `3061fc2` da `803` exacto (`621` mas `179` mas `3`); y el `REPORTE.md` de hoy aporta `626`, que son `5` mas | **salen** |
| deuda de `19` y `13` a `16` y `16` | `MM.4.h` | `scripts/deuda.py` hoy: `pendientes: 16    pagadas: 16`, y las `16` de la lista son las que el reporte imprime | **sale** |
| `9` de maquinaria, `1` de doctrina, `6` de trabajo | `MM.4.h` | contadas por mi de su lista: `9` mas `1` mas `6` dan `16` | **salen** |
| el sello `3b39a3fd` de `D.52` | `MM.4.c` | `git show 216b114:...` y la copia archivada dan los dos `3b39a3fd477a02d14ec5cdefb97255e689ae713c` | **sale**, y la cuarta linea ya no, ver `50.5.d` |
| `d044` da `2` y `1` por el metodo nuevo | `MM.1.c` | `.v51aud/18_comprobacion_d044.py` sobre la bandeja de `50`: `2` fichas declaran `P34` en su cabecera y `1` declara `P38` | **sale** |
| `2071` caracteres de correccion nueva en `P38` | `MM.1.c` | mi medida da `2072` en crudo y `2071` sin el espacio de cabeza. **Es convencion de borde, no cifra falsa**, y la declaro en vez de callarla | **sale con su nota** |
| `d045` y `d046` sin borrar | `MM.3` | prueba de prefijo y de claves en las tres fichas: `viejo es PREFIJO del nuevo: True`, `claves que cambian: ['resumen_teorico']`, y `pasos`, `titulo` y `atribuciones` identicos | **salen** |
| `cero` rancios sobre sus fichas | `MM.4.o` | `forja.py rancios` hoy: ninguna de las `9` fichas aparece en ninguna de las lineas `[RANCIO]` | **sale**, y su `72` no, ver `50.4.b` |

### 50.1.b. **EL CENSO ME DA OTRA CIFRA, Y LA DIFERENCIA ES MIA OTRA VEZ Y LA MIDO**

    $ python scripts/censar_rutas.py
    rutas publicadas y censadas : 805
      pasan                     : 805
      CAEN                      : 0

    $ python .v51aud/40_censo_por_doc.py
    docs/loop/REPORTE.md             censadas  626   pasan  626   caen 0
    docs/loop/ACTA_AUDITOR.md        censadas  179   pasan  179   caen 0
    docs/loop/APERTURA_CIEGA.md      censadas    0   pasan    0   caen 0
    APERTURA_CIEGA de b04ac62        censadas    3   pasan    3   caen 0

Esa segunda salida mide cuantas rutas censa cada uno de los tres documentos que `censar_rutas.py` barre, y cuantas censaba la `APERTURA_CIEGA.md` que el extractor tenia delante al cerrar.

`LECTURA`: el reporte publica `808` y yo saco `805`, y **la diferencia entera son `3` rutas de la apertura ciega anterior**, que el arnes rota en cada vuelta y la mia sustituyo. **`626` mas `179` mas `3` dan sus `808`, y `626` mas `179` mas `0` dan mis `805`.** **No es caida de nadie**, y es la **tercera acta seguida** que tropieza con la misma aritmetica (`ACTA 48` con `782` contra `780`, `ACTA 49` con `800` contra `798`). **Y la mia aporta `0` porque escribe sus rutas dentro de bloques de codigo sin comillas invertidas**, que es el mecanismo que mi propia `ACTA 48` adjudico.

## 50.2. LAS DOS GUARDAS QUE DECLARA MORDIENDO, VUELTAS A MORDER POR MUTACION (cosecha `7.C`)

**Este reporte declara dos guardas mordiendo, y no una:** la puerta de `D.39`, que es lo que impide que hoy entre un nodo (`MM.0.a`), y **el tallado, que su `MM.4.k` declara saliendo EN ROJO en su primera corrida.**

    $ python .v51aud/45_mutacion_puerta.py
    cerrados_en_extraccion en el repo      : ['scott_radical_candor', 'smart_who', 'zhuo_manager']
    grove_high_output CERRADO EN EXTRACCION: False    <- lo que el repo dice
    grove_high_output CERRADO EN EXTRACCION: True     <- con la celda mutada

    $ python .v51aud/46_mutacion_tallado.py
    SIN MUTAR              tablas comprobadas 240   DIFIEREN 0
    CON UNA CELDA MUTADA   tablas comprobadas 240   DIFIEREN 1

La primera salida mide la puerta de `D.39` sobre el `config/frentes.json` del repo y sobre una copia con la celda de `grove_high_output` anadida, fuera del arbol. La segunda mide el tallado sobre el reporte del arbol y sobre una copia con **una** celda de la tabla `D.52` de `MM.4.j` cambiada de `6 de 6` a `7 de 7`, tambien fuera del arbol.

`LECTURA`: **las dos muerden.** La puerta pasa de `False` a `True` con la unica celda que la decide, asi que **lee el estado y no una constante**; y el tallado pasa de `0` a `1` DIFIERE con una sola celda tocada, asi que **el rojo que `MM.4.k` cuenta es un rojo que esa guarda sabe dar**. Y mi reconstruccion de `50.1.a` lo confirma por el otro lado: el tallado corrido sobre el arbol de `3061fc2` **da exactamente `1` DIFIERE**, que es la tabla `D.52` de la vuelta 50 que `MM.4.k` describe. **Ni un byte del arbol vivo se toco para medir esto.**

## 50.3. LA RELECTURA CIEGA: **TRECE DISCUTIBLES MARCADOS, SE SOSTIENEN LOS TRECE**

**Empiezo por los marcados, que es lo que `5.1` manda**, y llego a ellos con los `49` pasos y los `8` renglones ya leidos en mi fase ciega, **antes de ver su tabla**.

| # | que sostiene | mi lectura, con lo que la sostiene | |
|---:|---|---|---|
| `1` | el paso `8` de `P6` es CONSECUENCIA y lo cuenta como paso | `L21` cierra con `which means that a scheduled meeting will have minimum impact`, y el paso lo transcribe con la forma `Cuenta con` que esta casa ya usa. Sin el, el sistema de control del paso `7` queda sin decir para que sirve | **SE SOSTIENE** |
| `2` | `P7` entra como nodo siendo enumeracion de `18` palabras | **es el marcado mas fragil y el propio extractor lo dice, y aun asi aguanta**: mi `ACTA 49` ya adjudico que la cabeza de serie de `cap_05` es `P7`, y la casa tiene el mismo molde escrito en `subir_productividad_gerencial_tres_vias`, que cuenta tres vias y las nombra. **Reabrirlo seria reabrir mi propia adjudicacion sin correccion declarada** | **SE SOSTIENE** |
| `3` | la arista de `P7` a sus cuatro partes es `D.29` y no `D.37` | es la aplicacion directa de `d045`, que yo firme en `49.5.d`: `D.37` ata la cabeza con las partes que **la cabeza NOMBRA**, y lo que `L23` nombra son **tres clases**. `P11` a `P14` no son clases: son la frecuencia, la duracion, la propiedad y el contenido de **una** de ellas | **SE SOSTIENE** |
| `4` | el paso `5` de `P11` es OBSERVACION que el libro aplaza | el contenido esta escrito entero en `L33`; lo aplazado es su desarrollo, no su enunciado. Y el `Accordingly` que abre la frase siguiente **cuelga de el**: sin el paso `5`, los pasos `6` y `7` son dos frecuencias sin criterio | **SE SOSTIENE** |
| `5` | mete `marketing` e `investigacion` dentro de los pasos `9` y `10` | los dos pasos escriben **`el libro pone como ejemplo`**, que es la forma declarada que manual `3.5` pide para el caso. **Meterlo sin declararlo seria la caida; declararlo es lo que la regla manda** | **SE SOSTIENE** |
| `6` | el paso `2` de `P12` es EXPERIMENTO MENTAL y es largo | `L37` lo escribe entero (`Look at it this way. If you had a big problem...`), y es el unico sitio del tramo que da el mecanismo del suelo de una hora. **Ninguna regla escrita de esta casa pone techo de longitud a un paso** | **SE SOSTIENE** |
| `7` | `P12` es UN nodo y no DOS | **y aqui la responsabilidad no es suya: el corte lo fijo MI encargo**, que da `P12` con `L37 a L39` y `1` nodo. El extractor siguio la tabla que yo le escribi. **Si hay que partirlo, es cifra mia y se corrige por correccion declarada**, no por una caida suya. Lo dejo medido en `50.5.f` | **SE SOSTIENE** |
| `8` | los pasos `4` y `5` de `P13` son EFECTOS del guion | misma familia que el `1`, y con el mismo apoyo: `L41` escribe `which is very important because it forces him...` y `Moreover, with an outline, the supervisor knows...`. Sin ellos el paso `3` es una orden sin motivo | **SE SOSTIENE** |
| `9` | deja el `ocho` de `P13` fuera de `atribuciones` | y es coherente dentro de la misma tanda: `P11` y `P12` **si** llevan atribucion porque sus cifras prescriben (`once a week`, `an hour at a minimum`), y el `ocho` de `L41` es aritmetica de un argumento (`would have to prepare eight times`). **La coherencia se ve en las tres fichas a la vez y por eso la firmo** | **SE SOSTIENE** |
| `10` | parte las cuatro clases de `L43` en cuatro pasos | el criterio va declarado antes de aplicarlo y es de forma del texto: dos puntos y lista frente al `such as` del paso `1`, que si se queda dentro. **Y no compra nada: el numerador de `PASOS INVENTADOS` es `0` con cuatro pasos y con uno** | **SE SOSTIENE** |
| `11` | el paso `10` de `P14` es OBSERVACION | misma familia que el `1` y el `8`. `L43` cierra con `These are often obscure and take time to surface` | **SE SOSTIENE** |
| `12` | publica `327,0` s sabiendo que sale de `5` pasadas | **y lo publica con el denominador pegado en los tres sitios donde la cifra aparece.** `EXTRACTOR.md` 5 manda decir que no hay cifra en vez de estimarla, y eso es lo que hizo. **La alternativa era la caida** | **SE SOSTIENE** |
| `13` | los `9` `SANO` viven dentro de la ficha y no en la bitacora | su sede esta cerrada por `D.39` y **no hay otra**. Mi propia adjudicacion de `d027` dice que una ficha de cuarentena **no es sede de `5.2`**, asi que escribir ahi no publica una cifra: deposita una razon. **Y los nueve la llevan**, medido en `50.7` | **SE SOSTIENE**, y con la factura que cobro en `50.5.a` |

`LECTURA`: **`13` de `13` en pie, `0` caidas DENTRO del marcado y `0` FUERA de el en materia de lectura.** Y digo lo que eso vale y lo que no: el extractor marco **once decisiones de lectura y dos del cierre**, y **ninguna de las trece es una cifra**. Las tres caidas que si encuentro estan **fuera** de su marcado y son **de aritmetica y de recuento**, que es justo donde el marcado no miro.
