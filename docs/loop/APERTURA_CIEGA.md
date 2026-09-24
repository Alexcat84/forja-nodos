# APERTURA CIEGA DE LA VUELTA 65, lote 7 (`grove_high_output`), **CLASE INSERCION**

*Auditor `claude-opus-5-5`, fase ciega, 23 sep 2026, la que el arnes numera `VUELTA 1` en la corrida que
arranco a las `21:50`. Linea **serial**, rama `extraccion-mundo-11`, arbol en `f770c8c`. **Es la segunda fase
ciega de la `65`**: la primera se paro a las `21:04` para reiniciar el equipo y quedo anulada sin sello
(`docs/loop/archivo/interrumpidas/2026-09-23-v65-fase-ciega/LEEME.md`: *no se reutiliza nada de aqui*). **No
he abierto sus clases ni sus partes**: todo lo de esta pagina sale de `.v65aud/`, escrito y corrido en esta
fase. Modo austero (`D.47`).*

## 0. **LA HERENCIA** (`D.40`)

ACTA ANTERIOR LEIDA: 37ecde5c2c542fb52426e7fac85127efb5e226d7

HEREDADO 1: NO APLICA en esta fase. **Motivo:** `R5` es un remedio **del extractor** y se mide **sobre su
reporte de la `65`** (`ACTA 63` `63.11`: *el reporte de la `65`, con `.v64ext/pegado64.py` y
`.v64aud/normal/bloques_mudos.py`*), y el reporte **no esta en el arbol**: el arnes lo retiro para esta fase
(`D.34.2`) y no lo recupero por ninguna via. **Se mide en mi turno normal**, con los dos instrumentos y la
cabecera del tramo cambiada a la vuelta `65`. Lo que si esta en mi mano lo cumplo en mi propia pagina:
**cada bloque `$` de esta apertura lleva la salida entera de su comando**, copiada de su fichero de
`.v65aud/`.

    $ ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl
    ls: cannot access 'docs/loop/REPORTE.md': No such file or directory
    ls: cannot access 'docs/loop/ultimo_extractor.json': No such file or directory
    ls: cannot access 'docs/loop/ultimo_auditor.json': No such file or directory
    ls: cannot access 'docs/loop/CREDITO_serial.jsonl': No such file or directory
    $ grep -n "VUELTA 1 : APERTURA CIEGA" docs/loop/loop.log | tail -1
    5251:[2026-09-23 21:50:18] VUELTA 1 : APERTURA CIEGA (claude-opus-5-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl

**LA HUELLA** es la que el prompt me entrega; **no la he recomputado**, porque `forja.py herencia` lee en esta
fase un fichero retirado (`d146`) y no lo corro aqui.

## 1. **LO QUE VI SIN BUSCARLO, Y LO DIGO ANTES DE MEDIR** (`d146`)

**La foto de `git status` que el entorno me pone delante trae los asuntos de los commits del extractor**, y
uno es el cierre de su vuelta: `d122a40` *Vuelta 65 cerrada: las 20 filas de Grove insertadas una por vez
(grafo 366, bandeja 71), 55 registros en la bitacora, 7 aristas por lectura cableadas, pasos inventados cap_02
4 de 50 y cap_03 2 de 108, guardas en verde*. **Lo lei antes de medir nada.** Es el tercer hueco de `d146`,
ya anotado por la `ACTA 63`, y no lo arreglo yo (`D.45`).

**LO QUE HAGO CON ELLO:** ninguna cifra de esta pagina sale de ese asunto. **Todas salen de un instrumento
corrido en esta fase**, con su salida al lado, y donde coinciden con el asunto lo digo como coincidencia y no
como fuente. **Las clases no las toca**: el asunto no nombra ningun veredicto ni ningun vecino. **No he
abierto `bitacora/VEREDICTOS.jsonl` por dentro**: de ella solo cuento lineas.

## 2. **EL ALCANCE, Y EL CENSO QUE LO SOSTIENE**

**La tanda son las filas `1` a `20` del orden comprobado** (encargo de la `65`, TAREA 2 punto 2), que son
las `20` primeras lineas de `.v64ext/los22.txt`: siete de `cap_02` y trece de `cap_03`. Las filas `21` y `22`
(`variar_frecuencia_inspeccion_nivel_calidad` y `simplificar_trabajo_reducir_numero_pasos`) **no entraban**.

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        366 dataset/nodos.jsonl
        795 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1162 total
    $ ls cuarentena/grove_high_output/*.json | wc -l
    71
    $ ls cuarentena/_insertados/grove_high_output/*.json | wc -l
    21
    $ ls cuarentena/grove_high_output/ | grep -E "variar_frecuencia|simplificar_trabajo"
    simplificar_trabajo_reducir_numero_pasos.json
    variar_frecuencia_inspeccion_nivel_calidad.json

(`.v65aud/censo.txt`.) **LECTURA:** contra el censo de la `ACTA 63` `63.1` (`346`, `740`, `1`, `91`), el grafo
sube `20`, la bandeja baja `20`, la bitacora gana `55` lineas y los pares mutuos no se mueven. **De los `21` de
`_insertados`, `20` son la tanda** (el instrumento de la seccion `3` encuentra los `20` ahi) y el
otro es `revisar_tres_preguntas_valor_carrera`, que ya estaba en `997054d`
(`git ls-tree --name-only 997054d cuarentena/_insertados/grove_high_output/` da solo ese, en
`.v65aud/insertados_antes.txt`). **Las dos filas que no entraban siguen en
la bandeja.** Cuanto de los `55` es de cada candidato no lo mido aqui: seria abrir la bitacora.

**Y DESDE QUE LA `65` CERRO, EL DATO NO SE HA MOVIDO; LA BANDEJA DE OTRO LIBRO, SI:**

    $ git diff --stat d122a40 HEAD -- dataset/ bitacora/ censos/ config/pares_mutuos.jsonl cuarentena/grove_high_output cuarentena/_insertados | wc -l
    0
    $ git diff --name-status d122a40 HEAD -- cuarentena/ | awk '{print $1, $2}' | sed 's#cuarentena/\([^/]*\)/.*#\1#' | sort | uniq -c
         17 A marquet_turn_the_ship
          3 M marquet_turn_the_ship

(`.v65aud/desde_d122a40.txt`.) **LECTURA:** la cosecha de Marquet (`f770c8c`, `21:49`) trajo a esta rama `17`
candidatos nuevos en `cuarentena/marquet_turn_the_ship/` (la lista en `.v65aud/marquet_nuevos.txt`) **despues
de que la `65` insertara**. **Mi barrido los tiene en su poblacion y la aduana de la `65` no los tenia.** No es
falta de nadie; es la razon de que la seccion `6` los cuente aparte.

## 3. **LO QUE ENTRO ES LO QUE SE LEYO** (`D.58`)

`D.58` pide la relectura de fidelidad **entera** del lote en la vuelta de insercion, sobre lo que entra, y la
`ACTA 63` `63.1` dejo escrito que **ya estaba hecha sobre esos mismos bytes** (`b63405c` para los `16` de la
`63`, `997054d` para los seis de `d005`). **Lo compruebo del lado del grafo**, que es el que importa ahora: el
nodo que vive hoy en `dataset/nodos.jsonl` contra la ficha del commit de su lectura, campo a campo, y el
fichero de `_insertados` contra ese mismo blob.

    $ python .v65aud/entra_lo_leido.py | tail -6
    nodos de la tanda en el grafo iguales a su lectura entera: 20 | distintos: 0
    fichas de _insertados con el mismo blob que su lectura entera: 20 | distintas: 0
    capitulo  cand pasos    P   por100
    cap_02       7    50    4     8.00
    cap_03      13   108    2     1.85
    tanda       20   158    6     3.80

(El `tail` va en el comando y el bloque trae todo lo que imprime; la salida del instrumento sin `tail`, con una
fila por candidato, esta en `.v65aud/entra_lo_leido.txt`.)

**LECTURA:** los `20` nodos del grafo tienen **el mismo titulo, las mismas condiciones, los mismos pasos y el
mismo entregable** que la ficha sobre la que se leyo su fidelidad entera, y el registro de `_insertados` es el
mismo blob. **La lectura entera que `D.58` pide esta hecha sobre lo que entro, y no se repite.**

## 4. **`PASOS INVENTADOS POR CAPITULO`, SOBRE LO QUE ENTRO** (`8`, `8.2`)

La misma salida de la seccion `3`, **y rotulo su poblacion antes de la cifra** (`R8`, que la `ACTA 63` retiro
cumplido y yo sigo usando): **los pasos de los `20` nodos tal como viven hoy en el grafo, y los PUENTE que las
lecturas enteras YA ADJUDICADAS les encontraron** (`ACTA 62` `62.5`: los cuatro de `equilibrar`, clausula
reescrita, columna `verbo` de `.v63ext/fidelidad.txt`; `ACTA 63` `63.3.a`: `construir_grafico` paso `5` y
`elegir_fabricar` paso `8`, filas `P` de `.v64ext/fidelidad.tsv`). **No es una lectura mia nueva: es la cuenta
de las adjudicadas, hecha por instrumento.**

| capitulo | que es | pasos que entraron | PUENTE adjudicados | por ciento |
|---|---|---:|---:|---:|
| `cap_02` | Cap. 1, *The Basics of Production* | `50` | `4` | **`8,00`** |
| `cap_03` | Cap. 2, *Managing the Breakfast Factory*, sin las filas `21` y `22` | `108` | `2` | **`1,85`** |
| tanda | | `158` | `6` | `3,80` |

**LECTURA:** los dos capitulos por debajo del `10`, y **los seis puentes entraron ya reescritos** (seccion `3`:
lo que entro es la ficha corregida). **`cap_02` repite la cifra de la `ACTA 62` `62.6` porque entraron sus
siete**; `cap_03` no es ni el `0 de 80` de la `62` ni el `2 de 41` de la `63`, porque aqui van **nueve de la
`63` menos las dos filas que no entraban, mas los seis de `d005`**. **Coincide con el asunto de `d122a40`** que
declare en la seccion `1`; la fuente es el instrumento.

**MI RELECTURA DE HOY, Y SU LIMITE.** He vuelto a leer `cap_02` y `cap_03` enteros (`79` y `179` lineas) y los
`158` pasos tal como viven en el grafo (`.v65aud/pasos_20.txt`), **de corrido y sin fila por paso**: no
encuentro ningun paso que hoy lea como PUENTE en la version que entro. **No lo publico como cifra**, porque no
lleva instrumento de fila por paso; lo digo como lectura para que el turno normal sepa que no traigo ninguna
discrepancia de fidelidad que adjudicar.

## 5. **LAS ARISTAS QUE LA `ACTA 63` DEJO ADJUDICADAS, CONTRA LAS QUE VIVEN** (`D.29`, `D.53`)

    $ python .v65aud/aristas.py
    VIVE      construir_flujo_produccion_paso_limitante        -> rehacer_flujo_paso_limitante_capacidad           (veredictos_listos CONTINUA en construir_flujo_produccion_paso_limitante)
    VIVE      construir_grafico_escalonado_pronosticos         -> casar_flujo_fabricacion_flujo_ventas             (aristas_lectura SOSTENGO)
    VIVE      construir_indicador_tendencia_patron             -> dimensionar_plantilla_administrativa_pronostico  (aristas_lectura SOSTENGO)
    VIVE      detectar_arreglar_fallo_etapa_menor_valor        -> dimensionar_inventario_materia_prima_reposicion  (veredictos_listos CONTINUA en dimensionar_inventario_materia_prima_reposicion)
    NO VIVE   detectar_arreglar_fallo_etapa_menor_valor        -> supervisar_tarea_delegada_etapa_menor_valor      (veredictos_listos CONTINUA en detectar_arreglar_fallo_etapa_menor_valor)
    VIVE      dimensionar_inventario_materia_prima_reposicion  -> decidir_aceptar_rechazar_material_defectuoso     (aristas_lectura SOSTENGO)
    VIVE      elegir_fabricar_pedido_pronostico                -> casar_flujo_fabricacion_flujo_ventas             (aristas_lectura SOSTENGO)
    VIVE      elegir_indicador_salida_trabajo_administrativo   -> dimensionar_plantilla_administrativa_pronostico  (aristas_lectura SOSTENGO)
    VIVE      emparejar_indicadores_efecto_contraefecto        -> elegir_indicador_salida_trabajo_administrativo   (veredictos_listos CONTINUA en elegir_indicador_salida_trabajo_administrativo)
    VIVE      rehacer_flujo_paso_limitante_capacidad           -> equilibrar_capacidad_personal_inventario_plazo   (aristas_lectura SOSTENGO)
    VIVE      representar_actividad_caja_negra_ventanas        -> construir_indicador_linealidad_alerta_temprana   (aristas_lectura SOSTENGO)
    VIVE      representar_actividad_caja_negra_ventanas        -> construir_indicador_tendencia_patron             (aristas_lectura SOSTENGO)
    la de cola (detectar_arreglar_fallo_etapa_menor_valor -> supervisar_tarea_delegada_etapa_menor_valor): no vive
    esperadas 12 | viven 11 | no viven 1 | vivas sin adjudicar 0

(`.v65aud/aristas.txt`; mide `nodos_previos` y `nodos_siguientes` de los `20` en el grafo.) **LECTURA:** las
`8` filas `SOSTENGO` de `.v64ext/aristas_lectura.txt` viven las `8`, y las tres `CONTINUA` de los veredictos
listos cuyo hijo esta en la tanda viven las tres. **La unica que no vive es la que el encargo mando dejar EN
COLA** (el hijo, `supervisar_tarea_delegada_etapa_menor_valor`, es de `cap_04` y sigue en la bandeja), **y no
hay ninguna arista entre los `20` que nadie adjudicara.** De las `8` `SOSTENGO`, la de
`construir_indicador_tendencia_patron` a `dimensionar_plantilla_administrativa_pronostico` era la que iba
**tambien** como `CONTINUA` en los veredictos (encargo, TAREA 3): **las otras siete son las que solo se
cablean por lectura.** Por que medio entro cada una (`arista` o veredicto) **no lo mido aqui**: esta en la
bitacora y en el reporte.

## 6. **MI BARRIDO DE VECINOS, SOBRE GRAFO MAS BANDEJAS** (`D.38.4`, `D.38.5`)

**El metodo.** `.v65aud/barrido_uno.py` toma la ficha de cada uno de los `20` tal como entro
(`cuarentena/_insertados/grove_high_output/`), la normaliza como la normaliza la aduana y le pasa
`aduana.buscar_vecinos` de `src/aduana.py`, **el mismo que usa `insertar`**, contra `dataset/nodos.jsonl` mas
`aduana.poblacion_de_bandejas()` de hoy, que descarta `_insertados` y `_derivadas`. **El candidato no se mide
contra si mismo**: lo excluye `buscar_vecinos` por su id. `.v65aud/barrer.sh` los corrio **cinco a la vez y no
mas**, y los recogio todos dentro de este turno:

    $ grep -E "INICIO|TODOS" .v65aud/barrido.log
    INICIO 2026-09-23 21:52:26
    TODOS TERMINADOS 2026-09-23 23:46:11
    $ grep -c 'rc=0' .v65aud/barrido.log
    20
    $ sort -t= -k3 -n .v65aud/barrido.log | grep rc= | sed -n '1p;$p'
    dimensionar_inventario_materia_prima_reposicion rc=0 segundos=841
    clasificar_trabajo_proceso_montaje_prueba rc=0 segundos=2503

**LECTURA:** la poblacion de hoy es `366` del grafo mas `113` de las bandejas (la cabecera de cada
`.v65aud/barrido_<id>.txt`). **Como los `20` estaban en grafo o en bandeja en cada momento de la `65`, la
union que midio la aduana al insertar es la misma que mido yo, salvo los `17` de Marquet de la seccion `2`.**

**EL CRUCE, contra las lineas que la `ACTA 63` dejo adjudicadas** (`.v64ext/veredictos_listos.txt` y, para
`detectar`, `.v63ext/cmd_02_detectar.sh`). El instrumento **no lee la bitacora**:

    $ python .v65aud/cruce_barrido.py
    construir_flujo_produccion_paso_limitante        pob 479 barrido  3 | con linea  3 | sin linea  0 (de marquet nuevo 0) | linea sin vecino hoy 0
    clasificar_trabajo_proceso_montaje_prueba        pob 479 barrido  1 | con linea  1 | sin linea  0 (de marquet nuevo 0) | linea sin vecino hoy 0
    rehacer_flujo_paso_limitante_capacidad           pob 479 barrido  3 | con linea  3 | sin linea  0 (de marquet nuevo 0) | linea sin vecino hoy 0
    equilibrar_capacidad_personal_inventario_plazo   pob 479 barrido  1 | con linea  1 | sin linea  0 (de marquet nuevo 0) | linea sin vecino hoy 0
    preferir_inspeccion_proceso_prueba_destructiva   pob 479 barrido  4 | con linea  4 | sin linea  0 (de marquet nuevo 0) | linea sin vecino hoy 0
    dimensionar_inventario_materia_prima_reposicion  pob 479 barrido  2 | con linea  2 | sin linea  0 (de marquet nuevo 0) | linea sin vecino hoy 0
    detectar_arreglar_fallo_etapa_menor_valor        pob 479 barrido  1 | con linea  1 | sin linea  0 (de marquet nuevo 0) | linea sin vecino hoy 0
    elegir_cinco_indicadores_diarios_fabrica         pob 479 barrido  0 | con linea  0 | sin linea  0 (de marquet nuevo 0) | linea sin vecino hoy 0
    emparejar_indicadores_efecto_contraefecto        pob 479 barrido  6 | con linea  6 | sin linea  0 (de marquet nuevo 0) | linea sin vecino hoy 0
    elegir_indicador_salida_trabajo_administrativo   pob 479 barrido  3 | con linea  3 | sin linea  0 (de marquet nuevo 0) | linea sin vecino hoy 0
    representar_actividad_caja_negra_ventanas        pob 479 barrido  0 | con linea  0 | sin linea  0 (de marquet nuevo 0) | linea sin vecino hoy 0
    construir_indicador_linealidad_alerta_temprana   pob 479 barrido  0 | con linea  0 | sin linea  0 (de marquet nuevo 0) | linea sin vecino hoy 0
    construir_indicador_tendencia_patron             pob 479 barrido  6 | con linea  6 | sin linea  0 (de marquet nuevo 0) | linea sin vecino hoy 0
    construir_grafico_escalonado_pronosticos         pob 479 barrido  3 | con linea  3 | sin linea  0 (de marquet nuevo 0) | linea sin vecino hoy 0
    archivar_indicadores_resolver_problemas          pob 479 barrido  4 | con linea  4 | sin linea  0 (de marquet nuevo 0) | linea sin vecino hoy 0
    elegir_fabricar_pedido_pronostico                pob 479 barrido  2 | con linea  2 | sin linea  0 (de marquet nuevo 0) | linea sin vecino hoy 0
    casar_flujo_fabricacion_flujo_ventas             pob 479 barrido  0 | con linea  0 | sin linea  0 (de marquet nuevo 0) | linea sin vecino hoy 0
    dimensionar_plantilla_administrativa_pronostico  pob 479 barrido  6 | con linea  6 | sin linea  0 (de marquet nuevo 0) | linea sin vecino hoy 0
    decidir_aceptar_rechazar_material_defectuoso     pob 479 barrido  1 | con linea  1 | sin linea  0 (de marquet nuevo 0) | linea sin vecino hoy 0
    elegir_inspeccion_barrera_monitorizacion         pob 479 barrido  2 | con linea  2 | sin linea  0 (de marquet nuevo 0) | linea sin vecino hoy 0
    pares del barrido 48 | con linea adjudicada 48 | sin linea 0, de ellos de los 17 de marquet 0 | lineas sin vecino hoy 0 | candidatos sin barrido 0
    lineas adjudicadas en total: 49 en 17 bloques

(`.v65aud/cruce_barrido.txt`; los `48` pares con sus tres seniales, en `.v65aud/pares48.txt`.)

**LECTURA, en tres partes:**

1. **Ningun vecino sin linea.** Los `48` pares que la aduana entera levanta hoy a los `20` **tienen los `48`
   su linea adjudicada** en la `ACTA 63`, y ninguna linea adjudicada de los `20` se queda sin su vecino. **Si la
   `65` escribio algun veredicto de lectura suya** (encargo, TAREA 3: *si levanta a un vecino que no tiene
   linea*), **no sale de ningun vecino que la aduana levante hoy**: lo busco en el turno normal.
2. **Marquet no levanta nada.** Ninguno de los `17` candidatos que la cosecha trajo despues de la `65` es
   vecino de ninguno de los `20` en el sentido candidato a vecino. **La aduana de la `65` no los tenia y no se
   ha perdido nada por eso.** El otro sentido (Marquet contra Grove) lo medira la insercion de Marquet cuando le
   toque; no es de esta vuelta.
3. **`48` contra `55`.** La bitacora gano `55` lineas (seccion `2`) y hoy levantan `48` pares. **La diferencia
   no la mido aqui**, porque medirla es abrir la bitacora. *Hipotesis, a comprobar y no cifra*: las `7` aristas
   que solo se cablean por lectura (seccion `5`), si `arista` escribe su registro en la bitacora. **Y si no son
   esas, son veredictos que la aduana levanto en su momento y hoy no**, que es justo lo que el turno normal
   tiene que mirar.

## 7. **MI LECTURA CIEGA DE LOS PARES** (`1.2`, `6.1`, y solo la vara `6.1`)

**LO PRIMERO, LO QUE YA HABIA VISTO.** Antes de leer ningun par abri, para preparar el cruce, ficheros donde
esta escrita la clase adjudicada de muchos de estos pares: las primeras `30` lineas de
`.v64ext/veredictos_listos.txt` (los bloques de `archivar`, `construir_grafico`, `construir_indicador_tendencia`
y `elegir_fabricar`, y la primera linea del de `elegir_indicador`), `.v64ext/aristas_lectura.txt` entero, la
salida de `.v64aud/normal/cruce_clases.txt` sin las lineas `COINCIDE`, `.v63ext/cmd_02_detectar.sh` y la salida
de mi propio `.v65aud/aristas.py`. **Un par cuya clase vi antes de leerlo no lo publico como lectura ciega.**
Esos son `31` de las `48` filas, y son todos pares **ya adjudicados** en la `ACTA 62` o la `ACTA 63`, que no
reabro (`D.47`).

**LOS OTROS `17`, que son `11` pares sin direccion, los lei con los pasos de los dos delante y el libro
abierto, sin haber visto su clase escrita junto a su nombre en ningun sitio** (y el limite de eso, debajo de la
tabla):

    $ python .v65aud/clases_48.py
    CIEGA  SANO   alta  clasificar_trabajo_proceso_montaje_prueba -> preferir_inspeccion_proceso_prueba_destructiva
    CIEGA  SANO   alta  construir_flujo_produccion_paso_limitante -> retirar_barreras_politicas_metodo
    CIEGA  SANO   alta  construir_flujo_produccion_paso_limitante -> preferir_inspeccion_proceso_prueba_destructiva
    CIEGA  SANO   alta  decidir_aceptar_rechazar_material_defectuoso -> dimensionar_plantilla_administrativa_pronostico
    CIEGA  SANO   alta  dimensionar_inventario_materia_prima_reposicion -> preferir_inspeccion_proceso_prueba_destructiva
    CIEGA  SANO   media dimensionar_plantilla_administrativa_pronostico -> elegir_cinco_indicadores_diarios_fabrica
    CIEGA  SANO   alta  dimensionar_plantilla_administrativa_pronostico -> emparejar_indicadores_efecto_contraefecto
    CIEGA  SANO   alta  dimensionar_plantilla_administrativa_pronostico -> simplificar_trabajo_reducir_numero_pasos
    CIEGA  SANO   alta  dimensionar_plantilla_administrativa_pronostico -> decidir_aceptar_rechazar_material_defectuoso
    CIEGA  SANO   media emparejar_indicadores_efecto_contraefecto -> elegir_cinco_indicadores_diarios_fabrica
    CIEGA  SANO   alta  emparejar_indicadores_efecto_contraefecto -> dimensionar_plantilla_administrativa_pronostico
    CIEGA  SANO   alta  preferir_inspeccion_proceso_prueba_destructiva -> clasificar_trabajo_proceso_montaje_prueba
    CIEGA  SANO   alta  preferir_inspeccion_proceso_prueba_destructiva -> rehacer_flujo_paso_limitante_capacidad
    CIEGA  SANO   alta  preferir_inspeccion_proceso_prueba_destructiva -> construir_flujo_produccion_paso_limitante
    CIEGA  SANO   alta  preferir_inspeccion_proceso_prueba_destructiva -> dimensionar_inventario_materia_prima_reposicion
    CIEGA  SANO   alta  rehacer_flujo_paso_limitante_capacidad -> preferir_inspeccion_proceso_prueba_destructiva
    CIEGA  SANO   alta  rehacer_flujo_paso_limitante_capacidad -> dimensionar_inventario_materia_prima_reposicion
    filas del barrido: 48 | con mi lectura ciega: 17 (SANO 17) | con la clase ya vista antes de leer: 31
    pares no ordenados en mi lectura: 11 | de ellos sin fila en el barrido: 0

**Las razones, una por par y con su linea del libro, estan en `.v65aud/mis_clases.tsv`**, escritas antes de
abrir nada que las juzgue. Las que sostienen algo mas que *comparten palabras*:

| par | mi clase | lo que la sostiene |
|---|---|---|
| `dimensionar_inventario` con `preferir_inspeccion` | **SANO, hermanos** | `cap_02` L69 abre con *What else could go wrong with our continuous egg-machine?*: el huevo que entra, despues de la temperatura que se sale de L67. Ninguno usa al otro |
| `clasificar_trabajo` con `preferir_inspeccion` | **SANO** | L67 no vuelve sobre los tres tipos de operacion de L39; la prueba del uno y la del otro solo comparten la palabra |
| `rehacer_flujo` con `preferir_inspeccion` | **SANO** | la similitud de texto mas alta de mis `17` filas (`0,460`, seccion `7`, `.v65aud/sim_ciegas.txt`) sale del huevo de tres minutos que se estropea en L51 y en L67, no de un paso comun |
| `emparejar_indicadores` con `elegir_cinco_indicadores` | **SANO, confianza media: DUDA MIA** | el paso `8` de los cinco (L27, *It is not enough to monitor the number of breakfasts each waiter delivers*) es la semilla de lo que L31 hace principio, pero **no lo procedimenta**: no nombra efecto ni contraefecto ni manda vigilar dos a la vez. *Nombrar no es procedimentar*, y aqui ni siquiera se nombra. **Si la `65` o la `63` lo leyeron CONTINUA, esa es la discrepancia que traigo** |
| `dimensionar_plantilla` con `elegir_cinco_indicadores` | **SANO, confianza media** | el paso `1` de la plantilla elige los indicadores de una unidad **administrativa** (L125), que es el procedimiento de `elegir_indicador_salida_trabajo_administrativo` (su madre por lectura, seccion `5`), no el de los cinco datos diarios de la fabrica |

**UN LIMITE DE LO CIEGO, QUE DECLARO, Y COMO LO CIERRO.** Antes de leer, lei entera la `ACTA 63`, y su
`63.3.c` dice que el discutible `D64.3` eran *tres pares con texto sobre `0,4`, SANO*, leidos SANO *en la
ciega (`APERTURA_CIEGA.md` `6.2`)*, **sin nombrarlos**. Tres de mis `17` filas pasan de `0,4`:

    $ python .v65aud/sim_ciegas.py | tail -1
    filas ciegas: 17 | con similitud de texto sobre 0,4: 3

(las `17` ordenadas, en `.v65aud/sim_ciegas.txt`: las tres son `rehacer_flujo` con `preferir_inspeccion` en los
dos sentidos y `preferir_inspeccion` contra `construir_flujo`.)

**DESPUES de escribir mis `11` pares** (`.v65aud/mis_clases.tsv`, guardado a las `23:47:50`) abri **mi propia
apertura sellada de la `64`** (`git show 5b866f1:docs/loop/APERTURA_CIEGA.md`, copiada en
`.v65aud/apertura_v64_propia.md`). **No es ninguno de los cuatro ficheros que `D.34.2` retira: es obra mia.** Su
`6.2` es la tabla de los pares de `cap_02` y del final de `cap_03`, **asi que las tres filas sobre `0,4` son, con
toda probabilidad, las de `D64.3`, y su clase SANO la sabia por la `ACTA 63` antes de leerlas.** **No las cuento
como ciegas:** mis filas ciegas de verdad son `14`, y las otras tres son una relectura con la clase sabida.

**Y EL CONTRASTE QUE ESA APERTURA ME DA, con instrumento:**

    $ python .v65aud/cruce_mi_v64.py | tail -1
    pares: 11 | misma clase que mi apertura de la 64: 11 | distinta: 0 | sin fila alli: 0

(fila a fila en `.v65aud/cruce_mi_v64.txt`.) **LECTURA:** dos lecturas mias hechas a ciegas con un dia de
distancia, la segunda sin mirar la primera, **dan la misma clase en los `11` pares**. No prueba que acierten:
**la `ACTA 63` me gano cinco discrepancias en esa misma apertura**, dos de ellas de pares, y por usar la vara
para una pregunta que no era la suya. **Ninguno de estos `11` era una de esas dos.**

**LECTURA:** **cero CONTINUA, cero REPITE y cero MUTUO en lo que lei**, `14` filas ciegas de verdad y tres con la
clase sabida, y **dos dudas** marcadas. Lo que comparo en el turno normal es **cada una de estas `17` filas contra
la linea que la `65` escribio en la bitacora para ese par**, con los pasos ya leidos y **solo despues** su razon.

## 8. **MI CLASIFICACION, CANDIDATO POR CANDIDATO**

La tabla es la salida de `.v65aud/tabla_20.py`, que **solo junta** las salidas ya guardadas de las secciones
`3`, `5`, `6` y `7`; la columna de la izquierda es la linea de `.v64ext/los22.txt`, **no la fila del orden de
insercion**, que esta en el reporte y no la he visto.

    $ python .v65aud/tabla_20.py | head -2
    | linea de los22 | candidato | cap | pieza | leida en | pasos | PUENTE | vecinos hoy | con linea | sin linea | filas mias ciegas | aristas vivas |
    |---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|

(El `head` va en el comando; la tabla entera, pegada debajo como tabla, es `.v65aud/tabla_20.txt`. La columna
*filas mias ciegas* cuenta las `17` de la seccion `7`, tres de ellas con la clase sabida.)

| linea de los22 | candidato | cap | pieza | leida en | pasos | PUENTE | vecinos hoy | con linea | sin linea | filas mias ciegas | aristas vivas |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | `construir_flujo_produccion_paso_limitante` | `cap_02` | P2 | `b63405c` | 10 | 0 | 3 | 3 | 0 | 2 | 1 |
| 2 | `clasificar_trabajo_proceso_montaje_prueba` | `cap_02` | P5 | `b63405c` | 7 | 0 | 1 | 1 | 0 | 1 | 0 |
| 3 | `rehacer_flujo_paso_limitante_capacidad` | `cap_02` | P6 | `b63405c` | 6 | 0 | 3 | 3 | 0 | 2 | 2 |
| 4 | `equilibrar_capacidad_personal_inventario_plazo` | `cap_02` | P7 | `b63405c` | 8 | 4 | 1 | 1 | 0 | 0 | 1 |
| 5 | `preferir_inspeccion_proceso_prueba_destructiva` | `cap_02` | P9 | `b63405c` | 6 | 0 | 4 | 4 | 0 | 4 | 0 |
| 6 | `dimensionar_inventario_materia_prima_reposicion` | `cap_02` | P10 | `b63405c` | 7 | 0 | 2 | 2 | 0 | 1 | 2 |
| 7 | `detectar_arreglar_fallo_etapa_menor_valor` | `cap_02` | P11 | `b63405c` | 6 | 0 | 1 | 1 | 0 | 0 | 1 |
| 8 | `elegir_cinco_indicadores_diarios_fabrica` | `cap_03` | P2 | `b63405c` | 10 | 0 | 0 | 0 | 0 | 0 | 0 |
| 9 | `emparejar_indicadores_efecto_contraefecto` | `cap_03` | P3 | `997054d` | 7 | 0 | 6 | 6 | 0 | 2 | 1 |
| 10 | `elegir_indicador_salida_trabajo_administrativo` | `cap_03` | P4 | `997054d` | 7 | 0 | 3 | 3 | 0 | 0 | 2 |
| 11 | `representar_actividad_caja_negra_ventanas` | `cap_03` | P7 | `b63405c` | 9 | 0 | 0 | 0 | 0 | 0 | 2 |
| 12 | `construir_indicador_linealidad_alerta_temprana` | `cap_03` | P9 | `b63405c` | 9 | 0 | 0 | 0 | 0 | 0 | 1 |
| 13 | `construir_indicador_tendencia_patron` | `cap_03` | P10 | `997054d` | 6 | 0 | 6 | 6 | 0 | 0 | 2 |
| 14 | `construir_grafico_escalonado_pronosticos` | `cap_03` | P11 | `997054d` | 8 | 1 | 3 | 3 | 0 | 0 | 1 |
| 15 | `archivar_indicadores_resolver_problemas` | `cap_03` | P12 | `997054d` | 4 | 0 | 4 | 4 | 0 | 0 | 0 |
| 16 | `elegir_fabricar_pedido_pronostico` | `cap_03` | P13 | `997054d` | 9 | 1 | 2 | 2 | 0 | 0 | 1 |
| 17 | `casar_flujo_fabricacion_flujo_ventas` | `cap_03` | P14 | `b63405c` | 12 | 0 | 0 | 0 | 0 | 0 | 2 |
| 18 | `dimensionar_plantilla_administrativa_pronostico` | `cap_03` | P15 | `b63405c` | 7 | 0 | 6 | 6 | 0 | 4 | 2 |
| 19 | `decidir_aceptar_rechazar_material_defectuoso` | `cap_03` | P17 | `b63405c` | 8 | 0 | 1 | 1 | 0 | 1 | 1 |
| 20 | `elegir_inspeccion_barrera_monitorizacion` | `cap_03` | P18 | `b63405c` | 12 | 0 | 2 | 2 | 0 | 0 | 0 |

**MI CLASE PARA LOS `20`: ENTRA, Y ENTRO COMO SE LEYO.** Los `20` estan en el grafo con los bytes de su lectura
entera (seccion `3`), los seis PUENTE que esa lectura les encontro entraron reescritos (seccion `4`), todas sus
aristas adjudicadas viven y ninguna sobra (seccion `5`), y **la aduana entera de hoy no les levanta ni un vecino
que no tenga su linea** (seccion `6`). **No traigo ninguna clase de fidelidad distinta de la adjudicada**, y de
los pares traigo `17` filas leidas (`14` ciegas de verdad, seccion `7`), todas SANO, con dos dudas.

**Y LAS DOS FILAS QUE NO ENTRABAN SIGUEN FUERA** (seccion `2`): `variar_frecuencia_inspeccion_nivel_calidad` y
`simplificar_trabajo_reducir_numero_pasos`, en la bandeja.

## 9. **LO QUE DEJO PARA MI TURNO NORMAL, ESCRITO ANTES DE VER EL REPORTE**

1. **`R5`** (seccion `0`): los dos instrumentos sobre el tramo de la `65` del reporte.
2. **La bitacora contra lo adjudicado**: las `55` lineas nuevas contra los `48` pares de mi barrido y las
   lineas de `.v64ext/veredictos_listos.txt`, **tal cual** (encargo, TAREA 3: *no se reescriben*); y que es lo
   que no cuadra entre `48` y `55` (seccion `6`, punto `3`).
3. **Mis `17` filas contra las suyas** (seccion `7`), empezando por mis dos dudas, **y sin contar como ciegas
   las tres que pasan de `0,4`** hasta haber mirado si eran las de `D64.3`.
4. **LA MUESTRA PINEADA DE LOS SANO (`7`), REGISTRADA AQUI Y SIN CORRER:** `.v65aud/muestra_sano.py`, poblacion
   las lineas SANO de la bitacora desde la `741`, tamano el mayor entre `3` y el `20` por ciento con techo de
   `20`, **semilla `65`**. **La dejo escrita ahora para que la eleccion no dependa de nada que vea despues.** No
   la corro en esta fase porque correrla es leer las clases de la bitacora.
5. **Los cerrojos** (`D.44`): el encargo mandaba al primer `insertar` romper y declarar
   `nodos.jsonl.679b2259.cerrojo`. **Hoy no queda ninguno**, ni ese ni los otros dos:

       $ ls procesos/ | wc -l
       0
       $ python .v64aud/normal/cerrojos.py
       cerrojo de dataset/nodos.jsonl en este arbol: nodos.jsonl.679b2259.cerrojo

   (La linea del instrumento es el **nombre** que tendria el cerrojo de este dataset, y debajo no lista ningun
   fichero.) **Quien quito cada uno no lo mido aqui**: el del dataset lo digo contra el reporte, y los otros dos
   no son de este arbol.
