# BANCO DE REGLAS de forja-nodos

Anclaje: MANUAL_SISTEMA_DE_CONOCIMIENTO seccion 2: "BANCO DE REGLAS versionado
en el repo: las doctrinas se citan por numero, se corrigen con fecha, y nadie
inventa reglas en caliente".

Aqui viven las reglas de ESTA forja: las que el manual manda y las que esta
casa tuvo que decidir para poder ejecutarlo. Se citan por numero (D.1, D.2) en
los veredictos, en los commits y en las actas del bucle.

Como se corrige una regla: se añade la correccion DEBAJO, con su fecha, y el
texto viejo queda en pie. Una correccion que tapa lo que corrige no se puede
auditar (manual principio 6). Nadie inventa reglas en caliente: si un caso pide
una regla que no existe, se marca PENDIENTE DE DOCTRINA en la razon del
veredicto y se sigue (docs/loop/EJECUTOR.md regla 3).

## D.1. Semantica de las aristas (12 ago 2026)
`nodos_previos` y `nodos_siguientes` son SECUENCIA DIRIGIDA de madre a hijo. La
arista existe en los DOS extremos (la madre declara al hijo en
`nodos_siguientes` y el hijo declara a la madre en `nodos_previos`); un extremo
sin el otro es un hueco y el gate lo declara.
La vuelta (el mismo par declarado en los dos sentidos) es un fallo, no una
redundancia. Vale para TODO par, no solo para las series numeradas.

**Adjudicacion del auditor A.1 (12 ago 2026):** ratificada estricta. La UNICA
vuelta bidireccional legitima es el ENLACE MUTUO DECLARADO: un veredicto de
clase MUTUO, con el procedimiento de ida y el procedimiento de vuelta escritos
por separado (nunca una razon comun), registrado en bitacora/VEREDICTOS.jsonl
y en la lista blanca config/pares_mutuos.jsonl (par, fecha, las dos razones y
quien lo declaro). El gate perdona la vuelta SOLO para los pares que esa lista
blanca cubre tras resolver (manual principio 3: la lista blanca tambien pasa
por el resolutor); cualquier otra vuelta sigue siendo fallo, declarada a mano
o no. Implementado en src/aduana.py (clase MUTUO, funcion parsear_veredicto) y
src/gate.py (guarda vuelta, funcion _pares_mutuos_resueltos). Caso positivo y
control en tests/test_aceptacion.py, clase PruebaMutuo y
PruebaGate.test_a1_vuelta_declarada_en_lista_blanca_pasa.

> **CORREGIDA POR ADICION el 4 sep 2026 (TANDA A), y el texto de arriba queda
> en pie porque una correccion que tapa lo que corrige no se puede auditar.**
> Dos cosas de ese parrafo ya no describen el codigo de hoy:
> **(1)** la lista blanca dejo de ser lista de pertenencia y es REGISTRO DE
> CITAS (**D.14**): el gate ya no comprueba que el par este, comprueba que su
> cita se sostenga entera, y `_pares_mutuos_resueltos` se llama hoy
> `_citas_mutuas` mas `_fallos_de_cita`.
> **(2)** las dos razones ya no bastan: cada sentido CITA SU LINEA y las dos
> tienen que ser distintas (**A.4**).
> Lo que A.1 dice y sigue intacto: la unica vuelta legitima es el enlace mutuo
> declarado, y todo lo demas es fallo.

## D.2. Toda comparacion de ids pasa por el resolutor (12 ago 2026)
Manual principio 3. Ninguna comparacion literal de ids fuera de
src/resolutor.py. El gate resuelve antes de contar auto-aristas, duplicadas,
vueltas y aristas rotas. La prueba D de tests/test_aceptacion.py es el caso
positivo de esta regla.

## D.3. Las señales ordenan, nunca deciden (12 ago 2026)
Manual principio 4. Las tres señales de la aduana (similitud de texto, familia
de id, paso contra nodo) construyen una cola de lectura. Ningun umbral de
config/umbrales.json puede insertar ni bloquear un nodo por si solo: la
insercion se bloquea hasta que una PERSONA escriba un veredicto con su razon.

## D.4. Calibracion de los umbrales (12 ago 2026)
Valores de arranque: similitud de texto 0,45; familia de id 0,50; paso contra
nodo 0,55. Estan medidos sobre cinco casos plantados (gemelo, hijo, familia
parecida, vecino legitimo y nodo ajeno), NO sobre un corpus real. Se recalibran
con el primer libro de verdad, y el recalibrado se declara aqui con su fecha y
con los casos que lo movieron.

## D.5. La familia de id no conjuga verbos (12 ago 2026)
La clave de familia normaliza sufijos numericos, preposiciones, articulos,
plurales y orden de palabras. NO normaliza formas verbales:
`registrar_fuentes` y `registro_fuentes` son familias distintas para el codigo.
Limite aceptado a sabiendas: un normalizador de verbos fusionaria ids legitimos
en silencio, que es peor que el fallo que evita. Detalle y ejemplos en
docs/REGLAS_DE_ID.md.

## D.6. A los alias se les exige forma, no doctrina (12 ago 2026)
Un `ids_alias` cumple snake_case y nada mas. Un alias existe porque alguna vez
se escribio un id que hoy no se aceptaria: exigirle doctrina borraria la
memoria de los errores y romperia las cadenas del resolutor. Al id canonico se
le exige todo.

## D.7. La aduana normaliza forma, nunca doctrina (12 ago 2026)
La aduana baja el id a minusculas, le quita acentos y convierte espacios y
rayas en guion bajo. Si despues de eso el id sigue rompiendo una regla, se
rechaza. Un id maquillado hasta pasar es una decision tomada por una maquina.

## D.8. Ningun veredicto sin razon escrita (12 ago 2026)
CONTINUA, REPITE y SANO exigen razon. La razon escrita es el activo mas
reutilizable del sistema entero (manual seccion 2). Un SANO sin razon es un
nodo que entro por cansancio, y la aduana lo rechaza.

## D.9. REPITE no escribe nada (12 ago 2026)
Cuando un veredicto es REPITE, el nodo NO entra y el comando imprime la
plantilla de reparto de las seis perdidas. La aduana NO ejecuta la fusion: la
fusion se planifica en plantillas/OPERACION_DE_FUSION.md, con simulacion previa
y caso positivo, porque el veredicto no es el riesgo, la fusion lo es (manual
principio 9).

## D.10. El orden de las fuentes se comprueba a mano (12 ago 2026)
El manual pide que la fuente añadida por injerto vaya en SEGUNDO lugar
(principio 8) y manda un barrido posicional al cerrar cada libro (seccion 7.3).
El gate NO puede comprobarlo solo: no sabe cual de las fuentes de un nodo llego
por injerto. Queda como paso de mano en docs/FLUJO_DE_EXTRACCION.md fase 3.
PENDIENTE: si en el futuro el nodo registra la fecha en que cada fuente se
añadio, esta regla pasa a ser automatica y se declara aqui.

