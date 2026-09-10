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
| 1 | cap_01 leido, vara como ejemplar, registrado no minado | **CERRADA** | leido entero (19 lineas). **CERO extraidos.** Vara pasada sobre los 4 parrafos: 0 procedimientos propios. Registrado NO MINADO POR LA MARCA. **Mi vara COINCIDE con la marca**, y en el parrafo 19 por poco margen: se dice |
| 2 | cap_02: frontera publicada y candidatos por la aduana | | |
| 3 | informe del lote en seco | | |
| 4 | commit del capitulo | | |

### Discutibles marcados ANTES de saber si acierto

(los marco aqui segun aparecen, no al final)

---

## TAREA 1. `cap_01`, apartado V-B: leido, vara pasada, registrado

### 1.a. El registro, primero, para que no se confunda con lo demas

**`cap_01.md` queda NO MINADO POR LA MARCA FRONTERA.** La marca, citada de su
sede, es la linea 9 del fichero:

    fuentes/onu_consumidor/cap_01.md:9
    _Nota: seccion FRONTERA, no se mina en el nucleo (ver plan de recorte)._

Es una decision previa del fundador, tomada en el plan de recorte del mundo 11.
**No la reabro y no la discuto: la cumplo.** De `cap_01` no sale ni un candidato,
y la razon que consta es **la marca**, no mi lectura.

**Lo que sigue es lo OTRO**, y el encargo pide que no se mezclen: la vara de la
seccion 9 pasada sobre el material como EJEMPLAR de trabajo, que esta casa
todavia no tiene para material normativo.

### 1.b. Que hay dentro de `cap_01`, parrafo a parrafo, con su linea

Cuatro parrafos, lineas 13, 15, 17 y 19 del fichero. Los cito por su numero de
parrafo de la ONU y por su linea del recorte.

| parrafo | linea | que es, segun la vara de la seccion 9 | por que |
|---|---|---|---|
| 16 | `cap_01.md:13` | **POSTURA** | manda *adoptar o fomentar la adopcion de medidas apropiadas* y enumera INSTRUMENTOS (sistemas juridicos, reglamentaciones, normas, registros de seguridad). Enumerar instrumentos no es procedimentar ninguno: no dice como se hace ni uno |
| 17 | `cap_01.md:15` | **POSTURA mas una DENOMINACION mas un CRITERIO** | la denominacion es *(en lo sucesivo denominados "distribuidores")*, que es campo `denominaciones`, no nodo. El criterio es *simbolos comprensibles internacionalmente*: es requisito sobre un entregable, una linea |
| 18 | `cap_01.md:17` | **LINEA NOMBRADA sin sus pasos** | es lo mas cerca de un procedimiento que hay junto al 19: trae actor (fabricante o distribuidor), activacion (percatarse de un peligro no previsto DESPUES de introducir el producto), destinatario (autoridad competente y, segun proceda, el publico) y plazo (*sin demora*). **Le faltan los pasos, y el libro no los escribe** |
| 19 | `cap_01.md:19` | **LINEA NOMBRADA sin sus pasos, y la mas procedimental de las cuatro** | la retirada del producto defectuoso. Trae activacion (*defecto grave o peligro considerable aun cuando se utilice en forma adecuada*) y, esto es lo raro aqui, una **bifurcacion con salida**: retirar y reemplazar, o modificar, o sustituir; y *si no es posible hacerlo en un plazo prudencial*, compensar. Aun asi **no escribe los pasos**: dice que hay que llegar, no como |

### 1.c. LA TRAMPA, trabajada: el imperativo que no ejecuta

El encargo la nombra y la confirmo con el texto delante. La forma
*"Los Estados Miembros deben adoptar politicas adecuadas"* (`cap_01.md:13`, y
otra vez en `:15` y `:17`) **se lee como un imperativo y no lo es**.

**El modo gramatical no es la ejecutabilidad.** La prueba del manual es
*"existe quien lo ejecuta"*, y aqui esa prueba se contesta sola:

1. **el ejecutor no es el lector**: es un legislador, y un nodo cuyo ejecutor es
   un parlamento no lo corre nadie que lea esta casa;
2. **el entregable no se puede dar por hecho**: *politicas adecuadas*,
   *medidas apropiadas*, *plazo prudencial*. **Un paso cuya condicion de exito es
   el adjetivo `adecuado` no se puede declarar cumplido**, y un paso que no se
   puede declarar cumplido no es un paso.

**Esa es la señal barata que me llevo escrita de este ejemplar, y la propongo
para material normativo:**

> **EL ADJETIVO DE ADECUACION EN EL SITIO DEL CRITERIO ES LA FIRMA DE UNA
> POSTURA.** Cuando el entregable de una linea normativa se mide con
> *adecuado*, *apropiado*, *suficiente* o *prudencial*, la linea no traia
> criterio: traia una vara delegada a otro. Se procedimenta cuando alguien
> escribe el criterio, y ese alguien no es el libro.

Y su reverso, que es lo que si sirve: **lo que en `cap_01` tiene hueso
procedimental no es el verbo, es la BIFURCACION del parrafo 19**. Un texto
normativo empieza a ser procedimiento cuando le pone una salida al camino que
falla (*si no es posible en un plazo prudencial, compensar*), porque eso obliga
a decidir, y decidir se puede escribir en pasos. **Los verbos deonticos son
gratis; las bifurcaciones no.**

### 1.d. Si mi vara coincide con la marca: SI, y donde casi no

**COINCIDE.** Pasada la vara de la seccion 9 sobre los cuatro parrafos, **de
`cap_01` no sale ni un nodo completo**, asi que mi lectura y la marca FRONTERA
llegan al mismo sitio por caminos distintos. Eso es informacion, y es la
tranquila.

**Y aqui va la parte que el encargo pide que no me calle: el parrafo 19 esta
cerca del corte.** Es una linea nombrada con activacion propia y bifurcacion
propia; lo unico que le falta es que alguien escriba los pasos, y **los pasos que
faltan no estan en este libro**. Por la vara (*una linea solo cuenta como
procedimiento propio si trae procedimiento propio, y no solo el nombre de otro*)
**no entra**. Pero es el material de `cap_01` que un dia, con otro libro al lado,
sera un nodo de retirada de producto, y su madre sera esta linea. **Lo dejo
escrito para que no haya que releer `cap_01` para encontrarlo.**

### DISCUTIBLE 1, marcado antes de saber si acierto

**Que el parrafo 19 (`cap_01.md:19`) no sea nodo es mi lectura mas fina de esta
vuelta, y es la que primero pondria a releer.** Quien lea que trae activacion,
tres salidas y una salida de respaldo puede sostener que ahi hay procedimiento y
que los pasos son deducibles. **Yo sostengo que deducirlos seria escribirlos yo**,
y que un nodo cuyos pasos los invento no es del libro. Si me equivoco, me
equivoco por estricto, y el coste es un nodo que se escribe mas tarde.

**Nota de dependencia: este discutible NO cambia la tarea 1.** Aunque yo hubiera
leido procedimiento en el 19, la marca FRONTERA manda igual y `cap_01` no se
mina. Por eso es discutible de doctrina, no de resultado.
