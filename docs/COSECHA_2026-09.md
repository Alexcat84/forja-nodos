# COSECHA DE DOCTRINA, septiembre 2026

**Fase 1 de 2. Documento de ESTUDIO, no de implementacion.** Aqui no se cambia
una linea de codigo, no se mueve un umbral y no se toca el dataset. Lo que hace
este documento es traer a la forja lo que la campaña de My-idea aprendio
pagandolo, con su cita, y dejar escrito que se haria con cada cosa. Ejecutar
algo de esto es decision de Alexis y trabajo de otra sesion.

**La fase 2 (calibracion de umbrales contra el grafo final de My-idea) NO se
hace aqui** y se dice por que en la seccion 4: la propia campaña midio que un
umbral calibrado contra casos plantados y no contra la distribucion del catalogo
entero es un umbral que no se puede defender.

---

## 0. QUE SE LEYO, CON SU CORTE

Todo lo de abajo se leyo el 4 sep 2026 de un clon de solo lectura del repo
`Alexcat84/My-idea`, rama `pasada-unica`, en carpeta hermana
(`../my-idea-lectura`). **Nada se escribio en ese repo.**

| | |
|---|---|
| commit leido | `edbc1a482182c2664c2575f551d75179dd5ac7d9` (4 sep 2026) |
| mensaje | *Decision del fundador: el campo estado se jubila, la vara es el instrumento, y las seis de verdad abren* |
| `docs/loop/paradas/` | **40 ficheros, 27 con DECISION DEL FUNDADOR escrita** |
| `docs/plan/BANCO_DEL_PLAN.md` | 1.253 lineas, P.1 a P.20 mas P.5.1 y P.5.2 |
| `docs/loop/EJECUTOR.md` | regla 1 entera (nueve renglones acumulados del 14 ago al 4 sep) |
| `docs/loop/AUDITOR.md` | seccion 0, ciclo 0 y regla 1 enteras |
| lectura de apoyo | `scripts/costuras_internas.py`, `docs/plan/08_VERIFICACION.md`, `docs/BANCO_DE_TEXTOS.md` 9.19 y 9.22 |

**Nota de honestidad sobre las citas.** Cada regla de abajo cita el fichero de
parada y la fecha de la decision. Las fechas son las que el propio texto declara,
no las del sistema de ficheros. Donde una regla vive a la vez en una parada y en
el banco del plan, se citan las dos sedes.

---

## 1. LAS REGLAS DE DOCTRINA QUE APLICAN A LA ADUANA DE NODOS NUEVOS

Cada entrada trae: la regla, su cita, y **una linea** de traduccion a la forja.
La traduccion es una PROPUESTA de estudio. Ninguna esta implementada.

### 1.A. Las que gobiernan el VEREDICTO (la vara)

---

**P.5.1 NOMBRAR NO ES PROCEDIMENTAR**
*Congelada el 3 sep 2026, decision del fundador. Parada:
`2026-09-03-credito-vara-movil-DECISION.md`. Sede: `BANCO_DEL_PLAN.md` P.5.1.*

> La segunda linea de un par solo cuenta como expansion si trae procedimiento
> propio, y no solo el nombre de otro.

Nacio de cuatro caidas de clase en dos tandas seguidas, todas de la misma
especie. Lleva sus cuatro ejemplares pegados a la frase (`052` y `095` aceptan,
`122` y `100` excluyen) porque **una regla sin sus casos se vuelve a estrechar
sola**, y ninguna vuelta la mueve sin correccion declarada del fundador.

**Traduccion a la forja:** un veredicto `CONTINUA` deberia exigir que la razon
nombre EL PASO del hijo que despliega la linea de la madre, y el gate deberia
rechazar la arista cuya razon no cite ningun paso.

---

**P.5.2 LA SEGUNDA LECTURA INDEPENDIENTE ES LA QUE DEJA MARCA CONTABLE**
*Escrita el 3 sep 2026 por encargo expreso del fundador. Sede:
`BANCO_DEL_PLAN.md` P.5.2.*

Dos actas publicaron 84 y 82 relecturas **y las dos eran honestas**: no median
lo mismo porque la definicion nunca se escribio. La regla define que marca cuenta
(relectura, con su vuelta, escrita en el campo `razon` del registro), quien puede
firmarla (la vuelta, no la persona) y que una relectura conjunta cuenta una sola
vez. Su frase central: *una lectura que no deja marca no es contable, no porque
no haya ocurrido, sino porque una cifra que no se puede recomputar de un fichero
no es una cifra*.

**Traduccion a la forja:** la relectura ciega del auditor deberia escribirse como
linea nueva en `bitacora/VEREDICTOS.jsonl` (misma pareja, marca de relectura y
vuelta), no solo en el acta, o la metrica de credito de la forja no se podra
recomputar del archivo.

---

**9.22 LA VARA EN LOS DOS SENTIDOS, y su comprobacion de las dos lineas**
*Banco de textos 9.22. Refinada por la CORRECCION 14 y adoptada como guarda en
`2026-09-02-opc05-bidireccionales-DECISION.md` (2 sep 2026).*

> La vara es una relacion entre LINEAS, no entre NODOS. Dos nodos pueden ser cada
> uno hijo del otro sin que ninguno repita al otro, porque la linea que uno
> expande no es la linea que el otro expande.
>
> **LA COMPROBACION QUE LA SEPARA DE LA DUPLICACION: si las dos direcciones
> apuntan a LA MISMA LINEA, no es esta figura: es un solape.** La figura exige
> dos lineas distintas, una en cada nodo.

**Traduccion a la forja:** el veredicto `MUTUO` de la v0.2 pide `ida=` y
`vuelta=` pero NO comprueba que sean lineas distintas; deberia exigir que cada
sentido cite el paso concreto que expande y rechazar el par cuando los dos
sentidos citan el mismo.

---

