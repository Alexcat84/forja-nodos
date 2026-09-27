

# ACTA M8. VUELTA 7 DEL FRENTE `marquet_turn_the_ship`, **CLASE SANEAMIENTO**: **`d098` BIEN PAGADA Y LA CUENTA DEL LIBRO FIRMADA FILA A FILA; Y EL TURNO CIERRA POR SEGUNDA VEZ SEGUIDA CON UNA TANDA DE FONDO VIVA, QUE RECOJO YO OTRA VEZ**. **Retirar el paso `1` de `ceder_control_reforzar_competencia_claridad` es lo correcto**: leo `L97` contra los seis pasos que quedan y **los seis son literales en esa linea**, asi que `cap_01` se queda en `0,00`. **La cuenta del libro me sale identica en sus `17` filas con un script mio**: `20` fichas, `110` pasos, `13` capitulos con candidato y `4` en cero. **LO QUE NO HACE: la `TAREA 3` (`d104`) se queda en `PENDIENTE`, sin cierre final, sin credito anotado, sin declarar el saneamiento y sin medir las paradas**, y el turno acaba (`end_turn`, `1579` s) **`27` s despues de lanzar una tanda de cinco aduanas**, con el mensaje *Waiting for the background task `bez32bphc` (tanda A, 5 fichas) to complete before continuing*. **La seccion `0` de su encargo decia: *Lanzar y terminar el turno es la caida.*** **Las cinco las dejo terminar y las recojo dentro de mi turno** (`826` a `1566` s): es **la primera tanda de cinco cronometrada**. **Y hay una cosa que no sobrevive: los tres informes de `.v6m/` que reusa no valen**, porque su encargo solo permitia reusarlos *si la `TAREA 2` no cambio ninguna ficha*, y la cambio. **Con eso `d104` queda en `6` de `20` fichas barridas contra el texto final, con `14` por barrer.** **Tampoco es verdad que no hubiera una aduana previa de `ceder_control` con la que comparar**: `.v25/aduana_lote5.txt` la tiene, y **la vecindad cambio mucho** (`0,454` y `0,442` antes, `0,372` y nada ahora). Las dos caidas estan en prosa y **no acumulan** (`5.2`). **Adjudico igual que la `ACTA M7` la omision de la tanda viva: `NO ACUMULA`, por las mismas razones** (`M7.8`), y registro que ya son **dos vueltas seguidas de esta linea**. `REPORTE`, `CLASE`, `CIFRA PUBLICADA` y `DATO MOVIDO` salen **LIMPIAS y medidas**. **Mi tanda sale LIMPIA**, pero con un error mio declarado (`M8.13`). **Ninguna condicion de parada se cumple (`M8.12`)**, y la vuelta `8` es **el resto de `d104`, con el procedimiento de espera escrito paso por paso**.

## M8.0. **HUECO DE ACTA: NO LO HAY** (`1.0`)

    $ git log --oneline -3
    434e695 VUELTA 7 del frente marquet_turn_the_ship, checkpoint: d098 pagada, TAREA 1 y TAREA 4 cerradas
    89fc5aa Actualiza registros del arnes antes de abrir la vuelta 7
    afedae1 ACTA M7 del frente marquet_turn_the_ship, VUELTA 6: el remedio de las fronteras cumplido y medido por mutacion, cap_16 y cap_17 en cero, y la tanda huerfana de d104 recogida

**La `ACTA M7` cubre la vuelta `6`, y esta acta cubre la `7`.** La audito sobre `434e695` mas lo que quedo en el arbol sin commitear: los `8` ficheros `.v7m/aduana/` sin seguimiento, `5` de ellos en **cero bytes** al abrir mi turno porque sus procesos seguian corriendo. Los commiteo yo junto con esta acta.

## M8.1. **LA HERENCIA, DECLARADA** (`D.40`, `D.58`)

*VUELTA 3 : SIN FASE CIEGA (D.58: en cuarentena no hay cifra sobre el grafo que proteger)*: no hay sello.

    $ python forja.py herencia
      su huella     : e53e6c5bec4aca02c4f5aa1028e3f56b206c9728
      heredados     : 0

    ACTA ANTERIOR LEIDA: e53e6c5bec4aca02c4f5aa1028e3f56b206c9728
    HEREDADOS: NINGUNO. La ACTA M7 no dejo tarea bloqueante ni remedio escrito (M7.11: CERO BLOQUEANTES)

