
## CC.2. **TAREA 1.A, BLOQUEANTE: LAS DOS PRUEBAS DEJAN DE CLAVAR EL `6` Y LEEN SU SEDE**

**Es la primera operacion de mi turno tras el commit del arnes**, porque si la vuelta cierra con la
suite en rojo se cumple la condicion de fallo tecnico repetido de `AUDITOR_FORJA.md` 3 **y el bucle
para**. El encargo me da la causa escrita y no la reabro: la `TAREA 4` de la vuelta 38 mando subir la
cola de `6` a `8`, **dos pruebas clavaban el `6`**, y la suite se puso en rojo **por obedecer**.

**LO QUE TOQUE, Y SOLO ESTO:** `tests/test_aceptacion.py`, las dos aseveraciones de
`PruebaColaDeDoctrina`. **Ni `src/`, ni el banco, ni los protocolos** (`D.45`). **Ni una guarda nueva**:
`7.F` de la cosecha veda arneses, guardas y lectores **nuevos**, y esto es reparar una aseveracion que
ya existia y que este bucle rompio.

| | antes | ahora |
|---|---|---|
| **la cuenta** | `assertEqual(len(cola), 6)`, una constante | `assertEqual(len(cola), len(preguntas))`, contra `config/frentes.json` |
| **que mas comprueba** | `pregunta` y `medida_en` no vacios | eso, **mas** que `bloquea` sea de verdad un `bool` y que los `n` salgan en el mismo orden que su sede |
| **el volcado** | `assertEqual(len(escritas), 6)`, otra constante | contra la misma sede, **que es lo que la regla de verdad exige**: que el tablero sirva lo que su sede tiene |
| **el nombre** | `test_la_cola_del_repo_trae_las_seis_con_su_medida` | `test_la_cola_del_repo_trae_las_de_su_sede_con_su_medida`. **Un nombre que dice `seis` es la misma constante clavada, escrita en otro sitio** |

**LA SUITE, EN VERDE Y CON SU SALIDA PEGADA:**

<!-- TALLADO: parcial salida=.v39/aceptacion_1a_tabla.txt -->

    $ python tests/test_aceptacion.py
      D.53, la cola de doctrina vive en el tablero: 5 pruebas mas
      total: 294 pruebas, 0 fallos, 0 errores

### CC.2.a. **Y LA COMPRUEBO POR MUTACION, porque una prueba que no muerde no es una prueba**

*El remedio mecanico de `D.35` aplicado a una aseveracion: **no prometo que muerde, la hago morder.***

**PRIMERA MUTACION: le quito al volcado una fila de doctrina** (el volcado dice `9`, la sede dice `10`).

<!-- TALLADO: parcial salida=.v39/mutacion_tablero.txt -->

    $ python -m unittest tests.test_aceptacion.PruebaColaDeDoctrina -v   # con el volcado mutado, una fila de doctrina menos
    ======================================================================
    FAIL: test_la_cola_esta_escrita_en_el_tablero_del_arbol (tests.test_aceptacion.PruebaColaDeDoctrina.test_la_cola_esta_escrita_en_el_tablero_del_arbol)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "C:\Users\AlexDesk\Documents\forja-nodos\tests\test_aceptacion.py", line 3850, in test_la_cola_esta_escrita_en_el_tablero_del_arbol
        self.assertEqual(len(escritas), len(self._preguntas_de_la_sede()))
    AssertionError: 9 != 10

**SEGUNDA MUTACION: le vacio el `medida_en` a la pregunta `3` de la sede.**

<!-- TALLADO: parcial salida=.v39/mutacion_medida.txt -->

    $ python -m unittest tests.test_aceptacion.PruebaColaDeDoctrina   # con la pregunta 3 de la sede sin medida_en
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "C:\Users\AlexDesk\Documents\forja-nodos\tests\test_aceptacion.py", line 3844, in test_la_cola_del_repo_trae_las_de_su_sede_con_su_medida
        self.assertTrue(fila["medida_en"], fila)
    AssertionError: '' is not true : {'tipo': 'doctrina', 'n': 3, 'pregunta': "Una cifra en denominaciones.nombre_largo que el libro no escribe: 'las cuatro conversaciones' donde L95 nombra tres. Segunda vuelta seguida con la figura, y las dos veces se registro sin cargar, porque D.30 cuenta pasos.", 'medida_en': '', 'bloquea': False, 'levantada_por': 'el auditor de la ACTA 32, linea serial, sobre la vuelta 33', 'cita': 'decision del fundador del 17 sep 2026, punto 4', 'cuando_se_resuelve': 'Se resuelven cuando el mundo 11 cierre, salvo que alguna bloquee a una linea, y entonces sube sola.'}

**Las dos mordieron y las dos se restauraron en el acto**, comprobado con `git diff --stat` sobre
`docs/loop/TABLERO.jsonl` y `config/frentes.json`: **cero lineas de diferencia tras restaurar.**

