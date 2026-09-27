# PARADA DEL 10 SEP 2026: FALTA EL LIBRO DEL LOTE 2

> **DECISION DEL FUNDADOR (10 sep 2026): se llena la bandeja entera de una vez,
> mundos 10 y 11, y el lote 2 arranca.**

> **ARCHIVADA, Y RESUELTA POR EXCESO.** Esta parada pedia un libro. El fundador
> trajo los once: 164 capitulos y 557.501 palabras en `fuentes/`, con sus once
> claves registradas en `fuentes/FUENTES_CANONICAS.json`. **Las dos condiciones
> que el auditor midio en rojo estan ahora en verde, y no solo para el lote 2:
> para los diez lotes que quedan.**
>
> Se archiva **entera y sin tocar una palabra de su cuerpo**. El bucle ya no esta
> detenido por ella: vive en `docs/loop/paradas/` y el arnes solo mira
> `docs/loop/PARA_ALEXIS.md`.

---


> **Escrito por el auditor del bucle del extractor, el 10 sep 2026, al cerrar la
> vuelta 3.** Sede del auditor (`AUDITOR_FORJA.md` 5.6, **`D.28`**). El extractor
> no escribe aqui, y no lo hizo: declaro su parada en su reporte, que es lo que le
> toca, y me la paso.
>
> **EL BUCLE ESTA DETENIDO.** `docs/loop/PROMPT_SIGUIENTE.md` esta vacio y este
> fichero existe: el arnes se detiene por cualquiera de las dos cosas.

---

## 0. LA VERSION CORTA, EN CUATRO LINEAS

**El bucle no se ha quedado sin trabajo. Se ha quedado sin libro.**

    fuentes/smart_who/            NO EXISTE en la maquina
    clave "smart_who"             NO ESTA en fuentes/FUENTES_CANONICAS.json
    la vuelta 3                   0 capitulos, 0 candidatos, 0 pasos, 0 inserciones
    todo lo demas                 VERDE, y el grafo intacto en 8 nodos

**Las dos cosas que faltan son tuyas y ninguna la puede producir el bucle.** Y
**hacen falta las dos**: traer el libro sin registrar la clave no desbloquea nada,
y lo probe por mutacion en vez de suponerlo (seccion 2.2).

---

## 1. EL MOTIVO: DECISION DE ALEXIS, Y NO ES LA MISMA PARADA DE LA VEZ PASADA

**La parada anterior (`paradas/2026-09-10-lote-1-consumado.md`) fue la parada
feliz: el lote 1 estaba consumado y no quedaba trabajo.** Tu la resolviste, y bien:

| lo que aquella parada te pidio | lo que hiciste |
|---|---|
| **autorizar la insercion de los seis** (`D.26`) | **HECHO.** `762e31d`. El grafo paso de 2 a 8 nodos |
| **traer el libro del lote 2** (`D.24`) | **NO.** Y es lo unico que para esta vuelta |
| **decidir el merge** | **NO.** La rama sigue viva y verde |

**Y ademas hiciste mas de lo que se te pidio** (`db88620`): escribiste el encargo
del lote 2, subiste el ritmo a dos capitulos por vuelta, firmaste `D.30` y `D.31`,
y **añadiste a `AUDITOR_FORJA.md` la seccion 8** que esta acta estrena.

**Lo unico que falto fue la carpeta del libro.** Por eso la vuelta 3 arranco,
commiteo sus artefactos, abrio su reporte en esqueleto, midio las dos condiciones
de apertura de tu propio encargo, **y se detuvo delante de la puerta.**

**ESTA PARADA ES DISTINTA DE LA ANTERIOR Y CONVIENE QUE NO SE CONFUNDAN DENTRO DE
UN MES:** aquella paro **porque no quedaba trabajo**; esta para **porque el trabajo
esta encargado, el encargo esta escrito y bien escrito, y falta la materia prima.**

---

## 2. EL ESTADO EXACTO, MEDIDO POR MI EN ESTA VUELTA

*Nada de esto se copio del reporte del extractor. Todo se re corrio.*

### 2.1. El repo

| | |
|---|---|
| **hash** | **`53b9bf0`**, rama `extraccion-mundo-11`. **Local y `origin` en el mismo hash** |
| **nodos vivos** | **8** (`wc -l dataset/nodos.jsonl`), 0 deprecados, 0 alias |
| **aristas** | **2 relaciones**, escritas en sus dos extremos cada una |
| **veredictos** | **2**, los dos CONTINUA, **los dos con razon escrita.** 0 SANO |
| **fuentes canonicas en la tabla** | **2**: `manual_sistema_conocimiento`, `onu_consumidor` |
| **pasos en el dataset** | **43** (11 de los dos semilla, **32 de los seis del lote 1**) |
| **cuarentena viva** | **0 candidatos.** Los seis del lote 1 archivados en `_insertados/` (`D.31` funcionando) |
| **gate** | **VERDE**, 8 nodos, 12 guardas |
| **barrido de guiones** | **VERDE** |
| **resolutor** | **VERDE** |
| **prueba de aceptacion** | **65 de 65, 0 fallos, 0 errores** |

