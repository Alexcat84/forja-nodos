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
