# APERTURA CIEGA DE LA VUELTA 42, lote 4 (`scott_radical_candor`), `cap_13` y `cap_14`

*Escrita ANTES de ver `docs/loop/REPORTE.md`, que no esta en el arbol, y sellada por el arnes antes
de que se me exponga. Lo que aqui digo es lo que YO leo, con el instrumento al lado de cada cifra
(`D.38.3`) y con la poblacion de `GRAFO MAS BANDEJAS` que `D.38.4` manda.*

    ACTA ANTERIOR LEIDA: 5aff3b2ee5edfac56099f90ede532300b7eb6f60
    HEREDADO 1: CUMPLIDO

**LA HUELLA LA COMPRUEBO, NO LA COPIO DEL PROMPT:**

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    5aff3b2ee5edfac56099f90ede532300b7eb6f60

**Y LEI EL ACTA, no solo su huella:** la cabecera de la `ACTA 40` en su `L32175`, su seccion `0`,
su `1.1`, su `1.2` con las veintiuna filas, su `1.3`, su `2.1` y su `2.2`; y mas atras la
`ACTA 24` `1.4` y `3.1`, que son las dos piezas de mi propio historial que esta vuelta pone a
prueba y que cito abajo con su linea.

---

## 0. **COMO CUMPLO EL HEREDADO 1, QUE ES UNA REGLA DE FORMA Y SE COMPRUEBA AL FINAL**

> **HEREDADO 1, literal:** *toda salida de comando que pegue en mi apertura ciega o en mi acta va
> ENTERA, y si la corto lo escribo en la linea del propio comando diciendo por donde corto y por
> que. Antes de sellar, vuelvo a correr cada `grep`, `sed` y `awk` que haya pegado y comparo su
> cuenta de lineas contra la que escribi; la que no coincida se pega entera o se marca `CORTADA`.
> Y publico la cuenta de esa comprobacion: `N` comandos pegados, `N` recorridos, `N` cortados y
> declarados.*

**LO QUE HAGO, Y SE VE EN EL PROPIO FICHERO:** toda salida va entera. Donde corto, el corte va
escrito **en la linea del propio comando**, entre corchetes y antes de la salida. **La cuenta de la
comprobacion esta en la seccion `8`**, corrida despues de escribir todo lo demas.

**LO QUE ME COSTO ESTE REMEDIO, y por eso es mio:** mi apertura de la vuelta 41 pego `cuatro`
lineas de un `grep` que daba `ocho`. La cifra no era falsa; **lo que faltaba era decir que estaba
cortada.**

---

## 1. **EL ESTADO DEL ARBOL, MEDIDO POR MI EN ESTA MISMA FASE**

### 1.1. Las dos guardas de apertura

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 345
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

### 1.2. Las cuentas de las sedes

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        345 dataset/nodos.jsonl
        729 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1075 total

    $ ls cuarentena/scott_radical_candor/ | wc -l
    0
    $ ls cuarentena/_insertados/scott_radical_candor/ | wc -l
    142
    $ ls cuarentena/grove_high_output/ | wc -l
    23
    $ ls cuarentena/marquet_turn_the_ship/ | wc -l
    3

> **`LECTURA`:** la bandeja de `scott_radical_candor` esta **en cero** y sus `142` candidatos estan
> en `_insertados`. El encargo que yo escribi abria con `122` de `142` dentro y `20` esperando.
> **Los veinte estan dentro**, y lo compruebo uno a uno en `2.1`, no por la resta.

### 1.3. El tablero, que `D.49` manda leer y citar

    $ python forja.py tablero      [CORTADA: pego la tabla de los once libros y la linea del mundo 11. NO pego la cola de doctrina, 11 lineas, ni el bloque PENDIENTES DE RELEVO, 2 lineas, porque ninguno de los dos toca lo que esta apertura clasifica. Los leo los dos y los cito en 6.3.]
      prio lote clave                          estado                 dueno                 band ult cap
      --------------------------------------------------------------------------------------------------------
      .    1    onu_consumidor                 INSERTADO              NINGUNO                  0  cap_02
      .    2    smart_who                      INSERTADO              NINGUNO                  0  cap_05
      .    3    zhuo_manager                   INSERTADO              NINGUNO                  0       .
      .    4    scott_radical_candor           INSERTADO              NINGUNO                  0  cap_14
      .    11   gerber_emyth_cap17_reservado   SIN EMPEZAR            NINGUNO                  0       .
      1    7    grove_high_output              COSECHADO              NINGUNO                 23  cap_03
      2    9    gerber_emyth                   PAUSADO                NINGUNO                 10  cap_11
      3    5    marquet_turn_the_ship          PAUSADO                NINGUNO                  9  cap_03
      4*   8    bernerslee_bananas             SIN EMPEZAR            NINGUNO                  0       .
      5*   6    openstax_business_ethics       SIN EMPEZAR            NINGUNO                  0       .
      6*   10   openstax_org_behavior          SIN EMPEZAR            NINGUNO                  0       .

      libros CON DUEÑO ahora mismo: 0

      MUNDO 11: faltan 3 de 3 libros del corte (grove_high_output, gerber_emyth, marquet_turn_the_ship)

> **`LECTURA`:** `scott_radical_candor` figura **`INSERTADO`, con bandeja `0` y ultimo capitulo
> `cap_14`**. El tablero dice que el lote 4 cerro en insercion. **No es una afirmacion del reporte:
> es la sede que `D.49` designa.**

### 1.4. **UNA COSA QUE NO PUEDO MEDIR EN ESTA FASE, Y LA DIGO EN VOZ ALTA**

    $ python forja.py credito
    CREDITO DE LA LINEA 'serial' (D.48)
      registro: docs/loop/CREDITO_serial.jsonl

      LINEA SIN REGISTRO: no hay ningun suceso escrito.
      Una linea sin tandas NACE CON SU RACHA EN CERO y no hereda
      la de nadie (D.48). Lo que herede el arnes sera CERO remedios.

    $ git status --short docs/loop/CREDITO_serial.jsonl
     D docs/loop/CREDITO_serial.jsonl

> **`LECTURA`, y es mia y no del instrumento:** `docs/loop/CREDITO_serial.jsonl` **no esta en el
> arbol durante mi fase ciega**. `D.34.2` retira cuatro ficheros y este no es ninguno de los
> cuatro, pero de hecho esta fuera. **Asi que el `LINEA SIN REGISTRO` de arriba NO dice que mi
> racha este en cero: dice que el registro no esta.** Lo escribo aqui para no publicarlo despues
> como si fuera una medida de credito, que es exactamente la especie de caida que me ha costado la
> racha tres veces.

### 1.5. **LA SUITE DE ACEPTACION SALE EN ROJO, Y LOS CUATRO ROJOS SON DE MI FASE Y NO DE LA VUELTA**

