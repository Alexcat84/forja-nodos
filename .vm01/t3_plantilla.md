
---

# TAREA 3. LA FIDELIDAD `D.30`, RELEIDA PASO A PASO CONTRA SU PARRAFO, FILA POR UNIDAD Y TOTAL

*`D.30`: **ninguna guarda de esta casa ve un paso que tu escribiste y el libro no dice.** La
relectura no la puede hacer la aduana, y el encargo la pide fila por unidad mas total, con la
escalada decidida **sobre el peor capitulo y no sobre el promedio**. Tope **10**.*

## 3.a. QUE PONE EL DATO Y QUE PONGO YO, dicho antes de la tabla

**El DENOMINADOR lo cuenta el instrumento de los JSON de la bandeja en esta corrida. La CLASE de
cada paso y la LINEA de la que sale las pongo yo leyendo**, y viven en `.vm01/clases.txt`. El
instrumento **comprueba que mi lectura cubre todos los pasos de todos los nodos**: si a un nodo le
faltan clases o le sobran, sale en rojo y lo nombra. **Una relectura que no cubre cada paso no es
una relectura**, y esa comprobacion es lo unico que el codigo puede aportar aqui.

**LA TABLA PASO A PASO, con la linea del libro de cada paso, esta entera en
`.vm01/fidelidad_lote.txt`: son `70` filas, una por paso, y no se repite aqui por el austero
(`D.47`).** Lo que se publica aqui es el saldo por unidad, que es lo que el encargo pide.

## 3.b. `PASOS INVENTADOS POR CAPITULO`, DEL LOTE ENTERO Y NO SOLO DEL TRAMO

`python .vm01/fidelidad.py`, guardada en `.vm01/fidelidad_lote.txt`. **Releo tambien `cap_01` y
`cap_02`**, que no son de esta vuelta, porque `EXTRACTOR.md` 5 prohibe tomar una cifra de un acta
previa: **una fila que yo no he releido no la puedo firmar, y un cero que nadie ha medido no es un
cero.** Asi las tres filas del lote son mias.

<!-- TALLADO: script=.vm01/fidelidad.py salida=.vm01/fidelidad_lote.txt -->

@@TABLA_UNIDADES@@

<!-- TALLADO: script=.vm01/fidelidad.py salida=.vm01/fidelidad_lote.txt -->

@@TABLA_FRENO@@

## 3.c. Y LO QUE UN `0,00` NO DICE: LOS OCHO PUENTES QUE ESCRIBI Y RETIRE EN EL ACTO

*`D.30` punto 3: **en el mismo acto**, no en una vuelta posterior. Y la vuelta 32 lo escribio
contra si misma en una linea: **una vuelta que solo encuentra aciertos propios no esta midiendo.**
Un numerador en `0` que no diga cuantos puentes hubo que retirar es un numerador que oculta el
trabajo que lo dejo en `0`.*

<!-- TALLADO: script=.vm01/fidelidad.py salida=.vm01/fidelidad_lote.txt -->

@@TABLA_RETIRADOS@@

> ### **SIETE DE LOS OCHO SON LA MISMA ESPECIE, Y ES UNA QUE LA TABLA DE TRES DE `D.30` NO TIENE**
>
> `D.30` nombra tres especies: **el destinatario, el periodo y el responsable.** **Siete de mis ocho
> puentes son una cuarta: EL MEDIO.** No inventan a quien, ni cada cuanto, ni quien responde:
> **inventan el soporte en que la accion se hace.** *Anota* donde el libro dice *observe*, *escribe*
> donde el libro dice *saco el veredicto*, *di en voz alta* donde el libro no dice nada.
>
> **POR QUE ESTE CAPITULO LA PRODUCE EN SERIE, y no es casualidad:** `cap_03` es narracion en pasado
> de lo que un hombre miro. **Para convertir *miro* en imperativo hay que elegir un verbo, y el verbo
> facil trae soporte pegado.** *Anota* suena a paso y *mira* suena a nada, asi que la mano escribe
> *anota*. Y la especie es barata de cazar **solo si se caza mientras se escribe**: en la relectura de
> una vuelta posterior, *anota* se lee como un paso perfectamente normal.
>
> **EL OCTAVO ES DE OTRA FAMILIA Y ES EL PEOR DE LOS OCHO: EL DESTINATARIO INVERTIDO.** *No te
> quedes en el medio con los que hablan* convierte en **prohibicion dirigida al lector** lo que el
> libro escribe como **descripcion de lo que el autor hizo**. Las dos piezas del dato son del libro
> (el medio es donde estaban los que hablaban, `L55`; el autor se fue por la periferia, `L57`); **la
> prohibicion la puse yo**, y es la unica de las ocho que **llego a pasar la aduana antes de que la
> cazara**, con su informe guardado en `.vm01/aduana/c6_intento1_puente_retirado.txt`. **La aduana le
> dio verde, que es exactamente lo que `D.30` dice que hace: mide otra cosa.**
>
> **NO PROPONGO NINGUNA REGLA NUEVA, Y ES A PROPOSITO:** en este frente una pregunta de doctrina es
> PARADA (`D.45`), y esto lo es. **Lo dejo medido y nombrado para el fundador**, con sus ocho casos y
> su capitulo, que es lo que una propuesta necesita antes de ser propuesta.

