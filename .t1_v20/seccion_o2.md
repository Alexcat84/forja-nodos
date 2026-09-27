
---

## O.2. TAREA 1, **BLOQUEANTE**: LOS REGISTROS, Y EL REMEDIO DE MI RACHA `REPORTE`. **CERRADA**

### O.2.a. LA `ACTA 19`, LEIDA ENTERA Y SITUADA CON SU LINEA

*`D.35`: la cita se pega, no se promete. **Y desde esta vuelta, la ruta tambien** (`O.2.d`).*

    $ grep -n "^# ACTA 19" docs/loop/ACTA_AUDITOR.md
      17299:# ACTA 19. VUELTA 19, lote 4 (scott_radical_candor), cap_09: las dos lecturas
             ciegas que coinciden en las 213 lineas, el capitulo partido que la regla no
             queria, y una ruta de prueba que promete mas de lo que guarda
    $ wc -l docs/loop/ACTA_AUDITOR.md
      18132 docs/loop/ACTA_AUDITOR.md
    $ awk 'NR>=17299' docs/loop/ACTA_AUDITOR.md | wc -l
      834                  <- las 834 lineas que van de L17299 al final, leidas enteras

**LEIDA DE `L17299` A `L18132`, que es lo que el encargo pide por su numero de linea.** Sus
doce secciones (`0` a `11`) y sus veintitres subsecciones.

### O.2.b. LAS CINCO ADJUDICACIONES, RECOGIDAS **SIN REABRIRLAS** (`1.a` del encargo)

*`EXTRACTOR.md` 5 me obliga a traer un hecho nuevo con su medida si lo encuentro, y a no
resolverlo copiando. **Encontre uno y esta en la fila 5.** Las otras cuatro las recojo y no
las toco.*

| # | que se adjudico | **como la recojo** |
|---:|---|---|
| **1** | `L317`, `four rules of thumb` contra cinco rotulos | **RECOGIDA Y APLICADA HOY, no solo anotada.** La serie de `P23` es de **CUATRO** (`L319`, `L321`, `L323`, `L325`) y `L327` es coda, **un paso mas del mismo nodo**. Es lo que escribe `O.3` en el candidato de `P23`, y **mi hipotesis de la vuelta 19 (fundir `L323` con `L325`) queda retirada por la suya**, que deja la serie en cuatro sin tocar ninguna regla |
| **2** | `P4` como UN nodo de 20 pasos | **RECOGIDA. No lo parto y no lo vuelvo a mirar.** Su reserva medida (`108,9` palabras por paso contra `60,3` de media) queda **para la auditoria ciega del cierre del lote**, no para esta vuelta |
| **3** | `12.4` punto 4 y el cierre en 15 | **RECOGIDA, y es la que gobierna toda mi vuelta.** Un capitulo que pasa del techo **se escribe entero**; el techo que se estira es el de candidatos y el que no se estira es el de capitulos. **No la traigo otra vez** (`1.f`) y **no la vuelvo a subir como discutible** |
| **4** | la frontera de `cap_09`: **30 piezas, 20 dan nodo, 10 no** | **RECOGIDA. Es la cifra de la casa y no la reabro.** Lo unico que publico de ella es que mis cinco de hoy son exactamente las cinco que faltaban (`O.3.b`) |
| **5** | el par `evitar_personalizar_guia_aceptar_personal` contra `manejar_enfado_persona_desafiada`, `paso_contra_nodo 0.867`, **`CONTINUA`** | **RECOGIDA, y con un hecho nuevo medido al lado, que es lo que `EXTRACTOR.md` 5 me obliga a hacer en vez de copiar. Ver `O.2.c`.** La arista queda anotada como **la numero 11** de mi cola `D.29` (`O.6.4`) |

### O.2.c. **EL HECHO NUEVO DE LA FILA 5, TRAIDO CON SU MEDIDA Y NO RESUELTO COPIANDO**

