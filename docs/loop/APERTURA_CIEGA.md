# APERTURA CIEGA DE LA VUELTA 1 DEL FRENTE `marquet_turn_the_ship`, escrita por el auditor ANTES de ver el reporte

*Fase ciega de `D.34.2`. Los cuatro ficheros que el arnes retira (`REPORTE.md`, `loop.log`,
`ultimo_extractor.json`, `ultimo_auditor.json`) **no se han abierto ni se han recuperado de git en
esta fase**. Lo que si he abierto, y lo digo porque es obra mia y no del extractor:
`docs/loop/ACTA_AUDITOR.md`, que es sede del auditor por `AUDITOR_FORJA.md` 5.6 y que `D.40` manda
abrir. Frente en paralelo: `D.45`, **este frente extrae y no inserta**.*

---

## 0. LA DECLARACION QUE EL ARNES EXIGE (`D.40`)

    ACTA ANTERIOR LEIDA: f6c76f63bd9b6aeea7b1d5a9d485977d2d61f593
    HEREDADO 1: CUMPLIDO
    HEREDADO 2: CUMPLIDO
    HEREDADO 3: CUMPLIDO
    HEREDADO 4: CUMPLIDO

**La huella no la copio del prompt: la recomputo aqui, en esta fase.**

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    f6c76f63bd9b6aeea7b1d5a9d485977d2d61f593

Coincide con la que el prompt me entrega, asi que la que he leido es la que se me encargo leer.

### 0.1. `HEREDADO 1`: **ninguna celda de mi apertura sellada lleva un numero que salga de una lectura mia**

**CUMPLIDO.** Toda celda numerica de este documento sale de la salida pegada de un instrumento
corrido en esta misma fase. **Mis numeros de lectura no estan en ninguna celda**: viven en la
seccion 8, en frase, marcados `LECTURA`, y su celda de tabla dice `POR ADJUDICAR`. La columna de
fidelidad de la seccion 7 es la que lo obligaba: **el denominador lo da mi censo, pero el numerador
lo pongo yo leyendo**, asi que el par entero baja a la frase.

### 0.2. `HEREDADO 2`: **la relectura ciega destapa una razon por vez, y despues de escribir mi clase a fichero**

**CUMPLIDO, y su segunda mitad no tiene poblacion en esta vuelta.** La comprobacion vigente, tal
como la `ACTA 30` `7.3` la corrigio, es que el acta publique la hora del fichero de clases y que sea
anterior a la primera corrida que **imprima una razon**:

    $ ls --time-style=full-iso -la .marquet_v1/mis_clases.txt
    -rw-r--r-- 1 AlexDesk 197609 1988 2026-09-16 22:14:41.968501700 -0400 .marquet_v1/mis_clases.txt

**Y no hay ninguna razon que destapar**, porque este frente no inserta (`D.45`) y la bitacora no
tiene ni una linea que nombre a ninguno de los nueve:

    $ python -c "cuenta de VEREDICTOS.jsonl por clave de fuente, SIN imprimir ninguna razon"
    LINEAS TOTALES EN bitacora/VEREDICTOS.jsonl        : 396
    LINEAS QUE NOMBRAN UN ID DE LA BANDEJA marquet     : 0
    IDS EN LA BANDEJA marquet_turn_the_ship            : 9
    NINGUNA RAZON IMPRESA: este comando cuenta lineas, no abre el campo razon

**Lo digo sin ensancharlo:** el remedio se cumple en su guarda (mis clases estaban escritas a
fichero antes que nada) y su cuerpo (destapar de una en una) **no se ha ejercido**, porque no habia
ninguna razon escrita contra la que ejercerlo. **Un remedio que pasa por falta de poblacion no es un
remedio probado**, y por eso va dicho aqui y no solo marcado `CUMPLIDO`.

### 0.3. `HEREDADO 3`: **toda cifra que firmo como mia la corro yo en esta vuelta**

**CUMPLIDO.** Los ocho instrumentos de la seccion 1 estan corridos **en esta fase**, con su salida
pegada, y ninguna cifra de este documento viene medida de fuera. El caso que lo pone a prueba es el
barrido de vecinos: **la vuelta anterior lo dejo en CERO BYTES** y esta vuelta lo he corrido entero
y lo publico en la seccion 5.

### 0.4. `HEREDADO 4`: **una tabla que publico como de instrumento no lleva una constante tecleada dentro**

**CUMPLIDO, y comprobado a maquina y no de palabra.** El barrido casa los ids vivos de `GRAFO MAS
BANDEJAS` contra el texto de mis cinco instrumentos:

    $ barrido de constantes tecleadas sobre MIS instrumentos
    ids vivos en GRAFO MAS BANDEJAS: 517
    barrido_vecinos.py                 ids tecleados dentro: 0   | declara en su cabecera: SI
    censo_pasos.py                     ids tecleados dentro: 0   | declara en su cabecera: SI
    denominaciones.py                  ids tecleados dentro: 0   | declara en su cabecera: SI
    mi_frontera_cap03.py               ids tecleados dentro: 0   | declara en su cabecera: SI
    poblacion_barrido.py               ids tecleados dentro: 0   | declara en su cabecera: SI

**El unico instrumento mio con una constante tecleada dentro es `mi_frontera_cap03.py`**, y la
constante es **mi propia clase por pieza**, que es justo lo que ese instrumento esta para publicar.
Usa la clausula del propio remedio y **lo dice en su primera linea**, no en una nota al pie.

---

## 1. LOS INSTRUMENTOS QUE HE CORRIDO EN ESTA FASE (`D.38.3`)

| instrumento | que mide | donde queda su salida |
|---|---|---|
| `python forja.py gate` | las trece guardas del grafo | pegada en 1.1 |
| `python forja.py guiones` | guiones largos y medios en el arbol | pegada en 1.1 |
| `python tests/test_aceptacion.py` | la bateria de aceptacion de la casa | pegada en 1.1 |
| `python .marquet_v1/poblacion_barrido.py` | mi poblacion contra la que mide la casa | `.marquet_v1/poblacion_barrido.txt` |
| `python .marquet_v1/mi_frontera_cap03.py` | mi frontera de `cap_03`, cerrada al digito | `.marquet_v1/mi_frontera_cap03.txt` |
| `python .marquet_v1/censo_pasos.py` | pasos, unidad y lineas declaradas de los nueve | `.marquet_v1/censo_pasos.txt` |
| `python .marquet_v1/denominaciones.py` | si cada termino extranjero esta en su propia unidad | `.marquet_v1/denominaciones.txt` |
| `python .marquet_v1/barrido_vecinos.py` | el barrido `D.38.4` sobre `GRAFO MAS BANDEJAS` | `.marquet_v1/informe_nueve.txt` |

