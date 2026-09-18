
### CC.7.g. **UN COSTE DE MI PROPIA CORRECCION, QUE NADIE ME PREGUNTA Y DECLARO YO**

**La correccion declarada de la `TAREA 1.B` sobre `practicar_triangulo_critica_tres_papeles` cambio la
huella del nodo, y con ella puso RANCIOS `4` veredictos** que se habian emitido contra su texto
anterior (lineas `484` a `487`).

<!-- TALLADO: parcial salida=.v39/rancios.txt -->

    $ python forja.py rancios | grep -c "\[RANCIO\]"
    51
    $ python forja.py rancios | grep "practicar_triangulo" | grep -c eec451c2e48944c6
    4

**NO ES UNA CAIDA Y `D.15` LO DICE POR SU NOMBRE**: la vigencia es **cola de trabajo**, no guarda que
tumbe el cierre, y el propio `cerrar_reporte.py` lo publica y cierra en verde. **Pero `4` de los `51`
rancios de hoy los puse yo esta vuelta**, y eso no se dice solo: **corregir una cifra falsa dentro de un
nodo del catalogo tiene el precio de dejar rancios los veredictos que lo citaban**, y el precio es
barato comparado con dejar la cifra. **Los `4` son sobre el mismo nodo y sobre vecinos que no cambiaron:
lo que cambio es el texto de mi lado.** Van a la cola de vigencia y no los releo yo, porque releerlos es
otra tarea y esta vuelta ya entrego cuatro.
