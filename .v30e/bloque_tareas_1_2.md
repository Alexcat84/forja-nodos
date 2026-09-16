
### W.2.e. **LA TANDA, UNO POR VEZ Y CON SU SALIDA PEGADA**

**UNO POR VEZ, Y ESTA VUELTA NO HIZO FALTA QUE LO RECORDARA NADIE.** Cada `insertar` termino antes de
lanzarse el siguiente, y **el cerrojo de `src/cerrojo.py` no llego a avisar ni una vez**, que es lo
que se espera cuando la regla se cumple. La caida de dato de la vuelta 28 (`V.5.e`) fue lanzar dos a
la vez; **hoy no hay ninguna que declarar por ese motivo.**

<!-- TALLADO: salida=.v30e/tanda_v30.txt -->

FILA_TANDA

**LAS TRECE CIFRAS DE LA COLUMNA DE NODOS EN EL GRAFO SON CONSECUTIVAS, DE `244` A `256`**, y eso es
lo que prueba que ninguna corrida se comio a otra: el censo sube de uno en uno, trece veces.

### W.2.f. **Y LOS `77` PARES DE LA COLA SALEN AL DIGITO CONTRA EL BARRIDO CIEGO DEL AUDITOR**

*Es la comprobacion que mas vale de la vuelta, porque **su cifra la escribio otro rol antes de que yo
tocara nada**, sobre una poblacion que yo no elegi, y la mia sale de doce corridas reales de la
aduana.*

<!-- TALLADO: salida=.v30e/cuadre_77.txt -->

FILA_CUADRE_77

**`77` contra `77`, y los doce repartos coinciden uno a uno** con la tabla de `APERTURA_CIEGA.md`
(`9`, `4`, `1`, `7`, `3`, `3`, `10`, `10`, `10`, `8`, `7`, `5`). **El encargo publica esa misma cifra
en su `TAREA 1`** (*quedan 12 candidatos con 77 pares de cola de lectura*).

> **`LECTURA`, en linea aparte: que cuadre no era obvio, y por eso lo mido en vez de darlo por hecho.**
> El barrido ciego corrio contra una poblacion de `348` con el grafo en `243`; **mis doce corridas
> fueron moviendo esa poblacion** (`243` mas `105` al abrir, `255` mas `93` al cerrar `cap_07`), porque
> cada nodo que entra sale de la bandeja y aparece en el grafo. **El total se conserva y el reparto
> tambien**, y eso dice que la poblacion de `D.38.5` (grafo mas bandejas) es la que hace comparables
> las dos medidas. Si se hubiera medido solo contra el grafo, esta cifra no habria cuadrado.

### W.2.g. **LAS DOS SERIES `D.37` QUE LA COLA DEL ENCARGO DABA POR ABIERTAS, CERRADAS LAS DOS**

*La `TAREA 3` del encargo las publica como cola: `3` partes de `minimizar_impuesto_colaboracion_equipo`
con **ninguna viva**, y la mitad `Burnout` de `aprender_resultados_vencer_dos_presiones`.*

| serie | cabeza | paso que enumera | partes | como se cablearon |
|---|---|---:|---:|---|
| las tres cosas del equilibrio (`L373`) | `minimizar_impuesto_colaboracion_equipo` | **4** | **3 de 3** | `proteger_tiempo_equipo_jefe` por la ADUANA, cerrando su arista en cola; `mantener_manos_trabajo_real_equipo` y `reservar_calendario_tiempo_ejecutar` por `forja.py arista` |
| las dos presiones (`L401`) | `aprender_resultados_vencer_dos_presiones` | **6** | **2 de 2** | `cambiar_posicion_hechos_explicar_cambio` ya vivia cableada; `cuidarse_agotamiento_centro_rueda` por `forja.py arista` |

**POR QUE DOS VIAS Y NO UNA, y lo digo porque parece incoherencia y no lo es:** la aduana cablea la
arista **solo cuando levanta a la madre como vecina del hijo**. Levanto a `minimizar_impuesto` para
`proteger_tiempo` y **no** para las otras dos, ni a `aprender_resultados` para `cuidarse`. `D.19` ya
lo tiene medido: **la señal 3 levanta el `3` por ciento de las aristas declaradas.** Donde la aduana
llega, la dejo hacer, que es lo que la vuelta 28 adjudico en su `V.5.d`; donde no llega, uso el
comando, que es para lo que `D.37` lo escribio. **Correr los dos sobre el mismo par seria el
duplicado.**