*No reabro la clase `CONTINUA`: la acepto. **Lo que traigo es donde vive el otro extremo**, y
lo traigo porque el acta lo llama `bandeja` sin decir cual, y la diferencia decide si la
arista se puede escribir algun dia y con que lote.*

    $ ls cuarentena/*/manejar_enfado_persona_desafiada.json
      cuarentena/zhuo_manager/manejar_enfado_persona_desafiada.json
    $ python (la clave de fuentes de ese fichero)
      zhuo_manager

> ### **EL PAR CRUZA DE LIBRO: `evitar_personalizar_guia_aceptar_personal` es del lote 4 (`scott_radical_candor`) y `manejar_enfado_persona_desafiada` es del lote de `zhuo_manager`.**
>
> **POR QUE IMPORTA Y NO ES UNA CURIOSIDAD:** mi cola `D.29` numero **2** y numero **4** son
> las dos que cruzan de libro, y de las dos dice la misma linea remedida al cierre de la
> vuelta 19: **`0` aristas cruzan de libro sobre las `79` del grafo.** **La numero 11 es la
> tercera de esa misma especie**, y la especie entera **sigue sin estrenarse en esta casa.**
> La anoto asi en `O.6.4` en vez de anotarla como una cola cualquiera.
>
> **Y NO ES CONTRADICCION CON EL ACTA:** el acta dice *los dos viven en la bandeja*, y es
> cierto, **las dos bandejas son bandejas**. Lo que anado es **cual**, que es el dato que
> decide si la arista espera al cierre del lote 4 o al de los dos.

### O.2.d. **EL REMEDIO DE MI RACHA `REPORTE`, QUE ES LO BLOQUEANTE DE ESTA TAREA**

*`ACTA 19` `4.4` y `8`: **mi racha `REPORTE` esta en 2 de 3 y la siguiente para el bucle.**
La caida fue publicar `la salida literal de los 40 informes que este reporte cita` cuando el
fichero guarda **35 de 41**. **La acepto entera y sin matices: la corri yo hoy y el acta
tiene razon al digito.***

    $ grep -cE "\[(ENTRARIA|CAERIA|BLOQUEARIA)\]" .aduana_v19/informes.txt
      35
    $ wc -l < .aduana_v19/informes.txt
      40
    $ grep -oE "\[(ENTRARIA|CAERIA|BLOQUEARIA)\]" .aduana_v19/informes.txt | sort | uniq -c
      5 [BLOQUEARIA]
      1 [CAERIA]
      29 [ENTRARIA]

**`40` ES EL NUMERO DE LINEAS Y `35` EL DE INFORMES, y los seis que faltan son los que el
acta nombra.** Mi `N.6.7` decia `40` y mi `N.6.8` decia `41`: **el reporte se contradecia a
si mismo y el numero bueno es `41`.**

> ### **EL REMEDIO, ADOPTADO DESDE ESTA LINEA Y APLICADO EN TODA LA VUELTA 20: TODA RUTA QUE PUBLIQUE COMO PRUEBA LLEVA, EN LA MISMA FRASE, EL COMANDO QUE LA CUENTA Y SU SALIDA.**
>
> Y su segunda mitad, que es la que de verdad muerde: **si la ruta guarda MENOS de lo que mi
> reporte cita, lo digo en la misma linea y nombro los que faltan.**
>
> **POR QUE ESTE REMEDIO SI PUEDE AGUANTAR, con la doctrina de la casa delante** (`D.35`:
> *un remedio que se cumple acordandose no es un remedio*; *los dos remedios que han
> funcionado obligan a teclear algo y los dos que se rompieron eran intenciones*): **este
> obliga a teclear un `grep -c` y su salida.** No es una intencion, es un par de lineas que
> o estan pegadas o no estan.
>
> **Y NO ES MAQUINARIA** (moratoria, `EXTRACTOR.md` 13): es un `grep -c` al lado de una ruta,
> y el encargo lo dice por su nombre: *no es maquinaria y no la pidas*.

**LA CUENTA DE MI PROPIO CUMPLIMIENTO VA AL CIERRE, EN `O.6.7`**, con la lista de todas las
rutas que este reporte publica y su `grep -c` pegado. **Lo digo aqui para que se pueda
comprobar que no me lo salte: la seccion existe y tiene su numero desde ahora.**

**Y UNA COSA QUE EL ACTA ME RECONOCE Y NO ME LA APROPIO SIN SU CIFRA:** mi fichero
`.aduana_v19/informes.txt` **ya era honesto por dentro**, y esta es su linea:

    $ sed -n '2p' .aduana_v19/informes.txt
      # TAREA 2.b, los 24 candidatos de bandeja tocados (3 corridos aparte, 21 en tanda):
    $ sed -n '2,26p' .aduana_v19/informes.txt | grep -cE "\[(ENTRARIA|CAERIA|BLOQUEARIA)\]"
      21

**El fichero decia `21 en tanda` y mi frase de reporte decia `40 informes`. Lo que fallo fue
la frase, no el fichero**, y por eso el remedio es una regla de escritura y no un instrumento.

### O.2.e. LA CORRECCION DECLARADA DEL AUDITOR, COMPROBADA EN MI PROPIO ARBOL Y NO DE OIDAS

*`1.c` del encargo. **El fichero sellado no se toca**, y no lo toco: `APERTURA_CIEGA.md` `2.3`
se queda como esta y la correccion vive en su `7.1`. **Lo que si hago es remedirla yo**, que
es lo que `EXTRACTOR.md` 5 pide de una cifra que voy a repetir.*

**Y APLICO SU PROPIA ORDEN A A MI TABLA** (`ACTA 19` `7.4`: *toda tabla de reparto lleva su
fila de residuo, y la fila de residuo tiene que ser cero o tener nombres*). **Es una orden
que se escribio para el auditor, y la adopto igual porque la averia es de las dos manos:**

    $ cat .t1_v20/reparto.py      (el rotulo y el codigo dicen lo mismo: primer 'cap_NN'
                                   EN EL TEXTO del resumen_teorico, no una cabecera concreta)
    $ python .t1_v20/reparto.py
      cap_01:   1 cand,    9 pasos
      cap_03:   1 cand,    7 pasos
      cap_04:   6 cand,   48 pasos
      cap_05:   8 cand,   76 pasos
      cap_06:  10 cand,  117 pasos
      cap_07:  25 cand,  225 pasos
      cap_08:  12 cand,  102 pasos
      cap_09:  15 cand,  177 pasos
      TOTAL:  78 cand,  761 pasos
      FILA DE RESIDUO 'SIN' -> 0 ids: []

> **SU CORRECCION ES CIERTA Y LA FIRMO: `cap_04` son 6 candidatos y 48 pasos, y la fila de
> residuo `SIN` es 0 con su lista vacia pegada al lado.** La fila `cap_04: 5` y `SIN: 1` de
> su apertura sellada es falsa, **y el candidato en disputa,
> `invitar_desafio_reciproco_equipo`, declara su capitulo en su propio `resumen_teorico`.**
>
> **Y DIGO POR QUE SU INSTRUMENTO FALLO Y EL MIO NO, porque el merito no es mio:** el suyo
> buscaba la cabecera `UNIDAD DE ORIGEN:`, que es la que **yo** puse en 24 candidatos en la
> vuelta 19 y que este no lleva. **El mio busca `cap_NN` en el texto del resumen, que es mas
> ancho.** No es mejor mano: es que **mi rotulo prometia lo que mi codigo hacia**, que es
> exactamente su ORDEN B.

### O.2.f. **LA CIFRA MIA QUE EL AUDITOR NO PUDO FIRMAR, Y LO QUE HAGO CON ELLA**

*`1.e` del encargo. La fila de `N.6.8`: **de los 25 corregidos, 20 `ENTRARIAN` y 5
`BLOQUEARIAN`**. El acta la cita como mia y la deja **a verificar, sin acusacion ninguna**,
porque el informe de lote sobre los 78 no cabe en un turno (`4m10.739s` por candidato en su
maquina).*

**LO QUE EL FICHERO SI PRUEBA, CONTADO HOY:**

    $ sed -n '2,26p' .aduana_v19/informes.txt | grep -oE "\[(ENTRARIA|CAERIA|BLOQUEARIA)\]" | sort | uniq -c
      5 [BLOQUEARIA]
      16 [ENTRARIA]

**`16` mas `5` son los `21` en tanda, y los `5 BLOQUEARIA` de mi cifra estan probados al
digito.** Lo que **no** esta en el fichero son los **4** que completan los 25 (los 3 corridos
aparte mas el de la TAREA 2.a), **y los cuatro son los que mi cifra cuenta como `ENTRARIA`
para llegar a 20.** `16 + 4 = 20`.

> **ASI QUE LA DIGO COMO ES, QUE ES LO QUE EL REMEDIO DE `O.2.d` ME OBLIGA A HACER: de los 25,
> `21` estan probados en la ruta que publico (5 `BLOQUEARIA` y 16 `ENTRARIA`) y `4` NO, y son
> estos cuatro:** los 3 que corri aparte mas `integrar_trabajo_vida_mejor_version` de la
> TAREA 2.a. **Mi cifra `20 / 5` es correcta solo si esos cuatro entraron, y la ruta no lo
> guarda.** **No la vuelvo a publicar como probada hasta que lo este.**

**Y LA OFERTA DEL ACTA LA TOMO EN LA PARTE QUE CABE:** el informe de lote sobre los 78 son
unas cinco horas y no cabe en mi turno tampoco. **Lo que si hago, y va en `O.3.d` con su
salida entera pegada, es el informe de los cinco de hoy uno por uno**, y **al cierre, en
`O.6.8`, el recuento de los 20 de `cap_09` con lo que de cada uno esta probado en ruta y lo
que no.** Es la mitad que cabe, y la digo como mitad.

### O.2.g. LO QUE **NO** HAGO EN ESTA TAREA, PORQUE EL ENCARGO LO PROHIBE (`1.f`)

| lo prohibido | lo cumplo asi |
|---|---|
| **no reabrir la frontera de 30** | no la republico entera. `O.3.b` publica **una linea** con la cuenta de las cinco que faltaban, que es lo que el encargo autoriza |
| **no reabrir `P4`** | no lo miro, no lo parto, no lo mido. Su reserva queda para el cierre del lote |
| **no subir otra vez la tension de `12.4`** | **no aparece en mis discutibles de `O.5` y no la propongo en `O.6`.** Esta adjudicada y la obedezco: hoy `cap_09` se escribe **entero** |
| **no escribir `PARA_ALEXIS.md`** | `EXTRACTOR.md` 14. No lo toco |

**LA TAREA 1 QUEDA CERRADA.** Y con ella se desbloquea el resto de la vuelta.
