
---

## O.4. TAREA 3: LAS TRES ARISTAS `D.37` DE `L173`. **CERRADA CON UN HECHO NUEVO, Y EL HECHO ES DEL INSTRUMENTO**

### O.4.a. LA SERIE, LEIDA Y CERRADA: LA CUENTA ESTA ESCRITA Y LAS TRES PARTES EXISTEN

    $ sed -n '173p' fuentes/scott_radical_candor/cap_10.md
      Firing people is hard, and it ought to be hard. But if you do three things, you can
      make it far, far easier on the person you are firing - as well as on yourself and
      your team.
    $ sed -n '175p;181p;189p;197p' fuentes/scott_radical_candor/cap_10.md
      175: Don't wait too long
      181: Don't make the decision unilaterally
      189: Give a damn
      197: Follow up

**`L173` ESCRIBE LA CUENTA (`three things`), asi que esto es `D.37` y no `D.29`**, que es
precisamente lo que `D.37` distingue (`EXTRACTOR.md` 15.6: *la cuenta es condicion, no un adorno
del ejemplo*). **Y las tres partes existen como nodos desde hoy.**

**EL PASO DE LA MADRE QUE ENUMERA LA SERIE ES EL 11, Y VA PEGADO** porque es lo que hace las
tres aristas verificables:

    $ python (paso 11 de facilitar_despido_tres_cosas, leido de su fichero)
      Y haz las tres cosas que el texto dice que, hechas, lo vuelven mucho mucho mas facil
      para la persona a la que despides, y tambien para ti misma y para tu equipo: no
      esperes demasiado, no tomes la decision unilateralmente, y que te importe de verdad
      la persona.

**LAS TRES ARISTAS, ENTERAS, CON SU MADRE, SU HIJO, SU PASO Y SU RAZON:**

| # | madre | hijo | `--paso` | la razon escrita |
|---:|---|---|---:|---|
| **1** | `facilitar_despido_tres_cosas` | `admitir_pronto_mal_desempenio_cuatro_razones` | **11** | el paso 11 de la madre enumera las tres cosas y la primera es *no esperes demasiado*; el hijo la despliega en **9** pasos que la cabeza no tiene, con las cuatro razones que `L179` numera una a una (*One, Two, Three, Four*) y con el ejercicio de las casillas de `L177` |
| **2** | `facilitar_despido_tres_cosas` | `calibrar_decision_despido_documentarla` | **11** | el mismo paso 11 pone la segunda, *no tomes la decision unilateralmente*; el hijo la despliega en **13** pasos, con los tres sitios donde se pide ayuda de `L183` y la regla de `L185` que la cabeza no tiene: no pidas consejo, consigue que editen lo que escribes |
| **3** | `facilitar_despido_tres_cosas` | `sopesar_consejo_legal_despedir_humildad` | **11** | el mismo paso 11 pone la tercera, *que te importe de verdad la persona*; el hijo la despliega en **8** pasos, con la pregunta operativa de `L193` que la cabeza no tiene: cual es el riesgo de NO hacerlo |

**Y LA CODA QUEDA FUERA DE LA SERIE, con la letra de la `ACTA 20` `4.5`:**
`contactar_despedido_mes_despues` (`P28`, `L197`, *Follow up*) **NO recibe arista de serie**,
porque **la cuenta de `L173` es de TRES y esta es la cuarta**, y porque su par es otro: su
condicion de activacion es *hace un mes que despediste* y su entregable es *el contacto hecho*.
**No es una omision: es la adjudicacion aplicada.**

### O.4.b. **EL HECHO NUEVO: EL INSTRUMENTO DE `D.37` NO PUEDE CABLEAR UNA ARISTA CUYOS DOS EXTREMOS VIVEN EN CUARENTENA. MEDIDO, NO SUPUESTO** (`EXTRACTOR.md` 5)

*El encargo dice **cableadas en la misma vuelta en que se escriban sus partes**. Lo intente con
el instrumento, que es lo que `EXTRACTOR.md` 5 me manda hacer antes de afirmar nada sobre lo que
se puede o no se puede. **Esta es la salida literal.***

    $ python forja.py arista --madre facilitar_despido_tres_cosas \
        --hijo admitir_pronto_mal_desempenio_cuatro_razones --paso 11 \
        --razon "el paso 11 de la madre enumera las tres cosas que facilitan un despido y
                 la primera es no esperar demasiado; el hijo la despliega en 9 pasos que la
                 cabeza no tiene, con las cuatro razones numeradas por el texto en L179"

      DECLARACION DE ARISTA POR LECTURA (D.37)
        madre: facilitar_despido_tres_cosas
        hijo : admitir_pronto_mal_desempenio_cuatro_razones

      RECHAZADO: la madre 'facilitar_despido_tres_cosas' no vive en el grafo
        Una arista se cablea contra ids que YA existen.
        Si todavia esta en cuarentena, entra por la aduana y declara la arista en el acto
        de insertarla.