**Adjudicacion del auditor A.2 (12 ago 2026):** la pendiente se resuelve. El
campo `fuentes` del esquema deja de ser una lista de claves y pasa a una lista
de objetos `{clave, fecha}` (esquema/nodo.schema.json, fecha en formato
AAAA-MM-DD). El barrido posicional de la fase 3 de
docs/FLUJO_DE_EXTRACCION.md deja de ser un paso de mano: el gate comprueba
automaticamente, guarda `orden_fuentes`, que en todo nodo con mas de una
fuente la fecha no retrocede de una posicion a la siguiente (src/gate.py). La
aduana completa la fecha de una entrada que llega sin ella con la fecha de
insercion (src/aduana.py, `normalizar_candidato`); no reordena, porque el
orden es doctrina y una vuelta silenciosa no se puede auditar. Los dos nodos
del dataset y los ejemplos se migraron al formato nuevo el 12 ago 2026, uno
por uno a traves de la aduana de verdad. Caso positivo en
tests/test_aceptacion.py, PruebaGate.test_a2_orden_de_fuentes_por_fecha.

## D.11. Alcance del blocking (12 ago 2026)
Por defecto el candidato se mide contra TODO el dataset. El manual habla de
medir "contra su dominio y el nucleo" (seccion 3.2), pero el nucleo de esta
forja todavia no existe. Cuando el grafo crezca y el coste lo pida, se activa
`solo_dominio_y_nucleo` en config/umbrales.json y se declaran aqui, con fecha,
que dominios forman el nucleo. Hasta entonces, medir de mas es mas barato que
dejar pasar un gemelo.

**Adjudicacion del auditor A.3 (12 ago 2026):** ratificada tal cual. El nucleo
sigue sin existir y `solo_dominio_y_nucleo` sigue apagado. Cuando el dueño
abra su primer grafo de verdad, el nucleo se declara aqui con fecha y con los
dominios que lo forman; hasta entonces medir de mas sigue siendo mas barato
que dejar pasar un gemelo. Sin cambio de codigo.

## D.12. Cero guiones largos y cero guiones medios (12 ago 2026)
Hook de estilo de la casa (manual seccion 2). Vale para TODO el repo, codigo
incluido. Los archivos que tienen que nombrar esos caracteres los escriben con
escape unicode: una guarda que se perdona a si misma deja de ser una guarda.
El hook no se salta. Si falla, se corrige y se reintenta.

## D.13. Entre dos reglas fechadas que chocan, gana la mas reciente (4 sep 2026)
**Regla madre:** My-idea, decision del fundador del 19 ago 2026
(`paradas/2026-08-19-punto-brillante-DECISION.md`, punto 1), recogida en
`docs/COSECHA_2026-09.md` seccion 1.D.

Cuatro textos sellados el 12 de agosto daban por hecha una ruta que una
operacion del 14 de agosto ya habia cambiado aplicando una regla posterior. Se
paro el bucle para resolverlo, y la salida quedo escrita:

> Cuando dos textos sellados chocan, **gana el que aplico la regla mas reciente
> del fundador, y el perdedor SE CORRIGE** por correccion declarada, sin borrar.

Vale para este banco: si dos entradas fechadas se contradicen, manda la de
fecha posterior, y la anterior se tacha con su nota. Nunca se borra (manual
principio 6).

## D.14. La lista blanca es un REGISTRO DE CITAS (4 sep 2026, TANDA A, C.2)
**Regla madre:** My-idea, decision del fundador del 2 sep 2026,
`paradas/2026-09-02-opc05-bidireccionales-DECISION.md`.

Alli la guarda de bidireccionales no podia encenderse: 153 pares vivos contra
una lista blanca de dos entradas, y 83 de esos pares eran anteriores al
mergebase, o sea estado previo que la campaña no habia creado. Meterlos todos
en la lista habria sido escribir 151 excepciones **sin una sola lectura
detras**, que es justo lo que la lista blanca vino a impedir. La salida:

> La lista blanca pasa de lista a mano a **REGISTRO DE CITAS**. Cada par
> bidireccional exige un veredicto de lectura registrado CON CITA.
> **UN PAR SIN CITA ES ROJO.**

En esta forja: `config/pares_mutuos.jsonl` deja de ser pertenencia. Cada
entrada lleva `par`, `fecha`, `declarado_por`, `paso_ida`, `razon_ida`,
`paso_vuelta`, `razon_vuelta` y las dos huellas, y **el gate verifica la cita
entera**, no que el par este en la lista: campos ausentes, un paso que el nodo
ya no tiene, o dos sentidos que hoy apuntan a la misma linea son ROJO que
nombra el par. Guarda `cita_incompleta` en `src/gate.py`.

CONVENIO, y lo escribe la aduana por construccion: `paso_ida` es un paso de
`par[0]` (quien declaro) y `paso_vuelta` es un paso de `par[1]`.

## D.15. El bloque de vigencia: una lectura contra texto muerto no vale (4 sep 2026, TANDA A, C.3)
**Regla madre:** los cinco pares rancios de `OP-D-03` en My-idea, parada del
15 ago 2026 y decision del fundador del mismo dia.

Medido alli: **de los seis pares A de un acto, CINCO estaban leidos contra
texto que ya no existia**, porque las cirugias de fases anteriores habian
reescrito los nodos. Y la precision que costo una vuelta entera: **la vara que
manda es la de TEXTO, no la de fecha**. La vuelta anterior habia mirado solo
fechas y conto DOS; contando por texto eran CINCO.

En esta forja:

1. Cada linea de `bitacora/VEREDICTOS.jsonl` guarda `huella_candidato` y
   `huella_vecino`: la huella del texto que se leyo para emitirla.
2. Cada cita de `config/pares_mutuos.jsonl` guarda la huella de las dos lineas
   que cita.
3. `python forja.py rancios` recomputa las huellas contra el texto de hoy y
   clasifica: VIGENTE, RANCIO (el texto cambio), SIN HUELLA (escrito antes de
   esta regla: **incomprobable, y eso se declara en vez de darse por bueno**) y
   NODO IDO.

**UN RANCIO NO SE CITA COMO VIGENTE:** se relee con el texto de hoy, o se
declara por que sigue valiendo. Las dos cosas las hace una persona, **y por eso
esto NO pone el gate en rojo**: el gate vigila lo que es cierto o falso hoy;
esto vigila lo que fue cierto ayer y nadie ha vuelto a mirar.

## D.16. Ninguna señal devuelve cero silencioso (4 sep 2026, TANDA A, C.4)
**Regla madre:** My-idea, la señal muerta de `scripts/costuras_internas.py`,
medida en la vuelta 33 y corregida por decision del fundador el 15 ago 2026
(`paradas/2026-08-15-cableado-deprecado-y-costuras.md`, decision 2).

La señal de bloque recorria un rango que con cinco pasos quedaba VACIO y
devolvia 0,0 dijera lo que dijera el texto. Y los dos nodos de calibracion
tenian cinco pasos, porque la propia campaña los habia destejido:

> El 0,0 no era un nodo sin bloque: **ERA LA SEÑAL MUERTA.**

El remedio que el fundador escribio: por debajo del minimo la señal devuelve
**NO APLICA explicito, y ese valor REVIENTA si alguien lo compara con un
umbral**, en vez de dejarse leer como "no hay bloque".

