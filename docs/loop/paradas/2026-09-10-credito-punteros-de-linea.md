# PARADA DEL 10 SEP 2026: CREDITO ROTO POR PUNTEROS DE LINEA

> ## LAS CINCO DECISIONES DEL FUNDADOR, 10 sep 2026
>
> **4.1. LA RACHA `REPORTE` SE REINICIA CON ESTA DECISION.** Y el remedio va al
> banco como acto mecanico y no como promesa: **ninguna cita de linea se teclea en
> una TABLA del reporte sin que la salida literal de `sed -n` o `grep -n` quede
> pegada al lado, en el propio reporte.** El desfase de ocho lineas de la vuelta 7
> queda como ejemplar de la regla.
>
> **4.2. INSERCION AUTORIZADA** de los 44 candidatos de `cuarentena/smart_who/`. Y
> regla nueva, **EL ORDEN QUE LEE**: cuando la asimetria de una señal decide si un
> par se lee o no, **se inserta en el orden que lo lee**. `sostener_contacto`
> antes, `celebrar` despues, **y el par pide su veredicto**.
>
> **4.3. LOS ARTEFACTOS DEL ARNES** (`loop.log`, `ultimo_extractor.json`,
> `ultimo_auditor.json`) **son registro de maquina: EXCLUIDOS del barrido de
> guiones y del hook**, coherente con `D.20`. El arnes los sigue commiteando en su
> commit de artefactos.
>
> **4.4. EL REMEDIO ROTO DEL AUDITOR ACUMULA EN RACHA PROPIA**, especie **REMEDIO
> ROTO**, y **tres seguidas paran**. Y **LA APERTURA CIEGA PASA A CODIGO**: el
> arnes entrega al auditor candidatos y fuentes, **sella sus clases**, y **solo
> despues le expone el reporte**.
>
> **4.5. `who` ENTRA EN `INGLES_CON_EQUIVALENTE`.** Y **la A de *jugador A* no
> sobrevive en el id: la regla vigente se sostiene.** El borde `cap_06`/`cap_07`
> **no se toca: se lee como unidad y se declara.**

> **ARCHIVADA.** Este fichero fue `docs/loop/PARA_ALEXIS.md` hasta que el fundador
> resolvio lo que pedia. **Se archiva entero y sin tocar una palabra de su
> cuerpo**; lo unico añadido es esta cabecera. El bucle ya no esta detenido por el:
> vive en `docs/loop/paradas/` y el arnes solo mira `docs/loop/PARA_ALEXIS.md`.
>
> **Lo ejecutado, con su commit:** las cinco en `docs/BANCO_DE_REGLAS.md` D.33 a
> D.36, el arnes y las listas en el commit de doctrina, y la insercion de los 44 en
> el suyo.

---


> **PARADA DEL BUCLE DEL EXTRACTOR, escrita por el auditor al cerrar la VUELTA 7.**
> **Fecha: 2026-09-10**, leida del instrumento (`date`, `datetime.date.today()` y
> `src.aduana._hoy()`, los tres dan lo mismo).
>
> **El acta completa es `docs/loop/ACTA_AUDITOR.md`, ACTA 7 (a partir de la linea
> 5745). `docs/loop/PROMPT_SIGUIENTE.md` queda VACIO, como manda `AUDITOR_FORJA.md`
> seccion 3.**

---

## 1. EL MOTIVO, EN UNA LINEA Y LUEGO ENTERO

> ## **CREDITO ROTO. La racha de especie REPORTE llega a TRES TANDAS SEGUIDAS (tandas 5, 6 y 7), que es su condicion de parada escrita en `AUDITOR_FORJA.md` 5.4.**

**El ACTA 6 lo dejo escrito antes de que ocurriera, para que hoy no se pudiera
rebajar en caliente:**

> *"UNA SOLA CIFRA FALSA EN TABLA, CABECERA O CONCLUSION EN LA VUELTA 7 PARA EL
> BUCLE."*

**Han sido tres, las tres en tabla.**

### 1.1. Las tres caidas de la vuelta 7, con su comando

**Las tres son la misma averia: un puntero de linea desplazado exactamente OCHO
lineas, todas dentro de la seccion `SELLING FAMILY` de `fuentes/smart_who/cap_06.md`.**

| # | donde, en `docs/loop/REPORTE.md` | el reporte cita | el texto vive en | desfase |
|---:|---|---:|---:|---:|
| 1 | **seccion 2.a, fila P5 de la tabla de frontera** | **L73** | **L81** | **-8** |
| 2 | **seccion 2.d, fila 3 de la tabla de puentes** | **L51** | **L59** | **-8** |
| 3 | **seccion 2.d, fila 4 de la tabla de puentes** | **L57** | **L65** | **-8** |

    $ grep -n "bring them to town" fuentes/smart_who/cap_06.md          ->  81
    $ grep -n "During nearly every conversation" fuentes/smart_who/cap_06.md ->  59
    $ grep -n "magnificent name is Tex Chance" fuentes/smart_who/cap_06.md   ->  65
    $ awk '<titulos de seccion>' fuentes/smart_who/cap_06.md
        43: SELLING FAMILY      83: SELLING FREEDOM

