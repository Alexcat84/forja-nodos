# CLASES CIEGAS DEL AUDITOR, frente `gerber_emyth`, vuelta 1

ESCRITO ANTES DE DESTAPAR NINGUNA RAZON. Cumple el REMEDIO 2 de la `ACTA 30`.
No hay razones que destapar en este frente: `bitacora/VEREDICTOS.jsonl` no tiene
ni una linea de `gerber_emyth`. Aun asi el fichero se escribe primero, que es lo
que el remedio manda.

LA BANDEJA ESTA VACIA. Estas clases NO son sobre candidatos: son sobre el TEXTO
FUENTE, unidad por unidad, y dicen lo que YO leo que cada unidad produce. Es la
lectura que despues comparo con la del extractor.

CLASES QUE USO, y son tres:
  PROCEDIMIENTO   la unidad dicta pasos que el lector puede ejecutar. Nodo.
  DIAGNOSTICO     la unidad describe, nombra o advierte. NO es nodo: sus pasos
                  habria que ponerlos yo, y eso es PUENTE (`D.30`).
  DISCUTIBLE      esta en la frontera: hay accion nombrada pero sin pasos propios.

| unidad | fichero | MI CLASE | lo que la sostiene |
|---|---|---|---|
| Foreword | `cap_01` | DIAGNOSTICO | autobiografia y dedicatoria. Cero imperativos dirigidos al lector |
| Introduction | `cap_02` | DIAGNOSTICO | anuncia cuatro IDEAS y publica tasas de quiebra. Material de `atribuciones`, no de `pasos_accionables` |
| Cap. 1 | `cap_03` | DIAGNOSTICO | define el Entrepreneurial Seizure y la Fatal Assumption. Son nombres, no procedimientos |
| Cap. 2 | `cap_04` | DISCUTIBLE x2 | (a) L257 observarse desde fuera durante el dia para ver que personalidad manda; (b) L278 a L285 el Future Work, el `I wonder what that business would be` |
| Cap. 3 | `cap_05` | DISCUTIBLE x1 | L114 `if your business depends on you, you don't own a business, you have a job`. Es una prueba de diagnostico enunciada, sin pasos para correrla |
| Cap. 4 | `cap_06` | DIAGNOSTICO | nombra `Management by Abdication rather than by Delegation` (L97) y no dice como delegar |
| Cap. 5 | `cap_07` | PROCEDIMIENTO x1 | L266 a L280: preparar el negocio para el crecimiento. Dicta las preguntas (donde, cuando, cuanto capital, cuanta gente, que tecnologia, cuanto espacio en Benchmark Uno, Dos y Tres), manda ESCRIBIRLO, y manda planes de contingencia mejor caso y peor caso |
| Cap. 6 | `cap_08` | PROCEDIMIENTO x2 | (a) L33 a L41, los tres pasos de Watson mas el cierre diario: dibujar como se ve la empresa acabada, preguntar como actuaria una empresa asi, actuar asi desde el principio, y al final de cada dia medir la disparidad y salir a cubrirla al dia siguiente; (b) L108 a L114, construir el modelo empezando por el CLIENTE y no por el negocio |
| Cap. 7 | `cap_09` | DIAGNOSTICO | historia de Ray Kroc y del Business Format Franchise. Cifras, no pasos |
| Cap. 8 | `cap_10` | DIAGNOSTICO | describe que ES el Franchise Prototype y cierra con las preguntas que el capitulo siguiente responde |
| Cap. 9 | `cap_11` | PROCEDIMIENTO x1 y hasta x3 | L28 a L50: fingir 5.000 replicas y las SEIS REGLAS, mas el resumen ejecutable de L238 a L256. Las reglas 2 y 4 traen procedimiento propio (L84 a L100 y L162 a L166) y podrian ser nodo aparte; las reglas 1, 3, 5 y 6 son criterios y NO lo son |

## LO QUE MI LECTURA PREDICE, y es falsable

1. Las ONCE primeras unidades del libro (`cap_01` a `cap_11`, la mitad del libro
   por cuenta de unidades) me dan entre CINCO y OCHO candidatos reales.
2. Las unidades `cap_01`, `cap_02`, `cap_03`, `cap_06`, `cap_09` y `cap_10` me dan
   CERO. Un nodo firmado sobre cualquiera de esas seis es, en mi lectura, un nodo
   con los pasos puestos por la mano que escribe y no por el libro.
3. El techo de candidatos de la vuelta (entre cinco y quince) NO se alcanza por
   orden de libro dentro de `cap_01` a `cap_11`. La vuelta que lo alcance ahi
   habra bajado la vara.
4. El grueso procedimental del libro esta de `cap_13` en adelante, y la maquina lo
   dice sin que yo lo lea: `cap_11`, `cap_13`, `cap_18` y `cap_19` son las cuatro
   unidades con conteo de lista por encima de siete.

## LOS TRES DISCUTIBLES QUE MARCO A CIEGAS

| # | unidad y linea | por que dudo |
|---|---|---|
| 1 | `cap_04` L257 | la observacion de si mismo esta dicha en UNA frase larga dentro de un dialogo. Si se parte en pasos, los pasos los pongo yo |
| 2 | `cap_04` L278 a L285 | `I wonder` es una pregunta, y una pregunta repetida tres veces no es una secuencia. La casa ya tiene doctrina: nombrar no es procedimentar |
| 3 | `cap_05` L114 | la prueba de dependencia acierta como criterio y no trae ni un paso. Puede vivir como `condiciones_activacion` de otro nodo en vez de como nodo |

---

## CORRECCION DECLARADA, misma fase ciega, SIN BORRAR LO DE ARRIBA

**Tres de mis citas de linea son IMPOSIBLES, y las caza una cuenta y no un ojo.**
En este recorte **toda linea con contenido lleva numero PAR** (las impares son las
lineas en blanco entre parrafos), medido en las 22 unidades:

    $ for f in fuentes/gerber_emyth/*.md; do awk '/^---$/{n++;next} n>=2' $f \
        | grep -n . | cut -d: -f1 \
        | awk -v F=$(basename $f .md) '{if($1%2)i++} END{print F " impares: " i+0}'; done
    cap_01 impares: 0
    ... (las 22 dan 0)

**LO QUE ESCRIBI ARRIBA Y QUEDA EN PIE, con su valor corregido al lado:**

| donde | escribi | el instrumento dice | por que fallo |
|---|---|---|---|
| `cap_04` (a) | `L257` | **`L256`** | lei el numero de un bloque ya impreso en vez de volver a grepearlo |
| `cap_06` | `L97` | **`L96`** | lo mismo |
| `cap_08` (a) | `L33 a L41` | **`L32 a L40`** | lo mismo |

**Y LAS QUE SALIERON BIEN, tambien con su instrumento:** `cap_05` `L114`,
`cap_07` `L266`, `L274` y `L280`, `cap_08` `L108`, `cap_11` `L34`, `L38` a `L48`
y `L246`.

**ES MI PROPIA ESPECIE Y LA DECLARO ASI:** son numeros cuya unica fuente era una
lectura mia, que es literalmente lo que mi `REMEDIO 1` prohibe. **Las cace ANTES
de sellar porque volvi a correr el instrumento**, que es lo que el remedio manda
hacer, y por eso no viajan a la apertura sellada. En la apertura van con su
`grep` pegado.