**LA LISTA BLANCA ES UN REGISTRO DE CITAS**
*Decision del fundador, 2 sep 2026.
`2026-09-02-opc05-bidireccionales-DECISION.md`.*

La guarda de bidireccionales de `OP-C-05` tenia tres letras que no podian ser
ciertas a la vez: encenderla tal cual ponia el gate en rojo 153 veces sobre un
grafo saneado, y blanquear los 153 obligaba a escribir 151 entradas sin lectura
detras. La salida:

> La lista blanca pasa de lista a mano a **REGISTRO DE CITAS**, y **un par sin
> cita es rojo**. Cada par bidireccional entre vivos exige un veredicto de
> lectura registrado con cita.

**Traduccion a la forja:** `config/pares_mutuos.jsonl` deberia dejar de ser una
lista de pares con razon libre y pasar a exigir la CITA del veredicto que lo
sostiene (fecha y linea de la bitacora), con el gate en rojo para todo par sin
cita resoluble.

---

**9.3.1 GANADOR POR DERECHO contra GANADOR POR ELEGIR, y P.8**
*Banco de textos 9.3.1; P.8 del banco del plan. Ejemplar medido en
`2026-08-19-fusion-opd04.md` (19 ago 2026): de los ocho pares A del acto, CERO
nombran ganador.*

Cuando ninguna razon del archivo nombra vencedor, el superviviente esta **POR
ELEGIR** y se decide por `P.8`: **el contenido decide, el cableado desempata
SOLO a contenido empatado**. El auditor de esa parada midio el cableado y
escribio por que no lo usaba: *poner el cableado delante seria saltarse el orden
de la propia regla*.

**Traduccion a la forja:** cuando un `REPITE` abra una fusion, la plantilla
deberia obligar a declarar si el superviviente es por derecho (con el par que lo
gana citado) o por eleccion (con la lectura de contenido escrita), y prohibir
justificarlo por numero de aristas mientras el contenido no haya hablado.

---

### 1.B. Las que gobiernan EL DESTINO DEL MATERIAL

---

**P.17 LA LECTURA VENCE AL METADATO**
*Adoptada el 14 ago 2026, decision del fundador. Parada:
`2026-08-14-fase01-dos-casos.md`, caso 1 por el camino A.*

> Cuando un nodo vive en dos operaciones, la pertenencia confirmada contra los
> pasos con frontera escrita vence a la argumentada por metadato (fuente,
> formato, familia).

El ejemplar (`background_startup_vs_corporativo`) estaba clasificado a la vez
por su metadato y por una lectura de sus pasos, **las dos ciertas el mismo dia y
contradictorias**. Gana la que leyo los pasos y publico frontera; la perdedora se
corrige por correccion declarada, sin borrar.

**Traduccion a la forja:** cuando la señal 2 (familia de id) y la señal 3 (paso
contra nodo) den veredictos opuestos sobre el mismo vecino, la razon escrita
deberia estar obligada a declarar cual lectura gano y por que, y familia de id
por si sola nunca deberia poder sostener un `REPITE`.

---

**P.18 EL DESTINO SE DECIDE POR LECTURA DE OBJETO**
*Adoptada el 14 ago 2026, decision del fundador. Paradas:
`2026-08-14-fase01-dos-casos.md` (caso 2) y `2026-08-14-muro-indice-y-destinos.md`.*

> Dentro de la familia que la frontera nombra, el bloque va al miembro cuyo
> OBJETO coincida, decidido por lectura sobre la NOMINA VIGENTE AL DIA. Si
> ninguno coincide, forma nodo propio en esa familia.

Sus tres obligaciones: la nomina se relee el dia que se ejecuta (no la publicada
en otra fecha), el miembro elegido se escribe como correccion declarada diciendo
POR QUE su objeto coincide, y **no se fuerza un encaje que la lectura no
sostiene**.

**Traduccion a la forja:** el veredicto `REPITE` deberia exigir nombrar el nodo
destino de cada una de las seis perdidas por coincidencia de OBJETO y permitir
explicitamente la salida "ninguno coincide", en vez de dar por hecho que el
vecino que levanto la señal es el destino.

---

**P.19 LA REPETICION INTERNA SE FUNDE, NO SE DESTEJE**
*Adoptada el 14 ago 2026, decision del fundador. Parada:
`2026-08-14-toque-unico-intra-nodo.md`.*

> Cuando material de dos o mas fuentes DENTRO de un nodo repite el mismo objeto,
> no va a ningun destino: se funde en un solo procedimiento dentro del nodo.

Nacio porque las dos salidas de `P.18` chocaban: mandar el bloque a nodo propio
fabricaba el gemelo exacto de su propio donante, y forzarlo a un miembro ajeno
era el encaje que `P.18` punto 3 prohibe. **La pregunta no era de `P.18`: el
objeto ya estaba en casa.** El nodo queda MULTIFUENTE LEGITIMO con la procedencia
declarada por bloque.

**Traduccion a la forja:** la aduana deberia medir la repeticion INTERNA del
candidato (paso contra paso del mismo nodo) antes de compararlo con el dataset, y
bloquear con una salida propia "funde tus pasos repetidos antes de entrar", que
hoy no existe.

---

**P.20 UN NODO, UN CORTE**
*Adoptada el 14 ago 2026, decision del fundador. Misma parada.*

> Cuando un nodo pertenece a dos operaciones de destejido, no se corta dos veces
> ni en orden: la frontera completa se publica como registro unico y el corte se
> ejecuta UNA vez, citado por las dos operaciones con correccion declarada.

Cortar dos veces partiria el mismo bloque en pedazos incompatibles; cortar en
orden dejaria a la segunda operacion leyendo un nodo que la primera ya movio.

**Traduccion a la forja:** si dos vecinos distintos reciben `REPITE` en la misma
insercion, la forja deberia obligar a UNA sola operacion de fusion con los dos
citados, en vez de imprimir dos plantillas de reparto independientes como hace
hoy.

