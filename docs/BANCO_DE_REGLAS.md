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

> ### CORRECCION DECLARADA, 11 sep 2026: ver `D.39`
>
> **El default se invierte: pasa a `insertar`.** Esta regla tenia razon el dia que
> se escribio, porque **el instrumento no se habia medido nunca**. Ya se ha medido
> seis veces, y `D.39` pone la condicion que la sustituye: **un lote CERRADO en
> extraccion cuyo informe certifique el acta entra sin firma nueva.**
>
> **Lo que sigue vivo de esta regla, y por eso no se borra:** lo que **no** esta
> cerrado **no** entra, y un modo mal escrito sigue deteniendo el arnes.

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

## D.31. UN CANDIDATO INSERTADO SE ARCHIVA EN `_insertados` CON SU COMMIT DE INSERCION (10 sep 2026, decision del fundador)

*Cita: decision del fundador del 10 sep 2026, al cerrar el lote 1 y sacar sus
seis candidatos de la bandeja.*

> **NADA SE BORRA: EL FICHERO DE CUARENTENA ES EL REGISTRO DE COMO ENTRO.**

    cuarentena/<libro>/<id>.json          ->   candidato, espera juicio
    cuarentena/_insertados/<libro>/<id>.json  ->  ya vive en el grafo

**POR QUE NO SE BORRA.** El nodo que vive en `dataset/nodos.jsonl` es el nodo
**despues** de la aduana: normalizado, con sus aristas cableadas y resueltas. El
fichero de cuarentena es el nodo **antes**. La diferencia entre los dos es lo
unico que dice **que le hizo la puerta al entrar**, y ese dato no se puede
reconstruir desde ningun otro sitio. **Vale mas cuanto mas viejo es.**

**POR QUE SE MUEVE, EN VEZ DE DEJARLO DONDE ESTABA.** Porque deja de ser un
candidato, y el informe lo contaba. Un candidato insertado que sigue en la
bandeja da `CAERIA: el id ya vive en el grafo`, que es cierto y es **la mentira
mas fea posible sobre un lote**: un lote recien insertado se leeria como un lote
entero rechazado, y la cifra que el fundador lee antes de autorizar la siguiente
insercion estaria envenenada por sus propios aciertos.

**Y CON SU COMMIT DE INSERCION.** Un `LEEME.md` en la carpeta del lote archivado
nombra cada candidato con **el commit que lo metio** y su veredicto. Sin esa
linea, saber cuando entro un nodo obliga a buscar en el historico de un fichero
que ya no cambia.

| | |
|---|---|
| **el archivo VIAJA en git** | es registro, no material de entrada. `.gitignore` no lo toca (`D.25`) |
| **el barrido de guiones NO entra** | sigue colgando de `cuarentena/`, que es bandeja: se barre lo que esta casa escribe (`D.20`) |
| **el `LEEME.md` del lote SI se barre** | lo escribe esta casa |

**LA MARCA ES EL SEGMENTO DE RUTA, NO EL NOMBRE DEL FICHERO.** `esta_archivado()`
parte la ruta y busca el segmento `_insertados`: un fichero que solo **se llame**
asi no esta archivado. Con su caso positivo en `PruebaArchivoDeInsertados`.

**Y EL RECORTE SE DECLARA, NUNCA SE APLICA EN SILENCIO** (la regla de siempre en
esta casa): un informe sobre un lote mezclado imprime `archivados, NO contados`
con su cifra, y un informe sobre una carpeta entera archivada lo dice y no
imprime saldo. **No contar en silencio es lo mismo que contar mal.**

**LO QUE NO SE HACE CON UN ARCHIVADO:** no se reinserta (la aduana lo rechaza por
`el id ya vive en el grafo`, y hace bien) y **no se edita**. Un registro que se
retoca deja de ser un registro.

**Cuatro pruebas** (`PruebaArchivoDeInsertados`): la carpeta archivada no se
cuenta; **su caso positivo**, la misma carpeta sin archivar si se cuenta, porque
si no la primera solo probaria que el informe calla; un lote mezclado declara
cuantos no conto; y la marca es el segmento y no el nombre.

## D.32. EL CIERRE DE UN LOTE ABRE EL SIGUIENTE (10 sep 2026, decision del fundador)

*Cita: decision del fundador del 10 sep 2026, al llenar la bandeja entera y
levantar la parada de la vuelta 3.*

> **EL ACTA QUE CIERRA UN LOTE ESCRIBE EL ENCARGO DEL SIGUIENTE, SIN PARADA ENTRE
> MEDIAS**, siempre que sus **dos condiciones de apertura** esten medidas en
> verde. **La excepcion es una sola: que el fundador tenga una decision
> pendiente.**

**LAS DOS CONDICIONES DE APERTURA, que son las que la vuelta 3 midio en rojo:**

1. **el material esta en `fuentes/<clave>/`**, con sus capitulos;
2. **la clave esta en `fuentes/FUENTES_CANONICAS.json`**, con su ficha.

**Desde el 10 sep 2026 las dos estan en verde PARA LOS DIEZ LOTES QUE QUEDAN**
(`docs/BANDEJA_DE_ENTRADA.md`, `docs/loop/ORDEN_DE_LOTES.md`), asi que el motivo
que paro la vuelta 3 no se puede repetir.

### Por que esto es una regla y no una comodidad

**El bucle gasto una vuelta entera, dos asientos y su coste, en descubrir que no
tenia libro.** El extractor abrio el repo, busco `fuentes/smart_who/`, escribio
que no estaba y se detuvo; el auditor lo verifico y escribio la parada. **Todo
correcto, y todo para producir una frase que se sabia de antemano.**

> **UNA PARADA QUE SE PODIA PREVER NO ES UNA PARADA: ES UNA VUELTA GASTADA EN
> AVERIGUAR ALGO QUE YA ESTABA ESCRITO.**

**Y EL ORDEN NO SE INVENTA:** el lote siguiente es el que dice
`docs/loop/ORDEN_DE_LOTES.md`, y su volumen por vuelta sale de la metrica
`PASOS INVENTADOS POR CAPITULO` del acta que cierra (`AUDITOR_FORJA.md` seccion
8). **El acta no elige libro: lee cual toca.**

### Lo que el acta de cierre tiene que hacer, en orden

1. **Medir las dos condiciones del lote siguiente** y publicar las dos medidas.
   **Medidas, no supuestas:** `ls` de la carpeta y la clave leida de la tabla.
2. **Si las dos estan en verde: escribir `docs/loop/PROMPT_SIGUIENTE.md`** con el
   encargo del lote siguiente, su volumen por vuelta y sus tareas. **No escribe
   `PARA_ALEXIS.md`.**
3. **Si alguna esta en rojo: entonces si es parada**, con su medida delante.
4. **Y si el fundador tiene una decision pendiente, tambien es parada**, aunque
   las dos condiciones esten en verde.

### LA INSERCION VA POR OTRO CAMINO, Y NO BLOQUEA

**Un lote cerrado y SIN INSERTAR no detiene la extraccion del siguiente.** Son dos
cosas distintas desde `D.26`:

| |  |
|---|---|
| **extraer** | lo hace el bucle, a cuarentena, en `MODO_INSERCION=cuarentena` |
| **insertar** | **es una autorizacion del fundador**, que se pide con el informe del lote delante |

**El acta pide la autorizacion de insercion del lote que cierra Y ABRE la
extraccion del siguiente, en el mismo documento.** Que el fundador tarde en leer
un informe no es motivo para que el bucle se pare: **la cuarentena existe
justamente para que esas dos velocidades no tengan que coincidir.**

**LO QUE SIGUE SIENDO PARADA, y esta regla no lo toca:** una contradiccion entre
reglas, una cifra publicada contradicha, una peticion de mover un umbral o una
vara, y cualquier decision que sea del fundador. `D.32` acorta el camino entre dos
lotes; **no acorta ninguna de las condiciones de parada de
`AUDITOR_FORJA.md` seccion 3.**

## D.33. LOS ARTEFACTOS DEL ARNES SON REGISTRO DE MAQUINA, Y NO SE BARREN (10 sep 2026, decision del fundador)

*Cita: decision 4.3 del fundador del 10 sep 2026, sobre
`docs/loop/paradas/2026-09-10-credito-punteros-de-linea.md` seccion 4.3.*

    docs/loop/loop.log
    docs/loop/ultimo_extractor.json
    docs/loop/ultimo_auditor.json

**EXCLUIDOS del barrido de guiones y del hook.** El arnes los sigue commiteando en
su commit de artefactos: **no se barren, se guardan.**

> ## SE ENSANCHA POR PATRON, 12 sep 2026 (decision del fundador, punto 1)
>
> *Sobre la parada de la vuelta 20, archivada en
> `docs/loop/paradas/2026-09-12-el-artefacto-que-faltaba.md`.*
>
> **LA LISTA DE TRES TENIA UNA GRIETA CON FORMA DE FECHA.**
> `docs/loop/ultimo_apertura.json` **nacio con `D.34`, despues de que esta lista se
> escribiera**, y por eso no estaba en ella. En la vuelta 20, tres guiones largos
> del mensaje final de la fase ciega pusieron en rojo **el barrido Y la prueba de
> aceptacion entera**, y la parada se adjudico contra el auditor por no haber
> formateado su propio volcado.
>
> > ### **CAPA EQUIVOCADA. FORMATEAR LA SALIDA DE UN MODELO ES TAREA DEL ARNES.**
>
> **LA LETRA NUEVA:**
>
> > **`docs/loop/ultimo_*.json`, `docs/loop/loop.log` Y TODO FICHERO QUE EL ARNES
> > ESCRIBA DESDE LA SALIDA DE UN MODELO quedan excluidos del barrido y del hook,
> > HOY Y PARA LOS QUE NAZCAN MAÑANA.**
>
> **POR QUE UN PATRON Y NO UN INVENTARIO:** un nombre que hay que acordarse de
> añadir a una lista **protege hasta el dia en que alguien escribe un fichero
> nuevo.** Es la misma leccion de `D.40`, un piso mas abajo: lo que depende de
> acordarse no esta protegido.
>
> **LA CONVENCION QUE HACE QUE EL PATRON BASTE:** el arnes escribe la salida de un
> modelo en `docs/loop/ultimo_<rol>.json`. **Un artefacto nuevo que nazca del
> volcado de un modelo se llama asi y queda exento EL DIA QUE NACE**, sin que nadie
> toque `src/comun.py`.
>
> **Y LO QUE NO SE AFLOJA, con su caso positivo en la prueba:** la exencion es de
> **CAPA**, no de contenido. **Un acta, un reporte, una regla o un candidato con un
> guion largo tumba el barrido, este donde este**, y un `ultimo_cualquiera.json`
> **fuera** de `docs/loop/` es prosa de esta casa como cualquier otra.
>
> **Sede:** `src/comun.py`, `PATRONES_DE_ARTEFACTO` y `es_artefacto_de_maquina()`.
> **Pruebas:** `test_d33_se_ensancha_por_patron_y_no_por_lista` y
> `test_el_patron_mira_el_nombre_y_la_carpeta`, las dos con su caso positivo.

**EL MOTIVO MECANICO:** el arnes vuelca el texto del turno en el artefacto
**despues del ultimo commit**. Son **la unica escritura del repo que no puede
pasar por su propio hook**, porque cuando se escriben el turno ya termino.

**Y EN LA VUELTA 7 DEJO DE SER COSMETICO.** Tres vueltas seguidas con guiones
largos dentro, y la tercera sobre `ultimo_extractor.json`:

    $ python forja.py guiones
      BARRIDO DE GUIONES EN ROJO: 2 hallazgo(s)
    $ python tests/test_aceptacion.py
      FAIL: test_e_guion_largo_rompe_el_hook
      AssertionError: 1 != 0 : el repo ha de estar limpio antes de ensuciarlo
      total: 65 pruebas, 1 fallos, 0 errores

**Un turno bueno dejaba al siguiente arrancando en rojo**, y la prueba que caia
era justamente la del hook.

**ES COHERENTE CON `D.20`, NO UNA EXCEPCION A ELLA.** La regla siempre fue **se
barre lo que esta casa ESCRIBE**. El mensaje final de un modelo, volcado tal cual
por una tuberia, **no es prosa de esta casa** mas de lo que lo es un capitulo de un
libro ajeno. La casa escribe el reporte y el acta; la maquina escribe su testigo.

**LA MARCA ES EL NOMBRE Y SU CARPETA**, no el nombre solo: un fichero que se llame
`loop.log` en otro sitio no es el testigo del arnes.

**PRUEBAS.** En el arnes, **escenario 12**: el claude falso devuelve un mensaje con
un guion largo, el arnes lo vuelca en el artefacto, **y la vuelta corre entera**;
con la comprobacion de que el guion **esta de verdad ahi dentro**, porque si no la
prueba no probaria nada. En la suite, `PruebaBandejas`: los tres artefactos no se
barren, **y su CASO POSITIVO**, que `docs/loop/ACTA_AUDITOR.md`, en la misma
carpeta, **si se barre**. Sin ese caso, la exclusion podria haberse tragado
`docs/loop/` entero.

## D.34. EL REMEDIO ROTO DEL AUDITOR ACUMULA EN RACHA PROPIA, Y LA APERTURA CIEGA PASA A CODIGO (10 sep 2026, decision del fundador)

*Cita: decision 4.4 del fundador del 10 sep 2026.*

### D.34.1. La racha propia

> **Un remedio escrito que el auditor rompe acumula en una RACHA PROPIA, de
> especie `REMEDIO ROTO`. TRES SEGUIDAS PARAN.**

`AUDITOR_FORJA.md` 5.5 decia que **acumula** y **no decia donde**, y el auditor no
se lo invento: habria sido doctrina nueva, y eso es parada. Ya hay **tres
ejemplares, los tres suyos**.

**Se cuenta aparte de la del extractor**, y por la misma razon por la que existen
especies: **una racha mezclada no dice de quien es el problema.** Y como toda
racha de esta casa, **no se reinicia sola**: la reinicia una decision escrita del
fundador en `docs/loop/paradas/`, y el acta lo dice citandola (`AUDITOR_FORJA.md`
5.4). **Un auditor que pone su propia racha a cero se esta absolviendo.**

### D.34.2. La apertura ciega, en codigo

> **EL ARNES ENTREGA AL AUDITOR LOS CANDIDATOS Y LAS FUENTES, SELLA SUS CLASES, Y
> SOLO DESPUES LE EXPONE EL REPORTE.**

**POR QUE HIZO FALTA CODIGO, y lo midio el propio auditor.** Durante siete actas
la apertura ciega fue una promesa, y las siete se rompieron. El ACTA 6 la
sustituyo por un artefacto, un bloque obligatorio al principio del acta, y el ACTA
7 escribio su epitafio:

> *"Lo escribi, es lo primero del ACTA 7, y NO evito la contaminacion: solo la
> hizo visible en la primera pagina en vez de en la cuarta. **EL ARTEFACTO
> DOCUMENTA, NO IMPIDE.**"*

**LO QUE IMPIDE ES QUE EL FICHERO NO ESTE.** El arnes:

1. **retira `docs/loop/REPORTE.md` del arbol** y lo guarda fuera del repo;
2. invoca al auditor en **fase ciega**, con los candidatos y las fuentes, y su
   testigo es `docs/loop/APERTURA_CIEGA.md`;
3. **comprueba si el reporte reaparecio** durante la fase (recuperarlo de git es
   la unica via que queda, y es un acto deliberado: se dice, no se calla);
4. **SELLA** con `git hash-object` en `docs/loop/SELLOS_APERTURA.jsonl` y commitea;
5. **y solo entonces devuelve el reporte** para el turno normal.

**Y EL SELLO SE VERIFICA AL TERMINAR EL TURNO.** Un sello que nadie comprueba es
otra promesa: si la clasificacion ciega cambia despues de que el auditor vea el
reporte, **el arnes lo caza y se detiene** con su `PARA_ALEXIS.md`, nombrando las
dos huellas.

**LO QUE UN SELLO ROTO SIGNIFICA, y lo que no:** no dice que la clasificacion sea
falsa ni que el acta este mal. Dice que **esa comparacion, en esa vuelta, no es
ciega** y por tanto no vale.

**PRUEBAS.** Escenarios **13** y **13b** del arnes. El 13 comprueba que la fase
corre, que retira el reporte, que sella, que verifica, que el auditor corre
despues, **que el reporte vuelve a su sitio**, y sobre todo **que el auditor ciego
no lo tuvo delante**, leido de lo que el propio claude falso escribio. El **13b es
su caso positivo**: un auditor que reescribe su apertura tras ver el reporte, y el
sello lo caza, nombra las dos huellas y detiene la corrida.

## D.35. LA CITA DE LINEA LLEVA SU `sed` PEGADO AL LADO (10 sep 2026, decision del fundador)

*Cita: decision 4.1 del fundador del 10 sep 2026. **Con ella se reinicia la racha
`REPORTE`, que estaba en 3 de 3.***

> **NINGUNA CITA DE LINEA SE TECLEA EN UNA TABLA DEL REPORTE SIN QUE LA SALIDA
> LITERAL DE `sed -n '<n>p'` O `grep -n` QUEDE PEGADA AL LADO, EN EL PROPIO
> REPORTE**, aunque sea en una columna estrecha.

**EL EJEMPLAR ES LA VUELTA 7**, y las tres caidas fueron la misma averia: **un
puntero desplazado exactamente OCHO lineas**, las tres dentro de la seccion
`SELLING FAMILY` de `fuentes/smart_who/cap_06.md`.

| donde | el reporte cita | el texto vive en | desfase |
|---|---:|---:|---:|
| tabla de frontera, fila P5 | L73 | **L81** | **-8** |
| tabla de puentes, fila 3 | L51 | **L59** | **-8** |
| tabla de puentes, fila 4 | L57 | **L65** | **-8** |

**LA MAS GRAVE NO ES LA CITA, ES SU CONSECUENCIA.** La tabla declaraba
`SELLING FAMILY` de L43 a L73 y la seccion corre hasta L81: **L75, L77, L79 y L81
no aparecen en ninguna de las diecinueve piezas** de una tabla que se anuncia como
*"las diecinueve piezas del capitulo, en el orden del libro"*. **La frontera tenia
un hueco de cuatro bloques.**

**POR QUE MECANICO Y NO UNA PROMESA, que es toda la regla.** El remedio anterior
decia *toda cita de linea se reabre con `sed -n` antes de teclearse*, y se
rompio. En esta casa **los dos remedios que han funcionado obligan a TECLEAR
ALGO** (imprimir las claves antes de contar; escribir el cociente antes del
comparativo) **y los dos que se rompieron eran intenciones.**

> **UN REMEDIO QUE SE CUMPLE ACORDANDOSE NO ES UN REMEDIO.**

**Y NO PIDE MAQUINARIA NUEVA**, que la moratoria prohibe encargar: pide pegar una
salida que ya se corre.

## D.36. EL ORDEN QUE LEE (10 sep 2026, decision del fundador)

*Cita: decision 4.2 del fundador del 10 sep 2026, al autorizar la insercion de los
44 candidatos del lote 2.*

> **CUANDO LA ASIMETRIA DE UNA SEÑAL DECIDE SI UN PAR SE LEE O NO, SE INSERTA EN
> EL ORDEN QUE LO LEE.**

**EL EJEMPLAR, medido por el auditor en la vuelta 7:**

    celebrar_aceptacion_primer_dia -> sostener_contacto_oferta_aceptacion : 0,613  LEVANTA
    sostener_contacto_oferta_aceptacion -> celebrar_aceptacion_primer_dia : 0,587  NO levanta

