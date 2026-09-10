# ENCARGO DE LA VUELTA 2: CERRAR EL LOTE 1, LIBRO `onu_consumidor`

*Escrito por el auditor el 10 sep 2026, con el ACTA 1 delante
(`docs/loop/ACTA_AUDITOR.md`). Es la vuelta que deja el lote 1 listo para que el
fundador decida si se inserta.*

> **EL FUNDADOR LEYO EL ACTA 1 Y FIRMO, EL MISMO 10 sep 2026.** Tres de sus
> adjudicaciones dejaron de ser fallos de acta y son **reglas del banco**:
> **D.27** la prueba del inventario con sus tres restricciones, **D.28** la sede
> de `PARA_ALEXIS.md`, **D.29** la arista que la señal no levanta.
>
> **Las citas, a partir de ahora, van al banco.** Un fallo de acta vale para una
> vuelta; una regla del banco vale siempre. Y las tres piden lo mismo que ya
> pedia este encargo: **no cambia tu trabajo, cambia de que cuelga.**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO QUE TIENES QUE SABER ANTES DE EMPEZAR

**LEE `docs/loop/EXTRACTOR.md` ENTERO Y LUEGO `docs/loop/ACTA_AUDITOR.md` ENTERA.**
El acta no es una nota de animo: trae **seis discutibles adjudicados, una vara
adjudicada con su restriccion y un hallazgo mio que te toca reparar**. Sin ella
la TAREA 2 no se entiende.

**LA VUELTA 1 SALIO BIEN Y SE DICE CON SUS CIFRAS:** cero caidas de clase, cero
de cifra publicada, los seis discutibles marcados a ciegas sostenidos uno a uno.
**Lo que no cubrio el marcado esta en la TAREA 2**, y es lo que va delante.

**SIGUES EN CUARENTENA.** El arnes arranca en `MODO_INSERCION=cuarentena` y **la
insercion es una autorizacion del fundador, no un default** (D.26). Aunque los
seis candidatos queden perfectos despues de la TAREA 2, **no entran**. No corres
`python forja.py insertar` ni una vez.

**Y NO FABRICAS MAQUINARIA** (seccion 13, cosecha 7.F). Ni arneses, ni guardas,
ni lectores. En particular, y lo digo porque el reporte de la vuelta 1 lo dejo
señalado: **no toques la señal 3, ni el `ratio` de `src/aduana.py`, ni la
calibracion.** El auditor ya adjudico ese punto en el ACTA 1 seccion 3.4 y el
remedio es de lectura, no de codigo. **Va dentro de la TAREA 2.**

---

## LO QUE EL AUDITOR ADJUDICO, Y QUE YA NO ES TUYO DECIDIR

**Esto es doctrina viva para esta vuelta. No lo reabres: lo aplicas y lo citas.**

### 1. LA PRUEBA DEL INVENTARIO: ADJUDICADA, con tres restricciones

Tu vara de `2.A.2` **queda adjudicada** como aplicacion de la regla escrita
*NOMBRAR NO ES PROCEDIMENTAR* mas la prueba del manual *existe quien lo ejecuta*
(`EXTRACTOR.md` seccion 9, manual seccion 4). **No era doctrina nueva: era esa
regla leida entera.** Se aplica asi, y las tres restricciones son parte de la
adjudicacion:

1. **el inventario que cuenta es de MEDIOS, ETAPAS u OBJETOS DE TRABAJO.** Un
   inventario de METAS o de FINES no cuenta: nombrar adonde hay que llegar sigue
   siendo nombrar;
2. **el adjetivo de adecuacion en el sitio del criterio tumba, aunque haya
   inventario**;
3. **esto NO mueve la vara de continua contra repite.** Esa sigue congelada, y
   moverla es parada.

**YA ENTRO EN EL BANCO: ES `D.27`, RATIFICADA POR EL FUNDADOR el 10 sep 2026 con
estas tres restricciones literales**, colgando de *NOMBRAR NO ES PROCEDIMENTAR*
con su cita. Tambien esta en `EXTRACTOR.md` **seccion 9.1**, que es tu sede de
consulta. **Citala como D.27, no como fallo del acta.**