---

### 1.C. Las que gobiernan EL CABLEADO Y EL ARCHIVO

---

**P.16 QUIEN FABRICA, LIMPIA**
*Adoptada el 14 ago 2026, decision del fundador. Parada:
`2026-08-14-doctrina-opc04.md` (opcion A ampliada).*

> Toda operacion de fusion retira, EN SU MISMO COMMIT, la arista interna del par
> que su propia simulacion reporta como auto-arista naciente.

El motivo esta medido: **las 33 auto-aristas del grafo no nacieron de golpe,
nacieron una fusion a la vez, y ninguna se limpio en el momento en que se
fabrico.** Aplazar la limpieza a una operacion de saneo posterior es exactamente
como nacieron, y esa espera es lo que las hizo dificiles de diagnosticar.

**Traduccion a la forja:** la simulacion de la aduana ya corre el gate entero
antes de escribir, pero deberia ademas RETIRAR en el mismo acto la arista que
ella misma vuelve redundante, en vez de limitarse a rechazar la insercion.

---

**EL DEPRECADO ES ARCHIVO**
*Decision del fundador, 15 ago 2026, decision 1 opcion a. Parada:
`2026-08-15-cableado-deprecado-y-costuras.md`.*

> El deprecado conserva su cableado como archivo, y Gate 0 deja de reciprocar
> aristas que nacen en deprecados. Es la que menos miente: **el deprecado es
> archivo, no participante.**

Las otras dos salidas se descartaron con su motivo escrito: reescribir las listas
del absorbido pierde el cableado historico que hace auditable la fusion, y
aflojar la guarda convierte la deuda en norma.

**Traduccion a la forja:** el dia que la forja tenga nodos deprecados (hoy solo
tiene `ids_alias`), sus aristas no deben contar como aristas vivas del grafo ni
alimentar ninguna guarda de simetria.

---

**P.10 EL CIERRE TRANSITIVO CONVOCA, LA LECTURA DECIDE (nodos puente)**
*Banco del plan P.10 y P.12. Ejemplar medido en `2026-08-19-fusion-opd04.md`
(19 ago 2026): un acto de siete que la lectura partio en dos triangulos cerrados,
un nodo colgado y TRES nodos puente.*

`P.10` prohibe fundir la componente conexa entera: **el cierre transitivo no lee,
cuenta.** Su tercera salida es fundir solo el subconjunto cerrado y enlazar el
resto. La decision del fundador (19 ago 2026) fue siete a tres.

**Traduccion a la forja:** si alguna vez la forja calcula componentes conexas
sobre los vecinos levantados, el resultado debe entrar como cola de lectura y
nunca como nomina de fusion.

---

### 1.D. Las que gobiernan LA VIGENCIA DE UNA LECTURA

Este es el bloque que la forja no tiene en absoluto, y el que mas barato sale
poner ahora.

---

**LOS PARES RANCIOS: una lectura contra texto muerto no vale**
*Parada `2026-08-15-p5-rancios-opd03.md` y su decision del 15 ago 2026.*

Medido: **de los seis pares A de un acto, CINCO se leyeron contra texto que ya no
existe**, porque las cirugias de una fase anterior habian reescrito los nodos.
La vara que manda es la de TEXTO, no la de fecha. La consecuencia se computo y no
se dibujo: volcar las cinco relecturas **disolvia el acto de seis en un acto de
dos**, y el auditor escribio que eso no era un fracaso, *era el destejido
haciendo su trabajo*.

**Traduccion a la forja:** cada linea de `bitacora/VEREDICTOS.jsonl` deberia
guardar una huella del texto de los dos nodos en el momento del veredicto, y el
gate deberia declarar RANCIO todo veredicto cuya huella ya no case con el nodo de
hoy.

---

**EL ALCANCE DE P.5: solo dentro del acto en operacion, nunca fuera**
*Decision del fundador, 15 ago 2026.
`2026-08-15-p5-rancios-opd03-DECISION.md`, punto 2.*

Releer por `P.5` alcanza al acto que se esta operando y a nada mas. Releer un par
cuyos dos nodos no cambiaron es **re cribar**, y ese frente no lo abre nadie sin
autorizacion expresa. Cuando el fundador quiso salirse (el cuarto miembro del
racimo mixto, 19 ago 2026) lo autorizo **de una sola vez y solo para ese racimo**.

**Traduccion a la forja:** el barrido de rancios debe acotarse a los veredictos
del nodo que se esta tocando, y una relectura fuera de ese alcance deberia exigir
autorizacion escrita en el propio comando.

---

**VALVULA DE VIGENCIA y CUMPLIDA POR CONSUNCION**
*Decision del fundador, 4 sep 2026, punto 2.
`2026-09-04-estado-de-las-fichas-DECISION.md`.*

> Antes de ejecutar, sus nominas se resuelven contra el grafo de hoy; si el acto
> fue consumido por las unificaciones, la operacion se declara CUMPLIDA POR
> CONSUNCION con la medicion citada; solo se ejecuta lo que siga vivo.

**Traduccion a la forja:** una operacion de fusion pendiente en
`plantillas/OPERACION_DE_FUSION.md` deberia re resolver su nomina contra el
dataset antes de ejecutarse, y poder cerrarse por consuncion con su medicion en
vez de ejecutarse sobre nodos que ya no existen.

---

**EL CAMPO ESTADO SE JUBILA: LA VARA ES EL INSTRUMENTO**
*Decision del fundador, 4 sep 2026, punto 1. Misma parada.*

Medido: **37 de 71 fichas no calzaban con el arbol**, y por leer el campo `estado`
como si fuera la vara el bucle encargo ejecutar una operacion que llevaba
ejecutada desde el 14 ago. La frase que el auditor se escribio a si mismo:
**contar bien un campo y sacar la conclusion equivocada sigue siendo una caida:
la fuente hay que elegirla antes de contarla.**