**La mas grave es la primera.** La tabla de frontera declara `SELLING FAMILY` en
**L43 a L73**; la seccion corre en realidad **de L43 a L81**. Como consecuencia,
**L75, L77, L79 y L81 no aparecen en ninguna de las diecinueve piezas** de una tabla
que se anuncia como *"Las diecinueve piezas del capitulo, en el orden del libro"*.
**La frontera tiene un hueco de cuatro bloques.** Y la cita que la tabla presenta como
**prueba de `D.27`** para esa pieza esta puesta en la linea equivocada.

### 1.2. Por que ACUMULA, y no lo decido yo hoy

- **Sede:** las tres viven **dentro de una TABLA** de `docs/loop/REPORTE.md`.
  `AUDITOR_FORJA.md` 5.2 dice que la especie REPORTE **acumula si la cifra vive en
  TABLA, CABECERA o CONCLUSION**, y no acumula solo en lista de rutas o prosa de
  acompanamiento.
- **Cosecha 7.B**, *la ruta que promete prueba es cifra*: una cita publicada como
  **evidencia de una comprobacion** cuenta como cifra en su sede.
- **Precedente de esta misma casa:** el ACTA 5 y el ACTA 6 contaron sus caidas de
  REPORTE con este mismo criterio, y ninguna estaba dentro de un discutible marcado.

### 1.3. Y ademas, un remedio escrito roto (cosecha 7.D)

El remedio de la vuelta 5 dice: **toda cita de linea se reabre con `sed -n` antes de
teclearse.** El ACTA 6 lo verifico y lo dio en verde (*unas 40 citas, cero punteros
rotos*). **El reporte de la vuelta 7 afirma en su 1.a que las de esta vuelta estan
reabiertas, y para tres citas eso es falso.** La cosecha 7.D: **romper un remedio
escrito acumula como caida para la parada, sea de quien sea.**

---

## 2. LO QUE **NO** ES LA PARADA, y hace falta decirlo para que decidas bien

**La vuelta 7 es, por lo demas, una vuelta BUENA. Esto no es un extractor
descarrilado.**

- **NINGUN DATO SE MOVIO.** Volque el nodo afectado campo a campo:
  `vender_cambio_trabajo_familia.json` **mina L75** (su paso 7), **L77 y L79**
  (Pillsbury, en el `resumen_teorico`) **y L81 en tres pasos** (4, 5 y 6). **El hueco
  esta en la tabla del reporte, no en el nodo.** Ni un paso inventado, ni una palabra
  perdida. Por eso la especie es REPORTE y **no** CLASE.
- **Los 12 candidatos son correctos.** 44 de 44 de la bandeja ENTRARIAN al correr yo
  el informe, con cero bloqueos, cero caidas y cero choques.
- **Los 8 discutibles que el extractor marco a ciegas: acerto en los OCHO.** Los ocho
  quedan SOSTENIDOS, cada uno con la regla escrita que lo gobierna (ACTA 7, seccion 3).
- **El remedio que encargue en el ACTA 6 FUNCIONO:** doce comparativos con su cociente
  escrito al lado, **los doce exactos**.
- **Las tres guardas estan VERDES en su commit** (`32bef53`), comprobadas por mi sobre
  el arbol limpio: gate verde, barrido verde, **65 pruebas con 0 fallos**.

> **La regla que para el bucle no mide si la vuelta fue buena. Mide si el dictado
> esta suelto, y lleva tres tandas suelto.** Por eso la aplico sin rebajarla, y por
> eso te doy el contexto entero en vez de solo el titular.

---

## 3. EL ESTADO EXACTO, MEDIDO POR MI HOY

| medida | cifra | comando |
|---|---|---|
| **hash** | **`32bef53`** | `git rev-parse HEAD` |
| rama | `extraccion-mundo-11` | `git rev-parse --abbrev-ref HEAD` |
| **fase** | **lote 2 (`smart_who`), vuelta 7 cerrada; 6 de 7 unidades LEIDAS, 5 de 7 MINADAS enteras** | |
| **nodos vivos** | **8** (43 pasos, 4 extremos de arista) | `wc -l dataset/nodos.jsonl` |
| **veredictos** | **2**, los dos del lote 1 | `wc -l bitacora/VEREDICTOS.jsonl` |
| pares mutuos | **0**, el fichero no existe todavia | `ls config/pares_mutuos.jsonl` |
| **candidatos en cuarentena** | **44** (`cuarentena/smart_who/`), con **269 pasos** | |
| informe del lote en seco | **44 revisados, 44 ENTRARIAN, 0 bloquean, 0 caen, 0 chocan** | `python forja.py informe --carpeta cuarentena/smart_who` |
| pares que levantaran al insertar | **59 de 1.892**: 0 similitud, 50 familia, 15 paso, **9 solo senal 3** | `src.aduana.medir`, remedido por mi |
| gate / barrido / pruebas | **VERDE / VERDE / 65 con 0 fallos**, sobre el arbol limpio en `32bef53` | |
| cola sin minar del lote 2 | **8.883 palabras**: 5.034 del Cap. 5, **370 de cuerpo del Cap. 6** y 3.479 de material de cierre de libro | |

