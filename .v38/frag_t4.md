
## BC.7. **TAREA 4. LAS DOS PREGUNTAS SUBEN A LA COLA DE DOCTRINA, Y NO LAS RESUELVO**

*`D.53`. La cola abrio en `6` y `0` bloquean. **Estas dos la dejan en `8`, y siguen sin bloquear.**
`EXTRACTOR.md` 7 dice que un pendiente de doctrina **no detiene**: se registra y se sigue.*

### BC.7.a. **PREGUNTA `7`: EL LIBRO SE CONTRADICE Y NINGUN NODO LO DICE**

**Las dos frases, las dos leidas hoy y las dos del mismo libro:**

<!-- TALLADO: parcial salida=.v38/contradiccion.txt -->

    $ sed -n "21p" fuentes/scott_radical_candor/cap_12.md | cut -c300-420
    icism. If you want, you can copy the Radical Candor framework in Chapter Two and track who's saying what to you there.
    $ python .v38/pasos.py desplegar_marco_franqueza_radical | grep "P08"
      P08: No escribas nombres en las casillas.

**`cap_12` `L21` invita a llevar en el marco la cuenta de quien te dice que; `cap_01` prohibe escribir
nombres en las casillas.** Puede que no choquen del todo, porque una cosa es apuntar de quien viene la
guia que **tu** recibes y otra etiquetar a una persona con un cuadrante. **Pero eso ya seria yo
decidiendo, y el libro no lo escribe.** Los dos pasos son transcripcion fiel de su linea y **ninguno es
`PUENTE`**.

**NO LA RESUELVE NADIE DE ESTE BUCLE Y NO TOCO NINGUNO DE LOS DOS NODOS.** Y lo digo con una cosa mas
que esta vuelta añade: **acabo de cablear la arista entre los dos** (`BC.5.a`), y **el cable cuelga de la
primera mitad de `P08`**, *copia el marco*. **La contradiccion vive en la segunda mitad y el cable no la
toca.**

### BC.7.b. **PREGUNTA `8`: LA SEÑAL `1` MIDE MI FORMULA TANTO COMO EL CONTENIDO DEL NODO**

**La señal `1` compara `titulo` mas `resumen_teorico` mas pasos.** En un lote escrito de una sentada,
eso mide **la formula del extractor** tanto como el contenido del nodo. **Lo midieron dos instrumentos
por separado**, `APERTURA_CIEGA.md` 13.2 y la aduana en seco de la `ACTA 36` 7.

**Y ESTA VUELTA LO VUELVE A VER, en tres de mis veredictos:** los pares
`contar_cuatro_historias` contra `evitar_presion_social_actos_equipo`,
`contar_historias_propias` contra `abrazar_incomodidad_silencio_contar_seis` y
`practicar_triangulo` contra `escuchar_entender_critica_dominar_defensa` **se levantan porque dos pasos
mios empiezan por la misma formula** (*Y cuenta con lo que el texto dice*), **no porque compartan objeto.**
**Los tres salen `SANO` y los tres cuestan una lectura entera.**

**NINGUN UMBRAL SE TOCA EN NINGUNA VUELTA** (`EXTRACTOR.md` 11), asi que **esto no es una propuesta de
mover el `0,35`**: es la pregunta de que se hace con una señal que en parte mide al que escribe.

### BC.7.c. LAS DOS, ESCRITAS EN EL TABLERO Y NO EN UN PARRAFO

<!-- TALLADO: parcial salida=.v38/cola_doctrina_salida.txt -->

    $ python .v38/cola_doctrina.py
    la pregunta 7 ya estaba: no se duplica
    la pregunta 8 ya estaba: no se duplica
    la cola queda en 8 pregunta(s), 0 bloquea(n)

**ESA SALIDA ES LA DE LA SEGUNDA CORRIDA Y LO DIGO EN VEZ DE PEGAR LA PRIMERA:** el instrumento es
idempotente, la primera corrida escribio *pregunta 7 anexada* y *pregunta 8 anexada*, y **volver a
correrlo es la comprobacion de que las dos aterrizaron**. Pego la que el fichero sostiene hoy (`D.41`),
no la que me gustaria ensenar.

**Su sede es `config/frentes.json`, que es de donde el tablero las lee**, y no este reporte: *una
pregunta que se contesta cuando haya tiempo y que no esta escrita en ningun sitio no esta en cola, esta
olvidada* (`src/tablero.py`, `cola_de_doctrina`). **La comprobacion de que el tablero las ve va en el
cierre**, recomputada alli y no aqui.