**GUARDADA EN `.aduana_v21/arista_intento_1.txt`, y `NADA SE ESCRIBIO`**: el modulo rechaza
antes de tocar `dataset/` ni `bitacora/`, y lo comprueban las cifras del cierre (`O.6`), que
cierran donde abrieron.

> ### **Y EL INSTRUMENTO NO ESTA ROTO: DICE LA MISMA COSA QUE MI MANUAL, CON OTRAS PALABRAS.**
>
> **`EXTRACTOR.md` 15.6, literal:** *DESDE AHORA DECLARAS ESAS ARISTAS EN LA MISMA VUELTA EN QUE
> **INSERTAS** LAS PARTES.*
>
> **El rechazo del instrumento, literal:** *Si todavia esta en cuarentena, entra por la aduana y
> declara la arista **en el acto de insertarla**.*
>
> **Las dos frases son la misma frase.** Y el propio encargo cita la regla bien en su
> parentesis (*el extractor declara esas aristas en la misma vuelta en que **inserta** las
> partes*) mientras su negrita dice *se escriban*. **Es la negrita la que se sale de la regla,
> no yo.**

**POR QUE ESTO NO ES PARADA, Y LO RAZONO CON LA LETRA DELANTE** (`EXTRACTOR.md` 7: se para solo
si algo contradice una regla vigente o una cifra publicada):

1. **`D.39` no deja insertar un lote ABIERTO**, y el lote 4 lo esta (`O.0`, medido).
2. **El propio encargo lo dice**: su seccion LO QUE NO HACE ESTA VUELTA abre con *NO INSERTA
   NADA*.
3. **La decision 4 del fundador lo dice**: *`cap_10` ENTERO ... **sin insercion porque el lote
   sigue abierto***.
4. Asi que **no hay dos reglas en conflicto**: hay una negrita del encargo que no cabe, y la
   regla que manda es la de mi manual. **Lo declaro, no lo resuelvo copiando, y no lo arreglo
   yo** (`EXTRACTOR.md` 14: propongo en mi reporte).

> ### **LO QUE SI DEJO HECHO, QUE ES TODO LO QUE CABE HACER HOY: LAS TRES ARISTAS ESTAN ESCRITAS ENTERAS ARRIBA, CON SU MADRE, SU HIJO, SU `--paso 11` Y SU RAZON. EL DIA QUE EL LOTE CIERRE SON TRES COMANDOS, NO TRES LECTURAS.**
> **Y NO ENGROSAN LA CUENTA DE LAS DOCE COLAS `D.29`**, porque no son `D.29`: son `D.37`, con la
> cuenta escrita en `L173`. Van en su propia fila de `O.6.4`.

---

## O.5. TAREA 4: EL PAR DE LA LUPA, POR LECTURA. **CERRADA, Y TAMBIEN CON UN HECHO NUEVO MEDIDO**

### O.5.a. **EL VEREDICTO, ESCRITO CON SU RAZON: `CONTINUA` CON ARISTA**

*Decision 3 del fundador del 12 sep 2026, segunda mitad, y `ACTA 20` `4.3`. El veredicto viene
adjudicado y yo lo escribo con su razon, que es lo que el encargo pide.*

| | |
|---|---|
| **madre** | `reconocer_recompensar_gente_estable`, de `cap_06`, **12 pasos**, en la bandeja |
| **hijo** | `reconocer_excelencia_trayectoria_gradual`, de `cap_10` `L239` a `L251`, **13 pasos**, escrito hoy |
| **veredicto** | **`CONTINUA` CON ARISTA. NO es `REPITE`** |
| **`--paso` de la madre** | **2** |

    $ python (paso 2 de reconocer_recompensar_gente_estable, leido de su fichero)
      Reconoce su aportacion por otras vias, y el texto nombra varias una a una: un bono o
      una subida; si les gusta hablar en publico, que presenten en la reunion general o en
      otros actos grandes; si les gusta ensenar, que ayuden a la gente nueva a aprender su
      papel mas rapido; y si son timidos, asegurate de que tu y otros del equipo les dais
      las gracias en privado por el trabajo que hacen.

**LA RAZON, ESCRITA Y NO PROMETIDA:** el paso 2 de la madre **nombra las vias en una linea** y el
hijo **despliega dos de ellas en trece pasos que la madre no tiene**: el agradecimiento con su
distincion escrita frente al elogio (`L243`: *A thank-you goes beyond praise*), y el papel de
experto de referencia con **su plazo de preparacion** (`L247`: *Give them a couple of months to
develop a class*) y **su condicion de honor y no de castigo**, con su salida para quien no quiere
ensenar. **Eso es exactamente lo que la vara de `CONTINUA` contra `REPITE` pide: el hijo añade
procedimiento propio, no vocabulario.**