> **LO QUE ESTA REPARACION NO PUEDE COMPROBAR, Y LO DIGO YO:** que la cuenta salga de la sede significa
> que **si maniana alguien sube una pregunta a la cola, la suite NO se pone en rojo**. Eso es lo que se
> queria. **Pero tampoco se pondra en rojo si alguien BORRA una**, mientras el volcado la borre tambien.
> La prueba que faltaria para eso es una que clave un minimo, **y no la escribo**: seria la guarda nueva
> que `7.F` veda y que el encargo me prohibe por su nombre. **Queda dicho, no hecho.**

## CC.3. **TAREA 1.B: LA CIFRA QUE YA ENTRO, Y LAS DOS QUE ENTRABAN SI NO LAS TOCO**

### CC.3.a. **LA QUE YA ESTA DENTRO DEL CATALOGO**, corregida con el instrumento que existe para eso

`practicar_triangulo_critica_tres_papeles` afirma, **dentro de `dataset/nodos.jsonl`**, que ese fichero
tiene `318` nodos.

<!-- TALLADO: parcial salida=.v39/cifra_318.txt -->

    $ wc -l dataset/nodos.jsonl
    321 dataset/nodos.jsonl
    $ PYTHONIOENCODING=utf-8 python .v39/acentos.py
    nodos en dataset/nodos.jsonl                     : 321
    caracteres NO ASCII, todos                       : 169
      U+00ED LATIN SMALL LETTER I WITH ACUTE      x1
      U+00F1 LATIN SMALL LETTER N WITH TILDE      x167
      U+00FC LATIN SMALL LETTER U WITH DIAERESIS  x1
    caracteres ACENTUADOS (tilde aguda o dieresis)   : 2
      conducir_entrevista_cronologica_trayectoria    í   ...dole como creia que se medía su exito ...

**Los `318` eran los nodos de ANTES de que entraran los tres de la vuelta 38, este incluido**, asi que
el nodo se citaba a si mismo desde un arbol en el que todavia no estaba.

**LA OTRA MITAD DE LA FRASE SE SOSTIENE Y NO LA TOCO**, y la recuento yo en vez de heredarla: los
caracteres acentuados vivos siguen siendo **`2`**, la `i` con tilde de *media* y la `u` con dieresis de
*averguenza*, escritas ahi arriba con su acento porque es de lo que va la cuenta. **La enie no es
acento y por eso sus `167` apariciones quedan fuera**, que es la unica decision que este instrumento
toma y va escrita en su cabecera.

    $ python forja.py corregir --nodo practicar_triangulo_critica_tres_papeles --anade "CORRECCION DECLARADA ..." --razon "..."
    CORRECCION DECLARADA SOBRE UN NODO YA INSERTADO
      nodo : practicar_triangulo_critica_tres_papeles
      campo: resumen_teorico
      el texto viejo SIGUE ENTERO: 1951 caracteres, ninguno borrado
      se aniaden 1022 caracteres al final
      huella antes  : eec451c2e48944c6
      huella despues: 5aebf76b97831357

    GATE VERDE sobre la simulacion. CORRECCION ESCRITA EN: practicar_triangulo_critica_tres_papeles
      razon en bitacora/VEREDICTOS.jsonl

**Los veredictos suben de `486` a `487` por esta correccion**, y esa linea es la unica que mueve la
bitacora antes de la primera insercion.

### CC.3.b. **LAS DOS QUE NO HAN ENTRADO, ARREGLADAS MIENTRAS SIGUEN SIENDO BANDEJA**

**LA PRIMERA, la cifra que justifica la grafia de `P15`:**

<!-- TALLADO: parcial salida=.v39/grafia_ceo.txt -->

    $ grep -o -i "consejero delegado" dataset/nodos.jsonl | wc -l
    39
    $ grep -o -iE "\bceo\b" dataset/nodos.jsonl | wc -l
    0

**`39` contra `0`, no `36` contra `1`. La grafia que esa cifra sostiene es la buena y `P15` no se
toca**: lo que estaba mal era el numero citado para justificarla, y **hoy la sostiene con mas holgura
que entonces**, porque `ceo` no aparece ni una sola vez en el catalogo.

**LA SEGUNDA, la cifra vieja que se lee como vigente.** El campo dice *17 pasos, 17 TRANSCRIPCION, 0
PUENTE* y, unas frases despues, *DOS defectos*. **Las dos son ciertas en momentos distintos y el campo
no dice cual es cual**, que es justo la especie que ninguna guarda caza. **Lo que hubo, en orden:** la
relectura de la vuelta 38 encontro `2` `PUENTE` (`P06` y `P15`), los dos se reescribieron contra sus
lineas, y el `17 de 17` vale para el nodo **ya corregido**, no para el que se releyo.

