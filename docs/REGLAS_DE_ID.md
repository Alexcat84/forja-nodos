# REGLAS DE ID

Anclaje: MANUAL_SISTEMA_DE_CONOCIMIENTO seccion 2 (fase cero), donde se manda
escribir las reglas de id ANTES del primer nodo: "un solo idioma, sin sufijos
numericos (_2, _3), sin variantes por preposicion o articulo, sin traducciones
paralelas. Si dos cosas merecen ids parecidos, merecen revision antes de
existir."

Estas reglas estan tambien en codigo, en src/reglas_id.py, y las hace cumplir
el gate en cada commit y la aduana en cada insercion. Si el codigo y este
documento se separan, manda este documento y el codigo esta roto.

El id no es el nombre del nodo: es su IDENTIDAD. El nombre por el que un lector
llega al nodo (nombre largo, sigla, termino en otro idioma) viaja en
denominaciones, y esa separacion entre NOMBRE e IDENTIDAD es justamente lo que
evita que dos entidades distintas se fundan en silencio (manual seccion 9).

## Regla 1. Un solo idioma: castellano
El id se escribe en castellano. Un termino en ingles, o cualquier otro idioma,
no genera un id: se registra en `denominaciones.otros_idiomas` y en
censos/denominaciones.md.

- valido: `registrar_fuente_canonica`
- invalido: `register_canonical_source`
- invalido: `registrar_source` (mezcla de idiomas en un mismo id)

### Las dos listas, y el criterio que las separa (10 sep 2026)

La version vieja de esta regla era **una lista negra de 37 palabras** sin mas
criterio que "lo que aparece con mas frecuencia". El estreno de la aduana la
midio: **dejaba pasar 269 de los 3.169 ids vivos** del catalogo auditado, y
dejaba entrar `variance_analysis` y `work_breakdown_structure` enteros.

**Decision del fundador del 10 sep 2026: no se engorda a ciegas, y NO se pone
una prueba de idioma automatica.** Se le da criterio, y son dos listas.

| lista | que es | donde vive |
|---|---|---|
| **NEGRA** | palabra inglesa **que tiene equivalente corriente en castellano**. Si la palabra existe en castellano y se usa, el id la usa | `INGLES_CON_EQUIVALENTE`, 366 piezas |
| **BLANCA** | **prestamo asentado** en el castellano de negocios, donde traducir fabricaria un termino que nadie dice | `PRESTAMOS_ASENTADOS`, 33 piezas |
| ni una ni otra | **nombre propio y sigla**: un apellido no tiene equivalente, y una sigla no es una palabra | `NOMBRES_Y_SIGLAS`, 27 piezas |

- **negra:** `customer`, `management`, `quality`, `supply`, `framework`,
  `variance`, `breakdown`, `procurement`, `stakeholders`.
- **blanca:** `marketing`, `benchmarking`, `startup`, `lean`, `coaching`,
  `scrum`, `feedback`, `stock`, `software`, `web`, `ranking`, `escrow`.
- **nombres y siglas:** `deming`, `shewhart`, `juran`, `osha`, `swot`, `leed`.

**LAS DOS LISTAS NO PUEDEN SOLAPARSE**, y el modulo lo comprueba al importarse:
una palabra no puede tener equivalente corriente **y** ser un prestamo
asentado. Si alguna vez chocan, la regla dejo de tener criterio.

**POR QUE ESTO NO ES PURISMO.** Dos grafias del mismo concepto **parten la
familia**: `retencion_clientes` y `customer_retention` tienen clave de familia
DISJUNTA, asi que la señal 2 no los ve juntos **y entran los dos**. Un solo
idioma en los ids es lo que deja trabajar a la señal.

**LOS 269 IDS DEL CATALOGO SON COSA JUZGADA.** Esta regla rige lo que se
**escribe** de ahora en adelante. No se reabre un id ya adjudicado por una
lista que llego despues.

Ampliar cualquiera de las dos listas es **correccion declarada con fecha**, no
una edicion silenciosa.

## Regla 2. Sin sufijos numericos DE VERSION
Nunca `_2`, `_3`, `_bis`, `_nuevo`, `_final`. Un sufijo numerico de version es
la firma de una duplicacion que alguien no quiso mirar: si hay un segundo nodo,
o continua al primero (y entonces pide arista y nombre propio) o lo repite (y
entonces no entra, seccion 5 del manual).

- valido: `elegir_grafia_clave`
- invalido: `elegir_grafia_clave_2`
- invalido: `registrar_fuente_canonica_final`

### El numero que es parte de la denominacion SI vale (10 sep 2026)

La version vieja prohibia **todo** numero al final. **Medido sobre el catalogo
auditado:** de los 48 ids vivos que acaban en numero, **44 llevan un numero de
una cifra y son versiones** (`accion_correctiva_2`, `consejo_de_calidad_3`), y
los **4** que llevan un numero mayor son **denominaciones**:

    familia_normas_iso_9000       cumplimiento_ftc_rule_436
    canales_de_traccion_19        riesgo_split_51_49

**NADIE HACE UNA VERSION 436.** Ese es el corte, y esta contado: **48 de 48**.
La regla prohibe el numero final **de una sola cifra** (`TOPE_DE_VERSION = 9`).

**Y EL NUMERO EN MEDIO NUNCA FUE VERSION.** Los 14 vivos que lo llevan son los
ejemplares de la regla, y todos son denominaciones:

    los_14_puntos_deming              benchmarking_7_pasos_juran
    iso_31000_gestion_riesgo          regla_50_por_ciento
    programa_mejora_calidad_14_pasos  modelo_lubin_esty_4_etapas

