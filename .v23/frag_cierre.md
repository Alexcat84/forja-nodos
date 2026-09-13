
---

# Q.12. EL CIERRE DE LA VUELTA 23

## Q.12.a. LAS TRES GUARDAS, CORRIDAS AL CERRAR Y NO AL EMPEZAR

Salida de `python forja.py gate`, guardada en `.t1_v23/salida_gate_cierre.txt`:

    GATE VERDE.
      nodos verificados: 203
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones

Salida de `python forja.py guiones`, guardada en `.t1_v23/salida_guiones_cierre.txt`:

    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

Salida de `python tests/test_aceptacion.py`, guardada en `.t1_v23/salida_aceptacion_cierre.txt`:

      D.40, lo que un auditor le deja al siguiente lo entrega el arnes: 13 pruebas mas
      la poblacion del informe es grafo mas bandejas (12 sep 2026, punto 3): 6 pruebas mas
      D.41, la tabla que dice ser de instrumento es la del instrumento: 13 pruebas mas
    
      total: 111 pruebas, 0 fallos, 0 errores
    ========================================================================

**Y EL HOOK NO SE SALTO NI UNA VEZ.** Cada commit de esta vuelta paso por `gate`, `guiones` y el
**tallado de `D.41`**, y el tallado **aborto un commit** cuando dos marcadores mios cayeron sobre las
tablas de la vuelta 22 (`Q.9` caida 4). **Se arreglo moviendo el marcador, no tecleando la celda.**

## Q.12.b. EL ESTADO AL CIERRE, **RECOMPUTADO AL CIERRE** (`EXTRACTOR.md` 4)

Salida de `python .t1_v23/cierre_v23.py`, guardada en `.t1_v23/salida_cierre_v23.txt`:

| medida | al abrir | al cerrar | se movio |
|---|---:|---:|---|
| nodos en el grafo | 203 | **203** | NO |
| veredictos en bitacora | 148 | **148** | NO |
| candidatos en cuarentena del lote 4 | 113 | **127** | **SI, +14** |
| ficheros en cuarentena/_insertados | 201 | **201** | NO |
| unidades en la bandeja del lote 4 | 15 | **15** | NO |

| sede | ficheros tocados desde `b05d040` |
|---|---:|
| `dataset/` | **0** |
| `bitacora/` | **0** |
| `censos/` | **0** |
| `config/` | **0** |
| `src/` | **0** |
| `esquema/` | **0** |
| `fuentes/` | **0** |
| `docs/` | **1** |

## Q.12.c. LOS PARES LEIDOS Y SUS VEREDICTOS, **IMPRESOS DE LOS INFORMES**

*`EXTRACTOR.md` 2: si la aduana bloquea, **lees a los vecinos antes de escribir el veredicto**, y
todo veredicto lleva su razon escrita. **Su sede propia es `bitacora/VEREDICTOS.jsonl` y hoy no puede
serlo**, porque a la bitacora se escribe por `forja.py insertar` y esta vuelta no inserta. **Lo digo
en vez de esconderlo: hoy su sede es este reporte.***

Salida de `python .t1_v23/veredictos_v23.py`, guardada en `.t1_v23/salida_veredictos_v23.txt`:

| # | candidato | vecino | senial que lo levanto | `sim` | `fam` | `paso` | veredicto |
|---:|---|---|---|---:|---:|---:|---|
| 1 | `abrazar_incomodidad_silencio_contar_seis` | `escuchar_entender_critica_dominar_defensa` | `similitud_texto` | 0.449 | 0.000 | 0.498 | **SANO, Y ES EL PAR QUE MAS CARO COSTARIA FALLAR DE TODA LA VUELTA** |
| 2 | `abrazar_incomodidad_silencio_contar_seis` | `practicar_triangulo_critica_tres_papeles` | `similitud_texto` | 0.373 | 0.000 | 0.489 | **SANO** |
| 3 | `abrazar_incomodidad_silencio_contar_seis` | `premiar_franqueza_hacer_escucha_tangible` | `similitud_texto` | 0.360 | 0.000 | 0.485 | **SANO** |
| 4 | `abrazar_incomodidad_silencio_contar_seis` | `contar_historias_propias_explicar_franqueza_radical` | `similitud_texto` | 0.376 | 0.100 | 0.464 | **SANO** |
| 5 | `contar_cuatro_historias_propias_ver_hueco_intencion` | `evitar_presion_social_actos_equipo` | `paso_contra_nodo` | 0.183 | 0.000 | 0.619 | **SANO** |
| 6 | `contar_cuatro_historias_propias_ver_hueco_intencion` | `contar_historias_propias_explicar_franqueza_radical` | `familia_id` | 0.301 | 0.300 | 0.487 | **CONTINUA con arista** |
| 7 | `contar_historias_propias_explicar_franqueza_radical` | `contar_cuatro_historias_propias_ver_hueco_intencion` | `familia_id` | 0.305 | 0.300 | 0.513 | **CONTINUA con arista** |
| 8 | `desplegar_plan_orden_operaciones_franqueza_radical` | `armar_plan_anual_crecimiento_equipo` | `paso_contra_nodo` | 0.166 | 0.100 | 0.711 | **CONTINUA con arista** |
| 9 | `desplegar_plan_orden_operaciones_franqueza_radical` | `bloquear_tiempo_pensar_calendario` | `paso_contra_nodo` | 0.189 | 0.000 | 0.650 | **CONTINUA con arista** |
| 10 | `desplegar_plan_orden_operaciones_franqueza_radical` | `desplegar_tres_conversaciones_carrera` | `paso_contra_nodo` | 0.227 | 0.111 | 0.608 | **CONTINUA con arista** |
| 11 | `desplegar_plan_orden_operaciones_franqueza_radical` | `desplegar_marco_franqueza_radical` | `familia_id` | 0.120 | 0.429 | 0.440 | **SANO, y con una tension del LIBRO declarada** |
| 12 | `desplegar_tres_conversaciones_carrera` | `conversar_historia_vida_descubrir_motivadores` | `paso_contra_nodo` | 0.225 | 0.000 | 0.647 | **CONTINUA con arista** |
| 13 | `escuchar_entender_critica_dominar_defensa` | `contar_historias_propias_explicar_franqueza_radical` | `similitud_texto` | 0.393 | 0.000 | 0.549 | **SANO** |
| 14 | `escuchar_entender_critica_dominar_defensa` | `abrazar_incomodidad_silencio_contar_seis` | `similitud_texto` | 0.446 | 0.000 | 0.507 | **SANO** |
| 15 | `escuchar_entender_critica_dominar_defensa` | `premiar_franqueza_hacer_escucha_tangible` | `similitud_texto` | 0.370 | 0.000 | 0.484 | **SANO** |
| 16 | `escuchar_entender_critica_dominar_defensa` | `practicar_triangulo_critica_tres_papeles` | `similitud_texto` | 0.350 | 0.111 | 0.469 | **SANO** |
| 17 | `integrar_peticion_critica_rutina_existente` | `pedir_critica_primero_crear_seguridad_psicologica` | `paso_contra_nodo` | 0.282 | 0.100 | 0.733 | **SANO, y es el espejo del par que mas cerca esta de caer** |
| 18 | `integrar_peticion_critica_rutina_existente` | `abrazar_incomodidad_silencio_contar_seis` | `similitud_texto` | 0.356 | 0.000 | 0.480 | **SANO** |
| 19 | `medir_critica_respuesta_oyente_brujula` | `desplegar_marco_franqueza_radical` | `paso_contra_nodo` | 0.139 | 0.000 | 0.723 | **CONTINUA con arista, Y ES LA ARISTA 53, QUE NO TENIA ANTES DE ESTE INFORME** |
| 20 | `mejorar_consciencia_propia_relacional_dos_practicas` | `desplegar_plan_orden_operaciones_franqueza_radical` | `paso_contra_nodo` | 0.202 | 0.000 | 0.601 | **SANO** |
| 21 | `pedir_critica_primero_crear_seguridad_psicologica` | `integrar_peticion_critica_rutina_existente` | `paso_contra_nodo` | 0.278 | 0.100 | 0.733 | **SANO, y es el par que mas cerca esta de caer** |
| 22 | `practicar_triangulo_critica_tres_papeles` | `abrazar_incomodidad_silencio_contar_seis` | `similitud_texto` | 0.375 | 0.000 | 0.471 | **SANO** |
| 23 | `practicar_triangulo_critica_tres_papeles` | `escuchar_entender_critica_dominar_defensa` | `similitud_texto` | 0.352 | 0.111 | 0.469 | **SANO** |
| 24 | `preguntar_seguimiento_hallar_huecos` | `calibrar_normalidad_preguntas_jefe` | `paso_contra_nodo` | 0.130 | 0.000 | 0.673 | **SANO** |
| 25 | `premiar_franqueza_hacer_escucha_tangible` | `abrazar_incomodidad_silencio_contar_seis` | `similitud_texto` | 0.353 | 0.000 | 0.469 | **SANO** |
| 26 | `premiar_franqueza_hacer_escucha_tangible` | `escuchar_entender_critica_dominar_defensa` | `similitud_texto` | 0.382 | 0.000 | 0.465 | **SANO** |
| 27 | `resolver_dudas_frecuentes_pedir_critica` | `despedir_persona_franqueza_radical` | `paso_contra_nodo` | 0.192 | 0.000 | 0.621 | **SANO** |
| 28 | `resolver_dudas_frecuentes_pedir_critica` | `resolver_dudas_frecuentes_reuniones_salto_nivel` | `familia_id` | 0.238 | 0.375 | 0.467 | **SANO, y lo levanta la familia de id porque comparten el APELLIDO resolver_dudas_frecuentes** |
| | | **28 pares** | | | | | |

