# APERTURA CIEGA DE LA VUELTA 63, TERCERA FASE CIEGA DE LA MISMA VUELTA

*Linea **serial** (`extraccion-mundo-11`), libro `grove_high_output`, vuelta de **INSERCION**
(`MODO_INSERCION=insertar`). Auditor ciego `claude-opus-5-5`, 23 sep 2026. Esta pagina se
escribe entera por `.v63aud/ensamblar.py`: cada bloque que empieza por `$` lo pega el propio
ensamblador con la salida que el comando imprimio al ensamblar, y nada mas (R5).*

**LAS DOS FASES CIEGAS ANTERIORES DE ESTA VUELTA ESTAN ANULADAS Y NO LAS REUTILIZO.** La primera
murio con el reinicio de las `00:29`; la segunda cerro a las `07:52` con el sello rechazado por
`censo_rutas` en ROJO. De la segunda solo lei su `LEEME.md` de archivo y la salida de la guarda
en su testigo, para saber que la tumbo (una seccion sin rellenar y un informe de aduana en `0`
bytes). **Su clasificacion no la abri.** Esta pagina no tiene ninguna seccion que dependa de un
trabajo sin recoger: el ensamblador se niega a escribirla si queda un hueco.

---

## 0. LA HERENCIA (D.40)

ACTA ANTERIOR LEIDA: 388afd4c343a24d59e548bba512e4fd3c2fd428e

La huella es la del fichero del acta tal como esta en el arbol, medida:

{{$ git hash-object docs/loop/ACTA_AUDITOR.md}}

**HEREDADO 1: NO APLICA en esta fase**, y el motivo es de sede: `R5` es un remedio **del
extractor** sobre los bloques `$` de SU reporte, y su sitio de comprobacion escrito es *la
vuelta que reabra esta linea, con `.v62aud2/pegado62_final.py`*. Ese instrumento lee el reporte,
y el reporte esta retirado del arbol en esta fase por `D.34.2`. **Se comprueba en mi turno normal,
contra el reporte de la vuelta 63.** Lo que si cumplo aqui es la misma regla en mi propia
pagina: todos mis bloques los pega el ensamblador con la salida literal. Lo que lo sostiene:

{{$ ls docs/loop/REPORTE.md 2>&1; head -12 .v62aud2/pegado62_final.py | sed -n 11p}}

**HEREDADO 2: NO APLICA en esta fase.** `R6` pide que todo criterio de seleccion que YO escriba
en un encargo lleve su alcance y su instrumento al lado, y se comprueba en *el proximo encargo que
escriba esta linea*. Esta fase ciega no escribe encargo, y el encargo vigente de la vuelta 63 no
es de un auditor: lo escribio la sesion de chat del `22` sep. El proximo encargo que escribe esta
linea es el de mi turno normal, y ahi se cumple. Lo que lo sostiene:

{{$ sed -n 3,4p docs/loop/PROMPT_SIGUIENTE.md}}

**HEREDADO 3: CUMPLIDO.** `R7` pide que toda adjudicacion de duplicado cite la vara `6.1` y solo
esa. En esta pagina no adjudico: clasifico a ciegas, y **cada clasificacion de par que escribo
(seccion 5) dice CONTINUA o REPITE por la vara `6.1` de `AUDITOR_FORJA.md`**, leyendo los pasos y
con la direccion escrita, madre e hijo. La vara de que es un nodo de `EXTRACTOR.md` no aparece
aqui para decidir ningun par. Lo mido sobre la plantilla de la que sale toda la prosa de esta pagina (el patron esta escrito
de modo que la linea del comando no se cuente a si misma):

{{$ grep -cE "EXTRACTOR[.]md.9[.]1" .v63aud/plantilla.md}}

