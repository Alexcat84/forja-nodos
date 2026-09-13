
### O.6.5.a. LOS SEIS PARES DISTINTOS QUE LA ADUANA LEVANTO, CON MI VEREDICTO Y SU RAZON

*Seis pares distintos en **siete** filas de `BLOQUEARIA` (dos pares aparecen dos veces, una por
cada extremo, que es como el informe de uno en uno los ve). **Cinco de los seis son entre
candidatos de `cap_10`**, y eso es `D.38.5` funcionando: hasta ayer ni se median.*

| par | señal que lo levanto | **mi veredicto, con los dos ficheros abiertos** |
|---|---|---|
| `admitir_pronto_mal_desempenio_cuatro_razones` contra `sopesar_consejo_legal_despedir_humildad` | `similitud_texto` **0,374** | **`SANO`, y con regla escrita:** son **dos partes HERMANAS de la misma serie `D.37`** de `L173`, la primera y la tercera. `EXTRACTOR.md` 15.6 lo dice con estas palabras: *una cabeza de seis vias y un vecino que no es ninguna de las seis **son hermanos, y su veredicto es `SANO`***. Comparten la cabeza y **ni un acto**: uno admite el bajo desempenio pronto, el otro sopesa el consejo legal. **La arista que les toca es la de cada uno con su cabeza, y esas son las `D.37` de `O.4`** |
| `calibrar_decision_despido_documentarla` contra `sopesar_consejo_legal_despedir_humildad` | `similitud_texto` **0,367** | **`SANO`.** Hermanas tambien: la segunda y la tercera de la misma serie. **Y aqui la frontera es fina y la digo:** el paso 1 del tercero (*no te quedes demasiado atrapada en el consejo de recursos humanos y del abogado*) **responde** al paso 9 del segundo (*consigue que editen lo que escribes*), y el libro lo escribe asi a proposito: `L191` abre con *Don't get too caught up in all the HR/legal advice, **though***. **Ese `though` es la prueba de que son dos actos y no uno** |
| `trazar_plan_dieciocho_meses_aprendizaje` contra `calibrar_decision_despido_documentarla` | `similitud_texto` **0,371** | **`SANO`, y es el par mas raro de los seis.** Un plan de aprendizaje de dieciocho meses contra la documentacion de un despido. **Comparten vocabulario de oficina y nada mas**: el `detalle_paso` apunta al paso 12 de cada uno, y uno dice *asegurate de que tienes dentro algunos elementos de accion* y el otro *asegurate de que alguien que ya lo ha hecho antes los edita*. **El molde `asegurate de que` es lo que la señal 1 vio.** Es el ejemplar de libro de la banda media como ruido (`EXTRACTOR.md` 11) |
| `admitir_pronto_mal_desempenio_cuatro_razones` contra `trazar_plan_dieciocho_meses_aprendizaje` | `similitud_texto` **0,356** | **`SANO`**, por lo mismo que el anterior y con el mismo molde |
| `calibrar_ascensos_evitar_politica` contra `evitar_obsesion_ascenso_estatus` | `familia_id` **0,333** | **`SANO`.** Los dos hablan de ascensos y **por eso comparten clave de familia**, que es lo que la señal 2 mide. Pero sus actos son disjuntos: uno **calibra los ascensos entre iguales antes de aprobarlos** (`L213` a `L223`), el otro **decide que se anuncia y que se elogia cuando ya hay ascenso** (`L229` a `L237`). Ni un acto compartido, **dos entregables distintos**, y el libro los pone en **dos secciones distintas** (`PROMOTIONS` y `REWARD YOUR ROCK STARS`) |
| `armar_plan_anual_crecimiento_equipo` contra `disenar_equipo_plan_anual` | `familia_id` **0,500**, y **es el unico que CRUZA DE LIBRO** | **`SANO`.** El vecino es de **Zhuo** (`fuentes: zhuo_manager`) y **vive en el grafo**, no en la bandeja. Los dos son planes anuales de equipo y de ahi la familia `0,500`, pero **son de dos cosas distintas**: el de Zhuo es un **plan de plantilla** (organigrama futuro, analisis de huecos, lista de puestos abiertos para contratar) y el mio es un **plan de crecimiento** (nombres en casillas, planes de tres a cinco puntos, calibracion entre iguales, equidad entre niveles). **Cero actos compartidos y dos entregables sin interseccion** |