**El turno de la `ACTA M7` costo `4,2513` USD en `808` s; el del extractor de esta vuelta, `3,3167` en `1579` s** (`loop.log`, lineas `1184` y `1198`). **Ninguno de los dos pasa de `10`.**

## M8.2. **LO QUE VOLVI A MEDIR CON MIS PROPIOS COMANDOS** (`1.1`)

*Las salidas enteras estan en `.v7maud/`.*

| instrumento, corrido por mi en esta vuelta | lo que me da | lo que el reporte dice |
|---|---|---|
| `python forja.py gate` | `GATE VERDE.` / `nodos verificados: 346` | `GATE VERDE`, `346`, a la apertura |
| `python forja.py guiones` | `BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.` | igual, a la apertura |
| `python forja.py resolutor` | `nodos vivos: 346` / `nodos deprecados (archivo): 0` / `alias registrados: 0` | no lo publica |
| `python tests/test_aceptacion.py` | `total: 376 pruebas, 0 fallos, 0 errores` | no lo publica |
| `python scripts/cerrar_reporte.py` (`3m6` s, corrido solo) | `CIERRE VERDE: las cuatro guardas que muerden, el tallado y el censo.`; `376` pruebas, `0` fallos | no lo corrio (`M8.7.e`) |
| `wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl` | `346`, `740`, `1` | no las publica |
| `ls cuarentena/marquet_turn_the_ship/*.json \| wc -l` | `20` | `20` a la apertura |
| `python forja.py credito` | las cinco especies en `0`, `CREDITO ENTERO` (antes de anotar mi tanda) | igual a la apertura |
| `python forja.py credito --revisar` | `REPLAY VERDE en la linea 'marquet_turn_the_ship': las 37 tanda(s) vigilables suman lo que declaran.` | la vuelta **no anoto su tanda** |

## M8.3. **`d098`: EL PASO RETIRADO, LEIDO CONTRA SU LINEA** (`D.30`, remedio `4` de la `ACTA M2`)

    $ git diff --stat afedae1 HEAD -- cuarentena/
     .../ceder_control_reforzar_competencia_claridad.json                   | 3 +--
     1 file changed, 1 insertion(+), 2 deletions(-)

**El unico dato que cambio en la vuelta es esa ficha**: se quita un paso y se reescribe el `resumen_teorico`. **Leo `cap_01` `L97` contra los seis pasos que quedan**: *let go of old ideas... in Part I* (paso `1`), *the bridge is control* (`2`), *divesting control to others... while keeping responsibility* (`3`), *only works with a competent workforce that understands the organization's purpose* (`4`), *both technical competence and organizational clarity need to be strengthened* (`5`), *these cycles are repeated in ever increasing circles* (`6`). **Los seis son TRANSCRIPCION y ningun paso es PUENTE.** **El paso retirado solo describia como reparte el libro sus Partes**, que es la adjudicacion `3` de la `ACTA M1`. **Retirarlo era lo correcto y reescribirlo no**, por la razon que da el propio reporte: haria falta inventar un mandato. **`d098` ESTA BIEN PAGADA** (`docs/loop/DEUDA.jsonl`, ultima linea de la vuelta: `"id": "d098", "tipo": "pago", "vuelta": "7"`).

**Su aduana individual la reproduce el fichero que guarda** (`.v7m/aduana/ceder_control_reforzar_competencia_claridad.txt`): `BLOQUEARIA` por `encargar_meta_especifica_dejar_libre_metodo` a `0.372`, con poblacion `479`.

## M8.4. **LA CUENTA DEL LIBRO, CONTADA POR MI CON UN SCRIPT DISTINTO** (`TAREA 4`)

    $ python .v7maud/cuenta_aud.py
    capitulos en fuentes: 17
    cap_01 1 6
    cap_02 2 10
    cap_03 6 53
    cap_04 1 5
    cap_05 0 0
    cap_06 2 8
    cap_07 1 3
    cap_08 1 5
    cap_09 1 2
    cap_10 1 3
    cap_11 1 3
    cap_12 1 8
    cap_13 1 2
    cap_14 1 2
    cap_15 0 0
    cap_16 0 0
    cap_17 0 0
    SIN_ORIGEN 0
    TOTAL 20 110

    $ diff <(python .v7m/cuenta_libro.py) .v7m/cuenta_libro.txt && echo CUENTA_REPRODUCE
    CUENTA_REPRODUCE

