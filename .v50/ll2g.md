
### LL.2.g. **CANDIDATO `2` DE `3`: `P42`, `agrupar_interrupciones_subordinados_reuniones_regulares`**

| | |
|---|---|
| **pieza y rango** | `P42`, `L317 a L317`, **`74` palabras**, las de `HH.2.c` y recomputadas en `LL.2.d` |
| **frontera dentro del nodo** | el tramo entero es de este nodo: **cero frontera interna y cero solapes**. L317 es una sola linea de prosa corrida |
| **pasos** | **`5`** |
| **fidelidad `D.30` en el acto** | **`5` TRANSCRIPCION, `0` PUENTE** |
| **puentes que estuve a punto de escribir** | **`2`, declarados dentro de la ficha**: EL PERIODO (poner *semanalmente* donde el libro dice `held regularly`) y EL RESPONSABLE (decir a quien se le pide que agrupe, cuando el libro lo escribe en pasiva) |
| **lo que el renglon dice y NO es paso** | `the subject of the next chapter`. **Es una remision**, y nombrar no es procedimentar: ese capitulo es otra unidad |

**LA FIDELIDAD, PASO A PASO Y CONTRA SU RENGLON**, con el `sed` pegado en `LL.2.c` fila `2`:

| paso | de donde sale, dentro de L317 | veredicto |
|---:|---|---|
| 1 | `Also, if you use the production principle of batching, that is, handling a group of similar chores at one time` | **TRANSCRIPCION** |
| 2 | `many interruptions that come from your subordinates can be accumulated and handled not randomly` | **TRANSCRIPCION** |
| 3 | `but at staff and at one-on-one meetings` | **TRANSCRIPCION** |
| 4 | `If such meetings are held regularly` | **TRANSCRIPCION** |
| 5 | `people cannot protest too much if they are asked to batch questions and problems for scheduled times, instead of interrupting you whenever they want` | **TRANSCRIPCION** |

> **LA UNICA LICENCIA DE ESTA TABLA, DECLARADA:** la fila `5` escribe `cannot` y `they are` donde el
> renglon del libro pone las contracciones. **El renglon literal esta pegado sin tocar en la ficha**
> y su linea entera esta en `LL.2.c`; aqui va desatado por mecanica de escritura y no por lectura.

**LA PASADA DE ADUANA, CON SU RELOJ:**

<!-- TALLADO: parcial salida=.v50/informe_02.txt -->

    $ python forja.py informe cuarentena/grove_high_output/agrupar_interrupciones_subordinados_reuniones_regulares.json
    poblacion del barrido       : 392   (346 del grafo mas 46 que esperan en bandejas)
    EL SALDO
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0
    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 7
      por candidato bloqueado          : menor 7, mediana 7, mayor 7
      que senial levanta cada vecindad  : paso_contra_nodo 3, similitud_texto 4

<!-- TALLADO: parcial salida=.v50/reloj_c02.txt -->

    reloj del candidato 2 (P42), pasada de aduana propia
    segundos: 335.0

**`0 CAERIA` Y `0` CHOQUES DENTRO DEL LOTE**, que es la cifra que mas me interesaba: **`P41` y
`P42` salen del mismo parrafo del libro y no chocan.**

### LL.2.h. **LOS SIETE VECINOS DE `P42`, LEIDOS, Y LOS SIETE SON MIOS DE EXPLICAR**

<!-- TALLADO: parcial salida=.v50/informe_02.txt -->

    [BLOQUEARIA] agrupar_interrupciones_subordinados_reuniones_regulares
        vecino sostener_contacto_oferta_aceptacion  [levantada por: paso_contra_nodo]
          similitud_texto 0.094 | familia_id 0.000 | paso_contra_nodo 0.700
          paso 4 del candidato contra paso 3 de sostener_contacto_oferta_aceptacion
        vecino agendar_cuidados_propios_cumplirlos  [levantada por: paso_contra_nodo]
          similitud_texto 0.129 | familia_id 0.000 | paso_contra_nodo 0.615
          paso 4 del candidato contra paso 4 de agendar_cuidados_propios_cumplirlos
        vecino nombrar_delegados_amigos_casa  [levantada por: paso_contra_nodo]
          similitud_texto 0.127 | familia_id 0.000 | paso_contra_nodo 0.609
          paso 4 del candidato contra paso 4 de nombrar_delegados_amigos_casa
        vecino preparar_respuestas_estandar_interrupciones_repetidas  [levantada por: similitud_texto]
          similitud_texto 0.536 | familia_id 0.111 | paso_contra_nodo 0.417
          paso 1 del candidato contra paso 1 de preparar_respuestas_estandar_interrupciones_repetidas
        vecino llevar_inventario_proyectos_discrecionales  [levantada por: similitud_texto]
          similitud_texto 0.352 | familia_id 0.000 | paso_contra_nodo 0.478
          paso 1 del candidato contra paso 1 de llevar_inventario_proyectos_discrecionales
        vecino buscar_regularidad_bloques_iguales_trabajo_mando  [levantada por: similitud_texto]
          similitud_texto 0.426 | familia_id 0.000 | paso_contra_nodo 0.415
          paso 1 del candidato contra paso 1 de buscar_regularidad_bloques_iguales_trabajo_mando
        vecino identificar_paso_limitante_jornada_desfases  [levantada por: similitud_texto]
          similitud_texto 0.351 | familia_id 0.000 | paso_contra_nodo 0.377
          paso 4 del candidato contra paso 1 de identificar_paso_limitante_jornada_desfases

