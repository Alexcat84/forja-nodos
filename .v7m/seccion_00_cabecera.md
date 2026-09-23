

# VUELTA 7 DEL FRENTE `marquet_turn_the_ship`: **SANEAMIENTO**. `d098`, EL BARRIDO ENTERO DE `d104` Y LA CUENTA DEL LIBRO

*Encargo en `docs/loop/PROMPT_SIGUIENTE.md`, escrito por el auditor al cerrar la `ACTA M7` (`docs/loop/ACTA_AUDITOR.md`).
Extractor `claude-sonnet-5`, MODO_INSERCION=cuarentena, CLASE: SANEAMIENTO (`python scripts/deuda.py --clase 7` da `SANEAMIENTO`,
*han pasado 5 vuelta(s) desde la primera vuelta de la linea, que todavia no ha saneado nunca y la cadencia es 5, con 35 deuda(s) pendientes*).*

| | |
|---|---|
| rama | `extraccion-marquet_turn_the_ship` |
| commit de apertura | `89fc5aa` (`git rev-parse HEAD`, tras commitear los registros pendientes del arnes que el ciclo 1 de `EXTRACTOR.md` manda pushear antes de tocar nada) |
| `gate` a la apertura | `GATE VERDE`, `346` nodos verificados |
| `guiones` a la apertura | `BARRIDO DE GUIONES VERDE` |
| candidatos en bandeja a la apertura | `20` (`ls cuarentena/marquet_turn_the_ship/*.json \| wc -l`) |
| credito a la apertura | `python forja.py credito`: `AUDITOR 0 de 3`, `CIFRA PUBLICADA 0 de 2`, `CLASE 0 de 2`, `DATO MOVIDO 0 de 2`, `REPORTE 0 de 3` (todas de la `ACTA M7`) |

### Las cuatro tareas de esta vuelta

| # | tarea | estado | resultado |
|---:|---|---|---|
| 1 | Registros: el ACTA M7 leida y sus adjudicaciones asumidas | PENDIENTE | |
| 2 | `d098`: el paso 1 de `ceder_control_reforzar_competencia_claridad` | PENDIENTE | |
| 3 | `d104`: el barrido de la bandeja entera, con el texto final | PENDIENTE | |
| 4 | La cuenta del libro | PENDIENTE | |

### Discutibles marcados ANTES de saber si acierto

| # | discutible | donde |
|---|---|---|
| | (se anexan segun aparezcan) | |