En esta forja: `src/aduana.py` define la clase `NoAplica`, que levanta
`TypeError` en toda comparacion de orden y en `float()`. Las tres señales la
devuelven fuera de su dominio (sin texto comparable, sin piezas de familia,
sin pasos que barrer). `medir()` **declara** la señal que no aplica y **no la
hace votar**; ordenar la cola si esta permitido, porque poner en fila no es
comparar con un umbral.

## D.17. EL DEPRECADO ES ARCHIVO, NO SUPERFICIE (4 sep 2026, TANDA A)
**Regla madre:** My-idea, decision del fundador del 15 ago 2026, decision 1
opcion a, `paradas/2026-08-15-cableado-deprecado-y-costuras.md`:

> El deprecado conserva su cableado como archivo y Gate 0 deja de reciprocar
> aristas que nacen en deprecados. **Es la que menos miente: el deprecado es
> archivo, no participante.**

Las otras dos salidas se descartaron con su motivo escrito: reescribir las
listas del absorbido pierde el cableado historico que hace auditable la
fusion, y aflojar la guarda convierte la deuda en norma. Y el mecanismo que lo
hacia urgente esta medido: las 33 auto-aristas de aquel grafo eran la vista
reciproca de enlaces que el gemelo deprecado tenia hacia su superviviente, y
el simetrizador las refabricaba enteras cada vez que se limpiaban. **La sombra
vuelve mientras viva lo que la proyecta.**

En esta forja, `esquema/nodo.schema.json` gana el campo `estado`
(`vivo` o `deprecado`), y la regla se reparte asi:

| | |
|---|---|
| **conserva su texto y su cableado** | la ficha del absorbido no se toca: es lo que hace auditable la fusion |
| **sus aristas NO se reciprocan** | las que nacen en un deprecado no entran al grafo: no forman vuelta, ni duplicada, ni hueco de reciprocidad |
| **no se ofrece** | la aduana no lo propone como vecino: su material vivo ya esta en el superviviente, y mandar a leer una ficha muerta es mandar a leer dos veces |
| **su id resuelve al superviviente** | el resolutor camina la cadena de alias del deprecado hasta el nodo vivo que lo lleva en `ids_alias`. Un deprecado sin sucesor devuelve su propia ficha: existe, y decir que no seria peor |
| **ningun vivo lo nombra** | guarda `deprecado_en_superficie`: una arista viva hacia el absorbido tenia que haberse redirigido al fundir |
| **deprecar no es una linea del candidato** | un candidato que llega declarandose deprecado entra VIVO con su aviso. Deprecar es un acto de fusion, con su plantilla y su simulacion |

**LO QUE ESTA REGLA NO ES:** no es el campo `estado` de las operaciones que
My-idea jubilo el 4 sep 2026. Aquel era una AFIRMACION SOBRE TRABAJO HECHO, y
por eso su vara paso a ser el instrumento. Este es la NATURALEZA DEL PROPIO
NODO, que es dato y no afirmacion. La distincion se escribe aqui para que
nadie las confunda citando la una contra la otra.

## A.4. Adjudicacion del auditor: el MUTUO cita DOS LINEAS DISTINTAS (4 sep 2026, TANDA A, C.1)
**Precisa a A.1.** Regla madre: banco de textos **9.22** de My-idea, LA VARA EN
LOS DOS SENTIDOS:

> La vara es una relacion entre LINEAS, NO entre NODOS. Dos nodos pueden ser
> cada uno hijo del otro sin que ninguno repita al otro, porque la linea que
> uno expande no es la linea que el otro expande.
>
> **LA COMPROBACION QUE LA SEPARA DE LA DUPLICACION: si las dos direcciones
> apuntan a LA MISMA LINEA, no es esta figura: es un solape.** La figura exige
> dos lineas distintas, una en cada nodo.

La A.1 de la v0.2 exigia `ida=` y `vuelta=` pero aceptaba dos razones sobre la
misma linea, que es un solape con firma de enlace mutuo. Desde hoy el formato
es:

    ida=<n>:<razon>       n es el paso DEL CANDIDATO que el vecino despliega
    vuelta=<m>:<razon>    m es el paso DEL VECINO que el candidato despliega

y la aduana comprueba, contra los nodos de verdad, que los dos pasos existen y
que **no son la misma linea**. Si lo son, RECHAZA nombrando los dos pasos con
su texto, y remite a la vara de siempre: CONTINUA o REPITE.

Fundir un enlace mutuo legitimo es el error caro (borra dos procedimientos
para dejar un nodo con dos lineas sueltas). Blanquear un solape como enlace
mutuo es el error barato y silencioso, **y es el que esta guarda caza.**

## D.18. Un umbral se juzga contra la COLA, no contra la mediana (9 sep 2026, TANDA B)

**Regla madre:** My-idea, la recalibracion de `costuras_internas.py` del 15 ago
2026, averia (b): *el p50 de la señal nueva es 45,8, o sea que el umbral quedo
POR DEBAJO DE LA MEDIANA. Disparar deja de ser noticia.*

**Lo que esta forja añade, y lo añade porque la vara heredada NO lo habria
cazado.** Medidos contra la mediana de la poblacion que no debe disparar, los
tres umbrales de la v0.2 salian **SANOS** (0,45 contra 0,198; 0,50 contra 0,000;
0,55 contra 0,412). Y aun asi la señal `paso_contra_nodo` estaba mal puesta:
su umbral 0,55 caia **dentro del uno por ciento superior de la poblacion ajena**
(p99 0,524, maximo 0,652), que sobre 3.169 vivos son **14,3 vecinos falsos por
candidato**, unas 2.400 lecturas de ruido en un lote de 167.

> **UN UMBRAL NO SE JUZGA CONTRA LA MEDIANA DE LO QUE NO DEBE DISPARAR, SINO
> CONTRA SU COLA.** La cifra que decide es **cuantos vecinos falsos abre por
> candidato**, y se calcula multiplicando la tasa de disparo de la poblacion
> ajena por el tamaño del catalogo.
>
> **La mediana dice si el umbral es absurdo; la cola dice si es usable.**

**LO QUE OBLIGA**

| | |
|---|---|
| **1** | todo umbral publicado lleva al lado **su cola falsa por candidato**, medida sobre una poblacion ajena y multiplicada por el tamaño del catalogo vigente |
| **2** | la cola se recalcula cuando el catalogo crece de orden de magnitud: **el mismo umbral que era usable con 3.000 nodos entierra la cola con 30.000** |
| **3** | ningun umbral se mueve sin volver a publicar las tres cifras de su clase (que caza, que deja pasar, que cola abre), y la medicion se recomputa de `calibracion/MEDIDAS_CRUDAS.jsonl` |

Calibracion vigente y sus cifras: `docs/CALIBRACION_D4.md`. Los valores del
9 sep 2026 son **similitud de texto 0,35; familia de id 0,30; paso contra nodo
0,60**, medidos sobre 671 gemelos adjudicados, 800 pares de jerarquia declarada
y 4.000 ajenos del catalogo limpio de My-idea.

