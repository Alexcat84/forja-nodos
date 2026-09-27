
---

## S.3. TAREA 2: LA TANDA DE INSERCION DEL LOTE 4

### S.3.a. **EL ORDEN, ESCRITO Y COMMITEADO ANTES DE CORRER LA TANDA**

*`ACTA 24` `3.3` me lo encarga con estas palabras: **una razon dada antes es metodo, la misma razon
dada despues es justificacion, y no se distinguen leyendolas.** Asi que esta seccion se escribe y se
commitea **antes** de la primera insercion, y el commit que la lleva es anterior al commit de la
tanda. Quien dude puede comprobarlo con `git log`.*

Salida de `python .v25/orden.py`, guardada en `.v25/orden_publicado.txt`:

<!-- TALLADO: parcial salida=.v25/orden_publicado.txt -->

    1. los que la aduana BLOQUEO en la vuelta 24, con sus pares ya leidos : 7
        1. ajustar_franqueza_oido_oyente
        2. cuidar_persona_completa_equipo
        3. revisar_ciclo_responsabilidades_relaciones
        4. elogiar_trabajo_especifico_contexto
        5. empezar_cultura_franqueza_radical
        6. pedir_critica_equipo_premiarla
        7. acompaniar_mejores_equipo_socio

    2. despues, el orden del libro, alfabetico por id dentro de cada unidad : 124
       cap_06 : 8     cap_09 : 20     cap_12 : 2
       cap_07 : 25    cap_10 : 14     cap_13 : 12
       cap_08 : 12    cap_11 : 16     cap_14 : 15

    TOTAL en la bandeja del lote 4 : 131

| la decision | la razon, escrita antes |
|---|---|
| **primero los 7 bloqueados** | **sus 24 pares ya estan leidos y sus veredictos escritos** en `.v24/veredictos_insercion.json`. **Son los mas baratos: el trabajo de lectura ya esta pagado**, y meterlos primero no abre cola nueva |
| **despues el orden del libro** | `EXTRACTOR.md` 12.3: *los nodos de un mismo capitulo llegan juntos, y el primero que entra cambia lo que el segundo mide* |
| **alfabetico por id dentro de cada unidad** | es el desempate que la casa ya usa y el que la vuelta 24 uso. **No lo elijo hoy: lo heredo, y por eso no necesita argumento nuevo** |
| **cuando uno bloquee, queda en cola y sigo** | **`D.36`, impresa:** *entre dos ordenes posibles, el que abre la cola gana. Leer de mas cuesta una lectura; leer de menos cuesta una arista que nadie sabra que falta.* **Dejar en cola al bloqueado y seguir mete a ese candidato mas tarde, con mas nodos delante, y por tanto abre MAS pares, no menos** |

> ### **LA TENSION DE `D.36` LA DECLARO OTRA VEZ, Y NO PORQUE ME LA HAYAN SOSTENIDO**
>
> La misma `D.36` cierra diciendo que **ni el extractor ni el auditor deciden el orden de insercion:
> lo fija quien autoriza la insercion, que es el fundador.** El auditor no la leyo como mordida
> (`ACTA 24` `3.3`) porque lo que el fundador fijo es el orden del libro, **y ese orden no legisla
> que hacer con un candidato que la aduana bloquea a mitad de tanda**.
>
> **Lo acepto y lo repito aqui por una razon que no es la comodidad:** si manana alguien decide que
> el bloqueado para la tanda, **esta seccion dice exactamente que se hizo y por que**, y no hay que
> reconstruirlo de los ficheros.

**Y LO QUE NO ENTRA EN ESTA TANDA, DICHO ANTES DE EMPEZAR:** el lote 5 abre hoy en la TAREA 5 y por
tanto es un lote **ABIERTO**. **Sus candidatos no se insertan** (`D.39`, `EXTRACTOR.md` 15.7), y eso
no es prudencia mia: **meterlos seria una caida de dato.**
