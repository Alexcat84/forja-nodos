
**LO QUE MI MEDIDA CONFIRMA Y LO QUE DESMIENTE, y la discrepancia se declara en vez de resolverse
copiando** (`EXTRACTOR.md` 5):

| | el encargo (arbol de ayer) | mi corrida (hoy) | |
|---|---:|---:|---|
| vecinos levantados | `1` | **`1`** | **igual**, y es el mismo |
| `paso_contra_nodo` | `0,733` | **`0,733`** | **igual** |
| `familia_id` | `0,100` | **`0,100`** | **igual** |
| `similitud_texto` | `0,246` | **`0,215`** | **BAJA**, y la causa es mia: la señal 1 compara titulo mas `resumen_teorico` mas pasos, y yo le he metido `1.977` caracteres de correccion declarada al `resumen_teorico`. **La correccion de la `TAREA 1.B` movio una señal**, y lo digo yo antes de que se note |
| saldo | `BLOQUEARIA` | **`BLOQUEARIA`** | **igual**. `0` caen, `0` chocan |

> **Y UNA MEDIDA QUE NO ME PIDE NADIE Y QUE VALE MAS QUE MI FILA: EL INFORME DE UN SOLO CANDIDATO
> COSTO `1.187` SEGUNDOS.** Casi **veinte minutos**, cronometrados de `04:04:12` a `04:23:59` sobre una
> poblacion de `348` (`321` del grafo mas `27` de bandejas), o sea **`3,41` segundos por nodo de
> poblacion, para UN candidato**. El encargo me daba `483` segundos por candidato de aduana: **son
> `2,5` veces esa cifra**, y no es una corrida lenta, es un proceso al `96` por ciento de CPU
> (`1.070` segundos de CPU en `1.110` de reloj, `Get-Process python`). **`D.43` saco el informe de LOTE
> del turno del extractor con esta misma aritmetica**; el de un candidato suelto sigue siendo mio y hoy
> cuesta lo que costaba entonces un lote pequenio. **No propongo quitarlo: propongo que la cifra este
> escrita**, porque el tramo de esta vuelta se dimensiono con `483` y la medida dice otra cosa.

### CC.6.f. **UNA FILA POR CANDIDATO, ESCRITA EN EL ACTO EN QUE ENTRA** (`TAREA 4`)

*Cada subseccion de aqui abajo se anexo al reporte **con el candidato ya dentro y antes de arrancar el
siguiente**. No es un resumen escrito al final: es el registro creciendo al ritmo de la insercion, que
es lo que `EXTRACTOR.md` 3 pide y lo que las dos vueltas anteriores no hicieron.*

#### CC.6.f.1. **CANDIDATO `1` DE `3`: `pedir_critica_primero_crear_seguridad_psicologica` (`L73`), DENTRO**

<!-- TALLADO: parcial salida=.v39/informes/i01_pedir_critica_primero.txt -->

    $ python forja.py insertar cuarentena/scott_radical_candor/pedir_critica_primero_crear_seguridad_psicologica.json [veredictos y censos]
    DECLARADOS POR LECTURA: 7. Ninguna señal los levanto.
    VECINOS POR ENCIMA DE UMBRAL: 1. LA INSERCION QUEDA BLOQUEADA.
      ARISTA EN COLA, no cableada: pedir_critica_primero_crear_seguridad_psicologica > abrazar_incomodidad_silencio_contar_seis
      ARISTA EN COLA, no cableada: pedir_critica_primero_crear_seguridad_psicologica > dar_elogio_disciplina_igual_critica
      arista madre-hijo cableada y escrita RESUELTA: empezar_cultura_franqueza_radical > pedir_critica_primero_crear_seguridad_psicologica
      ARISTA EN COLA, no cableada: pedir_critica_primero_crear_seguridad_psicologica > escuchar_entender_critica_dominar_defensa
      arista madre-hijo cableada y escrita RESUELTA: pedir_critica_primero_crear_seguridad_psicologica > fomentar_guia_reciproca_companieros
      ARISTA EN COLA, no cableada: pedir_critica_primero_crear_seguridad_psicologica > medir_critica_respuesta_oyente_brujula
      ARISTA EN COLA, no cableada: pedir_critica_primero_crear_seguridad_psicologica > premiar_franqueza_hacer_escucha_tangible
    GATE VERDE sobre la simulacion. NODO INSERTADO en dataset/nodos.jsonl.
      nodos en el grafo: 322
      censos escritos: denominaciones, series_y_cabezas
      veredictos en bitacora/VEREDICTOS.jsonl: 8
    CODIGO DE SALIDA: 0
      ARCHIVADO EN EL MISMO ACTO (D.31): cuarentena/_insertados/scott_radical_candor/pedir_critica_primero_crear_seguridad_psicologica.json