### 1.1. Las tres guardas de la casa, corridas por mi

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 270
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python tests/test_aceptacion.py
      total: 201 pruebas, 0 fallos, 0 errores

### 1.2. **UN INSTRUMENTO MIO QUE HE TENIDO QUE ARREGLAR EN ESTA FASE, Y LO DIGO**

`censo_pasos.py` sacaba las lineas declaradas con la expresion `linea[s]?` mas digitos, que **solo
caza la forma `linea 29` y no la forma `L27`**. Las correcciones de frontera de esta vuelta estan
escritas en la segunda forma, asi que la columna se dejaba fuera **justo las lineas que importan**,
mientras su rotulo prometia todas las lineas citadas. Queda cazando las dos formas.

**Y lo que la columna mide sigue sin ser exactamente lo que su rotulo sugiere**, asi que lo escribo
aqui en vez de dejarlo a la interpretacion del que lea: mide **todo numero en forma de linea que
aparezca en el `resumen_teorico`**, referencias cruzadas incluidas. Por eso `cambiar_forma` sale con
un `51` que no es de su frontera: es la mencion del `L51` del otro candidato de `cap_02`.

---

## 2. MI FRONTERA CIEGA DE `cap_03`, CERRADA AL DIGITO

    $ python .marquet_v1/mi_frontera_cap03.py
    AVISO: este instrumento LLEVA UNA CONSTANTE TECLEADA DENTRO, y es MI CLASE
           por pieza (el diccionario MI_CLASE). Los numeros de linea, las palabras
           y la cobertura salen del fichero.

    fichero                        : fuentes/marquet_turn_the_ship/cap_03.md
    primera linea de cuerpo        : L8 (tras el segundo --- del preambulo)
    lineas con contenido en cuerpo : 37

    SUMA DE LAS FILAS            : 1978 palabras
    wc -w DEL CUERPO (L8 en adelante, lineas con contenido) : 1978
    CIERRA                       : SI
    LINEAS DE CUERPO SIN CLASE MIA : 0 []

    MI REPARTO
      piezas P (yo escribiria nodo) : 18, 1424 palabras
      piezas R (residuo)            : 19, 554 palabras

La tabla pieza por pieza, con sus primeras palabras, esta entera en
`.marquet_v1/mi_frontera_cap03.txt`.

### 2.1. El cruce de mi frontera contra lo que los seis candidatos de `cap_03` declaran

    $ cruce de MI frontera contra las lineas que los candidatos de cap_03 declaran
    MIS PIEZAS P DE cap_03 : 18 [11, 15, 19, 21, 23, 25, 27, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57]
    MIS PIEZAS R DE cap_03 : 19 [9, 13, 17, 29, 31, 33, 35, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81]
    LINEAS QUE LOS 6 CANDIDATOS DE cap_03 DECLARAN : 20 [11, 15, 17, 19, 21, 23, 25, 27, 29, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57]

    P MIAS QUE NINGUN CANDIDATO DECLARA : []
    LINEAS DECLARADAS QUE YO CLASIFIQUE R : [17, 29]
    LINEAS DECLARADAS QUE NO EXISTEN EN MI FRONTERA : []

      auditar_formacion_premios_ultima_fila          [55, 57]
      contar_firmas_cadena_tramite_parado            [37, 39, 41, 43]
      inspeccionar_reparto_informacion_notas_jefe    [45, 47, 49, 51, 53]
      observar_reunion_rutinaria_senales_plantilla   [17, 19, 21]
      recorrer_organizacion_escuchar_plantilla       [11, 15]
      seguir_frustrado_preguntar_implantacion_ideas  [23, 25, 27, 29]

**`LECTURA`: mi frontera y el corte del capitulo coinciden pieza por pieza.** Las dieciocho piezas
que yo mineria estan las dieciocho declaradas, **cada una por un solo candidato**; ningun candidato
declara una linea que no exista en mi frontera; y las dos lineas de residuo que se declaran (`L17` y
`L29`) son exactamente las dos que sus candidatos declaran a la cara como venidas de pieza no
minada, con su motivo escrito al lado. Lo que sostiene esta lectura es la salida de arriba.

---

## 3. EL CORTE DE LA BANDEJA CON EL QUE TRABAJO

**La bandeja se movio mientras yo la media**, asi que el corte va con huella y con hora, y es el de
esta fase y no el de antes:

    $ (cd cuarentena/marquet_turn_the_ship && for f in *.json; do echo "$(git hash-object "$f")  $(date -r "$f" "+%Y-%m-%d %H:%M:%S")  $f"; done)
    319bc9d6deef958f82c184dad90778f7a4127a54  2026-09-16 21:24:01  auditar_formacion_premios_ultima_fila.json
    36cfd9d6f74ca02d7b7d5c69aa49a030131475c0  2026-09-16 21:33:20  cambiar_forma_trabajar_conservar_plantilla.json
    d3d72f7548cbbd043acb6f2ce5d61bc922d36dd2  2026-09-16 20:47:10  ceder_control_reforzar_competencia_claridad.json
    71426b3f58e9b0293ee59df6fadde0accf36582e  2026-09-16 21:13:34  contar_firmas_cadena_tramite_parado.json
    cda982ac44e84ff2674b793e022ec0f100dd8e9e  2026-09-16 21:24:01  encargar_meta_especifica_dejar_libre_metodo.json
    34ea4932a90ef3f5812b9f4e9e4aba0cff6b84ac  2026-09-16 21:14:15  inspeccionar_reparto_informacion_notas_jefe.json
    9d6356c978a80cd5eaaa486f0293651eae0aee8d  2026-09-16 21:12:13  observar_reunion_rutinaria_senales_plantilla.json
    fdda3b318a856b52923cbbfcf2fa9c91146efa21  2026-09-16 21:12:13  recorrer_organizacion_escuchar_plantilla.json
    33921de02e1c2bf027d89e5c03852b848fb3e77d  2026-09-16 21:12:56  seguir_frustrado_preguntar_implantacion_ideas.json