**`difflib.SequenceMatcher.ratio()` no es simetrico**, y aqui esa asimetria no
mueve un decimal: **mueve si el par llega a leerse.** Si `celebrar` entra despues,
la aduana bloquea y pide veredicto; si entra antes, no lo pide y **el par no se
lee nunca.**

**LA REGLA ELIGE LA LECTURA.** Entre dos ordenes posibles, el que abre la cola
gana. **Leer de mas cuesta una lectura; leer de menos cuesta una arista que nadie
sabra que falta.**

**NO ES UN PARCHE DEL UMBRAL Y NO LO MUEVE.** `D.29` ya dice que la jerarquia la
caza la lectura y no la señal; **esta regla dice que cuando la señal SI la caza,
en un solo sentido, se entra por ese sentido.**

**Y NO LO FIJA EL BUCLE:** ni el extractor ni el auditor deciden el orden de
insercion. **Lo fija quien autoriza la insercion**, que es el fundador (`D.26`),
con la medida delante.

## D.37. LA SERIE QUE DICE CUANTAS PARTES TIENE Y LAS NOMBRA ES ARISTA POR LECTURA (10 sep 2026, decision del fundador)

> ### CORRECCION DECLARADA DEL TITULAR, 11 sep 2026, decision del fundador 5.4
>
> **El titular decia *"LA SERIE DECLARADA POR EL TITULO"*, y su cuerpo exige dos
> cosas: que la enumeracion diga CUANTAS partes hay Y que las NOMBRE.** El
> extractor y el auditor sostuvieron los dos la lectura estrecha en la vuelta 11
> (0 de 6 casos pasaron), y tenian razon.
>
> **UNA REGLA NO PUEDE TENER DOS LECTURAS**, y un titular mas ancho que su cuerpo
> es exactamente eso: quien cite el titular declara aristas que el cuerpo no
> autoriza. **El texto viejo del titular no se borra: esta aqui arriba.**
>
> **LA LECTURA QUE MANDA, y es la conservadora:**
>
> | el texto de la cabeza | que se hace |
> |---|---|
> | dice **cuantas** partes hay **y las nombra** (*"con sus seis vias"* mas las seis) | **`D.37`**: arista por lectura, citando el paso |
> | **solo enumera** sin decir cuantas | **`D.29`**, con razon escrita: es una lectura que hay que argumentar, no una transcripcion |
>
> **El cierre no es "no se declara": es que cambia de regla.** Un par que no pasa
> `D.37` sigue pudiendo ser madre e hijo, y se declara por `D.29` **si la lectura
> lo sostiene y escribe por que**. Lo que pierde es el derecho a entrar sin
> argumentar.

*Cita: decision del fundador del 10 sep 2026, sobre el hallazgo del commit
`f6dd619`. **Cuelga de `D.19` y `D.29`.***