**UNA DISCREPANCIA DE HERENCIA QUE DECLARO Y NO RESUELVO.** El prompt me entrega `3` heredados.
El instrumento de la casa, corrido ahora, dice `0` y da el motivo: el credito de la serial esta
retirado del arbol en esta fase, y sin el la linea parece recien nacida. **Me atengo a los `3`
del prompt**, que es lo que el arnes midio antes de retirar. **LECTURA:** `forja.py herencia`
corrido dentro de la fase ciega mide la ausencia que la propia fase ciega fabrica; no es una
caida de nadie y no lo arreglo aqui (`D.45`, `D.55`).

{{$ python forja.py herencia 2>&1 | sed -n 5,9p}}

---

## 1. LO QUE ESTE TURNO NO VE (D.57)

La linea del arnes para este turno, leida en el log, que no se retira:

{{$ grep -n "08:07:46.*APERTURA CIEGA" docs/loop/loop.log}}

**Los cuatro retirados no estan en el arbol, y no los busque por ninguna otra via:**

{{$ ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl 2>&1}}

**LIMITACION, escrita en vez de afirmada:** no se que dice el reporte de la vuelta 63 ni cuantas
de sus tareas cerro. Lo que se de esa vuelta lo se **por el estado del arbol**, no por su palabra,
y va en la seccion 2. **No evidencia de mi turno tampoco:** la carpeta del extractor de esta vuelta
esta en el arbol y NO la abri, porque es su lectura y leerla antes de escribir la mia seria leer a
medias lo que vengo a leer a ciegas.

---

## 2. EL ESTADO, MEDIDO EN ESTA FASE

{{$ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl}}