> **CORRECCION DECLARADA A D.4 (9 sep 2026), y el texto de D.4 queda en pie
> arriba porque una correccion que tapa lo que corrige no se puede auditar.**
> D.4 decia que los umbrales estaban medidos sobre **cinco casos plantados** y
> que se recalibrarian con el primer libro de verdad. **Ese dia llego**: la
> recalibracion esta hecha contra un catalogo de 3.169 vivos auditado par a par,
> y los tres valores cambiaron. Lo que D.4 pedia (*el recalibrado se declara
> aqui con su fecha y con los casos que lo movieron*) se cumple en
> `docs/CALIBRACION_D4.md`.

## D.19. La aduana caza duplicados; la jerarquia la caza la LECTURA (9 sep 2026, TANDA B)

**Medido, no supuesto.** Sobre el catalogo limpio, **ninguna de las tres señales
separa un par de jerarquia declarada de un par al azar**:

| señal | p50 de la JERARQUIA declarada | p50 de los AJENOS |
|---|---:|---:|
| similitud_texto | 0,213 | 0,198 |
| paso_contra_nodo | 0,439 | 0,412 |

Y no se arregla bajando umbrales: para levantar el 40 por ciento de la jerarquia
haria falta poner `paso_contra_nodo` en 0,45, y ahi la cola falsa es de **523
vecinos por candidato**. Se leeria ruido, no jerarquia.

> **UN CANDIDATO QUE ENTRA CON LA COLA VACIA NO ESTA CERTIFICADO COMO SIN MADRE:
> ESTA CERTIFICADO COMO SIN GEMELO.** La jerarquia se busca POR LECTURA, no por
> señal: cuando el candidato despliega algo que el libro ya nombro en una linea,
> el extractor busca esa madre y declara la arista, aunque ninguna señal la haya
> levantado.

**LA PRECISION QUE IMPIDE LEER ESTO MAS ANCHO DE LO QUE ES:** la clase medida es
**arista declarada**, que es mucho mas ancha que la figura del hijo (la madre que
nombra en una linea lo que el hijo despliega en siete). La mayoria de las aristas
de aquel catalogo son secuencia de proceso. **La figura estrecha SI la caza la
señal 3**: el fixture del hijo de esta casa mide 0,658, por encima del p99 de la
jerarquia general (0,644), y por eso el umbral se puso en 0,60 y no en 0,70.

Es el principio 4 del manual medido en casa propia: **las señales de superficie
ordenan, nunca deciden.**

## D.20. El barrido de estilo cubre lo que esta casa ESCRIBE, no lo que espera en la puerta (9 sep 2026, TANDA B)

**Encontrado corriendo, no pensando.** El estreno de la aduana deposito el primer
lote en `cuarentena/` y **el pre-commit se puso en rojo**: el barrido de guiones
recorria el arbol entero, entraba en la bandeja de entrada y denunciaba los
guiones largos de material AJENO que todavia esperaba juicio.

**LAS DOS AVERIAS, y la segunda es la grave:**

1. **La barata:** tener un lote depositado rompe TODOS los commits. La regla se
   vuelve imposible de cumplir mientras hay trabajo en curso, y **una regla que
   todos violan por obligacion de otras reglas enseña a violar reglas** (cosecha
   7.F, la misma que retiro el tope de lineas del reporte).
2. **LA GRAVE:** empuja a **limpiar un candidato antes de que la aduana lo mida**.
   Un candidato retocado para que el barrido calle es un candidato del que ya no
   se sabe como llego. **Eso es falsificar la medida en la puerta.**

**LA LINEA, y es exactamente la de `.gitignore`:** se barre la RAIZ de cada
bandeja, que es doctrina de esta casa y viaja en git
(`cuarentena/LEEME.md`, `fuentes/FUENTES_CANONICAS.json`), y **no** sus
subcarpetas, que son material de otro (`cuarentena/<lote>/`, `fuentes/<clave>/`).

> **SE BARRE LO QUE ESTA CASA ESCRIBE. NI UN FICHERO MAS.**

**NO BARRER LA BANDEJA NO ES INDULTAR.** La guarda `guiones` del gate sigue
mirando a cada candidato, uno a uno, **cuando pide entrar**. La puerta es su
sitio; la bandeja no. En el estreno esa guarda mordio a cuatro de los 163.

Implementado en `comun.BANDEJAS_DE_ENTRADA` y `comun._es_bandeja`, con dos
pruebas en `tests/test_aceptacion.py` (`PruebaBandejas`): una comprueba que la
raiz SI se barre y la subcarpeta no, y **su caso positivo** comprueba que el
gate sigue mordiendo el mismo guion dentro de un candidato.

## D.21. La regla 1 de ids tiene CRITERIO, y son dos listas (10 sep 2026, decision del fundador)

*Cita: decision del fundador del 10 sep 2026, sobre la cifra de
`docs/ESTRENO_DE_LA_ADUANA.md` seccion 6.2.*

La lista negra vieja tenia 37 palabras y ningun criterio salvo "lo que aparece
mas". Medida contra el catalogo auditado, **dejaba pasar 269 de 3.169 ids vivos**
y dejaba entrar `variance_analysis` y `work_breakdown_structure` enteros.

**LA DECISION NO FUE ENGORDARLA A CIEGAS NI PONER UNA PRUEBA DE IDIOMA
AUTOMATICA**, que habria sido maquinaria nueva bajo moratoria. Fue darle criterio:

| lista | que es | tamaño |
|---|---|---:|
| **NEGRA** `INGLES_CON_EQUIVALENTE` | palabra inglesa **con equivalente corriente en castellano** | **366** |
| **BLANCA** `PRESTAMOS_ASENTADOS` | **prestamo asentado** en el castellano de negocios | **33** |
| **NI UNA NI OTRA** `NOMBRES_Y_SIGLAS` | nombre propio y sigla: un apellido no tiene equivalente | **27** |

**POR QUE NO ES PURISMO, y este es el motivo tecnico:** dos grafias del mismo
concepto **parten la familia**. `retencion_clientes` y `customer_retention`
tienen clave de familia **disjunta**, asi que la señal 2 no los ve juntos **y
entran los dos**. Un solo idioma en los ids es lo que deja trabajar a la señal.

**LO MEDIDO, sobre los 3.169 vivos:**

| | vieja | nueva |
|---|---:|---:|
| ids que la lista caza | 105 | **497** |
| ids que la blanca indulta | 0 | **138** |

**LOS 269 IDS DEL CATALOGO SON COSA JUZGADA.** Esta regla rige lo que se
ESCRIBE de ahora en adelante. **No se reabre un id ya adjudicado por una lista
que llego despues**, y eso vale tambien si el catalogo entrase algun dia entero.

**PRUEBAS** (`PruebaReglasDeId` en `tests/test_aceptacion.py`): la negra tumba
`customer_retention_tactics` **nombrando las dos piezas**; el **caso positivo**
comprueba que `plan_marketing_contenidos`, `medir_benchmarking_costes`,
`valorar_startup_temprana` y `aplicar_lean_produccion` pasan limpios, porque una
regla que tumba todo es un candado; una tercera comprueba que `deming`,
`shewhart` y `osha` **no se cazan**; y una cuarta que **las dos listas no se
solapan**, que es la comprobacion de que la regla sigue teniendo criterio. El
modulo tambien lo verifica al importarse.

Ampliar cualquiera de las dos listas es **correccion declarada con fecha**.

## D.22. La regla 2 prohibe la VERSION, no el numero (10 sep 2026, decision del fundador)