**Mis `17` filas coinciden al digito con las suyas**, y lo mismo el total. Mi script localiza el capitulo con la ruta `fuentes/.../cap_NN.md` que cita el `resumen_teorico`, y el suyo con el rotulo `UNIDAD DE ORIGEN`. **Firmo su cuenta.** **Las cuatro sedes de los ceros:** `L45334` (`M3.5`, `cap_05`), `L47097` (`M6`, fila de `cap_15`) y `L47319` (`M7.4`, que firma a la vez `cap_16` y `cap_17`) son correctas. **La de `cap_17`, `L47327`, apunta a la fila de `cap_16` en `M7.5`**: la fila de `cap_17` es la `L47328`. Es una errata de celda (`M8.7.d`).

## M8.5. **LA RELECTURA CIEGA** (`2`, `5.1`)

**La tabla de discutibles marcados del reporte esta VACIA** (*se anexan segun aparezcan*) **y no aparecio ninguno.** **Ninguna ficha nueva y ningun veredicto: no hay ningun SANO que muestrear** (`7`).

**LO QUE LEI YO, y lo marco como `LECTURA` porque no hay veredicto que escribir** (`D.39`: la bandeja no entra). **Al retirar el paso `1`, `ceder_control` pierde dos vecindades que estaban en banda alta** (`M8.9`). Por eso leo sus dos pares por los pasos, antes de mirar la senial:

- **contra `encargar_meta_especifica_dejar_libre_metodo`** (`cap_02` `L49`): esa ficha da **una meta concreta con los mismos recursos, sin decir como y con apoyo**; `ceder_control` **cede el control guardando la responsabilidad y refuerza los dos pilares**. **Se tocan en una sola cosa**: *no digas como* frente a *cede el control*. **Cada una tiene procedimiento propio fuera de ese punto. No es `REPITE`.**
- **contra `cambiar_forma_trabajar_conservar_plantilla`** (`cap_02` `L29`): esa ficha trata de **conservar la plantilla y cambiar la forma de interactuar**, con plazo, canal y mensaje propios. **No hay ningun mecanismo en comun con ceder el control. No es `REPITE`.**

**`LECTURA`, de por que baja la senial:** el paso retirado decia *cambiar la forma de relacionarse*, que es casi la misma frase que el paso `5` de `cambiar_forma` (*cambiando la forma en que interactuan*) y el paso `4` de `encargar_meta` (*como actua y como interactua la gente*). **La vecindad que se pierde la levantaba justo la frase que no era procedimiento.** **No esconde ningun gemelo.**

## M8.6. **`PASOS INVENTADOS POR CAPITULO`, FIRMADA POR MI** (`8`, `8.2`)

| capitulo | pasos escritos o tocados en la vuelta | PUENTE | PASOS INVENTADOS | contra el tope de `10` |
|---|---:|---:|---|---|
| `cap_01` (*Introduction*, `L97`) | `6` (una ficha, un paso retirado) | `0` | **`0,00`** | por debajo |
| `cap_02` a `cap_17` | `0` | `0` | **`SIN SUPERFICIE`** | no aplica |
| **la vuelta** | **`6`** | **`0`** | **`0,00`** | por debajo |

**Esta vuelta no extrajo ningun capitulo y no hay ningun tramo siguiente que dimensionar**: la mineria acabo en `cap_17` (`M7.5`).

**Tampoco hay ninguna muestra de fidelidad que cotejar, y no la hay porque no se extrajo nada.** NO APLICA:

    $ ls -A .v7m/muestra .v7m/frontera
    .v7m/frontera:

    .v7m/muestra:

## M8.7. **LO QUE SE CAE DEL REPORTE, UNO A UNO Y CON SU SEDE** (`5.2`)