> ### **SEIS PARES, SEIS `SANO`, CERO `CONTINUA` Y CERO `REPITE`. Y no es un `SANO` por cansancio: dos de los seis se resuelven con REGLA ESCRITA (hermanos de serie, `EXTRACTOR.md` 15.6) y los otros cuatro con la comparacion de actos y entregables, que es la vara de `4.1`.**
>
> **EL UNICO `CONTINUA` DE LA VUELTA ES EL DE `O.5.a`, Y LA ADUANA NO LO LEVANTO.** Esa es la
> frase que resume `D.19` mejor que ninguna de las mias: **la maquina levanto seis pares y los
> seis eran sanos; el par que de verdad tiene arista lo levanto una lectura.**

### O.6.5.b. **Y UN HECHO QUE ENCONTRE SIN BUSCARLO, Y QUE VA CONTRA MI PROPIA CORRECCION: MI ARREGLO DE `O.3.d` EMPUJO UNA SEÑAL POR DEBAJO DE SU UMBRAL**

*No lo buscaba. Salio de comparar los informes de antes y los de despues, que es lo que hay que
hacer cuando se corrige un candidato ya informado.*

| par | **ANTES** de la correccion de las cuentas | **DESPUES** |
|---|---|---|
| `evitar_obsesion_ascenso_estatus` contra `reconocer_excelencia_trayectoria_gradual` | `similitud_texto` **0,355**, `[BLOQUEARIA]` levantada | `similitud_texto` **0,343**, **NO se levanta** |

    $ (medido con src.aduana.medir, los dos sentidos)
      evitar_obsesion contra reconocer_excelencia : similitud_texto 0.343  levantada: ninguna
      reconocer_excelencia contra evitar_obsesion : similitud_texto 0.348  levantada: ninguna
    $ grep -c "reconocer_excelencia" .aduana_v21/12_evitar_obsesion.txt          ->  2   (ANTES: levantado)
    $ grep -c "reconocer_excelencia" .aduana_v21/final/evitar_obsesion_ascenso_estatus.txt -> 0   (DESPUES: no)

> ### **RETIRAR CUATRO PALABRAS MIAS DE DOS PASOS MOVIO LA SEÑAL DE `0,355` A `0,343` Y CRUZO EL UMBRAL `0,35` HACIA ABAJO. Y EL PAR QUE DESAPARECIO NO ES UN PAR CUALQUIERA: SON LOS DOS NODOS EN QUE LA `ACTA 20` `4.3` PARTIO EL MISMO TRAMO.**
>
> **LO QUE ESTO DICE, Y LO DIGO CONTRA MI, no a mi favor:** mi correccion **fue buena para la
> fidelidad y mala para la visibilidad del par**. Las dos cosas son ciertas a la vez, y **no me
> invento un arreglo para que salga solo la buena**: la fidelidad manda (`D.30`, `EXTRACTOR.md`
> 15.4) y las cuentas atribuidas se retiran igual.
>
> **LO QUE ANADE A `D.19`, y es la fila mas dura de esta vuelta:** un par a `0,355` y un par a
> `0,343` **son el mismo par**, y el umbral los separa. **La señal 1 en la banda media no esta
> midiendo hermandad: esta midiendo cuantas de mis muletillas sobrevivieron a mi propia
> relectura.** `EXTRACTOR.md` 11 ya lo dice de la banda media (*ruido tres de cada cuatro veces*);
> esto lo enseña desde dentro, **con el mismo par antes y despues**.
>
> **Y NO PIDO MOVER EL UMBRAL** (`EXTRACTOR.md` 11: un umbral se juzga contra su cola, no contra un
> par). **Lo que hago es lo que puedo hacer: dejar el par declarado por lectura**, aqui abajo, para
> que no dependa de una señal que un adjetivo mueve.

| par declarado por lectura, fuera de toda señal | mi veredicto |
|---|---|
| `evitar_obsesion_ascenso_estatus` contra `reconocer_excelencia_trayectoria_gradual` | **`SANO`, y la razon es la adjudicacion de la `ACTA 20` `4.3`:** son los dos nodos del tramo `L225` a `L251` y **lo que los separa es la activacion**, no el rotulo. El primero se dispara **cuando HAY ascenso o elogio publico**; el segundo, **precisamente cuando NO vas a ascender**. **Dos activaciones opuestas no son el mismo nodo**, y por eso el veredicto es `SANO` y no `CONTINUA`: **ninguno despliega al otro, se excluyen** |
