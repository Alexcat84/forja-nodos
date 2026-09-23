

# VUELTA 6 DEL FRENTE `marquet_turn_the_ship`: `cap_16` Y `cap_17`, EL BARRIDO DE `d104` Y EL CIERRE DEL LIBRO

*Encargo en `docs/loop/PROMPT_SIGUIENTE.md`, escrito por el auditor al cerrar la `ACTA M6` (`docs/loop/ACTA_AUDITOR.md`).
Extractor `claude-sonnet-5`, MODO_INSERCION=cuarentena, CLASE: EXTRACCION (`python scripts/deuda.py --clase 6` da `LIBRE`, `van 4 de 5`).*

| | |
|---|---|
| rama | `extraccion-marquet_turn_the_ship` |
| commit de apertura | `23d7d6e` (`git rev-parse HEAD`, tras commitear los registros pendientes del arnes que el ciclo 1 de `EXTRACTOR.md` manda pushear antes de tocar nada) |
| `gate` a la apertura | `GATE VERDE`, `346` nodos verificados |
| `guiones` a la apertura | `BARRIDO DE GUIONES VERDE` |
| candidatos en bandeja a la apertura | `20` (`ls cuarentena/marquet_turn_the_ship/*.json \| wc -l`) |
| credito a la apertura | `python forja.py credito`: `REPORTE 2 de 3` (ACTA M6), `CIFRA PUBLICADA 0 de 2`, `CLASE 0 de 2`, `DATO MOVIDO 0 de 2` |

### Las cuatro tareas de esta vuelta

| # | tarea | estado | resultado |
|---:|---|---|---|
| 1 | El remedio de `M6.9.a`: la frontera de cada capitulo se pega ENTERA, fila por pieza, sin resumen agrupado | **CERRADA** | Aplicado en las dos fronteras de la `TAREA 2`: `225` piezas totales (`15` de `cap_16`, `210` de `cap_17`), cero agrupadas, `<!-- TALLADO: salida=... -->` sin la palabra `parcial` |
| 2 | `cap_16` y `cap_17`: frontera, candidatos, pasos inventados por capitulo, muestra de fidelidad `m6` | **CERRADA** | `0` candidatos en los dos capitulos, los dos **SIN SUPERFICIE**, leidos enteros. Muestra `m6`: `cap_17` releido entero, `cap_16` por muestra, `0` pasos en los dos |
| 3 | `d104`: el barrido de la bandeja entera contra su texto de hoy | PENDIENTE | |
| 4 | La cuenta del libro y el cierre de la extraccion | PENDIENTE | |

### Discutibles marcados ANTES de saber si acierto

| # | discutible | donde |
|---|---|---|
| 1 | `cap_16` `L25` (`R9`): "pregunta a tu gente que autoridades querria tener" leida como POSTURA de una sola sugerencia, sin segunda etapa; si el auditor lee que es un procedimiento de un paso, ahi nace un candidato minimo | TAREA 2, seccion 2.a |