| vecino | senial que lo levanta | mi lectura |
|---|---:|---|
| `preparar_respuestas_estandar_interrupciones_repetidas` (`P41`) | `0,536` de senial `1` | **HERMANO, y es el par mas alto de la tanda.** Salen de renglones consecutivos del mismo parrafo (L315 y L317) y el libro los escribe como **dos remedios distintos**: alli QUE se responde, aqui CUANDO se atiende. **Cero pasos compartidos**, y la propia aduana dice `CHOCAN dentro del lote: 0` |
| `buscar_regularidad_bloques_iguales_trabajo_mando` (`P39`) | `0,426` de senial `1` | **HERMANO.** Mi paso `4` pide que las reuniones sean regulares y aquel despliega la regularidad como operacion propia: este la **nombra** y no repite sus pasos |
| `llevar_inventario_proyectos_discrecionales` (`P36`) | `0,352` de senial `1` | **AJENO.** Comparte la formula *aplica aqui un principio de produccion* y nada mas: alli el objeto es el proyecto discrecional |
| `identificar_paso_limitante_jornada_desfases` (`P32`) | `0,351` de senial `1` | **AJENO.** Mi paso `4` contra su paso `1`: los dos hablan de calendario y de principios de produccion, y ninguno comparte objeto |
| `sostener_contacto_oferta_aceptacion` (`smart_who`) | **`0,700` de senial `3`** | **AJENO, y es el mas alto de los tres.** Su paso `3` es *Manten el contacto con ella con regularidad* y mi paso `4` es *Manten esas reuniones con regularidad*. **La misma forma de frase y ni un objeto en comun**: alli el objeto es un candidato al que se le hizo una oferta |
| `agendar_cuidados_propios_cumplirlos` (`scott_radical_candor`) | `0,615` de senial `3` | **AJENO.** Su paso `4` es *No te saltes esas reuniones contigo mismo*: la palabra compartida es *reuniones* |
| `nombrar_delegados_amigos_casa` (`smart_who`) | `0,609` de senial `3` | **AJENO.** Su paso `4` es *Asegurate de que los delegados reportan con regularidad*: la expresion compartida es *con regularidad* |

**LO QUE LOS SIETE MIDEN JUNTOS, Y ES UNA MEDIDA CONTRA MI PROPIA ESCRITURA:**

<!-- TALLADO: parcial salida=.v50/encuadre.txt -->

    $ grep -c "levantada por: similitud_texto" .v50/informe_01.txt .v50/informe_02.txt
    .v50/informe_01.txt:2
    .v50/informe_02.txt:4
    $ grep -c "paso 1 del candidato contra paso 1" .v50/informe_01.txt .v50/informe_02.txt
    .v50/informe_01.txt:1
    .v50/informe_02.txt:3
    $ grep -h "paso .* del candidato contra" (los dos informes, agrupado y ordenado)
          2 paso 1 del candidato contra paso 1 de buscar_regularidad_bloques_iguales_trabajo_mando
          1 paso 5 del candidato contra paso 3 de llevar_inventario_proyectos_discrecionales
          1 paso 4 del candidato contra paso 4 de nombrar_delegados_amigos_casa
          1 paso 4 del candidato contra paso 4 de agendar_cuidados_propios_cumplirlos
          1 paso 4 del candidato contra paso 3 de sostener_contacto_oferta_aceptacion
          1 paso 4 del candidato contra paso 1 de identificar_paso_limitante_jornada_desfases
          1 paso 1 del candidato contra paso 1 de preparar_respuestas_estandar_interrupciones_repetidas
          1 paso 1 del candidato contra paso 1 de llevar_inventario_proyectos_discrecionales

**`4` DE LOS `6` LEVANTAMIENTOS DE SENIAL `1` DE LA TANDA SON `paso 1 contra paso 1`**, y mi paso
`1` es siempre el de encuadre, el que traslada la formula con la que el libro abre cada principio
de produccion. **Y `3` de los `3` de senial `3` caen sobre mi paso `4` de `P42`, que tiene CINCO
palabras.**

> **NO ES QUE EL MATERIAL SE REPITA: ES QUE MIS PASOS CORTOS Y MIS PASOS DE ENCUADRE SE PARECEN
> ENTRE SI MAS QUE LOS PROCEDIMIENTOS QUE CONTIENEN.**

**LO REGISTRO CON SU MEDIDA Y NO ABRO DOCTRINA CON ELLO** (`D.56`, y el encargo me lo manda asi):
`EXTRACTOR.md` 11 ya publica que la senial `3` trae **`2,4` de cola falsa por candidato** y hoy me
trae **`3`** en un candidato de `5` pasos, o sea **dentro de lo medido**. **Y no cambio el paso `4`
para bajar la senial**: el libro escribe `If such meetings are held regularly`, y quitarlo o
engordarlo para complacer a un umbral seria escribir yo lo que el libro no escribe.
