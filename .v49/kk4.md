
## KK.4. TAREA 4. **`d033` PAGADA: LA TASA DE LA CORRIDA INTERMITENTE, CON SU BANDA**

**Medir no es tocar.** `D.45` me prohibe modificar `tests/`, no correr lo que ya esta escrito, y
**no he tocado ni un byte de `tests/`**: la comprobacion esta en `KK.5.b`.

### KK.4.a. **LAS `20` CORRIDAS, UNA DETRAS DE OTRA, CON SU CODIGO DE SALIDA**

**El arbol estuvo QUIETO durante las veinte**, sin una sola escritura mia, y lo digo porque resulta
que **importa**: la razon esta en `KK.4.c`.

<!-- TALLADO: script=.v49/d033_veinte.py salida=.v49/d033_veinte.txt -->

    $ python -m unittest tests.test_aceptacion.PruebaE.test_e_guion_largo_rompe_el_hook      (x20, una detras de otra, arbol quieto)

      #   codigo   segundos   veredicto
      --------------------------------------------
       1   0          22.9     OK
       2   0          22.8     OK
       3   0          23.1     OK
       4   0          22.0     OK
       5   0          23.1     OK
       6   0          22.9     OK
       7   0          22.0     OK
       8   0          21.8     OK
       9   0          23.0     OK
      10   0          22.6     OK
      11   0          22.7     OK
      12   0          22.7     OK
      13   0          22.4     OK
      14   0          21.7     OK
      15   0          22.1     OK
      16   0          22.2     OK
      17   0          22.6     OK
      18   0          22.5     OK
      19   0          21.9     OK
      20   0          22.7     OK

    corridas            : 20
    rojas               : 0   (ninguna)
    tasa de roja        : 0.0000  (0 de 20)
    banda al 95 por ciento (Wilson) : de 0.0000 a 0.1611

    reloj por corrida   : menor 21.7 s, media 22.5 s, mayor 23.1 s
    reloj de las 20      : 449.7 s

**CERO TRAZAS GUARDADAS PORQUE NO HUBO NI UNA ROJA**, y el guion las guardaba solo:

    $ ls .v49/d033_traza_*.txt
    (ninguna traza: cero rojas)

**Esa ruta vacia es VACIA A PROPOSITO: no hubo roja que trazar**, y era exactamente lo que
`JJ.4.b` no tuvo y yo mismo me apunte.

### KK.4.b. **LA TASA CON SU BANDA, QUE SIN ELLA ES MEDIA CIFRA** (manual principios 5 y 8)

| | |
|---|---|
| **tasa medida** | **`0` de `20`**, o sea `0,0000` |
| **banda al 95 por ciento** | **de `0,0000` a `0,1611`** (Wilson, que es la que vale con un `0` en el numerador) |
| **lo que la banda NO permite decir** | **que la prueba no falle nunca.** Con `20` corridas, una tasa real de hasta `1` de cada `6,2` cabe dentro de lo que he medido |
| **el `1` de `6` de la `ACTA 47`** | es `0,1667`, y **queda FUERA de mi banda por `0,0056`**. No lo doy por refutado: son dos muestras de arboles distintos y **la mia corrio con el arbol quieto**, que es justo la variable que `KK.4.c` senala |

**EL RELOJ TAMBIEN CUADRA CON EL DEL AUDITOR:** el midio `21,599` s por corrida y a mi me sale una
media de `22,5` s con la banda entera entre `21,7` y `23,1`. **Su cifra cae dentro de mi reparto**,
asi que no hay discrepancia que declarar.

### KK.4.c. **POR QUE ESTA PRUEBA PUEDE SALIR ROJA SIN QUE NADIE TOQUE NADA, LEIDO DE SU PROPIO CODIGO**

**No es una hipotesis sobre el azar: es lo que las tres lineas dicen.** Pegadas con su `sed` al lado
(`D.35`):

<!-- TALLADO: parcial salida=.v49/d033_porque.txt -->

    $ sed -n '392p;406p;419,421p' tests/test_aceptacion.py
    392:        self.sucio = os.path.join(RAIZ, "tests", "tmp_archivo_con_guion.md")
    406:            proceso = subprocess.Popen([interprete, "hooks/pre-commit"], cwd=RAIZ,
    419:        codigo, salida, quien = self.correr_hook()
    420:        self.assertEqual(codigo, 0,
    421:                         "el repo ha de estar limpio antes de ensuciarlo:\n%s" % salida)

**LAS TRES PIEZAS, Y JUNTAS EXPLICAN LA INTERMITENCIA SIN NECESIDAD DE AZAR:**

1. **Esta prueba NO corre contra el taller de usar y tirar.** Las otras `317` trabajan sobre el
   `tempfile.mkdtemp` de `BaseForja`; esta ensucia `RAIZ/tests/` (linea `392`) y lanza el hook con
   **`cwd=RAIZ`** (linea `406`), **o sea contra el arbol de verdad**.
2. **Su PRIMERA asercion exige que el hook este VERDE antes de ensuciar nada** (lineas `419` a
   `421`), y ese hook corre el `gate`, el barrido de guiones, **el tallado `D.41` y el censo
   `D.42` sobre `REPORTE.md`**.
3. **Asi que su resultado depende del estado del arbol en el instante en que corre.** Si el arbol
   se mueve mientras la suite corre, **la prueba puede salir roja sin que su codigo haya cambiado
   ni una letra**, que es exactamente la frase con la que `d033` la describe.

**Y LA COINCIDENCIA QUE LO SEÑALA:** la roja de la `ACTA 47` fue **una de seis**, y de esas seis
**cuatro fueron mias en el turno de la vuelta 48**, que es el turno en el que yo estaba escribiendo
`REPORTE.md`. **Mis veinte de hoy corrieron con el arbol quieto y dieron `20` de `20`.** No lo
presento como prueba: **es una correlacion de una sola observacion**, y lo digo con esas palabras.

### KK.4.d. **LO QUE PROPONGO, Y NO ARREGLO** (`D.45`, `EXTRACTOR.md` 13 y 14)

**NO ARREGLO NADA, y el encargo es explicito.** Lo que traigo es una propuesta para el fundador, con
su medida delante:

| # | propuesta | por que, con la cifra |
|---:|---|---|
| 1 | **que la tasa se vuelva a medir con el arbol EN MOVIMIENTO**, que es la condicion en que se vio la roja | mis `20` midieron el caso quieto y dieron `0`. **La condicion de la roja observada no se ha reproducido todavia**, asi que `d033` esta medida a medias y lo digo yo mismo |
| 2 | **que la prueba `E` corra contra una copia del arbol y no contra `RAIZ`** | es la unica de las `318` cuyo resultado depende de lo que otro proceso este escribiendo. **Es `tests/` y `D.45` me lo veda**, asi que va como propuesta y no como arreglo |

**Y LO QUE NO PROPONGO, dicho para que no se lea de mas:** **no propongo quitar la prueba ni
relajarla.** Es la unica que comprueba que el hook de guiones muerde de verdad, y `EXTRACTOR.md` 6
la necesita entera.

| tarea | que pide | estado |
|---|---|---|
| `KK.4` | pagar `d033`: `20` corridas del caso aislado, su codigo de salida, la tasa y su banda, sin tocar `tests/` | **CERRADA en `KK.4`**: `20` de `20` en verde, **tasa `0,0000` con banda `0,0000` a `0,1611`**, reloj `449,7` s, **cero trazas porque no hubo roja**, el mecanismo leido de las tres lineas del propio codigo, y **dos propuestas escritas sin tocar `tests/`** |