**Y `D.27` TRAE UN COROLARIO QUE NO ESTABA EN EL FALLO Y QUE ES EXACTAMENTE TU
TAREA 2:** si el libro pone el inventario pero **no** pone el destinatario, ni el
responsable, ni el periodo, **esos no se escriben**. Un paso que cierra un bucle
que el libro deja abierto es un **PUENTE**.

### 2. LOS SEIS DISCUTIBLES: los seis sostenidos

Ninguno levantado. El **5** sostenido **con correccion**, que es trabajo tuyo en
la TAREA 2.

### 3. LA ASIMETRIA DE LA SEÑAL 3: confirmada, y no es parada

La reprodujo el auditor al sexto decimal. **No contradice ninguna cifra
publicada**: el fixture del hijo de esta casa mide `0,657718` **en los dos
sentidos**, o sea los `0,658` publicados. Y tu par madre e hijo **es una
dependencia de proceso**, que es la clase que `CALIBRACION_D4.md` seccion 7 ya
declara que la señal levanta el 3,0 por ciento de las veces. **La jerarquia la
caza la LECTURA (D.19), y la tuya la cazo.** Lo que faltaba era dejarla escrita
donde no se pierda, y eso va en la TAREA 2.

### 4. UNA CORRECCION DECLARADA EN ESTE MISMO DOCUMENTO

**El encargo de la vuelta 1 decia, en su seccion LAS PARADAS:** *"Paras y
escribes `docs/loop/PARA_ALEXIS.md` si..."*. **Eso chocaba con `EXTRACTOR.md`
secciones 7 y 14 y con `AUDITOR_FORJA.md` 5.6**, que dicen que `PARA_ALEXIS.md`
es del auditor y solo del auditor. **Lo trajiste declarado y acertaste.**

**Queda corregido en este encargo, y el texto viejo no se borra:** vive en el
`PROMPT_SIGUIENTE.md` de la vuelta 1, commiteado en `ea6c9f4` y antes, y esta
citado en el ACTA 1 seccion 3.5. **La formula vigente esta al final de este
documento.**

---

## EL LIBRO Y LO QUE QUEDA DE EL

**Clave canonica `onu_consumidor`, ya registrada.** Cuatro ficheros en
`fuentes/onu_consumidor/`, y este es el saldo medido al cerrar la vuelta 1:

| fichero | unidad | palabras | estado |
|---|---|---:|---|
| `cap_00.md` | portada y creditos | 171 | **no se mina.** Es de donde sale la ficha de la fuente |
| `cap_01.md` | V-B, parrafos 16 a 19 | 376 | **no minado por la marca FRONTERA.** Cerrado en la vuelta 1 |
| `cap_02.md` | V-C, parrafos 20 a 32 | 819 | **minado.** 6 candidatos en cuarentena, cero inserciones |
| `cap_03.md` | V-F, parrafos 37 a 41 | 389 | **SIN MINAR. Es el capitulo de esta vuelta** |

**Con `cap_03` cerrado, el lote 1 queda entero.** Eso importa para el final de
esta vuelta y para el acta que la audite.

---

## LAS TAREAS DE ESTA VUELTA

**Tope de cinco tareas (seccion 3). Estas son cuatro, y la 2 es bloqueante.**

### TAREA 1. Los registros

- **Lee `docs/loop/ACTA_AUDITOR.md` entera** y deja constancia en tu reporte de
  que la leiste, con la fecha del acta y su veredicto general.
- **Recoge las cuatro adjudicaciones** de arriba en la apertura de tu reporte,
  cada una con su cita. No las reabres.
- **Recoge la caida declarada contra ti**, que es una y de especie REPORTE que no
  acumula: escribiste *"su salida esta en cada commit"* refiriendote al hook, y
  **la salida del hook no esta en ningun commit de la vuelta 1**. El auditor la
  reparo en el suyo pegando la salida en el cuerpo. **Tu haras lo mismo en los
  commits de esta vuelta.**
- **Recoge tambien el limite que el auditor se puso a si mismo:** tu frase *"los
  seis pasaron la aduana al PRIMER intento"* **no es clonable contra el repo**,
  asi que quedo marcada A VERIFICAR y no aceptada. **Se arregla desde esta
  vuelta: cada vez que un candidato caiga en la aduana, pegas la salida del
  informe que lo tumbo, entera, en el reporte.** Si no cae ninguno, lo dices asi.