**Nueve en la bandeja y seis de `cap_03`.** Los otros tres son de `cap_01` y `cap_02` y estaban ahi
antes de esta vuelta; dos de ellos llevan hora de hoy porque esta vuelta los ha vuelto a tocar, y de
eso trata la seccion 9.1.

---

## 4. MI CENSO DE PASOS DE LOS NUEVE

    $ python .marquet_v1/censo_pasos.py cuarentena/marquet_turn_the_ship
    BANDEJA cuarentena/marquet_turn_the_ship : 9 candidatos

    id                                                   unidad       pasos  den fecha      lineas citadas en el resumen
    auditar_formacion_premios_ultima_fila                cap_03.md       11    2 2026-09-16 [55, 57]
    cambiar_forma_trabajar_conservar_plantilla           cap_02.md        5    2 2026-09-13 [25, 27, 29, 51]
    ceder_control_reforzar_competencia_claridad          cap_01.md        7    4 2026-09-13 [97]
    contar_firmas_cadena_tramite_parado                  cap_03.md       10    2 2026-09-16 [37, 39, 41, 43]
    encargar_meta_especifica_dejar_libre_metodo          cap_02.md        5    2 2026-09-13 [33, 49, 51]
    inspeccionar_reparto_informacion_notas_jefe          cap_03.md        8    2 2026-09-16 [45, 47, 49, 51, 53]
    observar_reunion_rutinaria_senales_plantilla         cap_03.md        9    2 2026-09-16 [17, 19, 21]
    recorrer_organizacion_escuchar_plantilla             cap_03.md        7    2 2026-09-16 [11, 15]
    seguir_frustrado_preguntar_implantacion_ideas        cap_03.md        8    2 2026-09-16 [23, 25, 27, 29]

    PASOS ESCRITOS EN LA BANDEJA: 70
      cap_01.md         7 pasos
      cap_02.md        10 pasos
      cap_03.md        53 pasos

**Lo que este instrumento mide es lo que la frase dice y nada mas:** cuenta elementos de
`pasos_accionables`, lee la unidad de la cabecera del `resumen_teorico` y recoge los numeros de
linea que ese resumen escribe. **No dice si un paso es transcripcion o puente**: eso lo leo yo y va
en la seccion 8.

### 4.1. Los terminos extranjeros, comprobados contra su propia unidad

    $ python .marquet_v1/denominaciones.py cuarentena/marquet_turn_the_ship
    TERMINOS COMPROBADOS                          : 20
    TERMINOS QUE NO APARECEN EN SU PROPIA UNIDAD  : 0

La tabla termino por termino, con las lineas donde cada uno aparece, esta en
`.marquet_v1/denominaciones.txt`.

---

## 5. MI BARRIDO DE VECINOS, `D.38.4`, SOBRE `GRAFO MAS BANDEJAS`