*Cita: decision del fundador del 10 sep 2026, sobre los 14 ejemplares de
`docs/ESTRENO_DE_LA_ADUANA.md` seccion 6.2.*

La regla vieja prohibia **todo** numero al final. **Contado sobre el catalogo:**
de los 48 ids vivos que acaban en numero, **44 llevan un numero de una cifra y
son versiones**, y los **4** restantes son **denominaciones**:

    familia_normas_iso_9000       cumplimiento_ftc_rule_436
    canales_de_traccion_19        riesgo_split_51_49

> **NADIE HACE UNA VERSION 436.**

Ese es el corte, y esta contado: **48 de 48**. `TOPE_DE_VERSION = 9`.

**Y EL NUMERO EN MEDIO NUNCA FUE VERSION.** Los **14 vivos** que lo llevan son
los ejemplares de la regla, y los catorce son denominaciones:
`los_14_puntos_deming`, `benchmarking_7_pasos_juran`, `iso_31000_gestion_riesgo`,
`regla_50_por_ciento`, `modelo_lubin_esty_4_etapas`.

**LA VERSION CUYA BASE YA VIVE SE CAZA DOS VECES, y la segunda no es esta
regla.** `familia()` normaliza los digitos finales, asi que `accion_correctiva_2`
y `accion_correctiva` tienen la **misma clave de familia entera**: la señal 2 los
levanta como vecinos aunque la regla 2 los dejara pasar. **De los 48, 39 tienen
su base viva en el grafo.** La puerta y la cola dicen lo mismo por caminos
distintos, y por eso acotar la regla no abre un agujero.

**POR ESO NO HIZO FALTA MAQUINARIA:** la regla 2 sigue siendo una regla de FORMA
PURA, sin acceso al grafo. Se penso darle el resolutor para comprobar si la base
existe, y **se descarto**: la señal ya lo hacia.

**PRUEBAS:** caen `accion_correctiva_2`, `consejo_calidad_3`, `cultura_justa_9`;
**caso positivo**, pasan `familia_normas_iso_9000`, `canales_traccion_19`,
`riesgo_split_51_49` y los tres de numero en medio; y una prueba mas comprueba
que la clave de familia de `accion_correctiva_2` y la de `accion_correctiva` son
**la misma**, con similitud **1,0**, con su propio caso positivo de dos ids que
**no** comparten familia.

## D.23. La aduana NO se relaja: el extractor aprende las reglas antes de escribir el primer id (10 sep 2026, decision del fundador)

*Cita: decision del fundador del 10 sep 2026, sobre la decision 7.3 de
`docs/ESTRENO_DE_LA_ADUANA.md`.*

El estreno midio que **tres de cada diez** candidatos escritos con la mano de
aquella campaña caerian en la puerta, y con las reglas nuevas son **cuatro de
cada diez**. Habia dos salidas y el fundador eligio la que cuesta antes:

> **LAS REGLAS NO BAJAN. EL EXTRACTOR APRENDE.**

**LO QUE ESTO OBLIGA, y es lo que lo convierte en regla y no en deseo:**

1. `docs/loop/EXTRACTOR.md` lleva las reglas de id **con sus dos listas y sus
   ejemplares**, no un enlace a otro documento.
2. **CADA CANDIDATO PASA POR LA ADUANA EN EL MISMO ACTO EN QUE SE ESCRIBE**,
   antes de darlo por escrito. El que cae **se corrige y se reintenta**. Nada se
   publica sin haber pasado la aduana.
3. Un lote no se da por cerrado con candidatos que el propio extractor sabe que
   caerian.

**EL MOTIVO:** un id mal puesto no cuesta un rechazo, cuesta **una arista**. Y
descubrirlo candidato a candidato al final del lote es lo caro. **La correccion
vale mas barata en el mismo minuto en que se escribio.**

## D.24. El mundo 11 entra POR LIBROS, uno por lote (10 sep 2026, decision del fundador)

*Cita: decision del fundador del 10 sep 2026, sobre la cifra de
`docs/ESTRENO_DE_LA_ADUANA.md` seccion 5: un lote de 163 cuesta unos 520
veredictos en regimen.*

**UN LIBRO POR LOTE. NO ENTRA EL MUNDO ENTERO.** Y el orden esta escrito:

| | libro | capitulos |
|---|---|---:|
| **LOTE 1, de calibracion** | **`onu_consumidor`** | **4** |
| 2 | `smart_who` | 7 |
| 3 | `zhuo_manager` | 12 |
| 4 | `scott_radical_candor` | 15 |
| 5 en adelante | el orden del `MANIFIESTO.md` del mundo 11 | |
| **el ultimo** | **`mundo_10_reservado`** (Gerber cap. 17) | **1** |

**POR QUE EL DE MENOS CAPITULOS PRIMERO:** el primer lote no se hace para meter
nodos, **se hace para medir el instrumento con trabajo de verdad delante**.
Cuatro capitulos caben en pocas vueltas, y si algo esta mal calibrado se
descubre barato. **Un lote de calibracion grande no calibra: solo cuesta mas.**

**Y EL ORDEN IMPORTA POR UNA RAZON MEDIDA, no por gusto:** el primero que entra
cambia lo que el segundo mide (`EXTRACTOR.md` seccion 12). Con el grafo casi
vacio la cola es corta; crece con el grafo.

**EL MUNDO 10 VA AL FINAL** porque es un solo capitulo apartado a proposito
(`docs/ESTRENO_DE_LA_ADUANA.md` seccion 1.1): entra cuando el grafo ya sabe con
quien compararlo.

## D.25. La cuarentena VIAJA en el repo (10 sep 2026, decision del fundador)

*Cita: decision del fundador del 10 sep 2026, sobre la decision abierta al final
de `cuarentena/LEEME.md`.*

`.gitignore` pierde su linea de la cuarentena. **Los lotes viajan.**

**EL MOTIVO ES LA RUTA QUE PROMETE PRUEBA ES CIFRA** (cosecha 7.C): un informe
que dice *"de estos 163, 49 caerian"* **solo se puede comprobar si los 163 estan
en el arbol**. Un lote que no viaja convierte cada informe en una firma en vez
de una prueba. Pesan, y se aceptan.

**`fuentes/<clave>/` SIGUE FUERA:** es texto con derechos de otro autor, y esa
es una razon distinta que la decision no toca.

**LA UNICA EXCEPCION, y es estrecha:** `cuarentena/_derivadas/` guarda copias
que hace la maquina para medir, entre ellas el catalogo de referencia ENTERO
(5,6 MB, 3.157 nodos). Eso ya vive en su repo, en su tag, y duplicarlo aqui no
prueba nada que el tag no pruebe mejor.

> ### CORRECCION DECLARADA A D.20, misma fecha
>
> **D.20 justificaba la linea del barrido diciendo que era "exactamente la que
> traza `.gitignore`". Esa frase deja de ser cierta hoy**, porque `.gitignore`
> movio su linea y el barrido no.
>
> **LA LINEA DEL BARRIDO NO SE MUEVE, y su razon verdadera nunca fue la
> coincidencia: era SE BARRE LO QUE ESTA CASA ESCRIBE.** Un candidato en
> cuarentena es material ajeno esperando juicio **tanto si viaja en git como si
> no**, y barrerlo seguiria empujando a limpiarlo antes de que la aduana lo
> mida, que es falsificar la medida en la puerta.
>
> La coincidencia con `.gitignore` era **incidental**, y hoy se ve que lo era.
> El texto viejo de D.20 no se borra: se lee con esta correccion al lado.