### TAREA 2, BLOQUEANTE. La pasada de transcripcion sobre los seis candidatos

**Va antes que `cap_03` y no se salta.** El motivo es el que hace irreversible
todo lo demas: **insertar es la unica accion de esta casa que no se deshace
leyendo** (D.26), y el fundador puede autorizar la insercion en cualquier
lanzamiento.

**Tu propio DISCUTIBLE 6 tenia el criterio correcto y no lo aplicaste a los otros
cinco.** Quitaste un paso de `verificar_afirmaciones_ambientales_publicidad`
porque *el bucle lo cerrabas tu y no el libro*. **El auditor releyo los 36 pasos
contra sus parrafos y encontro el mismo error en cuatro candidatos:**

| candidato | paso que el libro NO escribe |
|---|---|
| `vigilar_practicas_comerciales_perjudiciales` | paso 6, el traslado del expediente a la autoridad. El parrafo 21 alienta a vigilar y **no encarga ningun traslado** |
| `detectar_abusos_contractuales_consumo` | paso 6, el traslado del contrato marcado. El parrafo 26 **no nombra destinatario** |
| `formular_codigo_comercializacion_empresarial` | paso 4 (quien responde de cada regla) y paso 6 (la comprobacion al cabo del primer periodo). El parrafo 31 **no pone ninguna de las dos** |
| `examinar_normas_pesos_medidas` | paso 1, fijar por escrito el periodo. El parrafo 32 dice *periodicamente* y **el periodo lo fijas tu** |

**`informar_efectos_ambientales_productos` esta salvado**, y se dice para que no
lo toques de mas: su paso 7 aplica el criterio *inequivoca*, que si es del libro.

**LO QUE HACES, candidato por candidato y con el parrafo delante:**

1. **Marca cada uno de los 36 pasos** como TRANSCRIPCION (el libro pone el medio,
   la etapa o el objeto) o como PUENTE (lo escribiste tu). La marca va en tu
   reporte, en una tabla, **no dentro del JSON**.
2. **Cada PUENTE se resuelve de una de estas dos formas, y dices cual y por que:**
   se **retira** del nodo, o se **reescribe** para que no afirme lo que el libro
   no dice. **Un puente no se queda callado dentro de un nodo.**
3. **CADA CORRECCION CITA EL PARRAFO QUE NO LO DICE**, con su fichero y su linea
   (`cap_02.md:NN`), y **la frase del parrafo que si esta**, para que se vea el
   hueco. *Requisito del fundador, 10 sep 2026.* No basta con escribir *lo
   retiro*: **la cita es la prueba de que se releyo el parrafo y no la memoria
   del reporte anterior.**
4. **Vuelve a pasar por la aduana en seco CADA candidato que hayas tocado**, en
   el mismo acto (seccion 16), **despues de la correccion**, y **pega la salida**:
   caiga o no caiga. *Requisito del fundador, 10 sep 2026.* Un candidato
   corregido que nadie volvio a pasar es un candidato sin medir.
5. **Vuelve a correr el informe del lote entero** cuando acabes, y pega el saldo.

**Y DENTRO DE ESTA MISMA TAREA, LA ARISTA QUE SE PIERDE SI NADIE LA ESCRIBE:**

    formular_codigo_comercializacion_empresarial   (parrafo 31, MADRE)
        baja a
    verificar_afirmaciones_ambientales_publicidad  (parrafo 30, HIJO)

**Medido: en el sentido en que el hijo llegara de candidato, la señal 3 da
0,572289 y el umbral esta en 0,60. NO va a levantar a nadie.** Si esa arista solo
vive en la prosa de un reporte que se reescribe cada vuelta, se pierde.

**Escribela en tu reporte de esta vuelta en un bloque propio y titulado**, con:
la direccion, la razon con la vara (que añade el HIJO a la MADRE), **el orden de
insercion que exige (la madre primero)**, y la nota de que se cablea en el acto
del veredicto (`docs/FLUJO_DE_EXTRACCION.md` fase 2, paso 4). **Los JSON siguen
viajando con `nodos_previos` y `nodos_siguientes` vacios, y eso estuvo bien.**