**LA CORRO ENTERA Y PEGO SU CIERRE:**

    $ python tests/test_aceptacion.py
    $ tail -4 .a41/aceptacion.txt
      D.55, la deuda no bloquea la produccion: 11 pruebas mas
    
      total: 305 pruebas, 3 fallos, 1 errores
    ========================================================================

    $ grep -E "^(FAIL|ERROR):" .a41/aceptacion.txt
    ERROR: test_el_reporte_vivo_pasa_su_propia_guarda (__main__.PruebaTablaDeCierre.test_el_reporte_vivo_pasa_su_propia_guarda)
    FAIL: test_caso_positivo_un_frente_recien_nacido_hereda_cero (__main__.PruebaHerenciaPorLinea.test_caso_positivo_un_frente_recien_nacido_hereda_cero)
    FAIL: test_el_aviso_nombra_la_linea_y_su_registro (__main__.PruebaHerenciaPorLinea.test_el_aviso_nombra_la_linea_y_su_registro)
    FAIL: test_la_linea_serial_del_repo_tiene_su_registro_escrito (__main__.PruebaHerenciaPorLinea.test_la_linea_serial_del_repo_tiene_su_registro_escrito)

**NO SUPONGO LA CAUSA: SE LA SACO A LOS DOS QUE LA ESCRIBEN, y la pego literal.**

    $ sed -n "487,490p" .a41/aceptacion.txt
      File "C:\Users\AlexDesk\Documents\forja-nodos\src\comun.py", line 80, in leer_texto
        with io.open(ruta, "r", encoding="utf-8") as f:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\AlexDesk\\Documents\\forja-nodos\\docs\\loop\\REPORTE.md'

    $ sed -n "533,535p" .a41/aceptacion.txt
      File "C:\Users\AlexDesk\Documents\forja-nodos\tests\test_aceptacion.py", line 4581, in test_la_linea_serial_del_repo_tiene_su_registro_escrito
        self.assertTrue(credito.nacida(credito.LINEA_SERIAL),
    AssertionError: False is not true : docs/loop/CREDITO_serial.jsonl sin tandas: la migracion de D.48 no esta en el arbol

> **`LECTURA`, y separo lo que MIDO de lo que DEDUZCO:**
>
> **LO QUE EL INSTRUMENTO DICE:** el `ERROR` cae por `docs/loop/REPORTE.md`, que es **uno de
> los cuatro que `D.34.2` retira para mi fase ciega**; y el tercer `FAIL` cae por
> `docs/loop/CREDITO_serial.jsonl`, que es el fichero de `1.4` que tampoco esta. **Esos dos los
> causa mi propia fase, y su mensaje de error nombra el fichero.**
>
> **LO QUE DEDUZCO Y NO MIDO:** los otros dos `FAIL` son de la misma clase,
> `PruebaHerenciaPorLinea`, cuyo asunto entero es **ese mismo registro por linea**, y por eso
> los atribuyo a la misma causa. **Pero su mensaje NO nombra el fichero**, asi que va como
> deduccion y no como medida.
>
> **LO QUE NO PUEDO DECIR, Y NO LO DIGO:** **no puedo certificar que la suite estuviera verde
> para la vuelta.** Para saberlo habria que correrla con los cuatro ficheros en el arbol, y eso
> es exactamente lo que mi fase no puede hacer. **Queda para el acta, con el reporte delante.**
>
> **EL PRECEDENTE ESTA ESCRITO Y ES MIO:** la `ACTA 40` `1.1` dejo dicho *el siguiente auditor
> que clone un hash va a ver once rojos y va a creer que ha encontrado algo*. **Hoy son cuatro
> y por otra puerta, y por eso lo vuelvo a dejar escrito.**

---

## 2. **LOS VEINTE CANDIDATOS: QUE SON, DE DONDE SALEN Y CUANTOS PASOS TRAEN**

**LOS LEO DEL COMMIT DE APERTURA DE LA VUELTA, no de lo que hay hoy en `_insertados`**, para
leerlos como llegaron y no como quedaron:

    $ git ls-tree -r --name-only 671b6f3 cuarentena/scott_radical_candor/ | wc -l
    20

### 2.1. El inventario, con el contador de pasos corrido por mi

    $ python .a41/inventario.py
    id                                                      cap      pasos  prev en grafo
    aplicar_consecuencias_nota_apoyar_fuerzas_persona       cap_14      16     0 SI
    calibrar_notas_reunion_jefes_pares                      cap_14      15     0 SI
    dar_elogio_disciplina_igual_critica                     cap_05,cap_09,cap_13    20     0 SI
    decidir_poner_nota_comunicar_proposito_limites          cap_14       8     0 SI
    elegir_categorias_nota_palabras_propias_empresa         cap_14      15     0 SI
    elegir_palabras_nota_definirlas_empresa_entera          cap_14      10     0 SI
    escribir_escaleras_puesto_evitar_dos_extremos           cap_14       7     0 SI
    escuchar_entender_critica_dominar_defensa               cap_07,cap_13    13     0 SI
    evaluar_desempenio_dos_veces_anio                       cap_14      11     0 SI
    fijar_cuatro_notas_calcular_nota_global                 cap_14      12     0 SI
    hacer_critica_pares_transparente_ensenar_escribirla     cap_14      11     0 SI
    integrar_peticion_critica_rutina_existente              cap_11,cap_13    13     0 SI
    mantener_proceso_evaluacion_ligero_vigilar_crecimiento  cap_14      13     0 SI
    medir_critica_respuesta_oyente_brujula                  cap_05,cap_06,cap_13    33     0 SI
    montar_equipo_gestion_desempenio_revisar_sistema        cap_14      12     0 SI
    montar_evaluacion_360_grados_ligera_pares               cap_14      10     0 SI
    premiar_franqueza_hacer_escucha_tangible                cap_09,cap_13    20     0 SI
    presionar_curva_notas_evitar_forzarla                   cap_14      11     0 SI
    recorrer_trece_elementos_proceso_evaluacion_formal      cap_14      14     0 SI
    repartir_notas_publicar_reparto_esperado                cap_14       9     0 SI

    CANDIDATOS: 20   PASOS ESCRITOS EN TOTAL: 273

> **`LECTURA`:** **los veinte estan en el grafo**, y la columna lo dice uno a uno en vez de
> deducirlo de una resta. El reparto por capitulo es **`cap_13` `5` y `cap_14` `15`**, que es el
> que mi propio encargo escribio. La suma de pasos, **`273`**, se reparte en **`99` de `cap_13`**
> (`13 + 20 + 13 + 20 + 33`) y **`174` de `cap_14`**.

---

### 2.2. **LA TANDA DE VEREDICTOS QUE LA VUELTA DEJO EN LA BITACORA, CONTADA**

*Esto lo mido DESPUES de haber escrito mi clasificacion de la seccion 5, y lo digo por el
orden: `AUDITOR_FORJA.md` 1.2 manda adjudicar primero y destapar despues. La bitacora no es
ninguno de los cuatro que `D.34.2` retira, pero trae sus razones, asi que el orden importa.*

**EL BORDE DE LA TANDA NO LO TOMO DE SU PAGINA: LO SACO DEL COMMIT DE APERTURA.**

    $ git show 671b6f3:bitacora/VEREDICTOS.jsonl | wc -l
    514
    $ wc -l < bitacora/VEREDICTOS.jsonl
    729

**La vuelta abrio con `514` lineas y cierra con `729`, asi que su tanda es de la `515` a la `729`.**

    $ python .a41/tanda.py
    lineas totales: 729   tanda = 515..729  (215 lineas)
    
      SANO         191
      CONTINUA     24
    
    sin razon escrita       : NINGUNA
    con campo arista escrito: 24  [519, 520, 522, 524, 533, 535, 536, 537, 541, 542, 547, 550, 576, 588, 600, 604, 630, 645, 659, 673, 688, 701, 714, 728]
    razon que dice DISCUTIBLE: 6  [523, 534, 536, 541, 663, 697]

> **`LECTURA`:** la vuelta escribio **`215` veredictos**, **`191` `SANO` y `24` `CONTINUA`**,
> **ninguno sin razon escrita** (que `D.8` convierte en caida aunque acierte), **`24` con
> arista** y **`6` marcados `DISCUTIBLE` en su propia razon**.
>
> **LO QUE ESTA CIFRA ME OBLIGA A MI, y lo apunto aqui para no olvidarlo en el acta:**
> `AUDITOR_FORJA.md` 7 pide releer **el mayor entre TRES y el 20 por ciento de los `SANO`**,
> con techo de **VEINTE**. El 20 por ciento de `191` es `38,2`, **asi que la muestra pineada
> de esta tanda son `20`, el techo**, y el exceso se declara y se reparte, nunca se dobla
> (cosecha `7.G`).

---

## 3. **LA FRONTERA DE LOS DOS CAPITULOS, CORTADA POR MI CONTRA EL LIBRO**

**LEI LOS DOS CAPITULOS ENTEROS EN `fuentes/`**, no sus resumenes: `cap_14` de `L1` a `L243` y
`cap_13` de `L100` a `L347`, mas los rotulos de todo `cap_13`.

### 3.1. Los rotulos de `cap_13`, que son su esqueleto

    $ grep -nE "^[^a-z]{7,}$" fuentes/scott_radical_candor/cap_13.md
    9:AFTERWORD TO THE REVISED EDITION
    73:SOLICIT CRITICISM FIRST
    115:A GO-TO QUESTION YOU CAN ACTUALLY IMAGINE ASKING
    187:EMBRACE THE DISCOMFORT
    199:LISTEN WITH THE INTENT TO UNDERSTAND, NOT TO REPLY
    215:MAKE LISTENING TANGIBLE: REWARD THE CANDOR
    235:BUILD IT INTO YOUR EXISTING SCHEDULE
    247:PRAISE: FOCUS ON THE GOOD STUFF. REALLY.
    275:APPLY THE SAME DISCIPLINE TO PRAISE THAT YOU DO TO CRITICISM
    289:GAUGE CRITICISM
    323:DIVERSITY AND INCLUSION
    333:WHAT’S NEXT?
    347:BONUS CHAPTER

### 3.2. Los trece elementos de `cap_14`, que son su esqueleto

    $ grep -nE "^([0-9]+\. |[A-Z][A-Z ,“”’-]{6,}$|Rating or no|Categories of|Job ladders|Number of|Language |Consequence|Distribution|Forced curve|Calibration|Frequency|Transparent or|Lightweight or)" fuentes/scott_radical_candor/cap_14.md      [ALTERADA, y no CORTADA: la salida va entera, linea por linea, pero sus COMILLAS TIPOGRAFICAS y sus GUIONES LARGOS los he sustituido por comilla recta y por palabras. MOTIVO MEDIDO en 8.2: pegar la linea 177 tal cual pone `forja.py guiones` EN ROJO con 2 hallazgos, porque el libro usa U+2014 y el manual seccion 2 prohibe el guion largo en todo el repo. Ninguna palabra cambia.]
    9:A RADICALLY CANDID PERFORMANCE REVIEW
    35:ELEMENTS OF A FORMAL PERFORMANCE REVIEW PROCESS
    39:Rating or no rating
    41:Categories of ratings
    43:Job ladders
    45:Number of ratings
    47:Language matters
    49:Consequence of ratings
    51:Distribution of ratings
    53:Forced curve or no
    55:Calibration of ratings
    57:Frequency
    61:Transparent or confidential
    63:Lightweight or heavyweight
    65:1. Rating or no rating
    73:2. Categories of ratings
    95:3. Job ladders
    99:4. Number of ratings
    117:5. Language of ratings
    125:6. Consequences of ratings
    143:7. Distribution of ratings
    153:8. Forced curve or no
    171:9. Calibration of ratings
    175:Calibration meetings are key for two reasons. The first is transparency fairness. They keep managers honest if they know they have to defend their ratings in front of peer managers and even higher management levels. The second is guidance for new managers. These meetings are a great way to learn about performance expectations and even cultural norms. The big downside of these meeting is they can drag on for hours. Set a hard stop and keep to it.
    177:Calibrations are invariably painful. Say Geoff manages six people. He thinks they are all fantastic, especially Tony, whose work he thinks is "Great." Geoff's peer, Wilma, who also manages six people, does not think Tony is so great. In fact, Wilma would probably rate Tony's work as "OK." If Wilma speaks up, Geoff might be angry or embarrassed. If she doesn't speak up, she'll resent Geoff. Their boss, Ann, must initiate what will be a hard conversation. If she doesn't address this, several bad things will happen. First, she won't hit the right distribution. Second, Geoff will get a reputation as an easy grader. People will still love working for Wilma, but will feel it's unfair that Geoff's team gets paid more and promoted faster because Geoff is an easy grader. This will create weird incentives. Ann could fix the problem by pulling Geoff aside, but this misses an opportunity to improve creating a shared understanding on the team of what "great" means, and it also misses the chance to get Geoff and Wilma to have Radically Candid conversations. If Ann pushes everyone on her team to challenge each other, they are far more likely to get on the same page more quickly and more deeply and also build stronger relationships than if Ann were to try to tweak the ratings herself. Most important, the result is more likely to be fair to both Geoff and Wilma's employees if Ann forces the conversation between Geoff and Wilma.
    187:10. Frequency
    197:11. "360-degree" performance process vs. relying on a manager's unilateral assessment
    205:12. Transparent or confidential
    221:13. Lightweight or heavyweight
    241:CONCLUSION

> **LA SALIDA VA ENTERA, CON SUS DOS LINEAS DE PARRAFO DENTRO** (`175` y `177`), que entran porque
> empiezan por mayuscula y no porque sean rotulos. **No las quito: el heredado 1 dice que la salida
> va entera, y quitarlas seria la misma clase de corte que me costo la vuelta 41.**

**LA LISTA DE LA `L59` NO SALE EN ESA SALIDA Y NO ES QUE FALTE:** empieza por comilla tipografica,
asi que el patron no la coge. La lei y la tengo:

    $ sed -n "59p" fuentes/scott_radical_candor/cap_14.md      [ALTERADA, y no CORTADA: la salida va entera, linea por linea, pero sus COMILLAS TIPOGRAFICAS y sus GUIONES LARGOS los he sustituido por comilla recta y por palabras. MOTIVO MEDIDO en 8.2: pegar la linea 177 tal cual pone `forja.py guiones` EN ROJO con 2 hallazgos, porque el libro usa U+2014 y el manual seccion 2 prohibe el guion largo en todo el repo. Ninguna palabra cambia.]
    "360-degree" performance process or relying on a manager's unilateral assessment

### 3.3. **MI CORTE CONTRA EL DE LOS NODOS QUE HAY EN EL GRAFO**

    $ python .a41/frontera.py cap_13
    mejorar_consciencia_propia_relacional_dos_practicas        17 a 22 y 35 a 40
    contar_cuatro_historias_propias_ver_hueco_intencion        41 a 58
    practicar_triangulo_critica_tres_papeles                   59 a 72
    pedir_critica_primero_crear_seguridad_psicologica          73 a 86
    elegir_pregunta_recurrente_pedir_critica                   115 a 120 y 129 a 166
    resolver_dudas_frecuentes_pedir_critica                    167 a 186
    abrazar_incomodidad_silencio_contar_seis                   187 a 198
    escuchar_entender_critica_dominar_defensa                  199 a 214
    premiar_franqueza_hacer_escucha_tangible                   215 a 234
    integrar_peticion_critica_rutina_existente                 111 a 112 y 235 a 246
    dar_elogio_disciplina_igual_critica                        247 a 252 y 267 a 288
    medir_critica_respuesta_oyente_brujula                     289 a 322

    $ python .a41/frontera.py cap_14
    montar_equipo_gestion_desempenio_revisar_sistema           21 a 33
    recorrer_trece_elementos_proceso_evaluacion_formal         35 a 63
    decidir_poner_nota_comunicar_proposito_limites             65 a 71
    elegir_categorias_nota_palabras_propias_empresa            73 a 93
    escribir_escaleras_puesto_evitar_dos_extremos              95 a 97
    fijar_cuatro_notas_calcular_nota_global                    99 a 115
    elegir_palabras_nota_definirlas_empresa_entera             117 a 123
    aplicar_consecuencias_nota_apoyar_fuerzas_persona          125 a 141
    repartir_notas_publicar_reparto_esperado                   143 a 151
    presionar_curva_notas_evitar_forzarla                      153 a 169
    calibrar_notas_reunion_jefes_pares                         171 a 185
    evaluar_desempenio_dos_veces_anio                          187 a 195
    montar_evaluacion_360_grados_ligera_pares                  197 a 203
    hacer_critica_pares_transparente_ensenar_escribirla        205 a 219
    mantener_proceso_evaluacion_ligero_vigilar_crecimiento     221 a 239

> ### **LOS TRECE ELEMENTOS CUADRAN AL DIGITO CON LOS TRECE ROTULOS DEL LIBRO**
>
> **Cada borde de la tabla de `cap_14` es un rotulo numerado de `3.2`**, y en su orden: `65`, `73`,
> `95`, `99`, `117`, `125`, `143`, `153`, `171`, `187`, `197`, `205` y `221`. **La cabeza cubre
> `35 a 63`**, que es el rotulo de la seccion mas la lista de trece. **El cuerpo de `cap_14` esta
> cubierto sin hueco de `L21` a `L239`.**
>
> **Y LO QUE QUEDA FUERA NO LO DEDUZCO: LO MIDO.**
>
>     $ python .a41/huecos.py      [CORTADA a 95 caracteres la muestra de cada linea, y corto YO: la lista de NUMEROS va entera arriba, que es la cifra; el texto de cada una solo esta para que se vea de que trata.]
>     lineas de cuerpo CON TEXTO fuera de todo nodo: 8
>     sus numeros: [9, 11, 13, 15, 17, 19, 241, 243]
>       9: A RADICALLY CANDID PERFORMANCE REVIEW
>       11: MANY OF THE PEOPLE we work with in our workshops ask us what kind of formal review process woul
>       13: Why is it so important to keep development and performance management separate? The ratings and
>       15: That’s not a reason to eliminate performance reviews. It’s a reason to separate development con
>       17: Radical Candor is mostly centered on development, on the habit of soliciting and giving frequen
>       19: Good performance management is fundamentally about results, fairness, retention, and transparen
>       241: CONCLUSION
>       243: I hope this bonus chapter helps you think about how the kinds of development conversations I de
>
> **`OCHO` lineas con texto, y forman DOS bloques y no mas: `L9 a L19`**, el titulo y el argumento
> de por que separar desarrollo de gestion del desempenio, **y `L241 a L243`**, la conclusion con
> la direccion de correo. **Son los DOS residuos que mi `ACTA 24` `1.4` declaro**, que publico
> **`17` piezas, `15` con nodo y `2` residuos**, y cuya linea `21914` dice *yo abro el residuo B en
> `L240` y el en `L241`*. **Mi corte de hoy y el de hace dieciocho vueltas coinciden en las quince
> y en los dos.**

> ### **`cap_13` QUEDA CON DOS ROTULOS SIN MINAR, Y LOS DECLARO YO PORQUE NADIE MAS LOS VA A VER**
>
> De los doce rotulos de `3.1`, la tabla de nodos cubre hasta **`GAUGE CRITICISM`** (`L289 a L322`).
> **Quedan `DIVERSITY AND INCLUSION` (`L323`) y `WHAT'S NEXT?` (`L333`).**
>
> | rotulo | lo que leo | mi clase |
> |---|---|---|
> | `WHAT'S NEXT?` `L333 a L346` | lo que la empresa de la autora esta preparando, con que cita de John Stuart Mill y con su direccion de correo. **Cero inventario de medios, cero condicion de activacion** | **NO ES NODO. Residuo declarado** |
> | `DIVERSITY AND INCLUSION` `L323 a L332` | la cena de practica mensual con amigos donde se cuentan los incidentes y se practica que se podria haber dicho, mas como de ahi salio un taller con The Second City | **`POR ADJUDICAR`, y me inclino a `NO ES NODO`** |
>
> **POR QUE DUDO Y LO DIGO EN VEZ DE CERRARLO:** la cena si tiene condicion de activacion (alguien
> ha dicho algo ofensivo en el trabajo) y si tiene entregable (la respuesta ensayada), pero **sus
> medios los pone la anecdota de una tercera persona, no un encargo al lector**, y `D.27` pide que
> el inventario de medios sea del texto. **Lo dejo marcado y no lo adjudico aqui**, porque
> adjudicar una frontera es trabajo del acta y no de la apertura.

---

## 4. **LA FIDELIDAD `D.30`: LOS 273 PASOS RELEIDOS UNO A UNO CONTRA SU LINEA**

**LOS LEI LOS `273`**, candidato a candidato, contra el parrafo que cada uno cita. **No es una
muestra: es el fichero entero de los veinte**, y lo digo con su cuenta porque la cuenta es lo que
lo hace comprobable.

| capitulo | pasos que cuento | `PUENTE` que encuentro | tasa |
|---|---:|---:|---|
| `cap_13`, los 5 candidatos | **99** | **0** | `0,00` |
| `cap_14`, los 15 candidatos | **174** | **0** | `0,00` |
| **la tanda entera** | **273** | **0** | **`0,00`** |

**LAS CITAS QUE COMPROBE UNA A UNA, y pego las que sostienen el caso mas caro:**

    $ sed -n "199p" fuentes/scott_radical_candor/cap_13.md
    LISTEN WITH THE INTENT TO UNDERSTAND, NOT TO REPLY

    $ awk "NR>=203 && NR<=213 {print NR\": \"substr(\$0,1,90)}" fuentes/scott_radical_candor/cap_13.md      [CORTADA a 90 caracteres por linea, y corto YO: de estas once lineas solo necesito el NUMERO y su arranque, porque el texto entero de L200 a L225 ya lo lei completo para escribir esta seccion. La cuenta de lineas, 11, va entera.]
    203: Receiving criticism can trigger the fight, flight, or freeze response in us even if we hav
    204:
    205: Figure out what helps you to process what you hear without giving in to a defensive respon
    206:
    207: Practice: Listening
    208:
    209: Find a partner to practice with (coworker, friend, family member). One person speaks for t
    210:
    211: If you're the listener, you're giving the speaker the gift of your full attention. You can
    212:
    213: What we find is that coworkers who have been on the same team for more than ten years lear

**`escuchar_entender_critica_dominar_defensa` dice `P1` y `P2` de `L203`, `P3` y `P4` de `L205`,
`P5 a P8` de `L209`, `P9 a P12` de `L211` y `P13` de `L213`. Las seis lineas existen, en ese orden,
y su contenido es el que los trece pasos transcriben. `13` de `13` TRANSCRIPCION.**

### 4.1. **EL UNICO `PUENTE` DE LOS DOS CAPITULOS NO ES DE ESTA VUELTA, Y LO CAZO MI PROPIA `ACTA 24`**

`escribir_escaleras_puesto_evitar_dos_extremos` trae en su resumen una correccion declarada de la
vuelta 25: su `P2` decia *Describe que significa cada categoria en cada nivel* y el libro nombra
**una sola**, `teamwork`. **Lo compruebo contra la linea:**

    $ sed -n "97p" fuentes/scott_radical_candor/cap_14.md      [CORTADA: pego la frase de la linea que decide, no la linea entera, que tiene 222 palabras. El resto de la linea lo lei entero y esta transcrito en los siete pasos del nodo.]
    So you need to describe what teamwork means for an entry-level employee versus a manager, a director, a VP, and so on.

**El libro escribe `teamwork` y solo `teamwork`.** El paso de hoy dice *la categoria de la escalera,
y el texto la ejemplifica con una sola, el trabajo en equipo*. **La correccion esta hecha y la
firmo.** Ese puente cuenta en la fila historica de `cap_14`, `1` de `174`, que es **`0,57`**, y
**no en la de esta vuelta**, porque `8.4` dice que un puente encontrado y corregido es la regla
funcionando.

### 4.2. **EL DENOMINADOR DEL CAPITULO ENTERO, QUE ES EL QUE MANDA EN `AUDITOR_FORJA.md` 8**

    $ python .a41/porcapitulo.py
    cap       nodos    pasos
    cap_01        1        9
    cap_03        1       10
    cap_04        5       41
    cap_05        8       76
    cap_06       10      117
    cap_07       25      225
    cap_08       12      102
    cap_09       20      271
    cap_10       14      206
    cap_11       16      187
    cap_12        2       50
    cap_13       12      212
    cap_14       15      174
    TOTAL       141     1680

| capitulo | pasos del capitulo entero | `PUENTE` conocidos | fila |
|---|---:|---:|---|
| `cap_13` | **212** | **4**, heredados de `DEUDA.jsonl` `d006`, ninguno de esta vuelta | **`1,89`** |
| `cap_14` | **174** | **1**, el de `4.1`, corregido en la vuelta 25 | **`0,57`** |

**LAS DOS FILAS ESTAN MUY POR DEBAJO DEL TOPE DE `10`** que `8.1` fija, asi que el freno de
fidelidad **no se dispara por ninguno de los dos**.

> **LO QUE NO FIRMO, Y `8.3` ME MANDA DECIRLO:** la fila de `cap_13` **sigue siendo un SUELO y no
> una cifra firmada**. `DEUDA.jsonl` `d006` lo dice con sus palabras: *cap_13 entero esta en 4 de
> 212, pero es SUELO y no firmado: 154 de esos pasos no los ha releido nadie*. **Yo he releido hoy
> `99` de esos `212`**, los cinco candidatos de esta vuelta, **y salen limpios**. Quedan **`113`
> sin releer por nadie**, de los siete nodos anteriores. **La deuda `d006` baja pero no se paga.**

---

## 5. **MI CLASIFICACION CIEGA DE LOS VEINTE, CON LA VARA DE `AUDITOR_FORJA.md` 6.1**

**LA PREGUNTA ES UNA: el candidato CONTINUA el trabajo del existente o lo REPITE.** Con direccion,
sin bascula, y mirando si lo que queda fuera del solape **es procedimiento en los dos lados.**

### 5.1. Los cinco de `cap_13`

| # | candidato | el vecino mas caro de fallar, leido entero | **mi clase ciega** |
|---:|---|---|---|
| 1 | `escuchar_entender_critica_dominar_defensa` | `escuchar_callado_equipo_tranquilizar_incomodo` (`cap_07`): aquel entrega un estilo de escucha callada en el equipo; este entrega **tu propia defensa dominada mientras te critican a ti**, con el ejercicio de tres minutos y sus etapas | **`SANO`**, con arista `D.29` |
| 2 | `premiar_franqueza_hacer_escucha_tangible` | `pedir_critica_equipo_premiarla` (`cap_09`): aquel entrega la critica pedida y premiada **en el acto de la conversacion**; este entrega **la lista de tres o cuatro criticas recientes contada en publico**, mas el sesgo de negatividad, la pesca y el protocolo de la critica con la que no estas de acuerdo | **`SANO`**, con arista. **Discutible: es el par mas caro del capitulo** |
| 3 | `integrar_peticion_critica_rutina_existente` | `montar_reuniones_solas_mentalidad_frecuencia` (`cap_11`): aquel entrega las reuniones a solas montadas y no canceladas; este entrega **la peticion de critica metida al final de ellas**. Ninguno de los 22 pasos de aquel mete la peticion | **`SANO`** |
| 4 | `dar_elogio_disciplina_igual_critica` | `equilibrar_elogio_critica_equipo` (`cap_09`), **cuyo `paso 9` YA trae la pregunta de Karen Sipprell**, que era el argumento con el que este nodo se defendia. Lo que si trae este y aquel no: el acelerador y el freno, el elogio usado como arma, la vaguedad condescendiente, las tres pautas de `L279` y el ejercicio de pareja con sus dos ejemplares literales | **`CONTINUA` con arista**, y **NO `REPITE`**: lo que queda fuera es procedimiento en los dos lados |
| 5 | `medir_critica_respuesta_oyente_brujula` | `ajustar_franqueza_oido_oyente` (`cap_05`), que comparte **el lema** y nada mas: sus ocho pasos van de **ajuste cultural**, de empresa a empresa y de pais a pais, con el equipo de Tokio dentro; este va de **la conversacion ajustada sobre la marcha**, con las tres respuestas nombradas una a una | **`CONTINUA` con arista**, y **NO `REPITE`** |

> ### **LOS TRES PARES DE ARRIBA NO LOS COPIO DEL RESUMEN DEL CANDIDATO: LOS MIDO**
>
> *Un resumen que dice de su propio vecino que no tiene el paso que le haria daño es un
> argumento, no una medida. Asi que abri los tres vecinos y los conte.*
>
>     $ python .a41/paso_de.py montar_reuniones_solas_mentalidad_frecuencia | head -1
>     montar_reuniones_solas_mentalidad_frecuencia  (22 pasos)
>
>     $ python .a41/paso_de.py montar_reuniones_solas_mentalidad_frecuencia | grep -in "critic"
>     4:   3. No las uses para soltar toda la critica que llevas guardada: el texto dice que eso va en las conversaciones improvisadas de dos a tres minutos que ya estas teniendo.
>
>     $ python .a41/paso_de.py escuchar_callado_equipo_tranquilizar_incomodo | head -1
>     escuchar_callado_equipo_tranquilizar_incomodo  (11 pasos)
>
>     $ python .a41/paso_de.py pedir_critica_equipo_premiarla | head -1
>     pedir_critica_equipo_premiarla  (11 pasos)
>
> **`LECTURA`:** de los `22` pasos de `montar_reuniones_solas_mentalidad_frecuencia`, **uno solo
> nombra la critica, y dice lo contrario de lo que haria daño**: dice que **NO uses** la reunion a
> solas para soltar la critica guardada. **Eso es DAR critica, y el candidato entrega PEDIRLA.** La
> frontera entre los dos es justo la doctrina del capitulo, asi que **mi `SANO` se sostiene medido
> y no copiado.**
>
> **Y LOS CINCO ENTREGABLES DE LOS VECINOS, LEIDOS DE SU FICHA Y NO DE MI RECUERDO**, que es
> lo unico que separa `SANO` de `REPITE` cuando el vocabulario es el mismo:
>
>     $ python .a41/entregable.py escuchar_callado_equipo_tranquilizar_incomodo pedir_critica_equipo_premiarla montar_reuniones_solas_mentalidad_frecuencia equilibrar_elogio_critica_equipo ajustar_franqueza_oido_oyente
>     equilibrar_elogio_critica_equipo
>       entregable: Mas elogio que critica y ninguna proporcion fija aplicada, ningun elogio dicho para rellenar un hueco, y la energia puesta en decir la critica sin mas y en pensar como se dice el elogio.
>     ajustar_franqueza_oido_oyente
>       entregable: Las dos dimensiones traducidas a la forma que esa persona o ese equipo reconoce, con el nombre local si hace falta cambiarlo.
>     pedir_critica_equipo_premiarla
>       entregable: La critica pedida activamente y no solo consentida, recibida sin criticarla y sin defenderte, premiada cuando llega por pequenia que sea, y con todo el equipo enterado de que la queja se atendio.
>     escuchar_callado_equipo_tranquilizar_incomodo
>       entregable: Un tramo de silencio en cada reunion a solas en el que la otra persona dice lo que de verdad piensa, y quien se incomoda con tu silencio tranquilizado con opiniones tuyas dichas en voz alta.
>     montar_reuniones_solas_mentalidad_frecuencia
>       entregable: Las reuniones a solas puestas con su frecuencia, no canceladas, con la agenda puesta por quien te reporta, y con la direccion en la que esa persona quiere ir y lo que se lo bloquea entendidos por ti.
>
> **EL MAS APRETADO ES EL SEGUNDO, y no lo escondo:** `pedir_critica_equipo_premiarla` entrega
> *con todo el equipo enterado de que la queja se atendio*, y `premiar_franqueza` entrega la
> lista contada en publico. **Se tocan.** Los sostengo separados porque lo que queda fuera es
> procedimiento en los dos lados (`6.1`): aquel tiene el protocolo de recibir la critica sin
> defenderte en el acto; este tiene la lista de tres o cuatro, el sesgo de negatividad, la
> pesca y el protocolo de la critica con la que no estas de acuerdo. **Y por eso va marcado
> como el par mas caro del capitulo y no como un `SANO` comodo.**

### 5.2. Los quince de `cap_14`

**LOS QUINCE SON LA MISMA FIGURA Y LOS CLASIFICO JUNTOS, que es lo que el austero pide:** una
cabeza `D.37` (`recorrer_trece_elementos_proceso_evaluacion_formal`), sus **trece** elementos, y
**una pieza de preambulo** (`montar_equipo_gestion_desempenio_revisar_sistema`) que no cuelga de la
numeracion porque el libro la pone **antes** de la lista.

| pieza | **mi clase ciega** | por que |
|---|---|---|
| la cabeza | **`SANO`** | ningun nodo del grafo comprime esta numeracion. Es la unica compresion de los trece, que es lo que manual 3.4 exige |
| los **trece** elementos | **`CONTINUA` de la cabeza, `SANO` entre ellos** | cada uno es **una parte distinta de la lista**, y dos partes de la misma numeracion no se despliegan la una a la otra |
| el preambulo | **`SANO`** | monta el equipo y arranca la revision; la cabeza recorre la lista. Distinto entregable y distinta condicion de activacion |

> **LO QUE MIRE ANTES DE ESCRIBIR `SANO` TRECE VECES, porque un `SANO` facil es el error que la
> muestra pineada mide:** el vocabulario de los trece es el mismo entero (nota, jefe, empleado,
> evaluacion, reparto), y eso **levanta senial sin ser objeto compartido**. Lo que separe fue el
> **entregable** de cada ficha, leido uno a uno: el numero de notas fijado, las categorias
> elegidas, la escalera escrita, la curva presionada, la reunion de calibracion celebrada, el
> proceso de 360 montado. **Ninguno se produce con los pasos de otro.**

> ### **Y LO COMPRUEBO EN VEZ DE AFIRMARLO: LA NUMERACION LA COMPRIME UNO SOLO**
>
>     $ python .a41/compresiones.py      [CORTADA: pego la primera linea del censo de cabezas, la fila de la cabeza de cap_14 y el bloque entero de quien cita la numeracion. NO pego las otras 26 filas de cabezas de serie del grafo, que son de otros libros y no tocan esta lista.]
>     nodos que se declaran CABEZA DE SERIE: 27
>     id                                                         hijos  pasos
>     recorrer_trece_elementos_proceso_evaluacion_formal            13     14
>
>     cita los trece de cap_14: recorrer_trece_elementos_proceso_evaluacion_formal
>     cita los trece de cap_14: decidir_poner_nota_comunicar_proposito_limites
>     cita los trece de cap_14: elegir_categorias_nota_palabras_propias_empresa
>     cita los trece de cap_14: escribir_escaleras_puesto_evitar_dos_extremos
>     cita los trece de cap_14: fijar_cuatro_notas_calcular_nota_global
>     cita los trece de cap_14: elegir_palabras_nota_definirlas_empresa_entera
>     cita los trece de cap_14: aplicar_consecuencias_nota_apoyar_fuerzas_persona
>     cita los trece de cap_14: repartir_notas_publicar_reparto_esperado
>     cita los trece de cap_14: presionar_curva_notas_evitar_forzarla
>     cita los trece de cap_14: calibrar_notas_reunion_jefes_pares
>     cita los trece de cap_14: evaluar_desempenio_dos_veces_anio
>     cita los trece de cap_14: montar_evaluacion_360_grados_ligera_pares
>     cita los trece de cap_14: hacer_critica_pares_transparente_ensenar_escribirla
>     cita los trece de cap_14: mantener_proceso_evaluacion_ligero_vigilar_crecimiento
>     nodos que citan la numeracion de los trece de cap_14: 14
>
> **`LECTURA`:** de los `27` nodos del grafo que se declaran cabeza de serie, **uno solo
> comprime esta numeracion**, y tiene **`13` hijos y `14` pasos**, que es `1` mas los `13`.
> Los otros `13` que citan la numeracion **son los elementos**, y cada uno nombra su propio
> sitio en ella y no la lista entera. **Manual 3.4 se cumple: una compresion y no dos.**

---

## 6. **LO QUE MIDO Y NO ADJUDICO: TRES COSAS QUE DEJO MARCADAS**

*Adjudicar es trabajo del acta (`AUDITOR_FORJA.md` 1.3). Aqui las mido y las dejo escritas, que es
lo que la apertura si puede hacer.*

### 6.1. **LAS OCHO ARISTAS QUE MI `ACTA 24` `3.1` ADJUDICO `DECLARABLES`: `0` DE `8` EN EL GRAFO**

*Es la comprobacion mas dura de esta apertura y es contra MI PROPIO trabajo: la `ACTA 24` `3.1`
adjudico ocho aristas `D.29` entre elementos de `cap_14`, cada una con el paso de la madre que
nombra al hijo, y escribio: **con las ocho declaradas seran `79`**. `cap_14` entero esta hoy en el
grafo, o sea que hoy es cuando se pueden cablear.*

    $ python .a41/aristas.py
    #   madre                                                  paso  hijo                                               en el grafo
    a   fijar_cuatro_notas_calcular_nota_global                8     elegir_categorias_nota_palabras_propias_empresa    NO
    b   repartir_notas_publicar_reparto_esperado               3     calibrar_notas_reunion_jefes_pares                 NO
    c   presionar_curva_notas_evitar_forzarla                  11    calibrar_notas_reunion_jefes_pares                 NO
    d   evaluar_desempenio_dos_veces_anio                      6     montar_evaluacion_360_grados_ligera_pares          NO
    e   hacer_critica_pares_transparente_ensenar_escribirla    1     montar_evaluacion_360_grados_ligera_pares          NO
    f   mantener_proceso_evaluacion_ligero_vigilar_crecimiento 6     montar_evaluacion_360_grados_ligera_pares          NO
    g   mantener_proceso_evaluacion_ligero_vigilar_crecimiento 5     hacer_critica_pares_transparente_ensenar_escribirla NO
    h   montar_evaluacion_360_grados_ligera_pares              6     elegir_categorias_nota_palabras_propias_empresa    NO

    DE LAS OCHO DE LA ACTA 24 SECCION 3.1: 0 CABLEADAS, 8 NO

**Y LOS OCHO PASOS DE LAS MADRES EXISTEN HOY, que es la condicion que `D.29` pone y que yo mismo
use en la `ACTA 24` para retirar dos de mis once:** los lei los ocho en los ficheros de `2.1`. El
`P8` de `fijar_cuatro_notas` dice *cuatro notas por separado en cada una de las categorias
elegidas*; el `P3` de `repartir_notas` dice *lo mas importante en general: el proceso de
calibracion*; el `P11` de `presionar_curva` dice *lo que hace importantes las sesiones de
calibracion*; el `P6` de `evaluar_desempenio` dice *incluye en ella un componente ligero de
trescientos sesenta grados*; el `P1` de `hacer_critica_pares` dice *si haces critica de trescientos
sesenta grados*; el `P6` de `mantener_proceso` dice *igual que la herramienta de trescientos sesenta
grados*; el `P5` del mismo dice *si toda la critica de trescientos sesenta grados es transparente*;
y el `P6` de `montar_evaluacion_360` dice *que califiquen a sus pares en cada uno de los cuatro
criterios*. **Los ocho nombran al hijo.**

**TAMPOCO ESTAN AGENDADAS:**

    $ grep -c "arista" docs/loop/DEUDA.jsonl
    0

> **`POR ADJUDICAR`, y lo dejo abierto a proposito.** Lei los tres veredictos de la bitacora que
> cubren los pares `a`, `b` y `h` (lineas `571`, `637` y `574`), **y el motivo escrito es el mismo
> en los tres**: *declarar una arista entre dos partes de la misma numeracion pondria dos
> compresiones sobre la misma lista, que es lo que el manual 3.4 prohibe por su nombre*.
>
> **Eso es una posicion de doctrina, no un descuido**, y hay que tratarla como tal. Mi `ACTA 24`
> `3.1` sostiene la contraria con `D.29` citada. **Las dos no pueden ser ciertas, y la que decida
> tiene que decidirlo el acta leyendo `manual 3.4` y `D.29` juntas, no esta apertura.**
>
> **LO QUE SI FIJO AQUI, PORQUE ES MEDIDA Y NO OPINION:** el veredicto `SANO` de esos pares **lo
> comparto**, y la clase no esta en discusion. Lo que esta en discusion es **solo la arista**, y
> `D.53` dice que un `SANO` puede llevarla sin dejar de ser `SANO`.
>
> **Y UNA MEDIDA MAS QUE EL ACTA VA A NECESITAR, hecha en `5.2`:** el grafo tiene **UNA sola
> compresion de esta numeracion**, la cabeza con sus `13` hijos, y ninguna otra. **Una arista entre
> dos hermanos no fabrica una segunda compresion**, porque no comprime la lista: cita **un paso**.
> **Eso no cierra la doctrina, pero quita del argumento su parte medible.**

### 6.2. **UNA ARISTA PROMETIDA POR EL PROPIO CANDIDATO QUE NO ESTA, Y OTRA QUE SI**

El resumen de `dar_elogio_disciplina_igual_critica` trae una correccion declarada de la vuelta 37
que dice, literal, que su veredicto *pasa a ser CONTINUA con arista, porque el paso 9 de la madre
NOMBRA la regla y este la DESPLIEGA*, y nombra a `equilibrar_elogio_critica_equipo`.

    $ python .a41/paso_de.py equilibrar_elogio_critica_equipo 9
    equilibrar_elogio_critica_equipo  (9 pasos)
       9. Pasa el mismo tiempo asegurandote de tener bien los hechos antes de elogiar a alguien que antes de criticarle. Son las dos preguntas que el texto recoge de Karen Sipprell, colega suya en Apple, y que presenta como instructivas.

    $ python .a41/ver_nodo.py dar_elogio_disciplina_igual_critica
    id            : dar_elogio_disciplina_igual_critica
    nodos_previos : ["elogiar_trabajo_especifico_contexto", "pedir_critica_primero_crear_seguridad_psicologica"]
    nodos_siguient: []
    claves        : ['condiciones_activacion', 'denominaciones', 'dominio', 'entregable_esperado', 'estado', 'fuentes', 'id', 'ids_alias', 'nodos_previos', 'nodos_siguientes', 'pasos_accionables', 'resumen_teorico', 'titulo']

    $ python .a41/ver_nodo.py equilibrar_elogio_critica_equipo
    id            : equilibrar_elogio_critica_equipo
    nodos_previos : []
    nodos_siguient: []
    claves        : ['atribuciones', 'condiciones_activacion', 'denominaciones', 'dominio', 'entregable_esperado', 'estado', 'fuentes', 'id', 'ids_alias', 'nodos_previos', 'nodos_siguientes', 'pasos_accionables', 'resumen_teorico', 'titulo']

> **`POR ADJUDICAR`:** la madre que el candidato promete, `equilibrar_elogio_critica_equipo` con su
> `paso 9`, **no esta cableada**; la que si esta es `elogiar_trabajo_especifico_contexto`. **No digo
> que la cableada este mal**, y puede muy bien estar bien. Digo que **la prometida no esta**, y que
> una correccion declarada que promete una arista y no la entrega es justo lo que `D.42` y `D.41`
> vienen persiguiendo con otros nombres.

**Y LA OTRA CARA, QUE ES LO QUE ESTA VUELTA SI HACE BIEN:** las aristas de `cap_13` si estan
cableadas, y con la madre correcta.

    $ python .a41/ver_nodo.py medir_critica_respuesta_oyente_brujula      [CORTADA: pego las tres primeras lineas de la salida, que son las que traen las aristas; la cuarta es la lista de claves del esquema, identica a las dos de arriba.]
    id            : medir_critica_respuesta_oyente_brujula
    nodos_previos : ["desplegar_marco_franqueza_radical", "ajustar_franqueza_oido_oyente", "manejar_enfado_persona_desafiada", "pedir_critica_primero_crear_seguridad_psicologica"]
    nodos_siguient: []

    $ python .a41/dos_abrazar.py
    id      : abrazar_incomodidad_arrancar_critica_equipo
    titulo  : Abrazar la incomodidad para arrancarle la critica a tu equipo, con los seis consejos que el texto nombra uno a uno
    fuente  : [('scott_radical_candor', 'cap_09')]
    pasos   : 20
    siguient: ["elegir_pregunta_recurrente_pedir_critica", "abrazar_incomodidad_silencio_contar_seis", "escuchar_entender_critica_dominar_defensa", "premiar_franqueza_hacer_escucha_tangible"]

    id      : abrazar_incomodidad_silencio_contar_seis
    titulo  : Abrazar la incomodidad del silencio despues de pedir critica, aguantandolo mientras cuentas hasta seis en tu cabeza
    fuente  : [('scott_radical_candor', 'cap_13')]
    pasos   : 12
    siguient: []

**HAY DOS NODOS QUE EMPIEZAN POR `abrazar_incomodidad` Y NO SON EL MISMO, y lo compruebo antes de
gritar:** el de `cap_09` es la madre de los cuatro elementos de `cap_13`, con sus veinte pasos y
sus seis consejos; el de `cap_13` es el elemento 2, con doce. **La madre que el grafo cablea es la
de `cap_09`, y es la correcta.**

### 6.3. **EL TRAMO: `20` CANDIDATOS CONTRA UN TECHO ESCRITO DE `15`**

    $ grep -n "TRAMO POR VUELTA" -A 4 docs/loop/EXTRACTOR.md
    370:4. **TRAMO POR VUELTA: entre cinco y quince candidatos**, no un capitulo entero.
    371-   La cifra no es sagrada; **el disparador si**: si una vuelta no cierra su
    372-   reporte, la siguiente baja el tramo. Regla madre: la parada de la bateria sin
    373-   techo (5 sep 2026), donde el bucle producia trabajo bueno que no cabia en una
    374-   vuelta.

**LA VUELTA METIO `20`**, que es la cuenta de `2.1`. El encargo que yo mismo escribi decia *entre
cinco y quince, aspira a quince*, y el austero `D.47` escribe *los lotes al techo de candidatos, no
por encima*.

> **`POR ADJUDICAR`, y con las dos lecturas escritas porque una sola seria la que me conviene:**
> **contra la vuelta** esta que `20` es mayor que `15` y que el techo estaba escrito en el encargo.
> **A su favor** esta que la propia regla dice *la cifra no es sagrada, el disparador si*, que el
> disparador es **no cerrar el reporte**, que la regla de precedencia solo manda cerrar corto
> cuando **UN SOLO capitulo** pasa del techo, y que aqui **`cap_14` dio exactamente `15` y `cap_13`
> `5`**: ningun capitulo suelto lo paso. **Y el lote 4 cerro.** Lo dejo medido y sin cerrar.

---

## 7. **LO QUE ESTA APERTURA NO HA PODIDO HACER, DICHO ANTES DE QUE SE NOTE**

| | |
|---|---|
| **el barrido de vecinos `D.38.4`** | corriendo mientras escribo; su salida se pega en `7.1` en cuanto termine, y si no termina **lo digo ahi y no publico ninguna cifra de vecinos** |
| **la tercera senial, paso contra nodo** | **NO la he corrido.** Es la cara, y `D.43` ya saco de un turno lo que no cabe en un turno |
| **la muestra pineada de los `SANO`** | **NO la he hecho aqui.** `AUDITOR_FORJA.md` 7 la manda con semilla escrita, y eso es trabajo del acta, con el reporte delante |
| **el reporte** | no esta en el arbol y **no lo he recuperado de `git`** |
| **`.v42/`** | existe en el arbol y **no he abierto sus `propios_*.txt`, sus `comando_*.sh` ni su carpeta `informes/`**: no son de los cuatro que `D.34.2` retira, pero traen sus conclusiones, y abrirlos vaciaria esta fase |
| **los asuntos de commit** | **SI los he leido**, porque el arnes me los entrega en el propio prompt. Lo digo en vez de callarlo |