**Traduccion a la forja:** ningun estado declarado a mano deberia ser la vara de
nada; lo que la forja afirme sobre su propio dataset (cuantos nodos, que entro,
que falta) tiene que salir de `forja.py`, no de una tabla escrita.

---

**CUANDO DOS TEXTOS SELLADOS CHOCAN, GANA EL QUE APLICO LA REGLA MAS RECIENTE**
*Decision del fundador, 19 ago 2026.
`2026-08-19-punto-brillante-DECISION.md`, punto 1.*

Cuatro textos sellados el 12 de agosto daban por hecho una ruta que una operacion
del 14 de agosto ya habia cambiado aplicando `P.18`. **Gana el que aplico la
regla mas reciente del fundador, y el perdedor se corrige** (por correccion
declarada, sin borrar).

**Traduccion a la forja:** `docs/BANCO_DE_REGLAS.md` deberia llevar en cabecera
esta regla de conflicto, para que dos entradas fechadas que se contradigan se
resuelvan sin abrir una parada.

---

**LAS INSTITUCIONES DE LIBRO JAMAS SE OMITEN: SE MANTIENEN AL DIA**
*Doctrina de la ficha `vigencia-del-marco-internacional`, citada en la parada
`2026-08-28-titulo-nafta-ops01.md` y decidida el 28 ago 2026.*

Un titulo seguia nombrando el NAFTA, extinguido el 1 de julio de 2020. La salida
barata (quitar el token) se rechazo con su motivo escrito: **borrar es omitir, y
deja el catalogo mudo sobre el tratado que si rige.** La frase de la ficha: *un
catalogo que lo cite desactualizado miente con precision*.

**Traduccion a la forja:** el campo `vigencia` y su censo deberian admitir un
sucesor declarado (norma vieja tachada, norma nueva al lado), y el gate podria
avisar de toda `vigencia` con fecha de corte anterior a un umbral de antiguedad.

---

### 1.E. Las que gobiernan LAS GUARDAS Y LAS CIFRAS

Estas nacieron en el bucle, no en la aduana, pero la forja tiene bucle
(`docs/loop/`) y tiene guardas (`src/gate.py`), asi que le aplican enteras.

---

**EL CASO ROJO SE PRUEBA POR MUTACION**
*Decision del fundador, 29 ago 2026.
`2026-08-29-racha-y-escalada-omitida-DECISION.md`. Sede: `EJECUTOR.md` regla 1.*

El ejemplar: un caso rojo publicado como prueba donde la variable del veredicto
era una **constante literal** y el `assert` comparaba `"ENTRA"` con `"ENTRA"`. No
podia salir en rojo nunca.

> Ningun assert, guarda o caso rojo se publica como prueba sin haber corrido antes
> su PRUEBA DE MUTACION: se cambia el valor esperado y se comprueba que el caso
> CAE. Si no hay nada que mutar, **se declara que no hay caso rojo automatico**, y
> esa declaracion es la que se publica.

**Traduccion a la forja:** es la version dura de *una prueba que no puede fallar
no guarda nada*; `tests/test_aceptacion.py` deberia tener un modo que mute el
valor esperado de cada guarda y verifique que la prueba cae.

---

**UNA CIFRA EN EL CODIGO DE UNA GUARDA ES CIFRA PUBLICADA**
*Decision del fundador, 2 sep 2026, pregunta 2.
`2026-09-02-opc05-bidireccionales-DECISION.md`.*

> Si, una cifra falsa en el codigo o docstring de una guarda de `scripts/` cuenta
> como CIFRA PUBLICADA desde hoy, sin retroactividad.

El caso: un comentario decia "307 nodos vivos" donde lo medido eran **307 destinos
sobre 255 nodos vivos**. Una cifra dentro del codigo es mas duradera que una del
reporte.

**Traduccion a la forja:** las cifras del `_medicion_de_la_casa` de
`config/umbrales.json` y las de `docs/BANCO_DE_REGLAS.md` D.4 son cifras
publicadas y deben llevar su corte y su instrumento, no heredarse de memoria.

---

**LA CITA LLEVA SU LINEA, y sus tres renglones**
*Decision del fundador, 14 ago 2026 (parada `2026-08-14-segunda-hilada-y-dictado.md`),
ampliada el mismo dia (`2026-08-14-censo-y-derivado.md`) y el 15 ago
(`2026-08-14-toque-unico-intra-nodo.md`). Sede: `EJECUTOR.md` regla 1.*

Tres renglones acumulados, cada uno con su caida detras:

1. **La cita lleva su linea:** toda afirmacion sobre el estado del registro se
   escribe con la medicion del dia al lado, o no se escribe.
2. **El estado al cierre se mide al cierre:** medir temprano y publicar tarde sin
   remedir es la misma especie de caida que citar sin mirar.
3. **La apertura se mide antes de la primera operacion:** el estado TRAS la
   primera operacion ya es estado intermedio.

**Traduccion a la forja:** cualquier reporte del bucle de la forja que cite
cuantos nodos hay, que veredictos se escribieron o que censos se movieron tiene
que recomputarlo de `dataset/` y `bitacora/` en esa misma vuelta.

---

**LA TABLA SE IMPRIME, NO SE TECLEA. LA TABLA SE CUENTA DE SU FICHERO. LA
IDENTIDAD SE LEE DE GIT**
*Decisiones del fundador del 15 ago, 20 ago y 26 ago 2026. Paradas:
`2026-08-15-credito-celdas-manuales.md`, `2026-08-20-racha-de-reporte-DECISION.md`,
`2026-08-26-racha-tramo-mecanico-DECISION.md`, `2026-08-26-racha-hash-apertura-DECISION.md`.*