**LAS TRES DECLARACIONES, con el paso de la madre impreso por el propio comando** (`D.37`: *pegas la
salida del comando en tu reporte*):

<!-- TALLADO: parcial salida=.v30e/arista_01_mantener.txt -->

    DECLARACION DE ARISTA POR LECTURA (D.37)
      madre: minimizar_impuesto_colaboracion_equipo
      hijo : mantener_manos_trabajo_real_equipo
      paso citado de la madre: 4
        Aplica las tres cosas que el texto dice haber aprendido sobre como acertar con ese equilibrio: no malgastes el tiempo de tu equipo, manten la tierra b
      señales del par: familia_id 0.125, paso_contra_nodo 0.494, similitud_texto 0.321
        NINGUNA SEÑAL LA LEVANTA. La caza la lectura (D.19, D.29).
    GATE VERDE sobre la simulacion. ARISTA ESCRITA RESUELTA: minimizar_impuesto_colaboracion_equipo > mantener_manos_trabajo_real_equipo

<!-- TALLADO: parcial salida=.v30e/arista_02_reservar.txt -->

    DECLARACION DE ARISTA POR LECTURA (D.37)
      madre: minimizar_impuesto_colaboracion_equipo
      hijo : reservar_calendario_tiempo_ejecutar
      paso citado de la madre: 4
        Aplica las tres cosas que el texto dice haber aprendido sobre como acertar con ese equilibrio: no malgastes el tiempo de tu equipo, manten la tierra b
      señales del par: familia_id 0.0, paso_contra_nodo 0.452, similitud_texto 0.347
        NINGUNA SEÑAL LA LEVANTA. La caza la lectura (D.19, D.29).
    GATE VERDE sobre la simulacion. ARISTA ESCRITA RESUELTA: minimizar_impuesto_colaboracion_equipo > reservar_calendario_tiempo_ejecutar

<!-- TALLADO: parcial salida=.v30e/arista_03_cuidarse.txt -->

    DECLARACION DE ARISTA POR LECTURA (D.37)
      madre: aprender_resultados_vencer_dos_presiones
      hijo : cuidarse_agotamiento_centro_rueda
      paso citado de la madre: 6
        Vence las dos enormes presiones que el texto dice que tentaban a la autora a dejar de aprender cuando dirigia un equipo grande: la presion de ser cohe
      señales del par: familia_id 0.0, paso_contra_nodo 0.432, similitud_texto 0.346
        NINGUNA SEÑAL LA LEVANTA. La caza la lectura (D.19, D.29).
    GATE VERDE sobre la simulacion. ARISTA ESCRITA RESUELTA: aprender_resultados_vencer_dos_presiones > cuidarse_agotamiento_centro_rueda

**Y LA QUE CERRO LA ADUANA SOLA**, dos inserciones despues de quedar en cola:

<!-- TALLADO: parcial salida=.v30e/ins_09_proteger.txt -->

    arista madre-hijo cableada y escrita RESUELTA: minimizar_impuesto_colaboracion_equipo > proteger_tiempo_equipo_jefe

### W.2.h. **LAS CUATRO ARISTAS, COMPROBADAS POR SUS DOS EXTREMOS EN EL DATASET Y NO POR LA PROSA DE LA SALIDA**

<!-- TALLADO: salida=.v30e/aristas_cerradas.txt -->

FILA_ARISTAS_CERRADAS

### W.2.i. **LA FILA DE LA TAREA 1: `cap_07` QUEDA CERRADO EN INSERCION, 12 DE 12**

<!-- TALLADO: salida=.v30e/cap07_vacio.txt -->

FILA_CAP07_VACIO

## W.3. TAREA 2: **EL PAR DEL CALENDARIO, QUE NINGUNA SEÑAL CRUZA**

**HECHA, Y HECHA COMO EL ENCARGO MANDA: por lectura y sin esperar a una señal que no iba a llegar.**

El encargo dice *la vuelta que inserte al primero lo lee contra el segundo y escribe su veredicto por
lectura*. **El primero es `bloquear_tiempo_pensar_calendario`, que es de `cap_11` y no de `cap_07`**,
asi que entra como candidato numero `13` de la tanda, **despues de cerrar `cap_07` entero** para no
romper el orden del libro dentro del capitulo.