**LAS RAZONES ENTERAS, UNA POR PAR, ESTAN EN LA SECCION 2 DE ESE MISMO FICHERO**
(`.t1_v23/salida_veredictos_v23.txt`), y el guion **sale en rojo si un solo par levantado se queda
sin razon escrita**. Hoy sale en verde.

## Q.12.d. LAS RUTAS QUE PUBLICO COMO PRUEBA, **CON SU ALCANCE DICHO**

| ruta | que guarda | alcance |
|---|---|---|
| `.t1_v23/` | **mis instrumentos de esta vuelta y su salida guardada** | 48 ficheros entre guiones y salidas. **Es lo que el tallador compara celda a celda** |
| `.aduana_v23/` | **un informe de la aduana por candidato**, **20 ficheros y 21 corridas** (la de `pedir_critica` se repitio al corregir su `resumen`) | **solo informes de UN candidato**. El del lote entero no existe en esta corrida (`Q.0.2`) |
| `.v23/` | los fragmentos con los que arme este reporte | andamio, no prueba |
| `cuarentena/scott_radical_candor/` | **los 127 candidatos del lote 4** | **los 14 nuevos y los 6 corregidos viajan dentro del commit** (`D.25`), asi que quien lea *de `cap_13` salieron 12 candidatos* **puede abrir los doce** |

## Q.12.e. LO QUE PASA A LA VUELTA SIGUIENTE

| que | cifra | quien lo desbloquea |
|---|---|---|
| **`cap_14`**, la ultima unidad sin minar del lote 4 | **7.638** palabras | **y con el, el cierre del lote 4** |
| **las 53 aristas declaradas y no cableadas** | **53** | el mismo acto: la insercion del lote cerrado |
| **los veredictos sin sede propia** | **12 de la vuelta 22 mas 14 pares de hoy** | idem |
| **la relectura ancha de cinco filas del freno** | **96 ocurrencias** sin adjudicar | una tarea propia, que propongo en `Q.11.b` |
| **la pregunta del rotulo de `cap_14`** | 1 | Alexis o el auditor, y va en `Q.11.a` |

## Q.12.f. LA IDENTIDAD DE LA VUELTA, **LEIDA DE GIT** (`EXTRACTOR.md` 5)

Salida de los comandos, guardada en `.t1_v23/identidad_v23.txt`:

    $ git rev-parse --abbrev-ref HEAD
    extraccion-mundo-11
    $ git log --oneline b05d040..HEAD | wc -l
    6
    $ git log -1 --format="%h %ad" --date=iso
    f8ebe88 2026-09-13 13:14:03 -0400
    $ git diff --name-only b05d040..HEAD | sed "s#/.*##" | sort | uniq -c
         18 .aduana_v23
          1 .aduana_v23_tmp.txt
         40 .t1_v23
          7 .v23
         20 cuarentena
          1 docs