Cinco paradas de credito seguidas, todas por celdas tecleadas a mano. La regla
crecio tres veces porque tres veces el remedio dejo un hueco por donde volvio a
entrar la misma especie: primero las tablas del plan, luego la cabecera del
reporte, luego las tablas de las fases mecanicas (donde el tallador no llegaba) y
al final **la prosa de identidad** (el hash de apertura, que era prosa suelta
encima de la tabla). La frase final: **la celda que no salga de un instrumento no
se escribe.**

**Traduccion a la forja:** todo hash, fecha o cifra de un reporte de la forja se
lee de `git rev-parse`, `git log` o de la salida de `forja.py`, y el arbol de
ficheros de un reporte se genera, no se copia a mano.

---

**LA RACHA DISTINGUE DONDE VIVE LA CIFRA**
*Decision del fundador, 27 ago 2026. `2026-08-27-racha-parentesis-DECISION.md`.
Antecedente: la opcion B del 13 ago 2026 (`2026-08-13-credito-vuelta-13.md`).*

> La caida de reporte cuenta para la racha SOLO cuando la cifra vive en una tabla,
> una cabecera o una conclusion; en lista de rutas o prosa de acompañamiento se
> registra y se relee al doble pero NO acumula.

Es la segunda vez que la regla del credito se afina en vez de endurecerse. La
primera (13 ago) separo la caida de CLASE de la caida de REPORTE con el motivo
escrito: *lo que la regla del credito quiere cazar es un veredicto mal puesto, no
una etiqueta mal escrita.*

**Traduccion a la forja:** si la forja adopta metrica de credito, tiene que
escribir desde el dia uno las tres especies (clase, cifra publicada, reporte) y
donde vive cada una, o la primera parada sera una discusion sobre que cuenta.

---

**LA ESCALADA SE ENCARGA, NO SOLO SE DECLARA**
*Decision del fundador, 29 ago 2026.
`2026-08-29-racha-y-escalada-omitida-DECISION.md`. Sede: `AUDITOR.md` regla 2.*

El auditor declaro la racha en dos y **no encargo** la operacion de codigo que el
fundador ya habia autorizado tres dias antes; la tercera caida llego justo donde
el remedio no estaba puesto. **Declararla sin encargarla es una caida propia del
auditor** y se registra con su nombre.

**Traduccion a la forja:** `docs/loop/AUDITOR.md` de la forja deberia llevar este
renglon: un remedio ya autorizado se encarga como tarea bloqueante en el mismo
acta que detecta la racha.

---

**HUECO DE ACTA**
*15 ago 2026, tras la vuelta 34, que corrio entera y nunca fue auditada. Sede:
`AUDITOR.md` ciclo 0. Ejemplar contado en `2026-08-15-p5-rancios-opd03.md`.*

> Si la ultima acta NO cubre la vuelta inmediatamente anterior, hay hueco: se
> auditan TODAS las vueltas sin acta. Una vuelta sin auditar es una vuelta sin
> verificar, por mucho que las siguientes salgan verdes.

**Traduccion a la forja:** el `AUDITOR.md` de la forja no tiene esta guarda y
deberia tenerla, porque su bucle es identico en forma.

---

**EL REPORTE ABRE CON LA VUELTA Y CRECE POR ANEXION**
*Decision del fundador, 4 sep 2026, punto 3.
`2026-09-04-estado-de-las-fichas-DECISION.md`. Sede: `EJECUTOR.md` regla 1.*

Dos vueltas seguidas terminaron sin reporte. **Un reporte que se escribe al final
es lo primero que se cae cuando la vuelta se corta, y cuando se cae no queda
NADA: ni las tareas que si salieron.** El remedio: esqueleto tallado en la
apertura, cada tarea anexa su fila al cerrarse, el cierre lo talla entero, y
**tope de cinco tareas por vuelta**.

**Traduccion a la forja:** misma regla, tal cual, en `docs/loop/EJECUTOR.md` de
la forja.

---

**CERRADA CON REMISION y CUMPLIDA CON REMISION**
*Decisiones del fundador del 26 ago y 28 ago 2026.
`2026-08-26-cierre-fase-03-DECISION.md`, `2026-08-28-titulo-nafta-ops01-DECISION.md`.*

Dos estados que la campaña tuvo que inventar porque el binario hecho o no hecho
mentia: una fase puede cerrar con trabajo enrutado a otra fase con destino
escrito, y una operacion puede darse por cumplida cuando otra operacion consumio
su acto material.

**Traduccion a la forja:** si la forja llega a tener plan de operaciones, estos
dos estados se copian tal cual antes de escribir el primero, no despues.

---

**LA HERRAMIENTA DE SESION CON CREDENCIAL**
*Decision del fundador, 2 sep 2026.
`2026-09-02-aduana-vector-y-a13-DECISION.md`, pregunta 1.*

> `integrar_packs.py --ejecutar` se declara HERRAMIENTA DE SESION CON CREDENCIAL:
> corre solo en sesiones post campaña con humano presente y el `.env` disponible,
> jamas dentro del bucle autonomo; **invocada sin la clave falla ruidosamente
> nombrando lo que falta.**

**Traduccion a la forja:** si algun dia una señal de la forja usa un servicio con
clave, esa señal se declara de sesion, jamas de bucle, y su ausencia falla
ruidosamente en vez de degradarse en silencio.

---

## 2. HALLAZGOS DE MECANICA QUE AFECTAN A LAS SEÑALES

Esto no es doctrina: son tres averias medidas en instrumentos reales, y las tres
tienen gemelo posible en la forja.

### 2.1. LA FUSION ENCIENDE LA SEÑAL DE COSTURAS, PORQUE MIDE SOLAPE DE TOKENS

**Que es la señal.** `scripts/costuras_internas.py` caza repeticion DENTRO de un
nodo con dos señales independientes: **pareja de pasos** (`token_sort_ratio` de
rapidfuzz entre cada dos pasos del mismo nodo, umbral 80) y **alineacion de
bloques** (empareja el segundo bloque contra el primero en orden monotono y
promedia las tres mejores parejas, umbral 44). Basta con que dispare cualquiera y
se reportan siempre las dos.

