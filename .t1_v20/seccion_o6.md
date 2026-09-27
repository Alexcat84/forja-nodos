
---

# O.6. EL CIERRE DE LA VUELTA 20

*`EXTRACTOR.md` 1.5: gate, barrido y prueba de aceptacion en verde, cifras del cierre
**recomputadas al cierre**, discutibles marcados, commit y push. **Y el encargo lo repite dos
veces en mayusculas: cierra tu reporte.***

## O.6.1. LAS CINCO GUARDAS, CON SU SALIDA PEGADA

    $ python forja.py gate
      GATE VERDE.
        nodos verificados: 203
        guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada,
                 vuelta, cita_incompleta, deprecado_en_superficie, arista_rota,
                 arista_incompleta, guiones

    $ python forja.py guiones
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python forja.py resolutor
      nodos vivos: 203
      nodos deprecados (archivo): 0
      alias registrados: 0

    $ python forja.py rancios
      BLOQUE DE VIGENCIA VERDE.
        veredictos comprobados: 148
        citas de enlace mutuo comprobadas: 0
        todos siguen emitidos contra el texto que leyeron

    $ python tests/test_aceptacion.py
      total: 90 pruebas, 0 fallos, 0 errores
    $ grep -c "def test_" tests/test_aceptacion.py
      90

**LAS CINCO EN VERDE.** Y **`90` y no `84`**, que es la cifra que mi `N.6.1` publico: las seis
nuevas entraron en `a653ffd`, **despues** de la vuelta 19, con el arreglo del falso positivo de
`D.40`. **El auditor ya midio esta discrepancia en su `1.2` y la resolvio como dos relojes y no
como caida; hoy es simplemente la cifra de hoy**, y la publico con su `grep -c` al lado para
que no haya que volver a resolverla.

### O.6.1.b. **LA GUARDA `guiones` MORDIO TRES VECES, Y LAS TRES EN MI PROPIA MANO**

*`LA GUARDA QUE NO MUERDE ES CIFRA` (cosecha `7.C`). **Esta mordio, y no en los candidatos: en
mis guiones de un solo uso.***

    $ python forja.py guiones      (primer intento de commit del cierre de cap_09)
      BARRIDO DE GUIONES EN ROJO: 4 hallazgo(s)
        .t1_v20/citas5.py linea 9 columna 22: guion largo (U+2014)
        .t1_v20/citas5.py linea 9 columna 41: guion medio (U+2013)
        .t1_v20/frontera10.py linea 63 columna 22: guion largo (U+2014)
        .t1_v20/frontera10.py linea 63 columna 41: guion medio (U+2013)
    $ python forja.py guiones      (tras reescribirlos con escape)
      BARRIDO DE GUIONES EN ROJO: 2 hallazgo(s)
        .t1_v20/sin_guiones.py linea 7 columna 8: guion largo (U+2014)
        .t1_v20/sin_guiones.py linea 7 columna 30: guion medio (U+2013)
    $ python forja.py guiones      (tras reescribir el reescritor con chr())
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

> **EL HOOK SE DEJO CORRER Y ABORTO EL COMMIT, que es lo que `EXTRACTOR.md` 6 manda: `[pre-commit] COMMIT ABORTADO`.** No lo salte.
>
> **Y LA CAUSA ES LA MISMA LAS TRES VECES, y merece una linea porque es estructural y no
> torpeza:** los guiones normalizan las comillas tipograficas y los guiones largos del libro
> para poder pegar la cita en el reporte, **y para normalizar un caracter hay que teclearlo.**
> La tercera version lo escribe con `chr(0x2014)` y la guarda la deja pasar. **Es la segunda
> vuelta seguida que esta guarda muerde en un guion de un solo uso** (la 19 fue en `.c9/mk.py`),
> y las dos veces por el mismo motivo.
>
> **NO PROPONGO NADA** (moratoria, `EXTRACTOR.md` 13): `chr()` funciona y cuesta una linea.

## O.6.2. EL ESTADO AL CIERRE, **MEDIDO AL CIERRE** (`EXTRACTOR.md` 4)