**ESTO ES AHORA `D.29`, RATIFICADA POR EL FUNDADOR el 10 sep 2026:** la arista se
declara **POR LECTURA, en el acto de la insercion**, como D.19 manda, **y el
umbral NO se toca**. Que la señal mida 0,572289 y el umbral este en 0,60 no es un
argumento para bajarlo: es la razon por la que la lectura no delega en la señal.

### TAREA 3. `cap_03`: publicar la frontera y extraer, uno a uno y por la aduana

**SIGUES CON `cap_03` EN ESTA MISMA VUELTA SI LAS CORRECCIONES DE LA TAREA 2
CIERRAN** *(decision del fundador, 10 sep 2026)*. Cerrar significa las tres
cosas: los 36 pasos marcados, los puentes resueltos con su cita, y **el informe
del lote sin ninguna caida que no sepas explicar**.

**SI NO CIERRAN, NO EMPIEZAS `cap_03`.** Lo dices en el reporte con su razon y te
detienes ahi. **Media correccion mas un capitulo nuevo es peor que una correccion
entera**: el lote 1 existe para dejar el instrumento medido, no para acumular
candidatos.

**Apartado V-F, parrafos 37 a 41, 389 palabras.** Es el ultimo capitulo minable
del lote.

1. **Leelo entero.**
2. **Publica la frontera ANTES de cortar** (seccion 10): parrafo a parrafo, con su
   linea, que es procedimiento y que es postura, **y aplicando la prueba del
   inventario ya adjudicada con sus tres restricciones**. Di el saldo: cuantos
   procedimientos y cuantas posturas de cinco parrafos.
3. **Despues, cada candidato:** lo escribes en
   `cuarentena/onu_consumidor/<id>.json`, corres
   `python forja.py informe cuarentena/onu_consumidor/<id>.json`, lo corriges si
   cae, **y solo entonces cuenta como escrito** (seccion 16).
4. **Contesta los tres casos que el manual nombra** (serie numerada, caso o
   estudio, cifra del autor), aunque los tres salgan en negativo.
5. **Busca la madre POR LECTURA**, contra el dataset y contra los seis hermanos de
   cuarentena. **La cola vacia certifica sin gemelo, no sin madre** (D.19).

**AVISO DE MATERIAL, y no es una pista de lo que tiene que salir:** los cinco
parrafos de `cap_03` estan cargados de adjetivos de adecuacion (*justos*,
*efectivos*, *transparentes*, *poco costosos*, *accesibles*). **Tu propia vara
dice lo que eso delata.** Si el capitulo da menos candidatos que `cap_02`, eso es
el resultado y se publica con su razon. **Una tarea que produce cero nodos con su
razon escrita vale tanto como una que produce cinco. Lo que no vale es una tarea
sin razon.**

**TRAMO:** entre cinco y quince candidatos por vuelta (seccion 12.4). Con los seis
de `cap_02` revisados mas lo que de `cap_03`, vas holgado dentro.

### TAREA 4. El cierre del lote y el commit

1. **`python forja.py informe --carpeta cuarentena/onu_consumidor`** sobre el lote
   entero, ya con `cap_03` dentro. Pegas el saldo completo: cuantos entrarian,
   cuantos bloquearian, cuantos caerian **y por que guarda**.
2. **Un commit por capitulo** (seccion 17), en `extraccion-mundo-11`, con los JSON
   dentro (D.25). El mensaje dice **que capitulo y cuantos candidatos**, y el
   cuerpo lleva **la salida del hook**.
3. **DECLARA EL LOTE 1 CERRADO CONTANDO SUS CUATRO FICHEROS, UNO A UNO.** La
   vuelta 1 declaro cola de `cap_03` y **no dijo nada de `cap_00`**. No fue caida,
   porque el encargo ya lo habia resuelto, pero **un libro se cierra contando sus
   cuatro piezas, no tres.** Cada fichero con su estado: minado, no minado por la
   marca, o no minable por ser portada.

---

## EL BLOQUE DE APERTURA DE `docs/loop/REPORTE.md`

