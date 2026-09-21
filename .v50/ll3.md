
## LL.3. TAREA 3. **`d036` Y `d038` PAGADAS: NUEVE CORRECCIONES DECLARADAS, CERO PASADAS DE ADUANA**

**Las nueve estan DENTRO de la ficha, que es donde sobreviven al reporte**, y ninguna borra una
letra del texto viejo (manual principio 6). **Cero pasadas de aduana**, por adjudicacion `3.c` del
encargo, y la adjudicacion la firmo el auditor contra su propio encargo anterior: **un cambio de
`2.360` caracteres en `d032` no movio ni un vecino, y esto son numeros de dos y tres cifras.**

### LL.3.a. **`d036`: EL RECUENTO VA PRIMERO, PORQUE SI DISCREPABA ESTO ERA UNA PARADA**

**El encargo me prohibe inventar una tercera cifra y me manda parar si mi recuento no da el de la
frontera. Asi que lo corri ANTES de escribir ninguna correccion:**

<!-- TALLADO: script=.v50/palabras_d036.py salida=.v50/palabras_d036.txt -->

    ficha                                          pieza rango        dice  HH.2.c  cuento  veredicto
    reunir_informacion_gerencial_vias_variadas     P7    L145 a L147    356   210     210    la frontera manda
    escalonar_fuentes_informacion_gerencial        P9    L153 a L153    208   183     183    la frontera manda
    programar_visita_area_observar_despachar       P10   L155 a L157    337   236     236    la frontera manda
    transmitir_objetivos_prioridades_preferencias  P11   L159 a L159    197   160     160    la frontera manda
    empujar_persona_reunion_direccion_preferida    P13   L167 a L167    174   147     147    la frontera manda
    subir_productividad_gerencial_tres_vias        P18   L195 a L201     62    60      60    la frontera manda
    buscar_actividad_alta_palanca_tres_vias        P19   L203 a L213    118    76      76    la frontera manda
    elegir_momento_actividad_palanca_maxima        P20   L215 a L217    297   237     237    la frontera manda

    fichas leidas: 8 ; mi recuento coincide con la frontera en 8 ; cifras declaradas que discrepan: 8

**LAS OCHO CUADRAN CONTRA LA FRONTERA Y LAS OCHO DISCREPAN DE LO QUE LA FICHA DECLARABA: NO HAY
PARADA QUE TRAER.** Y tres cosas de ese instrumento que valen mas que su salida:

- **la columna `dice` no la teclee**: se saca de la propia ficha con una expresion regular;
- **la columna `HH.2.c` tampoco**: se lee fila a fila de la tabla de frontera publicada en este
  mismo reporte;
- **el recuento es el mismo de `.v46/frontera.py` linea `136`**, no un tokenizador nuevo. **Si
  hubiera usado otro, la comprobacion no habria comprobado nada.**

### LL.3.b. **LAS OCHO CORRECCIONES, ESCRITAS DENTRO DE CADA FICHA Y SIN BORRAR EL NUMERO VIEJO**

<!-- TALLADO: script=.v50/corregir_d036.py salida=.v50/corregir_d036.txt -->

    corregida reunir_informacion_gerencial_vias_variadas     P7  356 pasa a leerse 210
    corregida escalonar_fuentes_informacion_gerencial        P9  208 pasa a leerse 183
    corregida programar_visita_area_observar_despachar       P10  337 pasa a leerse 236
    corregida transmitir_objetivos_prioridades_preferencias  P11  197 pasa a leerse 160
    corregida empujar_persona_reunion_direccion_preferida    P13  174 pasa a leerse 147
    corregida subir_productividad_gerencial_tres_vias        P18  62 pasa a leerse 60
    corregida buscar_actividad_alta_palanca_tres_vias        P19  118 pasa a leerse 76
    corregida elegir_momento_actividad_palanca_maxima        P20  297 pasa a leerse 237

    fichas corregidas por correccion declarada: 8

**CADA CORRECCION LLEVA DENTRO EL RENGLON DEL INSTRUMENTO QUE LA SOSTIENE**, pegado fila a fila, que
es lo que deja recontarla sin salir de la ficha. **Y el texto de la correccion no lo teclee ocho
veces**: sale de una plantilla que rellena con las tres cifras leidas del fichero del instrumento,
porque **teclear ocho veces la misma frase con ocho numeros distintos es exactamente el metodo que
produjo las ocho cifras que hoy pago.**

### LL.3.c. **`d038`: LA LINEA DEL METODO QUE DEJO DE REPRODUCIRSE PORQUE SE MIDE A SI MISMA**

