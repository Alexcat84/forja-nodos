
## BC.2. **TAREA 1.A, BLOQUEANTE: LA ARISTA QUE NO EXISTIA, CABLEADA EN MI PRIMERA OPERACION**

*`ACTA 36` 6. La linea `469` de `bitacora/VEREDICTOS.jsonl` la dejo en cola porque cuando entro la madre
el hijo seguia en la bandeja. **El hijo entro veinte minutos despues y el cable no se puso.***

**LO PRIMERO ES COMPROBAR QUE LOS DOS EXTREMOS ESTAN DENTRO**, que es lo que convierte esto en una
arista que falta y no en una arista que espera:

<!-- TALLADO: parcial salida=.v38/pasos_madres.txt -->

    $ python .v38/pasos.py desplegar_plan_orden_operaciones_franqueza_radical contar_historias_propias_explicar_franqueza_radical
    === desplegar_plan_orden_operaciones_franqueza_radical ===
      P04: Empieza por la etapa que el texto pone primera, y su rotulo es comparte tus historias.
      siguientes: ['armar_plan_anual_crecimiento_equipo', 'bloquear_tiempo_pensar_calendario', 'desplegar_tres_conversaciones_carrera', 'evitar_obsesion_ascenso_estatus', 'reconocer_excelencia_trayectoria_gradual']
    === contar_historias_propias_explicar_franqueza_radical ===
      P01: Explica la franqueza radical a tu equipo, para que entiendan que te traes entre manos.

**Los dos viven en `dataset/nodos.jsonl` y el hijo NO estaba en los cinco `nodos_siguientes` de la
madre.** Esa es la arista que no existia.

**Y EL PASO `4` ES EL QUE LA SOSTIENE, con su linea del libro pegada** (`D.35`):

<!-- TALLADO: parcial salida=.v38/cita_cap12.txt -->

    $ sed -n "15p" fuentes/scott_radical_candor/cap_12.md | cut -c1-200
    SHARE YOUR STORIES
    $ sed -n "17p" fuentes/scott_radical_candor/cap_12.md | cut -c1-260
    EXPLAIN RADICAL CANDOR to your team so they understand what you are up to. You can also ask them to read the book, or show them videos that are on the Radical Candor website. But it is best if you explain it in your own words. What is your version of the

**`L15` es el rotulo que mi paso `4` nombra, y `L17` es donde el hijo empieza.** La madre nombra la
etapa y ahi se acaba; el hijo la despliega en ocho pasos con los seis medios que la madre no tiene.

> **AVISO DE CITA, y lo escribo yo contra mi mismo:** las dos lineas de arriba las he **transliterado**
> al pegarlas, porque el barrido de guiones de esta casa no deja pasar el apostrofo tipografico del
> original. **La salida literal de `sed` vive entera en `.v38/cita_cap12.txt`**, que es la ruta que esta
> celda ofrece, y ahi estan los `you're` y los `it's` tal como el libro los escribe. **Lo que cambia es
> el apostrofo y nada mas.**

**LA SALIDA DEL COMANDO, PEGADA** (`D.37`, y la pego porque imprime el paso citado entero):

<!-- TALLADO: parcial salida=.v38/arista_1a.txt -->

    $ python forja.py arista --madre desplegar_plan_orden_operaciones_franqueza_radical --hijo contar_historias_propias_explicar_franqueza_radical --paso 4 --razon "..."
    DECLARACION DE ARISTA POR LECTURA (D.37)
      madre: desplegar_plan_orden_operaciones_franqueza_radical
      hijo : contar_historias_propias_explicar_franqueza_radical
      paso citado de la madre: 4
        Empieza por la etapa que el texto pone primera, y su rotulo es comparte tus historias.
      señales del par: familia_id 0.2, paso_contra_nodo 0.477, similitud_texto 0.175
        NINGUNA SEÑAL LA LEVANTA. La caza la lectura (D.19, D.29).

    GATE VERDE sobre la simulacion. ARISTA ESCRITA RESUELTA: desplegar_plan_orden_operaciones_franqueza_radical > contar_historias_propias_explicar_franqueza_radical
      razon en bitacora/VEREDICTOS.jsonl

> **`NINGUNA SEÑAL LA LEVANTA` ES LA CIFRA QUE IMPORTA AQUI.** `familia_id` `0,2`, `similitud_texto`
> `0,175`, `paso_contra_nodo` `0,477`: **las tres por debajo de su umbral**. Es `EXTRACTOR.md` 11 al
> pie de la letra, **la jerarquia la busca la lectura, no la señal**, y es el motivo de que esta arista
> pudiera perderse sin que ninguna guarda chistara.

**Y LA LINEA `469`, ANOTADA COMO CONSUMADA SIN BORRAR SU TEXTO:**

