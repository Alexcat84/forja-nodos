
---

## O.3. TAREA 2: **`cap_09` SE CIERRA ENTERO**. LAS CINCO PIEZAS QUE DEBIA. **CERRADA**

*Es la deuda que el encargo anterior provoco y va primera del trabajo. **La frontera de 30
piezas no se republica** (`1.f`): esta adjudicada y la obedezco.*

### O.3.a. LAS CIFRAS DEL ENCARGO, REMEDIDAS POR MI ANTES DE USARLAS (`EXTRACTOR.md` 5)

*Una cifra del encargo no es fuente de una cifra mia. **Las cinco filas y su suma las volvi a
medir sobre el fichero**, y el porcentaje tambien.*

    $ python .t1_v20/remedir.py
      P22  L301 a L313    416 palabras
      P23  L315 a L329    573 palabras
      P24  L331 a L361   1526 palabras
      P27  L383 a L413   1419 palabras
      P28  L415 a L425    399 palabras
      SUMA de las cinco: 4333 palabras
      cuerpo de cap_09 (sed -n '8,$p' | wc -w): 17482
      las cinco sobre el cuerpo: 24.8 por ciento
    $ sed -n '8,$p' fuentes/scott_radical_candor/cap_09.md | wc -w
      17482

> **LAS CINCO FILAS DEL ENCARGO REPRODUCEN SU PALABRA AL DIGITO, la suma tambien (`4.333`) y
> el porcentaje tambien (`24,8`).** Cero discrepancias que declarar.

### O.3.b. **LAS CINCO QUE ESCRIBO SON EXACTAMENTE LAS CINCO QUE FALTABAN**, EN UNA LINEA Y CON SU CUENTA

*Es lo unico que el encargo me autoriza a publicar de la frontera, y lo publico asi y no mas.*

> ### **`cap_09`: 20 PIEZAS QUE DAN NODO, 15 ESCRITAS EN LA VUELTA 19, 5 HOY, 20 DE 20.**

    $ python .t1_v20/medidas.py
      cap_09 AL CERRAR: 20 candidatos, 272 pasos
        cuerpo de cap_09: 17482 palabras  ->  874.1 palabras por candidato
        el nodo con mas pasos del capitulo: ('conducir_reuniones_salto_nivel_diez_reglas', 31)
      LOTE 4 AL CERRAR cap_09: 83 candidatos, 856 pasos

**Y LAS CINCO SON `P22`, `P23`, `P24`, `P27` y `P28`, que son las mismas cinco que mi `N.4.9`
declaro una a una y que el encargo me remidio.** Ninguna sexta, ninguna cuarta.

### O.3.c. LOS CINCO CANDIDATOS, CADA UNO POR LA ADUANA **EN EL ACTO EN QUE SE ESCRIBIO** (`EXTRACTOR.md` 16)

*Y esta vez **uno escrito, uno comprobado, sin tandas**, que es la letra mas estricta y la que
mi discutible 9 de la vuelta 19 no cumplio. El informe tarda unos tres minutos en esta
maquina y aun asi los cinco fueron de uno en uno.*

    $ time python forja.py informe cuarentena/scott_radical_candor/revisar_critica_mujer_agresiva_cuatro_tacticas.json
      real 3m4.557s      <- el cronometro de esta maquina hoy, medido y no heredado

| # | pieza | id | pasos | palabras por paso | **aduana** |
|---:|---|---|---:|---:|---|
| 16 | **P22** `L301` a `L313` | `revisar_critica_mujer_agresiva_cuatro_tacticas` | **12** | 34,7 | **`[ENTRARIA]`** al primer intento |
| 17 | **P23** `L315` a `L329` | `responder_critica_abrasiva_cuatro_reglas` | **14** | 40,9 | **`[ENTRARIA]`** al primer intento |
| 18 | **P24** `L331` a `L361` | `entregar_evaluacion_formal_desempenio_nueve_consejos` | **22** | 69,4 | **`[ENTRARIA]`** al primer intento |
| 19 | **P27** `L383` a `L413` | `conducir_reuniones_salto_nivel_diez_reglas` | **31** | 45,8 | **`[ENTRARIA]`** al primer intento |
| 20 | **P28** `L415` a `L425` | `resolver_dudas_frecuentes_reuniones_salto_nivel` | **16** | 24,9 | **`[ENTRARIA]`** al primer intento, **y re informado despues de una correccion mia** (`O.3.e`) |
| | **las cinco** | | **95** | **45,6** | **5 de 5 por la aduana, 5 al primer intento** |