## D.26. LA INSERCION ES UNA AUTORIZACION DEL FUNDADOR, NO UN DEFAULT (10 sep 2026, decision del fundador)

*Cita: decision del fundador del 10 sep 2026, sobre la friccion que el reporte
del PASO 3 dejo señalada: el encargo de la vuelta 1 tuvo que contradecir por
escrito al prompt permanente del arnes.*

**EL SINTOMA.** El prompt permanente del extractor decia SIEMPRE que se inserta
con `python forja.py insertar`. Un encargo que pedia cero inserciones no tenia
mas remedio que contradecirlo, en voz alta y por escrito. **Y dos documentos que
se contradicen enseñan a elegir cual obedecer**, que es exactamente la enfermedad
que la moratoria y la congelacion de varas vinieron a curar.

**LA CAUSA, que no era el texto sino el default.** Insertar en el grafo es la
unica accion de esta casa que **no se puede deshacer leyendo**: un nodo que entro
mal deja arista, censo, veredicto y huella. Que eso fuera lo que pasa **si nadie
dice nada** era el fallo.

> **EL ARNES ARRANCA SIN PERMISO PARA INSERTAR. El permiso se da al lanzarlo, y
> se da a mano.**

**COMO QUEDA:** `orquestador_forja.sh` gana `MODO_INSERCION`.

| valor | que hace |
|---|---|
| **`cuarentena`** | **EL DEFAULT.** El prompt del extractor le prohibe insertar y le manda dejar cada candidato en `cuarentena/<libro>/<id>.json` con su informe en seco |
| `insertar` | el prompt le autoriza: `forja.py insertar`, un candidato por vez, con su veredicto escrito si la aduana bloquea |
| cualquier otro | **DETIENE EL ARNES antes de gastar un turno** |

**UN MODO MAL ESCRITO NO CAE AL DEFAULT, y esto no es rigor por gusto:** caer al
default seria benigno aqui (cuarentena es lo prudente), pero enseñaria que la
variable se puede escribir mal sin consecuencia. **Adivinar una autorizacion es
justo lo que esta variable existe para impedir**, y una guarda que perdona en el
caso facil no guarda en el dificil.

**Y EL ARNES YA NO SE CONTRADICE CON NINGUN ENCARGO:** dice UNA sola cosa, y la
dice el fundador al lanzarlo. La advertencia de contradiccion se retiro de
`docs/loop/PROMPT_SIGUIENTE.md` porque **ya no hay contradiccion que advertir**.

### D.26.1. El freno de rama, del mismo dia y por la misma razon

El arnes usa `$RAMA` solo para tirar y empujar: **no hace checkout**. Lanzarlo
desde otra rama trabajaria sobre la rama en la que estas y empujaria a otra. Ese
riesgo iba escrito en el reporte del PASO 3 como friccion; hoy es una guarda.

**Comprueba al arrancar que la rama activa es `$RAMA` y, si no, SE DETIENE
NOMBRANDO LAS DOS**, mas el comando para salir. Nombrar las dos no es adorno:
"rama equivocada" sin decir cuales obliga a ir a mirar, y quien lanza un arnes a
las tres de la mañana no va a mirar.

**PRUEBAS** (`tests/prueba_arnes.sh`, escenarios 8 a 11, con el claude falso, que
ahora guarda el prompt recibido para que se pueda afirmar SOBRE EL y no sobre sus
efectos, porque el efecto de "no insertes" es que no pasa nada y eso es
indistinguible de un turno vago):

- **8**, nadie pasa `MODO_INSERCION`: el prompt prohibe insertar, nombra
  `cuarentena/<libro>/`, manda el informe en seco, y **no** autoriza.
- **9**, el CASO POSITIVO: con `MODO_INSERCION=insertar` el MISMO arnes SI
  autoriza y manda uno por vez. Sin este, el 8 solo probaria que el prompt dice
  siempre lo mismo.
- **10**, `MODO_INSERCION=insertarr`: se detiene antes de arrancar, nombra el
  valor recibido, nombra los dos validos, dice la regla, y **no gasta ni un
  turno**.
- **11**, el freno de rama: desde `otra_rama` con `RAMA=bucle` se detiene
  nombrando las dos y dando el comando; **y su CASO POSITIVO**, el mismo banco de
  vuelta en su rama, arranca y corre la vuelta.

Once escenarios, **62 comprobaciones en verde**.

### D.26.2. Correccion declarada a D.21: la lista blanca pierde dos y gana una

*Misma fecha. El fundador adjudica las tres piezas que el reporte del PASO 3
dejo señaladas como discutibles.*

| pieza | va a | razon del fundador |
|---|---|---|
| `equity` | **NEGRA** | *capital* o *participacion* son equivalentes corrientes |
| `feedback` | **NEGRA** | *retroalimentacion* es equivalente corriente |
| `engagement` | **BLANCA** | *compromiso* e *interaccion* **no capturan el sentido de marketing** |

**Y AQUI HAY UN ERROR MIO QUE HAY QUE DECLARAR, porque la decision se tomo
encima de el.** El reporte del PASO 3 presento las tres como piezas de la lista
BLANCA que alguien razonable discutiria. **`equity` y `feedback` si lo estaban;
`engagement` NO: estaba en la NEGRA.**

Asi que para `engagement` la instruccion *"se queda"* **no fue una confirmacion
sino un movimiento**, y se ejecuto como movimiento **por su razon escrita**, que
es una razon de lista blanca: traducirlo fabricaria un termino que no dice lo
mismo. La otra lectura, dejarlo donde estaba, contradiria la razon con la que se
decidio.

**Lista negra: 367. Lista blanca: 32.** Sin solape, comprobado al importar el
modulo y en `PruebaReglasDeId`.

## D.27. LA PRUEBA DEL INVENTARIO (10 sep 2026, RATIFICADA POR EL FUNDADOR)

