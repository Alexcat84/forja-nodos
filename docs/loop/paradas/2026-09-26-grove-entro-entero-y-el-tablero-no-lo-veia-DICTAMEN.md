# DICTAMEN, 26 SEP 2026: **GROVE ENTRO ENTERO Y EL TABLERO NO LO VEIA**

*La linea serial se detuvo sola el 26 sep 2026 a las 06:37:07, al abrir su vuelta 5 de esta corrida (la
`76` del libro), con la guarda del tablero en ROJO. La sesion de chat la diagnostico y la arreglo con la
linea parada, que es donde se commitean los arreglos del arnes (decision del fundador del 24 sep 2026).*

## LO QUE PASO

- La `75` metio las 7 ultimas fichas de Grove, una por vez. La `ACTA 74` la audito y escribio el encargo
  de la `76`: **Gerber preparado para insertar**, que es el orden de la campania (Grove, Gerber, Marquet).
- Al abrir la `76`, `scripts/guarda_tablero.py` midio el tablero y `D.51` le dio a la serial
  `grove_high_output`, "COSECHADO y sin dueno: se continua desde el capitulo siguiente al ultimo minado".
  El encargo declaraba `gerber_emyth`: ROJO, y la vuelta no abrio. **No se gasto ningun turno.**

## LA CAUSA

`src/tablero.py`, `medir()`: para un libro declarado **cosechado**, el estado declarado `COSECHADO` se
fijaba **antes** que la medida `INSERTADO` (bandeja a cero y nodos en el grafo), y nunca se revisaba. Grove,
con la bandeja a cero, sus 18 capitulos de 18 minados y 92 nodos en el grafo, seguia `COSECHADO` para
siempre. Era la primera vez que un libro cosechado entraba entero: Scott y Zhuo se minaron en esta rama.

**Tambien habria impedido cerrar la campania:** `D.60` (MUNDO 11 COMPLETO) exige los libros del corte
`INSERTADO`, y los tres que quedaban (Grove, Gerber, Marquet) son cosechados.

## EL ARREGLO

Un cosechado con la bandeja a cero, **todos** los capitulos del libro minados y nodos en el grafo sale
`INSERTADO`, con la medida escrita en `estado_de`. Uno con candidatos en la bandeja sigue `COSECHADO`.
Medido despues del arreglo: Grove `INSERTADO` (0 en bandeja, 92 en el grafo), Gerber y Marquet `COSECHADO`
(22 y 20 en bandeja), y `D.51` le da a la serial `gerber_emyth`, que es lo que declara el encargo.

Pruebas nuevas en `tests/test_aceptacion.py` (rojas antes del arreglo, verdes despues, y validas cuando
Gerber y Marquet entren): un cosechado insertado entero sale `INSERTADO`; `D.51` no le da a la linea un
libro sin nada que hacer; caso negativo, un cosechado con bandeja sigue `COSECHADO`.

## EL PARA_ALEXIS QUE DEJO EL ARNES, LITERAL

> # PARA_ALEXIS: el encargo no puede abrir el libro que declara (D.49, D.51)
> 
> La vuelta 5 no llego a gastar un turno. El arnes volvio a medir el tablero, leyo
> que libro DECLARA docs/loop/PROMPT_SIGUIENTE.md, y ese libro no le corresponde a
> esta linea.
> 
> Lo que midio la guarda:
> 
> GUARDA DEL TABLERO (D.49)
>   linea de este arbol : serial
>   libro que declara el encargo : gerber_emyth
>   libro que el orden le da (D.51): grove_high_output
>     prioridad 1 del orden del mundo 11. 'grove_high_output' esta COSECHADO y sin dueño: su trabajo ya llego a esta rama, asi que se continua desde el capi
> 
> TABLERO EN ROJO. La vuelta NO abre:
>   D.51: el encargo declara 'gerber_emyth' y el orden del mundo 11 le da a esta linea 'grove_high_output'. prioridad 1 del orden del mundo 11. 'grove_high_output' esta COSECHADO y sin dueño: su trabajo ya llego a esta rama, asi que se continua desde el capitulo siguiente al ultimo minado (cap_18), citando su frontera. D.50.
> 
> QUE SIGNIFICA. D.49: un libro, un dueño a la vez. Ninguna linea abre ni continua
> un libro cuyo ESTADO no sea SIN EMPEZAR con dueño NINGUNO, o PAUSADO con dueño
> NINGUNO y ya COSECHADO. Y D.51: ninguna linea elige libro, toma el de PRIORIDAD
> mas baja cuyo estado lo permita.
> 
> QUE NO SIGNIFICA. No dice que el trabajo anterior este mal, ni que ninguna cifra
> sea falsa. Dice que la vuelta iba a trabajar sobre un libro que otra linea tiene
> abierto, o sobre uno que no le toca por el orden del mundo 11.
> 
> POR QUE ESTA GUARDA EXISTE. El 17 sep 2026 el lote 4 estaba a punto de cerrar, y
> D.32 abre el lote siguiente SIN PARADA entre medias. El siguiente por orden era
> el lote 5, que se estaba extrayendo en otra rama con 9 candidatos dentro. Lo unico
> que lo impedia era una frase escrita a mano en el encargo, y D.35 dice lo que vale
> eso: un remedio que se cumple acordandose no es un remedio.
> 
> Estado: rama extraccion-mundo-11, hash 9dcaa4b3.
> 
> Como retomar, y son dos caminos distintos:
> 
>   1. Si el libro que toca esta PAUSADO en otra rama, lo que falta es el RELEVO
>      (D.50): el frente detenido y sin proceso vivo, su rama cosechada a esta, el
>      tablero puesto al dia, y solo entonces se continua desde el capitulo
>      siguiente al ultimo minado. El paso de fundir es del fundador: el bucle no
>      funde ramas.
> 
>   2. Si el encargo simplemente declaraba otro libro, corrige su linea
>      'LIBRO DE ESTA VUELTA:' con el que 'python forja.py tablero --siguiente'
>      nombra, borra este fichero y relanza.
