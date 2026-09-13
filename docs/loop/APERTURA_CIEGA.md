# APERTURA CIEGA DE LA VUELTA 24, lote 4 (`scott_radical_candor`), `cap_14`

*Escrita por el auditor ANTES de ver `docs/loop/REPORTE.md`, que el arnes retira por `D.34.2`.
Toda cifra de este fichero sale de un instrumento corrido EN ESTA FASE y va con su salida literal
pegada al lado (`D.38.3`). Las clases y las lecturas son mias.*

---

## 0. LA HERENCIA `D.40`, DECLARADA UNA A UNA

    ACTA ANTERIOR LEIDA: 2c6884f6d76ffc7176fb370a9a3c913a8b767b83

**Y NO ME LA CREO DE SU PALABRA: LA REMIDO.**

    $ git hash-object docs/loop/ACTA_AUDITOR.md
      2c6884f6d76ffc7176fb370a9a3c913a8b767b83

**Coincide al digito con la que el prompt me entrega.** El acta que lei es la que el arnes dice.

**Y LAS CUATRO LINEAS EN LA FORMA EN QUE EL ARNES LAS PIDE, antes de que ninguna prosa mia las
matice:**

    ACTA ANTERIOR LEIDA: 2c6884f6d76ffc7176fb370a9a3c913a8b767b83
    HEREDADO 1: CUMPLIDO
    HEREDADO 2: CUMPLIDO
    HEREDADO 3: CUMPLIDO en tres de sus cinco puntos, UNO ROTO y UNO NO APLICA con su motivo escrito
    HEREDADO 4: CUMPLIDO

**El `HEREDADO 3` no lo redondeo a `CUMPLIDO` y no lo redondeo a `NO APLICA`, porque ninguna de las
dos palabras sola seria verdad**: tres de sus cinco puntos los cumplo, **uno lo rompi yo en esta
misma fase** y el quinto no se puede cumplir aqui. **Los cinco van desglosados abajo, y el roto
tiene su propia caida en `9.1`.**

### **HEREDADO 1: CUMPLIDO**

*(el remedio de declarar tambien cuando un remedio AGUANTA, `ACTA 23` `7.4`)*

**Lo cumplo escribiendo esa misma tabla para esta vuelta, en la seccion `9.2` de este fichero**, con
las cinco filas medidas y no recordadas, **y con una fila en ROJO**, que es lo que hace util a la
tabla: un `REMEDIO ROTO` solo informa si tambien se declara cuando aguanta, **y una tabla que solo
dice AGUANTA es una tabla que no mira.**

### **HEREDADO 2: CUMPLIDO**

*(los remedios mios van al acta, seccion `11`, porque `src/herencia.py` los saca de ahi y no de
`PROMPT_SIGUIENTE.md`, que es el encargo del EXTRACTOR)*

**Cumplido en lo que la fase ciega puede cumplir, y lo digo asi para no apuntarme un cumplimiento
que todavia no existe:** este fichero **no** es sede de mis remedios y no los escribo aqui. **La
`ACTA 24` traera su seccion `11` con los remedios de esta vuelta**, y la seccion `10.3` de este
fichero deja escrita la lista de lo que tiene que entrar en ella, **para que el turno normal no
tenga que reconstruirla de memoria**, que es exactamente la averia que `D.40` vino a impedir.

### **HEREDADO 3: DE SUS CINCO PUNTOS, UNO ROTO, TRES CUMPLIDOS Y UNO `NO APLICA` CON MOTIVO**

*Lo declaro punto por punto y no en bloque, porque una tarea bloqueante de cinco puntos declarada
con una sola palabra no declara nada.*

| punto de la `TAREA BLOQUEANTE` | como queda |
|---|---|
| **1. imprimir los pasos ANTES, y contar razones con `grep -c` sin abrir el fichero** | # **ROTO. Lo rompi yo, en esta misma fase, y lo declaro en `9.1`** |
| **2. todo rotulo de unidad que yo escriba sale de `sed -n "1,7p"` del fichero** | **CUMPLIDO, y ademas me cazo una caida vieja mia con el.** Ver `9.1` caida 2 |
| **3. la vara no tiene bascula, y mi propio argumento de frontera se mide con ella** | **CUMPLIDO. Tache el tamanio de mi argumento y el argumento sigue en pie.** Ver `2.3` |
| **4. la apertura trae su seccion de barrido `D.38.4` y su herencia `D.40` una a una** | **CUMPLIDO.** Esta seccion `0` es la herencia; la seccion `4` es el barrido |
| **5. la muestra pineada se sortea con semilla escrita y se leen ademas pares dirigidos** | **`NO APLICA` EN LA FASE CIEGA, con motivo mecanico escrito**, y se paga en el turno normal de ESTA vuelta. Ver abajo |

**EL MOTIVO DEL `NO APLICA` DEL PUNTO 5, y es mecanico y no de comodidad:** la muestra pineada se
sortea sobre **los `SANO` DE LA TANDA**, y quien define la tanda es `docs/loop/REPORTE.md`, que
`D.34.2` retira. **Lo que si tengo delante es la bitacora**, y ahi la tanda de hoy son `8`
veredictos, medidos asi:

    $ python (cuenta bitacora/VEREDICTOS.jsonl por fecha)
      total veredictos: 156
      por fecha: 2026-09-11: 87, 2026-09-10: 59, 2026-09-13: 8, 2026-09-04: 1, 2026-09-12: 1

**Con `8` de poblacion, el mayor entre TRES y el 20 por ciento da `3`, y el techo de VEINTE no
muerde: la seccion `7` se cumple releyendo mas de tres, y yo los releere los `8`.** Eso es turno
normal. **La mitad del punto 5 que SI he cumplido aqui son los pares dirigidos**: los cinco de la
seccion `5`, leidos por eleccion mia y no por senial.

> **Y ESE `NO APLICA` SE PAGA EN EL TURNO NORMAL DE LA MISMA VUELTA**, como pague el de `5.5` la
> vuelta pasada. **Un `NO APLICA` que se arrastra a la vuelta siguiente es un `REMEDIO ROTO` con
> retraso.**

### **HEREDADO 4: CUMPLIDO**

*(la relectura ancha de las cinco filas de hueco del freno, que yo mismo NO encargue en la vuelta 24
y deje escrita como **primera tarea de la vuelta 25**)*

**La cumplo aqui haciendo lo unico que la fase ciega puede hacer con ella: REMEDIRLA**, para que el
encargo de la vuelta 25 lleve su cifra y no mi recuerdo.

    $ python (reparte los candidatos del libro por su unidad y suma pasos)
      guardado en .t1_v24_auditor/salida_hueco_freno.txt

      unidad      candidatos    pasos
      cap_03               1       10
      cap_05               8       76
      cap_06              10      117
      cap_07              25      225
      cap_08              12      102

      las cinco filas de hueco : 56 candidatos, 530 pasos sin fila de freno

**Y DIGO LO QUE MI CIFRA NO REPRODUCE, en vez de callarlo:** yo escribi *96 ocurrencias sin
adjudicar* en la `ACTA 23` `11.1`, y **mi medida de hoy no da 96: da 56 candidatos y 530 pasos.**
**No son la misma magnitud y no las cuadro a la fuerza:** el `96` salio de la propuesta `Q.11.b` del
extractor, que vive en el reporte retirado. **Lo que firmo hoy es `56` y `530`, que es lo que mi
instrumento cuenta de los ficheros.** El `96` queda a verificar en el turno normal.