## Q.12.g. LA VUELTA 23, EN UNA TABLA

| | |
|---|---|
| **tareas encargadas** | **4**, el tope es 5. **Las cuatro CERRADAS**, una de ellas (la 4) **cerrada declarando que no se hace y por que**. Cero cola por techo de tareas |
| **la cola de siete** | **CERRADA ENTERA Y PRIMERA**, como el encargo mandaba. Seis tocan fichero y **las seis vuelven a pasar la aduana**; la septima es encargo para el dia de la insercion y queda escrita dos veces |
| **unidades minadas** | **`cap_12` (`Getting Started`) y `cap_13` (`Afterword`), las dos ENTERAS**, con su frontera cerrada contra el cuerpo al digito (**2.118** y **9.298** palabras) |
| **candidatos nuevos** | **14** (2 mas 12), **bajo el techo de 15**. Hueco que queda: **1** |
| **`cap_14`** | # **NO ENTRA, y se declara con su cuenta**: 7.638 palabras no caben en un hueco de un candidato, y `EXTRACTOR.md` 12.4 prohibe repartir un capitulo en dos vueltas |
| **aduana** | **21 corridas del informe de un candidato**, una por candidato en su acto **mas una repeticion** por una correccion posterior. Saldo en `Q.5.d`. # **CERO `CAERIA` en las 20** |
| **insercion** | # **CERO, por sexta vez con la puerta abierta**, y la razon medida: **al lote 4 le falta `cap_14` y solo `cap_14`**. Grafo `203` a `203`, bitacora `148` a `148`, `_insertados` `201` a `201` |
| **veredictos** | **21 pares distintos leidos, 28 filas con su razon escrita** (una fila y su espejo son un par). **Su sede hoy es este reporte y lo digo**; `bitacora/` lo sera el dia de la insercion |
| **aristas** | **53 declaradas y no cableadas** (`35` heredadas, `2` de la correccion 6, `16` nuevas), **repetidas enteras en `Q.7`** con su paso impreso del fichero |
| **`PASOS INVENTADOS`** | **peor fila firmada `cap_04` `16,67` contra tope `10`**. # **EL FRENO SIGUE DISPARADO Y EL TRAMO SIGUE EN DOS CAPITULOS, que son los dos que esta vuelta mino.** Lote 4 **`2,32` (35 de 1.511)**, **declarado INCOMPLETO**: cinco filas sin releer con el ancho |
| **discutibles** | **12, marcados antes de saber si acierto**, y en ocho escribo el argumento contra mi propia decision |
| **caidas mias** | **6, las seis cazadas ANTES de publicar**, y **tres de las seis las cazo un instrumento y no mi cuidado** |
| **guardas** | `gate`, `guiones` y `test_aceptacion` **corridas al cerrar**. Hook verde en todos los commits, **ninguno saltado**, y el tallado **aborto uno y se arreglo regenerando** |
| **tablas de instrumento** | **todas pegadas de su fichero, ninguna tecleada**, comprobadas celda a celda por el hook en cada commit |
| **paradas** | # **CERO.** Nada contradijo una regla vigente ni una cifra publicada con su corte |

> # **LA VUELTA 23 CIERRA `cap_12` Y `cap_13` ENTEROS, PAGA LA COLA DE SIETE DEL AUDITOR COMPLETA, Y DEJA EL LOTE 4 A UN SOLO CAPITULO DE CERRAR.**
>
> **Y LA COSA QUE MAS ME IMPORTA DE ESTA VUELTA NO ES LA CIFRA DE CANDIDATOS: ES QUE NINGUNA TABLA
> SE TECLEO.** Mi racha `REPORTE` se reinicio contra `D.41` despues de **cuatro caidas en cuatro
> vueltas que eran la misma cosa**. Esta vuelta el tallador **me cazo dos veces en el acto** (`Q.9`
> caidas 4 y 5) y **las dos se arreglaron regenerando**, no tecleando la celda buena.
>
> **LO QUE ESO PRUEBA, Y NO ES UN MERITO MIO:** *un remedio que se cumple acordandose no es un
> remedio.* La diferencia entre la vuelta 22 y esta **no es que yo tenga mas cuidado: es que hay
> codigo mirando.**