*Nace en la vuelta 1 del bucle: la escribio el extractor en `docs/loop/REPORTE.md`
2.A.2 y la declaro suya sin esconderlo (*"la prueba del inventario es mia, no de
la casa. No la he leido en el manual ni en el banco"*). El auditor la adjudico en
`ACTA_AUDITOR.md` 3.1 por extension de una regla escrita, con tres restricciones,
y dejo dicho que **el banco es sede de Alexis** y que meterla aqui con numero
propio no era suyo. **El fundador la ratifica hoy, con estas mismas tres
restricciones, y le da numero.**

**CUELGA DE `NOMBRAR NO ES PROCEDIMENTAR`, y no es una regla independiente:**

> **NOMBRAR NO ES PROCEDIMENTAR.** Una linea solo cuenta como procedimiento
> propio **si trae procedimiento propio, y no solo el nombre de otro**
> (`EXTRACTOR.md` seccion 9; `P.5.1` de My-idea, congelada el 3 sep 2026 tras
> cuatro caidas de clase en dos tandas; manual seccion 4).

> **La prueba de que una linea es procedimiento es que EXISTE QUIEN LO EJECUTA**
> (manual seccion 4, citado literal por `EXTRACTOR.md` seccion 9).

**LA PRUEBA, que es la cara POSITIVA de esa vara y por eso hacia falta:**

> Una linea normativa se vuelve procedimentable **cuando el libro pone su propio
> inventario**: los medios, las etapas o los objetos que hay que revisar,
> **nombrados uno a uno por el texto**. Entonces escribir los pasos es
> **transcribir** ese inventario en imperativo, y no se inventa nada.
>
> **Cuando el libro solo pone el mandato y un adjetivo de adecuacion** (*medidas
> apropiadas*, *politicas adecuadas*, *requisitos razonables*, *plazo
> prudencial*), **cualquier paso que se escriba lo escribe el extractor**, y un
> nodo cuyos pasos invento el extractor no es del libro.

**EL INVENTARIO PROPIO DEL LIBRO ES EL "PROCEDIMIENTO PROPIO" DE LA FRASE
MADRE.** Cuando el texto solo nombra el procedimiento de otro (parrafo 22 de
`cap_02`, que remite a la resolucion 35/63 de 5 diciembre 1980), estamos en el
caso literal de *solo el nombre de otro*. **No hace falta doctrina nueva para
leer eso: hace falta leer la frase entera.**

### Las tres restricciones, literales, y sin ellas esto no se ratifica

**Sin restriccion esto ensancharia la vara, y ensanchar una vara es parada**
(`AUDITOR_FORJA.md` 6.3).

1. **EL INVENTARIO QUE CUENTA ES DE MEDIOS, ETAPAS U OBJETOS DE TRABAJO.** Un
   inventario de **METAS** (parrafo 20) o de **FINES** (los cuatro desenlaces del
   parrafo 19 de `cap_01`) **no cuenta**: nombrar adonde hay que llegar sigue
   siendo nombrar.
2. **EL ADJETIVO DE ADECUACION EN EL SITIO DEL CRITERIO TUMBA, AUNQUE HAYA
   INVENTARIO.** Es lo que deja fuera el parrafo 23 con sus cuatro requisitos
   (durabilidad, utilidad, fiabilidad, aptitud) bajo el criterio *requisitos
   razonables*.
3. **ESTO NO MUEVE LA VARA DE CONTINUA CONTRA REPITE** (`AUDITOR_FORJA.md`
   seccion 6). Es la vara de **que es un nodo**, y la de adjudicar un par se
   queda donde estaba.

### Los ejemplares, que son de casa y estan medidos

| parrafo | inventario | fallo |
|---|---|---|
| 21, segunda mitad | adulteracion de alimentos, afirmaciones falsas o capciosas, fraudes en servicios | **PROCEDIMIENTO** |
| 26 | contratos uniformes que favorecen a una parte, no inclusion de derechos esenciales, condiciones excesivamente estrictas de credito | **PROCEDIMIENTO**: tres abusos nombrados son una lista que alguien recorre contra un contrato |
| 20 | METAS, no medios | **POSTURA**, por la restriccion 1 |
| 22 | remite a otro libro | **POSTURA**, y el ejemplar limpio de NOMBRAR NO ES PROCEDIMENTAR |
| 23 | cuatro requisitos, pero el criterio es *requisitos razonables* | **POSTURA**, por la restriccion 2 |
| 19 de `cap_01` | cuatro desenlaces: retirar y reemplazar, modificar, sustituir, compensar | **POSTURA**: son FINES, por la restriccion 1 |

**LAS DOS CARAS DE LA MISMA VARA:** el adjetivo de adecuacion delata la postura,
**el inventario propio delata el procedimiento.**

**NINGUNA VUELTA ESTRECHA NI ENSANCHA ESTA PRUEBA SIN CORRECCION DECLARADA DEL
FUNDADOR.** Si una lectura pide moverla, **eso es parada y se trae**.

## D.28. `PARA_ALEXIS.md` ES DEL AUDITOR Y SOLO DEL AUDITOR (10 sep 2026, RATIFICADA POR EL FUNDADOR)

*El extractor de la vuelta 1 trajo declarada una contradiccion real entre su
encargo y sus reglas permanentes, sin haberla sufrido, y acerto en las dos
mitades: en no traerla como parada sobre un supuesto que no ocurrio, y en decir
que habria seguido `EXTRACTOR.md`. El auditor la resolvio en `ACTA_AUDITOR.md`
3.5. **El fundador ratifica hoy la sede.***

> **`docs/loop/PARA_ALEXIS.md` LO ESCRIBE EL AUDITOR, Y SOLO EL.**
>
> **El extractor que quiera parar lo declara en SU REPORTE**, con su motivo y su
> estado, y se detiene. **El auditor lo recoge y lo enruta.**

**EL MOTIVO NO ES JERARQUIA, ES QUE UNA PARADA ES UN JUICIO.** Quien la escribe
en la sede que el fundador lee esta afirmando que el bucle no puede seguir, y esa
afirmacion se verifica antes de llegar ahi. El auditor la verifica; por eso pasa
por el.

**Y LA REGLA GENERAL QUE ESTE CASO DEJA ESCRITA, que vale mas que el caso:**

> **UN ENCARGO ASIGNA TRABAJO; NO MUEVE UNA SEDE.** La cabecera de
> `EXTRACTOR.md` ya lo decia: *"Estas reglas valen SIEMPRE, ademas de lo que diga
> el encargo."*

**D.13 NO RESCATA AL ENCARGO POR SER MAS RECIENTE**, y conviene decir por que
para que nadie lo intente: **una formula arrastrada en una plantilla no es una
regla fechada.** D.13 arbitra entre reglas que alguien escribio como reglas, no
entre una regla y un descuido de copia.

**LA CORRECCION YA ESTA HECHA Y NO SE REHACE:** el `PROMPT_SIGUIENTE.md` de la
vuelta 2 lleva la formula vigente desde que el auditor lo escribio. **El texto
viejo no se borra:** vive en el `PROMPT_SIGUIENTE.md` de la vuelta 1, commiteado
en `ea6c9f4` y antes, y citado en el acta.

## D.29. LA ARISTA QUE LA SEÑAL NO LEVANTA SE DECLARA POR LECTURA, EN EL ACTO DE LA INSERCION (10 sep 2026, RATIFICADA POR EL FUNDADOR)

*La vuelta 1 encontro el primer caso real de lo que D.19 predijo: una arista de
jerarquia que ninguna señal levanta. **El fundador ratifica el remedio y NO mueve
el umbral.***

**EL CASO, medido:**

    formular_codigo_comercializacion_empresarial   (parrafo 31, MADRE)
        baja a
    verificar_afirmaciones_ambientales_publicidad  (parrafo 30, HIJO)

**En el sentido en que el hijo llegara de candidato, `paso_contra_nodo` mide
`0,572289` y el umbral esta en `0,60`: NO va a levantar a nadie.**

**NO SE TOCA EL UMBRAL, y el motivo esta medido, no supuesto.** El acta reprodujo
las tres cifras que decidirian lo contrario:

- el fixture del HIJO de esta casa mide **`0,657718` EN LOS DOS SENTIDOS**, que
  redondea a los **0,658** que `CALIBRACION_D4.md` publica: **la cifra publicada
  no esta contradicha, esta reproducida**;
- la justificacion escrita del 0,60 sigue en pie: a 0,70 ese hijo entraria sin
  arista declarada;
- **este par no es un contraejemplo de la figura estrecha**: es una dependencia
  de proceso, o sea del **97 por ciento** de aristas declaradas que la casa YA
  tiene escrito que la señal 3 no caza.

> **HAY UN HUECO DE DECLARACION, NO UNA CONTRADICCION.** Y el remedio ya estaba
> escrito: **la aduana caza duplicados; la jerarquia la caza la LECTURA** (D.19).

**LO QUE LA RATIFICACION AÑADE ES EL CUANDO, que es lo que faltaba:**

> **LA ARISTA SE DECLARA EN EL ACTO DE LA INSERCION**, con su veredicto
> (`docs/FLUJO_DE_EXTRACCION.md` fase 2, paso 4), **y la madre entra primero**.
>
> **UNA ARISTA QUE SOLO VIVE EN LA PROSA DE UN REPORTE SE PIERDE**, porque el
> reporte se reescribe cada vuelta. Mientras el candidato espera en cuarentena,
> la arista vive **en un bloque propio y titulado del reporte**, no suelta en un
> parrafo.

**Y LOS JSON EN CUARENTENA SIGUEN CON `nodos_previos` Y `nodos_siguientes`
VACIOS**, que es lo correcto: una arista se cablea contra ids que ya viven, y en
cuarentena todavia no vive ninguno.

**LA ASIMETRIA DE LA SEÑAL 3 QUEDA ESCRITA COMO DATO, sin remedio y sin
maquinaria:** `difflib.SequenceMatcher(a, b).ratio()` no es simetrico, y el mismo
par mide `0,602410` en un sentido y `0,572289` en el otro. **No se toca el
`ratio`, no se toca la señal, no se rehace la calibracion.** Se sabe, y por eso
la lectura no delega en la señal.

## D.30. LA ADUANA CAZA LA FORMA; LA FIDELIDAD LA CAZA OTRO LECTOR (10 sep 2026, RATIFICADA POR EL FUNDADOR)

*Es la leccion medida del lote 1, y la mas cara que ha comprado esta casa: costo
una vuelta entera de reparacion. La ratifica el fundador el mismo dia en que
autoriza la primera insercion real.*

> **NINGUNA GUARDA DE ESTA CASA VE UN PASO QUE EL EXTRACTOR ESCRIBIO Y EL LIBRO
> NO DICE.**

**LA CIFRA, contada parrafo a parrafo y no estimada: 13 de los 36 pasos del lote
1, el 36 por ciento.** Cuatro de los seis candidatos llevaban al menos uno. Se
resolvieron con 4 pasos retirados enteros y 9 clausulas reescritas, cada una con
su fichero, su linea y la frase que si esta en el texto. El lote paso de 36 a 32
pasos.

**Y LA CIFRA QUE LA CONVIERTE EN REGLA: la aduana dio 6 de 6 verdes ANTES y
DESPUES de esa correccion.** El mismo informe, el mismo saldo, y trece defectos
en medio.

**NO ES QUE LA PUERTA ESTUVIERA ABIERTA, y esto se comprobo mordiendola a
proposito** (ACTA 2 seccion 1.5): mutando la fuente de un candidato y vaciando
los pasos de otro, el mismo informe da **4 entrarian y 2 caerian**, con las dos
guardas nombradas por separado. **Las doce guardas funcionan. Es que miden otra
cosa.**

| lo que la aduana SI ve | lo que NO ve |
|---|---|
| el esquema, las reglas de id, la fuente canonica, el orden de las fuentes por fecha, las aristas rotas o duplicadas, la auto arista, la vuelta no declarada, la cita incompleta, el deprecado en superficie, los guiones | **si un paso esta en el libro** |

**EL MOTIVO, y por eso ninguna guarda futura lo arregla: la aduana no tiene el
libro delante.** Compara el candidato con el grafo y consigo mismo. **El texto
fuente no es una entrada suya**, y no puede serlo sin volverla otra cosa.

### La regla que esto obliga

> **LA RELECTURA DE FIDELIDAD CONTRA EL TEXTO FUENTE ES OBLIGATORIA EN TODA
> VUELTA DEL EXTRACTOR, ANTES DE CUALQUIER INSERCION.**
>
> **NINGUNA MEDIDA DE LA ADUANA LA SUSTITUYE.** Un informe verde certifica que la
> ficha esta bien construida, **no que sus pasos sean del libro.**

**COMO SE HACE, y es barato si se hace en su sitio:** cada paso se marca contra
su parrafo como **TRANSCRIPCION** (el libro pone el medio, la etapa o el objeto) o
como **PUENTE** (lo escribio el extractor). **Cada puente se retira o se reescribe,
citando el parrafo que NO lo dice.** Un puente no se queda callado dentro de un
nodo.

**EN EL ACTO DE ESCRIBIR CADA CANDIDATO, NO EN UNA VUELTA POSTERIOR.** El lote 1
gasto **una vuelta entera** en reparar trece puentes de seis candidatos; aplicada
al escribir, la vuelta 1 habria salido con 32 pasos y sin deuda. Es la misma
forma de D.23 para las reglas de id: **la correccion vale mas barata en el minuto
en que se escribio.**

### El reparto, que es la lectura util y dice donde mirar

| parrafo | inventario | puentes |
|---|---|---:|
| 29, cinco medios nombrados | rico | **0 por ciento** |
| 32, una frase | pobre | **83 por ciento** |

> **UN PARRAFO POBRE NO PRODUCE UN NODO POBRE: PRODUCE UN NODO INVENTADO.**

**El puente sube cuando baja el inventario del parrafo.** Es la advertencia
practica de `D.27`: cuando el inventario del libro es delgado, la tentacion de
completarlo no se nota mientras se escribe, **y ninguna guarda la nota despues.**

### Su relacion con las otras dos varas, para que nadie las confunda

| vara | pregunta | quien la aplica |
|---|---|---|
| **`D.27`**, la prueba del inventario | **¿esto es un nodo?** | el extractor, al decidir que extraer |
| **`D.30`**, la fidelidad | **¿este paso lo dice el libro?** | el extractor, al escribir, con el parrafo delante |
| **`AUDITOR_FORJA.md` 6**, continua contra repite | **¿este nodo continua a otro o lo repite?** | quien inserta, con el grafo delante |

**Las tres son distintas y ninguna cubre a otra.** Un nodo puede pasar D.27 (el
libro pone su inventario), fallar D.30 (el extractor le añadio un destinatario que
el libro no nombra) y no tener ningun vecino que adjudicar. **Fue exactamente el
caso de cuatro de los seis candidatos del lote 1.**

**NINGUNA VUELTA SUSTITUYE ESTA RELECTURA POR UNA MEDIDA.** Si alguien propone
una guarda que la automatice, eso es maquinaria y cae bajo la moratoria: **el
texto fuente no esta en el repo** (`.gitignore`, bandeja (a)), y una guarda que no
tiene el libro no puede juzgar fidelidad al libro.