**Es el instrumento que la vuelta anterior dejo en cero bytes.** A 0,94 segundos por par medidos en
esta misma fase, los 4.644 pares pedian 73 minutos en serie, y por eso la salida se quedaba vacia.
El bucle va ahora repartido en procesos. **Ni una senial nueva ni un umbral tocado:** por dentro
sigue llamando a `src.aduana.medir`, que es lo que `src.aduana.buscar_vecinos` llama.

    $ python .marquet_v1/barrido_vecinos.py cuarentena/marquet_turn_the_ship
    POBLACION DEL BARRIDO (D.38.4)
      grafo dataset/nodos.jsonl : 270
      bandejas cuarentena/*/    : 247
      TOTAL                     : 517
      umbrales: sim 0.35 | fam 0.3 | paso 0.6

    candidatos a barrer en cuarentena/marquet_turn_the_ship: 9 (todos los de la carpeta, sin lista teclada)
    pares a medir: 4644

    ### auditar_formacion_premios_ultima_fila.json   (contra 516)
        vecino observar_reunion_rutinaria_senales_plantilla  [levantada por: similitud_texto]
          similitud_texto 0.37 | familia_id 0.0 | paso_contra_nodo 0.489
        vecino recorrer_organizacion_escuchar_plantilla  [levantada por: similitud_texto]
          similitud_texto 0.353 | familia_id 0.0 | paso_contra_nodo 0.462

    ### cambiar_forma_trabajar_conservar_plantilla.json   (contra 516)
        vecino escuchar_entender_critica_dominar_defensa  [levantada por: paso_contra_nodo]
          similitud_texto 0.201 | familia_id 0.0 | paso_contra_nodo 0.612
          paso 2 del candidato contra paso 4 de escuchar_entender_critica_dominar_defensa
        vecino encargar_meta_especifica_dejar_libre_metodo  [levantada por: similitud_texto]
          similitud_texto 0.441 | familia_id 0.0 | paso_contra_nodo 0.455

    ### ceder_control_reforzar_competencia_claridad.json   (contra 516)
        vecino encargar_meta_especifica_dejar_libre_metodo  [levantada por: similitud_texto]
          similitud_texto 0.434 | familia_id 0.0 | paso_contra_nodo 0.486

    ### contar_firmas_cadena_tramite_parado.json   (contra 516)
        vecino seguir_frustrado_preguntar_implantacion_ideas  [levantada por: similitud_texto]
          similitud_texto 0.388 | familia_id 0.0 | paso_contra_nodo 0.463
        vecino inspeccionar_reparto_informacion_notas_jefe  [levantada por: similitud_texto]
          similitud_texto 0.36 | familia_id 0.0 | paso_contra_nodo 0.405

    ### encargar_meta_especifica_dejar_libre_metodo.json   (contra 516)
        vecino ceder_control_reforzar_competencia_claridad  [levantada por: similitud_texto]
          similitud_texto 0.439 | familia_id 0.0 | paso_contra_nodo 0.473
        vecino cambiar_forma_trabajar_conservar_plantilla  [levantada por: similitud_texto]
          similitud_texto 0.436 | familia_id 0.0 | paso_contra_nodo 0.459
        vecino recorrer_organizacion_escuchar_plantilla  [levantada por: similitud_texto]
          similitud_texto 0.412 | familia_id 0.0 | paso_contra_nodo 0.416

    ### inspeccionar_reparto_informacion_notas_jefe.json   (contra 516)
        vecino observar_reunion_rutinaria_senales_plantilla  [levantada por: similitud_texto]
          similitud_texto 0.358 | familia_id 0.0 | paso_contra_nodo 0.452
        vecino contar_firmas_cadena_tramite_parado  [levantada por: similitud_texto]
          similitud_texto 0.379 | familia_id 0.0 | paso_contra_nodo 0.428

    ### observar_reunion_rutinaria_senales_plantilla.json   (contra 516)
        vecino seguir_frustrado_preguntar_implantacion_ideas  [levantada por: similitud_texto]
          similitud_texto 0.358 | familia_id 0.0 | paso_contra_nodo 0.466
        vecino auditar_formacion_premios_ultima_fila  [levantada por: similitud_texto]
          similitud_texto 0.361 | familia_id 0.0 | paso_contra_nodo 0.463
        vecino recorrer_organizacion_escuchar_plantilla  [levantada por: similitud_texto]
          similitud_texto 0.414 | familia_id 0.125 | paso_contra_nodo 0.435
        vecino inspeccionar_reparto_informacion_notas_jefe  [levantada por: similitud_texto]
          similitud_texto 0.367 | familia_id 0.0 | paso_contra_nodo 0.406

    ### recorrer_organizacion_escuchar_plantilla.json   (contra 516)
        vecino observar_reunion_rutinaria_senales_plantilla  [levantada por: similitud_texto]
          similitud_texto 0.42 | familia_id 0.125 | paso_contra_nodo 0.437
        vecino encargar_meta_especifica_dejar_libre_metodo  [levantada por: similitud_texto]
          similitud_texto 0.401 | familia_id 0.0 | paso_contra_nodo 0.426
        vecino inspeccionar_reparto_informacion_notas_jefe  [levantada por: similitud_texto]
          similitud_texto 0.352 | familia_id 0.0 | paso_contra_nodo 0.383

    ### seguir_frustrado_preguntar_implantacion_ideas.json   (contra 516)
        vecino observar_reunion_rutinaria_senales_plantilla  [levantada por: similitud_texto]
          similitud_texto 0.372 | familia_id 0.0 | paso_contra_nodo 0.468
        vecino contar_firmas_cadena_tramite_parado  [levantada por: similitud_texto]
          similitud_texto 0.39 | familia_id 0.0 | paso_contra_nodo 0.441

La salida entera, con la linea de `detalle_paso` de cada vecino, esta en
`.marquet_v1/informe_nueve.txt`.

### 5.1. El recuento del barrido, leido de su propia salida y no a ojo

    $ recuento de MI barrido, leido de mi propia salida .marquet_v1/informe_nueve.txt
    CANDIDATOS BARRIDOS                : 9
    VECINOS LEVANTADOS, TOTAL          : 21
      con el vecino DENTRO de la bandeja marquet : 20
      con el vecino FUERA de la bandeja          : 1
    POR SENIAL QUE LOS LEVANTA         : {'similitud_texto': 20, 'paso_contra_nodo': 1}
    CANDIDATOS SIN NINGUN VECINO       : 0

Y la sede de cada uno de esos veintiun vecinos, que es la mitad que decide:

    $ de donde sale cada vecino que mi barrido levanta: grafo, bandeja marquet, u otra bandeja
      BANDEJA marquet_turn_the_ship              20
      BANDEJA scott_radical_candor               1

      ids de ensayo_referencia_163 que levantan algun vecino : 0
      vecinos que son nodos del GRAFO                        : 0

**`LECTURA`, y es la que mas me importa de toda esta fase: NINGUNO DE LOS VEINTIUN VECINOS ES UN NODO
DEL GRAFO.** Barridos los nueve candidatos contra los `270` nodos vivos mas las bandejas enteras, **el
grafo no levanta ni una senial contra ninguno de ellos**, ni de texto, ni de familia de id, ni de
paso. Los veinte de dentro de la propia bandeja estan todos apenas por encima del umbral de texto,
que es lo que cabe esperar de nueve nodos escritos con la misma mano sobre el mismo libro. Y el unico
que cruza la frontera del libro es tambien **el unico que pasa el umbral de paso**, que es el mas
exigente de los tres: de ese trata la seccion 9.2.

---

## 6. LA POBLACION: MI CIFRA CONTRA LA QUE MIDE LA CASA (`D.38.5`)

    $ python .marquet_v1/poblacion_barrido.py
    TODOS LOS .json BAJO cuarentena/ : 515
        _insertados                   268
        ensayo_referencia_163         163
        marquet_turn_the_ship           9
        scott_radical_candor           75

    CARPETAS FUERA DE POBLACION (aduana.CARPETAS_FUERA_DE_POBLACION) : _insertados, _derivadas
    POBLACION DE BANDEJAS QUE LA CASA MIDE (aduana.poblacion_de_bandejas) : 84
    GRAFO dataset/nodos.jsonl : 270
    POBLACION DEL BARRIDO D.38.4 = GRAFO MAS BANDEJAS : 354

**AQUI HAY UNA DISCREPANCIA Y LA DECLARO EN VEZ DE RESOLVERLA COPIANDO** (`AUDITOR_FORJA.md` 1.1).
Mi barrido de la seccion 5 dice `517` y este instrumento dice que la casa mide `354`. **La diferencia
son 163 y tiene nombre**: la carpeta `cuarentena/ensayo_referencia_163/`, cuyos ficheros llevan claves
de fuente que **no estan en `fuentes/FUENTES_CANONICAS.json`**, y la casa los descarta por su tabla de
fuentes y no por su nombre de carpeta.

**Es discrepancia de metodo y no de dato, y por eso no la cargo a nadie.** `D.38.4` manda barrer
`dataset/nodos.jsonl` **mas todo lo que espera en `cuarentena/<libro>/`**, descartando `_insertados` y
`_derivadas`, y eso al pie de la letra da `517`. La aduana ademas filtra por tabla canonica, y eso da
`354`. **He barrido con la poblacion ancha, que es la que no puede dejarse un vecino fuera**, y el
resultado no cambia por ello, **que es lo unico que me deja decir que la discrepancia no me ha costado
un hallazgo**: la salida de la seccion 5.1 dice que los `163` de la carpeta de ensayo **levantan cero
vecinos**, y que los veintiuno salen todos de `marquet` y de `scott`. Si la poblacion estrecha fuera
la buena, mi barrido habria medido `163` nodos de mas **y habria encontrado exactamente lo mismo**.

**Lo que si queda por adjudicar, y va a mi turno normal**, es cual de las dos poblaciones es la que
`D.38.5` quiso hacer comparables, porque hoy **no lo son**: si la respuesta es la estrecha, mi barrido
mide de mas y hay que decirlo en el banco; si es la ancha, la que mide de menos es la aduana.

**Y UNA CORRIDA QUE LANCE Y NO LLEGO, DICHA AQUI PARA QUE NO SE CUENTE COMO PRUEBA.** Lance ademas
`python forja.py informe` sobre `cambiar_forma_trabajar_conservar_plantilla.json`, la aduana **en
seco**, para cruzar mi cuenta de vecinos contra la suya sobre el mismo candidato. **No habia
terminado al cerrar esta fase**, asi que la he parado y **he borrado su fichero de salida en vez de
dejarlo en cero bytes**: una ruta que promete prueba y apunta a un fichero vacio es caida de cifra
(cosecha `7.B`), y la manera de no cometerla no es no citarla, es no dejarla ahi. **La cifra de la
casa que publico arriba no viene de esa corrida**: viene de `aduana.poblacion_de_bandejas`, que es la
funcion de la casa, leida en directo por mi instrumento. **El cruce candidato a candidato queda
pendiente y lo encargo en mi turno normal.**

---

## 7. MIS CLASES, CANDIDATO A CANDIDATO

**Todas las cifras de esta tabla salen del censo de la seccion 4 y del barrido de la seccion 5.**
La columna de fidelidad lleva `POR ADJUDICAR` a proposito: **su cuenta sale de mi lectura**, asi que
vive en la seccion 8 y no en una celda (`HEREDADO 1`).

La columna `pasos` es la del censo de la seccion 4. La columna `vecinos` **no la cuento yo mirando el
barrido**, que seria exactamente lo que `HEREDADO 1` prohibe: la cuenta el instrumento sobre su propia
salida, y es esta:

    $ vecinos por candidato, contados sobre mi propia salida
      auditar_formacion_premios_ultima_fila          2
      cambiar_forma_trabajar_conservar_plantilla     2
      ceder_control_reforzar_competencia_claridad    1
      contar_firmas_cadena_tramite_parado            2
      encargar_meta_especifica_dejar_libre_metodo    3
      inspeccionar_reparto_informacion_notas_jefe    2
      observar_reunion_rutinaria_senales_plantilla   4
      recorrer_organizacion_escuchar_plantilla       3
      seguir_frustrado_preguntar_implantacion_ideas  2
      TOTAL                                          21

| # | candidato | unidad | pasos | vecinos | MI CLASE | MI FIDELIDAD `D.30` | MI VECINDAD |
|---|---|---|---|---|---|---|---|
| 1 | `recorrer_organizacion_escuchar_plantilla` | `cap_03.md` | 7 | 3 | **PROCEDIMIENTO** | SOSTIENE, cuenta `POR ADJUDICAR` | **NUEVO** |
| 2 | `observar_reunion_rutinaria_senales_plantilla` | `cap_03.md` | 9 | 4 | **PROCEDIMIENTO** | SOSTIENE, cuenta `POR ADJUDICAR` | **NUEVO** |
| 3 | `seguir_frustrado_preguntar_implantacion_ideas` | `cap_03.md` | 8 | 2 | **PROCEDIMIENTO** | SOSTIENE, cuenta `POR ADJUDICAR` | **NUEVO** |
| 4 | `contar_firmas_cadena_tramite_parado` | `cap_03.md` | 10 | 2 | **PROCEDIMIENTO** | SOSTIENE, cuenta `POR ADJUDICAR` | **NUEVO** |
| 5 | `inspeccionar_reparto_informacion_notas_jefe` | `cap_03.md` | 8 | 2 | **PROCEDIMIENTO** | SOSTIENE, cuenta `POR ADJUDICAR` | **NUEVO** |
| 6 | `auditar_formacion_premios_ultima_fila` | `cap_03.md` | 11 | 2 | **PROCEDIMIENTO** | SOSTIENE, cuenta `POR ADJUDICAR` | **NUEVO**, y es mi par mas proximo con el 2 |
| 7 | `ceder_control_reforzar_competencia_claridad` | `cap_01.md` | 7 | 1 | **PROCEDIMIENTO CON RESERVA EN SU PASO 1** | SOSTIENE, cuenta `POR ADJUDICAR` | **NUEVO** |
| 8 | `cambiar_forma_trabajar_conservar_plantilla` | `cap_02.md` | 5 | 2 | **PROCEDIMIENTO** | SOSTIENE con **FRONTERA INCOMPLETA**, `POR ADJUDICAR` | **NUEVO** |
| 9 | `encargar_meta_especifica_dejar_libre_metodo` | `cap_02.md` | 5 | 3 | **PROCEDIMIENTO** | SOSTIENE con **FRONTERA INCOMPLETA**, `POR ADJUDICAR` | **NUEVO** |

**Ninguno de los nueve lo leo como repeticion de nada.** Ni de otro de la bandeja, ni de un nodo del
grafo. Los seis de `cap_03` salen de seis escenas distintas del mismo capitulo, con objetos de
trabajo distintos y entregables distintos, y el barrido no levanta contra el grafo ni una sola senial
de texto ni de familia.

---

## 8. MIS LECTURAS, EN FRASE Y MARCADAS, CON SUS CUENTAS FUERA DE TODA CELDA

**`LECTURA` 1, la fidelidad `D.30` de los nueve, releida paso por paso contra su linea del libro:**
los setenta pasos de la bandeja me salen **setenta TRANSCRIPCION y cero PUENTE**, repartidos asi:
siete de siete en el 1, nueve de nueve en el 2, ocho de ocho en el 3, diez de diez en el 4, ocho de
ocho en el 5, once de once en el 6, siete de siete en el 7, cinco de cinco en el 8 y cinco de cinco
en el 9. **El denominador de cada uno es del censo de la seccion 4; el numerador es mio.**

**`LECTURA` 2, los pasos de `cap_03`:** los cincuenta y tres pasos del capitulo me salen **cero
inventados**, asi que la cifra de `PASOS INVENTADOS POR CAPITULO` de `AUDITOR_FORJA.md` 8 que yo
firmaria para `cap_03` es **cero por ciento**, por debajo del tope de diez. **No la publico como
cifra de acta todavia**: el numerador es una lectura mia y la seccion 8.3 me obliga a contrastarla
contra el desglose del reporte, que en esta fase no he visto.

**`LECTURA` 3, los cuatro pasos que mas trabajo me han costado sostener**, y los dejo nombrados para
que el siguiente lector los ataque:

1. **`contar_firmas` paso 5**, la cadena de siete puestos. El libro nombra `department chief` y
   `department head` como dos puestos distintos y los dos se dicen *jefe de departamento*; el paso
   los transcribe los dos, en el orden del texto, y lo dice. **Lo sostengo**, y la cuenta de siete
   es del libro (*Seven people!*) y no aritmetica de nadie.
2. **`auditar_formacion` paso 9**, que arrastra la valoracion del autor sobre el fotografo que
   faltaba. **Lo sostengo** porque la valoracion es del libro y va citada como suya.
3. **`inspeccionar_reparto` pasos 7 y 8**, que empiezan por *quedate con*. **Los sostengo** porque
   sin ellos el nodo se queda en la pregunta sin su respuesta.
4. **`observar_reunion` paso 1**, cuya activacion sale de una pieza que yo mismo clasifico residuo.
   **Lo sostengo**: la pieza es residuo por su cuerpo y su primera frase nombra la reunion.

**Los cuatro los marca el propio candidato como discutibles antes de saber si acertaba**, y eso es
exactamente lo que `AUDITOR_FORJA.md` 5.1 dice que hace informativa a la metrica.

---

## 9. LO QUE MI LECTURA CIEGA CAZA

### 9.1. En la bandeja: **dos fronteras dentro del nodo que declaraban de menos, y una reserva**

1. **`encargar_meta_especifica_dejar_libre_metodo`, paso 2.** Su glosa (*es lo que separa este
   encargo de la microgestion*) **no sale de `L49`, que es la linea que su resumen declara**: sale de
   `L51`, donde el autor escribe que su jefe no iba a hacerle microgestion. Lo compruebo abriendo las
   dos lineas y no de memoria:

        $ sed -n "49p;51p" fuentes/marquet_turn_the_ship/cap_02.md
        Upon reflection, Commodore Kenny was providing great leadership. He presented me with a specific goal-have Santa Fe ready for deployment in every way-but did not tell me how to do it. [...]
        Then I began to reconsider the situation. Since Mark wasn't going to micromanage me, maybe this was a chance to do something different. [...]

   **`L49` no contiene la palabra.** **NO ES PUENTE**: la linea existe, es del libro y es de la misma
   unidad. **Es FRONTERA INCOMPLETA**, que es otra especie, y se arregla declarando la linea.

2. **`cambiar_forma_trabajar_conservar_plantilla`, paso 4.** El paso dice *el mensaje que manda no
   despedir a nadie*, y **que no despidiera a nadie no esta en `L29`**, que es la linea que su
   resumen declaraba para ese paso: esta en `L27`.

        $ sed -n "25p;27p;29p" fuentes/marquet_turn_the_ship/cap_02.md
        "Look, here's the deal. If you need to change out some people, let me know, but I'm not interested in a lot of turnover. [...]"
        I was thinking that too. In the end, I fired no one.
        This was important because it sent the message to each crew member that he wasn't screwed up, the leadership was. [...]

   **`L29` trae el mensaje; `L27` trae la decision de no despedir a nadie.** El paso se apoya en las
   dos y declaraba una. **Misma especie que el punto 1: FRONTERA INCOMPLETA, no puente.** La frontera
   dentro del nodo queda en pasos 1 a 3 de `L25`, paso 4 de `L27` mas `L29`, paso 5 de `L29`.

3. **`ceder_control_reforzar_competencia_claridad`, paso 1: MI RESERVA, y no es de fidelidad.** El
   paso es transcripcion limpia de `L97`, asi que como fidelidad **se sostiene**. Lo que pongo en duda
   es que sea un **paso accionable**: lo que dice es **como reparte el libro sus propias Partes** (la
   primera fase en la Parte I, el puente y los pilares en las Partes II, III y IV). **Eso es la
   disposicion del libro, no algo que el lector ejecute en su organizacion.**

        $ sed -n "97p" fuentes/marquet_turn_the_ship/cap_01.md
        Turn the Ship Around! is the story of that journey and the men aboard Santa Fe who lived it with me. It describes essentially four phases in my struggle to change the way we interacted for the better. I describe how I needed to let go of old ideas to make room for new ones in Part I. In Parts II, III, and IV, I describe the bridge to leader-leader and supporting pillars. [...]

   **Es una reserva y no una caida**, y la traigo a mi turno normal: los otros seis pasos del nodo si
   son operaciones del lector, y el nodo entero no se cae por su primer paso. **Pero un paso que
   describe el indice del libro no es el mismo animal que los otros seis**, y si nadie lo dice viaja.

### 9.2. En la maquina: **el unico vecino que cruza el libro lo levanta una muletilla del extractor**

El vecino mas fuerte de todo mi barrido, y el unico por encima del umbral de paso, es este:

    vecino escuchar_entender_critica_dominar_defensa  [levantada por: paso_contra_nodo]
      similitud_texto 0.201 | familia_id 0.0 | paso_contra_nodo 0.612
      paso 2 del candidato contra paso 4 de escuchar_entender_critica_dominar_defensa

Y los dos pasos que la senial empareja son estos:

    $ cuenta de la formula de glosa del extractor en pasos, sobre GRAFO MAS BANDEJAS
    GRAFO dataset/nodos.jsonl    pasos  2181 | con "que es lo que el texto"   19 | y ademas "por encima de"   0
    BANDEJAS cuarentena/*/       pasos  1887 | con "que es lo que el texto"   58 | y ademas "por encima de"   2

    LOS PASOS QUE LLEVAN LAS DOS COSAS:
      cambiar_forma_trabajar_conservar_plantilla     paso  2 | Centrate en trabajar con lo que tienes, que es lo que el texto recomienda por encima de mucha rotacion.
      escuchar_entender_critica_dominar_defensa      paso  4 | Y sobre todo practica con otros, que es lo que el texto pone por encima de lo demas.

