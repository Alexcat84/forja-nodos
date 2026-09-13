
### S.3.b. **LA PRIMERA CIFRA DEL ENCARGO QUE NO ME SALE, Y LA DECLARO EN VEZ DE TRABAJARLA POR DEBAJO**

*`EXTRACTOR.md` 5: si una cifra del encargo discrepa de mi medicion, **la discrepancia se declara en
vez de resolverse copiando**. Esta la encontre al preparar el orden, antes de insertar nada.*

**LO QUE EL ENCARGO DICE:** *primero los `7` candidatos que la aduana bloqueo, **cuyos `24` pares ya
tienes leidos y cuyos veredictos ya estan escritos** en `.v24/veredictos_insercion.json`. **Son los
mas baratos: el trabajo de lectura ya esta pagado.***

Salida de `python .v25/censo_veredictos.py`, guardada en `.v25/censo_veredictos.txt`:

<!-- TALLADO: parcial salida=.v25/censo_veredictos.txt -->

| candidato bloqueado | pares en la cola de la vuelta 24 | con veredicto escrito | sin el |
|---|---:|---:|---:|
| `ajustar_franqueza_oido_oyente` | 3 | 1 | **2** |
| `cuidar_persona_completa_equipo` | 7 | 4 | **3** |
| `revisar_ciclo_responsabilidades_relaciones` | 2 | 1 | **1** |
| `elogiar_trabajo_especifico_contexto` | 3 | 1 | **2** |
| `empezar_cultura_franqueza_radical` | 4 | 1 | **3** |
| `pedir_critica_equipo_premiarla` | 3 | 2 | **1** |
| `acompaniar_mejores_equipo_socio` | 2 | 1 | **1** |
| **los 7** | **24** | **11** | # **13** |

**`11` DE LOS `24`, NO LOS `24`.** El fichero tiene `19` veredictos en total y **solo `11` son de
estos siete**: los otros `8` son de candidatos distintos. **El trabajo de lectura no estaba pagado:
estaba pagado a menos de la mitad.**

> **Y NO LO DIGO COMO REPROCHE, LO DIGO PORQUE CAMBIA LA PLANIFICACION, que es para lo que sirve una
> cifra.** El encargo llamo a estos siete *los mas baratos* y encargo el resto del orden detras. **Si
> hubiera empezado por ahi creyendo la cifra, la tanda se habria parado en el primero**, y el motivo
> habria parecido un fallo de la aduana en vez de lectura sin hacer. **La cifra buena convierte un
> tropiezo inexplicable en trece lecturas presupuestadas.**

### S.3.c. **LO QUE LA TANDA MIDIO Y NADIE HABIA MEDIDO: LA COLA NO SE VACIA, SE REALIMENTA**

*La vuelta 24 escribio que la cola de lectura **crece mientras se paga**, con un ejemplar. **Esta
vuelta lo ve funcionar cuatro veces seguidas sobre el mismo candidato**, y por eso lo publico con
sus nombres.*

**`cuidar_persona_completa_equipo` NO SE MOVIO DE LA BANDEJA EN TODA LA TANDA, Y CAMBIO DE VECINOS
CUATRO VECES**, sin que yo tocara ni una linea suya:

| pasada | pares que le faltaban | de donde salio el par nuevo |
|---:|---|---|
| **1** | `delimitar_franqueza_radical_cinco_noes`, `equilibrar_elogio_critica_equipo`, `imaginar_caso_simple_bragueta_abierta`, `manejar_enfado_persona_desafiada` | los cuatro ya vivian en el grafo al abrir |
| **2** | `ajustar_franqueza_oido_oyente` | # **entro en la pasada 1, minutos antes** |
| **3** | `elogiar_trabajo_especifico_contexto` | # **entro en la pasada 2** |
| **4** | `empezar_cultura_franqueza_radical` | # **entro en la pasada 3** |

> ### **LA CONSECUENCIA, Y ES LO QUE SE LLEVA QUIEN PLANIFIQUE LA VUELTA 26**
>
> **Un candidato bloqueado no tiene un coste fijo: tiene un coste que sube cada vez que otro entra
> delante.** Cada nodo insertado es un vecino potencial nuevo para todos los que quedan detras, y
> `cuidar_persona_completa_equipo` es el ejemplar limpio: **cuatro pasadas, cuatro pares nuevos, cero
> cambios en su fichero.**
>
> **Y ESO NO ES UN ARGUMENTO PARA CAMBIAR EL ORDEN, que es lo que invita a pensar.** `D.36` ya lo
> decidio: *entre dos ordenes posibles, el que abre la cola gana*, porque **leer de menos cuesta una
> arista que nadie sabra que falta.** Lo que si es, es un argumento para **no prometer una tanda
> entera en una vuelta**: la cola que se presupuesta al empezar no es la que se paga al acabar.