**LA SALIDA DE LA ADUANA, QUE ES LA PRUEBA DE QUE NINGUNA SEÑAL LO LEVANTO** y de que entro igual:

<!-- TALLADO: parcial salida=.v30e/ins_13_bloquear.txt -->

    DECLARADOS POR LECTURA: 1. Ninguna señal los levanto.
      agendar_cuidados_propios_cumplirlos  [Poner en el calendario lo que necesitas hacer por ti, y despues presentarte a esas citas como te presentarias a una con tu jefe]
        señales: familia_id 0.0, paso_contra_nodo 0.492, similitud_texto 0.309
        umbrales: similitud 0.35, familia 0.30, paso 0.60
      LA JERARQUIA LA CAZA LA LECTURA, NO LA SEÑAL (D.19, D.29).

**LAS TRES SEÑALES POR DEBAJO DE SU UMBRAL, LAS TRES**, que es exactamente lo que el auditor predijo
en `ACTA 28` `6.10` (*mi barrido no los cruza ni una vez en las `77` lineas*). **Sin este veredicto
declarado, este par no se habria leido nunca.**

**LO RELEI ENTERO ANTES DE FIRMARLO EN VEZ DE COPIAR LA CLASE DEL ACTA**, y lo digo porque copiar una
clase adjudicada es justo lo que `EXTRACTOR.md` 5 prohibe. Mi lectura coincide con la suya y `SANO` se
sostiene: comparten el instrumento (el calendario) y lo aplican a **dos objetos distintos**, uno el
tiempo de pensar en el trabajo y otro las citas de uno consigo mismo; **ninguno nombra el
procedimiento del otro en ningun paso**, asi que no hay madre que senialar; y **queda procedimiento en
los dos lados** cuando se quita lo comun: el paso `6` del candidato (*anima a todos los de tu equipo a
hacer lo mismo*) y los pasos `2` y `3` del vecino (*pon en el calendario tu tiempo de desplazamiento*,
*haz como si tuvieras que coger un tren*).

**EL VEREDICTO YA NO VIVE SOLO EN ESTE REPORTE: ESTA EN SU SEDE.** `D.39` nombraba por su nombre el
defecto que arreglaba (*un veredicto razonado que no llega a la bitacora vive solo en `REPORTE.md`,
que no es su sede*), y este era el ejemplar vivo que el encargo dejaba pendiente.

### W.3.a. **Y AL INSERTARLO APARECIO UNA ARISTA `D.29` QUE NADIE HABIA MEDIDO, QUE ES LO QUE ESTA TAREA VALIA**

**`desplegar_plan_orden_operaciones_franqueza_radical` es MADRE de `bloquear_tiempo_pensar_calendario`,
y las dos siguen siendo cifras del mismo lote.** La madre es la pieza 1 de `cap_12`, el plan de
franqueza radical que recorre el libro entero por su orden de operaciones, y **su paso `30` es una
sola frase**:

    30 | Pon algo de tiempo para pensar en tu calendario.

**El hijo despliega esa frase en seis pasos que la madre no tiene** y que son de `cap_11`: reconocer a
que te enfrentas, la consecuencia de no hacer nada, agendarlo, mantenerlo sagrado, decir que nadie
agende encima, enfadarse si lo intentan, y animar al equipo a hacer lo mismo. **Eso es `D.29` literal:
la madre NOMBRA y el hijo PROCEDIMENTA.**

**Y LA MADRE SE DECLARA A SI MISMA CABEZA Y PARTE**, en su propio `resumen_teorico`, que lei antes de
firmar: *LOS REMITES NO SE CONVIERTEN EN PASOS DE PROCEDIMIENTO AJENO: cada paso de aqui nombra la
etapa y su condicion, y NO copia los pasos del nodo que la despliega, que es justo la linea que
`EXTRACTOR.md` 9 traza entre nombrar y procedimentar*.

**LA ARISTA QUEDA EN COLA PORQUE LA MADRE ESPERA EN LA BANDEJA**, y va al bloque titulado de `W.5`.
**Va marcada como discutible en `W.6`** y digo por que sin esperar a que me lo digan: la `ACTA 28`
`2.2` adjudico que **una remision hacia atras no es una cabeza**, y este paso `30` remite hacia
`cap_11` desde `cap_12`. **Mi lectura es que aquella era una remision suelta dentro de una anecdota y
esta es un ITEM de un inventario ordenado**, que es la cara positiva de `D.27`; pero el que adjudica
no soy yo.