**`LECTURA`: no son el mismo nodo ni se parecen en nada.** Uno dice *trabaja con la tripulacion que
tienes en vez de rotar gente* y sale de Marquet; el otro dice *practica el ejercicio de escuchar tres
minutos con una pareja* y sale de Scott. **Distinto libro, distinta activacion, distinto entregable.**
Lo unico que comparten es **la muletilla de glosa del extractor**: *que es lo que el texto \<verbo\>
por encima de*. La senial dijo donde mirar y ahi acabo su trabajo, que es lo que `D.19` dice que hace
una senial.

**LO QUE ME PREOCUPA NO ES ESTE PAR, QUE ES INOFENSIVO: ES QUE LA FORMULA ESCALA.** Los dos unicos
pasos de toda la poblacion que llevan las dos mitades de la muletilla son exactamente los dos que la
aduana ha emparejado. **Y la mitad larga va a mas**: `58` de `1887` pasos en las bandejas contra `19`
de `2181` en el grafo, que es **mas del triple de densidad en lo que aun no ha entrado**. Cada nodo
nuevo con la muletilla es un candidato a levantar un vecino falso contra todos los demas que la
lleven, y eso **no lo caza ninguna guarda**, porque la aduana esta midiendo de verdad lo que le
pidieron medir. **Va a mi turno normal como propuesta, no como caida:** aqui no adjudico.