**LAS CUATRO GUARDAS EN VERDE, corridas por mi al abrir y al cerrar.** Y el rojo
del barrido de la vuelta 2 **no se repitio**: el testigo del extractor traia nueve
guiones prohibidos entonces y trae **cero** ahora. **El remedio que escribi en el
ACTA 2 se sostuvo solo.**

### 2.2. Lo que falta, y la prueba de que hacen falta las dos cosas

    $ find fuentes -type f | sort
      fuentes/FUENTES_CANONICAS.json
      fuentes/onu_consumidor/cap_00.md ... cap_03.md     (cuatro, y ni uno mas)

    $ ls fuentes/smart_who/
      No such file or directory                          (no existe; no es que este vacia)

    $ git log --all --oneline -- 'fuentes/smart_who*'
      (vacio: no ha existido nunca en ninguna rama)

    claves de fuentes/FUENTES_CANONICAS.json:
      ['manual_sistema_conocimiento', 'onu_consumidor']   smart_who: False

**LA SEGUNDA CONDICION SOBREVIVE A LA PRIMERA, Y LO PROBE EN VEZ DE SUPONERLO.**
Coja un nodo real del lote 1, le cambie el id, **y mute solo la clave de fuente**:

| ficha | clave | resultado del `informe` |
|---|---|---|
| **MUTANTE** | `smart_who` | **CAE.** `LA FUENTE ES UN CAMPO SAGRADO (manual principio 8)`, con el mensaje de `src/aduana.py:197` |
| **CONTROL** | `onu_consumidor` | **NO cae por esa guarda.** Pasa a bloqueo por vecino, que es otra cosa |

**La guarda muerde y ademas discrimina.** Si mañana copias los siete capitulos y la
clave sigue fuera de la tabla, **el primer candidato del lote 2 lo tumba la aduana
igual.** No es un fallo: es el manual seccion 7.1 haciendo su trabajo.

---

## 3. LO QUE NECESITO DE TI, POR ORDEN

### 3.1. LOS SIETE CAPITULOS, en la maquina donde corre el arnes

    fuentes/smart_who/cap_01.md
    fuentes/smart_who/cap_02.md
    ...
    fuentes/smart_who/cap_07.md

**No llegan por `git pull` y no es un defecto:** `.gitignore` bandeja (a) deja
`fuentes/*/` fuera del repo **a proposito**, porque son texto con derechos de otro
autor. **Esa razon no la toca esta parada.** Lo pones tu a mano, como pusiste el
lote 1.

**Y una peticion pequeña que ahorra una vuelta:** si el numero de capitulos o sus
nombres no coinciden con los siete que `D.24` supone, **dilo en el encargo al
reabrirlo**, porque el ritmo de dos por vuelta se dimensiono sobre siete capitulos
de unas 6.332 palabras.

### 3.2. LA CLAVE `smart_who` EN LA TABLA CANONICA, con la ficha del libro delante

`fuentes/FUENTES_CANONICAS.json`, con **titulo completo, autor, edicion y año.**

**Esto no lo puede hacer el bucle por dos razones independientes, y las dos
bastan:** (a) el fichero **no es sede del extractor**, y (b) **la ficha se lee de la
portada del libro**, que es exactamente lo que no hay en la maquina. Una ficha
tecleada de memoria seria **una fuente inventada en el campo que el manual llama
sagrado**, que es el peor sitio de todo el sistema para inventar algo.

### 3.3. EL MERGE, que te lo pido y no lo hago

**`extraccion-mundo-11` esta verde**, con las cifras de la seccion 2.1 delante y
todo pusheado a `origin`. **EL BUCLE NO FUNDE RAMAS Y EL BUCLE NO CREA REMOTOS**
(`AUDITOR_FORJA.md` seccion 3), asi que **este fichero PIDE el merge y no lo
ejecuta.**

Y una consideracion, no una recomendacion: la rama lleva ya **el lote 1 entero
insertado y medido**. Si el lote 2 va a tardar en tener libro, **una rama que
acumula tres vueltas y una campaña completa sin fundirse es una rama que se va
poniendo cara de resolver.**

### 3.4. LO QUE QUEDA PENDIENTE DE LA PARADA ANTERIOR Y NO HE MOVIDO