**LA VERSION CUYA BASE YA VIVE SE CAZA DOS VECES, y la segunda no es esta
regla.** `familia()` normaliza los digitos finales, asi que
`accion_correctiva_2` y `accion_correctiva` tienen la **misma clave de
familia**: la señal 2 los levanta como vecinos aunque la regla 2 los dejara
pasar. **De los 48, 39 tienen su base viva en el grafo.** La puerta y la cola
dicen lo mismo por caminos distintos, que es como tiene que ser.

## Regla 3. Sin preposiciones ni articulos
Las piezas del id son las palabras con carga. Nada de `de`, `del`, `la`, `el`,
`los`, `las`, `por`, `para`, `con`, `sin`, `en`, `y`, `a`, `al`, `que`. La lista
completa esta en `PALABRAS_VACIAS`.

- valido: `registrar_fuente_canonica`
- invalido: `registrar_la_fuente_canonica`
- invalido: `registro_de_fuentes`

La razon es medida: la variante por preposicion es la forma mas barata de
fabricar un gemelo invisible, porque `registro_de_fuentes` y `registro_fuentes`
se leen igual y se buscan distinto.

## Regla 4. Sin traducciones paralelas ni familias repetidas
Dos ids no pueden pertenecer a la misma FAMILIA. La familia se calcula
normalizando el id: se quitan sufijos numericos, preposiciones, articulos y
plurales, y se ignora el orden de las palabras.

- `registro_de_fuentes`, `registro_fuentes` y `fuentes_registro` son LA MISMA
  familia: solo puede vivir uno.
- `registrar_fuente_canonica` y `elegir_grafia_clave` son familias distintas:
  pueden convivir, y de hecho conviven como madre e hijo.

Quien comprueba que aplica cada cosa:

- FAMILIA EXACTA (misma clave): el gate lo pone en rojo. `registro_fuentes` y
  `fuente_registro` no pueden coexistir.
- FAMILIA PARECIDA: la señal 2 de la aduana la levanta desde 0,5 de solape.
  `registrar_fuente_canonica` contra `registro_fuentes_canonicas` mide 0,5
  exacto: la insercion se bloquea y alguien lee. El umbral esta en
  config/umbrales.json y es editable.

LIMITE DECLARADO de esta regla: la familia normaliza plurales, numeros,
palabras vacias y orden, pero NO conjuga verbos. `registrar_fuentes` contra
`registro_fuentes` mide 0,33 (dos piezas, una compartida) y por tanto NO
levanta la señal 2. Si esos dos nodos hacen el mismo trabajo, quien los caza
es la señal 1 o la 3, que miran el texto y los pasos; si ninguna llega,
entran los dos, y ese es el riesgo residual que la casa acepta a sabiendas.
El remedio obvio (un normalizador de verbos) es peor que la enfermedad:
fusionaria ids legitimos en silencio, que es exactamente lo que el principio
4 prohibe. Las señales ordenan, nunca deciden.

Cuando dos candidatos caen en la misma familia, el gate lo declara en rojo y
alguien tiene que leer los dos: o son el mismo nodo, o merecen revision antes
de existir. La familia de id es ademas la señal 2 de la aduana (midio 50,8 por
ciento de precision en esta casa: buena para ordenar la cola, incapaz de
decidir sola).

## Regla 5. Verbo mas objeto, minimo dos piezas
Un id nombra un procedimiento, no una categoria. Se escribe con verbo en
infinitivo mas su objeto.

- valido: `resolver_ids_alias`, `auditar_veredictos_ciegos`
- invalido: `fuentes` (categoria, no procedimiento)
- invalido: `calidad` (una palabra suelta no nombra un trabajo)

## Regla 6. Forma: snake_case estricto
Solo minusculas de la a a la z, digitos y guion bajo, empezando por letra.
Sin acentos, sin eñes, sin espacios, sin guiones cortos, y por supuesto sin
guiones largos ni medios (hook de estilo de la casa). Sin guion bajo doble.

- valido: `extraer_nodos_capitulo`
- invalido: `Extraer_Nodos`, `extraer-nodos`, `extraer_diseño`, `extraer__nodos`

## Regla 7. Los ids_alias son ids muertos: forma si, doctrina no
Un alias existe precisamente porque alguna vez se escribio un id que hoy no se
aceptaria. Al alias se le exige la FORMA (regla 6) y nada mas: si se le exigiera
doctrina, el sistema no podria guardar la memoria de sus propios errores, y el
resolutor perderia la cadena.

Un alias no puede ser a la vez id canonico vivo (dos cosas con un nombre), ni
alias de si mismo, ni estar reclamado por dos nodos. El resolutor declara las
tres cosas en rojo.

## Regla 8. La comparacion de ids no es literal
Ningun conteo, guarda o busqueda de este repo compara ids con `==`: se resuelve
por src/resolutor.py y se compara despues (manual principio 3). Escribir una
comparacion literal fuera del resolutor es escribir un bug: inventa salud
(auto-aristas por alias que nadie ve) e inventa enfermedad (aristas a ids
deprecados que si resuelven).

La prueba D de tests/test_aceptacion.py existe solo para esto: un nodo con una
auto-arista VIA ALIAS pone el gate en rojo, y una comparacion literal no la
veria.

## Que hace la aduana antes de rechazar
La aduana normaliza lo que es forma antes de juzgar (src/aduana.py,
`normalizar_candidato`): baja a minusculas, quita acentos, y convierte espacios
y rayas en guion bajo. No normaliza lo que es doctrina: si despues de eso el id
sigue rompiendo una regla, se rechaza en vez de maquillarse. Un id maquillado
es una decision tomada por una maquina.