**El hallazgo.** Cuando una operacion reparte bloques hacia un nodo receptor, el
receptor **nace o queda con la costura dentro**, y la señal se enciende sola. No
es un fallo del reparto: es aritmetica. `08_VERIFICACION.md` lo documenta nodo a
nodo. Tres ejemplares medidos:

| receptor | que recibio | costura medida |
|---|---|---|
| `fases_traccion_producto` | los pasos 4 a 6 de `fit_problema_solucion` | 7 pasos contra los 4 que tenia; **los tres que entraron repiten sus pasos 1, 2 y 4 casi literales** |
| `clasificacion_leads_abc` | los pasos 5 a 9 de `sales_funnel_get_keep_grow` | 10 pasos contra 5; **tres de los cinco que entraron repiten**, con las mismas cifras |
| `silla_vacia_del_cliente_en_decisiones` | un paso de cada uno de dos donantes | **2 pasos, y los dos son el mismo objeto**: el nodo NACE con la costura dentro y con nada mas |

**La regla que la casa escribio encima** (14 ago 2026, `08_VERIFICACION.md`):

> Una repeticion que un reparto crea dentro de un miembro entra a la nomina como
> COSTURA NUEVA, y **no se desteje en el acto**. Destejer en el acto seria una
> operacion que ninguna pagina escribio.
>
> Y su ampliacion del 15 ago: **el disparador de esta puerta es LA REPETICION, NO
> EL DOMICILIO.** Un nodo creado hoy es miembro hoy.

**Lo que significa para la forja.** La señal 1 de la aduana (`difflib` sobre
titulo mas resumen mas pasos) mide solape de texto igual que aquella mide solape
de tokens. **Cuando la forja ejecute su primera fusion, el superviviente quedara
con solape interno y cualquier candidato futuro que toque ese tema medira mas
alto contra el.** La consecuencia es doble: hay que medir la repeticion interna
del superviviente al fundir, y hay que saber que los umbrales se mueven solos
segun cuantas fusiones lleve el grafo.

### 2.2. EL SIMETRIZADOR Y LAS AUTO ARISTAS POR ALIAS

*Medido en `2026-08-14-doctrina-ops07.md` (14 ago 2026) y resuelto por decision
del fundador el mismo dia, camino A.*

**El mecanismo, medido 33 de 33.** Cada auto arista del grafo era **la vista
reciproca de un enlace que el gemelo DEPRECADO tenia hacia su superviviente**. El
paso 5 de `run_phase1.py` (simetrizar) fabrica toda reciproca que falte y la
escribe de vuelta al fichero del nodo; **su unica defensa comparaba LITERAL y
ninguna de las 33 era literal.**

> Retiras las 33, corres Gate 0, y las 33 vuelven: variacion neta CERO. **La
> sombra vuelve mientras viva lo que la proyecta.**

La salida elegida no fue tocar el simetrizador sino **matar la causa con datos**:
retirar las 33 vivas Y sus 33 reciprocas literales del gemelo deprecado, 66
entradas en 59 ficheros. Y una particion que conviene tener a mano, porque
distingue lo que molesta de lo que no:

| donde | que | cuanto |
|---|---|---|
| vivos | enlaces que resuelven al propio nodo | **33 en 27 nodos** |
| deprecados | reciprocas literales de esas 33 (**las que el simetrizador proyecta sobre vivos**) | **33 en 32 nodos** |
| deprecados | alias contra alias (**no proyectan sobre vivos**) | **48 en 33 nodos, censadas como INERTES** |

**Lo que significa para la forja.** La prueba D de `tests/test_aceptacion.py` ya
guarda la auto arista via alias, y esa guarda es correcta. Lo que la forja NO
tiene es el fabricante: no hay simetrizador. **La leccion aplicable es la
inversa: el dia que la forja añada cualquier paso que fabrique aristas
automaticamente, ese paso tiene que resolver antes de fabricar**, o volvera a
sembrar exactamente lo que el gate caza. Y la categoria INERTE (una arista mala
que no toca a ningun vivo) merece existir antes de que haya deprecados, no
despues.

### 2.3. LA VARA DE VEREDICTOS COMO REGISTRO DE CITAS

*Decision del fundador, 2 sep 2026,
`2026-09-02-opc05-bidireccionales-DECISION.md`.*

La guarda de bidireccionales no podia encenderse: 153 pares vivos y una lista
blanca de dos entradas, con 83 de esos pares **anteriores al mergebase**, o sea
estado previo que la campaña no habia creado. Meterlos todos en la lista blanca
habria sido escribir 151 excepciones sin lectura detras, que es justo lo que la
lista blanca vino a impedir.

**La salida, y es la pieza que la forja deberia copiar entera:**

> La lista blanca pasa de lista a mano a **REGISTRO DE CITAS**. Cada par
> bidireccional entre vivos exige un veredicto de lectura registrado **con cita**:
> el del cribado cuando existe (con cita del puesto) o la declaracion sellada de
> `P.10`. Solo los pares sin veredicto van a lectura dirigida. **Un par sin cita
> es rojo.**

**Y la mecanica del registro, que es lo que lo hace medible** (`P.5.2`, 3 sep
2026): el registro es un `jsonl` donde cada fila lleva su `razon`, y las
relecturas se **añaden por adicion** a esa razon marcando que son relectura y en
que vuelta. De ahi salen las cifras: 122 pares de lectura dirigida, 85 con al
menos una segunda lectura independiente, 37 con ninguna. **Cifras que se
recomputan de un fichero, no de un acta.**