### 9.3. **UNA ANOMALIA DE PROCEDIMIENTO QUE NO PUEDO RESOLVER EN ESTA FASE, Y QUE POR ESO DECLARO**

El fichero `cuarentena/marquet_turn_the_ship/cambiar_forma_trabajar_conservar_plantilla.json`, sin
commitear, **ya contiene escrito que el hallazgo del punto 2 de arriba es mio y cita su direccion**:

> *EL HALLAZGO NO ES MIO: LO CAZO LA APERTURA CIEGA DEL AUDITOR DE ESTA MISMA VUELTA
> (`docs/loop/APERTURA_CIEGA.md` seccion 9.1 punto 2)*

**Y `docs/loop/APERTURA_CIEGA.md` no estaba en el arbol cuando yo he empezado esta fase**, ni hay
sello registrado despues de las `19:01:13` de hoy:

    $ tail -3 docs/loop/SELLOS_APERTURA.jsonl
    {"vuelta": 2, "fecha": "2026-09-16 10:41:02", "sello": "2f326b1b60e28a42ed21a96ce2bf967d9d20208b"}
    {"vuelta": 1, "fecha": "2026-09-16 16:16:54", "sello": "406ca90e54a2097d3f8371f01346b48a5d377d51"}
    {"vuelta": 2, "fecha": "2026-09-16 19:01:13", "sello": "480d3b91340f63988cb1fb028d50106fee142ac2"}

