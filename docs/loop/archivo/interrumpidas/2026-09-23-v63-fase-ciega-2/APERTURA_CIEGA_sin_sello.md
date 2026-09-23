# APERTURA CIEGA, VUELTA 63 de la linea serial (`extraccion-mundo-11`)

*Auditor `claude-opus-5-5`, 23 sep 2026. Escrita sin `REPORTE.md`, sin `ultimo_extractor.json`,
sin `ultimo_auditor.json` y sin `CREDITO_serial.jsonl`, que el arnes retiro (linea de `loop.log`
de las `06:32:32`). No he recuperado ninguno de git. Lo que si he abierto: `AUDITOR_FORJA.md`
entero, `PROMPT_SIGUIENTE.md` (el encargo de la `63`, escrito por la sesion de chat), el
tablero, `DEUDA.jsonl` (`d005`), los `22` candidatos de `cap_02` y `cap_03` en la bandeja, y
`fuentes/grove_high_output/cap_02.md` y `cap_03.md` enteros. Toda mi evidencia esta en
`.v63ciega/`.*

**Clase de esta vuelta: INSERCION** (encargo, cabecera). Regimen completo: hay fase ciega.

---

## 0. LA HERENCIA (D.40)

ACTA ANTERIOR LEIDA: 388afd4c343a24d59e548bba512e4fd3c2fd428e

HEREDADO 1: NO APLICA en esta fase: `R5` es del extractor y se comprueba contra los bloques `$` de su `REPORTE.md`, que el arnes me ha retirado; se mide en mi turno normal con `.v62aud2/pegado62_final.py`. Y lo cumplo en lo mio: cada bloque `$` de esta apertura trae lo que el comando imprimio y nada mas.

    $ ls docs/loop/REPORTE.md .v62aud2/pegado62_final.py
    ls: cannot access 'docs/loop/REPORTE.md': No such file or directory
    .v62aud2/pegado62_final.py

HEREDADO 2: NO APLICA en esta fase: `R6` rige los encargos que escribe esta linea. El de la `63` no lo escribio un auditor sino la sesion de chat, y el de la `64` lo escribo yo en el turno normal, donde se comprueba. Y lo cumplo en lo mio: el criterio con el que elijo lo que leo aqui (seccion 1) lleva su alcance y su instrumento al lado.

    $ sed -n 3,4p docs/loop/PROMPT_SIGUIENTE.md
    *Linea **serial** (`extraccion-mundo-11`). **Escrito por la sesion de chat del 22 sep 2026**,
    no por un auditor, al aplicar la decision del fundador `DOS SEMANAS` (punto `4`), archivada en

HEREDADO 3: CUMPLIDO. Toda clasificacion de par de esta apertura (seccion 4) se adjudica con la vara `6.1` y solo con `6.1`; ninguna cita `EXTRACTOR.md` `9.1`.

**UN HALLAZGO DEL ARNES, que no es mio de arreglar y registro con su salida.** Con
`CREDITO_serial.jsonl` retirado, el instrumento de la herencia no ve ya la linea serial y
comprueba **cero** heredados donde el prompt me entrego **tres**:

    $ python forja.py herencia 2>&1 | head -7 | tail -3
      acta anterior : (ninguna de esta linea)
      su huella     : 388afd4c343a24d59e548bba512e4fd3c2fd428e
      heredados     : 0

LECTURA: si el sello corre `herencia --comprobar` con el registro retirado, **mide contra cero y
aprueba cualquier apertura**, la mia incluida. Esta apertura declara los tres igual. Lo llevo a
mi acta como especie ARNES; no toco `src/` (`D.45`).

---

## 1. QUE LEO, CON SU ALCANCE Y SU INSTRUMENTO (`R6` aplicado a mi)

**Alcance:** los candidatos de `cuarentena/grove_high_output/` cuya `UNIDAD DE ORIGEN` declarada
en su `resumen_teorico` es `cap_02.md` o `cap_03.md`. Es el criterio del encargo (*`cap_02`
entero y los `9` de `cap_03` que entran*), y leo los `15` de `cap_03` y no solo `9` porque cuales
son los `9` lo decide la aduana, no yo.

    $ python .v63ciega/unidades.py > .v63ciega/unidades2.txt; cmp .v63ciega/unidades.txt .v63ciega/unidades2.txt && echo IDENTICO
    IDENTICO
    $ grep -c . .v63ciega/unidades.txt
    22
    $ grep -c '^cap_02' .v63ciega/unidades.txt
    7
    $ grep -c '^cap_03' .v63ciega/unidades.txt
    15
    $ awk '{split($3,a,"="); s[$1]+=a[2]; n[$1]++} END{for(c in s) print c, n[c]" candidatos", s[c]" pasos"}' .v63ciega/unidades.txt | sort
    cap_02 7 candidatos 50 pasos
    cap_03 15 candidatos 121 pasos