## 3.d. LA OTRA ESPECIE QUE LA RELECTURA CAZO, Y NO ES UN PUENTE: LA **FRONTERA INCOMPLETA**

**Son DOS casos, los dos en `cap_02`, y el segundo NO LO ENCONTRE YO.**

### 3.d.1. El primero, mio: la microgestion que no esta en la linea que el nodo declara

**Releyendo `cap_02` encontre que la glosa del paso `2` de
`encargar_meta_especifica_dejar_libre_metodo`** (*es lo que separa este encargo de la
microgestion*) **NO sale de `L49`, que es la linea que ese candidato declara, sino de `L51`.** La
comprobacion, corrida en esta vuelta y guardada en `.vm01/micromanage.txt`:

<!-- TALLADO: parcial salida=.vm01/micromanage.txt -->

| lo que corri | lo que salio |
|---|---|
| `grep -in "micromanage" fuentes/marquet_turn_the_ship/cap_02.md` | **linea 51**, y solo esa: *Since Mark wasn't going to micromanage me, maybe this was a chance to do something different* |
| `grep -ilc "micromanage" fuentes/marquet_turn_the_ship/*.md` | **dos unidades del libro** la traen, `cap_02` y `cap_09` |

### 3.d.2. El segundo, del AUDITOR CIEGO, y mi relectura no lo vio

**`cambiar_forma_trabajar_conservar_plantilla`, paso `4`, dice *el mensaje que manda no despedir a
nadie*. Que no despidiera a nadie NO esta en `L29`, que es la linea que ese nodo declara para el
paso: esta en `L27`.** Lo encontro la `APERTURA_CIEGA.md` de esta misma vuelta, seccion `9.1`
punto `2`, y **yo habia dado ese paso por cerrado contra `L29` una hora antes**.

<!-- TALLADO: parcial salida=.vm01/citas_cap02.txt -->

    27: I was thinking that too. In the end, I fired no one.
    29: This was important because it sent the message to each crew member that he wasn't screwed up, the leadership was. My challenge wou ...

**LO DIGO SIN ADORNARLO: relei las mismas diez lineas de `cap_02` que el auditor, encontre una de
las dos fronteras corridas y no la otra.** La suya es incluso mas visible que la mia, porque la
linea que falta esta **pegada** a la declarada. **Corregido en el acto, en cuanto lo lei, con su
credito escrito dentro del propio candidato.**

### 3.d.3. Por que la especie importa, y es la mitad del valor de los dos casos

| | |
|---|---|
| **que NO es** | **un puente.** Las dos lineas son del libro y de la misma unidad, y el numerador de `cap_02` se queda en `0` |
| **que SI es** | una **FRONTERA INCOMPLETA**: el nodo declara unas lineas y un paso se apoya en otra que no declara |
| **como se arregla** | **declarando la linea**, que es lo que hice en los dos: correccion anadida al `resumen_teorico` **sin borrar una palabra de lo anterior**, y los dos candidatos vueltos a pasar por la aduana |
| **por que importa la diferencia** | un puente se **retira**; una frontera incompleta se **escribe**. **Confundirlas retiraria un paso que el libro si dice**, y eso es un dano y no una correccion |
| **y que la delata** | las dos veces, **un paso que lleva dos afirmaciones y una sola linea citada.** Es una señal barata y no la tenia escrita en ningun sitio |