**LA RUTA QUE GUARDA ESOS CINCO INFORMES, CON EL COMANDO QUE LA CUENTA PEGADO EN LA MISMA
FRASE** (`O.2.d`, mi remedio):

    $ grep -cE "\[(ENTRARIA|CAERIA|BLOQUEARIA)\]" .aduana_v20/informes.txt
      6
    $ grep -oE "\[(ENTRARIA|CAERIA|BLOQUEARIA)\]" .aduana_v20/informes.txt | sort | uniq -c
      6 [ENTRARIA]

**SON SEIS INFORMES Y NO CINCO, Y DIGO POR QUE ANTES DE QUE SE PREGUNTE: el sexto es el re
informe de `P28` tras la correccion de `O.3.e`.** Cinco candidatos, seis informes, cero
caidas. **La ruta guarda MAS de lo que la tabla cita, no menos, y aun asi lo digo**, porque
la mitad del remedio que muerde es nombrar la diferencia en la misma linea.

**LOS ID, CONTRA LAS SEIS REGLAS** (`EXTRACTOR.md` 15): **cinco de cinco limpios en la puerta,
contra 14 de 15 la vuelta pasada.** Las piezas que mas riesgo tenian eran `P27` y `P28`,
porque su rotulo ingles es `SPEAKING TRUTH TO "POWER"` y `skip level meeting`: **`speaking`,
`truth` y `power` estan las tres en la lista NEGRA**, asi que el id va entero en castellano
(`conducir_reuniones_salto_nivel_diez_reglas`) y el ingles viaja en `denominaciones`, que es
su sede. **`performance` de `P24` es la misma especie** y sale como `desempenio`.

### O.3.d. **EL INFORME DE LOTE DE LOS 20 DE `cap_09`, QUE ES LO QUE LA `ACTA 19` `2.3` PIDIO**

*El auditor no pudo correrlo (mato el de los 78 a los 600 segundos) y me lo dejo encargado en
`1.e`: **si corres el informe de lote del capitulo que cierras, pega su salida entera y la
firmo yo en la siguiente**. Lo corri sobre los 20, y **no sobre los 83**, porque los 83 son
unas cuatro horas a tres minutos por candidato.*

**Y DIGO PARA QUE SIRVE, PORQUE NO ES UNA FORMALIDAD:** un informe de un solo candidato **no
puede medir `CHOCAN entre si dentro del lote`**, que es la unica de las cuatro cifras del
saldo que necesita a los veinte en la misma llamada. Los cinco informes de `O.3.c` prueban
que cada uno entra contra el grafo; **este prueba que los veinte no se pisan entre ellos.**

    $ python forja.py informe $(tr '\n' ' ' < .aduana_v20/lista_cap09_lf.txt)
      (salida entera en .aduana_v20/informe_lote_cap09_v2.txt)

**Y UNA CAIDA DE MI INSTRUMENTO QUE DECLARO CON SU FICHERO ENTERO EN EL ARBOL:** la primera
corrida salio **`CAERIAN por una guarda: 20`**, y no era de los candidatos:

    $ grep -c "el fichero no se puede leer" .aduana_v20/informe_lote_cap09_ROJO_MIO.txt
      21
    $ grep -m1 "Errno 22" .aduana_v20/informe_lote_cap09_ROJO_MIO.txt
      [Errno 22] Invalid argument: '...abrazar_incomodidad_arrancar_critica_equipo.json\r'

**MI LISTA DE RUTAS SALIO CON FIN DE LINEA CRLF Y LAS 20 RUTAS LLEGARON CON UN RETORNO DE
CARRO PEGADO.** El rojo es mio y no de la aduana, **y la aduana se porto exactamente como
debia: un fichero que no se puede leer es `CAERIA`, no un aviso.** No borro la corrida roja:
queda en `informe_lote_cap09_ROJO_MIO.txt`, porque **retirarla seria retirar la prueba de una
caida que acabo de escribir**, que es el criterio que la `ACTA 19` `7.6` uso con la suya.

### O.3.e. LA RELECTURA DE FIDELIDAD `D.30`, EN EL ACTO, Y **LA CIFRA QUE CACE CON ELLA**

