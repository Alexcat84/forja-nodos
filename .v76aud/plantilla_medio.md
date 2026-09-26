**LECTURA:**

1. **Las `22` dan `54` filas de vecino en `34` pares sin orden**, `24` entre dos de la tanda y `10` con uno de fuera, todos del
   grafo. **Coincide con los *54 pares* del asunto de `a0d42852`**, que ahi llama *pares* a mis filas dirigidas, como en la `73`; y lo
   digo como coincidencia.
2. **Dos fichas no levantan a nadie**: `aplicar_ocho_reglas_juego_personas` (tampoco la levanta nadie) y
   `fingir_prototipo_cinco_mil_replicas` (solo la levanta la contratacion). **Por eso las cuatro partes de la serie de las seis reglas
   quedan sin par**, y su arista es por lectura (seccion `6`).
3. **Los de fuera son todos del grafo**: de Grove, `responder_primer_aviso_renuncia_subordinado` (levantada por cuatro de las `22`),
   `entregar_evaluacion_desempeno_tres_claves`, `pedir_critica_anonima_curso_entrenamiento_dictado` y
   `planificar_tres_pasos_demanda_estado_brecha`; de Scott, `recorrer_trece_elementos_proceso_evaluacion_formal` y
   `descubrir_motivacion_sentido_persona`. **Ninguno de la bandeja de Marquet.** El mas cercano por lectura es
   `planificar_tres_pasos_demanda_estado_brecha` con `dictar_ritmo_crecimiento_preguntas_escritas` (seccion `5`).
4. **`D.36`, lo que un solo lado levanta dentro de la tanda**: va a la seccion `7`, y no obliga.

## 5. **MI LECTURA CIEGA DE LOS PARES** (`1.2`, `6.1`, y solo la vara `6.1`)

**Leidos con los pasos de los dos delante**, todos con `pasos_ciego.py` (`R6`): `.v76aud/pasos_22.txt` para las `22` y
`.v76aud/pasos_fuera.txt` para los seis de fuera. **Una fila por par** en `.v76aud/mis_clases.tsv`, con su razon. **De donde sale cada
fila:** los `25` pares posibles dentro de un mismo capitulo los escribi **todos antes de que el barrido terminara** (con `4` de `22`
recogidas), en `.v76aud/clases_intra.txt`; los de entre capitulos y los de fuera, al recogerlo, en `.v76aud/clases_fuera.txt`.
**Cuando escribi cada fichero, contra cuando cerro cada ficha del barrido** (las seis primeras):

@@RUN:0::ls -l --time-style=full-iso .v76aud/clases_intra.txt .v76aud/aristas_lectura.tsv .v76aud/clases_fuera.txt | awk '{print $6, substr($7,1,8), $9}'; ls -l --time-style=full-iso .v76aud/vecinos_*.json | awk '{print substr($7,1,8)}' | sort | head -6@@

`armar_clases.py` los junta, y el cruce comprueba que cada par del barrido tiene su fila y cada fila su par:

@@RUN:0::python .v76aud/armar_clases.py@@
@@RUN:0::python .v76aud/cruce_clases.py@@

**El par de fuera mas cercano**, con los pasos de los dos delante:

@@RUN:0::python .v67aud/normal/pasos_ciego.py dictar_ritmo_crecimiento_preguntas_escritas planificar_tres_pasos_demanda_estado_brecha@@

**LECTURA, los cuatro `CONTINUA`**, y en los cuatro el hijo trae procedimiento propio y ningun paso del otro, asi que ninguno es
`REPITE`:

- `aplicar_seis_pasos_sistema_venta` madre de `medir_sistema_venta_trece_indicadores_benchmark`: la condicion del hijo es el sistema
  de venta operando, y L303 y L307 encadenan con palabras el Information System al Soft System *in our example*. **El mas firme.**
- `cambiar_saludo_cliente_dos_ramas` madre de `cuantificar_impacto_innovacion_6_pasos`: los pasos `2` y `3` del hijo cuentan antes y
  despues de *cambiar las palabras* del saludo, que es lo que L95 cuantifica.
- `construir_estrategia_gente_cuatro_componentes` madre de `aplicar_cinco_pasos_proceso_contratacion`: los pasos `10` y `11` del hijo
  entregan y repasan el Manual, el Objetivo Estrategico, la Organizational Strategy y el Position Contract que la madre compone (L119
  y L269), y L245 hace de la contratacion el primer medio de esa estrategia.
- `recorrer_siete_pasos_programa_desarrollo_negocio` madre de `construir_estrategia_gente_cuatro_componentes`: el hijo es el paso `5`
  que la madre nombra (su paso `8`, L53), y es la parte de `d111` (seccion `6`).

**MIS DUDAS, escritas antes de saber, y si alguna me cae, cae dentro de lo que marco aqui:**

- **Las tres ultimas `CONTINUA` pueden leerse `SANO`**: el saludo es el ejemplo del libro y la cuantificacion vale para cualquier
  innovacion; la estrategia de gente solo **nombra** en una linea lo que la contratacion repasa; y `recorrer` con la estrategia de
  gente es la pregunta de `d111`.