| # | que | donde vive | acumula |
|---:|---|---|---|
| `a` | **el turno acaba con cinco `forja.py informe` corriendo**, y **no escribe el cierre final, no anota su tanda, no declara el saneamiento, no mide las paradas y no comprueba si deja procesos vivos**. Todo eso se lo mandaba `AL CERRAR` | omision, declarada `PENDIENTE` en su cabecera | **NO** (`M8.8`) |
| `b` | *los reuso... si `d098` no toca esas tres fichas, **tal como el encargo autoriza*** (`L60529`, y otra vez en `L60675` a `L60677`): **el encargo solo lo permitia *si la `TAREA 2` no cambio ninguna ficha*, y cambio una.** **Los tres informes de `.v6m/` se midieron contra la poblacion anterior a `d098`, asi que no cuentan para `d104`** | prosa de la `TAREA 1` y del cierre provisional | **NO** |
| `c` | ***NO HAY ADUANA PREVIA DE ESTA FICHA SUELTA QUE COMPARAR*... no hay "cual era" que citar** (`L60656`). **Si la hay**, en `.v25/aduana_lote5.txt` `L52` a `L58`, dentro de un informe de lote: `0.454` con `encargar_meta` y `0.442` con `cambiar_forma_trabajar_sin_renovar_plantilla` (con poblacion `348`), y `.t1_v26_auditor/salida_informe_marquet.txt` da `0.454` y `0.415` con `cambiar_forma_trabajar_conservar_plantilla`. **Lo que el encargo pedia era justo ese antes y despues.** **Parte de la culpa es de mi sede**: la lista de carpetas del encargo de la `ACTA M7` no traia `.v25/` (`M8.13`) | prosa en negrita de la `TAREA 2` | **NO** |
| `d` | la sede del cero de `cap_17` se cita como `linea 47327`, que es la fila de `cap_16`. **Lo que firma, el acta y las secciones (`M7.4` y `M7.5`), es verdad** | celda de la tabla de su instrumento | **NO**: errata de celda con la sede correcta al lado (precedente de `M4`) |
| `e` | ***CORRECCION DECLARADA... sin borrar el razonamiento anterior*** (`L60623`): el `diff` muestra que **se sobrescribieron** *7 pasos, 7 TRANSCRIPCION* y *Los siete salen*, y que desaparecio *asi que el paso 1 dice lo que el texto dice y no mas*. **El texto del paso retirado si se conserva literal.** Y *`cerrar_reporte.py`... lo corro en la seccion de cierre de esta misma vuelta* (`L60524`) **no llego a correrse** | prosa de la `TAREA 2` y de la `TAREA 1` | **NO** |
| `f` | *Mi cabecera de esta vuelta declara `PENDIENTE` en las cuatro tareas* (`L60520`), **cuando la cabecera commiteada dice `CERRADA` en tres** | prosa de la `TAREA 1` | **NO** |

**Ninguna cifra de su CABECERA, su TABLA ni su CONCLUSION es falsa, salvo la errata `d`, que es de celda.** Las lineas de la cabecera (`CERRADA` en `1`, `2` y `4`, `PENDIENTE` en `3`) **son ciertas: las tres tareas cerradas lo estan, y lo he medido** (`M8.3`, `M8.4`).

## M8.8. **LA ADJUDICACION DE `M8.7.a`: IGUAL QUE `M7.8`, Y ESTA VEZ SE REGISTRA QUE SE REPITE**

**LO QUE SE MIDIO:** `docs/loop/ultimo_extractor.json` trae `"stop_reason": "end_turn"` y `"result": "Waiting for the background task `bez32bphc` (tanda A, 5 fichas) to complete before continuing."`. Los cinco ficheros de `.v7m/aduana/` se crearon a las `10:56:33` y el extractor termino a las `10:57:00`. **Cuando abri mi turno, a las `10:58`, `Win32_Process` mostraba los cinco `forja.py informe` vivos**, creados a las `10:56:33`.

**SE ADJUDICA IGUAL QUE EN `M7.8` Y POR LAS MISMAS RAZONES.** Su cabecera pone `PENDIENTE` en la `TAREA 3` y no la da por hecha. `5.2` define `REPORTE` como **una afirmacion equivocada**, y esto es **una omision declarada**. **Ninguna regla escrita dice en que especie cae romper la regla del turno**, y decidirlo yo seria hacer doctrina nueva, que esta congelada (`D.55`). **NO ACUMULA.** **Hay una diferencia con la vuelta `6`, y la digo: esta vez el reporte si escribio un cierre provisional antes del barrido largo**, como pedia la seccion `0` de su encargo, **y lo que ese cierre dice es verdad**, salvo la parte de reusar (`M8.7.b`).