**LO QUE HAGO CON ESO, Y POR QUE.** El hallazgo lo he verificado yo, en esta fase, abriendo `L27` con
su `sed` y no de memoria, **antes de leer esa cita**; es correcto, y lo dejo escrito en la direccion
que la cita promete, **porque una ruta que promete prueba tiene que resolver** (cosecha `7.B`). **Lo
que no hago es cargarlo como caida de cifra**: la sede es un `resumen_teorico` de `cuarentena/`, que
no es ninguna de las sedes de `AUDITOR_FORJA.md` 5.2 ni el reporte. **Y lo que no puedo decidir aqui
es como una fase que se llama ciega termina citada por dentro del material que viene a leer a
ciegas.** Eso es cuestion de arquitectura del arnes, **es del fundador por `D.45`**, y sube.

---

## 10. LO QUE NO HE ABIERTO, DICHO PARA QUE SE PUEDA COMPROBAR

**Los cuatro de `D.34.2`**: `docs/loop/REPORTE.md`, `docs/loop/loop.log`,
`docs/loop/ultimo_extractor.json` y `docs/loop/ultimo_auditor.json`. No estaban en el arbol y **no los
he recuperado de git ni por ninguna otra via**.

**Y tampoco los papeles de trabajo del extractor de esta vuelta**, que no son de los cuatro pero
serian su lectura y no la mia: `.vm01/razones.txt`, `.vm01/clases.txt`, `.vm01/contraste.txt`,
`.vm01/informe_lote.txt`, `.vm01/fidelidad_lote.txt`, `.vm01/retirados.txt` y la carpeta
`.vm01/aduana/`. **Lo unico del arbol del extractor que he abierto son los nueve candidatos y el
diff de la bandeja**, que es el material que esta fase manda abrir.

**Lo que si he abierto, y lo repito porque tres vueltas se comportaron como si estuviera prohibido**:
`docs/loop/ACTA_AUDITOR.md`, que es obra mia.

---

## 11. EL CIERRE DE LA PAGINA, MEDIDO A LA HORA DEL SELLO

> ### **ESTA SECCION LA ESCRIBE UNA SEGUNDA FASE CIEGA QUE EL ARNES ABRIO ENCIMA DE LA PRIMERA, SOBRE ESTE MISMO ARBOL Y SIN CERRAR LA ANTERIOR. NO HE BORRADO NI UNA LINEA DE LO QUE YA ESTABA: LO HE VUELTO A MEDIR Y LO FIRMO.**

**POR QUE SE QUEDA TODO LO DE ARRIBA Y NO LO REESCRIBO.** Las secciones `0` a `10` son la lectura
ciega del auditor de esta misma vuelta, sobre esta misma bandeja, hecha antes de ver el reporte.
Reescribirlas de cero habria destruido trabajo verificado para poner en su sitio un duplicado.
**Lo que si me toca, por `HEREDADO 3`, es no firmar ninguna cifra que no haya corrido yo**, y eso es
lo que hace esta seccion.

### 11.1. Lo que el arnes hizo mientras esta pagina estaba viva, con su salida

`docs/loop/ultimo_apertura.json` se vacio a las `22:25:08`, que es lo que `apertura_ciega()` hace al
empezar una fase nueva, y los cuatro de `D.34.2` volvieron a salir del arbol:

    $ date '+%H:%M:%S'; ls -la --time-style=full-iso docs/loop/ultimo_apertura.json
    22:27:56
    -rw-r--r-- 1 AlexDesk 197609 0 2026-09-16 22:25:08.727878900 -0400 docs/loop/ultimo_apertura.json

    $ git status --porcelain docs/loop/ | grep '^ D'
     D docs/loop/REPORTE.md
     D docs/loop/loop.log
     D docs/loop/ultimo_auditor.json
     D docs/loop/ultimo_extractor.json