- **Dos `SANO` de dentro de un capitulo que el barrido no levanta pueden leerse `CONTINUA`**: `interrogar_negocio_cinco_preguntas`
  con madre `fingir_prototipo_cinco_mil_replicas` (su condicion es cerrar el trabajo del prototipo), y `aplicar_ocho_reglas_juego_personas`
  con madre `construir_estrategia_gente_cuatro_componentes` (su condicion nombra la People Strategy entre parentesis). **No los
  levanta el barrido, asi que no llevan linea**; si alguno fuese madre e hijo, seria arista por lectura, y **mi lectura no la
  sostiene**.
- **`responder_4_preguntas_estandares_objetivo_estrategico` con `responder_8_preguntas_construir_primary_aim`**, `SANO`: cap_15 L21
  encadena los dos capitulos, pero ningun paso del hijo usa las respuestas del Primary Aim.

**Los `30` `SANO`** comparten la forma pregunta, la palabra sistema, plan o crecimiento, o la imagen del negocio mirado desde fuera,
y ningun paso. **El mas cercano es `dictar_ritmo_crecimiento_preguntas_escritas` con `planificar_tres_pasos_demanda_estado_brecha`**
de Grove: los dos planifican, pero Grove compara demanda y estado presente y los concilia, y Gerber contesta sus preguntas de donde,
cuando, cuanto capital, gente, tecnologia y espacio, con contingencias y por escrito. **Hay procedimiento fuera del solape en los dos
lados** (`6.1`, sin bascula): dos doctrinas legitimas, no duplicado.

## 6. **LAS ARISTAS POR LECTURA** (`D.29`, `D.37`, `D.53`), **CON `d111`, `d108` Y `d098` DELANTE**

**Las que mi lectura sostiene o descarta**, una fila cada una en `.v76aud/aristas_lectura.tsv`, con su tramo de madre, de hijo y su
linea del libro, **escritas antes de que el barrido terminara** (con `5` de `22` recogidas), **mirando tambien madres que viven en el
grafo y en otras bandejas** (la busqueda por asunto, abajo). El cruce dice si el barrido levanto el par y donde vive hoy cada extremo:

@@RUN:0::python .v76aud/cruce_aristas.py@@

**La busqueda por asunto, y las partes de los titulos que dicen cuantas tienen**, por id y titulo sobre grafo mas bandejas:

@@RUN:0::python .v76aud/temas.py | grep -v "^    "@@

(La salida entera, un id por linea con su sede y su libro, en `.v76aud/temas.txt`.)

**LECTURA:**

- **MIS `11` `SOSTENGO` SON `4` LINEAS `CONTINUA` DE LA SECCION `5`, QUE EL BARRIDO LEVANTA, Y `7` ARISTAS POR LECTURA QUE NO**
  (`D.53`): las **`4` de `D.37`** de `fingir_prototipo_cinco_mil_replicas` a las reglas `1`, `2`, `4` y `6` (sus pasos `5`, `6`, `8` y
  `10`, cap_11 L45, L47, L51 y L55), que el barrido no levanta en ningun sentido; **`fingir_prototipo_cinco_mil_replicas` a
  `recorrer_siete_pasos_programa_desarrollo_negocio`** por `D.29` (cap_13 L21 y L41: el programa es el vehiculo del prototipo que la
  madre manda fingir); y **las dos de la pregunta de regla de abajo**, con su duda. **El asunto de `a0d42852` dice *6 aristas por
  lectura*: si es la misma cosa, difiere de mi cuenta en una, y mis dudas son justo donde puede estar.** Lo cruzo par a par en mi
  turno normal, sin decidir aqui cual.
- **`D.37` DISPARA EN UNA SERIE Y NO EN LAS DEMAS.** En `fingir_prototipo_cinco_mil_replicas` si: su titulo y su paso `4` dicen seis,
  sus pasos `5` a `10` las nombran, y **cuatro de las seis partes existen como nodo**; las reglas `3` y `5` no tienen ficha en ninguna
  sede (la busqueda de arriba da `0` en las dos). **En las demas no**: los cinco componentes de la contratacion, las ocho reglas del
  juego, los seis pasos de venta, los trece indicadores y las cinco preguntas **son los propios pasos de su ficha**, y ninguna parte
  existe como nodo aparte; en los tres tipos de sistemas, la venta y la medicion son **ejemplares** de un Soft System y de un
  Information System (L137 y L303), no las clases, y `D.37` pide que la parte sea *la que ese paso nombra*.