**EL ARBOL DE TRABAJO ESTA SUCIO Y NO ES UN ERROR DE NADIE:** el arnes deja
modificados `docs/loop/loop.log`, `ultimo_auditor.json` y `ultimo_extractor.json`
despues del ultimo commit. **Ver el punto 3 del apartado 4.**

---

## 4. LO QUE NECESITO DE TI. **CINCO COSAS, Y SOLO LA PRIMERA DESBLOQUEA EL BUCLE**

### 4.1. **BLOQUEANTE: el reinicio de la racha REPORTE, o su sustituto**

`AUDITOR_FORJA.md` 5.4: **la racha NO se reinicia sola. La reinicia una decision tuya
escrita en `docs/loop/paradas/`, y el acta lo dice citandola.** Un auditor que pone su
propia racha a cero se esta absolviendo, asi que **no la toco**.

**Lo que propongo, y es propuesta y no encargo** (la escalada de mi seccion 1 punto 4
ya no tiene escalon siguiente que encargar; ir mas alla seria doctrina nueva y por
tanto parada):

> **Que el remedio para el dictado suelto sea, como los dos que han funcionado, un
> ACTO MECANICO y no una promesa: que ninguna cita de linea se teclee en una TABLA del
> reporte sin que la salida literal de `sed -n '<n>p'` o `grep -n` quede pegada en el
> propio reporte, aunque sea en una columna estrecha.** Los dos remedios que
> funcionaron en esta casa (imprimir las claves antes de contar; escribir el cociente
> antes del comparativo) **funcionan porque obligan a teclear algo**. Los dos que se
> rompieron eran intenciones.

**Y esto NO pide maquinaria nueva**, que la moratoria (cosecha 7.F) prohibe encargar.

### 4.2. La autorizacion de insercion. **SEPTIMA tanda con cero SANO**

    veredictos SANO de la tanda 7 : 0      (y de las tandas 1 a 6: 0)
    candidatos esperando           : 44

**El error de dejar pasar sigue sin tasa y sin banda** (manual seccion 6), y la
muestra pineada de mi seccion 7 lleva siete actas sin poder medirse **porque no hay
poblacion**, no porque nadie la mire. La causa es `MODO_INSERCION=cuarentena` y
`D.26`: **la insercion es autorizacion tuya, no un default.**

**Y un dato medido esta vuelta que necesitas ANTES de fijar el orden de insercion:**
la senal 3 **no es simetrica**, y hay ya un par en la bandeja donde eso decide si el
par **llega a leerse**:

    celebrar_aceptacion_primer_dia -> sostener_contacto_oferta_aceptacion : 0.613  LEVANTA
    sostener_contacto_oferta_aceptacion -> celebrar_aceptacion_primer_dia : 0.587  NO levanta

**Si `celebrar` entra despues, bloquea y pide veredicto; si entra antes, no lo pide.**
Es `EXTRACTOR.md` 12.3 con un ejemplar propio. **Ni el extractor ni yo movemos
umbrales, y ninguno de los dos fija el orden de insercion.**

### 4.3. El artefacto del arnes: **ya no solo tumba el hook, tumba una prueba**

**Tercera vuelta seguida, y primera vez sobre `ultimo_extractor.json`.** El arnes
vuelca el texto del turno en el artefacto **despues** del ultimo commit, con guiones
largos dentro:

    $ git show HEAD:docs/loop/ultimo_extractor.json | wc -c   ->  0
    $ wc -c docs/loop/ultimo_extractor.json                   ->  4468
    $ python forja.py guiones
      BARRIDO DE GUIONES EN ROJO: 2 hallazgo(s)
        docs/loop/ultimo_extractor.json linea 1 columna 1562: guion largo (U+2014)
        docs/loop/ultimo_extractor.json linea 1 columna 1891: guion largo (U+2014)
    $ python tests/test_aceptacion.py
      FAIL: test_e_guion_largo_rompe_el_hook
      AssertionError: 1 != 0 : el repo ha de estar limpio antes de ensuciarlo
      total: 65 pruebas, 1 fallos, 0 errores