{{$ ls cuarentena/grove_high_output/*.json | wc -l; ls cuarentena/_insertados/grove_high_output/}}

{{$ git status --short dataset/ bitacora/ censos/ config/ | wc -l}}

**LECTURA:** el grafo sigue en `346` nodos, la bitacora en `740` veredictos, `1` par mutuo, y la
bandeja de Grove en `91` con `1` solo insertado de antes. **En la vuelta 63 no entro ningun
nodo**, y el arbol de datos no tiene cambios sin commitear. Lo que el extractor de la `63` si movio
son **los candidatos de la bandeja** (el dictamen del `23` sep habla de correcciones de
fidelidad hechas antes de insertar): **mi lectura de la seccion 3 es sobre los candidatos tal como estan
ahora**, ya corregidos, y no se cuales fueron.

**EL CERROJO HUERFANO DE LA INSERCION INTERRUMPIDA sigue en el arbol**, y su dueno no vive. No lo
toco: el arnes ya lo declaro y `src/cerrojo.py` lo rompe en el proximo `insertar` (`D.44`).

{{$ cat procesos/nodos.jsonl.679b2259.cerrojo; echo; tasklist //FI "PID eq 14980" | tail -1}}

---

## 3. LA LECTURA DE FIDELIDAD, ENTERA Y NO MUESTREADA (D.30)

**LA TANDA SON `16` CANDIDATOS:** los `7` de `cap_02` enteros y los `9` de `cap_03` que su aduana
en seco dio como `ENTRARIA`. Los `6` restantes de `cap_03` son la deuda `d005` y no entran en esta
vuelta. La lista de los `16` es `.v63aud/tanda.txt`, y la de los `9` sale de la linea de saldo de
cada informe de `.v2g/`:

{{$ for f in .v2g/informe_[a-z]*_*.txt; do printf "%s %s\n" "$(grep -m1 'ENTRARIAN sin leer' $f | tr -s ' ' | cut -d: -f2)" "$(basename $f .txt)"; done}}

**COMO LA HICE:** cada paso de cada candidato contra la linea del libro de la que dice salir, con
el capitulo impreso delante (`fuentes/grove_high_output/cap_02.md` L15 a L79 entero y
`fuentes/grove_high_output/cap_03.md` L15 a L179 entero). Cada paso tiene su fila en
`.v63aud/fidelidad.tsv`, con su clase, su linea y su nota. **LAS CIFRAS NO LAS CUENTO YO:** las
cuenta `.v63aud/contar_fidelidad.py`, que ademas comprueba que cada paso de cada candidato tenga
su fila y que ninguna fila sobre.

{{$ python .v63aud/contar_fidelidad.py}}

### 3.1. **`PASOS INVENTADOS POR CAPITULO`, MI LECTURA CIEGA**

| capitulo | pasos leidos | PUENTE | DUDA | puente por ciento |
|---|---:|---:|---:|---:|
| `cap_02` | `50` | `0` | `1` | `0` |
| `cap_03` | `80` | `0` | `0` | `0` |

*Las cifras de esta tabla son las del bloque de arriba, copiadas de su salida.* **LECTURA:** cero
puentes en los `130` pasos. **No lo leo como que el libro sea facil**: `cap_02` y `cap_03` son de
inventario rico (el libro nombra el medio, la etapa y el objeto en casi cada frase), y **ademas el
material ya viene corregido de fidelidad por el propio extractor de la `63`**. Lo que mido es el
material que va a entrar, que es lo que importa en insercion.

### 3.2. **LA UNICA DUDA, Y LOS PASOS QUE SON GLOSA**

- **`detectar_arreglar_fallo_etapa_menor_valor` paso `1`, DUDA.** *Ordena las etapas de tu flujo
  por el valor que el material lleva encima.* L73 da la **propiedad** (*the material becomes more
  valuable as it moves through the process*), no la accion de ordenar. **LECTURA:** no llega a
  puente, porque en un flujo las etapas ya estan ordenadas y el valor crece con ellas, asi que
  ordenar por valor es seguir el flujo; pero el verbo es del extractor y lo dejo marcado para que
  su lectura lo diga o no.
- **Pasos que estan en el libro y NO son paso**, sino glosa: `detectar_arreglar_fallo...`
  paso `2` (L73, el rotulo que el cliente ve al aparcar), `variar_frecuencia_inspeccion...` paso
  `6` (L143, *we are creatures of habit*) y los pasos `5`, `6` y `7` de
  `representar_actividad_caja_negra_ventanas` (L73, los tres ejemplos del libro puestos como
  pasos). **LECTURA:** son TRANSCRIPCION por la vara de `D.30`, que solo pregunta si el libro lo
  dice. **No son caida.** Los anoto porque engordan la cuenta de pasos sin anadir procedimiento.

---

## 4. LA CLASE DE CADA CANDIDATO, CON LAS LINEAS QUE LA SOSTIENEN

**Los `16` son procedimiento**: en cada tramo el libro pone su propio inventario de medios y
etapas. Ninguno me parece postura ni definicion suelta. **El unico al borde es
`representar_actividad_caja_negra_ventanas`**: L73 y L77 son casi una definicion (entrada, salida,
trabajo, ventanas). **LECTURA:** lo sostengo como nodo porque es la **madre** de las ventanas que
el capitulo abre despues (L81 a L99), y sin ella el indicador de linealidad y el de tendencia no
tienen caja en la que recortar.

| candidato | cap | tramo | clase | madre que leo en el libro |
|---|---|---|---|---|
| `construir_flujo_produccion_paso_limitante` | `cap_02` | L15 a L27 | procedimiento | ninguna: es la cabeza del capitulo |
| `clasificar_trabajo_proceso_montaje_prueba` | `cap_02` | L37 a L47 | procedimiento | ninguna |
| `rehacer_flujo_paso_limitante_capacidad` | `cap_02` | L49 a L55 | procedimiento | `construir_flujo...` (L53 rehace el flujo que L25 construyo) |
| `equilibrar_capacidad_personal_inventario_plazo` | `cap_02` | L57 a L61 | procedimiento | `rehacer_flujo...` (L57: *let's complicate things a little further*, la misma cola del tostador) |
| `preferir_inspeccion_proceso_prueba_destructiva` | `cap_02` | L67 | procedimiento | ninguna en la tanda (L63, la operacion continua, no tiene nodo) |
| `dimensionar_inventario_materia_prima_reposicion` | `cap_02` | L69 | procedimiento | ninguna en la tanda |
| `detectar_arreglar_fallo_etapa_menor_valor` | `cap_02` | L71 a L75 | procedimiento | ninguna |
| `elegir_cinco_indicadores_diarios_fabrica` | `cap_03` | L15 a L29 | procedimiento | ninguna |
| `representar_actividad_caja_negra_ventanas` | `cap_03` | L71 a L79 | procedimiento, al borde | ninguna |
| `construir_indicador_linealidad_alerta_temprana` | `cap_03` | L83 a L87 | procedimiento | `representar_actividad_caja_negra_ventanas` (L83: *a window cut into the black box*) |
| `casar_flujo_fabricacion_flujo_ventas` | `cap_03` | L111 a L121 | procedimiento | **dos candidatos de `d005`** (seccion 6) y `detectar_arreglar_fallo...` por L119 |
| `dimensionar_plantilla_administrativa_pronostico` | `cap_03` | L123 a L125 | procedimiento | **dos candidatos de `d005`** (seccion 6) |
| `decidir_aceptar_rechazar_material_defectuoso` | `cap_03` | L135 a L137 | procedimiento | `dimensionar_inventario...` (L69 solo da *devolver*; L135 anade *usar lo que no llega*) |
| `elegir_inspeccion_barrera_monitorizacion` | `cap_03` | L139 a L141 | procedimiento | `preferir_inspeccion...`, de lejos |
| `variar_frecuencia_inspeccion_nivel_calidad` | `cap_03` | L143 | procedimiento | hermano de `elegir_inspeccion...` (L143: *another way to lower the cost*) |
| `simplificar_trabajo_reducir_numero_pasos` | `cap_03` | L169 a L173 | procedimiento | ninguna: el libro lo numera por si mismo (*first, second, third*) |

---

## 5. EL BARRIDO DE VECINOS SOBRE GRAFO MAS BANDEJAS (D.38.4), Y MI CLASE DE CADA PAR

**EL METODO VIGENTE de `D.38.4`** (su correccion del 16 sep): se barre **uno por vez**, entregando a
la aduana el candidato y dejando que ella ponga las bandejas. Lance los `16` en paralelo con
`.v63aud/barrer.sh`, **los recogi todos dentro del turno**, y ninguno quedo en cero bytes. El registro
del lanzador, con el codigo de salida y los segundos de cada uno:

{{$ cat .v63aud/barrido.log}}

**LA POBLACION**, leida de los `16` informes y no de memoria:

{{$ grep -h "poblacion del barrido" .v63aud/informe_*.txt | sort | uniq -c}}

**LO QUE LEVANTO CADA UNO**, resumido por `.v63aud/vecinos.py` desde los informes de la carpeta
`.v63aud/`, uno por candidato:

{{$ python .v63aud/vecinos.py}}

### 5.1. **MI CLASE DE CADA PAR LEVANTADO, POR LA VARA `6.1` Y LEYENDO LOS PASOS**

*La senial dijo donde mirar y ahi acabo su trabajo (`D.19`). Cada par lo he leido con los pasos de los
dos delante. Un par que la aduana levanta desde los dos lados va en una sola fila.*

| par | mi clase | lo que la sostiene |
|---|---|---|
| `construir_flujo_produccion_paso_limitante` con `rehacer_flujo_paso_limitante_capacidad` | **CONTINUA, madre `construir_flujo...`, hijo `rehacer_flujo...`** | el hijo rehace el flujo de la madre cuando la capacidad es finita: su paso `4` vuelve a calcular hacia atras desde la entrega (madre pasos `7` a `9`), y su paso `5` mantiene los ciclos y cambia solo los desfases (madre paso `9`). Lo que anade (la cola, la espera dentro del flujo) es procedimiento que la madre no trae. L51 a L53 sobre L23 a L27 |
| `detectar_arreglar_fallo_etapa_menor_valor` con `supervisar_tarea_delegada_etapa_menor_valor` (bandeja, `cap_04`) | **CONTINUA, madre `detectar_arreglar...`, hijo `supervisar_tarea...`** | el paso `2` del hijo es la regla de la madre (paso `3`) aplicada a la delegacion, y el hijo trae procedimiento propio que la madre no tiene: los borradores en sucio, la frecuencia variable por madurez en la tarea, el detalle al azar. **El hijo espera en la bandeja**: la arista se declara cuando entre el |
| `construir_flujo_produccion_paso_limitante` con `retirar_barreras_politicas_metodo` (grafo, `smart_who`) | **SANO** | nada en comun: contratar sin barreras de politica contra construir un flujo. La senial sale de la muletilla del paso `4` del candidato (*que es por donde el libro dice que se empieza*) contra la del vecino (*que es con quien el libro dice*) |
| `preferir_inspeccion_proceso_prueba_destructiva` con `construir_flujo...`, con `rehacer_flujo...` y con `clasificar_trabajo_proceso_montaje_prueba` | **SANO** los tres | la misma fabrica de desayunos y el mismo vocabulario (el huevo, el tostador, rehacer); procedimientos distintos a los dos lados, y ninguno desarrolla un paso del otro |
| `preferir_inspeccion_proceso_prueba_destructiva` con `dimensionar_inventario_materia_prima_reposicion` | **SANO**, hermanos | los dos cuelgan de la maquina continua de L63 (L67 y L69, *what else could go wrong*): uno elige como vigilar el proceso, el otro inspecciona la entrada y dimensiona el inventario. Ninguno continua al otro |
| `dimensionar_inventario_materia_prima_reposicion` con `detectar_arreglar_fallo_etapa_menor_valor` | **SANO, y lo marco DISCUTIBLE** | lo comun es un ejemplo, el huevo podrido rechazado al recibirlo (paso `4` de `detectar...` contra pasos `1` a `3` de `dimensionar...`). Lo que queda fuera es procedimiento en los dos lados, asi que no REPITE. **La duda es si `dimensionar...` CONTINUA a `detectar...` desarrollando su paso `4`**; lo leo SANO porque lo que anade `dimensionar...` (el tamano del inventario por el tiempo de reposicion y la oportunidad en riesgo) no desarrolla la regla del menor valor, desarrolla otra cosa |
| `rehacer_flujo_paso_limitante_capacidad` con `dimensionar_inventario...` | **SANO** | vocabulario comun (parar, esperar), procedimientos distintos |
| `dimensionar_plantilla_administrativa_pronostico` con `decidir_aceptar_rechazar_material_defectuoso`, con `elegir_cinco_indicadores_diarios_fabrica` y con `simplificar_trabajo_reducir_numero_pasos` | **SANO** los tres | la plantilla administrativa contra material defectuoso, contra los cinco datos del dia y contra quitar pasos de un flujo: ningun paso de uno desarrolla un paso del otro |

### 5.2. **LOS PARES QUE LEO Y LA SENIAL NO LEVANTA**

**La aduana deja entrar sin vecino a candidatos que yo leo como hijos.** No es un fallo de la aduana
(`D.19`: ninguna senial separa jerarquia de ruido). **Es exactamente el caso de `D.29`**: el par se
declara por lectura, con su razon, o no se declara nunca.

| madre | hijo | lo que lo sostiene | la aduana |
|---|---|---|---|
| `representar_actividad_caja_negra_ventanas` | `construir_indicador_linealidad_alerta_temprana` | el paso `2` del hijo (*recorta en tu caja esta ventana concreta*) desarrolla el paso `8` de la madre (*recorta ventanas en la caja*); L83: *a window cut into the black box* | el hijo sale `ENTRARIA` |
| `dimensionar_inventario_materia_prima_reposicion` | `decidir_aceptar_rechazar_material_defectuoso` | el paso `1` del hijo (*cuando rechaces material en la inspeccion de recepcion*) abre la decision que la madre cierra en su paso `3` con una sola salida (*devuelve*); L135 anade la segunda (usar lo que no llega) y el grupo que decide | no levanta el par |
| `rehacer_flujo_paso_limitante_capacidad` | `equilibrar_capacidad_personal_inventario_plazo` | L57 (*let us complicate things a little further*, en el libro con contraccion) es la misma cola del tostador de L51, ahora chocando con el huevo; el hijo trae las salidas que la madre no tiene (especializar, pedir ayuda, otro tostador, inventario). **Confianza media**: tambien se puede leer como hermano | el hijo sale `ENTRARIA` |
| `elegir_indicador_salida_trabajo_administrativo` (**`d005`**) | `dimensionar_plantilla_administrativa_pronostico` | L125: *if we have carefully chosen indicators that characterize an administrative unit*; el paso `1` del hijo nombra el trabajo de la madre y los pasos `3` a `7` siguen donde ella acaba | no levanta el par |
| `construir_indicador_tendencia_patron` (**`d005`**) | `dimensionar_plantilla_administrativa_pronostico` | L125: *de facto standards, inferred from the trend data*; el paso `2` del hijo sale del patron que la madre mide en su paso `4` | no levanta el par |
| `elegir_fabricar_pedido_pronostico` (**`d005`**) | `casar_flujo_fabricacion_flujo_ventas` | L111: *delivering a product that was built to forecast*; el hijo empieza donde la madre decide fabricar contra pronostico | el hijo sale `ENTRARIA` |
| `construir_grafico_escalonado_pronosticos` (**`d005`**) | `casar_flujo_fabricacion_flujo_ventas` | L121 (*as noted*) remite al grafico de L91 a L97; el paso `12` del hijo lo usa en los dos pronosticos. **Confianza baja**: es un paso de doce, y nombrar no es procedimentar | el hijo sale `ENTRARIA` |

**Y DOS QUE LEO COMO NO CONTINUA**, para que conste que las mire: `casar_flujo...` paso `11` nombra la
regla de `detectar_arreglar_fallo...` (L119, *as we have learned before*, en el libro con
contraccion) y la aplica al inventario en una sola linea, y **nombrar no es procedimentar**: SANO. Y
`variar_frecuencia_inspeccion_nivel_calidad` con `elegir_inspeccion_barrera_monitorizacion` son
**hermanos** (L143: *another way to lower the cost*): SANO.

---

## 6. EL ORDEN QUE LEE Y LAS SERIES

**EL ORDEN DENTRO DE LA TANDA NO TIENE PROBLEMA.** Cada madre que leo dentro de la tanda va delante
de su hijo si se inserta por capitulo y por pieza: `construir_flujo...` antes que `rehacer_flujo...`
y este antes que `equilibrar...`; `dimensionar_inventario...` (`cap_02`) antes que
`decidir_aceptar...` (`cap_03`); `representar_actividad_caja_negra...` antes que
`construir_indicador_linealidad...`.

**EL PROBLEMA ESTA FUERA DE LA TANDA, Y LO DECLARO: DOS DE LOS `16` SON HIJOS DE CANDIDATOS DE `d005`,
QUE NO ENTRAN EN ESTA VUELTA.** `dimensionar_plantilla_administrativa_pronostico` tiene dos madres ahi
y `casar_flujo_fabricacion_flujo_ventas` tiene una clara y otra floja (seccion 5.2). **Si los dos
hijos entran ahora**, sus veredictos se escriben sin la madre en el grafo, y **la senial no los va a
levantar cuando las madres entren**, porque hoy no los levanta en ningun sentido. **LECTURA:** o esos
dos esperan a la vuelta que repare `d005`, o su veredicto de hoy deja escrito el par pendiente para que
la vuelta de `d005` declare la arista por lectura. **No es mio decidir el orden** (`D.36`: lo fija quien
autoriza la insercion); lo dejo leido para que la adjudicacion lo tenga delante.

**LAS SERIES (`D.37`): NINGUNA EN LA TANDA.** Los tres textos que cuentan sus partes no tienen las
partes como nodos: *las tres operaciones* de `clasificar_trabajo...` (L39), *los cinco datos* de
`elegir_cinco_indicadores...` (L17 a L27) y *las dos tecnicas* de `elegir_inspeccion...` (L141), que
viven dentro del mismo nodo. Los tres puntos de inspeccion de `cap_03` L131 si tienen dos partes con
nodo (la de recepcion en `dimensionar_inventario...` y la de proceso en `preferir_inspeccion...`),
**pero L131 no tiene nodo cabeza**, asi que no hay arista cabeza a parte que declarar.

---

## 7. LAS PIEZAS DE LOS DOS CAPITULOS QUE NO TIENEN CANDIDATO, LEIDAS UNA A UNA

| tramo | que es | mi clase |
|---|---|---|
| `cap_02` L17 a L21 | los requisitos de la produccion y la hora comprometida | **absorbida** en `construir_flujo...` pasos `1` a `4`. Bien |
| `cap_02` L31 a L35 | la contratacion como flujo: el paso limitante es el **mas caro** (la visita a la planta) y se filtra por telefono antes | **aplicacion con una tecnica propia** (filtrar antes del paso caro para subir la razon de ofertas por visita). **LECTURA:** su decision es la misma que `detectar_arreglar_fallo...` paso `5` con el mismo ejemplo; **no la leo como nodo perdido**, pero es la pieza de `cap_02` con mas procedimiento sin candidato |
| `cap_02` L41 | la formacion de ventas como proceso, montaje y prueba, con el ensayo en seco | **absorbida** en `clasificar_trabajo...` pasos `1`, `2` y `5` |
| `cap_02` L63 a L65 | pasar a operacion continua, perdiendo flexibilidad | **descripcion con su coste**, dos medios y ninguna etapa. Sin nodo, bien. Es la premisa de L67 y L69 |
| `cap_02` L77 a L79 | la justicia penal como flujo: el paso limitante equivocado (la celda barata) limita al caro (la condena) | **ejemplo** del criterio de `construir_flujo...` paso `10` (*o el mas caro*). Sin nodo, bien |
| `cap_03` L81 | los indicadores adelantados solo sirven si te los crees y actuas | **advertencia**. **LECTURA:** podria ser un paso de `construir_indicador_linealidad...` y no lo es; no la leo como nodo |
| `cap_03` L129 a L133 | rechazar en la etapa de menor valor, y los tres puntos de inspeccion con su nombre | **el libro repitiendose** (*as noted*) sobre `cap_02` L75, mas nomenclatura. Sin nodo, bien |
| `cap_03` L145 a L155 | la embajada de Londres: muestreo en vez de revisar el cien por cien, con criterios fijados antes | **aplicacion** del muestreo de `elegir_inspeccion...` con una tecnica propia (elegir la muestra por criterio fijado). L155 anuncia el uso gerencial en un capitulo posterior |
| `cap_03` L159 a L167 | productividad como salida entre trabajo, y la palanca | **definicion**. Los procedimientos de la palanca viven en capitulos posteriores |

---

## 8. LAS GUARDAS AL CERRAR ESTA PAGINA

Corridas **despues** de ensamblar el resto de la pagina, porque una cifra vale en el instante del
sello (`D.38.3`). El testigo del arnes las vuelve a correr al sellar.

{{$ python forja.py gate 2>&1 | tail -3}}

{{$ python forja.py guiones 2>&1 | tail -2}}

{{$ python scripts/censar_rutas.py 2>&1 | tail -1}}

{{$ python forja.py credito --citas 2>&1 | tail -2}}

{{$ grep -c " rc=0 " .v63aud/barrido.log; tail -1 .v63aud/barrido.log}}

**Ese ultimo bloque es el registro de mi barrido de la seccion 5**: los `16` informes volvieron con
codigo `0` y el lanzador los espero a todos antes de escribir su ultima linea. **No dejo ningun
proceso vivo al cerrar.**