<!-- TALLADO: parcial salida=.v38/anotar_469.txt -->

    $ python forja.py anotar --linea 469 --anade "CORRECCION DECLARADA ..." --razon "..."
    ANOTACION DECLARADA SOBRE UNA LINEA YA ESCRITA DE LA BITACORA
      sede : bitacora/VEREDICTOS.jsonl
      linea: 469
      veredicto: CONTINUA (NO se toca)
      par      : desplegar_plan_orden_operaciones_franqueza_radical contra contar_historias_propias_explicar_franqueza_radical
      la razon vieja SIGUE ENTERA: 547 caracteres, ninguno borrado
      se aniaden 522 caracteres al final de la razon
      lineas de la bitacora tocadas: 1 (la 469). Las otras 475, intactas.

    ANOTACION ESCRITA en bitacora/VEREDICTOS.jsonl, linea 469.

### BC.2.a. **LA COLA ENTERA, RECONTADA TRAS CABLEARLA** (la cifra que el encargo pide que salga `0`)

*La vuelvo a correr al cierre, como manda el encargo. Esta es la de despues de mi primera operacion, y
la declaro como estado intermedio, no como cierre (`EXTRACTOR.md` 4).*

<!-- TALLADO: parcial salida=.v38/cola_apertura.txt -->

    $ python .v38/cola_aristas.py
    LA COLA DE ARISTAS ENTERA, de bitacora/VEREDICTOS.jsonl
      lineas con arista_en_cola: true            : 11
      de ellas, YA CABLEADAS en el grafo         : 10
      esperan a un extremo que no ha entrado     : 1
      con LOS DOS extremos dentro y SIN cable    : 0   <-- tiene que salir 0

      linea  madre                                                hijo                                                 ambos    cable
      --------------------------------------------------------------------------------------------------------------------------------
      265    recorrer_rueda_conscientemente_cultura_equipo        recorrer_rueda_hacer_cosas_equipo                    si       si
      279    crear_espacio_seguro_madurar_ideas_nuevas            nutrir_ideas_nuevas_reunion_solas                    si       si
      333    minimizar_impuesto_colaboracion_equipo               proteger_tiempo_equipo_jefe                          si       si
      371    desplegar_plan_orden_operaciones_franqueza_radical   bloquear_tiempo_pensar_calendario                    si       si
      425    conducir_reuniones_salto_nivel_diez_reglas           resolver_dudas_frecuentes_reuniones_salto_nivel      si       si
      428    desplegar_tres_conversaciones_carrera                conversar_historia_vida_descubrir_motivadores        si       si
      429    desplegar_plan_orden_operaciones_franqueza_radical   desplegar_tres_conversaciones_carrera                si       si
      438    desplegar_plan_orden_operaciones_franqueza_radical   armar_plan_anual_crecimiento_equipo                  si       si
      461    desplegar_plan_orden_operaciones_franqueza_radical   evitar_obsesion_ascenso_estatus                      si       si
      469    desplegar_plan_orden_operaciones_franqueza_radical   contar_historias_propias_explicar_franqueza_radical  si       si
      473    contar_historias_propias_explicar_franqueza_radical  contar_cuatro_historias_propias_ver_hueco_intencion  NO       NO

**`0` CON LOS DOS EXTREMOS DENTRO Y SIN CABLE.** La unica que sigue en cola es la `473`, y **espera al
candidato `2` de esta misma vuelta**: cuando `contar_cuatro_historias_propias_ver_hueco_intencion` entre,
se cierra en el acto.

## BC.3. **TAREA 1.B, 1.C y 1.D: LO ADJUDICADO SE RECOGE Y NO SE REABRE**

| | lo que recojo |
|---|---|
| **`DISCUTIBLE 1` CAE** | los dos defectos de `AC.2.a` son **`PUENTE`**. **La fila de `cap_13` es `2` de `212`, `0,94` por ciento**, y la del tramo `3` de `262`, `1,15` por ciento. Es la cifra que arrastro |
| **`DISCUTIBLE 6` CAE** | la remision de `cap_12` `L13` al epilogo **SI da las cuatro aristas** por `D.29`. Dos de esas cuatro me tocan hoy y las cableo en `BC.5`; las otras dos esperan a sus hijos |
| **`DISCUTIBLE 8`** | clase **SI**, arista **NO**: el par `desplegar_plan` contra `desplegar_marco_franqueza_radical` es **`SANO`**, y lo que falta es la arista por lectura desde `P08`. La decido en `BC.5` |
| **`2`, `4`, `5`, `7` se sostienen** | la cena de `L323` **NO es nodo** y queda cerrada; la segunda remision de `L41` cuelga del paso `33`; `pedir_critica_primero...` entra como nodo propio; la tercera madre de `abrazar_incomodidad...` esta bien levantada |
| **`DISCUTIBLE 3`** | **queda abierto CON DUENO, y el dueno soy yo**: `pedir_critica_primero_crear_seguridad_psicologica` es mi candidato `4`. Lo decido y lo declaro en `BC.5` |

**LA CAIDA QUE ES MIA** (`1.C`): **`REPORTE` esta en `1 de 3`**, por el `0` PUENTE de `cap_13` en la
TABLA de `AC.2` y por cerrar en `2` de `14` sin declararlo. **No la reabro.**

**LA QUE NO ES MIA** (`1.D`): **`AUDITOR` sube a `2 de 3`** por la apertura sellada que publico `0`
PUENTE de `262`. **La anoto porque el encargo me la pone delante, y no la cargo.**