**Lo abres AL EMPEZAR, no al final** (seccion 3). Copia esto y rellenalo **con lo
que midas tu**, no con lo que diga esta tabla: si el instrumento discrepa de una
linea de aqui, **escribes la del instrumento y declaras la discrepancia al lado**,
que es exactamente lo que la vuelta 1 hizo bien con la fecha.

    # REPORTE DEL EXTRACTOR

    ## VUELTA 2, lote 1 (onu_consumidor), cap_03 y la revision de cap_02

    | | |
    |---|---|
    | fecha | (la que mida tu instrumento, con el comando al lado) |
    | rama | extraccion-mundo-11 |
    | commit de apertura | (git rev-parse HEAD tras commitear lo pendiente) |
    | lote | onu_consumidor, LOTE 1 DE CALIBRACION (D.24) |
    | capitulo de extraccion | cap_03.md, apartado V-F parrafos 37 a 41 |
    | acta del auditor leida | ACTA 1, 2026-09-10, reporte verificado |
    | nodos en el dataset al empezar | (wc -l dataset/nodos.jsonl, antes de tocar nada) |
    | candidatos en cuarentena al empezar | (contados) |
    | inserciones autorizadas en esta vuelta | CERO. MODO_INSERCION=cuarentena (D.26) |

    ### Las cuatro tareas

    | # | tarea | estado | resultado |
    |---|---|---|---|
    | 1 | registros del acta y de las adjudicaciones | | |
    | 2 | BLOQUEANTE: pasada de transcripcion sobre los 6, mas la arista escrita | | |
    | 3 | cap_03: frontera publicada y candidatos por la aduana | | |
    | 4 | informe del lote entero, commit y cierre del lote | | |

    ### Discutibles marcados ANTES de saber si acierto

    (los marcas aqui segun aparecen, no al final)

**Cada fila se anexa AL CERRARSE su tarea.** Una vuelta cortada deja reporte
parcial, **nunca vacio**.

**Y MARCA TUS DISCUTIBLES A CIEGAS OTRA VEZ.** Los seis de la vuelta 1 son lo que
hizo posible el acta 1: sin ellos el auditor no habria tenido por donde empezar.

---

## LO QUE ESTA VUELTA TIENE QUE DEJAR MEDIDO

Ademas de los nodos, en el cierre del reporte:

1. **Cuantos de los 36 pasos de `cap_02` eran PUENTE y no transcripcion**, con la
   cuenta por candidato. Es la primera medida real de cuanto pone el extractor de
   su cosecha cuando cree estar transcribiendo, **y no es una acusacion: es la
   cifra que le falta a esta casa.**
2. **Si `cap_03` dio mas o menos candidatos por palabra que `cap_02`**, con las
   dos cifras al lado. `cap_02` dio 6 candidatos en 819 palabras.
3. **Si la prueba del inventario, ya adjudicada, te resolvio `cap_03` sola** o si
   te volvio a faltar un corte. **Si te falto, lo marcas como discutible y no lo
   adjudicas tu.**
4. **Cuantos candidatos cayeron en la aduana y por que guarda, con la salida
   pegada.** Si cayeron cero, lo dices y dices contra que se lee ese cero.

---

## LAS PARADAS

**Paras, lo declaras en TU REPORTE y te detienes si:**

- una regla de la casa te obliga a algo que rompe otra regla de la casa;
- necesitas mover un umbral, una regla de id, el esquema o la vara de continua
  contra repite. **Ninguna vuelta mueve nada de eso** (seccion 5, D.23, y
  `AUDITOR_FORJA.md` 6.3);
- una adjudicacion de este encargo te obliga a escribir un nodo que tu lectura
  dice que no esta en el libro.

**TU NO ESCRIBES `docs/loop/PARA_ALEXIS.md`.** Eso lo hace el auditor, y solo el
(**`D.28` del banco**, ratificada por el fundador el 10 sep 2026; `EXTRACTOR.md`
secciones 7 y 14, `AUDITOR_FORJA.md` 5.6). **Y la regla general que D.28 deja
escrita, que vale mas que el caso: un encargo asigna trabajo, NO MUEVE UNA SEDE.**
Si un encargo futuro te dice lo contrario, manda la sede y eso es una parada. **Declaras la parada en
tu reporte, con su motivo y su estado, y te detienes.** El auditor la recoge.

**NO paras por:** que un candidato caiga en la aduana (lo corriges y pegas la
salida), que `cap_03` de pocos nodos o ninguno (se dice con su razon y ya), ni
porque la revision de la TAREA 2 te obligue a retirar pasos de tus propios nodos
de la vuelta 1. **Eso ultimo no es un castigo: es la aduana funcionando antes de
que el dato entre.**

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.**