**Y LA PAGINA SE MOVIO TRES VECES SIN QUE YO ESCRIBIERA NADA**, medido con su huella y sin tocarla:

    $ for i in 1 2 3; do printf '%s  %s\n' "$(date '+%H:%M:%S')" "$(git hash-object docs/loop/APERTURA_CIEGA.md)"; sleep 20; done
    22:28:48  2bd7b2d67b95c52f5a09f37a34f146fe0d6e8ea0
    22:29:13  993c24ac0830fb896538d3b311ea88626bd3612f
    22:30:21  bfa62878d2f6a94e525aab413bf34ba1a798a934
    22:32:02  bfa62878d2f6a94e525aab413bf34ba1a798a934

**`LECTURA`: dos fases ciegas del auditor han estado vivas a la vez sobre este arbol.** Lo sostienen
tres cosas que yo no he hecho y que llevan hora de mi turno: el vaciado de `ultimo_apertura.json` de
las `22:25:08`, las tres huellas distintas de la pagina entre las `22:28:48` y las `22:30:21`, y los
ficheros de `.marquet_v1/` escritos entre las `22:07` y las `22:23`. **Es la misma figura que la
seccion `9.3` declara desde el otro lado**, y por `D.45` es del fundador y no mia: **sube, no se
arregla aqui.**

### 11.2. Las cifras de esta pagina, vueltas a correr a la hora del sello

**Las tres guardas de la casa**, corridas por mi a las `22:32:47`, dan lo mismo que la seccion `1.1`:

    $ date '+%H:%M:%S'; python forja.py gate; python forja.py guiones; python tests/test_aceptacion.py
    22:32:47
    GATE VERDE.
      nodos verificados: 270
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
      total: 201 pruebas, 0 fallos, 0 errores

**La huella del acta anterior**, que es la cifra de la seccion `0`:

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    f6c76f63bd9b6aeea7b1d5a9d485977d2d61f593

**El corte de la bandeja de la seccion `3`, a las `22:34:06`: las nueve huellas coinciden una a una**,
y ninguna se ha movido desde que la seccion `3` las congelo:

    $ for f in cuarentena/marquet_turn_the_ship/*.json; do echo "$(git hash-object $f)  $(basename $f)"; done
    319bc9d6deef958f82c184dad90778f7a4127a54  auditar_formacion_premios_ultima_fila.json
    36cfd9d6f74ca02d7b7d5c69aa49a030131475c0  cambiar_forma_trabajar_conservar_plantilla.json
    d3d72f7548cbbd043acb6f2ce5d61bc922d36dd2  ceder_control_reforzar_competencia_claridad.json
    71426b3f58e9b0293ee59df6fadde0accf36582e  contar_firmas_cadena_tramite_parado.json
    cda982ac44e84ff2674b793e022ec0f100dd8e9e  encargar_meta_especifica_dejar_libre_metodo.json
    34ea4932a90ef3f5812b9f4e9e4aba0cff6b84ac  inspeccionar_reparto_informacion_notas_jefe.json
    9d6356c978a80cd5eaaa486f0293651eae0aee8d  observar_reunion_rutinaria_senales_plantilla.json
    fdda3b318a856b52923cbbfcf2fa9c91146efa21  recorrer_organizacion_escuchar_plantilla.json
    33921de02e1c2bf027d89e5c03852b848fb3e77d  seguir_frustrado_preguntar_implantacion_ideas.json

**El censo de pasos de la seccion `4` y la columna `pasos` de la tabla de la seccion `7`**, contados
otra vez por mi, con un contador escrito aqui y sin ninguna lista de ids tecleada dentro
(`HEREDADO 4`): recorre la carpeta con `glob`, cuenta `pasos_accionables` y saca la unidad del
`UNIDAD DE ORIGEN:` del propio `resumen_teorico`.

    $ python - (cuenta pasos_accionables y lee UNIDAD DE ORIGEN de cada .json de la bandeja)
       11  cap_03.md     auditar_formacion_premios_ultima_fila
        5  cap_02.md     cambiar_forma_trabajar_conservar_plantilla
        7  cap_01.md     ceder_control_reforzar_competencia_claridad
       10  cap_03.md     contar_firmas_cadena_tramite_parado
        5  cap_02.md     encargar_meta_especifica_dejar_libre_metodo
        8  cap_03.md     inspeccionar_reparto_informacion_notas_jefe
        9  cap_03.md     observar_reunion_rutinaria_senales_plantilla
        7  cap_03.md     recorrer_organizacion_escuchar_plantilla
        8  cap_03.md     seguir_frustrado_preguntar_implantacion_ideas
      TOTAL PASOS EN LA BANDEJA: 70

**El recuento del barrido de la seccion `5.1`**, releido de `.marquet_v1/informe_nueve.txt` por un
contador propio y no a ojo:

    $ python - (recuenta ### y 'vecino ... [levantada por: ...]' sobre .marquet_v1/informe_nueve.txt)
    CANDIDATOS BARRIDOS      : 9
    VECINOS LEVANTADOS TOTAL : 21
    POR SENIAL               : {'similitud_texto': 20, 'paso_contra_nodo': 1}
      vecino DENTRO de la bandeja marquet : 20
      vecino FUERA                        : 1

### 11.3. Lo que esta seccion firma y lo que no

**FIRMO, porque lo he corrido yo entre las `22:32` y las `22:35`:** las tres guardas de la casa, la
huella del acta anterior, las nueve huellas del corte, los setenta pasos repartidos en sus nueve
filas con su unidad, y el recuento de veintiun vecinos del barrido. **Las cinco cuadran al digito con
lo que las secciones `0` a `10` ya decian.**

**NO FIRMO COMO MIAS DE ESTA FASE, y por eso van nombradas:** las lecturas de contenido de la seccion
`8` y los hallazgos de `9.1` y `9.2`. Son lectura del auditor de esta vuelta, estan sostenidas con
su cita y su linea en el sitio donde se escriben, **y yo no las he vuelto a leer paso por paso en
esta segunda fase.** Quedan como estan y se cierran en mi turno normal.

**NO HE ABIERTO NINGUNO DE LOS CUATRO DE `D.34.2` NI LOS HE RECUPERADO DE `git`**, y tampoco
`.vm01/`. Lo unico que he abierto del arbol del extractor son los nueve candidatos de la bandeja.