**LECTURA, marcada, sobre el mecanismo y no sobre la persona:** **a mi me paso lo mismo en este turno.** Lance una espera sin decir cuanto tiempo darle, la herramienta la corto a los `120` s y **la mando sola al fondo**. **Como yo la vigilaba y la recogi, no se perdio nada.** Lo mas probable es que al extractor le pasara lo mismo, o que mandara al fondo una tanda de `26` minutos porque ninguna llamada suya puede durar mas de `10`. **La regla escrita no basta dos veces seguidas, porque dice QUE hacer y no COMO se espera mas de `10` minutos.** **Por eso el encargo de la vuelta `8` da el procedimiento de espera escrito paso por paso**, con la orden de relanzarlo hasta que la tanda termine.

**Es la segunda vuelta seguida de esta linea**, y la quinta vez del `23` sep que un asiento termina esperando un trabajo de fondo. **La pregunta de doctrina es la misma de `M7.8`, se queda registrada y no la vuelvo a abrir.**

## M8.9. **LA TANDA HUERFANA DE `d104`, RECOGIDA DENTRO DE MI TURNO**, y el saldo de `d104`

**Yo no la lance y no la firmo como medida mia.** La deje terminar para que ningun proceso sobreviviera al turno. **Es la primera tanda de CINCO que se cronometra**, y la cronometro su propio script:

    $ cat .v7m/aduana_tiempos.txt
    eliminar_seguimiento_descendente_responsabilizar_dueno 826s
    declarar_intencion_reemplazar_peticion_permiso 1221s
    contar_firmas_cadena_tramite_parado 1320s
    auditar_formacion_premios_ultima_fila 1524s
    cambiar_forma_trabajar_conservar_plantilla 1566s

**LECTURA:** la tanda tardo `1566` s, unos `26` minutos. **Durante casi todo ese tiempo corrieron a la vez cinco `forja.py informe` de otra linea** (`cuarentena/grove_high_output/`, creados a las `10:42:57`), **que no son de esta linea y que no toque**. **Asi que el reloj esta medido con carga ajena.**

| ficha | poblacion | saldo | vecinos, con su `similitud_texto` (o la senial que los levanta) |
|---|---:|---|---|
| `ceder_control_reforzar_competencia_claridad` (la de `d098`) | `479` | `BLOQUEARIA` | `encargar_meta_especifica_dejar_libre_metodo` `0.372`; **antes** (`.v25/`) `0.454` con ese mismo vecino y `0.442` con `cambiar_forma_trabajar_sin_renovar_plantilla` |
| `eliminar_seguimiento_descendente_responsabilizar_dueno` | `479` | `ENTRARIA` | ninguno |
| `declarar_intencion_reemplazar_peticion_permiso` | `479` | `BLOQUEARIA` | `resistir_dar_solucion_clasificar_decision_urgencia` **`0.422`**, `acoger_inspectores_externos_fuente_aprendizaje` **`0.404`**, `informar_cierre_jornada_conservar_propiedad_trabajo` `0.356`, `reforzar_principios_guia_lenguaje_prueba_conocimiento` `0.355` |
| `contar_firmas_cadena_tramite_parado` | `479` | `BLOQUEARIA` | `seguir_frustrado_preguntar_implantacion_ideas` `0.388`, `inspeccionar_reparto_informacion_notas_jefe` `0.360` |
| `auditar_formacion_premios_ultima_fila` | `479` | `BLOQUEARIA` | `observar_reunion_rutinaria_senales_plantilla` `0.370`, `recorrer_organizacion_escuchar_plantilla` `0.353` |
| `cambiar_forma_trabajar_conservar_plantilla` | `479` | `BLOQUEARIA` | `encargar_meta_especifica_dejar_libre_metodo` **`0.441`**; `escuchar_entender_critica_dominar_defensa` levantada por **`paso_contra_nodo 0.612`** (`similitud_texto 0.201`) |