- **`d111`, LA SERIE DE `recorrer_siete_pasos_programa_desarrollo_negocio`**: **de las fichas de `cap_18`, la parte es
  `construir_estrategia_gente_cuatro_componentes`**, que es la People Strategy misma (L117 y L119 son su definicion), y el barrido la
  levanta desde los dos lados: **es linea `CONTINUA`, no arista por lectura**, citando el paso `8` de la cabeza (cap_13 L53). La
  contratacion y las reglas del juego son piezas dentro del paso, no el paso. **De `cap_19`, ninguna es el paso `7`**: cap_19 nunca
  define la Systems Strategy como procedimiento, y sus tres fichas son la tipologia y dos ejemplares. **Mi lectura: la cabeza entra
  con `1` de `7` y su unica arista a parte es esa.** Y lo dejo a la vista porque es el punto que `d111` pide decidir con la medida
  delante: **si la estrategia de gente se lee como METODO DENTRO del paso**, que es como la frontera de la vuelta `5` leyo los pasos
  `1` y `2`, **la cabeza entra con `0` de `7` y sin arista a parte**. `D.37` cubre las dos lecturas por su letra; lo que cambia es si
  esta ficha *es* la parte, y eso es lectura, no doctrina.
- **LA PREGUNTA DE REGLA, la de mas peso de esta pagina, y no la decido aqui:** `construir_estrategia_gente_cuatro_componentes` dice en
  su **titulo** *cuatro componentes* y los nombra (Primary Aim, Strategic Objective, Organizational Strategy, Operations Manuals), y dos
  de esas partes tienen ficha que las construye: `responder_8_preguntas_construir_primary_aim` y
  `responder_4_preguntas_estandares_objetivo_estrategico`. **Leido por la letra de `D.37`, la estrategia de gente seria CABEZA y esas
  dos, sus PARTES**; **mi lectura va en la direccion contraria, por `D.29`**: esas dos son **madres** de la estrategia de gente, cuya
  condicion es tenerlas escritas y cuyo paso `2` *arranca con* el Primary Aim. Mis razones: **la cuenta es del titulo de la ficha y
  no del libro** (L119 enumera sin contar, y la correccion del titular de `D.37` manda `D.29` cuando el texto solo enumera), y **esas
  dos fichas son metodos dentro de los pasos `1` y `2` del programa**, no el Primary Aim ni el Objetivo Estrategico (la misma lectura
  de `d111`). **Si la letra de `D.37` alcanza a una cuenta que solo pone la ficha, la direccion se invierte y eso es doctrina**: mi
  encargo dice que se para y se trae. **Lo llevo a mi turno normal con la lectura del extractor delante.**
- **`d108`, cap_14 L27 contra L117, con las dos delante:** L27 pregunta *What do I value most? What kind of life do I want? What do I
  want my life to look like, to feel like? Who do I wish to be?* y L117 abre *the following questions*, las ocho de L119 a L133 que
  `responder_8_preguntas_construir_primary_aim` transcribe enteras (seccion `3`). **Mi lectura firma la de la `ACTA G4`**: L27 es el
  mismo cuestionario del mismo Primary Aim en corto, su *look like* esta en L119, y separarlo haria el gemelo de su propio donante. **La
  ficha no le da nodo aparte y no hace falta.**
- **`d098`, el puntero de las tres fases de `cap_05` L29:** **ninguna ficha es su cabeza** (ninguna enumera Infancy, Adolescence y
  Maturity) **y ninguna es una de sus partes**: las dos de `cap_08`, el capitulo de Maturity, son piezas de ese capitulo (la plantilla
  de Watson y el modelo desde el cliente), no la fase; y `dictar_ritmo_crecimiento_preguntas_escritas`, de `cap_07`, es el remedio
  que el libro da al salir de la zona de confort, no la Adolescencia. En grafo mas bandejas **no hay cabeza ni nodo de fase** (la
  busqueda de arriba: lo que levanta *madurez* es la madurez relevante a la tarea de Grove, otra doctrina). **Sin arista**, y `d098`
  sigue esperando su cabeza.
- **Ninguna madre del grafo ni de otra bandeja para las `22`**, por mi lectura: lo que la busqueda levanta por contratacion,
  organizacion, sistema, manual, color o plan son otras doctrinas de otros libros (`6.1`), y ninguna es la condicion de una de las
  `22` ni la remite con palabras.

## 7. **EL ORDEN QUE MI LECTURA OBLIGA** (`D.36`)

**No es un orden: son las restricciones**, escritas antes de ver el del extractor. Madre antes que hijo por mis `CONTINUA` y mis
`SOSTENGO` con los dos extremos en la tanda, y cuantas cumple el orden de pieza del libro, **que saco de mi fidelidad** (capitulo y
primera linea), porque `.v76aud/las22.txt` va alfabetica:

@@RUN:0::python .v76aud/restricciones_orden.py@@

**LECTURA:** las `11` que obligan **las cumple ya el orden de pieza del libro**. De las `4` de `D.36` de un solo lado, **dos no las
cumple** (`medir_sistema_venta_trece_indicadores_benchmark` antes que `construir_estrategia_gente_cuatro_componentes`, y
`interrogar_negocio_cinco_preguntas` antes que `operar_modelo_gente_destreza_minima`); **son informativas y no obligan**, porque la
aduana de `insertar` mide grafo mas bandejas (`D.38.5`) y el par se levanta igual desde el lado que entre despues. **Su orden, contra
estas once, lo compruebo en mi turno normal.**