**La pregunta de doctrina de `D.27`** (*cuantos objetos hacen inventario*) sigue
**abierta, sin adjudicar y sin tocar**, exactamente donde la dejo el ACTA 2:
`paradas/2026-09-10-lote-1-consumado.md` seccion 3.4. **Ni el extractor ni yo la
hemos movido un milimetro**, y el nodo que la decide
(`examinar_normas_pesos_medidas`) **ya esta insertado**, asi que ahora la pregunta
vive en el grafo y no en cuarentena. **No es urgente y no bloquea nada. Pero el
lote 2 va a traer el mismo filo.**

---

## 4. LAS TRES COSAS QUE HAY QUE HEREDAR, Y ESTAN AQUI PORQUE NO HAY ENCARGO

*Mi protocolo dice que **la escalada se encarga, no solo se declara**, y que
declararla sin encargarla es caida propia mia. Como el encargo va vacio, las
encargo al unico sitio donde alguien las va a leer.*

### 4.1. ADJUDICADA A FAVOR: las dos condiciones se comprueban y se publican ANTES de la TAREA 1

**Es la unica propuesta que el extractor hizo esta vuelta, y la adjudico a favor**
(ACTA 3, seccion 3.6). Su argumento es correcto: **esta vuelta comprobo las dos
condiciones por suerte y no por regla**, porque tu las habias escrito arriba del
todo en el encargo. **Un encargo futuro que no las traiga dejaria al extractor
descubriendo el hueco a mitad de la TAREA 2, con candidatos a medio escribir
contra un libro que no tiene delante**, que es el escenario donde `D.30` predice
una tasa de puentes del **100 por ciento**.

**El remedio es una linea de reporte, NO una guarda.** Lo digo expresamente porque
la tentacion tomaria forma de guarda, y **la moratoria de maquinaria la prohibe por
su nombre** (cosecha 7.F). Ademas una guarda no podria juzgar nada: el texto fuente
no esta en el repo.

**Ya esta escrito en el encargo archivado**, en su cabecera, para que viaje solo.

### 4.2. EL HUECO QUE YA LLEVA TRES TANDAS, y que ahora es peor

> **El error de dejar pasar SIGUE SIN TASA Y SIN BANDA en esta casa.**

**Cero veredictos SANO en tres tandas**, asi que la muestra pineada
(`AUDITOR_FORJA.md` seccion 7) no ha tenido nunca poblacion que sortear. **No la he
inventado y no la voy a inventar**: una muestra fabricada sobre poblacion vacia
seria peor que ninguna.

**LO QUE HA CAMBIADO, Y ES A PEOR:** en la vuelta 2 esto era un hueco sobre seis
candidatos **en cuarentena**. Hoy **esos seis estan en el grafo.** Y sabemos,
medido, por que importa:

> **La aduana dio 6 de 6 verdes ANTES y DESPUES de retirar 13 puentes.**
> El instrumento no ve la especie de defecto que esta campaña produce.

**Es lo primero que hay que medir el dia que haya una tanda con veredictos de
verdad.** Y no pide maquinaria: pide una tanda que inserte.

### 4.3. MI PROPIA CAIDA, Y NO ESTOY REINICIANDO NADA

**Conte el campo `pasos` en un dataset donde el campo se llama
`pasos_accionables`.** Mi primera corrida devolvio **"0 pasos"** para los ocho
nodos, y **iba camino de publicar que el dataset tiene cero pasos** en un acta cuyo
trabajo era, justamente, verificar la linea base del 36 por ciento contra ese
dataset. **Habria sido una CIFRA PUBLICADA falsa en `docs/`: la especie que
acumula y que para el bucle a las dos.**

**La cace antes de publicarla** porque el resultado era absurdo, y abri las claves
reales del registro antes de escribir nada. **Se declara igual**: una caida que solo
se declara cuando escapa no es una metrica.

**MI RACHA PROPIA VA POR TRES ACTAS SEGUIDAS, y la dejo escrita en tres:**

| acta | mi caida | especie |
|---|---|---|
| 1 | una corrida que leyo un sitio distinto del que escribio | instrumento mal apuntado |
| 2 | una salida publicada que ninguna corrida pudo dar | transcripcion fabricada |
| 3 | un campo contado con un nombre que no existe | instrumento mal apuntado |

**Dos de las tres son de la misma especie, con una distinta en medio.** La cosecha
7.D pide tres SEGUIDAS de la misma para obligarme a abrir con el remedio, **asi que
leida a la letra no se dispara.** No me acojo a eso: **7.D nacio de una confesion
contra la letra, y usarla al reves seria indecente.**

**MI REMEDIO, aplicado ya y no prometido:**

> **Antes de publicar una cuenta sobre un fichero de datos, imprimo primero las
> claves reales de un registro y cuento contra una clave que existe.** Un cero
> devuelto por un campo inexistente es indistinguible de un cero medido.

**No he reiniciado mi racha.** Un auditor que pone su propia racha a cero se esta
absolviendo. La reinicia una decision tuya escrita en `docs/loop/paradas/`, o no se
reinicia.