*`NINGUNA GUARDA DE ESTA CASA VE UN PASO QUE TU ESCRIBISTE Y EL LIBRO NO DICE.* Los cinco
informes verdes de arriba **no dicen nada de esto**, y por eso esta seccion existe.*

| candidato | pasos | **TRANSCRIPCION** | **PUENTE** | de donde sale cada tramo |
|---|---:|---:|---:|---|
| `revisar_critica_mujer_agresiva_cuatro_tacticas` | 12 | **12** | **0** | P1 y P2 de `L303`; P3 a P5 de `L305`; P6 y P7 de `L309`; P8 a P10 de `L311`; P11 y P12 de `L313` |
| `responder_critica_abrasiva_cuatro_reglas` | 14 | **14** | **0** | P1 de `L317`; P2 y P3 de `L319`; P4 a P7 de `L321`; P8 y P9 de `L323`; P10 y P11 de `L325`; P12 de `L327`; P13 y P14 de `L329` |
| `entregar_evaluacion_formal_desempenio_nueve_consejos` | 22 | **22** | **0** | P1 de `L335`; P2 de `L337`; P3 de `L341`; P4 a P6 de `L343`; P7 de `L345`; P8 de `L347`; P9 de `L349`; P10 de `L351`; P11 a P14 de `L353`; P15 y P16 de `L355`; P17 a P19 de `L357`; P20 de `L359`; P21 y P22 de `L361` |
| `conducir_reuniones_salto_nivel_diez_reglas` | 31 | **31** | **0** | P1 de `L385`; P2 de `L389`; P3 a P5 de `L391`; P6 de `L393`; P7 de `L395`; P8 a P10 de `L397`; P11 y P12 de `L399`; P13 de `L401`; P14 a P16 de `L403`; P17 a P20 de `L405`; P21 y P22 de `L407`; P23 y P24 de `L409`; P25 a P29 de `L411`; P30 y P31 de `L413` |
| `resolver_dudas_frecuentes_reuniones_salto_nivel` | 16 | **16** | **0** | P1 y P2 de `L419`; P3 a P6 de `L421`; P7 a P10 de `L423`; P11 a P16 de `L425` |
| **`cap_09`, esta vuelta** | **95** | **95** | **0** | |

**LAS TRES ESPECIES DE PUENTE DEL LOTE 1, VIGILADAS UNA A UNA, y aqui hay un dato que cambia
el argumento de las vueltas anteriores:**

| especie | como queda en los cinco |
|---|---|
| **el periodo** | **NO lo escribo yo, y esta vez el libro lo escribe casi siempre.** Los seis periodos y duraciones que aparecen en mis pasos son del texto: `cinco minutos` y `dos veces al anio` en `L343`, `cincuenta minutos` y `diez minutos de descanso` en `L355`, `un dia o mas` en `L361`, `una vez al anio` en `L385` y `L413`, y `ocho minutos` en `L409` |
| **el destinatario** | **NO lo escribo yo, y uno de ellos tambien es del libro:** la copia a ti del correo que el jefe manda a su equipo esta escrita en `L411`. **Los que el libro no pone no estan**, y cada candidato dice cual falta en su propio `resumen_teorico` |
| **el responsable** | **NO lo escribo en ninguno de los cinco.** `P28` es el caso mas tentador: `L419` dice *empieza a excavar en los problemas* y **no dice quien decide si el jefe sigue.** Lo deje abierto |

> ### **Y LA CIFRA QUE LA RELECTURA CAZO, QUE ES LO QUE HACE QUE ESTA SECCION NO SEA UN ADORNO. LA DECLARO ENTERA.**
>
> Corri un barrido propio sobre **toda cifra y todo numeral escrito con letra** dentro de los
> 95 pasos, buscandolos en el tramo del libro de su propio candidato:
>
>     $ python .t1_v20/cifras.py          (primera corrida)
>       cifras y numerales comprobados en los 95 pasos: 41
>       los que NO estan en su tramo del libro          : 1  [('P28', 16, 'numeral dos')]
>
> **MI `P16` DE `P28` DECIA *la diferencia que el texto pone entre LAS DOS MANERAS de
> compadecerse*, Y EL TEXTO NO DA ESA CUENTA:** `L425` dice *there's a world of difference
> between saying X and saying Y*. **Pone dos frases y no dice `dos`.**
>
> **ES UN PUENTE, Y DE UNA ESPECIE QUE ESTA CASA YA TIENE NOMBRADA AUNQUE NO EN ESTA LISTA:
> la cuenta que el libro no escribe.** Es la prima de *`LA CUENTA ES CONDICION`* de `D.37`
> (correccion del titular del 11 sep 2026) y del `four rules of thumb` de `L317` que acaba de
> costar una adjudicacion entera. **Lo mismo que no me deja cablear una serie sin cuenta
> escrita no me deja atribuirle al libro una cuenta que no da.**
>
>     $ python .t1_v20/fix_p28.py ; python .t1_v20/cifras.py
>       corregido P16 de resolver_dudas_frecuentes_reuniones_salto_nivel | pasos: 16
>       cifras y numerales comprobados en los 95 pasos: 40
>       los que NO estan en su tramo del libro          : 0  []
>
> **CORREGIDO EN EL ACTO, ANTES DE DAR EL CANDIDATO POR ESCRITO, y con la correccion declarada
> dentro de su propio `resumen_teorico` sin borrar lo que habia** (que es lo que esta casa hizo
> con las dos caidas de regla 3 de `cap_04` y con la de la vuelta 19). **Y el candidato volvio
> a la aduana despues de la correccion**, porque `EXTRACTOR.md` 16 dice que un candidato no
> esta escrito hasta que ha pasado la aduana, **y el que paso la aduana era el de antes.**
>
> **LO QUE ESTO DICE DE MI MANO, Y NO ME CONVIENE:** el barrido de cifras lo corri **despues**
> de escribir los cinco, no mientras los escribia. **Si hubiera escrito la cuenta en un paso
> que no lleva numeral, ese barrido no la habria visto.** `1 de 40` es la cifra, y la digo con
> su denominador; **lo que no digo es que mi mano sea limpia por haberla cazado una maquina.**

### O.3.f. `D.37` Y `D.29` SOBRE LAS CINCO, CON **LOS DOS BARRIDOS PEGADOS** Y NO UNO

*El remedio de la `ACTA 18` mando pegar los dos `grep` y la `ACTA 19` `4.4` verifico que lo
cumpli. **Lo cumplo otra vez, y con el barrido ancho ademas del estrecho.***

    $ grep -nE "(two|three|four|five|six|seven|eight|nine|ten) (rules|things|tactics|questions|conversations|reasons|steps|tips|ways)" fuentes/scott_radical_candor/cap_09.md
      83:three things   127:two things   317:four rules   429:two questions
    $ grep -noE "\b(two|three|four|five|six|seven|eight|nine|ten)\b [a-z]+s\b" fuentes/scott_radical_candor/cap_09.md | wc -l
      18        <- el mio, mas ancho: numeral seguido de sustantivo plural
    $ grep -noE "\b(two|three|four|five|six|seven|eight|nine|ten)\b [a-z]+s\b" fuentes/scott_radical_candor/cap_09.md
      67:three months     83:three things    85:five minutes   89:three touchstones
      125:three minutes   125:three times    127:two things    261:three weeks
      269:two colleagues  279:seven years    279:two levels    317:four rules
      343:five minutes    393:two goals      409:eight minutes 409:eight minutes
      419:three times     429:two questions

**EL ANCHO LEVANTA `18` SITIOS Y EL ESTRECHO `4`, Y LOS 14 DE DIFERENCIA LOS NOMBRO EN VEZ DE
CONTARLOS**, que es la otra mitad del remedio: doce son minutos, meses, semanas, anios,
personas y niveles, **y dos son de mi tramo de hoy y merecen una linea cada uno.**

| el sitio | que es, y por que no cablea |
|---|---|
| **`L393`, `two goals`** | esta **dentro de mi `P27`**, en su paso 6: *tienes dos objetivos, ayudarla a ser mejor jefe y que su equipo se sienta comodo*. **Es una cuenta escrita con sus partes nombradas, y aun asi NO es `D.37`: son METAS**, y `D.27` restriccion 1 dice que un inventario de metas no cuenta. **Nombrar adonde hay que llegar sigue siendo nombrar** |
| **`L419`, `three times`** | esta **dentro de mi `P28`**: *en anios haciendo estas reuniones esto solo me ha pasado tres veces*. **No es una serie, es una cifra del autor**, y su sede es `atribuciones`, donde esta, con su autor y su falta de fecha de corte dicha |

> ### **`D.37`: LA UNICA CUENTA ESCRITA DEL TRAMO DE HOY ES EL `four rules of thumb` DE `L317`, Y **NO CABLEA NINGUNA ARISTA**. LA RAZON ES LA LETRA DE `D.37` Y NO UNA COMODIDAD MIA.**
>
> `D.37` cablea **cabeza a parte** cuando *esas partes existen como nodos*. **Las cuatro
> reglas de `L317` NO existen como nodos: son cuatro pasos de `responder_critica_abrasiva_cuatro_reglas`**,
> que es el nodo entero de la pieza. **Una arista de un nodo a sus propios pasos no es una
> arista: es el nodo.** Y la guarda `auto_arista` del gate existe justamente por eso.
>
> **LAS OTRAS CUATRO SERIES DEL CAPITULO YA ESTABAN RESUELTAS Y NO LAS REABRO:** `L83` y
> `L127` cayeron dentro de piezas de la vuelta 19, y `L429` esta en `P29`, que **no da nodo**.
>
> **Y LO QUE NO ES `D.37` LO DIGO POR SU NOMBRE, porque es donde mas facil seria colarla:**
> `P22` dice *try these tactics* (cuatro), `P24` dice *here is my advice* (nueve), `P27` dice
> *a few rules of thumb* (diez) y `P28` dice *some of the questions* (cuatro). **Ninguna de
> las cuatro escribe su cuenta.** Las cuento yo de los rotulos, **lo digo asi en cada
> `resumen_teorico`**, y **ninguna cablea serie.**

> ### **`D.29`: LA ARISTA `P27` A `P28` SE DECLARA CON SU RAZON ESCRITA, Y ES LA NUMERO 12 DE MI COLA**
>
> **Es la que el encargo llama *la arista `D.29` mas obvia del tramo*, y la declaro asi:**
>
> | | |
> |---|---|
> | **madre** | `conducir_reuniones_salto_nivel_diez_reglas` (`P27`, `L383` a `L413`) |
> | **hija** | `resolver_dudas_frecuentes_reuniones_salto_nivel` (`P28`, `L415` a `L425`) |
> | **razon escrita** | **las cuatro preguntas de la hija son preguntas SOBRE el procedimiento de la madre**, y las cuatro nombran su objeto: `L419` y `L423` hablan de lo que pasa **dentro de la reunion** que `L385` define; `L421` remata en *Embrace the discomfort*; y `L425` responde al equilibrio que `L391` de la madre plantea como el peligro de la reunion. **La hija no existe sin la madre: su rotulo es `Skip level meeting FAQs`** |
> | **es `D.29` y no `D.37`** | `L417` dice *some of the questions* y **no dice cuantas**. La cuenta es condicion, asi que hay algo que argumentar, **y lo argumento arriba** |
> | **por que hoy no se escribe** | **los dos extremos viven en cuarentena.** `python forja.py arista` necesita a la madre y a la hija en el grafo, y el grafo cierra en 203 igual que abrio |
>
> **Y POR ESO SE ESCRIBIERON LAS DOS EN LA MISMA VUELTA, que es lo que el encargo exige por su
> nombre: partirlas dejaria la hija sin madre**, y el capitulo se habria cerrado con una deuda
> peor que la que esta vuelta vino a saldar.

### O.3.g. **`cap_09` QUEDA CERRADO**, DECLARADO POR SU NOMBRE

> # **`cap_09` QUEDA CERRADO CON SUS 20 CANDIDATOS.**
>
> **20 piezas que dan nodo, 20 candidatos escritos, 20 por la aduana, `272` pasos.** Cero
> piezas que dan nodo sin candidato, cero candidatos sin pieza.
>
> **Y LO QUE ESO ARREGLA, dicho con la cifra del acta que lo abrio:** la `ACTA 19` `9` medio el
> lote 4 como *`cap_00` a `cap_08` enteros, **`cap_09` A MEDIAS** (15 de sus 20 piezas), y
> `cap_10` a `cap_14` sin tocar*. **Hoy la fila del medio desaparece.** El lote 4 pasa a
> `cap_00` a `cap_09` **enteros** y `cap_10` a `cap_14` sin minar. **Ningun capitulo de este
> libro esta partido.**

**LA TAREA 2 QUEDA CERRADA.**