**Censo al abrir**, antes de que nada entre:

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1087 total
    $ ls cuarentena/grove_high_output/*.json | wc -l
    91
    $ ls cuarentena/_insertados/grove_high_output/ | wc -l
    1

    $ python .v63ciega/cruza.py
    de los 22, ya en el grafo: 0

LECTURA: el grafo y la bandeja estan donde el encargo dice que estaban al abrir la `63`, y
ninguno de los `22` vive ya en el grafo. Es decir: **la insercion que el arnes encontro en vuelo no dejo nada escrito**, y
lo que leo es la tanda entera, sin nada dentro todavia.

---

## 2. FIDELIDAD `D.30`: TODOS LOS PASOS, CONTRA SU LINEA

**Leidos los `171` pasos (`50` + `121`, cifra del `awk` de arriba), uno por uno, contra
`sed`/`cat -n` de la fuente.** Mi vara es la de `D.30`: TRANSCRIPCION si el libro dice ese
paso en esa linea; PUENTE si el paso pone algo que el libro no dice. Anado una clase de lectura,
**DUDOSO**, para los pasos donde el libro AFIRMA algo y el paso lo convierte en un acto del
lector: es la especie que el propio candidato `construir_flujo_produccion_paso_limitante`
declara haber corregido en su paso `6` (*convertir una afirmacion del libro en una comprobacion
del lector es escribir un paso que el libro no dice*), y la aplico con esa misma vara a sus
vecinos de capitulo.

### 2.1. `cap_02` (Grove, Cap. 1, *The Basics of Production*)

| candidato | pasos | lectura | lineas |
|---|---:|---|---|
| `construir_flujo_produccion_paso_limitante` | 10 | 10 TRANSCRIPCION | L19, L21, L23, L25, L27 |
| `clasificar_trabajo_proceso_montaje_prueba` | 7 | 7 TRANSCRIPCION | L39, L41, L45 |
| `detectar_arreglar_fallo_etapa_menor_valor` | 6 | 5 TRANSCRIPCION, **1 DUDOSO (paso 2)** | L73, L75 |
| `dimensionar_inventario_materia_prima_reposicion` | 7 | 7 TRANSCRIPCION | L69 |
| `equilibrar_capacidad_personal_inventario_plazo` | 8 | 8 TRANSCRIPCION | L57, L59, L61 |
| `preferir_inspeccion_proceso_prueba_destructiva` | 6 | 6 TRANSCRIPCION | L67 |
| `rehacer_flujo_paso_limitante_capacidad` | 6 | 4 TRANSCRIPCION, **1 PUENTE (paso 6), 1 DUDOSO (paso 1)** | L51, L53 |

**Las piezas que no son TRANSCRIPCION limpia, con la linea que lo sostiene:**

- **`rehacer_flujo_paso_limitante_capacidad` paso 6, PUENTE de la especie del acto.** El paso
  dice *Y no cambies de componente el que manda la calidad*. **L51** dice: *The egg still
  determines the overall quality of the breakfast, but your time offsets must be altered.* El
  libro **afirma** que el huevo sigue mandando la calidad; **no encarga** nada sobre no cambiarlo.
  Es la misma figura que el paso `6` de `construir_flujo` ya corrigio, en el candidato que es su
  hijo. Remedio posible sin quitar contenido: reescribirlo sin imperativo (*cuenta con que el
  huevo sigue determinando la calidad general aunque el paso limitante sea ya el tostador*).
- **`rehacer_flujo_paso_limitante_capacidad` paso 1, DUDOSO.** *Comprueba si tu flujo esta
  dibujado suponiendo capacidad infinita.* **L51**: *In a schematic flow chart, our breakfast
  operation assumed infinite capacity... But no such ideal world exists.* El libro describe su
  propio modelo; la comprobacion es del lector. Lo dejo en DUDOSO y no en PUENTE porque la
  consecuencia imperativa del libro (*you have to redo your flow*) presupone haberlo visto.
- **`detectar_arreglar_fallo_etapa_menor_valor` paso 2, DUDOSO.** *Cuenta dentro de ese valor
  el valor percibido que el cliente asocia al establecimiento...* **L73**: *The last carries the
  perceived value the customer associates with the establishment...* Afirmacion del libro vuelta
  instruccion; no anade una comprobacion nueva, solo carga la escalera de valor del paso 1.
- **LECTURA, no clase:** `construir_flujo_produccion_paso_limitante` paso 10 abre con *cuando el
  paso que manda no sea el mas largo*, condicion que **L27** no pone (*we construct our production
  flow by starting with the longest (or most difficult, or most sensitive, or most expensive)
  step*). El acto es del libro y por eso lo cuento TRANSCRIPCION; la condicion anadida ademas
  choca con su propio contenido (empieza *por el mas largo*). Reparo de redaccion.

### 2.2. `cap_03` (Grove, Cap. 2, *Managing the Breakfast Factory*)

| candidato | pasos | lectura | lineas |
|---|---:|---|---|
| `archivar_indicadores_resolver_problemas` | 4 | 4 TRANSCRIPCION | L99 |
| `casar_flujo_fabricacion_flujo_ventas` | 12 | 12 TRANSCRIPCION | L111 a L121 |
| `construir_grafico_escalonado_pronosticos` | 8 | 7 TRANSCRIPCION, **1 DUDOSO (paso 3)** | L91, L93, L95 |
| `construir_indicador_linealidad_alerta_temprana` | 9 | 9 TRANSCRIPCION | L83, L87 |
| `construir_indicador_tendencia_patron` | 6 | 6 TRANSCRIPCION | L89 |
| `decidir_aceptar_rechazar_material_defectuoso` | 8 | 8 TRANSCRIPCION | L135, L137 |
| `dimensionar_plantilla_administrativa_pronostico` | 7 | 7 TRANSCRIPCION | L123, L125 |
| `elegir_cinco_indicadores_diarios_fabrica` | 10 | 10 TRANSCRIPCION | L15 a L29 |
| `elegir_fabricar_pedido_pronostico` | 9 | 9 TRANSCRIPCION | L103 a L109 |
| `elegir_indicador_salida_trabajo_administrativo` | 7 | 7 TRANSCRIPCION | L35, L37, L39 a L67 |
| `elegir_inspeccion_barrera_monitorizacion` | 12 | 12 TRANSCRIPCION | L139, L141 |
| `emparejar_indicadores_efecto_contraefecto` | 7 | 7 TRANSCRIPCION | L31, L33 |
| `representar_actividad_caja_negra_ventanas` | 9 | 9 TRANSCRIPCION | L73, L77 |
| `simplificar_trabajo_reducir_numero_pasos` | 7 | 7 TRANSCRIPCION | L169, L171 |
| `variar_frecuencia_inspeccion_nivel_calidad` | 6 | 6 TRANSCRIPCION | L143 |

**Las piezas que no son TRANSCRIPCION limpia:**

- **`construir_grafico_escalonado_pronosticos` paso 3, DUDOSO de la especie figura.** *Marca con
  un asterisco el numero real de cada mes.* **L95** es la leyenda de una figura: *(\* means the
  actual number for that month)*. El libro no encarga marcar nada; describe la convencion de su
  grafico. **Y el propio lote se contradice aqui**: `construir_flujo_produccion_paso_limitante`
  declara que *NO escribo quien dibuja el flujo... porque el libro lo ensena en una figura y no
  encarga dibujarla*. Una misma mano no puede tratar la figura como no imperativa en un nodo y
  como imperativa en otro.
- **LECTURA, no clase:** `variar_frecuencia_inspeccion_nivel_calidad` paso 6 (*cuenta con que este
  metodo casi no se usa... somos animales de costumbres*) transcribe **L143** fielmente pero no es
  un acto: es comentario del autor. No lo cuento PUENTE (el libro lo dice); lo registro como paso
  sin accion. Lo mismo, mas leve, el paso 9 de `elegir_cinco_indicadores_diarios_fabrica`: **L27**
  dice *Perhaps you should set up a customer complaint log*, y el paso lo pone firme.

### 2.3. `PASOS INVENTADOS POR CAPITULO`, mi lectura ciega

| capitulo | pasos leidos | PUENTE firme | DUDOSO | inventados, PUENTE solo | contando DUDOSO |
|---|---:|---:|---:|---:|---:|
| `cap_02` | 50 | 1 | 2 | **1 de 50, 2 %** | 3 de 50, 6 % |
| `cap_03` | 121 | 0 | 1 | **0 de 121, 0 %** | 1 de 121, 0,8 % |

LECTURA: los dos capitulos quedan por debajo del `10` por ciento de `8.1` en cualquiera de las
dos columnas. **Lo que si importa en una vuelta de insercion es que el PUENTE de `rehacer_flujo`
paso `6` no entre sin corregir** (encargo `2.a.1`): si el extractor lo leyo como TRANSCRIPCION,
es la comparacion que traigo a mi turno normal.

---

## 3. LA ADUANA EN SECO, CORRIDA POR MI EN ESTA FASE

(se rellena con la salida de `.v63ciega/informe_*.txt`)

---

## 4. LOS PARES, ADJUDICADOS CON `6.1` Y SOLO `6.1`

(se rellena tras la aduana)