---

## 5. LO QUE ESTA VUELTA COSTO, DICHO SIN ADORNO

**Una vuelta entera, unos 10 minutos de extractor y su coste, para escribir que no
habia nada que leer.** No fue trabajo mal hecho: el extractor comprobo las dos
condiciones **antes de la TAREA 1**, no escribio ni un paso inventado, no toco
ninguna sede ajena y dejo el reporte parcial en vez de vacio. **Se detuvo donde
habia que detenerse.**

**PERO HAY UN COSTE REAL Y NO ES EL DINERO:**

> **`PASOS INVENTADOS POR CAPITULO` NO EXISTE PARA ESTA VUELTA, y esa es la cifra
> con la que se dimensiona el lote 3.**

`AUDITOR_FORJA.md` seccion 8.1 tiene dos entradas (se mantiene o baja: mas
capitulos; sube: el techo a uno) **y esta vuelta no dispara ninguna, porque no se
escribio ni un paso.** No me la invento y no la firmo. **El lote 3 no se puede
dimensionar todavia.**

**Y las otras tres cosas que tu encargo pedia dejar medidas tambien quedan SIN
MEDIR**, dichas una a una: si dos capitulos de 6.000 palabras caben en una vuelta,
cuantos vecinos levanta la aduana con el grafo en ocho nodos, y si la prueba del
inventario aguanta en material narrativo. **Las tres siguen siendo preguntas
abiertas, y la primera vuelta con libro las contesta las tres.**

**LO QUE SI VERIFIQUE, y sirve de ancla para cuando el lote 2 arranque:** la linea
base del **36 por ciento** del lote 1 (13 puentes de 36 pasos) **se sostiene contra
el dataset de hoy**: los seis nodos insertados llevan **32 pasos vigentes**, que es
exactamente 36 menos los 4 retirados. **La cifra contra la que se va a comparar el
lote 2 esta comprobada.**

---

## 6. COMO SE RETOMA

**1. Pon el libro y registra la clave** (secciones 3.1 y 3.2). **Las dos.**

**2. Devuelve el encargo a su sitio.** No hay que reescribirlo: esta archivado
entero, sin tocarle una palabra al cuerpo.

    cp docs/loop/paradas/2026-09-10-encargo-lote-2-sin-libro.md docs/loop/PROMPT_SIGUIENTE.md
    (y le quitas la cabecera de archivado)

**El encargo sigue siendo valido entero**, incluido el ritmo de **dos capitulos por
vuelta**: nada de esta vuelta lo mueve, porque nada se midio. **Una medicion ausente
no autoriza a bajar el techo ni a subirlo.**

**3. Añadele la adjudicacion de 4.1**, que ya va escrita en la cabecera del fichero
archivado: **las dos condiciones de apertura se comprueban y se publican como su
propia linea del reporte, antes de la TAREA 1.**

**4. Borra `docs/loop/PARA_ALEXIS.md` o archivalo** en `docs/loop/paradas/` como
hiciste con el anterior. **Mientras exista, el arnes se detiene**, y hace bien.

**5. Relanza el arnes.** El rol se reparte solo por medicion: el ACTA 3 es mas
nueva que el REPORTE, asi que **arrancara como EXTRACTOR y no habra vuelta sin
auditar delante.**

---

## 7. Y SI DECIDES QUE EL LOTE 2 NO VA A TENER LIBRO PRONTO

**No es mi decision y no la tomo. Solo dejo el dato para que la tuya sea barata:**

- **`D.24` fija el orden de los lotes y el bucle no lo elige.** Saltar al lote 3
  (`zhuo_manager`) **seria cambiar el alcance de la extraccion**, que es una de las
  cosas que la casa te reserva expresamente. **Si lo decides, se escribe como
  correccion declarada de `D.24` y el bucle la obedece.** Lo que no puede es
  decidirlo.
- **Y `zhuo_manager` tampoco esta en la maquina.** Lo comprobe: `find fuentes` da
  cuatro ficheros de `onu_consumidor` y nada mas. **Cambiar de lote no ahorra el
  paso de traer un libro.**
- **La otra salida es cerrar la campaña aqui:** fundir `extraccion-mundo-11` con su
  lote 1 insertado y medido, y abrir el lote 2 en su propia rama cuando haya
  material. **Deja el trabajo hecho a salvo en vez de en una rama que envejece.**

**Las tres son tuyas. Yo solo he comprobado que las tres son posibles y que ninguna
la puede tomar el bucle.**

---

**FIN.** Reporte de la vuelta 3 **verificado**, cinco discutibles adjudicados y los
cinco sostenidos, **la guarda de la fuente probada por mutacion**, credito intacto,
**el grafo en ocho nodos y las cuatro guardas en verde**, y el bucle detenido
esperando **siete ficheros de texto y una linea en una tabla.**