**Sobre el arbol limpio en `32bef53` las tres guardas dan verde y las 65 pruebas pasan
con 0 fallos**, asi que **no es caida de nadie y no la cuento**. Pero **una prueba de
aceptacion que se pone roja por un fichero que el propio arnes escribe** deja al
siguiente turno arrancando en rojo, y **la decision de tocar el arnes es tuya**: yo no
encargo maquinaria (cosecha 7.F) y el artefacto no es sede mia.

### 4.4. En que racha cae un remedio roto **del auditor**

**Heredada del ACTA 5, y ahora con TRES ejemplares, los tres mios.** `AUDITOR_FORJA.md`
5.5 dice que **acumula** y **no dice donde**. No me la invento: seria doctrina nueva.

**Y hay un dato nuevo que te sirve para decidirlo:** el ACTA 6 sustituyo mi promesa
por un artefacto (**el bloque `LO QUE HE LEIDO HASTA AQUI`, obligatorio antes de
adjudicar**). **Lo escribi, es lo primero del ACTA 7, y NO evito la contaminacion:
solo la hizo visible en la primera pagina en vez de en la cuarta.** **El artefacto
documenta, no impide.** Siete actas seguidas con caida propia, y la mitad 2 rota tres
veces.

### 4.5. Las dos piezas de las reglas de id, que solo tu metes

1. **`who` en `INGLES_CON_EQUIVALENTE`** (heredada del ACTA 6).
2. **La A de *jugador A***. La Regla 3 tiene `a` en `PALABRAS_VACIAS`, asi que
   `vender_puesto_jugador` pierde la A del id; **la A viaja entera en `titulo` y en
   `denominaciones`**, y el precedente `seleccionar_jugador_cuatro_entrevistas` ya
   paso igual. **El id esta bien escrito con la regla vigente**, y lo sostuve. Si
   quieres que la A sobreviva en los ids, **eso es una excepcion escrita y es tuya**,
   por correccion declarada con fecha.

---

## 5. COMO SE RETOMA

1. **Escribe tu decision en `docs/loop/paradas/`**, con fecha y motivo, al menos sobre
   el punto 4.1. Sin eso, **la racha REPORTE sigue en 3 de 3** y cualquier vuelta nueva
   nace ya parada.
2. **Si tocas el arnes** (punto 4.3), hazlo antes de reencender: si no, la primera
   vuelta arranca con una prueba en rojo que no es suya.
3. **Reencender no exige insertar nada.** `D.32` es explicito: **un lote sin insertar
   no bloquea el siguiente.** La extraccion puede continuar por donde quedo aunque no
   autorices todavia el punto 4.2.
4. **Donde continua el trabajo, medido y no estimado:**
   - la **cola del Cap. 5**: `cap_06.md` **L247 a L455**, 5.034 palabras, 105 bloques,
     con **una serie numerada de diez y otra de cuatro** dentro (16 nodos con sus dos
     cabezas: **ya pasa por si sola el techo de quince**);
   - el **Cap. 6**: **`cap_07.md` L9 a L41, 370 palabras**, no 3.849. Y ojo al borde:
     `cap_06.md` L455 y `cap_07.md` L9 **son prosa continua partida en dos ficheros**,
     asi que **la etiqueta `unidad` de la cabecera del recorte no coincide ahi con el
     capitulo**. El extractor lo midio, lo declaro y **no movio la etiqueta**, que es
     lo correcto; **cambiar el recorte es decision tuya.**
   - el **material de cierre de libro**: `cap_07.md` **L43 a L429**, 3.479 palabras.
     **Nadie ha juzgado todavia si es minable.**
5. **El volumen del lote siguiente**, cuando toque: `PASOS INVENTADOS POR CAPITULO` del
   Cap. 5 sale al **5,00 por ciento** (subio respecto al 3,09 del Cap. 4, cociente
   1,618) **pero no mueve el peor del lote 2**, que sigue siendo el Cap. 3 con 7,55, y
   esta muy por debajo del 36,11 de la linea base. **Firmo el denominador de 72 pasos
   finales, que conte yo; NO firmo el numerador de 4 puentes ni el denominador de 80,
   porque los 8 pasos retirados no viven en ningun fichero del repo.**

---

## 6. LO QUE ESTA PARADA **NO** HACE

- **NO funde ramas y NO crea remotos.** `extraccion-mundo-11` se queda donde esta.
- **NO pide el merge**, porque **esta no es la parada feliz**: la campana no esta
  consumada, el lote 2 esta a 6 de 7 unidades y quedan nueve lotes.
- **NO reinicia ninguna racha, ni la del extractor ni la mia.**
- **NO deja encargo escrito.** `docs/loop/PROMPT_SIGUIENTE.md` queda **vacio**: un
  encargo escrito junto a una parada es una parada que alguien puede saltarse.
