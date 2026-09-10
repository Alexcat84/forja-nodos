# REPORTE DEL EXTRACTOR

## VUELTA 1, lote 1 (onu_consumidor), cap_02

| | |
|---|---|
| fecha | **2026-09-09**, leida del instrumento (`date`, `python -c datetime.date.today()` y `src.aduana._hoy()`, los tres dan `2026-09-09`). Ver DISCREPANCIA DECLARADA mas abajo |
| rama | `extraccion-mundo-11` (`git rev-parse --abbrev-ref HEAD`) |
| commit de apertura | `6b24d8b` (`git rev-parse HEAD` tras commitear lo pendiente, seccion 1.1) |
| lote | onu_consumidor, LOTE 1 DE CALIBRACION (D.24) |
| capitulo de extraccion | cap_02.md, apartado V-C parrafos 20 a 32 |
| cap_01.md | leido y registrado NO MINADO por la marca FRONTERA |
| nodos en el dataset al empezar | 2 (`wc -l dataset/nodos.jsonl`, corrido antes de la primera operacion) |
| inserciones autorizadas en esta vuelta | CERO. Todo queda en cuarentena (`MODO_INSERCION=cuarentena`, D.26) |

**DISCREPANCIA DECLARADA (seccion 5: la discrepancia se declara, no se resuelve
copiando).** El bloque de apertura que el encargo manda copiar trae
`fecha | 10 sep 2026`. **El instrumento corrido en esta vuelta dice 2026-09-09**,
y la misma linea la escribe el arnes en `docs/loop/loop.log`
(`[2026-09-09 23:48:46] arranque: rama extraccion-mundo-11, MODO_INSERCION=cuarentena`).
Escribo la del instrumento, porque una nota previa nunca es fuente de una cifra
nueva, y dejo la del encargo aqui al lado en vez de elegir en silencio. **La
fecha que llevan las `fuentes` de los candidatos es la del instrumento**, que es
ademas la que la aduana pondria sola (`aduana._hoy()`).

### Las cuatro tareas

| # | tarea | estado | resultado |
|---|---|---|---|
| 1 | cap_01 leido, vara como ejemplar, registrado no minado | | |
| 2 | cap_02: frontera publicada y candidatos por la aduana | | |
| 3 | informe del lote en seco | | |
| 4 | commit del capitulo | | |

### Discutibles marcados ANTES de saber si acierto

(los marco aqui segun aparecen, no al final)