<!-- TALLADO: parcial salida=.v50/d038_grep.txt -->

    $ grep -l "PIEZA P34" cuarentena/grove_high_output/*.json
    cuarentena/grove_high_output/decir_no_trabajo_excede_capacidad.json
    cuarentena/grove_high_output/dimensionar_numero_subordinados_medio_dia_semanal.json
    cuarentena/grove_high_output/usar_calendario_herramienta_planificacion_produccion.json
      fichas: 3

    $ grep -l "Sale de la PIEZA P34" cuarentena/grove_high_output/*.json
    cuarentena/grove_high_output/decir_no_trabajo_excede_capacidad.json
    cuarentena/grove_high_output/usar_calendario_herramienta_planificacion_produccion.json
      fichas: 2

**`3` CONTRA `2`, Y EL TERCERO ES LA PROPIA FICHA.** La afirmacion que la linea sostiene **es cierta
y no cambia**: `P34` es madre de esas dos. **Lo defectuoso es la linea del metodo**, y la declare yo
mismo en `KK.2.e` antes de que nadie me la senialara.

**LA CORRECCION ESCRITA DENTRO DE LA FICHA CAMBIA EL COMANDO Y DEJA EL VIEJO EN PIE**, y lleva
pegados los dos renglones de arriba. **Y la leccion, que vale mas que la linea:**

> **UNA CITA DE METODO ESCRITA DENTRO DEL OBJETO QUE MIDE DEJA DE REPRODUCIRSE EN CUANTO EL OBJETO
> ENTRA EN LA POBLACION QUE EL METODO BARRE.**

### LL.3.d. **LO QUE ESTAS NUEVE CORRECCIONES NO TOCARON, MEDIDO POR DIFERENCIA Y NO PROMETIDO**

<!-- TALLADO: script=(comparacion campo a campo contra HEAD) salida=.v50/pasos_intactos.txt -->

    las 9 fichas corregidas, comparadas con HEAD campo a campo
    reunir_informacion_gerencial_vias_variadas         campos cambiados: ['resumen_teorico']   pasos identicos: True
    escalonar_fuentes_informacion_gerencial            campos cambiados: ['resumen_teorico']   pasos identicos: True
    programar_visita_area_observar_despachar           campos cambiados: ['resumen_teorico']   pasos identicos: True
    transmitir_objetivos_prioridades_preferencias      campos cambiados: ['resumen_teorico']   pasos identicos: True
    empujar_persona_reunion_direccion_preferida        campos cambiados: ['resumen_teorico']   pasos identicos: True
    subir_productividad_gerencial_tres_vias            campos cambiados: ['resumen_teorico']   pasos identicos: True
    buscar_actividad_alta_palanca_tres_vias            campos cambiados: ['resumen_teorico']   pasos identicos: True
    elegir_momento_actividad_palanca_maxima            campos cambiados: ['resumen_teorico']   pasos identicos: True
    dimensionar_numero_subordinados_medio_dia_semanal  campos cambiados: ['resumen_teorico']   pasos identicos: True

    fichas cuyo UNICO campo cambiado es resumen_teorico: 9 de 9

**NI UN PASO, NI UNA ATRIBUCION, NI UNA FUENTE, NI UN TITULO.** Es lo que el encargo dice que esto
es (*no es un puente, no mueve un paso y no toca una atribucion*), **y lo mido en vez de repetirlo.**

**Y EL TEXTO VIEJO SIGUE EN PIE EN LAS NUEVE**, que es lo que convierte esto en correccion declarada
y no en borrado:

<!-- TALLADO: parcial salida=.v50/d036_intacto.txt -->

    el numero VIEJO sigue escrito en la ficha, y la correccion se lee al lado
    reunir_informacion_gerencial_vias_variadas     P7   viejo 356 en pie: True    correccion escrita: True
    escalonar_fuentes_informacion_gerencial        P9   viejo 208 en pie: True    correccion escrita: True
    programar_visita_area_observar_despachar       P10  viejo 337 en pie: True    correccion escrita: True
    transmitir_objetivos_prioridades_preferencias  P11  viejo 197 en pie: True    correccion escrita: True
    empujar_persona_reunion_direccion_preferida    P13  viejo 174 en pie: True    correccion escrita: True
    subir_productividad_gerencial_tres_vias        P18  viejo  62 en pie: True    correccion escrita: True
    buscar_actividad_alta_palanca_tres_vias        P19  viejo 118 en pie: True    correccion escrita: True
    elegir_momento_actividad_palanca_maxima        P20  viejo 297 en pie: True    correccion escrita: True

    d038: la linea vieja sigue en pie: True   correccion escrita: True

**LAS DOS GUARDAS DE UNA LINEA QUE EL ENCARGO SI ME PIDE, sobre el arbol con las nueve dentro:**

<!-- TALLADO: parcial salida=.v50/t3_gate.txt -->

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346

<!-- TALLADO: parcial salida=.v50/t3_guiones.txt -->

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

**NINGUNA FICHA ROTA**, que es lo unico que estas dos guardas pueden certificar de nueve
correcciones de prosa.

### LL.3.e. **LO QUE PROPUSE EN `KK.5.j` Y EL AUDITOR NO TOMO, DICHO SIN REABRIRLO**

**Mi propuesta `4` de la vuelta 49 pedia que la linea del metodo de `P38` se rehiciera EN la pasada
de aduana de esta vuelta**, para que saliera gratis. **El encargo adjudica lo contrario en `3.c`:
que las nueve se escriben sin pasada propia.** No lo discuto y lo recojo, **y digo por que la
adjudicacion es mejor que mi propuesta**: la mia daba por supuesto que `P38` iba a pasar la aduana
hoy, y hoy **`P38` no se inserta ni se vuelve a medir**, porque el lote no cierra. **Mi propuesta
habria comprado una pasada de `1017,3` s para un cambio que no mueve ni un vecino.**

| tarea | que pide | estado |
|---|---|---|
| `LL.3` | pagar `d036` y `d038`: nueve correcciones declaradas sin borrar, y cero pasadas de aduana | **CERRADA en `LL.3`, las dos deudas PAGADAS**: `8` mas `1` correcciones escritas dentro de su ficha con su renglon pegado, `9` de `9` con solo `resumen_teorico` tocado, texto viejo en pie en las nueve, `gate` y `guiones` verdes, y **cero pasadas de aduana gastadas** |