> **CUANDO EL TITULO O EL TEXTO DE UN NODO ENUMERA SUS PARTES** (*"con sus seis
> vias"*, *"los cuatro pasos"*, *"las cinco efes"*) **Y ESAS PARTES EXISTEN COMO
> NODOS, LA ARISTA CABEZA A PARTE SE DECLARA POR LECTURA EN EL ACTO DE INSERTAR
> LA PARTE, CITANDO LA LINEA QUE ENUMERA, SIN ESPERAR A QUE UNA SEÑAL LA
> LEVANTE.**

**NO SE ESPERA A LA SEÑAL PORQUE YA ESTA MEDIDO QUE NO VA A VENIR.** `D.19` lo
dice con cifras propias: **ninguna señal separa jerarquia declarada de ruido**, y
`paso_contra_nodo` levanta el **3 por ciento** de las aristas declaradas. Esperar
a la señal es esperar a algo que la casa tiene escrito que no ocurre.

**Y AQUI LA LECTURA NO ES UN JUICIO DIFICIL: ES UNA TRANSCRIPCION.** No hay que
decidir si dos nodos se parecen. El texto de la cabeza **dice cuantas partes tiene
y las nombra una a una**. Comprobar cuales de esas partes existen como nodo es
mirar una lista.

### Lo que la hace verificable: la linea citada

**LA ARISTA SE DECLARA CITANDO EL PASO DE LA MADRE QUE ENUMERA LA PARTE.** Es la
misma exigencia que la adjudicacion `A.4` le puso al MUTUO, y por la misma razon:

> **UNA ARISTA SIN SU LINEA ES UNA AFIRMACION SIN CITA.**

**El auditor la verifica contra la linea citada como cualquier otra arista**: abre
el paso `n` de la madre y comprueba que ahi se nombra al hijo. Si el paso no lo
nombra, la arista cae, **y no hace falta discutir de parecidos.**

### La operacion, porque el instrumento no llegaba

La aduana cablea la arista **en el acto de insertar** y solo cuando alguien
escribe un veredicto sobre un vecino que una señal levanto. **Para dos nodos que
YA viven no habia camino**, y escribir a mano en `dataset/nodos.jsonl` esta
prohibido siempre (`EXTRACTOR.md` seccion 2).

    python forja.py arista --madre <id> --hijo <id> --paso <n> --razon "..."

**Es una OPERACION, con lo que el manual seccion 5 exige de una: simulacion del
gate sobre copia en memoria antes de escribir, y caso positivo.** Comprueba que
los dos extremos viven, que no es auto arista, que el paso citado existe en la
madre, que la arista no esta ya declarada, y que el gate admite el resultado.
**Si el gate sale rojo, no escribe nada.**

**Y GUARDA LAS TRES SEÑALES AUNQUE NO LEVANTEN**, con `levantada_por` en
`lectura declarada`. Esa fila de la bitacora es la prueba, en cada arista, de que
la vio un lector y no el instrumento.

### Su relacion con las otras dos, que no se solapan

| regla | dice |
|---|---|
| **`D.19`** | ninguna señal separa jerarquia de ruido: **la jerarquia la caza la LECTURA** |
| **`D.29`** | la arista que la señal no levanta **se declara por lectura, en el acto de la insercion** |
| **`D.37`** | y **cuando el texto ENUMERA sus partes, esa lectura ya esta hecha por el libro**: se transcribe, citando la linea |

**`D.37` no ensancha `D.29`: le pone el caso facil delante.** Donde `D.29` pide
una lectura que decida, `D.37` señala los pares en que **no hay nada que decidir**
porque el propio nodo los enumera.

### Lo que NO autoriza

**NO autoriza declarar una arista porque dos nodos compartan familia o tema.** La
enumeracion tiene que estar **escrita** en el titulo o en el texto de la cabeza,
**tiene que decir CUANTAS partes hay**, y **la parte tiene que ser la que ese paso
nombra**. **Sin la cuenta no hay `D.37`**: hay `D.29` con razon escrita. Una cabeza que dice *"con sus
seis vias"* y un nodo del mismo dominio que no es ninguna de las seis **no son
madre e hijo**: son hermanos, y su veredicto es `SANO`.

**Siete pruebas** (`PruebaAristaDeclarada37`): la arista se escribe resuelta por
los dos lados con su paso citado entero en la bitacora; **su caso positivo**, un
paso que la madre no tiene es rechazo **y no deja media arista escrita**; sin
razon escrita no se declara; un extremo que no vive es rechazo; la auto arista es
rechazo; declararla dos veces es rechazo y no la duplica; y **la simulacion del
gate manda**, comprobado cerrando una vuelta que el gate caza sobre la copia en
memoria dejando el dataset intacto.

## D.38. SEGUIDAS SIGNIFICA CONSECUTIVAS, Y EL AUDITOR TIENE UNA SOLA RACHA (11 sep 2026, decision del fundador)

*Cita: decisiones 5.2 y 5.3 del fundador del 11 sep 2026, sobre la parada de la
vuelta 11 (`docs/loop/paradas/2026-09-11-credito-y-la-quinta-peticion.md`).*

### D.38.1. Seguidas significa CONSECUTIVAS

> **UNA TANDA LIMPIA EN MEDIO PONE EL CONTADOR A CERO. NO LO CONGELA.**

**Es la misma letra que rige en la otra casa desde el 13 ago 2026**, y aqui se
escribe porque `AUDITOR_FORJA.md` 5.2 decia *"tres seguidas"* sin decir que pasa
con la vuelta limpia que se mete en medio. **Una regla que no dice eso tiene dos
lecturas**, y la ancha convierte cualquier racha en una condena perpetua: bastaria
una caida cada cinco vueltas para no salir nunca.

**CONSECUENCIA INMEDIATA, y por eso esta decision desbloquea el bucle:** la vuelta
10 fue limpia, asi que **la racha `REPORTE` estaba en 1 de 3 y no en 3 de 3**. Ese
motivo de parada **no existia**.

**LO QUE NO CAMBIA:** la racha **sigue sin reiniciarse sola por el paso del
tiempo**. La pone a cero **una tanda limpia** o **una decision escrita del
fundador**, y el acta lo dice citando cual de las dos (`AUDITOR_FORJA.md` 5.4).
**Un auditor que pone su propia racha a cero sin una de esas dos cosas se esta
absolviendo.**

> ## **QUE SIGNIFICA `LIMPIA`, RESUELTO PARA SIEMPRE** (16 sep 2026, decision del fundador)
>
> > **`LIMPIA` SIGNIFICA SIN CAIDAS DE LA ESPECIE QUE ESA RACHA ACUMULA.**
> >
> > **Una tanda con caidas solo de las que NO acumulan reinicia la racha igual.**
>
> **POR QUE HACIA FALTA DECIRLO.** `D.38.1` dijo *una tanda limpia pone el contador a
> cero* y **no dijo que es limpia**. Con una caida registrada que no acumula, la regla
> tenia dos lecturas, y la diferencia entre ellas **era una parada**.
>
> **Y NO ERA UNA DUDA TEORICA: PASO TRES ACTAS SEGUIDAS.** La `ACTA 25` se la planteo
> sobre si misma y escribio *que ninguna acumule por la letra no la vuelve limpia*; la
> `ACTA 26` la volvio a plantear y volvio a elegir la lectura estrecha; y las dos lo
> hicieron **sabiendo que la otra lectura las salvaba**, y dejandolo escrito para que
> cualquiera pudiera acusarlas de absolverse.
>
> > ### **UNA REGLA QUE OBLIGA A CADA AUDITOR A DECIDIR SI SE ABSUELVE ES UNA PRUEBA DE CARACTER, NO UNA REGLA. SE ACABA HOY.**
>
> **LO QUE NO CAMBIA:** la racha **sigue sin reiniciarse sola por el paso del tiempo**,
> y la caida que no acumula **se sigue registrando con su nombre**. Lo que deja de
> pasar es que una caida registrada y no acumulable **congele** el contador.

### D.38.2. El auditor tiene UNA sola racha, con DOS especies propias

> **`REMEDIO ROTO` y `CIFRA PUBLICADA PROPIA` acumulan EN LA MISMA RACHA. Tres
> seguidas paran**, con la regla de consecutividad de arriba.

`D.34.1` creo la racha propia para `REMEDIO ROTO` y no dijo donde caia una cifra
falsa del propio auditor. **Las dos cifras falsas de su apertura sellada de la
vuelta 11 son de esa segunda especie, y entran en la misma racha.**

**POR QUE UNA Y NO DOS, que es lo que habria salido de seguir partiendo:** las dos
especies son **el mismo fallo visto por dos sitios**. Un remedio roto es una
promesa que no se cumplio; una cifra propia falsa es una comprobacion que no se
hizo. **Lo que la racha mide es si el auditor se esta verificando a si mismo**, y
eso no se mide mejor repartiendolo en dos contadores que suben a la mitad de
velocidad.

**SIGUE SIENDO APARTE DE LA DEL EXTRACTOR** (`D.34.1`): una racha mezclada no dice
de quien es el problema.

> ## SE ACOTA, 12 sep 2026 (decision del fundador, punto 1)
>
> > **`REMEDIO ROTO` CUENTA SOLO CUANDO EL REMEDIO ES DE SUSTANCIA DE AUDITORIA:
> > clases, cifras, lecturas, herencia.**
> >
> > **UN REMEDIO SOBRE FORMATO DE ARTEFACTOS NO EXISTE COMO REMEDIO: ES TAREA DEL
> > ARNES.**
>
> **EL CASO QUE LO OBLIGO.** La `ACTA 19` `8.1` se encargo a si misma esto:
>
> > *Y CERO GUIONES LARGOS Y CERO GUIONES MEDIOS EN MI MENSAJE FINAL, porque el
> > arnes lo escribe en `ultimo_auditor.json` despues de que mis comprobaciones
> > hayan pasado.*
>
> **SE RETIRA POR CORRECCION DECLARADA.** No se borra de su acta, que es sede del
> auditor y no se toca: se declara aqui que **ese remedio no rige**, y que la
> tercera caida de la racha de la vuelta 20 **no era `REMEDIO ROTO`: era `D.33`**,
> un artefacto de maquina sin exencion escrita.
>
> **POR QUE LA DISTINCION NO ES UN FAVOR.** Un remedio es una promesa que el
> auditor puede cumplir **leyendo y midiendo mejor**. Pedirle a un modelo que
> formatee su propio volcado **le pide algo que no controla**: el volcado lo
> escribe la tuberia del arnes despues de que su turno haya terminado. **Una racha
> que cuenta eso no mide si el auditor se verifica: mide si el arnes esta bien
> cableado, y eso ya tiene su propia sede.**
>
> **Y NO AFLOJA LA RACHA.** `CIFRA PUBLICADA PROPIA` sigue entera, y `REMEDIO ROTO`
> sigue acumulando **en todo lo que si es sustancia**: una clase mal leida que el
> remedio pedia releer, una cifra que el remedio pedia remedir, una herencia que el
> remedio pedia declarar. **Lo que sale de la racha es una sola especie de cosa: el
> formato de lo que escribe la maquina.**

### D.38.3. Y la fase ciega deja de depender de la voluntad del auditor

*Decision 5.1 del fundador, que **reinicia la racha `REMEDIO ROTO` con condicion
mecanica**.*

**El auditor tenia razon al decir que su propio remedio era del genero que no
funciona: una promesa** (`D.35`: *un remedio que se cumple acordandose no es un
remedio*). **La racha se reinicia porque el remedio cambia de genero**, no porque
se le perdone.

`D.34.2` retiraba `REPORTE.md` durante la fase ciega. **Ahora el arnes retira
CUATRO ficheros:**

    docs/loop/REPORTE.md              el reporte
    docs/loop/loop.log                lo que hizo el turno
    docs/loop/ultimo_extractor.json   EL MENSAJE FINAL DEL EXTRACTOR
    docs/loop/ultimo_auditor.json     el acta anterior, resumida

**Y EL QUE FALTABA ERA EL PEOR:** `ultimo_extractor.json` guarda el mensaje final
del extractor, **que es un resumen de su propio reporte escrito por el**. Un
auditor que lo abre **lee la version corta de lo que venia a leer a ciegas**.

**Los devuelve al sellar, y el sello se comprueba al cerrar el turno**, igual que
antes.

**UN DETALLE DE FONTANERIA QUE ERA UNA GRIETA:** el arnes escribia su propio log
en `loop.log`, asi que **recreaba el fichero que acababa de retirar**. El log tiene
ahora destino conmutable: durante la ventana ciega va a un provisional, y **sus
lineas se anexan al de verdad cuando el fichero vuelve**, para que la ventana no
se pierda del registro por haber ocurrido con el fichero fuera. **Lo cazo la
propia prueba**, no una lectura.

**PRUEBA** (escenario 13 del arnes, ampliado): el auditor ciego **va a por los
cuatro y anota cual encontro**; la prueba exige `ausentes:` con los cuatro nombres
y **ninguno marcado como encontrado**; los cuatro **vuelven a su sitio** tras
sellar; y **el log recupera la ventana ciega**. Con los cuatro creados antes de la
corrida, porque si no existieran *"volvio a su sitio"* no probaria nada.

### D.38.3. LA APERTURA CIEGA PUBLICA CLASES Y LECTURAS, NO CIFRAS CONTADAS A MANO (11 sep 2026, decision del fundador)

*Cita: decision 1 del fundador del 11 sep 2026, sobre la parada de la vuelta 14.
**Con ella se reinicia la racha propia del auditor**, y no se le quita la razon a
su autocondena: su `ACTA 12` juzgo el mismo defecto en la misma sede y acumulo, y
**la consistencia vale mas que la absolucion.***

**EL DATO QUE LA PARIO:** en tres actas seguidas, **las tres caidas propias del
auditor fueron de la misma familia**: una cifra publicada en la **apertura ciega**.
Ninguna toco un dato, ninguna movio un veredicto, ninguna cambio un volumen de
lote. **Todas nacieron en el mismo sitio.**

> **TODA CIFRA QUE APAREZCA EN LA APERTURA CIEGA SALE DE UN INSTRUMENTO DE LA CASA
> CORRIDO EN ESA FASE, CON SU SALIDA LITERAL PEGADA AL LADO. UNA CIFRA SIN
> INSTRUMENTO AL LADO NO SE PUBLICA.**

    | clase                     | cuantos | el instrumento, pegado                |
    |---------------------------|--------:|---------------------------------------|
    | candidatos en la bandeja  |      68 | `$ ls cuarentena/zhuo_manager/*.json | wc -l` -> 68 |

**POR QUE ESTA SEDE Y NO OTRA.** La apertura ciega se escribe **con los cuatro
ficheros del bucle retirados** (`D.38.3` no los devuelve: `D.34.2` los retira),
contra reloj y **sin poder contrastar contra el reporte**. Es la sede donde mas
facil es publicar una cifra sin cruzarla, **y `D.38.2` la trata igual de seria que
al acta**, que es lo correcto y lo que la hacia cara.

**LAS TRES CAIDAS SE HABRIAN CAZADO CON ESE CRUCE.** No es una hipotesis comoda:
las tres eran cifras de recuento, y las tres tenian un instrumento de la casa
capaz de darlas. **Ahora el cruce es obligatorio.**

**LO QUE LA APERTURA CIEGA SI PUBLICA, y es lo que vale de ella:** **clases** (que
es cada candidato, de que especie es cada pieza) y **lecturas** (que dice el texto,
que linea lo sostiene). **Eso es lo que despues se compara con la del extractor**,
y para eso no hace falta ninguna cifra contada de memoria.

> ## SE ENSANCHA, 16 sep 2026: **LA FRASE ES LA DEL INSTRUMENTO**
>
> *Punto 2.b de la decision del fundador del 16 sep 2026.*
>
> > **LA LINEA QUE ACOMPANIA A UNA CIFRA DICE LO QUE EL INSTRUMENTO MIDIO** (*campo `X`
> > presente en `33` de `234`*), **Y TODA CONCLUSION SOBRE CONTENIDO VA EN LINEA APARTE
> > MARCADA `LECTURA`, CON LO QUE LA SOSTIENE.**
> >
> > **Contar campos y publicar una frase sobre contenido es caida de cifra.**
>
> **EL CASO.** La vuelta 26 corrio un censo de **campos** y publico, en su apertura
> sellada, que *ningun nodo del grafo y ningun candidato de la bandeja dice de que capitulo
> sale*. **`33` de `234` lo dicen**, en `resumen_teorico`, **y los doce de esa vuelta
> estaban entre ellos.** El instrumento estaba pegado y la cifra era cierta: **lo falso era
> la frase.**
>
> **NINGUNA MAQUINA COMPRUEBA SEMANTICA, y por eso esta mitad es de FORMA y no de codigo.**
> Lo que la forma consigue es separar **la medida** de **la conclusion**, y **dejar la
> conclusion a la vista, marcada, para que el siguiente lector la cace.** Una conclusion
> escondida dentro de la frase de una cifra viaja de acta en acta sin que nadie la mire;
> una marcada `LECTURA` se lee como lo que es: **una lectura, que puede estar mal.**
>
> **ASI SE ESCRIBE:**
>
>     campo cap_NN presente en resumen_teorico : 33 de 234
>     $ grep -lc "cap_[0-9]" ...   ->  33
>     LECTURA: la costumbre de nombrar la unidad empieza en cap_07, asi que los
>     anteriores no la traen. La sostiene el reparto por commit de alta de 4.2.
>
> **Y LA REGLA DE ORO DE LA FASE CIEGA SIGUE ENTERA:** *contar bien un campo y sacar la
> conclusion equivocada sigue siendo una caida; la fuente hay que elegirla antes de
> contarla* (`AUDITOR_FORJA.md` `0`).

**NO ES UNA PROHIBICION DE MEDIR: ES UNA PROHIBICION DE CONTAR A OJO.** Medir con
el instrumento y pegar su salida esta no solo permitido, sino que es lo unico que
convierte una cifra de esa fase en publicable.

### D.38.4. EL BARRIDO DE VECINOS DE LA APERTURA CIEGA SE HACE SOBRE GRAFO MAS BANDEJAS (11 sep 2026, decision del fundador)

*Cita: decision 2 del fundador del 11 sep 2026, **como el auditor lo dejo
encargado y medido** en su `ACTA 14` seccion 7.3.*

> **LA POBLACION DEL BARRIDO ES EL GRAFO MAS TODO LO QUE ESPERA EN CUARENTENA.**
> **Un vecino que esta en la bandeja es vecino.**

**LA MEDIDA QUE LO DECIDE, y la trajo el propio auditor contra si mismo:**

    el auditor barrio   135 titulos   (solo el grafo)
    el extractor barrio 203 titulos   (135 del grafo + 68 de la bandeja)

**Y EL VECINO MAS CERCANO DEL CANDIDATO 1 ESTABA EN LA BANDEJA.** Tres de los once
pares del extractor **no existirian** en la lectura del auditor.

**POR QUE LA ADUANA NO LO VE Y LA LECTURA SI TIENE QUE VERLO.** `aduana.buscar_vecinos`
compara contra `dataset/nodos.jsonl`, que es lo correcto **para decidir si un nodo
entra**: un candidato no puede tener por madre a algo que todavia no vive. **Pero la
apertura ciega no decide inserciones: decide si dos lecturas independientes ven lo
mismo**, y para eso la poblacion tiene que ser la que el extractor tuvo delante.

**~~EL METODO, con instrumentos que ya existen y sin maquinaria nueva:~~**
**TACHADO EL 16 sep 2026. El texto viejo se queda en pie y el vigente esta al
final de esta regla, en la CORRECCION DECLARADA del 16 sep: la receta de abajo
cuenta las bandejas DOS VECES desde que `D.38.5` llego a `src/aduana.py`.**

    # la poblacion entera, grafo mas bandejas, en un jsonl de usar y tirar
    python -c "import io,json,os,glob; \
      f=[l for l in io.open('dataset/nodos.jsonl',encoding='utf-8')]; \
      f+= [json.dumps(json.load(io.open(p,encoding='utf-8')),ensure_ascii=False)+chr(10) \
           for p in glob.glob('cuarentena/*/*.json') if '_insertados' not in p \
           and '_derivadas' not in p]; \
      io.open('/tmp/poblacion.jsonl','w',encoding='utf-8').writelines(f)"

    # y el barrido de vecinos contra ESA poblacion
    FORJA_DATASET=/tmp/poblacion.jsonl python forja.py informe --carpeta cuarentena/<lote>

**EL DESCARTE DE `_insertados` Y `_derivadas` NO ES OPCIONAL:** el primero son nodos
que ya viven en el grafo y entrarian dos veces; el segundo son copias que hace la
maquina para medir.

**Y LA CIFRA DE LA POBLACION SE PUBLICA CON SU INSTRUMENTO AL LADO** (`D.38.3`):
decir *"barri sobre grafo mas bandejas"* sin decir **cuantos** y **sin el `wc -l`
pegado** es exactamente la especie que `D.38.3` prohibe.

> ### **CORRECCION DECLARADA, 12 sep 2026, `ACTA 18` del auditor: UN NODO NO ES VECINO DE SI MISMO**
>
> **EL METODO DE ARRIBA NO SE BORRA, porque su fondo es correcto: lo que falla es su
> ejemplo.** Corrido tal como esta escrito, **no devuelve ni un vecino**, y esta es la
> salida, de la fase ciega de la vuelta 18 (`APERTURA_CIEGA.md` seccion 6.2, sellada):
>
>     $ FORJA_DATASET=<grafo mas bandejas> python forja.py informe --carpeta cuarentena/scott_radical_candor
>       candidatos revisados        : 63
>       nodos en el grafo de destino: 429
>       ENTRARIAN  0  |  BLOQUEARIAN  0  |  CAERIAN  63  |  CHOCAN  0
>       POR QUE GUARDA CAEN
>           63  el id ya vive en el grafo
>
> **LA RECETA METE LA BANDEJA EN LA POBLACION Y DESPUES BARRE ESA MISMA BANDEJA**, asi que
> cada candidato se encuentra a si mismo, la guarda de id muerde primero y el barrido
> **corta antes de llegar a buscar vecinos.** Un auditor que la cumpla al pie de la letra
> publica **cero vecinos** y cree que ha barrido.
>
> **LO QUE LA REGLA DICE HOY:** la poblacion es el grafo mas las bandejas **menos el propio
> candidato**, y por eso se barre **uno por vez**. **No es doctrina nueva y por eso lo
> adjudica el auditor** (`AUDITOR_FORJA.md` 1.3, *si una regla escrita cubre el caso por
> extension natural, se adjudica citandola*): esta casa ya sostiene en el codigo de su gate
> que **un nodo no puede ser vecino de si mismo**, y esa guarda se llama `auto_arista`.
>
> **CORRIDA ASI, la misma poblacion (429 menos 1 igual a 428, trece veces) levanta 10
> vecinos y 9 pares** donde la receta literal levantaba cero.
>
> **Y LA MEDIDA QUE DICE QUE ESTO YA VENIA PASANDO:** la `ACTA 17` publico `416 = 203 + 213`
> y su testigo dice *contra 415 titulos*, que es `416` menos `1`. **Aquella vuelta ya barrio
> con la exclusion puesta y no dejo escrito que la receta del banco no la trae.** Una regla
> que solo funciona si quien la lee la arregla por su cuenta **no esta escrita: esta
> adivinada.**

> ### **CORRECCION DECLARADA, 16 sep 2026, `ACTA 29` `6.6`: LA RECETA DE ARRIBA CUENTA LAS BANDEJAS DOS VECES**
>
> *`D.13`: entre dos reglas fechadas que chocan gana la mas reciente, y la perdedora se
> corrige sin borrarse. Aqui la mas reciente es `D.38.5`, y lo que la hace ganar no es su
> fecha sola: es que el 16 sep llego a `src/aduana.py` y cambio lo que la maquina hace.*
>
> **LO QUE QUEDA SUPERADO:** la receta de construir **a mano** la poblacion del barrido como
> grafo mas bandejas, volcarla a un jsonl de usar y tirar y pasarsela a la aduana por
> `FORJA_DATASET`. **Era correcta mientras la aduana cargaba solo el grafo. Hoy ya no.**
>
> **LO QUE PASA SI SE CORRE HOY AL PIE DE LA LETRA, medido en `ACTA 29` `6.6`:** la aduana
> **vuelve a poner las bandejas por su cuenta**, asi que la poblacion sale con las bandejas
> **contadas dos veces**, `440` en vez de `348`, y **el candidato acaba dentro de su propia
> poblacion**: la guarda `el id ya vive en el grafo` lo tumba. Es la misma figura que la
> `ACTA 18` corrigio en 2026, **pero por la puerta contraria**: entonces la sobraba la
> bandeja en el fichero, hoy la pone la aduana.
>
> **EL METODO VIGENTE, y es mas corto que el viejo:**
>
>     # se le entrega a la aduana la poblacion del GRAFO, y ella pone las bandejas
>     python forja.py informe cuarentena/<lote>/<id>.json
>
> **EL BARRIDO SE HACE ENTREGANDO A LA ADUANA LA POBLACION DEL GRAFO Y DEJANDO QUE ELLA
> PONGA LAS BANDEJAS.** Lo que `D.38.4` mandaba (que el auditor y la maquina midan la misma
> poblacion) **se cumple hoy sin construir nada a mano**, que era justamente su motivo.
>
> **Y LO QUE NO CAMBIA:** la exclusion del propio candidato sigue entera (`ACTA 18`), la
> guarda `el id ya vive en el grafo` sigue mirando **solo el grafo** (`D.38.5`), y la cifra
> de la poblacion se sigue publicando con su instrumento al lado (`D.38.3`).

### D.38.5. LA POBLACION DEL BARRIDO ES GRAFO MAS BANDEJAS **TAMBIEN PARA LA ADUANA** (12 sep 2026, decision del fundador)

*Punto 3 de la decision del fundador del 12 sep 2026. **No es una regla nueva: es
`D.38.4` llegando a la otra mitad de la casa**, y por eso lleva su numero y no uno
propio.*

**`D.38.4` mando desde el 11 sep que el barrido del AUDITOR se hiciera sobre grafo
mas bandejas.** El informe de la aduana seguia cargando **solo el grafo**
(`src/informe.py`, la linea que leia `dataset/nodos.jsonl` y nada mas), asi que
durante nueve vueltas **la maquina y el auditor midieron poblaciones distintas.**

> **UN PAR CUYOS DOS EXTREMOS VIVEN EN CUARENTENA SE LEVANTA IGUAL.**

**EL EJEMPLAR, Y ES LO QUE LO OBLIGO:** `cap_10` `L225` a `L251` contra
`reconocer_recompensar_gente_estable` de `cap_06`, **los dos en la bandeja.** La
`ACTA 20` lo leyo, lo clasifico y dejo escrito que **la aduana no lo iba a levantar
sola**. Un par que solo se ve si alguien se acuerda de mirarlo no esta guardado.

### Lo que NO se ensancha, y es la mitad que impide el estropicio

| pieza | poblacion |
|---|---|
| **el barrido de vecinos** (las tres señales) | **grafo mas bandejas** |
| **la guarda `el id ya vive en el grafo`** | **solo el grafo.** Un id que espera en la bandeja **no vive en el grafo todavia**, y tumbarlo por eso convertiria toda la bandeja en un lote rechazado |
| **los instrumentos de `calibracion/`** | **solo el grafo, declarado en su linea**: miden la aduana contra un catalogo de referencia con su tag y su commit, y meterles las bandejas de hoy haria que la misma medida diera otro numero cada dia |

**Y EL PROPIO CANDIDATO NO SE MIDE CONTRA SI MISMO**, que es la errata de metodo de
`D.38.4` corregida en la `ACTA 18`: se barre **uno por vez**, y su id lo excluye.

### Lo que entra en la poblacion, y el criterio NO es una lista de carpetas

**`cuarentena/` tambien aloja `ensayo_referencia_163/`**, que son **163 nodos de un
catalogo de referencia ajeno** puestos ahi para calibrar la aduana
(`docs/ESTRENO_DE_LA_ADUANA.md`). **Esos no esperan juicio: no van a entrar nunca en
este grafo**, y medir el trabajo de hoy contra ellos seria abrir cola de lectura
contra material que la puerta rechazaria de todas formas.

> **ENTRA EN LA POBLACION EL CANDIDATO CUYAS FUENTES ESTAN TODAS EN LA TABLA
> CANONICA VIGENTE.** Se descartan ademas `_insertados` (ya viven en el grafo,
> `D.31`) y `_derivadas`.

**POR QUE ASI Y NO POR NOMBRE DE CARPETA:** una lista de nombres es exactamente el
error que el **punto 1 de esta misma decision** acaba de corregir en `D.33`. Una
fuente fuera de la tabla **ya tumbaria al candidato en la puerta** (guarda
`fuentes`), asi que lo que la poblacion deja fuera es **exactamente lo que no
podria entrar**. Y es simetrico: el ensayo se corre con `FORJA_FUENTES` apuntando a
su tabla derivada, y **ese dia los 163 son los canonicos y los 83 del lote 4 no.**
**El criterio sigue a la tabla que mande, no a una carpeta.**

**LA POBLACION SE PUBLICA CON SU REPARTO** (`D.38.3`): el informe escribe
`poblacion del barrido : 286 (203 del grafo mas 83 que esperan en bandejas)`,
porque **`286` solo no deja leer por que un candidato levanto vecino.**

**Medido el 12 sep 2026:** la poblacion de bandejas del lote 4 es **83**, y los 163
del catalogo de control **quedan fuera**, como el propio auditor los habia dejado
fuera a mano en su barrido de la vuelta 20.

> ## CORRECCION DECLARADA, 16 sep 2026: **LLEVABA CUATRO DIAS A MEDIO CABLEAR**
>
> **ESTA REGLA DICE `TAMBIEN PARA LA ADUANA` EN SU PROPIO TITULAR, y durante cuatro
> dias solo estuvo en `src/informe.py`, que corre EN SECO.** La que decide es
> `src/aduana.py`, y ahi seguia midiendo **solo el grafo**:
>
>     src/informe.py:222   poblacion = list(nodos) + list(bandejas)
>     src/aduana.py:797    vecinos = buscar_vecinos(candidato, nodos, umbrales)
>     $ grep -n "poblacion_de_bandejas" src/aduana.py   ->  cero coincidencias
>
> **LO LEVANTARON LOS DOS A CIEGAS Y POR CAMINOS DISTINTOS** en la vuelta 26: el
> auditor con un barrido dirigido, el extractor con un rechazo de la aduana.
>
> **EL COSTE, MEDIDO POR LA `ACTA 26`:** cinco pares por encima de umbral **sin
> veredicto**, los cinco con un extremo en la bandeja. **No era perdida: era
> aplazamiento**, porque el par se paga cuando entra el segundo. **Pero esta regla
> nacio para que un par no dependa de que alguien se acuerde.**
>
> **YA ESTA CABLEADA DONDE SE DECIDE**, con la poblacion mudada a `src/aduana.py` y
> el informe tomandola de ahi. **La tabla de arriba no cambia ni una linea**: el
> resolutor sigue mirando solo el grafo, los instrumentos de calibracion siguen
> midiendo contra su catalogo, y el candidato sigue sin medirse contra si mismo.
>
> **CASO POSITIVO:** un candidato cuyo unico vecino vive en la bandeja **queda
> BLOQUEADO** por la aduana de verdad, y antes entraba limpio. **CASO NEGATIVO:** sin
> vecino en la bandeja entra limpio, **porque una aduana que bloquea todo es un
> candado**; y `el id ya vive en el grafo` **sigue mirando solo el grafo**, que si se
> ensanchara convertiria la bandeja entera en un lote rechazado. **6 pruebas**
> (`PruebaAduanaMideBandejas`).
>
> **Y LA BANDEJA SE PUEDE SOBREESCRIBIR** (`FORJA_CUARENTENA`), como el dataset y la
> bitacora: sin eso la prueba de aceptacion mediria contra los candidatos del repo de
> verdad y su resultado cambiaria de una vuelta a otra.

---

## D.39. LA INSERCION DE UN LOTE CERRADO ES AUTOMATICA (11 sep 2026, decision del fundador)

*Cita: decision 3 del fundador del 11 sep 2026. **Es la sexta vez que el auditor
pide la insercion**, y las mediciones ya la sostienen.*

> ### CORRECCION DECLARADA A `D.26`
>
> **`D.26` decia que la insercion es una autorizacion del fundador y no un
> default, y tenia razon el dia que se escribio: el instrumento no se habia medido
> nunca.** Ya se ha medido. **El texto de `D.26` no se borra**, y su motivo sigue
> siendo bueno para lo que ahora cubre `D.39`: lo que no esta cerrado no entra.

**LO QUE LO SOSTIENE, medido y no supuesto:**

| | |
|---|---|
| tres lotes con su tasa de pasos inventados | entre **3 y 8 por ciento**, desde el 36 del lote 1 |
| la aduana | **muerde**, comprobado por mutacion en cada acta |
| la apertura ciega del auditor | **en codigo** desde `D.34.2`, con su sello verificado |
| inserciones indebidas en toda la campaña | **CERO** |

### La letra, que es lo que el default NO autoriza

> **CUANDO UN LOTE QUEDA CERRADO EN EXTRACCION Y EL ACTA DEL AUDITOR CERTIFICA SU
> INFORME** (todos `ENTRARIAN`, o las caidas declaradas con su motivo), **EL
> EXTRACTOR INSERTA ESE LOTE EN SU VUELTA SIGUIENTE, SIN FIRMA NUEVA DEL
> FUNDADOR.**
>
> **LOS CANDIDATOS DE UN LOTE ABIERTO SIGUEN EN CUARENTENA HASTA QUE SU LOTE
> CIERRE.**

**Con `D.36`** (el orden que lee), **`D.37`** (la serie que dice cuantas partes
tiene), **sus veredictos a `bitacora/VEREDICTOS.jsonl`** y **los insertados a
`cuarentena/_insertados/<libro>/` en el mismo acto** (`D.31`).

**`MODO_INSERCION` pasa a `insertar` por defecto**, y `cuarentena` sigue
disponible para una vuelta que no deba insertar nada.

### Por que la condicion es LOTE CERRADO y no CANDIDATO LISTO

**Un candidato suelto que entra antes de que su lote cierre se lleva por delante
la comparabilidad de todo el lote:** los que entren despues lo veran como vecino y
los que entraron antes no, **y la cifra de vecinos del lote deja de significar una
sola cosa.** Ademas, `D.36` (el orden que lee) **solo se puede calcular sobre un
lote completo**: con el lote abierto no se sabe todavia quien va a entrar.

**EL ARNES NO PUEDE COMPROBAR ESTO.** No sabe que es un lote cerrado ni lee actas.
**Lo comprueba el extractor leyendo esta regla, y el auditor lo verifica**, que es
lo mismo que pasa con todas las reglas de doctrina de esta casa.

### Lo que esta regla NO toca

**Las condiciones de parada siguen enteras.** Un lote cuyo informe traiga caidas
**sin motivo declarado** no esta certificado, y entonces **no se inserta y se
trae**. `D.39` acorta el camino entre cerrar y meter; **no acorta ninguna guarda.**

**Y LA PRIMERA APLICACION VA ENCARGADA, no supuesta:** los **68 candidatos de
`zhuo_manager`** que esperan, y **los 26 veredictos razonados que hoy viven solo en
`REPORTE.md`** y que con la insercion pasan por fin a la bitacora, que es donde
`D.26` los pone.

## D.40. LO QUE UN AUDITOR LE DEJA AL SIGUIENTE LO ENTREGA EL ARNES, NO LA MEMORIA (12 sep 2026, decision del fundador)

*Cita: decision 1 del fundador del 12 sep 2026, sobre la parada de la vuelta 17. **La
racha propia del auditor se reinicia, y se reinicia con condicion mecanica**, porque el
fallo es de arquitectura y no de voluntad.*

### LO QUE LO SOSTIENE: tres actas seguidas, el mismo remedio, y el propio auditor diagnosticandolo

| acta | el remedio que el auditor se escribio a si mismo | como salio |
|---|---|---|
| `ACTA 14` | un rotulo de **tres lineas** en la apertura ciega | roto |
| `ACTA 15` 7.2 | el mismo, **simplificado a una sola cadena** *para que no pudiera volver a romperse* | roto igual |
| `ACTA 16` 7.3 | `ACTA ANTERIOR LEIDA`, con su `grep` al lado, *que corre el auditor siguiente sin leerme* | roto por tercera vez: `grep -c` dio **0** donde el remedio dice **1** |

**Y LA CAUSA NO LA PONE ESTA REGLA: LA ESCRIBIO EL AUDITOR, EN LA `ACTA 16` 7.1, UNA
VUELTA ANTES DE VOLVER A CAER:**

> *el problema no era la complejidad del rotulo: era que mi fase ciega **no lee la
> `ACTA 15` antes de escribir**, y por eso el remedio no llega. Eso si lo puedo
> arreglar.*

**No lo arreglo.** Su `ACTA 17` 7.1 lo dice entero: *escribi el diagnostico, escribi el
remedio, y volvi a hacer lo mismo.* **Tres intentos de arreglar con voluntad un problema
que no es de voluntad son la prueba de que la voluntad no era la pieza.**

> ### UN REMEDIO QUE HAY QUE ACORDARSE DE IR A BUSCAR NO ESTA ENTREGADO: ESTA ARCHIVADO
>
> `docs/loop/ACTA_AUDITOR.md` tiene **16.577 lineas**. Pedirle a la fase ciega que
> recuerde abrirlo, encuentre dentro su propia tarea y la cumpla **es pedirle tres cosas
> donde el arnes puede darle una.** `D.35` ya lo tenia escrito: *un remedio que se cumple
> acordandose no es un remedio.*

### La letra

> **AL ABRIR LA FASE CIEGA, EL ARNES EXTRAE DEL ACTA ANTERIOR la seccion `TAREA
> BLOQUEANTE DEL AUDITOR` y cualquier `REMEDIO` que el auditor anterior dejase escrito, y
> LOS ANTEPONE AL PROMPT bajo el titulo `REMEDIOS PENDIENTES QUE HEREDAS`.**
>
> **EL SELLO DE APERTURA CIEGA EXIGE:**
>
>     ACTA ANTERIOR LEIDA: <hash>
>
> **y UNA LINEA POR REMEDIO HEREDADO**, `CUMPLIDO` o `NO APLICA` **con su motivo**.
>
> **SI FALTA ALGUNA, EL ARNES SE DETIENE ANTES DE QUE EL ACTA SE ESCRIBA, NOMBRANDO LO
> QUE FALTA.**

**Solo de la ULTIMA acta**, que es la que se hereda: un remedio de la vuelta 9 que
sobreviva ocho actas no es herencia, es deuda vieja y se declara a mano.

**`NO APLICA` EN BLANCO NO VALE.** Un remedio que no toca esta vuelta se declara y se
dice por que; dejarlo sin motivo es perderlo con una palabra encima, que es justo lo que
esta regla vino a impedir.

> ## SE ENSANCHA, 16 sep 2026: **UN `NO APLICA` LLEVA LA SALIDA PEGADA**
>
> *Punto 2.a de la decision del fundador del 16 sep 2026, sobre la parada de la vuelta 26.*
>
> > **UN `NO APLICA` SOBRE UN HEREDADO LLEVA PEGADA LA SALIDA DEL INSTRUMENTO QUE LO
> > SOSTIENE, NO SOLO EL MOTIVO. SIN SALIDA PEGADA, EL SELLO NO LO ACEPTA.**
>
> **EL CASO, Y ES LITERAL.** La vuelta 26 declaro `NO APLICA` el heredado que le pedia
> sanear los guiones al volcar texto del libro al arbol, **con el motivo de que ninguno de
> sus instrumentos escribia en el arbol.** Seis escribian, **su propia tabla los lista**, y
> **el barrido de guiones estaba en ROJO con ocho hallazgos suyos** al empezar su turno.
>
> **`D.40` EXIGIA MOTIVO Y EL MOTIVO ESTABA ESCRITO: exigia que lo hubiera, no que fuera
> cierto.** Esa es la grieta, y es la misma forma que `D.41` y `D.42` ya cerraron en sus
> sedes: **una regla que se cumple escribiendo algo se cumple escribiendo cualquier cosa.**
>
> **UNA SALIDA PEGADA NO PRUEBA QUE EL MOTIVO SEA CIERTO**, y conviene decirlo para no
> vender mas de lo que es. **Lo que hace es obligar a correr algo antes de escribirlo**, y
> ese motivo concreto **lo habria cazado al instante**: no hay forma de pegar un comando que
> diga que ninguno escribe cuando seis escriben.
>
> **LA FORMA:** una linea que empiece por `$` dentro de las doce lineas siguientes a la
> declaracion. Vale el markdown de la casa (cita, negrita, sangria). **Un `CUMPLIDO` no la
> necesita**: la exigencia es de la excusa, no del cumplimiento.
>
> **Sede:** `src/herencia.py`. **Pruebas:** 5 mas, con su caso positivo (un `NO APLICA`
> pelado cae), su negativo (con la salida debajo pasa) y el que fija que **pegada quiere
> decir DEBAJO** y no en cualquier sitio del documento.

**Y EL `<hash>` ES EL DE `git hash-object` SOBRE EL ACTA**, el mismo que usa el testigo:
**no vale decir que se leyo otra version.**

### La confirmacion que hace falta decir, porque parece lo contrario

> **`docs/loop/ACTA_AUDITOR.md` ESTA EN LA LISTA DE LO QUE LA FASE CIEGA **SI** PUEDE
> ABRIR.**

**El acta es obra del auditor, no del extractor.** `D.34.2` retira **cuatro** ficheros de
la fase ciega (`REPORTE.md`, `loop.log`, `ultimo_extractor.json`, `ultimo_auditor.json`)
y **el acta no es ninguno de los cuatro. Leer su propia acta no es contaminacion: es lo
unico que le deja saber que se encargo a si mismo.** El prompt ciego lo dice ahora con
esas palabras, para que ninguna vuelta vuelva a tratarlo como si estuviera prohibido.

### Donde vive, y con que caso positivo

| | |
|---|---|
| el instrumento | `src/herencia.py`, `python forja.py herencia` y `python forja.py herencia --comprobar` |
| el cableado | `orquestador_forja.sh`, dentro de `apertura_ciega()`, antes de invocar y antes de sellar |
| la parada | `para_alexis_por_herencia()`, que devuelve los cuatro ficheros retirados a su sitio antes de salir |
| **caso positivo** | `tests/prueba_arnes.sh` escenario **14b**: con el falso claude callando la linea, **el arnes para, nombra las dos que faltan, el auditor no corre y los cuatro ficheros vuelven** |
| pruebas de unidad | `PruebaHerencia` en `tests/test_aceptacion.py`, **7 pruebas**, con el corte de la acta vieja y la huella ajena cazados |

> ## CORRECCION DECLARADA A `D.40`, 12 sep 2026: **SE COMPRUEBA PRESENCIA, NO CONTEO**
>
> *La escribo el mismo dia que la regla, porque el mismo dia la guarda mordio a quien
> cumplia.* **La vuelta 19 se detuvo por `D.40` y la apertura estaba bien.**
>
> **LO QUE LA APERTURA DE LA 19 ESCRIBIO**, y su huella es la buena al digito:
>
>     > ### **ACTA ANTERIOR LEIDA: `80fd74cdf15bb0b1ff02bcbe560ba03f11f22472`**
>     ### `HEREDADO 1`: **CUMPLIDO**
>
> **LO QUE EL COMPROBADOR BUSCABA:** esas dos lineas **desnudas**, sin comillas, sin
> negrita y sin encabezado. **Pedirle a un documento de esta casa que escriba una linea
> sin el formato de esta casa es pedirle que escriba peor**, y el precio fue una parada
> contra un auditor que habia leido el acta, remedido la huella y declarado el remedio.
>
> **Y LA MITAD QUE YA ESTABA ROTA ANTES:** el remedio que el auditor se escribio en la
> `ACTA 16` 7.3 pedia `grep -c "ACTA ANTERIOR LEIDA" -> 1`. **Su propia apertura de la
> vuelta 18 midio 2 y lo dijo en voz alta** (*`-> 2 (mi remedio pide 1)`*), porque una
> apertura que declara arriba y lo repite en su tabla de cierre **cita la linea que
> declara**. **UN CONTEO EXACTO CASTIGA A QUIEN DECLARA DE MAS.**
>
> ### La letra corregida
>
> > **SE COMPRUEBA QUE LA DECLARACION ESTE, NO QUE VAYA DESNUDA NI QUE APAREZCA UNA SOLA
> > VEZ.** El adorno de markdown (comillas, negrita, encabezado, cita) **se quita antes de
> > buscar**, y **basta con que UNA de las veces que aparece este bien puesta.**
>
> **SE RETIRA, POR ESTA CORRECCION, LA CLAUSULA DE CONTEO DEL REMEDIO DE LA `ACTA 16`
> 7.3** (`grep -c ... -> 1`). **No se borra de su acta**, que es sede del auditor y no se
> toca: se declara aqui que **esa mitad ya no rige**, porque `D.40` la sustituyo entera al
> pasar la comprobacion del recuerdo al arnes. **La otra mitad del remedio, leer el acta
> antes de escribir, sigue viva y ahora la cumple el arnes.**
>
> **LO QUE NO SE AFLOJA, Y VA CON SU CASO POSITIVO:** quitar el adorno afloja el
> **formato**, no la **exigencia**. Una apertura sin declaracion **sigue cayendo**, por
> muy bien maquetada que este, y una huella ajena decorada **tampoco cuela**. Las dos van
> probadas en `PruebaHerencia` (13 pruebas), y el banco de pruebas del arnes escribe ahora
> sus lineas **en el markdown de la casa**, que es la forma en que fallo.

### Lo que esta regla NO hace

**NO cumple el remedio por el auditor.** El arnes entrega y exige la declaracion; **quien
cumple sigue siendo el auditor, y quien lo verifica sigue siendo el fundador.** Lo que
deja de ser posible es **perder un remedio por no haber ido a buscarlo.**

**Y NO BORRA NADA DE LA RACHA.** `D.38.2` sigue entera, con sus dos especies y sus tres
escalones. **La racha se reinicia a 0 de 3 una sola vez**, por esta decision y con esta
condicion mecanica puesta; **el siguiente `REMEDIO ROTO` acumula como cualquier otro.**

## D.41. LA TABLA QUE DICE SER DE INSTRUMENTO ES LA DEL INSTRUMENTO (13 sep 2026, decision del fundador)

*Punto 1 de la decision del fundador del 13 sep 2026, sobre la parada de la vuelta 22,
archivada en `docs/loop/paradas/2026-09-13-la-tabla-tecleada.md`. **La racha `REPORTE`
del extractor se reinicia CON ESTA CONDICION MECANICA PUESTA ENCIMA**, que es la forma
que ya funciono en la otra casa y la que funciono aqui con `D.40`.*

### CUATRO CAIDAS EN CUATRO VUELTAS, Y LAS CUATRO ERAN LA MISMA COSA

| vuelta | que se publico | que decia el instrumento |
|---|---|---|
| **19** | una fila de rutas | otra |
| **22** | la tabla de frontera de `cap_11`, **14 de sus 18 filas** | el fichero la tenia impresa, bajo el titulo `LA TABLA, IMPRESA Y NO TECLEADA` |
| **22** | el saldo de la aduana: `10 ENTRARIA`, `7 BLOQUEARIA` | los diecisiete informes dicen **`9` y `8`** |
| **22** | `11` pares distintos, `8 SANO` y `3 CONTINUA` | son **`12`**, `8 SANO` y **`4 CONTINUA`** |

**Y LO QUE LO CIERRA: EN LA MISMA VUELTA, EL MISMO REPORTE LLEVABA UNA TABLA PEGADA Y
UNA TECLEADA.** La de `cap_10` reprodujo al digito; la de `cap_11` tenia 14 filas
falsas. **La diferencia no fue el cuidado: fue el metodo.**

**NI UNA DE LAS CUATRO MOVIO UN DATO.** El grafo, la bitacora, los veredictos y las
fronteras estaban bien. **Lo que estaba mal era la cuenta de lo que se habia hecho**, y
no era inocuo: quien sumara la columna publicada de `cap_11` obtenia `7345` y concluia
que la frontera **no cierra**, que es lo contrario de lo que pasa.

> ### **UNA REGLA QUE SE CUMPLE TECLEANDO CON CUIDADO NO ES UNA REGLA: ES UNA INTENCION.**

### La letra

> **TODA TABLA QUE EL REPORTE DECLARE COMO SALIDA DE UN INSTRUMENTO (fronteras, censos,
> conteos de pasos, aristas) SE COMPARA CELDA A CELDA CONTRA LA SALIDA DE ESE
> INSTRUMENTO.**
>
> **UNA TABLA QUE DIFIERE ABORTA EL COMMIT, NOMBRANDO LA FILA.**
>
> **Y SE CORRIGE REGENERANDO, NUNCA TECLEANDO LA CELDA BUENA.**

| pieza | donde |
|---|---|
| el tallador | `scripts/tallar_reporte.py` |
| el cierre | `scripts/cerrar_reporte.py`, en el cierre de cada vuelta (**estricto**) y en `hooks/pre-commit` (modo corto) |
| como se declara | la prosa que esta casa ya escribe (*Salida de `X`, guardada en `Y`*) o el marcador `<!-- TALLADO: script=X salida=Y -->` |
| como se arregla | `python scripts/tallar_reporte.py --arreglar`, y la correccion se declara citando la caida |

### Lo que la guarda NO hace, y cada linea tiene su motivo medido

**NO CORRE NINGUN INSTRUMENTO POR SU CUENTA.** Compara contra **el fichero de salida
guardado**. Los instrumentos de una vuelta **escriben** (`.t1_v22/lote_a.py` crea
candidatos en `cuarentena/`) y **llaman a la aduana**, que cuesta minutos por candidato:
**un hook que re ejecuta lo que encuentra escrito en un documento no es una guarda, es
una bomba.** Correr el instrumento es una orden explicita (`--regenerar`) y el hook no
la da nunca. **Coste medido del hook entero: 1,3 segundos.**

**NO MIRA LAS TABLAS QUE NO DECLARAN NADA.** El reporte tiene **705 tablas** y **8**
dicen venir de un instrumento. Medir las 705 contra nada convertiria cada commit en un
campo de minas, y la regla es sobre las que **dicen** venir de un instrumento.

**NO CONFUNDE CITAR CON REPRODUCIR.** Una tabla de resumen puede traer dos filas que
salen de un instrumento y diez que no: se declara `<!-- TALLADO: parcial ... -->` y
queda como **CITA**, listada en cada corrida para que se vea. **La primera version de
esta guarda se lo hizo a si misma con su propia correccion**, y por eso la distincion
esta escrita.

**Y UN RE FLUJO DE ESPACIOS NO ES UNA CIFRA FALSA.** Que el instrumento alinee con dos
espacios y el markdown con uno no cambia ningun dato. **Una guarda que grita donde no
hay nada enseña a no mirarla**, que es la unica forma segura de que nadie la mire.

### Caso positivo, y es el que la decision pidio por su nombre

> **LA TABLA DE LA VUELTA 22, TAL COMO QUEDO, CAE NOMBRANDO SUS 14 FILAS. REGENERADA,
> PASA.**

Corrido el 13 sep 2026, antes de tocar el reporte: `14 fila(s) distintas de su
instrumento`, con su fila, su columna y los dos valores. Tras `--arreglar`: `TALLADO
VERDE`. Mas **13 pruebas de unidad** (`PruebaTallado`), entre ellas que una celda
tecleada cae con su fila y su columna, que una tabla sin declaracion no se mira, y que
citar un fichero cerca **no** es declarar que la tabla salga de el.

### Lo que esta regla NO arregla, y conviene decirlo

**No comprueba que el instrumento tenga razon.** Comprueba que la tabla sea la suya. Un
instrumento mal escrito publica una tabla mal escrita, y eso lo caza una lectura, no un
`diff`. **Lo que esta regla cierra es el hueco entre lo que la maquina midio y lo que el
documento dice que midio**, que es donde cayeron las cuatro.

## D.42. LA UNIDAD DE LA RUTA ES LA CELDA (15 sep 2026, decision del fundador)

*Punto 1 de la decision del fundador del 15 sep 2026, sobre la parada de la vuelta 25,
archivada en `docs/loop/paradas/2026-09-15-la-ruta-vacia-DECISION.md`. **La racha
`REPORTE` del extractor se reinicia con esta condicion instalada y corriendo en el
hook**, que es la forma que ya funciono con `D.40` y con `D.41`.*

### POR QUE `D.41` NO BASTABA, Y NO ES QUE ESTUVIERA MAL ESCRITA

**`D.41` ata un instrumento a una TABLA ENTERA**: lee la declaracion de encima
(*Salida de `X`, guardada en `Y`*) y compara la tabla contra `Y`. La vuelta 25 **no
cayo asi**. Cayo publicando una ruta **por fila**, en una columna titulada *de donde
sale*:

    | los pares del candidato parado | 2 por leer | `.v25/cola_lectura.txt` |

y ese fichero tenia **CERO BYTES** mientras la cifra decia `2` donde el instrumento da
`4`. **La unidad de `D.41` es la tabla; aqui la unidad es la celda**, y por eso hizo
falta otra guarda y no un parche a la primera.

### La letra: TRES FORMAS Y SOLO TRES

> **TODA RUTA PUBLICADA EN UN REPORTE O UN ACTA COMO SEDE DE UNA CIFRA** (en tabla, en
> columna *de donde sale*, o en linea) **LA VERIFICA EL CENSO EN EL COMMIT, CELDA A
> CELDA:**
>
> | | |
> |---|---|
> | **(a) RUTA CON CONTENIDO** | pasa |
> | **(b) RUTA VACIA** (o que no esta) | **TUMBA**, salvo que la MISMA celda lleve la marca literal `VACIA A PROPOSITO: <motivo>`. Una ruta vacia sin marca es **caida de cifra** (cosecha `7.B`) |
> | **(c) PATRON** | la celda lo escribe como `PATRON: <glob>` y se exige **al menos una coincidencia con contenido**. Un patron sin coincidencias tumba |
>
> Mas una **lista FIJA** en `config/sedes_vacias.json` con las sedes que una regla
> escrita manda dejar vacias, que el censo no cuenta.

**POR QUE LA MARCA VA EN LA CELDA Y NO EN UN FICHERO DE EXCEPCIONES.** Una excepcion
escondida en `config/` la lee quien va a buscarla; **una marca en la celda la lee quien
lee la cifra**, que es justo el que tiene que saber que la sede esta vacia. Y obliga a
escribir el motivo **al lado del numero que sostiene.**

**Y POR QUE LA LISTA DE `config/` ES FIJA Y CORTA.** Ahi solo entra lo que **una regla
escrita manda dejar vacio**, con su cita: hoy solo `docs/loop/PROMPT_SIGUIENTE.md`, que
`AUDITOR_FORJA.md` `3` manda vaciar en una parada. **Esta vacio porque el auditor
cumplio, y contarlo como caida seria castigar el cumplimiento.** Una exencion que crece
sola deja de ser exencion y pasa a ser la regla.

### Que es SEDE y que es solo NOMBRAR, porque la diferencia era la guarda entera

La letra dice **como sede de una cifra**, y eso no es toda mencion. Una frase que
**habla** de un fichero (*el barrido de guiones tumbo `.c9/mk.py`*, *los cinco
`.frag_*.md`*) no esta ofreciendo nada como origen de ningun numero: **es el sujeto de
la frase.**

> **SE CUENTA COMO SEDE cuando la CELDA ES la ruta** (la forma de la columna *de donde
> sale*) **o cuando la unidad la OFRECE como origen** (*salida de*, *guardada en*, *de
> donde sale*, *medido con*, *su testigo lo prueba*, *como prueba*).

**MEDIDO EL 15 sep 2026, y por eso la distincion esta escrita:** censar toda mencion da
**902 rutas y 42 celdas que marcar** en dos documentos de treinta mil lineas, casi
ninguna sosteniendo una cifra. Censar las sedes da **293 rutas**. **Una marca que se
pone cuarenta veces deja de leerse**, y a la quinta se pone sin mirar: seria fabricar
exactamente la excusa que esta regla vino a cerrar.

### Dos resoluciones que son regla de la casa, no excepciones

| | |
|---|---|
| una ruta **relativa al documento** | un acta que vive en `docs/loop/` y escribe `paradas/2026-09-13-....md` **no publica una ruta falsa**: escribe una relativa, y resuelve |
| un candidato **insertado** | `D.31` lo archiva en `cuarentena/_insertados/<lote>/` **en el mismo acto de insertarlo**. El acta que lo cito en su bandeja publico la unica ruta que habia; el fichero sigue en el arbol un nivel mas alla. **Pedirle al auditor que vuelva sobre su acta de hace cuatro vueltas cada vez que un candidato entra seria castigar la insercion** |

### Casos, y son los que la decision pidio por su nombre

| | |
|---|---|
| **POSITIVO** | `.v25/cola_lectura.txt` **sin marca y en cero bytes TUMBA nombrando la celda** (`docs/loop/REPORTE.md` linea 30980, `celda 3`). Con la marca, o regenerada con sus `4`, pasa |
| **NEGATIVO** | `.barrido_C_con_ensayo_v16.txt` **con su marca y su cita de la `ACTA 15` `1.9` pasa** |
| **NEGATIVO** | `.aduana_v22/*.txt` **declarado `PATRON` pasa**, con sus 17 coincidencias |

Mas **16 pruebas de unidad** (`PruebaCensoDeRutas`), entre ellas que la marca **sin
motivo** no vale, que la marca **de otra celda** no cubre esta, y que una ruta
**nombrada** en prosa no se cuenta.

### Lo que la guarda NO hace

**NO corre ningun instrumento.** Solo mira ficheros que ya estan escritos: **el hook
entero cuesta 1,75 segundos.**

**NO dice que la cifra sea correcta.** Dice que **la sede que la sostiene sostiene algo**.
Una cifra falsa con su fichero lleno pasa el censo y la caza una lectura. **Lo que esta
regla cierra es el hueco entre la cifra y su prueba**, que es donde cayo la vuelta 25.

### Una cosa que la letra no preveia, y se declara

**CERO COINCIDENCIAS ES A VECES LA CIFRA.** `cuarentena/_insertados/*.json` da `0`
**porque ahi no cuelga ningun JSON suelto**, y eso es exactamente lo que su fila
publica. La letra dice que un patron sin coincidencias tumba; **se resuelve con la
misma marca**, que sigue exigiendo el motivo escrito al lado. **Se anota aqui porque es
una lectura mia de un caso que la decision no nombra**, y el fundador puede tumbarla.

## D.43. EL INFORME DE LOTE VIVE DONDE CABE, Y NO CABE EN UN TURNO (12 sep 2026, decision del fundador)

*Punto 2 de la decision del fundador del 12 sep 2026.*

> ### RENUMERADA DOS VECES. **FUE `D.41`, LUEGO `D.42`, Y HOY ES `D.43`.**
>
> El numero se lo puse yo el 12 sep porque el fundador no numero su decision, y lo
> escribi con esta condicion: *si el numero estorba, se renumera.* **Estorbo el 13
> sep**, cuando el fundador asigno `D.41` al tallado, **y volvio a estorbar el 15**,
> cuando asigno `D.42` al censo de rutas. **El numero del fundador manda sobre el
> mio, las veces que haga falta.**
>
> **El texto viejo no se borra y el contenido no cambia**: lo unico que cambia es el
> numero. Si encuentras un `D.41` o un `D.42` que hablan del informe de lote en un
> acta o un reporte de las vueltas 21 a 25, **son esta, y esta aqui.**
>
> **Y LO DIGO PARA QUE SE PUEDA DECIDIR:** una regla que se ha movido dos veces en
> tres dias es una regla cuyo numero nadie puede citar de memoria. **Si el fundador
> quiere fijarlo, este es el sitio**; yo no me asigno otro numero por mi cuenta.

### La cifra que lo obliga

**`CHOCAN entre si dentro del lote` es la unica salida del informe que un informe de
uno en uno NO PUEDE VER**, porque el choque es **entre dos candidatos del mismo
lote**, y de uno en uno nunca hay dos. Toda la campaña la ha publicado el informe de
lote entero.

### Y el informe de lote entero no cabe en un turno. Medido, no supuesto

    2 candidatos contra el grafo (203)              193 s   ->   96,5 s cada uno
    2 candidatos contra grafo mas bandejas (286)    313 s   ->  156,5 s cada uno

**Mas de TRES HORAS para los 83 del lote 4.** Ni el extractor de la vuelta 20 ni el
auditor pudieron terminarlo: `.aduana_v20/informe_lote_cap09_v2.txt` quedo en **480
bytes, solo la cabecera.** **No es lentitud de un modelo: es el coste del
instrumento**, y pedirselo a un turno es pedirle que falle.

### La letra

> **EL ARNES CORRE EL INFORME DE LOTE EL MISMO, COMO PASO PROPIO, ANTES DEL TURNO DE
> INSERCION DE UN LOTE CERRADO (`D.39`), SIN RELOJ DE MODELO, y le entrega al
> extractor EL FICHERO SELLADO CON SU HASH.**
>
> **EL EXTRACTOR NO LO RECOMPUTA: LO CITA.**

| pieza | donde |
|---|---|
| se pide | `INFORME_DE_LOTE=cuarentena/<lote> bash orquestador_forja.sh` |
| el fichero | `docs/loop/INFORME_DE_LOTE.txt` |
| el sello | `git hash-object`, registrado en `docs/loop/SELLOS_INFORME.jsonl` con su vuelta, su lote y **sus segundos** |
| el mandato | el prompt del extractor lleva el fichero, su sello, y **NO LO RECOMPUTES: CITALO** |

**VACIO POR DEFECTO, Y ES DELIBERADO.** `D.39` dice con estas palabras que **el
arnes no puede comprobar que un lote este cerrado** ni lee actas. **Quien lo sabe lo
nombra al lanzar**, igual que con `MODO_INSERCION`. **Una ruta que no existe detiene
el arnes antes de gastar un turno**, en vez de entregar un informe vacio; y **sin
lote que informar el paso se salta Y SE REGISTRA en el log**, porque un paso que se
salta en silencio es un paso que nadie puede echar en falta.

**EL INFORME DE UN CANDIDATO SUELTO SIGUE SIENDO DEL EXTRACTOR**, en el mismo acto
en que lo escribe (`EXTRACTOR.md` 12). Lo que se saca del turno es **el del lote
entero**, y solo ese.

**Casos positivos:** escenarios **15**, **15b** y **15c** de `tests/prueba_arnes.sh`,
que comprueban que el sello cae **antes** del turno, que un lote inexistente detiene
la corrida **sin que el extractor corra**, y que sin lote el prompt **no promete un
informe que no existe.**

## D.44. EL CENSO NO DECRECE, Y UNA SOLA CORRIDA ESCRIBE EL DATASET (16 sep 2026, decision del fundador)

*Punto 1 de la decision del fundador del 16 sep 2026, sobre la parada de la vuelta 29,
archivada en `docs/loop/paradas/2026-09-16-el-cerrojo-y-el-testigo-DECISION.md`.*

### LA CAIDA, Y ES LA PEOR FORMA QUE ESTA CASA HA VISTO

**UN NODO ENTRO EN EL GRAFO Y DESAPARECIO, CON EL `gate` EN VERDE ENCIMA.** La vuelta 28
lanzo dos `insertar` a la vez: el segundo escribio su nodo, y el primero, que **habia
leido el dataset ANTES**, volco su propia copia en memoria **dejando fuera lo que el
segundo habia metido.**

> **UN GRAFO AL QUE LE QUITAN UN NODO ENTERO SIGUE SIENDO COHERENTE, solo que mas
> pequenio.** Las doce guardas lo miraban todo menos eso. **Lo cazo el extractor con una
> resta que no cuadro por uno.**

**`EXTRACTOR.md` 2 manda UN CANDIDATO POR VEZ desde que existe.** Es la tercera vez que
esta casa encuentra la misma figura: **una regla escrita que no llego a `src/`** (`D.29` a
la aduana, `D.38.5` a la aduana, y esta).

### PRIMERO EL DATO: lo que se busco antes de construir nada

**EL FUNDADOR MANDO RECUPERAR EL NODO BORRADO. NO HABIA NADA QUE RECUPERAR, y se declara
con su medida en vez de con una ceremonia:**

    $ (censo del dataset en los 27 commits que lo tocan)
      222 -> 224 -> 226 -> 227 -> 229 -> 234 -> 234 -> 237 -> 239 -> 240 -> 241 -> 243
      nodos perdidos entre un commit y el siguiente: 0

    $ grep -c '"id": "crear_obligacion_disentir_equipo"' dataset/nodos.jsonl   ->  1
    $ (commit donde entro definitivamente)  32fa203
    $ (lineas suyas en bitacora/VEREDICTOS.jsonl)                             ->  21

**LA PERDIDA VIVIO SOLO EN EL ARBOL DE TRABAJO, ENTRE DOS ORDENES, Y EL EXTRACTOR LA
REPARO ANTES DE COMMITEAR.** El `32fa203` es a la vez el commit donde el nodo entra y el
que declara la caida. **Ningun commit de esta casa ha perdido nunca un nodo.**

### Las dos redes, a dos alturas distintas

| pieza | que impide | sede |
|---|---|---|
| **el cerrojo** | que la perdida **ocurra** | `src/cerrojo.py`, tomado en la entrada de `insertar` |
| **`D.44`** | que una perdida **llegue a un commit** | `src/gate.py`, guarda `censo_no_decrece` |

> **LA LETRA.** Si un nodo que estaba en el dataset del commit anterior **falta en el arbol
> que se va a commitear**, y **no esta marcado `deprecado` con su motivo** (`D.17`), **el
> gate cae nombrandolo.**

**EL CERROJO ENVUELVE LA CORRIDA ENTERA, no solo la escritura**, y el motivo es la caida
misma: **el dano no fue escribir a la vez, fue LEER antes y escribir despues.** Un cerrojo
que cubriera solo el `write` no habria salvado nada. Quien no lo consigue **espera**; no
pisa, y no se salta el turno de nadie. **Un cerrojo huerfano se rompe, pero nunca en
silencio**, y se dice si el proceso no existe o si no se pudo comprobar.

### Casos positivos, que es lo que hace que esto guarde algo

| | |
|---|---|
| **el cerrojo** | con el cerrojo tomado, **el segundo no entra**; y se suelta aunque lo de dentro reviente, **porque un cerrojo que se queda puesto bloquea la casa para siempre** |
| **`D.44`** | quitar `crear_obligacion_disentir_equipo` del arbol, **que es el nodo de verdad que la vuelta 28 perdio**, tumba el gate nombrandolo. **Antes salia VERDE** |
| **negativo de `D.44`** | el arbol tal como esta **pasa**, y un nodo marcado `deprecado` **pasa**: `D.17` dice que no se borra, se marca |

**12 pruebas** entre las dos (`PruebaCerrojoYCenso`).

### Lo que `D.44` NO hace, y conviene no venderlo de mas

**NO habria cazado la caida de la vuelta 28**, porque el extractor la reparo antes de
commitear. **Esa la caza el cerrojo.** `D.44` es la red de abajo: la que se entera cuando
la de arriba falla.

---

## D.45. EL PARALELO EXTRAE, EL SERIAL INSERTA (16 sep 2026, decision del fundador)

*Decision del fundador del 16 sep 2026. **Es la regla que abre la extraccion en paralelo
por libro**, y lo que la hace posible es que separa dos actos que hasta hoy corrian juntos.*

### Por que se puede paralelizar la extraccion y NO la insercion

| acto | que toca | se puede en paralelo |
|---|---|---|
| **EXTRAER** | escribe en `cuarentena/<libro>/`, **ficheros nuevos y disjuntos**, uno por candidato | **SI** |
| **INSERTAR** | escribe en `dataset/nodos.jsonl`, `bitacora/`, `censos/` y `config/pares_mutuos.jsonl`, **que son sedes UNICAS y compartidas** | **NO** |

**Y NO ES UNA PRECAUCION TEORICA: ES LA CAIDA DE LA VUELTA 28.** Dos `insertar` a la vez,
y un nodo entro y desaparecio **con el `gate` en VERDE encima**. Por eso existe
`src/cerrojo.py`, y por eso esta regla **no se apoya solo en el cerrojo**: el cerrojo
impide que dos escrituras se pisen, **no hace que dos lecturas del grafo midan lo mismo.**
Cada insercion cambia lo que la siguiente mide (`D.36`, el orden que lee), asi que **dos
inserciones en paralelo no son la misma campania corriendo mas deprisa: son dos campanias
distintas.**

### La letra

> **LA EXTRACCION DE LIBROS DISTINTOS PUEDE CORRER EN PARALELO**, una rama y una carpeta
> por libro, **siempre en `MODO_INSERCION=cuarentena`.**
>
> **LA INSERCION ES SERIAL Y UNICA:** una sola sesion, en la rama de insercion, **de un
> libro por vez, con gate entre libros.**
>
> **DURANTE EL PARALELO RIGE MORATORIA DE MAQUINARIA Y DOCTRINA:** ninguna sesion toca
> `src/`, el banco, el arnes ni los protocolos. **Una pregunta de doctrina es PARADA y
> sube al fundador.**

### Por que la moratoria de doctrina, y no solo la de maquinaria

**Tres sesiones que corrigen la misma regla a la vez producen tres doctrinas.** El banco
es una sede unica igual que el dataset, y **una regla escrita dos veces en paralelo es
peor que una regla que falta**: la que falta se nota. **Por eso una pregunta de doctrina
no se resuelve en un frente: se para y sube.**

**Y LA MORATORIA DE MAQUINARIA YA EXISTIA** (`EXTRACTOR.md` 13, cosecha `7.F`). Lo que esta
regla anade es que **en paralelo no admite ni la excepcion de la caida de dato**: un frente
que encuentre una caida de dato **la declara y para**, porque arreglar `src/` en tres ramas
a la vez es exactamente lo que la cosecha siguiente no sabria fundir.

### La guarda, que es lo unico que el arnes puede comprobar

> **AL ARRANCAR, SI `MODO_INSERCION=insertar`, LA RAMA ACTIVA TIENE QUE SER LA RAMA DE
> INSERCION. Si no lo es, el arnes se detiene.**

**El arnes no sabe que es un libro ni que es un frente**, igual que no sabe que es un lote
cerrado (`D.39`). Lo unico que puede comprobar sin leer nada es **donde esta parado y con
que permiso corre**, y eso basta para que **ninguna rama de libro pueda insertar por
accidente.** Se declara con `RAMA_DE_INSERCION`, que por defecto es
`extraccion-mundo-11`.

**Caso positivo:** con `MODO_INSERCION=insertar` en una rama que no es la de insercion,
**el arnes se detiene y nombra las dos ramas**. **Negativo:** en cuarentena corre en
cualquier rama, que es lo que el paralelo necesita.

### El procedimiento de cosecha va escrito aparte

**`docs/loop/PARALELO.md`**: como se lanza cada frente, la regla de que ninguno inserta, y
**como se funde cada rama de libro a la rama de insercion**, una por vez, con gate y suite
detras de cada una.

---

## D.46. UNA CIFRA VALE EN EL INSTANTE DEL SELLO (16 sep 2026, decision del fundador)

> ### RENUMERADA EL MISMO DIA. **ERA `D.45` Y PASA A `D.46`.**
>
> El numero se lo puse yo esta manana, porque el punto 2 de aquella decision no venia
> numerado. **El fundador asigno `D.45` por la tarde a otra regla**, y el numero del
> fundador manda sobre el mio. **El contenido no cambia; solo el numero.**

*Punto 2 de la decision del fundador del 16 sep 2026. **La racha del auditor se reinicia
con esta condicion mecanica encima**, que es la forma que ya funciono con `D.40`, `D.41` y
`D.42`. Ensancha `D.38.3`.*

### El caso, con sus horas

| | |
|---|---|
| `09:57:02` | el auditor corre el barrido de guiones. **VERDE**, y pega la salida literal |
| `10:41:02` | se sella la pagina, que publica **`guardas en rojo: 2`** |
| `10:41:05` | el `pre-commit` imprime **cinco guiones largos** metidos por los ficheros de trabajo del propio auditor, y **aborta el commit del sello** |

> **LA CIFRA ERA CIERTA AL MEDIRSE Y FALSA AL PUBLICARSE**, y ninguna regla cubria eso:
> `D.38.3` exige que la cifra **tenga** instrumento, **no que el instrumento siga siendo
> cierto al publicar.** Cuarenta y cuatro minutos en medio.

### La letra

> **AL SELLAR LA APERTURA CIEGA, EL ARNES CORRE LAS GUARDAS Y DEJA JUNTO AL SELLO LA
> VERDAD DEL ARBOL EN ESE INSTANTE**: la hora, la salida de cada guarda y el hash del
> arbol.
>
> **SI UNA GUARDA ESTA EN ROJO EN EL INSTANTE DEL SELLO, EL SELLO NO SE ACEPTA**, y el
> arnes se detiene nombrandola.

**POR QUE NO SE LEE LA PAGINA, Y ES UNA LECCION QUE COSTO UN INTENTO.** La primera version
comprobaba *si el testigo dice rojo y la pagina no lo dice, se rechaza*. **No servia:** en
una pagina de seiscientas lineas que habla de las guardas, cualquier heuristica encuentra
una linea con `guion` y `rojo` cerca. **Probada contra la pagina de la vuelta 29, la daba
por buena.** Una guarda que se deja convencer por la prosa no guarda nada.

**ASI QUE SE MIDE EL ARBOL Y NO EL TEXTO.** Un rojo al cerrar significa que la pagina
cerro **sobre un arbol que ya no era el que midio**, y eso vale para cualquier cifra suya,
no solo para las que hablen de guardas. **El remedio que el propio auditor se escribio
dice lo mismo por el otro lado:** *la tabla de cierre se escribe DESPUES de volver a
correr las guardas.* **Si al sellar hay un rojo, esa tabla no se escribio despues.**

**Con este testigo, la caida de la vuelta 29 habria sido VERDE a las `09:57` y DETENIDA a
las `10:41` por la maquina**, con el nombre de la guarda delante y **sin gastar una
racha.**

**Sede:** `scripts/testigo_guardas.py`, cableado en `apertura_ciega()` antes del sello, con
su parada propia. **4 pruebas** (`PruebaTestigoDeGuardas`), con su caso positivo (una
guarda en rojo no deja sellar) y su negativo (todo verde sella).

**LO QUE NO HACE:** no comprueba que las cifras de la pagina sean ciertas. **Hace imposible
que una medida caduque sin que quede constancia de que caduco.** Lo demas lo caza una
lectura.

## D.47. MODO AUSTERO DE LA FORJA (16 sep 2026, decision del fundador)

*Vigente **hasta que se cierre el mundo 11**. Punto 2 de la decision del 16 sep 2026.*

> **EL AUSTERO RECORTA TINTA, NO CONTROL.**

### Lo que encoge

| | |
|---|---|
| **el reporte y el acta** | **nada que el registro ya diga**; cifras talladas; **los discutibles por numero y linea**, sin reabrir el argumento |
| **los lotes** | **al techo de candidatos** (`EXTRACTOR.md` 12.4), no por encima |
| **los instrumentos** | **CERO nuevos**, salvo que una caida **de DATO** lo exija **con su cita** |

### Lo que NO se toca, y es la mitad que importa

**LAS GUARDAS DE DATO QUEDAN INTACTAS:** el cerrojo (`D.44`), el censo no decreciente
(`D.44`), la aduana entera con sus tres señales y sus doce guardas, y la fidelidad `D.30`
con su relectura contra el parrafo.

> **UN REPORTE MAS CORTO NO ES UN REPORTE CON MENOS PRUEBA.** Lo que se quita es la
> repeticion: lo que el `loop.log` ya registro, lo que el acta anterior ya adjudico, el
> argumento que ya esta escrito en el banco. **Lo que no se quita nunca es la cifra con su
> instrumento al lado** (`D.38.3`), **la tabla pegada de su fichero** (`D.41`) **ni la ruta
> que sostiene lo que dice sostener** (`D.42`).

**POR QUE AHORA.** La campania va por el `45` por ciento de un lote de `142` y quedan
**cuatro libros**. Un reporte de treinta mil lineas no es un registro mejor: **es un
registro que nadie relee**, y el propio auditor lleva tres actas midiendo que lo que se
pierde no es la cifra, **es el encargo que no llego.**

---

## D.48. LA RACHA ES DE SU LINEA (17 sep 2026, decision del fundador)

*Decision del fundador del 17 sep 2026, puntos 1 y 2. **Cierra un hueco que no se podia
cerrar por extension**, y por eso no es una aclaracion de `D.38`: es regla nueva.*

### Quien levanto el hueco, y por que no lo resolvio

**El auditor del frente `gerber_emyth`**, el 16 sep 2026, parando por `DOCTRINA NUEVA
NECESARIA` en vez de elegir la lectura que le convenia:

> *`5.2` y `D.38.1` cuentan tandas **seguidas**, y seguidas significa consecutivas. Pero
> **cuatro sesiones simultaneas no tienen orden entre si**, asi que la palabra que
> sostiene la regla **no tiene referente aqui**. No es una regla que se pueda extender:
> **es un hueco.***

Y midio su propia posicion antes de negarse: su rama salio del commit `269c068` a las
`20:46`, la linea serial declaro su parada a las `22:21`, **y su arbol no puede ver esa
acta**. Las dos salidas, escritas por el con sus consecuencias opuestas:

| lectura | `REPORTE` tras su tanda | que pasa con los tres frentes |
|---|---|---|
| **(a)** la racha del extractor es UNA sola de la campania | sigue en `3 de 3` | **los tres frentes estan corriendo por encima de una parada** |
| **(b)** cada frente lleva la suya | `1 de 3` | los frentes siguen, y la parada es solo de la rama serial |

> **Elegir `(b)` seria absolverme para poder seguir. Elegir `(a)` seria cargarle a este
> frente tres tandas de un libro que no es el suyo.**

**QUEDA CITADO COMO QUIEN LO LEVANTO.** Esta regla existe porque un auditor prefirio
parar a elegir, teniendo delante la lectura que le dejaba seguir.

### La letra

> **CADA LINEA DE TRABAJO LLEVA SU PROPIA RACHA.** Una racha cuenta tandas **SEGUIDAS**,
> y **una secuencia solo existe dentro de una linea**: entre sesiones simultaneas no hay
> orden, asi que fuera de su linea la palabra no tiene referente.
>
> **UN FRENTE NACE CON SU RACHA EN CERO**, porque no ha dictado nada todavia.
>
> **LA RACHA DE LA SERIAL NO VIAJA A LOS FRENTES NI AL REVES.**
>
> **AL COSECHAR UN FRENTE, SU RACHA MUERE CON EL FRENTE.** Sus caidas quedan como
> registro en sus actas archivadas, **y no se suman a la serial.**

### Por que la racha muere al cosechar, y no se suma

**Una racha no es una deuda: es una sonda.** Mide si una linea de dictado esta
repitiendo un patron **mientras dicta**, para pararla a tiempo. Un frente cosechado ya
no dicta: lo que queda de el es su trabajo, ya auditado, y sus actas. **Sumar sus caidas
a la serial pararia a la serial por tandas que la serial no corrio**, que es exactamente
el error de la vuelta 32 del frente `grove`, al reves.

**Y LA CAIDA NO SE PIERDE:** queda escrita en el acta del frente, archivada con su
cosecha. Lo que muere es el **contador**, no el **registro**.

### La segunda mitad, que es la que sostiene la primera: OPCION B

> **EL CREDITO VIVE EN UN FICHERO POR LINEA: `docs/loop/CREDITO_<linea>.jsonl`, LA
> SERIAL INCLUIDA** (`CREDITO_serial.jsonl`), **con la especie, la vuelta, la tanda y su
> cita.**
>
> **Y LA HERENCIA DE `D.40` ES LA DE SU LINEA.**

**POR QUE UN FICHERO Y NO UNA SECCION MAS DEL ACTA.** Una sede unica compartida por
varias lineas **es el problema, no la solucion**: es lo que hizo que tres frentes
heredaran el acta de la serial al ramificar. Un fichero por linea convierte el registro
en lo que ya es el `cuarentena/<libro>/`: **ficheros disjuntos que se funden sin
tocarse**, y borra la unica fila de la tabla de cosecha de `PARALELO.md` que decia
`CONFLICTO SEGURO`.

**LO QUE NO CAMBIA, Y CONVIENE DECIRLO:** `AUDITOR_FORJA.md` 5.4 sigue entero. **La
racha no se reinicia sola**, la reinicia una tanda limpia o una decision del fundador
escrita en `docs/loop/paradas/`, **y ninguna de las dos es el auditor**. Lo unico que
`D.48` cambia es **de quien** es la racha, no **quien** la puede tocar.

### El instrumento

    python forja.py credito             la racha de ESTA linea, con su cita
    python forja.py credito --lineas    que lineas tienen registro
    python forja.py credito --revisar   el replay contra lo declarado
    python forja.py credito --anotar    escribe una tanda, un reinicio o un nacimiento

`src/credito.py`. **La cifra declarada manda y el replay se publica aparte**: `estado()`
devuelve lo que la ultima linea de cada especie declara, que es lo que el acta adjudico;
`revisar()` vuelve a sumar `cae` y **dice donde las dos cuentas discrepan en vez de
elegir una en silencio**. El replay **no vigila la historia migrada**, porque los
reinicios de ese tramo viven en `docs/loop/paradas/` y no en el registro: **una guarda
que acusa de lo que no puede saber es ruido que se aprende a ignorar.**

**Caso positivo:** en una linea sin ninguna tanda cerrada, `forja.py herencia` entrega
**CERO remedios** y dice por que, aunque el arbol tenga las `31` actas de la serial
delante. **Negativo:** en la linea serial, que tiene `31` tandas escritas, entrega sus
`4` remedios como siempre.

### La historia migrada, y lo que la migracion no invento

**`scripts/migrar_credito.py`** volco las `31` actas de la linea serial a
`CREDITO_serial.jsonl`: `127` sucesos, uno por especie y acta, **cada uno con el literal
de su celda al lado** (`D.38.3`). Las actas `1` a `7` escribian la fila del auditor como
*"N actas seguidas"*, que es **otra unidad**, anterior a que `D.38` le diera una racha
sola con tope: sin el literal al lado, aquel `7` se leeria como siete de tres.

**`cae` solo se escribio donde el acta publica sus dos columnas** y se puede restar.
Donde el acta publica una sola cifra, la fila va **sin `cae`**, y el replay la declara no
replayable. **Un migrador que rellena huecos con su criterio no migra: dicta.**

---

## D.49. UN LIBRO, UN DUEÑO A LA VEZ (17 sep 2026, decision del fundador)

*Decision del fundador del 17 sep 2026, puntos 1 y 2. **Nace `docs/loop/TABLERO.jsonl`**,
sede unica del estado de la campania de extraccion.*

### La caida que no llego a ocurrir, y por que iba a ocurrir

**`D.32` dice que el acta que cierra un lote ABRE EL SIGUIENTE, sin parada entre medias**,
con las dos condiciones de apertura en verde. Y estan en verde **para los diez lotes que
quedan.**

El lote `4` iba por el `47` por ciento. **El siguiente por orden es el lote `5`,
`marquet_turn_the_ship`, que estaba siendo extraido en otra rama con `9` candidatos
dentro**, tres de ellos ya en la bandeja de la serial. Si el lote 4 hubiera cerrado, el
acta habria abierto el `5` **y habria vuelto a minar `cap_01`, `cap_02` y `cap_03`**, que
el frente ya cerro con sus fronteras al digito.

> **LO UNICO QUE LO IMPEDIA ERA UNA FRASE ESCRITA A MANO EN EL ENCARGO.** Y esta casa
> tiene medido lo que vale eso: **`D.35`, un remedio que se cumple acordandose no es un
> remedio.**

### El tablero

> **`docs/loop/TABLERO.jsonl` ES LA SEDE UNICA DEL ESTADO DE LA CAMPANIA DE EXTRACCION**,
> una linea por libro con: **clave, rama, worktree, ESTADO, ultimo capitulo minado y su
> commit, candidatos en su bandeja, y quien es su DUEÑO ACTUAL** (la linea que lo
> trabaja) **o `NINGUNO`.**
>
> **SE GENERA DEL DATO** (ramas, bandejas, actas), **no se teclea**, y **se actualiza en
> el cierre de cada vuelta de cualquier linea.**

**LOS SEIS ESTADOS:** `SIN EMPEZAR`, `EN CURSO`, `PAUSADO`, `CERRADO EN EXTRACCION`,
`COSECHADO`, `INSERTADO`.

**LA BANDEJA SE CUENTA EN EL ARBOL DE SU DUEÑO, y esa es la mitad que nadie ve venir.**
Los cuatro worktrees comparten historial, asi que **el arbol de cada frente tiene las
bandejas de los otros libros copiadas**: `cuarentena/marquet_turn_the_ship/` da `3` en la
serial y `9` en su frente. **La cifra buena es la de quien lo trabaja.**

**Y LO QUE EL DATO NO PUEDE DECIR VA DECLARADO CON SU CITA**, en `config/frentes.json`:
cual es el frente activo (**un frente detenido esperando decision sigue teniendo su
libro**, que no es lo mismo que tener proceso vivo) y que libro esta `CERRADO EN
EXTRACCION` (que es la adjudicacion de un acta, no una cuenta de ficheros). **El
instrumento se detiene si una declaracion no lleva cita.**

### La letra

> **NINGUNA LINEA ABRE NI CONTINUA UN LIBRO CUYO `ESTADO` NO SEA:**
>
> - **`SIN EMPEZAR` con dueño `NINGUNO`**, o
> - **`PAUSADO` con dueño `NINGUNO` y ya `COSECHADO`.**
>
> **EL ARNES LO COMPRUEBA AL ABRIR VUELTA CONTRA EL TABLERO Y SE DETIENE NOMBRANDO AL
> DUEÑO** si el libro tiene uno.
>
> **TODA LINEA LEE EL TABLERO EN SU APERTURA Y LO CITA.**

### El instrumento

    python forja.py tablero              lo imprime, medido en este instante
    python forja.py tablero --escribir   lo vuelca a docs/loop/TABLERO.jsonl
    python forja.py tablero --puedo <clave>   si ESTA linea puede abrir ese libro
    python forja.py tablero --dueno <clave>   quien lo trabaja hoy

**Caso positivo:** `--puedo marquet_turn_the_ship` desde la serial **dice NO** y nombra
sus `9` candidatos sin cosechar y la rama donde estan. **Negativo:**
`--puedo openstax_business_ethics` **dice SI**, porque esta `SIN EMPEZAR` y sin dueño.

---

## D.50. EL RELEVO: SE RELEVA EL LIBRO ENTERO, NUNCA CAPITULOS SUELTOS (17 sep 2026, decision del fundador)

*Decision del fundador del 17 sep 2026, punto 3. **Es lo que convierte un frente pausado
en trabajo que la serial puede continuar**, y el orden de sus cuatro pasos es obligatorio.*

### La letra

> **CUANDO LA LINEA PRINCIPAL CIERRA UN LIBRO, CONSULTA EL TABLERO**, y si hay un libro
> `EN CURSO` o `PAUSADO` en otra rama, **lo RELEVA en este orden obligatorio:**
>
> **(a)** el frente **debe estar detenido y sin proceso vivo**;
> **(b)** su rama **se COSECHA a la rama de insercion** (una por vez, gate y suite
> despues), con lo que **sus candidatos, su frontera y sus actas llegan**;
> **(c)** el tablero pasa ese libro a **dueño `NINGUNO` y estado `PAUSADO COSECHADO`**;
> **(d)** **solo entonces** el principal lo toma y **continua DESDE EL CAPITULO SIGUIENTE
> al ultimo minado, citando la frontera heredada.**
>
> **NUNCA SE RELEVAN CAPITULOS SUELTOS: SE RELEVA EL LIBRO ENTERO.**

### Por que el orden es obligatorio y no una recomendacion

**Cada paso existe porque el anterior no basta.**

| paso | que impide que pase |
|---|---|
| **(a) detenido y sin proceso vivo** | que la cosecha lea un arbol **que se esta escribiendo**. El 17 sep un frente que yo di por muerto llevaba **seis horas y media** dentro de un turno de extractor y cerro una vuelta entera despues |
| **(b) cosechar antes de tocar** | que la serial mine **lo que ya esta minado**. Los candidatos del frente no existen en esta rama hasta que se funden: **contarlos no es tenerlos** |
| **(c) el tablero antes de trabajar** | que dos lineas se crean dueñas del mismo libro. **El tablero es la sede, y una sede que se actualiza despues del trabajo no es una sede: es un parte** |
| **(d) desde el capitulo SIGUIENTE, citando la frontera** | que el relevo **repita o se salte** una unidad. La frontera heredada es lo unico que dice donde acaba lo minado, y `D.41` obliga a que venga de su instrumento |

### Por que el libro entero y no el capitulo

**Un libro medio relevado tiene dos fronteras que nadie casa.** El frente cerro las suyas
contra el cuerpo, al digito; un relevo por capitulos obligaria a **volver a cerrar la
frontera del tramo partido**, y eso es rehacer el trabajo con mas sitios donde fallar.
**El libro entero tiene una sola frontera que heredar.**

### Y no releva cualquiera

**EL RELEVO LO HACE LA LINEA PRINCIPAL, y solo cuando CIERRA un libro.** No es una tarea
que se pueda encargar a mitad de lote: `D.45` dice que **la insercion es serial y de un
libro por vez**, y un relevo a mitad de libro es dos libros a la vez por la puerta de
atras.

**EL BUCLE NO FUNDE RAMAS** (`AUDITOR_FORJA.md`, y lo repite cada parada). **El paso
`(b)` lo hace el fundador**, con el procedimiento de `docs/loop/PARALELO.md`. Lo que el
bucle si hace es **pedirlo, nombrando la rama y el estado**, y **detenerse hasta que
llegue**.

### El alcance de hoy, que es parte de la decision

> **DOS LINEAS Y NO MAS:** la principal **siempre activa**, y **UN solo frente de
> extraccion**, hoy `grove_high_output` **hasta cerrar su libro**.
>
> **`gerber_emyth` y `marquet_turn_the_ship` quedan `PAUSADOS` con dueño `NINGUNO`** y su
> trabajo parcial declarado en el tablero (**`10` y `9` candidatos**): **no se lanzan**, y
> **seran relevados por el principal cuando le toquen por el orden.**

**Vive en `config/frentes.json` con su cita**, porque es una decision y no una medida, y
el tablero lo dice en la columna `estado_de` de cada fila que lo usa.

---

## D.51. EL ORDEN LO DA EL TABLERO (17 sep 2026, decision del fundador)

*Decision del fundador del 17 sep 2026, **EL ORDEN DE PRIORIDAD DEL MUNDO 11**. Cierra el
ultimo hueco que quedaba abierto en `D.49` y `D.50`: **saben decir que NO, y no sabian
decir que SI.***

### La letra

> **NINGUNA LINEA ELIGE LIBRO POR SU CUENTA.** Toma el de **PRIORIDAD MAS BAJA cuyo
> estado lo permita** (`D.49`), y **si ninguno lo permite, PARA Y LO DICE.**
>
> **EL ARNES LO COMPRUEBA EN LA APERTURA.**

**Y AL CERRAR UNO, PASA AL SIGUIENTE POR `D.50`**, que es el relevo con sus cuatro pasos.

### El orden, y lleva sus motivos porque un orden sin motivo no se puede discutir

| prioridad | libro | estado al escribirse | por que ahi |
|---:|---|---|---|
| **1** | `grove_high_output` | `EN CURSO`, dueño grove | **Operaciones y apalancamiento gerencial: cubre el hueco de la campania**, que tiene mucho trato con la gente y poco produccion de la maquina. **Densidad de procedimiento la mas alta del lote, medida:** `0,00` por ciento de pasos inventados en su ultimo capitulo, **porque el autor escribe en pasos** |
| **2** | `gerber_emyth` | `PAUSADO`, `10` candidatos hechos | **Sistematizacion del negocio, manual de operaciones, trabajar SOBRE el negocio y no EN el**: es el libro que **habla directo al usuario final** y el unico del lote que aporta esa materia. Al minarlo entero **se completa ademas el capitulo 17 reservado al mundo 10** |
| **3** | `marquet_turn_the_ship` | `PAUSADO`, `9` candidatos hechos | **Delegacion real y control distribuido con practicas concretas.** Solapa en parte con Zhuo y Scott, ya insertados, **pero es barato de cerrar y cierra el cuerpo** |

> # **=== CORTE DEL MUNDO 11 ===**
>
> **Con los tres anteriores mas los cuatro ya insertados** (`onu_consumidor`,
> `smart_who`, `zhuo_manager`, `scott_radical_candor`), **EL MUNDO 11 SE DECLARA
> COMPLETO**: gente, comunicacion, contratacion, operaciones y sistematizacion. **La
> campania de extraccion cierra ahi.**

| prioridad | libro | por que NO entra en esta campania |
|---:|---|---|
| **4** | `bernerslee_bananas` | `19` cap. **Mas analisis que procedimiento** |
| **5** | `openstax_business_ethics` | `17` cap. **Manual academico, densidad de procedimiento baja, mucho marco conceptual** |
| **6** | `openstax_org_behavior` | `32` cap. **El mas caro del lote y el de mayor solape con lo ya insertado** (Zhuo, Scott, Grove): **el peor candidato por costo y beneficio de los diez** |

**LOS TRES DEL CORTE NO SE EXTRAEN EN ESTA CAMPANIA.** Quedan en la bandeja, **con su
ficha**, para **entrar por la aduana de a uno y sin campania cuando el fundador lo
decida.** Ninguna linea los elige sola: **una campania que decide su propio alcance no
tiene alcance.**

### Por que esto es una regla y no una lista

**`D.49` y `D.50` sabian decir que NO.** Sabian que un libro con dueño no se toca y que un
frente pausado se releva entero. **Lo que ninguna de las dos sabia decir es cual SI**, y
ese hueco lo llenaba lo mismo de siempre: el orden de `ORDEN_DE_LOTES.md`, que es el orden
en que los libros **llegaron**, no el orden en que **valen**. Por ese orden, el siguiente
del lote 4 era el lote 5; **por este, el siguiente es el `1`.**

**Y HAY UNA SEGUNDA COSA QUE ESTA REGLA IMPIDE, mas silenciosa:** que una linea que se
queda sin libro **se busque uno.** Con `D.51`, una linea sin libro **no elige: para y
dice cual necesita y que le falta a ese libro para estar disponible.**

### El instrumento

    python forja.py tablero               la tabla, ordenada por prioridad
    python forja.py tablero --siguiente   que libro le toca a ESTA linea, y por que

**La prioridad vive en `config/frentes.json` con su cita**, porque es una decision y no
una medida, y `src/tablero.py` **se detiene si el orden no la lleva.** Cada fila de
`docs/loop/TABLERO.jsonl` publica `prioridad`, `fuera_de_campania` y su `motivo`.

**Caso positivo:** con `scott_radical_candor` ya `INSERTADO` y `grove` todavia vivo,
`--siguiente` **da `NINGUNO` y nombra el relevo que falta**: `gerber_emyth`, prioridad `2`,
rama `extraccion-gerber_emyth` sin cosechar con `10` candidatos dentro. **Negativo:** con
ese mismo `gerber_emyth` ya `COSECHADO`, **da `gerber_emyth` y dice desde que capitulo se
continua** (`cap_11`).

**Y MIENTRAS LA LINEA TIENE LIBRO PROPIO EN CURSO, `--siguiente` DEVUELVE ESE**, porque
`D.50` releva **al cerrar** uno y no a mitad.

---

## D.56. `dataset/` ES EL CATALOGO Y NADA MAS (17 sep 2026, decision del fundador)

> ### RENUMERADA DOS VECES. **FUE `D.52`, FUE `D.53`, Y ES `D.56`.**
>
> **Las dos veces por lo mismo y las dos veces contra mi:** la decision que la creo no
> venia numerada, **le puse un numero yo**, y el fundador uso ese numero despues para otra
> regla. Primero `D.52` (la tabla de cierre), luego `D.53` (el veredicto y la arista). **El
> numero del fundador manda sobre el mio**, igual que con `D.45` y `D.46` el 16 sep. **El
> contenido no cambia: solo el numero.**
>
> **Y LA LECCION ES MIA, NO DEL FUNDADOR:** numerar yo una regla que el fundador dicta sin
> numero **invita a la colision**. Lo que corresponde es escribirla sin numero y pedirlo.
> **Dos renumeraciones del mismo texto en un dia son dos avisos.**
>
> **LO QUE NO SE REESCRIBE, Y SE DICE:** las actas, el reporte y la parada ya archivada
> siguen diciendo `D.52` donde esta regla era `D.52`. **Son registro de lo que se escribio
> cuando se escribio**, y reescribirlos seria borrar historia para tapar una renumeracion
> mia. Lo que si se actualizo es lo que esta sesion mantiene: `src/`, `scripts/`,
> `config/` y las pruebas.

*Decision del fundador del 17 sep 2026 sobre la parada de la vuelta 33. **Tres piezas: la
sede de los ficheros de coordinacion, una reclasificacion de racha, y una correccion
declarada del fundador sobre su propia `D.48`.***

### 1. La letra

> **`dataset/` CONTIENE EL CATALOGO Y NADA MAS.** Los ficheros de coordinacion (el
> cerrojo, las marcas de proceso) **viven fuera, con su ruta escrita.**

**Sede nueva:** `procesos/`, declarada en `comun.DIR_PROCESOS` y **fuera de git**.

**LA HUELLA DE LA RUTA VA EN EL NOMBRE, y no es adorno:** el taller de las pruebas usa un
dataset que **se llama `nodos.jsonl` igual que el de verdad**, y sin la huella las pruebas
y la forja compartirian cerrojo. Se calcula sobre la ruta absoluta normalizada, asi que el
mismo dataset da siempre el mismo fichero: `procesos/nodos.jsonl.66c1fadb.cerrojo`.

### Por que, con la caida delante

El 17 sep 2026 el turno de un extractor commiteo con `git add -A` mientras una insercion
corria, **y el cerrojo VIVO entro en git dentro de `dataset/`**. Un `checkout` de ese
commit entrega **el cerrojo de un proceso que ya no existe**, y la insercion siguiente se
queda esperando a un cadaver hasta que el tope de huerfano lo declara. **No fallo en
silencio** (el cerrojo resuelve la duda por edad y nunca por adivinanza, `D.44`), **pero
costo una espera y una parada que no son de nadie.**

**Caso positivo, re corrido tras la mudanza** (`.v34/cerrojo_dos_procesos.py`): dos
procesos de verdad sobre el mismo dataset, el primero retiene `3` segundos, **el segundo
espera `2,51` y entra**, y el cerrojo queda suelto al final.

### 2. La reclasificacion, y lo que ensena sobre las especies

> **EL EJEMPLAR DEL CERROJO SE RECLASIFICA DE `DATO MOVIDO` A `ARNES`: NO ACUMULA.** La
> racha `DATO MOVIDO` queda en **`1 de 2`**.

**Y EL AUDITOR QUE LA CARGO TENIA RAZON CON LA LETRA QUE HABIA.** La fila de `DATO MOVIDO`
dice *una operacion que cambia `dataset/`, `bitacora/` o `censos/`*, y `git add -A` cambio
lo que `dataset/` contiene en el repositorio. **Eligio la lectura que le costaba el
escalon teniendo la contraria ofrecida.** Lo que cambia no es su adjudicacion: **es la
letra**, porque `dataset/` deja de poder contener un fichero de proceso.

**LA ESPECIE SE DECIDE POR LA SEDE** (`5.2`), y esta regla **limpia la sede** en vez de
discutir el ejemplar. Es la unica via que no deja la pregunta abierta para la proxima.

### 3. La fase ciega no ve el registro de credito

> **CORRECCION DECLARADA DEL FUNDADOR SOBRE `D.48`**, que es suya. **El arnes RETIRA
> `docs/loop/CREDITO_<linea>.jsonl` durante la fase ciega**, como ya retira los otros
> cuatro, y le entrega al ciego **SOLO la herencia que `D.40` exige** (remedios pendientes
> con su motivo y su salida pegada), **sin cifras ni conclusiones.**

**QUIEN LO LEVANTO Y CON QUE MEDIDA:** el auditor de la `ACTA 32`. *La apertura ciega esta
OBLIGADA a leer el registro de credito, y el campo `cita` trae conclusiones del reporte
copiadas dentro. Hoy me dijo `11 SANO` antes de que yo contara los mios.* **El arnes
retiraba cuatro ficheros por una puerta y `D.48` abrio otra.**

**EL ORDEN DE LA RETIRADA IMPORTA, y es la parte que se puede romper sin darse cuenta:**
la herencia `D.40` se calcula **ANTES**, porque `forja.py herencia` **pregunta al registro
de que linea es** (`D.48`). Retirarlo antes haria que `D.40` entregara **CERO remedios
creyendo que la linea acaba de nacer**, que es el defecto que `D.40` vino a cerrar,
reintroducido por la puerta de atras.

### Y la cita se escribe como REFERENCIA

> **EL CAMPO `cita` DEL REGISTRO ES LA RUTA Y LA LINEA DEL ACTA, NUNCA UN RESULTADO
> COPIADO.** Un `cita` con conclusion dentro **no pasa el sello.**

    python forja.py credito --citas

**Va en `anotar` Y en el SELLO**, y las dos hacen falta: `anotar` solo mira lo que se
escribe por el instrumento, y **una linea anadida a mano al fichero no pasaria por ahi**.
El testigo de guardas tiene ahora **cuatro**.

**SE CAZA POR VOCABULARIO Y NO POR DIGITOS**, y esa es la decision de diseno: una
referencia legitima **lleva numeros por todas partes** (`ACTA 33, seccion 9.1`), asi que
contar digitos daria falso positivo en casi todas. Lo que una referencia **no lleva nunca**
es el vocabulario con el que esta casa dice un veredicto: `SANO`, `CONTINUA`, `PUENTE`,
`por ciento`, `al digito`, `verde`, `rojo`.

**Y `de 2` Y `de 3` SE QUEDARON FUERA A PROPOSITO:** cazarian `punto 2 de 3` en una
referencia legitima. **Esta casa ya pago dos veces el precio de una guarda con falsos
positivos: se aprende a no mirarla.**

**Al estrenarla cayeron CINCO citas ya escritas**, todas del auditor que levanto el
defecto. **No se borro ninguna:** el texto entero pasa a `cita_original` y `cita` se queda
con la referencia que ese mismo texto ya traia delante.

### 4. La cola de doctrina

> **Las preguntas de doctrina que no bloquean a nadie quedan EN COLA DECLARADA: se
> resuelven cuando el mundo 11 cierre.** Si alguna **bloquea a una linea, sube sola.**

**Viven en la seccion `COLA DE DOCTRINA` de `docs/loop/TABLERO.jsonl`**, con su medida y su
sitio, **para que no se pierdan**. Una pregunta que se contesta *cuando haya tiempo* y que
no esta escrita en ningun sitio **no esta en cola: esta olvidada.**

---

## D.52. TODA TABLA DEL REPORTE DECLARA SU INSTRUMENTO (17 sep 2026, decision del fundador)

*Decision del fundador del 17 sep 2026 sobre la parada de la vuelta 35, punto 2. **Es la
cura de una especie de credito con TRES tandas medidas**, y por eso viene con una
excepcion expresa a `D.45` para poder construirse.*

### La letra

> **UNA TABLA SIN INSTRUMENTO DECLARADO NO SE PUBLICA**, porque es precisamente **la que
> ninguna guarda mira.**

### El ejemplar, que son tres y son la misma tabla

**La racha `REPORTE` de la linea serial llego a su tope con tres caidas seguidas, y las
tres viven en la MISMA tabla:**

| tanda | vuelta | la caida |
|---|---:|---|
| `ACTA 32` | `33` | `13` vecindades levantadas donde se levantaron `11` |
| `ACTA 33` | `34` | `0` PUENTE de `181` donde la relectura da `1` |
| `ACTA 34` | `35` | `15 de 15 DEL CAPITULO` donde `cap_09` son `20 de 20` |

**LA TABLA DE CIERRE DE TAREAS ERA LA UNICA DEL REPORTE QUE NO DECLARABA INSTRUMENTO.**
`D.41` compara cada tabla contra su fichero de salida; **una tabla sin fichero no se
compara con nada.** Es, literalmente, **el unico sitio del reporte donde una cifra
tecleada vivia tranquila**, y las tres caidas fueron a parar ahi.

> **NINGUNA DE LAS TRES ERA CAZABLE POR DISEÑO**, y esa es la frase que hace falta leer
> antes de culpar a nadie: no fue descuido tres veces. **Fue el unico hueco que quedaba, y
> el dictado lo encontro solo.**

### El instrumento

    python scripts/tabla_de_cierre.py              la comprueba y dice que cae
    python scripts/tabla_de_cierre.py --escribir   regenera su fichero de salida

**Corre en cada commit**, dentro de `scripts/cerrar_reporte.py`, que es lo que el hook
llama. **`hooks/pre-commit` NO se toco**, y es deliberado: mientras haya un frente vivo,
un fichero que esta sesion no mueve **es un fichero que la cosecha de ese frente no puede
encontrar en conflicto.**

**LO QUE SABE MEDIR, Y SOLO ESO:** una afirmacion de la forma **`N` de `M` del capitulo**
con un `cap_NN` nombrado en la misma fila, donde `M` es **cuantos nodos del grafo salen de
ese capitulo**, medido **por la ruta completa** (`<clave>/cap_NN.md`) y no por el nombre
suelto, que aparece tambien en otros libros.

**LO QUE NO INVENTA:** una fila sin cifra medible **se copia tal cual y se declara
`SIN COMPROBAR`**. Y el patron es **estrecho a proposito**: un `5 de 5` de un TRAMO no se
toca, porque un tramo no es un capitulo y **esta casa ya pago dos veces el precio de una
guarda con falsos positivos.**

**Caso positivo:** la tabla de la vuelta `35` **tal como quedo** cae nombrando su fila `3`
(*la celda publica `15 de 15 del capitulo` y `cap_09` son `20 de 20` en el grafo, `272`
pasos*). **Negativo:** regenerada y pegada, pasa.

### La excepcion a `D.45` que hizo falta para construirlo

> **LA MORATORIA DE MAQUINARIA NO CUBRE LA CURA DE UNA ESPECIE DE CREDITO CON TRES TANDAS
> MEDIDAS.** Autorizada **solo en la linea serial**, y **acotada**: toca unicamente
> `scripts/` y el hook de la rama de insercion. **No toca el banco de pruebas, ni los
> protocolos, ni `orquestador_forja.sh`, ni nada que `grove` edite.**

**POR QUE LA EXCEPCION ES SANA, y no un agujero en `D.45`:** `D.45` existe para que dos
lineas no escriban la misma sede a la vez. **Una cura que solo toca `scripts/` de la linea
serial no es una sede compartida**, y dejarla sin construir significaba **abrir la vuelta
36 con el mismo hueco que produjo las tres caidas**. Una moratoria que impide arreglar lo
que esta midiendo mal **deja de proteger y empieza a conservar el defecto.**

---

## D.54. UN PASO RETIRADO POR DECLARACION SE RETIRA DEL CAMPO (17 sep 2026, decision del fundador)

*Decision del fundador del 17 sep 2026, punto 4. **Es la pregunta `7` de la cola de
doctrina, decidida**, y se decide asi porque **es dato y no forma.***

### La letra

> **UN PASO RETIRADO POR DECLARACION SE RETIRA DEL CAMPO.** Un nodo insertado cuyo
> `resumen_teorico` declara retirado un paso **que sigue literal en `pasos_accionables`**
> publica un puente a quien lee los pasos.
>
> **El paso sale de `pasos_accionables`, y su retirada queda escrita con su cita.** Un
> retiro futuro **se aplica en el mismo acto, no solo en la prosa.**

### Por que es dato y no forma

**Un nodo tiene dos lectores y la declaracion solo alcanza a uno.** Quien lee el
`resumen_teorico` se entera de que el paso esta retirado; **quien lee `pasos_accionables`
se lleva el puente entero**, sin saber que fue retirado. Y `pasos_accionables` es el campo
que la maquina consume.

**LA GUARDA QUE PARECIA CUBRIRLO NO LO CUBRE:** `deprecado_en_superficie` vigila
**aristas**, no pasos. El hueco estaba entero.

**Y NINGUN INSTRUMENTO DE LA CASA REESCRIBIA UN PASO DE UN NODO YA INSERTADO**, que es el
motivo real de que la retirada se quedara en la prosa: **no habia por donde hacerlo.**
`forja.py corregir` toca el `resumen_teorico`; el paso no lo tocaba nadie.

---

## D.53. EL VEREDICTO Y LA ARISTA SON PUERTAS DISTINTAS (17 sep 2026, decision del fundador)

*Decision del fundador del 17 sep 2026, punto 2. **Es la pregunta `5` de la parada de
`grove`, decidida**, y `grove` la levanto adjudicando contra si mismo.*

### La letra

> **UN `SANO` PUEDE LLEVAR ARISTA DECLARADA, Y DECLARARLA NO LO CONVIERTE EN `CONTINUA`.**
>
> **El veredicto dice si un par REPITE, CONTINUA o esta SANO en su procedimiento.** **La
> arista dice si hay RELACION DECLARABLE entre los dos.** Son dos preguntas distintas y se
> contestan por separado.
>
> Dos nodos sanos pueden estar unidos **por serie declarada** (`D.37`) o **por jerarquia
> leida** (`D.19`, `D.29`).

### La prueba por reduccion, que es la que cierra la discusion

> **SI UN `SANO` CON ARISTA FUESE `CONTINUA`, `D.37` SERIA IMPOSIBLE: toda cabeza de serie
> devoraria sus partes.**

`D.37` manda declarar arista **de la cabeza a cada una de sus partes** cuando el texto dice
cuantas hay y las nombra. Si declarar esa arista convirtiera el par en `CONTINUA`, **la
cabeza y cada parte serian el mismo procedimiento**, y una serie de diez quedaria reducida
a uno. **La regla que existe desde el 10 sep no podria aplicarse ni una sola vez.**

### Quien la levanto, y como

**El auditor del frente `grove`**, en su `ACTA 32`. La adjudico como `CONTINUA` **porque
`AUDITOR_FORJA.md` 3 le obliga a adjudicar lo que una regla escrita cubre**, y acto seguido
escribio que **si el fundador leia lo contrario, una de sus propias caidas desaparecia**:

> *si tu lees que un `SANO` puede convivir con una arista `D.29`, mi caida de `3.3`
> desaparece y la racha se queda en `4`.*

**ES LA SEGUNDA VEZ QUE ESE AUDITOR ELIGE LA LECTURA QUE LE CUESTA** teniendo la contraria
delante y escrita. **Queda escrito quien levanto la pregunta.**

**Los dos veredictos que `grove` adjudico como `CONTINUA` por la lectura vieja se re
adjudican en la linea serial bajo `D.53`, con correccion declarada**, y **la caida suya que
dependia de ello se retira citando esta decision.**

---

## D.55. LA DEUDA NO BLOQUEA LA PRODUCCION: DOS CLASES DE VUELTA (18 sep 2026, decision del fundador)

*Decision del fundador del 18 sep 2026. **Nace de una medida, no de una molestia.***

### La medida que la obliga

**La linea serial metio `14` nodos en la vuelta `36`, en una sola vuelta. En las cinco
siguientes metio `8` en total, y una de ellas metio CERO.** No falto candidato ni mordio
ninguna guarda: **cada vuelta abria con una tarea bloqueante de reparacion**, y lo que
quedaba de turno ya no daba para insertar.

    V.38  TAREA 1.A: la arista en cola de la linea 469 cableada
    V.39  TAREAS 1 y 2, todas ANTES de la primera insercion
    V.40  TAREA 1.A CERRADA: los dos U+0008 corregidos        (0 nodos)
    V.41  TAREA 1.A CERRADA: la 498 releida contra el grafo   (0 nodos)

### La letra

> **HAY DOS CLASES DE VUELTA.**
>
> **VUELTA DE INSERCION:** abre **SIN tareas de reparacion**. Su unico trabajo es **meter
> candidatos al grafo por la aduana**, con sus guardas de dato intactas (fidelidad `D.30`,
> cerrojo, censo, tallado).
>
> **VUELTA DE SANEAMIENTO:** corre **UNA de cada CINCO**, **sin insertar nada**, y paga la
> deuda.
>
> **TODA DEUDA VA A `docs/loop/DEUDA.jsonl` con su cita y su vuelta de origen**: aristas en
> cola, relecturas, cifras mal derivadas, rotulos, propuestas de doctrina.
>
> **UNICA EXCEPCION:** **una guarda de DATO en rojo** (`gate`, cerrojo, censo no
> decreciente, fidelidad con puente) **bloquea en el acto**, porque **eso no es deuda: es
> averia.**

### El auditor encarga, no bloquea

> **SU ACTA PUEDE DEJAR COMO MAXIMO UNA TAREA BLOQUEANTE** para la vuelta siguiente, **y
> solo si cita la guarda de dato en rojo que la justifica.** Todo lo demas lo escribe en
> `DEUDA.jsonl`.
>
> **Un acta con mas de una bloqueante sin guarda roja es CAIDA DE REPORTE del auditor.**

**POR QUE ESTO ES SANO Y NO UN INDULTO:** la deuda **no se perdona, se agenda**. Sigue
escrita, con su cita y su vuelta de origen, y **se paga junta**, que ademas es mas barato:
cuatro reparaciones en una vuelta cuestan menos que cuatro vueltas con una reparacion cada
una. **Lo que se acaba es que una arista de hace dieciseis vueltas decida cuantos nodos
entran hoy.**

### El austero, con cifra

> **Si un turno pasa de `10` USD sin que la vuelta sea de saneamiento, el acta lo declara
> con el desglose de en que se fue.**

**Hoy la media es `14,92` por turno**, asi que esto no es teorico: **es la mayoria.** No
prohibe gastar; **obliga a decir en que**, que es lo unico que deja decidir despues.

> ### **CORRECCION DECLARADA, 21 sep 2026: EL AUSTERO DECLARA, NO PARA**
>
> *Punto 2 de la decision del fundador del 21 sep 2026, archivada en
> `docs/loop/paradas/2026-09-21-el-precio-del-extractor-DECISION.md`.*
>
> **El encargo de la vuelta `54` escribio:** *si tras DOS vueltas el turno sigue por
> encima de `8` USD, el bucle **se para** para revisarlo.* **Eso contradecia esta regla**,
> que dice **declarar** y no parar, y **lo escribi yo, no el fundador.**
>
> **EL AUDITOR NO ELIGIO ENTRE LAS DOS: paro y lo subio**, poniendo los dos textos con su
> fecha y diciendo que `D.13` no lo resolvia porque una es del banco y otra de un encargo.
> **Eso es exactamente lo que hay que hacer con una contradiccion.**
>
> **LO QUE QUEDA VIGENTE ES ESTA REGLA.** El `se para` de aquel encargo **era un disparador
> de medicion de una sola vez**, ya cumplido: dio la cifra que no existia (`14,98` de media
> en regimen ligero, ningun turno bajo `8`). **Se retira.** Un turno sobre `10` USD **se
> declara con su desglose**, y **la parada la decide el fundador con la cifra delante**.
>
> **LA LECCION, Y ES MIA:** un encargo no puede escribir una regla que contradiga al
> banco. Si hace falta un disparador de una vez, **se escribe diciendo que es de una vez y
> para que medicion**, y no con el verbo de una regla permanente.

### El instrumento

    python scripts/deuda.py                  lo pendiente, y que clase toca
    python scripts/deuda.py --anotar ...     contrae una deuda, con su cita
    python scripts/deuda.py --pagar <id>     la salda, en su vuelta de saneamiento
    python scripts/deuda.py --clase N        INSERCION o SANEAMIENTO para esa vuelta

**LA CADENCIA SE CUENTA DESDE LA ULTIMA DE SANEAMIENTO**, no contra un calendario fijo: si
se contara por el resto de una division, **una vuelta perdida correria el turno de todas
las demas** y el registro dejaria de poder explicar por que le toco a esa.

### Y la doctrina se congela hasta que el mundo 11 cierre

> **LA COLA DE DOCTRINA NO CRECE**, y **el banco no gana reglas nuevas salvo que una guarda
> de dato lo exija con su cita.**

**Sesenta y cuatro reglas en veinte dias son suficientes para insertar `21` nodos.**

---

## D.57. LA FASE CIEGA SABE QUE NO VE (18 sep 2026, decision del fundador)

*Decision del fundador del 18 sep 2026, punto 3, sobre la parada de la vuelta 44. **El
numero lo asigna esta sesion**, que es como se hace desde la decision de hoy: el fundador
dicta sin numero.*

### La caida que la obliga, y la conto el propio caido

El auditor de la `ACTA 43` publico, **en su apertura ciega sellada y repetido en celda de
tabla**, que `docs/loop/CREDITO_serial.jsonl` se retira **y que nadie lo declaro**. Es
falso, y lo desmentia un registro que existia mientras el lo escribia:

    $ grep -n "APERTURA CIEGA.*retirados" docs/loop/loop.log | tail -1
    [2026-09-18 21:22:25] VUELTA 3 : APERTURA CIEGA, retirados: REPORTE.md
          loop.log ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl

**El arnes lo venia declarando en la linea de su propio turno desde el 17 sep.** Y el no
tenia con que mirarlo: **`loop.log` era uno de los retirados.** Se retiraba **el registro
que dice que se retira.**

> **EL NO SE EXCUSO CON ESO, Y ESA ES LA PARTE QUE HAY QUE LEER:** *ese es exactamente el
> motivo de la regla. La frase que si podia escribir era de una linea: no puedo comprobar
> si el arnes lo declara, porque `loop.log` es uno de los retirados.* **Elegi la afirmacion
> en vez de la limitacion.**

**Fue la tercera de tres tandas seguidas de la misma familia** (`ACTA 41`, `42` y `43`):
**publicar sin comprobar**. Su racha propia llego a `3 de 3` y el bucle se detuvo.

### La letra

> **`loop.log` NO SE RETIRA EN LA FASE CIEGA.** Es **registro del arnes, no del
> extractor**, y sin el la ciega **no puede comprobar que se le retiro**.
>
> **Y EL ARNES PEGA EN EL PROMPT DE LA FASE CIEGA LA LINEA LITERAL DE `retirados:` DE ESE
> MISMO TURNO.**

**LAS DOS MITADES HACEN FALTA, y la segunda no es adorno:** mientras `loop.log` se
retiraba, **las lineas del arnes de esa ventana iban a un fichero provisional**, asi que
dejar el fichero en su sitio sin quitar ese desvio **habria arreglado la mitad**: el
fichero estaria, y la linea de ese turno no.

### Lo que se pierde, y por que se acepta

**`loop.log` dice lo que hizo el turno del extractor**, asi que **es una via de
contaminacion** y por eso se retiraba desde `D.34.2`. Se acepta el cambio porque **es la
unica sede donde la ciega puede verificar su propia premisa**, y el balance no esta
reñido: **una ciega que no puede comprobar lo que afirma publica sin comprobar**, y eso ya
costo tres tandas seguidas. **Una contaminacion posible pesa menos que una caida medida
tres veces.**

### Caso positivo, con claude falso

**Escenario `17` de `tests/prueba_arnes.sh`.** Desde **dentro** de la fase ciega, el turno
ciego abre `docs/loop/loop.log`, encuentra la linea de `retirados:` de su propio turno y lo
deja escrito (`COMPROBADO_EN_LOG`); la prueba exige ademas que **no** aparezca
`NO_PUEDO_COMPROBARLO`, y que el prompt traiga la linea literal y la orden de **escribir la
limitacion** cuando algo no se pueda comprobar.

**Negativo:** los otros tres siguen retirados, y el log lo dice con su nombre.

---

## D.58. DOS REGIMENES: EL LIGERO NO TOCA EL GRAFO (19 sep 2026, decision del fundador)

*Decision del fundador del 19 sep 2026. **El numero lo asigna esta sesion.** Nace de una
cifra: `USD 300` en un dia para `30` candidatos, unos `10` por candidato, contra los `3,60`
que costo el mismo trabajo cuando corria sin auditoria completa encima.*

### La letra, y la linea que la divide

> **HAY DOS REGIMENES, Y LOS SEPARA UNA SOLA PREGUNTA: SI EL DATO EXISTE YA.**

**REGIMEN DE EXTRACCION** (`MODO_INSERCION=cuarentena`), **ligero, porque nada toca el
grafo:**

| | |
|---|---|
| **el extractor** | mina **TRES capitulos por vuelta**, con techo de **`30` candidatos** |
| **las guardas** | **tallado y censo**, que son baratos |
| **la fidelidad `D.30`** | **POR MUESTRA**: **uno de cada tres capitulos entero**, y en los otros dos **una muestra fija de `15` pasos con semilla escrita** |
| **el auditor** | verifica **la frontera al digito**, coteja la muestra, publica **pasos inventados por capitulo** y escribe **un acta corta** |
| **lo que NO corre** | **sin fase ciega, sin sello y sin testigo**. No hay cifra sobre el grafo que proteger |
| **objetivo medido** | **turno bajo `5` USD** |

> **EL DISPARADOR, que es lo que hace de la muestra una alarma y no un adorno:** si la
> muestra de un capitulo **pasa del `10` por ciento de pasos inventados, ESE CAPITULO SE
> RELEE ENTERO ANTES DE SEGUIR.** El tope de `D.30` no se toca: lo que cambia es que aqui
> se mide sobre `15` pasos, **y por eso escala a relectura entera en vez de a veredicto**.

**REGIMEN DE INSERCION** (`MODO_INSERCION=insertar`), **completo y sin quitar nada: es
donde el dato existe y donde cada guarda se paga sola.**

> **LA RELECTURA DE FIDELIDAD DE UN LOTE SE HACE ENTERA EN SU VUELTA DE INSERCION**, sobre
> los candidatos que entran, **y no antes**: asi **ningun paso entra al grafo sin haber
> sido leido contra su libro una vez.**

### Por que esto no afloja nada, y es la parte que hay que entender

**En cuarentena, un candidato mal leido no ha hecho daño todavia**: vive en su bandeja y
`D.39` no lo deja entrar hasta que su lote cierre. **La relectura no se quita: se mueve al
momento en que el dato existe**, que es cuando puede hacer daño. Releer los mismos pasos
dos veces, una en cuarentena y otra al insertar, **cuesta el doble y protege lo mismo**.

**Y LA MUESTRA SIGUE MIDIENDO ALGO REAL:** no certifica el capitulo, **avisa**. Si la
muestra sale sucia, el capitulo entero se relee ahi mismo, antes de que la vuelta siga.

### La muestra se reproduce, o no es una muestra

    python scripts/muestra_fidelidad.py --libro <clave> --capitulos a,b,c --semilla <texto>

**LA SEMILLA SE ESCRIBE EN EL REPORTE.** Quien audite vuelve a correr el instrumento con
ella y **tiene que salirle la misma lista**. Se calcula con `sha1` sobre `semilla|clave`,
sin `random`: el mismo texto da el mismo numero en cualquier maquina.

> **Una muestra que no se puede reproducir no es una muestra: es una eleccion**, y **el que
> elige sus pasos elige su resultado.**

### La cadencia de saneamiento la hace cumplir el codigo

> **Si desde la ultima vuelta de saneamiento han pasado cinco, LA VUELTA QUE ABRE ES DE
> SANEAMIENTO Y EL ENCARGO NO PUEDE DECIR OTRA COSA.**

**Se comprueba en la apertura**, dentro de `scripts/guarda_tablero.py`, que es lo que el
arnes ya llama. **El encargo declara su clase** en su propia linea:

    CLASE DE ESTA VUELTA: EXTRACCION | INSERCION | SANEAMIENTO

**POR QUE HIZO FALTA, CON EL EJEMPLAR MEDIDO:** la vuelta `49` **si corrio como
saneamiento**, pero **no lo anoto en el registro**, y durante un dia `deuda.py` dijo
*ultima vuelta de saneamiento: ninguna todavia*. **Lo cazo el auditor solo**, en la
`ACTA 48`, y escribio la declaracion que faltaba citando donde constaba. **La cadencia
dependia de que alguien se acordara de anotarla**, que es el genero de remedio que esta
casa tiene medido que no funciona (`D.35`).

**Caso positivo:** con la ultima de saneamiento en la `49`, un encargo de la `54` que
declare `EXTRACCION` **no abre**, y la guarda nombra la cuenta. **Negativo:** ese mismo
encargo declarando `SANEAMIENTO` pasa.

### El alcance, con la cifra delante

> **`grove_high_output` se termina y se inserta**, y **el mundo 11 puede declararse
> COMPLETO con esos cinco libros si el fundador lo decide al cerrar Grove.**
>
> **`gerber_emyth` y `marquet_turn_the_ship` siguen pausados con sus `19` candidatos**, y
> **se relevan solo si el coste medido del regimen ligero lo permite**. Eso se decide **con
> la cifra de Grove delante, no ahora.**

---

## D.59. LA CIFRA DERIVADA LA CALCULA EL INSTRUMENTO (20 sep 2026, decision del fundador)

*Decision del fundador del 20 sep 2026 sobre la parada de la vuelta 53. **El numero lo
asigna esta sesion.** Es la cura de una racha con tres tandas medidas.*

### La letra

> **TODA MEDIA, PORCENTAJE, RAZON O DIFERENCIA QUE EL REPORTE PUBLIQUE LA IMPRIME UN
> INSTRUMENTO, con su numerador y su denominador NOMBRADOS.**
>
> **Una cifra derivada a mano de dos celdas no se publica.**

### El ejemplar, y son tres de la misma figura

La racha `REPORTE` llego a su tope con tres caidas seguidas, y el auditor las resumio en
una linea: **una frase sobre una cifra cierta que el propio instrumento desmiente dos
lineas abajo.** La tercera:

    media por pasada CON reloj             : 517,7 s
    pasadas de aduana lanzadas             : 11
    pasadas CON fichero de reloj           : 9
    suma del reloj de aduana               : 4659,0 s

**`11` pasadas en el numerador y `9` en el denominador.** Los `4659,0` s **incluyen la
pasada de `600` s que la celda de al lado marca sin fichero de reloj**, asi que dividirlos
entre `9` **mezcla dos poblaciones**. De ahi salia un `-29,2` por ciento donde **la caida
real por pasada es `-42,1`**.

> **LO QUE CAYO NO FUE LA CIFRA: FUE LA FRASE.** `4659,0` es cierto y `9` es cierto; **lo
> falso es que uno sea el numerador del otro.** Por eso la regla no pide mas medicion:
> pide **que quien divide diga entre que divide.**

### La guarda, y por que solo mira la vuelta viva

`scripts/tallar_reporte.py` gana `cifras_derivadas_sueltas()`, y **corre en cada commit**
dentro de `scripts/cerrar_reporte.py`. **Una frase con cifra derivada sin instrumento en su
parrafo cae nombrando la frase.**

**SOLO EN LA VUELTA VIVA, Y ESO NO ES UNA CONCESION: es lo que separa una guarda de un
grito.** Medido antes de escribirla: sobre el reporte entero **caerian `591` lineas** de
`53` vueltas de historia ya auditada; **sobre la vuelta viva cayeron `2`, y las dos eran de
verdad.** Una guarda con quinientos noventa y un avisos **se aprende a no mirar**, y esta
casa ya pago ese precio dos veces.

**Y LA UNIDAD ES EL PARRAFO, NO LA LINEA.** Lo corrigio un falso positivo el mismo dia en
que la guarda nacio: **la correccion declarada que repara la caida de la vuelta 53 cita su
instrumento dos lineas por debajo de la cifra**, y por linea la guarda **tumbaba el arreglo
que ella misma pedia**. Una frase se publica dentro de un parrafo.

**Y LA PALABRA VA JUNTO AL NUMERO**, no solo en la misma linea: sin eso, un encabezado que
dice *UNA FILA POR CAPITULO Y NO UNA MEDIA* caia por la palabra `media` y por el digito de
su numero de seccion.

**Caso positivo:** la frase de la vuelta 53 (`la media cayo un 29,2 por ciento`) **cae**.
**Negativo:** ese mismo parrafo nombrando `.v53/reloj.txt` **pasa**.

### Y la cifra buena entro por regeneracion

    $ python .v54/media_por_pasada.py
      sobre las 11 pasadas LANZADAS                                423.5 s
      sobre las 9 pasadas CON fichero de reloj                     517.7 s
      su media por pasada (vuelta 52)                              731.2 s
      (423.5 menos 731.2) sobre 731.2                              -42.1 por ciento

**`42,1` por ciento es la caida por pasada, y esa es la que presupuesta.**

---

## D.60. UN MUNDO SE CIERRA CUANDO SUS LIBROS ESTAN INSERTADOS, NO EXTRAIDOS (21 sep 2026, decision del fundador)

*Decision del fundador del 21 sep 2026 sobre la parada feliz de la vuelta 62. **El numero lo
asigna esta sesion.** Es la regla que faltaba el dia en que una campania cerro su extraccion
y nadie tenia escrito que eso todavia no era cerrar.*

### La letra

> **UN MUNDO SE DECLARA COMPLETO CUANDO LOS LIBROS DE SU CORTE DEFINITIVO ESTAN
> INSERTADOS EN EL GRAFO. Una bandeja llena no cierra nada.**
>
> **La rama del mundo se funde a `main` cuando el mundo se declara completo, con `gate` y
> la suite corridas y verdes delante, y ese es el estado que la app consume.**
>
> **El bucle no funde: pide.**

### Por que hacia falta escribirla

**El `21` sep de `2026` la extraccion del mundo `11` quedo consumada**, `18` de `18`
capitulos del ultimo libro leidos y adjudicados, `92` candidatos en bandeja. **Y el grafo
seguia exactamente donde estaba: `346` nodos, uno solo de Grove.**

**La casa no tenia escrito que esas dos frases no se contradicen.** El auditor de la
`ACTA 61` tuvo que razonarlo de cero para poder parar sin decir que el mundo estaba cerrado,
y lo razono bien; pero razonar de cero lo que deberia estar escrito es exactamente lo que
`D.32` manda evitar.

> **`D.39` ya decia que un libro entra cuando su extraccion cierra. Lo que faltaba es la
> otra mitad: que la extraccion cerrada NO es el cierre del mundo.**

### El corte del mundo `11`, que esta regla fija

**CINCO LIBROS** (decision del fundador del `21` sep, punto `4`, que confirma el corte del
mismo dia por la manana):

| | libro | estado al escribirse esta regla |
|---|---|---|
| `1` | `onu_consumidor` | **INSERTADO**, `6` nodos |
| `2` | `smart_who` | **INSERTADO**, `59` nodos |
| `3` | `zhuo_manager` | **INSERTADO**, `136` nodos |
| `4` | `scott_radical_candor` | **INSERTADO**, `142` nodos |
| `5` | `grove_high_output` | extraccion CERRADA, `1` insertado de `92`. **Es lo que falta** |

### El sexto, y la condicion que lo deja entrar

**`gerber_emyth` entra como sexto SOLO si cierra su extraccion antes de que la cuota de la
semana se agote**, y entonces se cosecha e inserta por el relevo de `D.50`. **Si no la
cierra, queda en bandeja entero y NO bloquea el cierre del mundo.**

**`marquet_turn_the_ship` solo si sobra semana despues de Gerber.**

> **UNA BANDEJA A MEDIAS NO RETRASA UN CIERRE.** Es la misma letra de `D.32`, *un lote
> cerrado y sin insertar no bloquea nada*, aplicada un piso mas arriba: **al mundo.**

### Caso positivo y caso negativo

**POSITIVO, y es el de hoy:** el mundo `11` con Grove extraido entero y sin insertar
**NO esta completo**, la rama **no se funde**, y quien lo pregunte tiene donde leerlo.

**NEGATIVO:** el mundo `11` con los `92` de Grove en el grafo, `gate` verde y la suite
verde **SI esta completo**, y se funde **aunque Gerber y Marquet sigan con sus `19`
candidatos en bandeja.**

### Lo que esta regla no toca

**No cambia quien funde.** `AUDITOR_FORJA.md` seccion `3` sigue diciendo que **el bucle no
funde ramas y el bucle no crea remotos**, y esta regla solo fija **cuando** se pide.