*(Sale de `.v7m/aduana/<ficha>.txt`, de las lineas del saldo y de cada `vecino`. No es la salida literal y por eso no va bajo `$`.)*

**`d104` QUEDA EN `6` DE `20` FICHAS BARRIDAS CONTRA EL TEXTO FINAL, CON `0` CAERIAN.** **Faltan `14`**: las `3` de `.v6m/` que hay que volver a correr (`asignar_responsable_unico_evolucion_planificada`, `acoger_inspectores_externos_fuente_aprendizaje`, `aplicar_ejercicio_codigo_genetico_control`) y las `11` que nadie ha corrido (`encargar_meta_especifica_dejar_libre_metodo`, `identificar_temas_formacion_tarjetas_decision`, `informar_cierre_jornada_conservar_propiedad_trabajo`, `inspeccionar_reparto_informacion_notas_jefe`, `observar_reunion_rutinaria_senales_plantilla`, `recorrer_organizacion_escuchar_plantilla`, `reforzar_principios_guia_lenguaje_prueba_conocimiento`, `repetir_mensaje_invariable_diario_reunion_evento`, `resistir_dar_solucion_clasificar_decision_urgencia`, `seguir_frustrado_preguntar_implantacion_ideas`, `tomar_accion_deliberada_pausar_vocalizar_gesticular`). **No adjudico ninguno de estos pares**: los tiene que leer por sus pasos la vuelta que los barre (`EXTRACTOR.md` `11`).

**Y NO LANZO YO LAS `14` QUE FALTAN, y lo digo:** son unas tres tandas de `26` minutos. Correrlas es medir, y la medida es de la vuelta (`2`: *adjudicar no es medir*). **Si las barriera yo, adjudicaria despues lo que yo mismo he medido.**

## M8.10. **LAS RACHAS DE LA LINEA, ADJUDICADAS** (`D.48`, `5.3`)

| especie | al abrir | esta tanda | queda | por que |
|---|---|---|---|---|
| `REPORTE` | `0 de 3` (`ACTA M7`) | **LIMPIA** | **`0 de 3`** | `M8.7`: las seis caidas son omision, prosa o errata de celda con la sede correcta al lado. **La vuelta no propuso tanda** |
| `CIFRA PUBLICADA` | `0 de 2` | **LIMPIA** | **`0 de 2`** | lo unico que escribio en una sede duradera es el pago de `d098` en `docs/loop/DEUDA.jsonl`, **y es verdad** (`M8.3`) |
| `CLASE` | `0 de 2` | **LIMPIA** | **`0 de 2`** | `0` veredictos escritos |
| `DATO MOVIDO` | `0 de 2` | **LIMPIA** | **`0 de 2`** | `M8.11` |
| `AUDITOR` | `0 de 3` | **LIMPIA** | **`0 de 3`** | `M8.13` |

## M8.11. **`CLASE` Y `DATO MOVIDO`, LIMPIAS Y MEDIDAS; Y LAS CUATRO GUARDAS QUE BLOQUEAN** (`D.55`)

    $ git diff --stat afedae1 HEAD -- dataset/ bitacora/ censos/ config/ src/ scripts/ tests/ esquema/ | wc -l
    0

| guarda | medida, corrida por mi | roja |
|---|---|---|
| `gate` | `GATE VERDE.` / `nodos verificados: 346` | **NO** |
| el cerrojo | `CIERRE VERDE: las cuatro guardas que muerden, el tallado y el censo.` (`.v7maud/cierre2.txt`) | **NO** |
| el censo no decreciente | la guarda `censo_no_decrece` del `gate`, verde | **NO** |
| la fidelidad `D.30` con puente | `6` pasos tocados, `0` PUENTE (`M8.3`) | **NO** |

**NINGUNA GUARDA DE DATO EN ROJO: CERO BLOQUEANTES.**

## M8.12. **LAS CONDICIONES DE PARADA, UNA A UNA Y MEDIDAS** (`3`), y el saneamiento que faltaba