**Lo que significa para la forja.** `config/pares_mutuos.jsonl` de la v0.2 es hoy
una lista blanca de la primera especie: guarda `razon_ida` y `razon_vuelta` en
texto libre, pero el gate solo comprueba **pertenencia**, no cita. Es exactamente
el diseño que My-idea tuvo que abandonar.

### 2.4. DOS AVERIAS DE CALIBRACION, PORQUE VALEN PARA LA FASE 2

Las dos salen de la recalibracion declarada de `costuras_internas.py` (15 ago
2026, decision del fundador, parada `2026-08-15-cableado-deprecado-y-costuras.md`).

**(a) EL CERO SILENCIOSO DE UNA SEÑAL MUERTA.** La señal de bloque recorria
`range(MIN_BLOQUE, n - MIN_BLOQUE + 1)` con `MIN_BLOQUE = 3`: **con cinco pasos
ese rango es VACIO y devolvia 0,0 dijera lo que dijera el texto.** Y los dos nodos
de calibracion tenian cinco pasos, porque la propia campaña los habia destejido.

> El 0,0 no era un nodo sin bloque: **era la señal muerta.**

El remedio del fundador: por debajo del minimo la señal devuelve **`NO APLICA`
explicito, y ese valor REVIENTA si alguien lo compara con un umbral**, en vez de
dejarse leer como "no hay bloque".

**(b) EL UMBRAL POR DEBAJO DE LA MEDIANA.** Al bajar `MIN_BLOQUE` se descubrio que
no era un solo dial: **tambien es la K del promedio de las K mejores parejas.**
Promediar dos en vez de tres subio el puntaje de todo el catalogo con el umbral
quieto, y la cola paso de 122 a 1.497 nodos, el 42,3 por ciento del catalogo. El
p50 de la señal nueva quedo en 45,8 contra un umbral de 44:

> El umbral quedo **POR DEBAJO DE LA MEDIANA. Disparar deja de ser noticia.**

Y la frase hermana, de la calibracion original del mismo instrumento: **una
baranda que caza lo correcto no es estricta, esta rota** (bajar el umbral de
pareja hasta cazar los dos nodos de calibracion habria cazado 856 nodos, el 24
por ciento del catalogo).

**(c) Y UNA TERCERA, DE LECTURA DE LA COLA** (banco de textos 9.19, 13 ago 2026):

> **La similitud alta caza duplicados, la media caza jerarquias.** Una cola
> ordenada por similitud pone delante los pares que dicen lo mismo y deja detras
> los que estan en distinto nivel: una madre que nombra un paso en una linea y un
> hijo que trae el procedimiento.

Con su precision del 18 ago: la figura **no viene repartida por la cola, viene en
RACIMOS**, y la cifra de la vara **sirve por TRAMO y no por par**.

**Lo que significa para la forja.** Los tres hallazgos apuntan al mismo sitio y
son el encargo de la fase 2: el umbral de una señal no se defiende con casos
plantados, **se defiende con la distribucion del catalogo entero al lado**, y la
banda de la señal predice de que ESPECIE es el vecino (gemelo arriba, hijo en
medio), que es informacion que la forja hoy tira.

---

## 3. CAMBIOS CANDIDATOS A LA FORJA v0.3

**Ninguno esta implementado. Ninguno toca umbrales.** Cada uno cita su regla
madre. Estan ordenados por lo que cuesta ponerlos, no por lo que valen.