**LAS DOS SE ARREGLAN POR ANEXION Y SIN BORRAR NADA**, que es como corrige esta casa, y **antes de que
ese campo sea `CIFRA PUBLICADA` en sede duradera** (`AUDITOR_FORJA.md` 5.2):

    $ python .v39/corregir_cand1.py
    resumen_teorico: 4764 caracteres antes, 6741 despues, 1977 aniadidos, 0 borrados

**Y UNA TERCERA QUE NO ME PIDE EL ENCARGO Y SALE DE MI PROPIA RELECTURA:** la cita de `P17` estaba
**corta**. Decia *P17 de la linea 113*, y la `113` solo trae la CUENTA (*each of the four tips for
soliciting criticism*); **los cuatro nombres que el paso escribe salen de la `237`**, que es la unica
linea del capitulo que los nombra uno a uno. **El paso no cambia: cambia su cita, que estaba
incompleta.**

    $ sed -n '237p' fuentes/scott_radical_candor/cap_13.md | cut -c1-105
    237: Now that you've practiced the four elements of soliciting criticism-coming up with a go-to question,

## CC.4. **TAREA 1.C: LA SEDE QUE NO EXISTIA, REPARADA EN LA CELDA Y SOLO EN LA CELDA**

`CIFRA PUBLICADA` esta en `1 de 2` por esto y **no lo discuto**: `config/` es sede, y una ruta ofrecida
como evidencia de una corrida que no existe es cosecha `7.B`.

<!-- TALLADO: parcial salida=.v39/frentes_1c.txt -->

    $ grep -n "BC.7" config/frentes.json
    147:        "pregunta": "Una cita medida_en que ofrece como sede una seccion que aun no se ha escrito, o un fichero que se reescribe cada vuelta. Esta cola ofrecia REPORTE.md BC.7 y BC.7 nunca se escribio; y ofrece APERTURA_CIEGA.md 13.2, que es un fichero que el arnes sobreescribe en cada vuelta. Es la pregunta 4 de esta misma cola vista desde config/.",
    $ python -c "import json; print(json.load(open(\"config/frentes.json\",encoding=\"utf-8\"))[\"cola_de_doctrina\"][\"preguntas\"][6][\"medida_en\"])"
    REPORTE.md AC.7 (vuelta 37); encargo de la vuelta 38, tarea 4.1

**`BC.7` sale de la celda `medida_en` y `AC.7` se queda**, que existe y lo compruebo:

    $ grep -n "^## AC\.7" docs/loop/REPORTE.md
    39319:## AC.7. **LA CONTRADICCION DEL LIBRO QUE LA ADUANA ME PUSO DELANTE, Y LA SUBO COMO PREGUNTA**

**LO QUE NO TOQUE:** la pregunta `7` misma, ni las otras nueve. **Y `BC.7` sigue apareciendo una vez en
el fichero**, dentro del TEXTO de la pregunta `10`, que es la que narra esta misma caida: **ahi no es
una sede ofrecida, es el relato de la sede que fallo**, y borrarlo seria borrar la caida.

**El tablero se vuelve a volcar porque yo he cambiado su sede**, que es la unica condicion con la que
el encargo lo permite (`TAREA 1.D`): `ESCRITO: 21 fila(s) en docs/loop/TABLERO.jsonl`.

## CC.5. **TAREA 1.D: LO ADJUDICADO SE RECOGE Y NO SE REABRE**

*Austero (`D.47`): lo que la `ACTA 37` ya adjudico no se vuelve a argumentar aqui. Solo lo que cambia
lo que yo hago hoy.*

| lo adjudicado | que hago con ello |
|---|---|
| mis **seis** discutibles se sostienen los seis, **cero caidas dentro del marcado** | lo recojo. **La arista `50` se cablea hoy**, porque mi adjudicacion de `BC.5.b` quedo sostenida |
| la fila de `PASOS INVENTADOS` la re firma el auditor: **`3` de `101`, `2,97` por ciento** en el tramo de la 38, y `cap_13` entero **`4` de `212`, que es un SUELO** | lo recojo, y **por eso mi fila de hoy dice TRAMO y no capitulo**, con los `212` escritos al lado (`CC.7`) |
| el `DISCUTIBLE 1` del auditor **cae contra el auditor**: `mejorar_consciencia_propia_relacional_dos_practicas` **es nodo** | lo recojo. **`CLASE` sale LIMPIA** y la cabeza de serie sigue siendo nodo, que es lo que `D.37` presupone |
| la cola de aristas: **`11` lineas, `11` cableadas, `0` con los dos extremos dentro y sin cable** | **lo recuento yo al abrir y me sale lo mismo** (`CC.0.e`). No lo heredo: lo remido |
| **`REPORTE` en `2 de 3` es la caida que SI es mia** | **no la reabro.** Su remedio entero es la `TAREA 4`, y `CC.6` queda abierta antes de la primera insercion |
| el auditor subio las preguntas `9` y `10` y volco `TABLERO.jsonl` | no lo repito. **Lo vuelvo a volcar una sola vez y solo porque yo cambie su sede** (`CC.4`) |