**Y POR QUE EL CORTE EN DOS ES LO QUE HACE EL PAR LEGIBLE, que es la razon que la `ACTA 20` `4.3`
escribio:** contra **UN** nodo hijo la lectura es `CONTINUA` con arista; contra **cuatro** habria
que adjudicar cuatro pares y tres de ellos con dos actos cada uno.

### O.5.b. **EL HECHO NUEVO: LA ADUANA **NO** LO LEVANTA, NI CON LA POBLACION DE `D.38.5`. LAS TRES SEÑALES ESTAN POR DEBAJO DE SU UMBRAL**

*El encargo lo dice asi: **si NO te lo levanta, eso es un hecho nuevo y lo traes con tu medida**
en vez de resolverlo copiando. Lo traigo con la medida del mismo medidor que usa el informe
(`src.aduana.medir`) y con los umbrales cargados por el mismo cargador.*

    $ python .t1_v21/par_lupa.py
    umbrales de esta corrida: {"umbral_familia_id": 0.3, "umbral_paso_contra_nodo": 0.6,
                               "umbral_similitud_texto": 0.35, ...}

| candidato | vecino | similitud_texto | familia_id | paso_contra_nodo | la levanta alguna? |
|---|---|---:|---:|---:|---|
| `reconocer_excelencia_trayectoria_gradual` | `reconocer_recompensar_gente_estable` | 0.257 | 0.143 | 0.472 | **NO, ninguna** |

    detalle_paso : paso 10 del candidato contra paso 9 de reconocer_recompensar_gente_estable

**Y LO CONFIRMA SU PROPIO INFORME DE LA ADUANA, que es otro instrumento y no el mismo:**

    $ grep -A3 "^\[" .aduana_v21/final/reconocer_excelencia_trayectoria_gradual.txt
      (el vecino `reconocer_recompensar_gente_estable` NO aparece en su lista)

> ### **LAS TRES POR DEBAJO, Y NO POR POCO EN DOS DE LAS TRES: `0,257` contra `0,35`; `0,143` contra `0,30`; `0,472` contra `0,60`.**
>
> **LO QUE ESTO CORRIGE DE MI ENCARGO, dicho sin rodeos:** su TAREA 4 decia *Y AHORA LA ADUANA SI
> LO VA A LEVANTAR SOLA (`D.38.5`): los dos extremos viven en cuarentena y antes eso lo hacia
> invisible.* **La primera mitad es falsa y la segunda es cierta.** `D.38.5` cambio **la
> POBLACION**, no los **UMBRALES**: ahora el par se **mide**, y antes ni se medía. Pero medirlo
> no basta para levantarlo, porque **sus tres señales no llegan.**
>
> ### **Y ESTO NO ES UNA SORPRESA: ES `D.19` OTRA VEZ, Y AHORA CON UN EJEMPLAR QUE EL FUNDADOR ELIGIO A MANO.**
> `EXTRACTOR.md` 11, literal: *ninguna señal separa un par de jerarquia declarada de un par al
> azar. **LA JERARQUIA LA BUSCA LA LECTURA, NO LA SEÑAL.*** **El par que la casa considera el mas
> cerrado del lote entero da `0,257` de similitud**, que esta en plena banda media, la que
> `EXTRACTOR.md` 11 llama **ruido** por su nombre. **Si alguien esperaba que la poblacion nueva
> cazara jerarquias, esta fila dice que no.**
>
> **NO PIDO MOVER NINGUN UMBRAL** (`EXTRACTOR.md` 11: ninguna vuelta mueve un umbral, y un umbral
> se juzga contra su cola y no contra un par). Lo que traigo es **la fila medida**, y la propuesta
> que sale de ella va en `O.6` sin que yo la adjudique.

### O.5.c. **DONDE QUEDA ESCRITO EL VEREDICTO, Y POR QUE NO EN SU SEDE**

*`EXTRACTOR.md` 14: `bitacora/` la escribe **la aduana**, por `forja.py insertar`. **Nunca a
mano.** Y hoy no se inserta.*

    $ wc -l < bitacora/VEREDICTOS.jsonl
      148          (148 al abrir la vuelta 21 y 148 al cerrarla)

**El veredicto de `O.5.a` esta escrito entero aqui y dentro del propio `resumen_teorico` del
candidato**, con su madre, su paso citado y su razon. **No lo meto a mano en la bitacora**: eso
seria escribir en la sede de la aduana, que es la unica prohibicion que esta casa llama *la que
no admite excepcion*. **Es el veredicto numero 27 que vive solo en `REPORTE.md`**, y `D.39` dice
que los 26 anteriores se resuelven de golpe el dia que el lote entre.