| | cambio candidato | regla madre | por que |
|---|---|---|---|
| **C.1** | **MUTUO exige DOS LINEAS DISTINTAS.** El veredicto `MUTUO` pasa a pedir, en cada sentido, el paso concreto que se expande; la aduana rechaza el par cuando los dos sentidos citan el mismo paso | **9.22**, comprobacion que separa la figura de la duplicacion | La v0.2 ya exige `ida=` y `vuelta=` pero acepta dos razones sobre la misma linea, que es un solape disfrazado de enlace mutuo |
| **C.2** | **La lista blanca pasa a REGISTRO DE CITAS.** `config/pares_mutuos.jsonl` guarda la cita del veredicto (fecha y fila de la bitacora) y el gate exige que resuelva; par sin cita, rojo | **LA LISTA BLANCA ES UN REGISTRO DE CITAS**, 2 sep 2026 | Hoy el gate comprueba pertenencia, no cita: es el diseño exacto que My-idea abandono con 153 pares delante |
| **C.3** | **Huella de texto en el veredicto.** Cada fila de `bitacora/VEREDICTOS.jsonl` guarda una huella del texto de los dos nodos; `forja.py rancios` lista los veredictos cuya huella ya no casa | **LOS PARES RANCIOS**, 15 ago 2026 | Cinco de seis veredictos de un acto estaban emitidos contra texto muerto y nadie lo vio hasta que una regla obligo a mirar |
| **C.4** | **`NO APLICA` explicito en las señales.** Una señal que no puede medirse (candidato de un solo paso, vecino sin pasos) devuelve `NO APLICA` y revienta si se compara con un umbral, en vez de 0.0 | **EL CERO SILENCIOSO**, 15 ago 2026 | Un 0.0 de señal muerta es indistinguible de un 0.0 de vecino ajeno, y la forja hoy los escribe igual |
| **C.5** | **Repeticion interna del candidato.** La aduana mide paso contra paso DENTRO del candidato antes de compararlo con el dataset, y bloquea con salida propia | **P.19**, 14 ago 2026, y la señal de costuras | Un candidato que repite su propio objeto no tiene destino que buscar: el objeto ya esta en casa |
| **C.6** | **La razon de CONTINUA cita el paso.** El veredicto `CONTINUA` exige nombrar el paso de la madre que el hijo despliega; sin paso citado, se rechaza | **P.5.1 NOMBRAR NO ES PROCEDIMENTAR**, 3 sep 2026 | Cuatro caidas de clase en dos tandas fueron todas segundas lineas que solo nombraban |
| **C.7** | **Un REPITE contra dos vecinos abre UNA operacion, no dos.** La plantilla de reparto se emite una vez citando a los dos | **P.20 UN NODO, UN CORTE**, 14 ago 2026 | Cortar dos veces parte el mismo bloque en pedazos incompatibles |
| **C.8** | **Superviviente por derecho o por eleccion, declarado.** La plantilla de fusion obliga a decir cual de los dos es, y prohibe el argumento de cableado mientras el contenido no haya hablado | **9.3.1** y **P.8** | De ocho pares A de un acto, CERO nombraban ganador, y el auditor tuvo que escribir por que no usaba el cableado que ya habia medido |
| **C.9** | **Valvula de vigencia en la plantilla de fusion.** Antes de ejecutar, la nomina se re resuelve contra el dataset; si el acto ya fue consumido, se cierra por CONSUNCION con su medicion | **VALVULA DE VIGENCIA**, 4 sep 2026 | Una operacion ejecutada tres semanas antes seguia figurando como pendiente y el bucle la volvio a encargar |
| **C.10** | **Prueba de mutacion en la aceptacion.** Un modo de `tests/test_aceptacion.py` que muta el valor esperado de cada guarda y verifica que la prueba CAE; donde no haya nada que mutar, se declara | **EL CASO ROJO SE PRUEBA POR MUTACION**, 29 ago 2026 | Es la version dura del principio que la forja ya tiene escrito, y la unica que lo hace comprobable |
| **C.11** | **Renglones que le faltan al bucle de la forja:** hueco de acta, la escalada se encarga, el reporte abre con la vuelta y crece por anexion, tope de cinco tareas, la identidad se lee de git | **AUDITOR.md** ciclo 0 (15 ago), **AUDITOR.md** regla 2 (29 ago), **EJECUTOR.md** regla 1 (4 sep y 26 ago) | La forja copio el bucle en agosto; estos cuatro renglones nacieron despues y curan averias que ya ocurrieron dos veces cada una |
| **C.12** | **Regla de conflicto en el banco.** `docs/BANCO_DE_REGLAS.md` declara en cabecera que entre dos entradas fechadas que se contradigan gana la mas reciente y la perdedora se corrige | **19 ago 2026**, punto 1 del punto brillante | Cuatro textos sellados chocaron con una regla posterior y hubo que parar el bucle para resolverlo |
| **C.13** | **Sucesor declarado en `vigencia`.** El campo admite norma vieja tachada mas norma nueva al lado, y el censo lo refleja | **LAS INSTITUCIONES DE LIBRO SE MANTIENEN AL DIA**, 28 ago 2026 | Borrar el nombre de una norma extinta deja el catalogo mudo sobre la que si rige |
| **C.14** | **La banda de la señal, no solo el valor.** El informe de vecinos dice en que tramo cae cada señal y que especie predice ese tramo | **9.19 LA COLA CAMBIA DE PRESA**, 13 ago 2026 | La forja hoy imprime tres numeros sin decir que significa que uno este alto y otro medio |

**Lo que NO se propone, y se dice para que conste:**

- **No se propone tocar ningun umbral.** Eso es la fase 2 y necesita el grafo
  final (seccion 4).
- **No se propone añadir señales nuevas.** Las tres actuales todavia no se han
  medido contra un corpus real.
- **No se propone el indice semantico por embeddings.** La campaña lo tiene y le
  costo dos paradas (el muro del indice y el candidato sin vector); si algun dia
  entra, entra como HERRAMIENTA DE SESION CON CREDENCIAL y con la leccion del
  2 sep 2026 delante: **el vector del candidato se fabrica del texto del propio
  candidato, no del grafo.**

---

## 4. POR QUE LA FASE 2 ESPERA, Y QUE NECESITA

La fase 2 es la calibracion de los umbrales de `config/umbrales.json`. Hoy esos
tres numeros estan medidos sobre **cinco casos plantados** y asi lo declara
`docs/BANCO_DE_REGLAS.md` D.4. La campaña de My-idea midio dos veces por que eso
no basta:

1. **Una baranda que caza lo correcto puede estar rota.** El umbral que cazaba los
   dos nodos de calibracion cazaba tambien el 24 por ciento del catalogo.
2. **Un umbral se juzga contra la distribucion, no contra sus ejemplares.** El
   dia que el p50 de la señal quedo por encima del umbral, disparar dejo de ser
   noticia, y eso solo se ve con el catalogo entero delante.

**Lo que la fase 2 necesita, cuando el grafo final exista:** la distribucion de
las tres señales sobre todos los pares del catalogo (p50, p90, p99), la banda por
tramo de cada una, y la tasa de acierto por tramo separando gemelo de jerarquia
por el 9.19. Con eso, y solo con eso, los tres numeros se pueden defender.

---

## 5. LO QUE ESTE DOCUMENTO DEJA ABIERTO PARA ALEXIS

No son paradas: son preguntas que la cosecha levanto y que este documento no
resuelve porque no le toca.

1. **De los catorce candidatos de la seccion 3, cuales entran a la v0.3 y en que
   orden.** Mi lectura, y es opinion: **C.1, C.2, C.3 y C.4** son los que curan
   averias que la forja ya tiene puestas hoy; **C.10 y C.11** son baratos y
   guardan el bucle; el resto puede esperar a que la forja tenga un libro dentro.
2. **Si la metrica de credito entra ahora o cuando arranque el bucle.** La
   campaña la tuvo desde el dia uno y le sirvio; la forja no la tiene escrita, y
   la regla de las tres especies (clase, cifra publicada, reporte) es mas facil
   de escribir antes de la primera caida que despues.
3. **Si la forja adopta la nocion de nodo DEPRECADO.** Hoy solo tiene
   `ids_alias`. La doctrina de **EL DEPRECADO ES ARCHIVO** esta lista para
   copiarse, pero adoptarla cambia el esquema del nodo y eso es decision de casa.