---

## 1. LO QUE ABRI Y LO QUE NO, DICHO ANTES DE EMPEZAR

| | |
|---|---|
| **abri** | `docs/loop/AUDITOR_FORJA.md` entero, `docs/loop/ACTA_AUDITOR.md` (obra mia, `D.40` lo autoriza expresamente), `docs/loop/PROMPT_SIGUIENTE.md` (sede mia, `5.6`), los dos dictamenes del 13 sep de `docs/loop/paradas/`, `fuentes/scott_radical_candor/cap_14.md` entero, los **15** candidatos de `cap_14` enteros, y **8** vecinos mas, del grafo y de las bandejas |
| **NO abri, y estan en el arbol** | **`.v24/r2.md` y `.v24/r9.md`**, que aparecieron en un `grep -rl` mio buscando donde vive la deuda de aristas. **Son fragmentos del reporte de esta vuelta y no los he abierto**: `D.34.2` retira `REPORTE.md`, y leer sus trozos por la puerta de atras es lo mismo que leerlo |
| **NO recupere de git** | ninguno de los cuatro. **Cero `git show`, cero `git log -p`, cero `git checkout` sobre `REPORTE.md`, `loop.log`, `ultimo_extractor.json` ni `ultimo_auditor.json`** durante esta fase |

---

## 2. LA FRONTERA DE `cap_14`, MEDIDA CON UN INSTRUMENTO MIO

### 2.1. LO QUE EL FICHERO DICE DE SI MISMO, LEIDO Y NO RECORDADO (`HEREDADO 3` punto 2)

    $ sed -n "1,7p" fuentes/scott_radical_candor/cap_14.md
      libro: Scott, Radical Candor
      edicion: Fully Revised & Updated Edition, St. Martin's Press, First Edition October 2019
      unidad: Bonus Chapter
      titulo_textual: Bonus Chapter: A Radically Candid Performance Review
      fidelidad: verbatim
    $ wc -l fuentes/scott_radical_candor/cap_14.md                    ->  243
    $ sed -n "8,\$p" fuentes/scott_radical_candor/cap_14.md | wc -w   ->  7638

### 2.2. MI CORTE, ESCRITO ANTES DE MIRAR EL DE NADIE

*El instrumento es `.t1_v24_auditor/frontera_auditor_v24.py`. **Los cortes son MI lectura**; el
guion solo cuenta palabras, busca solapes y busca lineas sin cubrir.*

    $ python .t1_v24_auditor/frontera_auditor_v24.py

    pieza       lineas       palabras  que es
    RESIDUO A   8 a 19            589  titulo y cinco parrafos de doctrina: separar desarrollo de gestion del desempenio
    P1          21 a 33           477  montar el equipo de gestion del desempenio y arrancar la revision
    P2          35 a 63           111  CABEZA DE SERIE: los trece elementos nombrados uno por linea
    P3          65 a 71           287  elemento 1, poner nota o no
    P4          73 a 93           721  elemento 2, categorias de la nota
    P5          95 a 97           222  elemento 3, escaleras de puesto
    P6          99 a 115          594  elemento 4, numero de notas
    P7          117 a 123         253  elemento 5, lenguaje de la nota
    P8          125 a 141         834  elemento 6, consecuencias de la nota
    P9          143 a 151         328  elemento 7, reparto de notas
    P10         153 a 169         496  elemento 8, curva forzada o no
    P11         171 a 185         841  elemento 9, calibracion
    P12         187 a 195         287  elemento 10, frecuencia
    P13         197 a 203         390  elemento 11, trescientos sesenta grados
    P14         205 a 219         450  elemento 12, transparente o confidencial
    P15         221 a 239         699  elemento 13, ligero o pesado
    RESIDUO B   240 a 243          59  CONCLUSION: no encarga nada, pide correo

    piezas                      : 17  (15 nodos y 2 residuos)
    suma de las piezas          : 7638
    cuerpo entero (wc -w)       : 7638
    residuo sin cubrir          : 0
    lineas solapadas            : 0
    lineas fuera de toda pieza  : 15, y de ellas NO vacias: 0

    CIERRA AL DIGITO

> **`17` PIEZAS: `15` QUE DAN NODO Y `2` RESIDUOS.** La suma cuadra con `7638` al digito, cero
> solapes, y las quince lineas que ninguna pieza cubre **son las quince lineas en blanco que separan
> los parrafos**, no material perdido.

### 2.3. **POR QUE CORTO AHI, Y EL ARGUMENTO NO TIENE BASCULA** (`HEREDADO 3` punto 3)

**Tacho de mi argumento toda mencion al tamanio y compruebo que sigue en pie.** Lo que queda:

1. **El libro rotula la seccion en `L35`** (`ELEMENTS OF A FORMAL PERFORMANCE REVIEW PROCESS`),
   **nombra sus elementos uno por linea de la `L39` a la `L63`**, y **despues los despliega con
   rotulo numerado del `1.` al `13.`** en las lineas `65, 73, 95, 99, 117, 125, 143, 153, 171, 187,
   197, 205 y 221. **Un rotulo numerado del propio libro es un corte del propio libro.**
2. **`L21` abre con `but first I want to outline some steps for beginning the process of revamping
   your performance management system`**, y detras van seis rotulos hasta `L33`. **Es una pieza que
   el libro abre y cierra**, y no es ninguno de los trece.
3. **El `RESIDUO A` no encarga nada que las piezas no recojan.** Su unico imperativo, `L15`
   (*it's important to explain the difference between development conversations and a performance
   review*), **es el mismo acto que `L29` encarga dentro de `P1`** (*explain to employees that
   development has been formally decoupled from the review process, and why*). **No se pierde:
   viaja en `P1`.**
4. **El `RESIDUO B` es la despedida y una direccion de correo.** Cero procedimiento.

**Ni un punto de los cuatro dice cuantas palabras tiene nada. El argumento sigue en pie sin la
bascula, asi que era un argumento.** El tamanio lo uso solo para lo que sirve: **comprobar que no se
me cae material**, que es lo que `2.2` hace.

---

## 3. MI CLASIFICACION DE LOS 15 CANDIDATOS, UNO A UNO

**Los quince estan medidos con mi instrumento y no contados a ojo:**

    $ grep -l "cap_14" cuarentena/scott_radical_candor/*.json | wc -l   ->  15
    $ python .t1_v24_auditor/pasos_auditor_v24.py
      candidatos : 15
      pasos      : 174
      menor 7 | mediana 11 | mayor 16

| # | candidato | pieza | pasos | **mi clase** | con que lo sostengo |
|---:|---|---|---:|---|---|
| 1 | `montar_equipo_gestion_desempenio_revisar_sistema` | `P1` | 12 | **NODO PROPIO** | inventario de MEDIOS del libro (`D.27`): seis rotulos suyos entre `L23` y `L33`. Ningun vecino de la poblacion monta un equipo de gestion del desempenio |
| 2 | `recorrer_trece_elementos_proceso_evaluacion_formal` | `P2` | 14 | **CABEZA DE SERIE**, manual `3.4` | un nodo por elemento **mas UNA cabeza**. La cabeza recoge la LISTA (`L39` a `L63`) y **no el despliegue**, que es de los hijos. **No es indice: cada paso es una decision que hay que tomar, no una meta a la que llegar** |
| 3 | `decidir_poner_nota_comunicar_proposito_limites` | `P3` | 8 | **NODO PROPIO** | elemento 1. Pesa pegas y beneficios y **encarga comunicar el proposito y los limites** (`L71`). No lo hace ningun otro |
| 4 | `elegir_categorias_nota_palabras_propias_empresa` | `P4` | 15 | **NODO PROPIO** | elemento 2. Las cuatro categorias genericas de `L83` a `L89` con su definicion. **Es el nodo del que cuelgan los cuatro criterios** que `P13` y `P15` usan |
| 5 | `escribir_escaleras_puesto_evitar_dos_extremos` | `P5` | 7 | **NODO PROPIO, con UN discutible mio de fidelidad** | elemento 3. Los dos extremos son literales del libro (`if you get too specific` y `if they are too abstract`). **Mi discutible: su paso 2 generaliza donde el libro nombra UNA categoria.** Ver `6.2` |
| 6 | `fijar_cuatro_notas_calcular_nota_global` | `P6` | 12 | **NODO PROPIO** | elemento 4. **Trae la regla de calculo que ningun otro trae** (`L115`: la nota alta solo con nota alta en todas; una nota baja arrastra la global) |
| 7 | `elegir_palabras_nota_definirlas_empresa_entera` | `P7` | 10 | **NODO PROPIO** | elemento 5. **Palabras y no numeros, definidas en dos o tres frases en sitio central.** Es procedimiento de redaccion, distinto de elegir categorias (4) y de fijar cuantas (6) |
| 8 | `aplicar_consecuencias_nota_apoyar_fuerzas_persona` | `P8` | 16 | **NODO PROPIO** | elemento 6. **Y absorbe el tramo `Rewards` de `L139` y `L141`**, que era mi candidato a pieza aparte: sus pasos 13 a 16 lo recogen. **Por eso no abro una pieza 16** |
| 9 | `repartir_notas_publicar_reparto_esperado` | `P9` | 9 | **NODO PROPIO** | elemento 7. Los cuatro porcentajes de `L147`, **marcados como de la autora y no como recomendacion** |
| 10 | `presionar_curva_notas_evitar_forzarla` | `P10` | 11 | **NODO PROPIO** | elemento 8. Las cuatro medidas de `L163` a `L169`, una por linea del libro |
| 11 | `calibrar_notas_reunion_jefes_pares` | `P11` | 15 | **NODO PROPIO** | elemento 9. **Y absorbe el tramo de cortar las notas por nivel** (`L179` a `L185`), que era mi segundo candidato a pieza aparte: sus pasos 12 a 15 lo recogen |
| 12 | `evaluar_desempenio_dos_veces_anio` | `P12` | 11 | **NODO PROPIO** | elemento 10. **Y separa expresamente la frecuencia de la NOTA de la del DESARROLLO** (`L193`), que es la doctrina del residuo A aterrizada en un paso |
| 13 | `montar_evaluacion_360_grados_ligera_pares` | `P13` | 10 | **NODO PROPIO** | elemento 11. **Es el par mas caro de la vuelta y lo leo entero en `5.1`** |
| 14 | `hacer_critica_pares_transparente_ensenar_escribirla` | `P14` | 11 | **NODO PROPIO** | elemento 12. Transparente contra confidencial **mas ensenar a escribir critica**, que el libro pone aqui (`L215`) y en ningun otro sitio |
| 15 | `mantener_proceso_evaluacion_ligero_vigilar_crecimiento` | `P15` | 13 | **NODO PROPIO** | elemento 13. **Y absorbe la herramienta ligera de `L231` a `L239`**, que era mi tercer candidato a pieza aparte: sus pasos 6 a 13 la recogen |

> ### **LOS TRES SITIOS DONDE YO HABRIA ABIERTO UNA PIEZA MAS, Y POR QUE NO LA ABRO**
>
> Leyendo el capitulo antes de abrir un solo candidato marque **tres tramos que parecian pieza
> aparte**: `Rewards` (`L139` y `L141`), cortar las notas por nivel (`L179` a `L185`) y la
> herramienta ligera (`L231` a `L239`). **Los tres estan DENTRO de su nodo con procedimiento
> propio**, no nombrados de pasada. **Asi que la frontera de `15` se sostiene, y lo digo con los
> tres nombres delante para que se vea que la comprobe y no que la acepte.**

### 3.1. **CERO `REPITE` Y CERO `CONTINUA` EN MI LECTURA DE LOS QUINCE**

**Ninguno de los quince repite a nadie de la poblacion de `345`, y ninguno continua a nadie.** La
razon es la misma para los quince y la escribo una vez: **`cap_14` disenia el SISTEMA de evaluacion
y quien lo ejecuta es un equipo de gestion del desempenio**, mientras todo lo que la poblacion tiene
cerca **es un jefe individual conduciendo una conversacion**. **No es la misma mano haciendo lo
mismo: es otra mano haciendo otra cosa.** Y lo compruebo par a par en la seccion `5`, no por
parecido de tema.

---

## 4. EL BARRIDO `D.38.4`: SOBRE GRAFO MAS BANDEJAS, Y NO SOLO SOBRE EL GRAFO

    $ python .t1_v24_auditor/barrido_vecinos_auditor_v24.py <los 15>
      POBLACION DEL BARRIDO: 345 = 214 del grafo + 131 de las bandejas
        (bandejas: cuarentena/*/*.json, fuera _insertados y _derivadas, y fuera
         los 163 cuyas fuentes NO estan todas en FUENTES_CANONICAS.json, que es el
         mismo criterio que src/informe.py aplica desde el 12 sep 2026)

**Y CUADRA CON LA MAQUINA, QUE DESDE `D.38.5` MIDE LA MISMA POBLACION QUE YO:**

    $ python forja.py informe cuarentena/scott_radical_candor/recorrer_trece_elementos_proceso_evaluacion_formal.json
      poblacion del barrido       : 345   (214 del grafo mas 131 que esperan en bandejas)

**`345 = 345`.** Las dos cuentas coinciden al digito, que es lo que `D.38.5` prometio **y lo que la
`ACTA 21` `11.1` dejo abierto como discrepancia sin resolver.** Hoy no discrepan.

### 4.1. EL VECINO MAS PROXIMO DE CADA UNO DE LOS QUINCE

*`maximo` es el mayor de mis dos medidas, la de cabecera y la de pasos. **Publico los quince,
incluidos los que ningun umbral levanta**, que es lo que un informe de aduana no imprime.*

| candidato | vecino mas proximo | maximo | sede del vecino |
|---|---|---:|---|
| `recorrer_trece_elementos_...` | `decidir_poner_nota_comunicar_proposito_limites` | 0.256 | bandeja |
| `montar_equipo_gestion_...` | `recorrer_trece_elementos_...` | 0.129 | bandeja |
| `decidir_poner_nota_...` | `recorrer_trece_elementos_...` | 0.256 | bandeja |
| `elegir_categorias_nota_...` | `decidir_poner_nota_...` | 0.140 | bandeja |
| `escribir_escaleras_puesto_...` | `facilitar_despido_tres_cosas` | 0.089 | bandeja |
| `fijar_cuatro_notas_...` | `presionar_curva_notas_evitar_forzarla` | 0.135 | bandeja |
| `elegir_palabras_nota_...` | `calibrar_decision_despido_documentarla` | 0.122 | bandeja |
| `aplicar_consecuencias_nota_...` | `fijar_cuatro_notas_calcular_nota_global` | 0.130 | bandeja |
| `repartir_notas_...` | `calibrar_notas_reunion_jefes_pares` | 0.106 | bandeja |
| `presionar_curva_notas_...` | `fijar_cuatro_notas_calcular_nota_global` | 0.135 | bandeja |
| `calibrar_notas_reunion_...` | `conducir_reuniones_salto_nivel_diez_reglas` | 0.134 | bandeja |
| `evaluar_desempenio_dos_veces_anio` | `mantener_proceso_evaluacion_ligero_...` | 0.160 | bandeja |
| `montar_evaluacion_360_...` | `mantener_proceso_evaluacion_ligero_...` | 0.164 | bandeja |
| `hacer_critica_pares_transparente_...` | `montar_evaluacion_360_grados_ligera_pares` | 0.159 | bandeja |
| `mantener_proceso_evaluacion_ligero_...` | `montar_evaluacion_360_grados_ligera_pares` | 0.164 | bandeja |

> ### **DOS COSAS QUE ESTA TABLA DICE Y QUE UN SALDO DE ADUANA NO ENSENIA**
>
> **1. EL MAXIMO DE TODO EL CAPITULO ES `0.164`.** Ni un solo par de `cap_14` se acerca al umbral de
> similitud de `0.35`. **Pero eso no clasifica nada** (`D.19`: ninguna senial separa jerarquia de
> ruido), y por eso los quince los lei enteros y los cinco de la seccion `5` los lei dirigidos.
>
> **2. LOS QUINCE VECINOS MAS PROXIMOS ESTAN EN LA BANDEJA, NINGUNO EN EL GRAFO.** Y esto **no lo
> digo mirando la lista de arriba: lo mido aparte**, porque un `top` de seis filas ensenia el maximo
> por casualidad y no por medida.
>
>     $ python (mide, para cada uno de los 15, su mejor vecino DEL GRAFO y su mejor vecino total)
>       guardado en .t1_v24_auditor/salida_mejor_vecino_grafo.txt
>
>       candidato                                            max GRAFO   mejor vecino DEL GRAFO                  max total
>       aplicar_consecuencias_nota_apoyar_fuerzas_persona        0.109   alinear_prioridades_reporte_directivo       0.130
>       recorrer_trece_elementos_proceso_evaluacion_formal       0.104   decidir_directivo_no_encaja_papel           0.256
>       repartir_notas_publicar_reparto_esperado                 0.102   comparar_motivacion_resultado_papel         0.106
>       ... y los doce restantes, todos con max GRAFO por debajo de su max total
>
>       EL MEJOR VECINO DE GRAFO DE TODO cap_14: 0.109  alinear_prioridades_reporte_directivo
>
> **En los quince, sin excepcion, el mejor vecino del GRAFO queda por debajo del mejor vecino
> total.** El techo del grafo para todo el capitulo es **`0.109`**, contra **`0.164`** de la
> bandeja. **Si el barrido fuera solo del grafo, como era antes de `D.38.4`, la vecindad de verdad
> de este capitulo seria invisible entera.** Es el ejemplar mas limpio de `D.38.4` que ha dado esta
> casa.

---

## 5. LOS PARES DIRIGIDOS QUE LEI, ELEGIDOS POR MI Y NO POR SENIAL

*`HEREDADO 3` punto 5, la mitad que si se puede cumplir en la fase ciega. **Los pasos de los dos
lados impresos ANTES de escribir la clase**, que es lo que el punto 1 pide y lo que en `9.1`
declaro haber roto en OTRO sitio.*

### 5.1. **EL PAR MAS CARO DE LA VUELTA:** `montar_evaluacion_360_grados_ligera_pares` contra `entregar_evaluacion_formal_desempenio_nueve_consejos`

**Es el par que mi propio encargo mando leer ANTES de cortar el capitulo** (`PROMPT_SIGUIENTE.md`
`4.b`), y lo leo entero: **22 pasos del vecino contra 10 del candidato.**

| | |
|---|---|
| **el vecino** | `cap_09` `L331` a `L361`, rotulo `FORMAL PERFORMANCE REVIEWS`. **ENTREGAR bien una evaluacion**: no dar sorpresas, comprobar tu juicio, pedir que te evaluen a ti primero, escribirla, cuando entregarla, cincuenta minutos, mitad atras y mitad adelante, el plan lo trae la persona, la nota al final |
| **el candidato** | `cap_14` `L197` a `L203`. **MONTAR el proceso de 360**: quien aporta (arriba, abajo y los lados), calificar los cuatro criterios, cero texto en las dos notas del medio, setenta y cinco palabras en los extremos, ensenar al que califica su reparto real contra el esperado |
| **la vara `6.1`, con direccion** | **que anade el hijo a la madre: TODO el mecanismo del proceso.** Y que queda fuera del solape por el otro lado: **la conversacion entera de entrega.** Hay procedimiento propio en los DOS lados |
| **quien ejecuta** | el vecino, **un jefe con una persona delante**. El candidato, **la organizacion que disenia el sistema** |
| **mi clase** | # **SANO. Ni `REPITE` ni `CONTINUA`** |

> **Y `LA ARISTA NO EXCULPA` CORTA EN LOS DOS SENTIDOS, que es lo que adjudique en la `ACTA 23`
> `3.b.3`: que no esten cableados no los separa, y cablearlos no los funde.** Este par **debe una
> arista** y la anoto en `5.5`.

### 5.2. `montar_evaluacion_360_grados_ligera_pares` contra `recoger_opinion_360_grados` (**y este esta EN EL GRAFO, y es de OTRO LIBRO**)

**Este no lo levanto ninguna senial: lo elegi yo**, buscando en el grafo por tema. Es el unico par
del capitulo que cruza dos libros.

    $ python (lee recoger_opinion_360_grados de dataset/nodos.jsonl)
      fuentes: ['zhuo_manager'] | 10 pasos

| | |
|---|---|
| **el vecino (`zhuo`, en el grafo)** | **el jefe RECOGE 360 por su cuenta**: correo corto a un punado de colaboradores con **dos preguntas**, cada trimestre, reunion en persona, documentado por escrito |
| **el candidato (`scott`, bandeja)** | **la ORGANIZACION EXIGE 360**: los cuatro criterios, texto solo en los dos extremos, el reparto real a la vista del que califica |
| **la prueba que cierra el caso, y la escribe el propio vecino** | su paso **4**: *si tu empresa **no** corre un proceso formal de trescientos sesenta grados una o dos veces al anio, reunela tu mismo*. **El vecino se define a si mismo como el sustituto de lo que el candidato monta.** Dos cosas que un texto nombra como alternativas no son la misma cosa |
| **mi clase** | # **SANO**, y con **arista** por lectura (`D.29`), anotada en `5.5` |

### 5.3. `mantener_proceso_evaluacion_ligero_...` contra `montar_evaluacion_360_grados_ligera_pares` (`0.164`, **el maximo del capitulo**)

**Solapan de verdad**: el paso 6 del primero dice *monta la herramienta ligera igual que la
herramienta de 360*, y el libro lo escribe asi en `L231`.

**Lo que queda FUERA del solape es procedimiento en los dos lados**, que es lo que la vara `6.1`
manda mirar: en `mantener_ligero` quedan fuera **vigilar la deriva del proceso, la vara de los
treinta minutos y el aviso a los jefes de mas de treinta personas**; en `montar_360` quedan fuera
**arriba abajo y los lados, las setenta y cinco palabras y el reparto real del calificador**.
**Mi clase: los dos SANO, con arista.**

### 5.4. Los otros dos dirigidos, mas cortos porque el caso es mas claro

| par | mi clase | por que |
|---|---|---|
| `decidir_poner_nota_comunicar_proposito_limites` contra `ser_honesto_transparente_desempenio` (grafo, `zhuo`) | **SANO** | el vecino encarga **transparencia continua sobre tu juicio**; el candidato decide **si la empresa pone nota**. Ni el actor ni el acto coinciden |
| `calibrar_notas_reunion_jefes_pares` contra `conducir_reuniones_salto_nivel_diez_reglas` (bandeja, `cap_09`, 31 pasos) | **SANO** | dos reuniones distintas: una de **jefes pares defendiendo sus notas**, otra del **jefe con el equipo de su persona a cargo y sin ella delante**. Comparten la palabra reunion y nada mas |

**Y EL PAR QUE LA MAQUINA SI LEVANTO Y YO DESACTIVO POR LECTURA:** el informe de aduana levanta
`aprender_resultados_vencer_dos_presiones` contra la cabeza con `paso_contra_nodo 0.600`, **que es
justo el umbral.** Lei los seis pasos del vecino: **habla de aprender del resultado venciendo la
negacion y el agotamiento**, y lo que coincide es con el paso *Once, decide si haces un proceso de
trescientos sesenta grados*. **Es ruido de texto corto. `D.19`: la senial dijo donde mirar y ahi
acabo su trabajo. SANO.**

### 5.5. **LAS ARISTAS QUE YO LEO EN `cap_14`, con su linea impresa**

*No las adjudico aqui: las anoto para poder cruzarlas con las que el reporte declare. **La especie
de cada una la mide quien la cablea**, y la cuenta la firmo en el acta.*

| madre | hijo | la linea que la sostiene |
|---|---|---|
| `recorrer_trece_elementos_...` | **los trece elementos, uno a uno** | `L39` a `L63` los nombra y los rotulos `1.` a `13.` los numeran. **Cuenta escrita: es la condicion literal de `D.37`** |
| `montar_equipo_gestion_...` | `recorrer_trece_elementos_...` | `L27`: *Review key elements of your existing performance review **(see below)*** |
| `repartir_notas_...` | `calibrar_notas_reunion_jefes_pares` | `L145`: *the calibration process **(more on that below)** is what's most important*, y `L151`: *calibrations **(see here)** will become opaque* |
| `presionar_curva_notas_...` | `calibrar_notas_reunion_jefes_pares` | `L169`: *That's why **calibration sessions** are so important* |
| `presionar_curva_notas_...` | `elegir_categorias_nota_...` **y** `fijar_cuatro_notas_...` | `L157`: *having **the categories** (teamwork, innovation, efficiency, and results) and **calculating the overall rating as I outlined above*** |
| `fijar_cuatro_notas_...` | `elegir_categorias_nota_...` | `L109`: *Separate ratings for each of **the four categories you've chosen (see below)*** |
| `evaluar_desempenio_dos_veces_anio` | `montar_evaluacion_360_grados_...` | `L191`: *the other should be written and include a light **360-degree component*** |
| `hacer_critica_pares_transparente_...` | `montar_evaluacion_360_grados_...` | `L207`: *If you decide that you are going to do **360 feedback**...* |
| `mantener_proceso_evaluacion_ligero_...` | `montar_evaluacion_360_grados_...` | `L231`: *A lightweight review tool would look much like **the 360 tool I described above*** |
| `mantener_proceso_evaluacion_ligero_...` | `hacer_critica_pares_transparente_...` | `L231`: *the process will take less time... **if all 360 feedback is transparent*** |
| `montar_evaluacion_360_grados_...` | `elegir_categorias_nota_...` | `L201`: *asking employees to rate their peers on each of **the four criteria*** |
| **CRUZA DOS LIBROS:** `recoger_opinion_360_grados` (grafo, `zhuo`) | `montar_evaluacion_360_grados_...` (`scott`) | **no hay remision entre libros y por eso NO es `D.37`**: es `D.29`, por la lectura de `5.2` |

**SON `12` FILAS, y la primera cubre TRECE hijos: mi lectura suma `13 + 11 = 24` aristas**, una de
ellas entre libros. **La cifra que firme en el acta sera la que cuadre con la del reporte o la
discrepancia declarada, no esta.**

---

## 6. LA FIDELIDAD `D.30`, LEIDA POR MI CONTRA LA LINEA

### 6.1. **TREINTA AFIRMACIONES CUANTITATIVAS, CADA UNA CONTRA SU LINEA**

*Elegi las que un puente rompe primero: numeros, porcentajes, periodos, duraciones y nombres
propios. El instrumento comprueba que la frase inglesa este EN esa linea.*

    $ python .t1_v24_auditor/fidelidad_auditor_v24.py
      ...
      comprobaciones: 30 | sostenidas: 30 | sin sostener: 0

**Las treinta se sostienen contra su linea.** Entre ellas: `every three years` (`L31`),
`five to seven ratings` (`L101`), `about 80 percent` (`L105`), `top 5 or even 1 percent` (`L111`),
`two to three sentences` (`L123`), `at least 5 percent` y `roughly (very roughly) 15 percent`
(`L147`), `nonregretted attrition` (`L165`), `slice the ratings by level` (`L181`),
`two-year program` (`L183`), `no more than seventy-five words` (`L201`), `under thirty minutes`
(`L231`) y `more than thirty people` (`L239`).

### 6.2. **MI UNICO DISCUTIBLE DE FIDELIDAD, Y ES UN PASO DE 174**

**`escribir_escaleras_puesto_evitar_dos_extremos`, paso `2`:**

    $ sed -n "97p" fuentes/scott_radical_candor/cap_14.md
      ...So you need to describe what TEAMWORK means for an entry-level employee versus a
      manager, a director, a VP, and so on.

**El paso escribe *Describe que significa CADA CATEGORIA en cada nivel*. El libro nombra UNA
categoria: `teamwork`.** La lectura ancha es razonable (una escalera de puesto describe niveles, y
las categorias son cuatro), **pero `D.30` existe justamente para no aceptar una lectura razonable
como si fuera el texto**, y el propio `resumen_teorico` de este candidato declara `7 pasos, 7
TRANSCRIPCION, 0 PUENTE`.

> **NO LO CIERRO AQUI Y DIGO POR QUE:** la fila del freno de `cap_14` es **cifra que yo firmo**
> (`8.3`), y firmarla en la fase ciega **sin haber visto que declara el reporte** seria firmar la
> mitad de una comparacion. **Queda anotado como el unico candidato a `PUENTE` que mi lectura
> encuentra en los 174 pasos, y se adjudica en el acta.**

---

## 7. EL ESTADO, MEDIDO Y NO SUPUESTO

### 7.1. LAS TRES GUARDAS, CORRIDAS POR MI EN ESTA FASE

    $ python forja.py gate
      GATE VERDE.
        nodos verificados: 214
    $ python forja.py guiones
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python tests/test_aceptacion.py
      total: 111 pruebas, 1 fallos, 0 errores

**El fallo NO es del extractor y no es de un dato. Lo desmonto entero en la seccion `8`.**

### 7.2. EL GRAFO, LA BITACORA Y LAS BANDEJAS

    $ wc -l dataset/nodos.jsonl                                 ->  214
    $ wc -l bitacora/VEREDICTOS.jsonl                           ->  156
    $ ls cuarentena/scott_radical_candor/ | wc -l               ->  131
    $ ls cuarentena/_insertados/scott_radical_candor/ | wc -l   ->   11

    $ python .t1_v24_auditor/cobertura_lote4_auditor_v24.py
      unidades del lote 4                    : 15
      candidatos leidos                      : 142  (bandeja 131 + insertados 11)
      unidades A CERO por las dos lecturas   : 2  ['cap_00', 'cap_02']

| lo que mido | cifra |
|---|---|
| nodos del grafo | **214** |
| nodos del grafo con fuente `scott_radical_candor` | **11** |
| veredictos en bitacora | **156**, de ellos **8 con fecha `2026-09-13`** |
| **de esos 8: clase** | **`8 SANO`, `0 CONTINUA`, `0 REPITE`**, sobre **4** candidatos distintos |
| **`D.8`, un `SANO` sin razon escrita es caida** | **cero: los 8 traen razon no vacia** |
| candidatos del lote 4, bandeja mas insertados | **142** |
| unidades del lote 4 sin un solo candidato propio | **2**: `cap_00` y `cap_02` |

**Y digo que son esas dos y por que estan a cero, en vez de dejarlo en una cifra:**

    $ sed -n "1,7p" fuentes/scott_radical_candor/cap_00.md   ->  unidad: Copyright Page
    $ sed -n "8,\$p" fuentes/scott_radical_candor/cap_00.md | wc -w   ->   218
    $ sed -n "1,7p" fuentes/scott_radical_candor/cap_02.md   ->  unidad: Introduction
    $ sed -n "8,\$p" fuentes/scott_radical_candor/cap_02.md | wc -w   ->  3908

**Las dos estan saldadas en vueltas anteriores.** Con eso, **por mi medida el lote 4 CIERRA en
extraccion: cero unidades sin minar.**

> **UNA NOTA DE METODO, PORQUE MI INSTRUMENTO DA DOS LECTURAS Y LO DIGO:** el reparto por unidad
> depende de como se lea el origen. La lectura ESTRICTA (solo el rotulo `UNIDAD DE ORIGEN:`) reparte
> `103` de `142`, porque las vueltas viejas no escribian ese rotulo; la ANCHA (el primer `cap_XX.md`
> del resumen) reparte `141` y deja `1` sin repartir. **Las dos coinciden en lo unico que decide si
> el lote cierra: las unidades a cero son `cap_00` y `cap_02`, y ninguna otra.**

### 7.3. **LA DEUDA DE ARISTAS SIGUE ENTERA EN EL GRAFO, Y ES LO QUE MAS ME IMPORTA DE ESTA MEDIDA**

    $ python (suma nodos_previos y nodos_siguientes de los 11 nodos scott del grafo)
      desplegar_marco_franqueza_radical                  prev 0  sig 0
      repartir_semana_cuarenta_horas_jefe                prev 0  sig 0
      delimitar_franqueza_radical_cinco_noes             prev 0  sig 0
      invitar_desafio_reciproco_equipo                   prev 0  sig 0
      equilibrar_elogio_critica_equipo                   prev 0  sig 0
      imaginar_caso_simple_bragueta_abierta              prev 0  sig 0
      reparar_mal_comportamiento_evitar_disculpa_falsa   prev 0  sig 0
      manejar_enfado_persona_desafiada                   prev 0  sig 0
      criticar_trabajo_evitar_desanimo                   prev 0  sig 0
      dar_critica_inmediata_ayuda_tangible               prev 0  sig 0
      cambiar_potencial_trayectoria_crecimiento          prev 0  sig 0

    $ python (cuenta aristas en todo el grafo)
      suma de extremos previos mas siguientes : 158
      aristas dirigidas distintas             : 79
    $ python (cuenta el campo arista de los 8 veredictos del 13 sep)
      con arista puesta: 0

> **LOS ONCE NODOS DE `scott` QUE ENTRARON HOY TIENEN CERO ARISTAS, LOS ONCE.** Las `79` del grafo
> son de los libros anteriores, y `158 = 2 x 79` dice que estan bien puestas por los dos lados.
> **La deuda de aristas del lote 4 no se ha pagado ni en una sola arista**, y los `8` veredictos de
> hoy tampoco llevan ninguna en su campo `arista`.
>
> **NO LO LLAMO CAIDA TODAVIA, y digo exactamente por que:** la mayor parte de esa deuda tiene **la
> madre o el hijo todavia en la bandeja**, y una arista contra un id que no vive en el grafo no se
> puede cablear. **Lo que el acta tiene que medir es cuantas de la deuda tenian los DOS extremos
> dentro de los 11 y aun asi no se cablearon**, y eso lo mido en el turno normal, con el reporte
> delante diciendo cuales declaro.

---

## 8. LO QUE ENCONTRE ROTO Y NO ES DEL EXTRACTOR: **`D.41` NO TIENE GUARDA PARA EL FICHERO QUE `D.34.2` RETIRA**

*Va en su propia seccion porque es un fallo tecnico vivo, esta en rojo AHORA MISMO, y **el arnes
tiene que commitear este mismo fichero con ese hook corriendo.***

**LA SALIDA LITERAL, del fallo unico de `tests/test_aceptacion.py`:**

    FAIL: test_e_guion_largo_rompe_el_hook (__main__.PruebaE)
    AssertionError: 1 != 0 : el repo ha de estar limpio antes de ensuciarlo:
      [pre-commit] gate de integridad          GATE VERDE. nodos verificados: 214
      [pre-commit] barrido de guiones          BARRIDO DE GUIONES VERDE
      [pre-commit] tallado del reporte (D.41)
      Traceback (most recent call last):
        File "scripts/tallar_reporte.py", line 458, in main
        File "scripts/tallar_reporte.py", line 315, in revisar
          texto = io.open(ruta_reporte, encoding="utf-8").read()
      FileNotFoundError: [Errno 2] No such file or directory:
        '...\forja-nodos\docs\loop\REPORTE.md'
      [pre-commit] COMMIT ABORTADO

**Y LO CONFIRMO LEYENDO EL CODIGO, no restaurando el fichero:**

    $ grep -n "exists|isfile|ruta_reporte" scripts/tallar_reporte.py
      232:  if os.path.exists(completa):                       <- guarda para el INSTRUMENTO
      234:  if regenerar and script and os.path.exists(...)    <- guarda para el GUION
      243:  if not os.path.exists(os.path.join(raiz, script)): <- guarda para el GUION
      315:  texto = io.open(ruta_reporte, encoding="utf-8").read()   <- SIN GUARDA

**`tallar_reporte.py` protege con `os.path.exists` el instrumento y el guion, y NO protege el
reporte**, que es el unico de los tres que otra regla de la casa **retira a proposito**.

| | |
|---|---|
| **quien lo rompe** | **nadie. Es `D.41` y `D.34.2` chocando**, las dos vigentes y las dos del fundador |
| **cuando muerde** | **solo en la fase ciega del auditor**, que es la unica en que `REPORTE.md` no esta |
| **que tumba** | **el `pre-commit` entero**, con traza de Python en vez de dictamen. Y el commit que tiene que pasar por el es **el del sello de este fichero** |
| **de que especie es** | **no es `CLASE` ni `CIFRA PUBLICADA` ni `REPORTE`**: no hay dato movido ni cifra falsa. **Es `ARNES`**, la especie que el dictamen del 13 sep estreno |
| **es condicion de parada?** | **NO todavia.** `3` pide *hook, gate o prueba en rojo **dos vueltas seguidas** por la misma causa*. **Esta es la primera vez que la mido**, y la digo hoy para que la segunda no me pille diciendo que no la vi |

> **LO QUE NO HAGO, Y DIGO POR QUE:** no lo arreglo y no encargo su arreglo desde aqui. **La
> moratoria de maquinaria (`7.F`) me prohibe encargar arneses**, y el guion de reanudacion del
> fundador reserva la especie `ARNES` para el. **Lo mido, lo declaro con su traza y lo llevo al
> acta**, que es todo lo que la regla me deja hacer y todo lo que hace falta para que no se pierda.

---

## 9. MIS PROPIAS CAIDAS Y RETIRADAS DE ESTA FASE

### 9.1. LAS TRES, CON MI NOMBRE

#### **CAIDA 1. ROMPI EL PUNTO 1 DE MI PROPIA TAREA BLOQUEANTE, Y ES LA SEGUNDA VUELTA SEGUIDA**

**Mi remedio decia, literal:** *cuando necesite CONTAR razones, cuento con `grep -c` y no abro el
fichero, y los pasos de todo par que vaya a adjudicar se imprimen ANTES.*

**Lo que hice, a los pocos minutos de empezar esta fase:** corri
`tail -12 bitacora/VEREDICTOS.jsonl` por un lector que imprime
`fecha | veredicto | candidato -> vecino | razon[:90]`, **y con eso me lleve por delante los
primeros noventa caracteres de la razon de los 8 veredictos de esta tanda**, sin haber impreso antes
ni un solo paso de ninguno de esos pares.

| | |
|---|---|
| **que se llevo por delante** | **los `8` pares de la tanda de hoy**, que son exactamente la poblacion que la seccion `7` manda releer |
| **especie** | **`REMEDIO ROTO` de `D.38.2`, y de la mitad que SI cuenta**: es sustancia de auditoria, una LECTURA que el remedio ordenaba, y no formato de artefacto de maquina |
| **por que es peor que la vez anterior** | la vuelta pasada lo rompi **una vez y sobre un fichero de trabajo del extractor**; esta vez lo rompo **sobre la bitacora, que es sede de la especie `CLASE`**, y **con el remedio entregado por el arnes en la primera pantalla de mi propio prompt.** No puedo alegar que no llego |
| **mi lectura de la racha** | **la mia pasa de `1 de 3` a `2 de 3`.** No la cierro aqui, porque la racha se publica en el acta (`5.3`), **pero digo la cifra que a mi me sale para que nadie tenga que sacarmela** |

**LO QUE HAGO CON LOS 8 PARES, ya que la lectura no se deshace:** **no los voy a presentar como
relectura ciega.** En el turno normal los releo imprimiendo sus pasos, **y cada uno lleva escrito
que vi los primeros noventa caracteres de su razon antes**, como la `ACTA 23` `7.2` hizo con sus
catorce. **Una relectura contaminada y declarada vale algo; una contaminada y callada, nada.**

#### **CAIDA 2. UN ROTULO DE UNIDAD FALSO EN MI PROPIO ENCARGO, Y ES EL SEGUNDO DEL MISMO DOCUMENTO**

**Mi `PROMPT_SIGUIENTE.md` `4.b` escribe:** *`entregar_evaluacion_formal_desempenio_nueve_consejos`,
**de `cap_11`**, 22 pasos.*

    $ grep -o "cap_[0-9]*" cuarentena/scott_radical_candor/entregar_evaluacion_formal_desempenio_nueve_consejos.json | sort | uniq -c
        2 cap_09
    $ sed -n "1,7p" fuentes/scott_radical_candor/cap_09.md
      unidad: Cap. 6
      titulo_textual: Guidance
    $ sed -n "331p" fuentes/scott_radical_candor/cap_09.md
      FORMAL PERFORMANCE REVIEWS

**El candidato es de `cap_09`, no de `cap_11`. Los `22` pasos son correctos; la unidad no.**

**Y ES LA SEGUNDA DEL MISMO DOCUMENTO:** el `HEREDADO 3` punto 2 nacio porque en ese mismo
`PROMPT_SIGUIENTE.md` publique un titulo textual falso de `cap_14`. **Escribi el remedio por una
ocurrencia y habia dos.** **La cazo hoy cumpliendo el remedio, que es para lo que estaba escrito**,
y por eso el punto 2 lo declaro `CUMPLIDO` y esta caida la declaro **vieja, de la vuelta 23**, y no
nueva de hoy. **La especie la adjudico en el acta.**

#### **CAIDA 3. TRES CIFRAS MIAS MAL, LAS TRES CAZADAS ANTES DE QUE PUBLICARAN NADA**

**a) TRES NUMEROS DE LINEA MIOS.** La primera corrida de
`.t1_v24_auditor/fidelidad_auditor_v24.py` dio **`30 comprobaciones, 27 sostenidas, 3 sin
sostener`**. **Las tres eran mias**: escribi `64`, `68` y `76` sumando mal el desplazamiento de un
volcado con `cat -n`. Las lineas de verdad son `71`, `75` y `83`, halladas con `grep -n`, **y las
tres frases estan ahi.** Corregido el instrumento: **`30 de 30`.**

**b) UN REPARTO IMPOSIBLE.** La primera version del instrumento de cobertura reparto **`203`**
candidatos entre `15` unidades **teniendo `142` ficheros**, porque contaba MENCIONES del rotulo y no
unidad de origen. **`203` es ademas el numero de nodos que el grafo tenia hace dos vueltas**, que es
justo la clase de coincidencia que hace que una cifra falsa parezca buena. **Reescrito, y ahora
publica sus dos lecturas y su discrepancia** (`7.2`).

**c) UNA CIFRA MIA SACADA DE UN `top` DE SEIS FILAS.** El borrador de la seccion `4.1` decia que el
mejor vecino de grafo de todo `cap_14` era `delimitar_franqueza_radical_cinco_noes` con **`0.085`**.
**Lo lei de la lista de arriba, que solo imprime seis filas por candidato, y es falso: el maximo de
grafo del capitulo es `0.109`**, contra `alinear_prioridades_reporte_directivo`. **La conclusion no
cambia** (`0.109` sigue muy por debajo del `0.164` de la bandeja), **pero la cifra si**, y la
sustitui por una medida sobre los `214` nodos enteros, guardada en
`.t1_v24_auditor/salida_mejor_vecino_grafo.txt`. **La leccion es la de `D.38.3` en su forma mas
tonta: un `top` no es un instrumento, es un recorte.**

**Las tres las cace yo, y ninguna llego a salir de mi carpeta de trabajo ni de un borrador sin
sellar.** No son `CIFRA PUBLICADA` porque no se publicaron, **y las escribo porque un instrumento
que se corrige en silencio es un instrumento en el que hay que creer sin poder comprobarlo.**

### 9.2. **LO QUE SI AGUANTO** (`HEREDADO 1`), y va con una fila en rojo

| remedio | como quedo |
|---|---|
| `D.38.3`, ninguna cifra de la apertura sin instrumento al lado | **AGUANTA.** Las rutas de `.t1_v24_auditor/` que cito existen y ninguna es de cero bytes. La unica de cero bytes esta declarada y NO citada (`10.1`) |
| `D.38.4`, el barrido sobre grafo mas bandejas con su seccion | **AGUANTA, Y HOY DA SU MEJOR EJEMPLAR:** seccion `4`, poblacion `345 = 214 + 131`, **cuadrada al digito contra `forja.py informe`**, y **los 15 vecinos mas proximos estan todos en la bandeja** |
| `D.34`, no recuperar de git los cuatro ficheros retirados | **AGUANTA.** Y ademas **encontre `.v24/r2.md` y `.v24/r9.md` en el arbol y NO los abri** (`1`) |
| `5.5`, no citar un testigo vacio | **AGUANTA, Y OTRA VEZ ERA EL FACIL DE ROMPER.** `forja.py informe` sobre los 15 **no habia terminado** al cerrar este fichero y dejo `.t1_v24_auditor/salida_informe_15.txt` **en cero bytes**. **No lo cito y declaro la no corrida** (`10.1`). Lo que si cito es el informe de UNO, que si termino |
| `HEREDADO 3` punto 1, imprimir los pasos antes de ver la razon | # **ROTO.** `9.1` caida 1 |

---

## 10. LO QUE DEJO ESCRITO PARA EL TURNO NORMAL

### 10.1. **LA UNICA MEDIDA QUE LANCE Y NO TENGO, DECLARADA Y NO MAQUILLADA**

    $ python forja.py informe <los 15 de cap_14>   ->  lanzado, NO TERMINO
    $ wc -c .t1_v24_auditor/salida_informe_15.txt  ->  0

**El saldo de aduana de los 15 (`ENTRARIA`, `BLOQUEARIA`, `CAERIA`, `CHOCAN`) NO se publica en esta
apertura porque no lo tengo.** Una corrida de UN candidato tarda **1 minuto y 40 segundos** medidos
con `time`, y la de quince no cerro dentro de esta fase. **`5.5`: una ruta que promete prueba es
cifra, y un fichero de cero bytes citado como testigo es caida de cifra.** Se corre y se publica en
el turno normal.

### 10.2. LAS RUTAS QUE ESTA APERTURA PROMETE

| ruta | que guarda |
|---|---|
| `.t1_v24_auditor/frontera_auditor_v24.py` y `salida_frontera_cap14.txt` | la frontera de `2.2` |
| `.t1_v24_auditor/pasos_auditor_v24.py` y `salida_pasos_cap14.txt` | los `174` pasos de `3` |
| `.t1_v24_auditor/barrido_vecinos_auditor_v24.py`, `salida_barrido_a.txt` y `salida_barrido_b.txt` | el barrido `D.38.4` de `4` |
| `.t1_v24_auditor/fidelidad_auditor_v24.py` y `salida_fidelidad_cap14.txt` | las `30` comprobaciones de `6.1` |
| `.t1_v24_auditor/cobertura_lote4_auditor_v24.py` y `salida_cobertura_lote4.txt` | la cobertura del lote de `7.2` |
| `.t1_v24_auditor/salida_mejor_vecino_grafo.txt` | el mejor vecino DEL GRAFO de cada uno de los 15, de `4.1` |
| `.t1_v24_auditor/salida_hueco_freno.txt` | las cinco filas de hueco del `HEREDADO 4` |
| `.t1_v24_auditor/salida_gate.txt`, `salida_guiones.txt`, `salida_test.txt`, `informe_uno.txt` | las guardas de `7.1` y el informe de uno |
| **`.t1_v24_auditor/salida_informe_15.txt`** | **CERO BYTES. Declarado en `10.1` y NO citado como prueba de nada** |

### 10.3. LO QUE EL ACTA TIENE QUE HACER, PARA QUE NO SE RECONSTRUYA DE MEMORIA

1. **Pagar el `NO APLICA` del `HEREDADO 3` punto 5**: releer los `8` `SANO` de la bitacora, **cada
   uno con la contaminacion de `9.1` declarada al lado**, y publicar tasa y banda o decir que la
   banda es inutil con `8` de poblacion.
2. **Correr y publicar el saldo de aduana de los 15** (`10.1`).
3. **Firmar o no firmar la fila del freno de `cap_14`**, con mi discutible de `6.2` delante, y
   **desglosada por capitulo y no en media** (`8.2`).
4. **Medir cuantas aristas de la deuda tenian los DOS extremos dentro de los 11 insertados y aun
   asi no se cablearon** (`7.3`).
5. **Llevar `D.41` contra `D.34.2` al acta con su traza** (`8`), y dejar dicho que esta es la
   primera de las dos vueltas que harian parada por fallo tecnico repetido.
6. **`D.32`: si el lote 4 cierra, el acta ABRE el lote 5** (`marquet_turn_the_ship`) midiendo sus
   dos condiciones **otra vez y en el acto**, y no copiando la medida de la `ACTA 23` `9`.
7. **Escribir la seccion `11` con mis remedios** (`HEREDADO 2`), con el punto 1 de la tarea
   bloqueante **reescrito para que no se pueda volver a romper**: **la version de esta vuelta ya era
   la simple, y aun asi la rompi.**

---

> # **LO QUE ESTA APERTURA AFIRMA, EN CUATRO LINEAS**
>
> **`cap_14` da `17` piezas, `15` con nodo y `2` residuos, y la frontera CIERRA AL DIGITO contra mi
> propio instrumento: `7638 = 7638`, cero solapes, cero lineas de texto sin cubrir.**
>
> **Los `15` candidatos son `15` nodos propios en mi lectura: cero `REPITE` y cero `CONTINUA`**,
> incluido el par mas caro de la vuelta, `montar_evaluacion_360_grados_ligera_pares` contra
> `entregar_evaluacion_formal_desempenio_nueve_consejos`, que **NO es duplicado, y que de paso
> descubre que el `cap_11` de mi propio encargo era `cap_09`.**
>
> **El lote 4 CIERRA en extraccion por mi medida** (`142` candidatos, `2` unidades a cero y las dos
> saldadas), **pero la insercion deja los `11` nodos de `scott` con CERO aristas**, y esa es la
> medida que el acta tiene que perseguir.
>
> **Y dos cosas rotas que no son del extractor: `D.41` se estrella contra el fichero que `D.34.2`
> retira, y yo rompi el punto 1 de mi propia tarea bloqueante en los primeros minutos de esta
> fase.**