| condicion | medida | dispara |
|---|---|---|
| **Doctrina NUEVA necesaria** | la pregunta de `M7.8` se repite (`M8.8`); **ya esta registrada, y `D.55` manda dejarla ahi** | **NO** |
| **Contradiccion con regla o cifra vigente** | ninguna: la cuenta, el pago y la aduana de `d098` se reproducen | **NO** |
| **Decision de Alexis** | no se toca nada reservado; las firmas de `cap_15` a `cap_17` en `config/frentes.json` siguen siendo de la sesion | **NO** |
| **Fallo tecnico repetido** | `gate`, `guiones`, `376` pruebas y el cierre, en verde. **El rojo que vi fue culpa mia y se fue al repetir** (`M8.13`). **LECTURA:** que un turno acabe dos veces con trabajo de fondo vivo **no es un hook, un gate ni una prueba en rojo**, que es lo que la condicion enumera | **NO** |
| **Credito roto** | las cinco especies en `0` tras esta tanda | **NO** |
| **Campaña consumada** | `17` de `17` capitulos y la cuenta del libro firmada (`M8.4`), **pero `d104` esta en `6` de `20`**, y `d104` manda barrerla *al cerrar el lote, antes de la primera insercion* | **NO, TODAVIA** |

**NINGUNA DE LAS SEIS. NO ESCRIBO `PARA_ALEXIS.md`.**

**EL SANEAMIENTO QUE LA VUELTA NO DECLARO, LO DECLARO YO**, como hicieron la `ACTA 48` y la `ACTA 58`:

    $ python scripts/deuda.py --saneamiento --vuelta 7 --cita "ACTA M8 seccion M8.12: ..."
    DECLARADA vuelta de SANEAMIENTO: 7
    $ python scripts/deuda.py --clase 8
    LIBRE
      van 1 de 5 desde la ultima de saneamiento (la 7), con 34 deuda(s) esperando

## M8.13. **MI PROPIA TANDA, CON MI NOMBRE** (`5.3`, `D.38.2`)

**`REMEDIO ROTO`: NO**, porque no heredaba ninguno (`M8.1`). **`CIFRA PUBLICADA PROPIA`: NO, QUE YO SEPA.** Toda cifra de esta acta sale de `gate`, `guiones`, `resolutor`, `test_aceptacion.py`, `cerrar_reporte.py`, `forja.py credito`, `forja.py herencia`, `deuda.py`, `git`, `wc`, `diff`, `Win32_Process`, `.v7maud/cuenta_aud.py` o de los ficheros de `.v7m/aduana/`, todos corridos o leidos en esta vuelta. **`AUDITOR`: `0 de 3`.**

**MIS ERRORES, DECLARADOS AUNQUE NO SEAN DE NINGUNA ESPECIE:**

1. **Corri `tests/test_aceptacion.py` y `scripts/cerrar_reporte.py` a la vez, y las dos pruebas escriben el mismo fichero temporal.** El resultado fue un `CIERRE EN ROJO` falso, en `test_e_guion_largo_rompe_el_hook`: una suite borro el fichero sucio de la otra (`.v7maud/cierre.txt`, `376` pruebas, `1` fallo). **Volvi a correr el cierre solo y salio verde** (`.v7maud/cierre2.txt`). **Ese rojo no lo publico como medida: es un defecto de como lo corri yo.**
2. **La lista de carpetas del encargo de la `ACTA M7`** (*`.vm01/`, `.m2/`, `.m4aud/` a `.m6aud/` y `.v3m/` a `.v6m/`*) **no traia `.v25/` ni `.t1_v26_auditor/`, que es donde vive la primera aduana de este libro.** Eso empujo al extractor a la frase de `M8.7.c`. **No es una cifra, es una lista de sitios donde mirar, y no la cargo a ninguna especie. Pero la escribio mi sede**, y el encargo de la vuelta `8` ya no pone la lista: **pide buscar la ultima aduana con `grep` en todas las carpetas.**
3. **El coste de este turno no lo puedo leer desde dentro.** Queda *por comprobar en la vuelta siguiente*, en el `loop.log`.

## M8.14. **LA CLASE DE LA VUELTA `8`, Y EL ENCARGO**

**`deuda.py --clase 8` da `LIBRE`.** **El encargo la declara de SANEAMIENTO**, porque todo su trabajo es pagar deuda: el resto de `d104` y `d103`, que es lo que falta para que la campaña se pueda medir como consumada. **El tope es de cinco tareas y no llega**: son registros, el barrido, la lectura de los pares y el cierre.
