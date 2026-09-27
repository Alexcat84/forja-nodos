
---

## Q.5. TAREA 4: EL CIERRE DEL LOTE 4. **DECLARADA Y NO HECHA, PORQUE SU CONDICION NO SE CUMPLE**

*El encargo la condiciona con una letra que no admite lectura: **SI Y SOLO SI `cap_12` A `cap_14`
QUEDAN MINADOS Y EL LOTE CIERRA EN EXTRACCION**. Y anade: **si el lote no cierra porque el techo de
candidatos cerro la vuelta antes, nada de esta tarea se hace y se declara**.*

### Q.5.a. LA CONDICION, MEDIDA Y NO SUPUESTA

Salida de los dos comandos, guardada en `.t1_v23/cierre_lote.txt`:

    $ ls fuentes/scott_radical_candor/*.md | wc -l
    15
    $ python .t1_v23/cobertura_lote4.py
    unidades en la bandeja de entrada : 15
    unidades con candidato escrito    : 12
    unidades saldadas sin candidato   : 2   ['cap_00', 'cap_02']
    unidades SIN MINAR                : 1   ['cap_14']
      cap_00  unidad=Copyright Page  -> Copyright Page: no minable, no hay procedimiento que extraer
      cap_02  unidad=Introduction  -> Introduction: minado en su vuelta con resultado CERO candidatos

**LAS DOS UNIDADES SALDADAS SE DICEN CON SU ROTULO Y NO SE ESCONDEN EN UNA RESTA:** `cap_00` es la
pagina de creditos y no es minable, y `cap_02` es la introduccion, minada en su vuelta con resultado
**cero candidatos**. **Una unidad sin candidato no es una unidad sin minar**, y confundirlas haria
creer que al lote le faltan tres capitulos cuando le falta **uno**.

> # **EL LOTE 4 NO CIERRA EN ESTA VUELTA: LE FALTA `cap_14`, Y SOLO `cap_14`.**
>
> **`D.39` INSERTA UN LOTE CERRADO, Y MEDIO LOTE NO ES UN LOTE.** Por sexta vez la insercion llega
> abierta y por sexta vez no entra nada, **y la razon se mide en vez de suponerse**: de las 15
> unidades de la bandeja, **12 tienen candidato, 2 estan saldadas con su motivo y 1 esta sin
> minar**.
>
> **NO ES UNA ELECCION MIA NI UNA PRUDENCIA:** meter candidatos de un lote abierto es una **caida de
> dato** (`EXTRACTOR.md` 15.7), y el motivo esta escrito: un candidato que entra antes **se lleva por
> delante la comparabilidad del lote entero**, y **`D.36` solo se puede calcular sobre un lote
> completo**, porque con el lote abierto no se sabe todavia quien va a entrar.

### Q.5.b. LO QUE NO SE HACE, PUNTO POR PUNTO DEL ENCARGO

| punto de la TAREA 4 | estado | por que |
|---|---|---|
| **1.** citar el informe de lote por su sello | **NO SE HACE** | esta corrida **no trae `INFORME_DE_LOTE.txt` ni `SELLOS_INFORME.jsonl`**, medido en `Q.0.2`. `D.42` es literal: **no lo invento y no lo lanzo** |
| **2.** `D.39` inserta, uno por vez, con `D.36` y `D.37` | **NO SE HACE** | el lote sigue ABIERTO: falta `cap_14` |
| **3.** cablear las **37** aristas (hoy **52**) | **NO SE HACE** | `forja.py arista` rechaza por construccion una arista cuyos extremos viven en cuarentena, medido dos veces (vuelta 21 `O.4.b` y `ACTA 21` `2.3`). **No lo vuelvo a medir una tercera** |
| **4.** dar sede a los veredictos sin bitacora | **NO SE HACE** | los veredictos entran a `bitacora/VEREDICTOS.jsonl` **por `forja.py insertar`, en el mismo acto** (`D.31`), y no hay insercion. **No se escribe a mano en la bitacora** (`EXTRACTOR.md` 14) |

### Q.5.c. LA CORRECCION 9 SIGUE VIVA Y SIN EJECUTAR, Y POR ESO SE REPITE

**El dia que la insercion ocurra, la arista de la rueda de la cultura NO se cablea con `--paso 2` de
la madre.** Va escrita entera en `Q.2.h` y repetida en la deuda de `Q.7`, **porque una correccion
que solo vive en la vuelta que la escribio es una correccion que se pierde.**

### Q.5.d. EL SALDO DE MIS INFORMES DE UN CANDIDATO, IMPRESO DE SUS FICHEROS

*No es el informe de lote, que esta vuelta no existe (`Q.0.2`). Es la cuenta de **los informes de UN
candidato que si corri yo**, uno por cada candidato escrito o corregido, en el mismo acto de
escribirlo (`EXTRACTOR.md` 16).*

Salida de `python .t1_v23/saldo_v23.py`, guardada en `.t1_v23/salida_saldo_v23.txt`:

| grupo | informes | `ENTRARIA` | `BLOQUEARIA` | `CAERIA` | vecinos levantados |
|---|---:|---:|---:|---:|---:|
| **la cola de siete (TAREA 1)** | 6 | **4** | **2** | **0** | 2 |
| **cap_12** | 2 | **0** | **2** | **0** | 5 |
| **cap_13** | 12 | **2** | **10** | **0** | 21 |
| **los tres grupos** | **20** | **6** | **14** | **0** | **28** |

| informe | poblacion | del grafo | de bandejas |
|---|---:|---:|---:|
| el primero de la vuelta, `desplegar_tres_conversaciones_carrera` | **316** | 203 | 113 |
| el ultimo de la vuelta, `medir_critica_respuesta_oyente_brujula` | **330** | 203 | 127 |

| candidato | vecino | senial |
|---|---|---|
| `desplegar_tres_conversaciones_carrera` | `conversar_historia_vida_descubrir_motivadores` | `paso_contra_nodo` |
| `preguntar_seguimiento_hallar_huecos` | `calibrar_normalidad_preguntas_jefe` | `paso_contra_nodo` |
| `desplegar_plan_orden_operaciones_franqueza_radical` | `armar_plan_anual_crecimiento_equipo` | `paso_contra_nodo` |
| `desplegar_plan_orden_operaciones_franqueza_radical` | `bloquear_tiempo_pensar_calendario` | `paso_contra_nodo` |
| `desplegar_plan_orden_operaciones_franqueza_radical` | `desplegar_tres_conversaciones_carrera` | `paso_contra_nodo` |
| `desplegar_plan_orden_operaciones_franqueza_radical` | `desplegar_marco_franqueza_radical` | `familia_id` |
| `contar_historias_propias_explicar_franqueza_radical` | `contar_cuatro_historias_propias_ver_hueco_intencion` | `familia_id` |
| `mejorar_consciencia_propia_relacional_dos_practicas` | `desplegar_plan_orden_operaciones_franqueza_radical` | `paso_contra_nodo` |
| `contar_cuatro_historias_propias_ver_hueco_intencion` | `evitar_presion_social_actos_equipo` | `paso_contra_nodo` |
| `contar_cuatro_historias_propias_ver_hueco_intencion` | `contar_historias_propias_explicar_franqueza_radical` | `familia_id` |
| `practicar_triangulo_critica_tres_papeles` | `abrazar_incomodidad_silencio_contar_seis` | `similitud_texto` |
| `practicar_triangulo_critica_tres_papeles` | `escuchar_entender_critica_dominar_defensa` | `similitud_texto` |
| `pedir_critica_primero_crear_seguridad_psicologica` | `integrar_peticion_critica_rutina_existente` | `paso_contra_nodo` |
| `resolver_dudas_frecuentes_pedir_critica` | `despedir_persona_franqueza_radical` | `paso_contra_nodo` |
| `resolver_dudas_frecuentes_pedir_critica` | `resolver_dudas_frecuentes_reuniones_salto_nivel` | `familia_id` |
| `abrazar_incomodidad_silencio_contar_seis` | `escuchar_entender_critica_dominar_defensa` | `similitud_texto` |
| `abrazar_incomodidad_silencio_contar_seis` | `practicar_triangulo_critica_tres_papeles` | `similitud_texto` |
| `abrazar_incomodidad_silencio_contar_seis` | `premiar_franqueza_hacer_escucha_tangible` | `similitud_texto` |
| `abrazar_incomodidad_silencio_contar_seis` | `contar_historias_propias_explicar_franqueza_radical` | `similitud_texto` |
| `escuchar_entender_critica_dominar_defensa` | `contar_historias_propias_explicar_franqueza_radical` | `similitud_texto` |
| `escuchar_entender_critica_dominar_defensa` | `abrazar_incomodidad_silencio_contar_seis` | `similitud_texto` |
| `escuchar_entender_critica_dominar_defensa` | `premiar_franqueza_hacer_escucha_tangible` | `similitud_texto` |
| `escuchar_entender_critica_dominar_defensa` | `practicar_triangulo_critica_tres_papeles` | `similitud_texto` |
| `premiar_franqueza_hacer_escucha_tangible` | `abrazar_incomodidad_silencio_contar_seis` | `similitud_texto` |
| `premiar_franqueza_hacer_escucha_tangible` | `escuchar_entender_critica_dominar_defensa` | `similitud_texto` |
| `integrar_peticion_critica_rutina_existente` | `pedir_critica_primero_crear_seguridad_psicologica` | `paso_contra_nodo` |
| `integrar_peticion_critica_rutina_existente` | `abrazar_incomodidad_silencio_contar_seis` | `similitud_texto` |
| `medir_critica_respuesta_oyente_brujula` | `desplegar_marco_franqueza_radical` | `paso_contra_nodo` |
| | **28 pares levantados** | |

> **EL COSTE DEL INSTRUMENTO, MEDIDO POR MI EN ESTA VUELTA, Y LO DIGO PORQUE CAMBIA COMO TRABAJO:**
> el primer informe de un candidato de esta vuelta tardo **mas de nueve minutos** con dos procesos
> compitiendo, y los siguientes entre **tres y cinco** con la maquina para ellos solos. **Con veinte
> informes eso es mas de una hora de reloj.** `D.42` ya quito de mi turno el informe del lote entero
> por esta misma razon (**156,5 s por candidato**, medido el 12 sep); **el de un candidato sigue
> siendo mio y lo he corrido 21 veces: 20 candidatos mas una repeticion.**
>
> **LA REPETICION LA CUENTO Y DIGO POR QUE EXISTE:** toque el `resumen_teorico` de
> `pedir_critica_primero_crear_seguridad_psicologica` **despues** de tener su informe, para corregir
> la especie de sus cuatro aristas de `D.29` a `D.37` (`Q.9` caida 3). **Una correccion vuelve a
> escribir el candidato, asi que vuelve a pasar la puerta** (`EXTRACTOR.md` 16), y por eso hay 21
> corridas y 20 ficheros.
>
> **COMO LOS CORRI, Y LO DIGO EN VEZ DE DEJARLO SUPUESTO:** cada candidato se escribe y **su informe
> se lanza acto seguido**, y mientras corre escribo el siguiente. **Ninguno se publico como escrito
> antes de tener su informe delante**, que es lo que `EXTRACTOR.md` 16 protege. Lo que la regla
> prohibe (*escribir doce candidatos y pasar la aduana al final*) no ha pasado: **el que cae se ve en
> su minuto, no al final del lote.**
