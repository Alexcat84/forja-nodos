
---

# AC.8. LAS TRES FICHAS QUE LA VUELTA CORRIGIO, Y SI LA CORRECCION BORRO ALGO

Mi encargo pedia tres correcciones declaradas **sin borrar** (`d044`, `d045`, `d046`, manual
principio `6`). Eso se puede medir sin leer una linea de prosa: **si nada se borro, el texto viejo
tiene que seguir siendo un PREFIJO exacto del nuevo.**

    $ python .v51aud/20_sin_borrar.py
    dimensionar_numero_subordinados_medio_dia_semanal        viejo 11576 chars, nuevo 13648, crece  2072, el viejo es PREFIJO del nuevo: True
    buscar_regularidad_bloques_iguales_trabajo_mando         viejo  6169 chars, nuevo  7997, crece  1828, el viejo es PREFIJO del nuevo: True
    preparar_respuestas_estandar_interrupciones_repetidas    viejo  6267 chars, nuevo  8242, crece  1975, el viejo es PREFIJO del nuevo: True

    dimensionar_numero_subordinados_medio_dia_semanal        claves que cambian: ['resumen_teorico']
    buscar_regularidad_bloques_iguales_trabajo_mando         claves que cambian: ['resumen_teorico']
    preparar_respuestas_estandar_interrupciones_repetidas    claves que cambian: ['resumen_teorico']

Esa salida mide, para cada una de las tres fichas corregidas, el tamano de su `resumen_teorico` en
el commit de apertura de la vuelta 51 y hoy, si el viejo es prefijo literal del nuevo, y que claves
del fichero cambian entre las dos versiones.

`LECTURA`: **las tres correcciones anaden y no borran**, medido y no creido; y **la clave que cambia
es `resumen_teorico` y nada mas**, asi que ni un paso, ni una atribucion, ni un titulo se movieron.
Eso es exactamente lo que mi `TAREA 3` compro cuando adjudico que esas dos correcciones no pagaban
una pasada de aduana: **un cambio que no toca un paso no mueve un vecino**, y aqui se puede
comprobar que no toco ninguno.

## AC.8.a. **`d044`: EL PAGO QUE MI ACTA DIJO QUE ROMPIA SU PROPIO PAGO**

La vuelta 50 escribio dentro de la ficha el comando preciso, y con ello metio la cadena del comando
en la ficha que el comando barre. Corro el comando hoy, sobre el arbol ya corregido:

    $ grep -rl "Sale de la PIEZA P34" cuarentena/ docs/
    cuarentena/grove_high_output/decir_no_trabajo_excede_capacidad.json
    cuarentena/grove_high_output/dimensionar_numero_subordinados_medio_dia_semanal.json
    cuarentena/grove_high_output/usar_calendario_herramienta_planificacion_produccion.json
    docs/loop/ACTA_AUDITOR.md
    docs/loop/DEUDA.jsonl
    docs/loop/PROMPT_SIGUIENTE.md

Esa salida mide que ficheros de `cuarentena/` y de `docs/` contienen hoy la cadena que el pago de la
vuelta 50 uso como comando.

`LECTURA`: **el comando sigue devolviendo `3` fichas de la bandeja y no `2`**, o sea que el defecto
que mi `ACTA 49` midio **sigue midiendose igual**. Y eso **NO es un pago roto esta vez**, por lo que
la ficha hace con ello, que es lo contrario de afinar el comando:

    $ (cola del resumen_teorico de la ficha de P38, .v51aud/17_p38_cola.out, recortada por mi a sus dos frases de cierre)
    LA AFIRMACION, ESCRITA CON SUS DOS IDS Y SIN NINGUN COMANDO: la pieza P34 de la frontera de
    cap_04 publicada en la vuelta 46 (HH.2.c) es la madre de DOS fichas de la bandeja de
    grove_high_output, y son estas dos, nombradas una a una: decir_no_trabajo_excede_capacidad y
    usar_calendario_herramienta_planificacion_produccion.
    COMO SE COMPRUEBA SIN BARRER NADA: cada una de esas dos fichas declara su pieza de origen en la
    primera linea de su propio resumen_teorico.

Ese pegado es el texto que la ficha de `P38` tiene hoy en la cola de su `resumen_teorico`, cortado
por mi a las dos frases que dicen que hacer, y lo declaro cortado.

**ASI QUE CORRO LA COMPROBACION QUE LA PROPIA FICHA PROPONE**, que es la prueba de si el pago cierra:

    $ python .v51aud/18_comprobacion_d044.py
    decir_no_trabajo_excede_capacidad
       UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_04.md, unidad Cap. 3, titulo textual Managerial Leverage. Sale de la PIEZA P34 de la frontera publicada en la vuelta 46 (H

    usar_calendario_herramienta_planificacion_produccion
       UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_04.md, unidad Cap. 3, titulo textual Managerial Leverage. Sale de la PIEZA P34 de la frontera publicada en la vuelta 46 (H

    dimensionar_numero_subordinados_medio_dia_semanal
       UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_04.md, unidad Cap. 3, titulo textual Managerial Leverage. Sale de la PIEZA P38 de la frontera publicada en la vuelta 46 (H

    fichas cuya PRIMERA frase declara 'Sale de la PIEZA P34': 2
    fichas cuya PRIMERA frase declara 'Sale de la PIEZA P38': 1

Esa salida mide la cabecera del `resumen_teorico` de las tres fichas, y cuantas fichas de la bandeja
entera declaran cada una de esas dos piezas **en su frase de cabecera**.

`LECTURA`: **el metodo que la ficha propone da `2` y `1`, y da `2` y `1` sobre la bandeja de hoy, que
ya tiene `50` fichas**. La diferencia con el metodo viejo no es de afinado: **el viejo contaba
coincidencias en cualquier parte del fichero y por eso se contaba a si mismo; el nuevo ancla en la
frase de cabecera, que es la que declara el origen**, y una cita de metodo escrita en la cola de
otra ficha ya no lo ensucia. **Mi lectura es que `d044` SI cierra**, y lo que queda dentro de la
ficha son las dos lineas viejas en pie, que es lo que el principio `6` manda.

**LO QUE NO PUEDO COMPROBAR EN ESTA FASE, Y LO ESCRIBO EN VEZ DE AFIRMARLO**: la ficha dice que el
metodo vive a partir de hoy en `REPORTE.md MM.1.c`, **y `REPORTE.md` es uno de los cuatro que el
arnes retiro**. No se si esa seccion existe ni que pego. **Lo verifico en mi turno normal**, y si
esa seccion no esta o no trae la salida, entonces el pago se queda sin la mitad que se saco de la
bandeja.