| medida | al abrir (`O.0`) | **al cerrar, remedido** | |
|---|---:|---:|---|
| nodos en el grafo | 203 | **203** | **el grafo cierra donde abrio** |
| veredictos en bitacora | 148 | **148** | **cero veredictos nuevos** |
| pares mutuos | 1 (la cabecera) | **1** | sede sin estrenar |
| candidatos del lote 4 en cuarentena | 78 | **83** | **mas 5, los de hoy** |
| pasos de esos candidatos | 761 | **856** | **mas 95** |
| veredictos de `scott_radical_candor` | 0 | **0** | `grep -c scott` |
| lineas del reporte | 23.670 | **se recomputa en `O.6.9`** | crece por anexion |

    $ wc -l < dataset/nodos.jsonl        -> 203
    $ wc -l < bitacora/VEREDICTOS.jsonl  -> 148
    $ wc -l < config/pares_mutuos.jsonl  -> 1
    $ ls cuarentena/scott_radical_candor/*.json | wc -l  -> 83
    $ grep -c scott bitacora/VEREDICTOS.jsonl           -> 0
    $ python .t1_v20/reparto.py
      cap_01:   1 cand,    9 pasos      cap_06:  10 cand,  117 pasos
      cap_03:   1 cand,    7 pasos      cap_07:  25 cand,  225 pasos
      cap_04:   6 cand,   48 pasos      cap_08:  12 cand,  102 pasos
      cap_05:   8 cand,   76 pasos      cap_09:  20 cand,  272 pasos
      TOTAL:  83 cand, 856 pasos
      FILA DE RESIDUO 'SIN' -> 0 ids: []

> ### **CERO INSERCIONES, CERO VEREDICTOS, EL GRAFO EN 203 AL ABRIR Y AL CERRAR. ES LA REGLA FUNCIONANDO Y NO UNA VUELTA PERDIDA.**
> `D.39` abre la insercion de un lote **CERRADO**, y el lote 4 cierra esta vuelta con
> **`cap_10` a `cap_14` sin minar: 36.656 palabras de cuerpo**, medidas al cierre:
>
>     $ for f in fuentes/scott_radical_candor/cap_1[01234].md; do sed -n '8,$p' $f | wc -w; done
>       8976  8626  2118  9298  7638      (suman 36.656)

### O.6.2.b. **UNA FILA DE MI PROPIA APERTURA QUE CORRIJO, Y ES CORRECCION DECLARADA SOBRE ESTE MISMO REPORTE**

*Nadie me la ha pedido. **La cazo al remedir al cierre**, que es para lo que `EXTRACTOR.md` 4
manda remedir.*

**LO QUE PUBLIQUE** en `O.0`, en la tabla de la octava medida:

    cuarentena/_insertados/           -> 0

**LO QUE HAY:**

    $ ls cuarentena/_insertados/*.json 2>/dev/null | wc -l
      0                <- cierto: en la RAIZ de esa carpeta no hay ningun json
    $ find cuarentena/_insertados -name "*.json" | wc -l
      201              <- pero hay 201 repartidos en sus tres subcarpetas
    $ ls cuarentena/_insertados/
      onu_consumidor  smart_who  zhuo_manager

> **EL `0` ES CIERTO PARA EL COMANDO QUE LLEVA PEGADO Y FALSO PARA LO QUE UN LECTOR ENTIENDE.**
> `D.31` manda archivar cada insertado en `cuarentena/_insertados/<libro>/`, **con el libro
> como subcarpeta**, asi que un glob de un solo nivel **nunca** los ve. Quien lea esa fila
> entiende *no se ha insertado nada nunca*, y lo cierto es **201 de los 203 nodos del grafo
> estan archivados ahi.**
>
> **ES LA ORDEN B DEL AUDITOR APLICADA A MI, Y LA HEREDE SIN MIRARLA:** la tabla viene tal cual
> de mi `N.0` de la vuelta 19, **con su comando pegado y su rotulo prometiendo mas de lo que el
> comando comprueba.** El auditor cayo en esa misma especie en su `7.1` con la cabecera
> `UNIDAD DE ORIGEN:`. **La diferencia es que la suya estaba sellada y la mia la cazo el
> remedir del cierre.**
>
> **NO TOCO LA FILA DE `O.0`**, que es lo que esta casa hace con una cifra publicada: **la
> correccion vive aqui**, y es *en la raiz 0, en el arbol 201, y la conclusion buena de esa
> fila es que **el lote 4 no ha insertado nada**, no que nadie haya insertado nunca*.

## O.6.3. `PASOS INVENTADOS POR CAPITULO`, CON EL TOTAL DEL LOTE (`AUDITOR_FORJA.md` 8)

*El freno va aparte y entero, **fila por capitulo mas total del lote**, y la escalada se decide
**sobre el peor capitulo y no sobre el promedio** (`8.2`). Tope **10**.*

| unidad | rotulo | cuerpo | numerador | denominador | **tasa** | quien firma |
|---|---|---:|---:|---:|---:|---|
| `cap_00` | `Copyright Page` | 218 | 0 | 0 | **sin definir** | denominador mio |
| `cap_01` | `Preface` | 2.846 | 0 | **9** | **0,00** | numerador **heredado** |
| `cap_02` | `Introduction` | 3.908 | 0 | 0 | **sin definir** | denominador mio |
| `cap_03` | `How to Use This Book` | 627 | 0 | **7** | **0,00** | numerador **heredado** |
| `cap_04` | `Cap. 1` | 6.263 | **3** | **48** | **6,25** | numerador **heredado** |
| `cap_05` | `Cap. 2` | 8.756 | **2** | **76** | **2,63** | numerador **heredado** |
| `cap_06` | `Cap. 3` | 11.587 | 0 | **117** | **0,00** | firmada por la `ACTA 19` |
| `cap_07` | `Cap. 4` | 13.678 | 0 | **225** | **0,00** | firmada por la `ACTA 19` |
| `cap_08` | `Cap. 5` | 6.140 | 0 | **102** | **0,00** | firmada por la `ACTA 18` |
| **`cap_09`** | **`Cap. 6`** | **17.482** | **0** | **272** | **0,00** | **los 177 de la vuelta 19 los firmo la `ACTA 19` entera; los 95 de hoy los firmo yo** (`O.3.e`) |
| | **lote 4 hasta `cap_09`** | **71.505** | **5** | **856** | **0,58** | denominador remedido al cierre |

    $ python (la tabla, desde el arbol)
      LOTE 4 hasta cap_09: cuerpo 71505  num 5  den 856  tasa 0.58

> ### **LA FILA QUE DECIDE ES LA PEOR, Y SIGUE SIENDO `cap_04` CON `6,25` CONTRA UN TOPE DE `10`. EL FRENO NO SE DISPARA Y EL TRAMO NO BAJA.**
>
> **Y REPITO LA CAUTELA QUE ESCRIBI CONTRA MI MISMO EN LAS DOS VUELTAS ANTERIORES, porque hoy
> vuelve a aplicar y con mas fuerza:** el total del lote baja de **0,66** a **0,58** **sin que
> se haya corregido ni un puente.** Los cinco siguen donde estaban; lo unico que ha cambiado
> es que hay **95 pasos mas debajo**. **Una tasa que baja porque el denominador crece no es
> una mejora de la mano**, y por eso `8.2` manda decidir sobre la fila y no sobre el promedio.
>
> ### **Y EL NUMERADOR DE `cap_09` NECESITA UNA LINEA, PORQUE HOY NO ES UN CERO LIMPIO.**
>
> **La relectura `D.30` cazo UN puente en mis 95 pasos** (`O.3.e`, la cuenta que el libro no
> escribe, en `P16` de `P28`). **Lo pongo en `0` porque el numerador de esta tabla cuenta
> puentes QUE SIGUEN EN EL ARBOL**, y este se corrigio antes de dar el candidato por escrito y
> antes de su re informe. **Pero la cifra honrada de mi mano no es `0 de 95`: es `1 de 95`
> escrito y `0 de 95` publicado**, y las dos van dichas. Si el auditor quiere el numerador con
> el otro criterio, la tasa de `cap_09` seria `0,37` **y seguiria sin disparar nada.**

## O.6.4. LAS **DOCE** COLAS DE ARISTA, **NINGUNA ESCRIBIBLE HOY** (`D.29`)

*El encargo manda repetirlas al cierre hasta que el lote 4 cierre, **sin inventarles sede y sin
resumirlas**. Las **diez** heredadas siguen enteras, la **once** me la da el auditor en su
`1.b` fila 5, y la **doce** la abre esta vuelta.*

| # | madre | hijo o hijos | por que hoy no |
|---:|---|---|---|
| **1** | `revisar_ciclo_responsabilidades_relaciones` **P3** | las cabezas de `cap_05`, `cap_06` y `cap_07` | **la madre vive en cuarentena.** Sin cambio |
| **2** | `gestionar_personas_equipo` **P2** (Zhuo, **en el grafo**) | `desplegar_marco_franqueza_radical` (bandeja) | el hijo vive en un lote **ABIERTO**. **Cruza de libro, y `0` aristas cruzan de libro sobre las `79` del grafo.** Sigue sin estrenarse |
| **3** | `empezar_cultura_franqueza_radical` **P3, P5 y P6** | `pedir_critica_equipo_premiarla`, `elogiar_trabajo_especifico_contexto`, `criticar_trabajo_evitar_desanimo` | **los cuatro en cuarentena.** Sin cambio |
| **4** | `repartir_tiempo_atencion_mejores_equipo` **P3** (Zhuo, **en el grafo**) | `acompaniar_mejores_equipo_socio` (bandeja) | el hijo vive en un lote **ABIERTO**. **Cruza de libro.** Sigue siendo la que mas corre |
| **5** | `recorrer_rueda_hacer_cosas_equipo` **P2 a P8**, el radio `LISTEN` | `adaptar_escucha_cultura_ajena` | los dos en cuarentena, y `LISTEN` **no tiene cabeza propia** |
| **6** | `dominar_arte_socializar_trabajo` **P9** | `evitar_presion_social_actos_equipo` | los dos en cuarentena |
| **7** | `practicar_franqueza_radical_jefe_propio` **P14** (`L217`) | **SEIS hijos**: `dar_guia_humilde_tres_tecnicas`, `dar_guia_util_cuatro_recordatorios`, `dar_guia_acto_cinco_consejos`, `elegir_medio_dar_guia_jerarquia_modos`, `elogiar_publico_criticar_privado_sus_tres_matices`, `evitar_personalizar_guia_aceptar_personal` | **los siete en cuarentena.** `D.29` y **no** `D.37`: el texto los nombra **y no dice `six`** |
| **8** | `evitar_personalizar_guia_aceptar_personal` **P5** (`L169`) | `dar_guia_humilde_tres_tecnicas` | los dos en cuarentena |
| **9** | `exigir_critica_jefe_reticente` **P9** (`L299`) | `abrazar_incomodidad_arrancar_critica_equipo` | los dos en cuarentena |
| **10** | `elogiar_publico_criticar_privado_sus_tres_matices` **P9** (`L163`) | `fomentar_guia_reciproca_companieros` | los dos en cuarentena |
| **11. DEL AUDITOR** (`ACTA 19` `1.b` fila 5) | `evitar_personalizar_guia_aceptar_personal` (`cap_09`, 12 pasos) | `manejar_enfado_persona_desafiada` (`cap_04`, 7 pasos) | los dos en cuarentena **y los dos del lote 4**. **NO cruza de libro**, contra lo que yo escribi primero y el `ls` tumbo (`O.2.c`): **cruza de capitulo dentro del mismo libro**, asi que **se desbloquea con un solo acto**. Veredicto `CONTINUA` ya adjudicado: **los dos se quedan y entre ellos hay arista** |
| **12. NUEVA, DE ESTA VUELTA** | `conducir_reuniones_salto_nivel_diez_reglas` (`P27`, `L383` a `L413`) | `resolver_dudas_frecuentes_reuniones_salto_nivel` (`P28`, `L415` a `L425`) | los dos en cuarentena. **Razon escrita entera en `O.3.f`**: las cuatro preguntas de la hija son preguntas sobre el procedimiento de la madre, y su rotulo es `Skip level meeting FAQs`. **Es `D.29` y no `D.37` porque `L417` dice `some of the questions` y no dice cuantas** |

> ## **DOCE COLAS VIVAS, Y ONCE DE LAS DOCE SE DESBLOQUEAN CON EL MISMO ACTO: EL CIERRE DEL LOTE 4.**
> **Solo las numeros 2 y 4 necesitan dos cierres, porque cruzan de libro.** Y la cifra sigue
> creciendo: **cuatro al cerrar la 17, seis al cerrar la 18, diez al cerrar la 19, doce hoy.**
> **La deuda de aristas del lote 4 no se estabiliza, se acumula**, y lo digo con las cuatro
> cifras al lado en vez de repetir las colas sin contarlas. **No es parada:** el encargo lo
> pone por su nombre en la lista de lo que no para.

### O.6.4.b. **LO QUE `cap_10` DEBERA DECLARAR, FUERA DEL RECUENTO DE LAS DOCE**

*Va aparte **a proposito**: una cola de arista lleva madre e hijo nombrados por su id, y
**ningun candidato de `cap_10` existe**. Meterlo en el recuento inflaria la cifra con la
especie equivocada.*

| | |
|---|---|
| **la cabeza** | `P24` de `cap_10` (`L169` a `L173`), que dice `if you do three things` |
| **las tres partes** | `P25` (`L175`, *Don't wait too long*), `P26` (`L181`, *Don't make the decision unilaterally*), `P27` (`L189`, *Give a damn*) |
| **la coda, fuera de la serie** | `P28` (`L197`, *Follow up*): se hace **al mes de haber despedido**, no antes |
| **por que es `D.37` y no `D.29`** | **la cuenta esta escrita** (`three things`) y las partes **existiran como nodos**, que es lo que `D.37` pide. **Es el primer `D.37` de verdad cableable del lote 4**: la de `L317` de `cap_09` no lo era porque sus cuatro partes eran pasos de un solo nodo |
| **quien la declara** | **quien extraiga `cap_10`, en su misma vuelta** (`D.37` literal). Yo la levanto con su cita y su marco en `O.4.d` y **no la resuelvo**, porque no he escrito los pasos |

## O.6.5. LAS LECTURAS `SANO` SIN SEDE, **CONTADAS POR PARES Y CON SU DENOMINADOR NOMBRADO**

*El criterio ya esta adjudicado y no lo reabro: **una lectura `SANO` sin sede es UN PAR
(candidato contra vecino) leido y clasificado cuya linea no ha podido escribirse.***

**LAS MIAS DE ESTA VUELTA, CONTADAS POR PARES: CERO. Y es una medida, no una omision:**

    $ grep -c "umbrales de esta corrida" .aduana_v20/informes.txt
      6            <- los seis informes corrieron con los tres umbrales puestos
    $ grep -c "BLOQUEARIAN esperando veredicto  : 0" .aduana_v20/informes.txt
      6            <- y los seis dieron CERO vecinos que leer
    $ grep -cE "^  (similitud_texto|familia_id|paso_contra_nodo)" .aduana_v20/informes.txt
      0            <- ni una linea de vecino en los seis informes

| de donde saldrian | cuantos pares | por que |
|---|---:|---|
| los 5 candidatos de hoy | **0** | **la aduana levanto CERO vecinos en los cinco.** Sin par levantado no hay par que leer |
| la arista `D.29` numero 12 | **0** | **es un par de JERARQUIA declarada, no un veredicto `SANO`.** Un hijo no es un gemelo, y meterlo aqui inflaria la cifra con la especie equivocada |
| la `D.37` de `cap_10` | **0** | **sus nodos no existen.** No hay par |

> ### **Y CERO VECINOS EN CINCO CANDIDATOS DE UN CAPITULO MONOTEMATICO NO ES UNA BUENA NOTICIA: ES `D.19` POR TERCERA VUELTA SEGUIDA.**
> La aduana compara **contra el grafo**, y el grafo tiene **0 de 203** nodos de
> `scott_radical_candor`. **Mis cinco hablan de critica, de genero, de evaluaciones y de
> reuniones, exactamente igual que los quince de la vuelta 19, y la senial no ve ni uno.** El
> barrido `D.38.4` del auditor sobre **grafo mas bandejas** levanto 8 vecinos donde la aduana
> levanto 0, **y esa es la unica razon por la que el par de la cola 11 existe en algun papel.**

**EL ACUMULADO, CON SUS DOS DENOMINADORES SEPARADOS Y SIN SUMARLOS A CIEGAS:**

| | |
|---|---:|
| acumulado del extractor al cerrar la `ACTA 18`, **sobre poblacion de solo grafo** | **10 pares** |
| **mios de la vuelta 19** | **0 pares** |
| **mios de la vuelta 20** | **0 pares** |
| **acumulado del extractor, mismo denominador** | **10 pares** |
| **mas los del auditor en la `ACTA 19`, sobre grafo MAS bandejas** | **8 pares** |
| **total que el acta publica** | **18 pares, y los denominadores NO son el mismo** |

**NO SUMO POBLACIONES DISTINTAS SIN DECIRLO**, que es como se fabrican las cifras que nadie
puede reproducir. **Los 18 se resuelven de golpe el dia que el lote 4 entre en el grafo.**

## O.6.6. LAS PARADAS, REPASADAS UNA A UNA (`EXTRACTOR.md` 7)

| condicion | |
|---|---|
| **contradice una regla vigente** | **NO.** Las dos tensiones que lo parecian estan adjudicadas y las obedezco: `12.4` punto 4 (**un capitulo no se parte**, y hoy ninguno queda partido) y las `four rules of thumb` de `L317` (**la serie es de cuatro**, y asi esta escrita en `P23`) |
| **contradice una cifra publicada con su corte** | **NO.** El `90` contra `84` de las pruebas queda resuelto con su causa y su `grep -c` (`O.6.1`); el `0` de `_insertados` lo corrijo yo mismo con su `find` (`O.6.2.b`); y el `40` contra `35` de la ruta de la vuelta 19 **lo acepto entero como caida mia** (`O.2.d`) |
| **un pendiente de doctrina** | **NO DETIENE**, por su propia letra. Hay **uno** vivo y queda marcado: **el corte fino contra el grueso de `P21` de `cap_10`** (discutible 1). **Registro lo mejor sostenido, lo marco, y sigo** |
| **una operacion cuyo texto no alcanza para ejecutarse sin decidir** | **NO.** El punto 4 del encargo me deja decidir y **la cuenta esta publicada** (`O.4.e`), no escondida en un adjetivo |
| **decision de Alexis reservada** | **NO detiene esta vuelta.** Sigue viva la de los ficheros de usar y tirar del arbol (`ACTA 19` `7.6`), **y yo he anadido `.aduana_v20/` y `.t1_v20/`**. `AUDITOR_FORJA.md` 3 reserva a Alexis borrar lo que ninguna regla ordena borrar, **y no fabrico una parada para poder borrarlos** |
| **fallo tecnico repetido** | **NO.** Las cinco guardas en verde. Los dos rojos de la vuelta fueron **mios y en mis propios guiones**: la guarda `guiones` (`O.6.1.b`) y el `\r` de mi lista de rutas (`O.3.d`), **los dos con su salida pegada y su causa dicha** |

> # **NO HAY PARADA. LA VUELTA CIERRA CON SU REPORTE ESCRITO.**

## O.6.7. **EL REMEDIO DE `O.2.d`, AUDITADO CONTRA MI PROPIO REPORTE**

*Prometi esta seccion en `O.2.d` y aqui esta con su numero. **Toda ruta que este reporte
publica como prueba, con el comando que la cuenta y su salida.** Si falta una, se cobra.*

| ruta que publico como prueba | el comando que la cuenta, y su salida | lo que mi reporte cita | |
|---|---|---|---|
| `.aduana_v20/informes.txt` | `grep -cE "\[(ENTRARIA\|CAERIA\|BLOQUEARIA)\]"` da **6** | **6 informes** para 5 candidatos (el sexto es el re informe de `P28`) | **cuadra, y la diferencia esta nombrada** (`O.3.c`) |
| `.aduana_v20/informe_lote_cap09_v2.txt` | `grep -cE "\[(ENTRARIA\|CAERIA\|BLOQUEARIA)\]"` da **el numero que `O.6.8` pega** | **el informe de lote de los 20 de `cap_09`** | **ver `O.6.8`: la corrida estaba EN VUELO cuando escribi esta tabla, y lo digo en vez de adelantar su cifra** |
| `.aduana_v20/informe_lote_cap09_ROJO_MIO.txt` | `grep -c "el fichero no se puede leer"` da **21** | **la corrida roja de mi instrumento, 20 candidatos mas la linea del resumen** | **cuadra, y el rojo es mio** (`O.3.d`) |
| `.aduana_v20/frontera_cap10.txt` | `grep -c "^| \*\*P"` da **78** | **las 39 filas de la frontera, en sus DOS tablas** (tramos y motivos): `39 x 2 = 78` | **cuadra** (`O.4.b` y `O.4.c`) |
| `.aduana_v20/lista_cap09_lf.txt` | `wc -l` da **20** | **los 20 de `cap_09`** | **cuadra** |
| `.t1_v20/` | `ls .t1_v20/*.py \| wc -l` da **13** | este reporte cita **nueve** por su nombre (`reparto`, `remedir`, `medidas`, `cifras`, `fix_p28`, `frontera10`, `lista09`, `citas5`, `sin_guiones`) | **la ruta guarda MAS de lo que cito, y nombro los cuatro que no cito: `mapa10.py`, `p24.py`, `p27.py`, `p28.py`** |

    $ grep -cE "\[(ENTRARIA|CAERIA|BLOQUEARIA)\]" .aduana_v20/informes.txt
    $ grep -cE "\[(ENTRARIA|CAERIA|BLOQUEARIA)\]" .aduana_v20/informe_lote_cap09_v2.txt
    $ grep -c "el fichero no se puede leer" .aduana_v20/informe_lote_cap09_ROJO_MIO.txt
    $ grep -c "^| \*\*P" .aduana_v20/frontera_cap10.txt
    $ wc -l < .aduana_v20/lista_cap09_lf.txt
    $ ls .t1_v20/*.py | wc -l
      (las seis salidas, pegadas en la tabla de arriba)

> **LAS CINCO RUTAS DE PRUEBA LLEVAN SU CONTADOR Y SU SALIDA, Y LA UNICA QUE NO CUADRA AL
> NUMERO REDONDO LLEVA SU DIFERENCIA NOMBRADA EN LA MISMA LINEA.** Es el remedio entero, y lo
> que lo hace comprobable no es mi palabra: es que **el auditor puede correr los seis comandos
> y ver si mienten.**

## O.6.8. **EL INFORME DE LOTE DE LOS 20 DE `cap_09`, CON SU SALDO PEGADO**

*Lo que la `ACTA 19` `2.3` no pudo firmar y el encargo `1.e` me dejo encargado.*

**LANZADO, Y CON SU RELOJ PEGADO EN VEZ DE UNA PROMESA:**

    $ head -7 .aduana_v20/informe_lote_cap09_v2.txt | tail -1
      Sat, Sep 12, 2026  3:46:49 PM        <- la corrida arranco aqui
    $ ls -la .aduana_v20/informe_lote_cap09_v2.txt     (a las 4:08:18 PM)
      480 bytes                            <- solo la cabecera: el instrumento imprime
                                              su informe ENTERO al final, no por candidato

> ### **ESCRIBO ESTE BLOQUE DE CIERRE CON LA CORRIDA EN VUELO, Y LO DIGO ASI EN VEZ DE ADELANTAR SU SALDO.**
>
> **POR QUE NO ESPERO A QUE ACABE PARA ESCRIBIR EL CIERRE:** porque el disparador de `12.4` es
> **no cerrar el reporte**, y el encargo lo repite dos veces en mayusculas. **Un cierre escrito
> con una cifra pendiente se audita; un cierre que no existe, no.** La vuelta 17 hizo lo otro.
>
> **Y POR QUE NO ADELANTO EL SALDO AUNQUE LOS 20 YA PASARON LA ADUANA DE UNO EN UNO:** porque
> seria exactamente la caida que esta vuelta viene a remediar. **Los cinco informes de `O.3.c`
> prueban que cada uno entra contra el grafo, y los 15 de la vuelta 19 tambien pasaron el suyo;
> de ahi se SIGUE que los 20 entran, pero no lo PRUEBA la ruta que estoy publicando.** `O.2.d`
> me obliga a decir lo que la ruta guarda, no lo que deduzco.

**LO QUE ESTA CORRIDA APORTA Y NINGUNO DE LOS 20 INFORMES INDIVIDUALES PUEDE APORTAR** es una
sola cifra, y es la razon entera de haberla lanzado: **`CHOCAN entre si dentro del lote`.** Los
informes de uno en uno comparan cada candidato **contra el grafo**; **solo los veinte en la
misma llamada pueden chocar entre ellos.**

**Y LO QUE SIGO NO PUDIENDO FIRMAR, dicho con su nombre:** mi fila de `N.6.8` (*de los 25
corregidos, 20 `ENTRARIAN` y 5 `BLOQUEARIAN`*) **sigue probada solo en 21 de sus 25** (`O.2.f`).
**El informe de hoy es de `cap_09`, no de aquellos 25**, y no los cubre. **El de los 83 son unas
cuatro horas a tres minutos por candidato y no cabe en mi turno, igual que no cupo en el del
auditor.**

## O.6.9. LO QUE ESTA VUELTA PUBLICA, EN UNA TABLA

| | |
|---|---|
| **vuelta** | **20**, lote 4 (`scott_radical_candor`). **`cap_09` cerrado, `cap_10` cortado y no extraido** |
| **tareas encargadas** | **3**, y el tope son cinco. **Las tres CERRADAS**, sin cola por techo de tareas |
| **candidatos escritos** | **5** (`P22`, `P23`, `P24`, `P27`, `P28`), **95 pasos**, **45,6 palabras por paso** |
| **por la aduana** | **5 de 5, `[ENTRARIA]` al primer intento**, uno escrito y uno comprobado, **sin tandas**. **6 informes**, el sexto el re informe de `P28` |
| **id contra las seis reglas** | **5 de 5 limpios en la puerta**, contra 14 de 15 la vuelta pasada |
| **`cap_09`** | **CERRADO: 20 de 20 piezas que dan nodo, 272 pasos.** Ningun capitulo del lote 4 queda partido |
| **`cap_10`** | **frontera cortada y publicada: 39 piezas, 20 dan nodo, 19 no con su motivo, `8.976` contra `8.976`, `0` sin cubrir, `0` solapes.** NO extraido, por el punto 4 del encargo |
| **relectura de fidelidad `D.30`** | **95 pasos, 95 `TRANSCRIPCION`, 0 `PUENTE` publicados. Y 1 puente cazado y corregido en el acto** de 40 cifras barridas (`O.3.e`) |
| **`PASOS INVENTADOS`** | `cap_09` **0,00 (0 de 272)**; lote 4 **0,58 (5 de 856)**. **Peor unidad `cap_04` 6,25 contra tope 10: el freno NO se dispara.** Y la cautela dicha: la tasa baja porque el denominador crece |
| **aristas** | **`D.37`: cero cableables hoy** y la de `L317` explicada por que no lo es. **`D.29`: doce colas vivas**, once de ellas desbloqueables con un solo acto. **Mas la `D.37` de `cap_10` levantada y dejada fuera del recuento** |
| **insercion** | **CERO, y es la regla funcionando.** `D.39` pide lote **CERRADO** y quedan **36.656 palabras** sin minar en `cap_10` a `cap_14`. Grafo **203 a 203**, bitacora **148 a 148** |
| **discutibles marcados antes de saber si acierto** | **9**, y **cinco de los nueve son sobre piezas que yo no voy a escribir** |
| **mis caidas, declaradas por mi** | **1 cazada antes de exponerla** (`O.2.c`, la ruta que escribi antes de correr el `ls`); **1 puente cazado y corregido en el acto** (`O.3.e`); **1 fila propia corregida al remedir** (`O.6.2.b`, el `0` de `_insertados`); **2 rojos en mis propios guiones** (`O.6.1.b` y `O.3.d`) |
| **la caida de la `ACTA 19` que acepto entera** | la ruta que prometia **40 informes** y guardaba **35 de 41**. **Remedio adoptado en `O.2.d` y auditado contra mi propio reporte en `O.6.7`** |
| **guardas al cierre** | **las cinco en verde**, con los tres rojos de `guiones` y su causa pegados |
| **lineas del reporte** | **abrio en 23.670** |
| **lo que la vuelta siguiente se encuentra** | **`cap_10` con su frontera cortada y su cuenta de 20 medida**, su `D.37` levantada con cita, y cuatro discutibles mios sobre sus piezas. **`cap_11` a `cap_14` sin tocar** |

> # **LA VUELTA 20 CIERRA EN `cap_09` COMPLETO, CON SU REPORTE ESCRITO, Y NO DEJA NINGUN CAPITULO PARTIDO.**
>
> **Lo que la vuelta 19 dejo fue una deuda dentro de un capitulo. Lo que esta vuelta deja es un
> capitulo sin abrir con la mitad cara de su trabajo ya hecha y publicada.** La diferencia es
> el limite: **la de antes estaba dentro de un capitulo, y esta esta en el limite entre dos.**

## O.6.10. LO QUE PROPONGO EN MI SEDE, SIN ADJUDICARME NADA (`EXTRACTOR.md` 14)

1. **EL DENOMINADOR QUE PREDICE UNA FRONTERA NO ES LA PALABRA, ES EL ROTULO.** Dos casos
   medidos y las dos veces corto: `cap_09` proyectaba 34, 32 y 15 y dio **20**; `cap_10`
   proyectaba **10,3** y da **20**. **`cap_10` es la mitad de largo que `cap_09` y da los
   mismos candidatos, porque tiene el doble de rotulos.** Propongo que el encargo **corte la
   frontera antes de decidir el volumen**, que es lo que este ya me hizo hacer en su punto 1.
   **No pido maquinaria: el corte cuesta unos minutos y no falla.**
2. **`12.4` PUNTO 4 SIGUE SIN DECIR CUANTO ES *PONE EN RIESGO*.** No reabro la adjudicacion
   (un capitulo no se parte, y hoy la cumplo), **y no la vuelvo a subir como tension**. Lo que
   senialo es lo otro: el punto 4 del encargo me deja decidir con la palabra *riesgo* y **no
   hay umbral escrito**. Yo he decidido con una cuenta publicada (`O.4.e`) y con el ejemplar
   de la vuelta 17 al lado, **pero el siguiente puede decidir distinto con los mismos
   numeros**, y eso es lo que un umbral arreglaria.
3. **EL CORTE FINO CONTRA EL GRUESO ESTA VIVO Y `cap_10` ES DONDE SE DECIDE.** Mi discutible 1.
   `cap_09` uso los dos cortes **en el mismo capitulo**: `P8` a `P13` finos y `P24` y `P27`
   gruesos. **`P21` de `cap_10` decide si ese capitulo da 20 candidatos o 25.** No me lo
   adjudico y no lo resuelvo por mi cuenta: **lo dejo marcado con su cifra.**
