# FICHAS DE REAPERTURA DE LA FORJA

La forja esta en reposo desde la fusion del mundo 11 (tag `forja-mundo-11`, 26 sep 2026). Estas fichas son lo que
la integracion de ese mundo en My-idea encontro que la forja producia mal, y lo que tiene que cambiar el dia que se
reabra, para que el extractor no lo vuelva a producir. Las anoto el 28 sep 2026 por decision del fundador; el detalle
de lo medido vive en My-idea: `docs/SANEAMIENTO_DATASET.md` (seccion del mundo 11) y
`docs/saneamiento/instrumentos/M11_LIMPIEZA.md`.

---

## Ficha 1. La barrera de "voz de libro" (decision del fundador, 28 sep 2026, punto 4)

**Lo que paso.** 465 de los 471 nodos del mundo 11 le hablaban al cliente con voz de libro: "las tres preguntas que
el libro nombra", "el texto lo dice asi: <cita en ingles>", "la autora cuenta". En el catalogo vivo de My-idea eso
pasaba en 11 de 3.169. My-idea lo limpio a mano antes de integrar, por correccion declarada.

**Lo que la forja hereda.** La barrera que My-idea ya tiene en su guarda de voz de cliente
(`web/lib/i18n/frasesProhibidas.ts`, reglas `vozDeLibro` y `marcasInternas`): el extractor no escribe en ningun
campo de cara (titulo, resumen, pasos, entregable, condicion) "el libro", "el texto" como fuente, "el autor",
"el capitulo", ni citas en ingles; nombra el contenido directamente, en espanol, con palabras propias. Y el gate de la
forja la corre sobre cada nodo antes de aceptarlo.

**Condicion de cierre.** Un lote nuevo extraido con la forja reabierta pasa la guarda de voz de cliente de My-idea sin
una sola falta.

---

## Ficha 2. Las notas de auditoria van a su propio campo (decision del fundador, 28 sep 2026, punto 5)

**Lo que paso.** La operacion de corregir de la forja escribia en `resumen_teorico` y contamino el campo: en 237 de los
471 nodos el resumen era la nota de extraccion entera ("UNIDAD DE ORIGEN: fuentes/<libro>/cap_NN.md, lineas A a B...
POR QUE ES PROCEDIMIENTO... VA MARCADO COMO DISCUTIBLE"), en otros 48 se mezclaba con ella, y el resto eran
meta-descripciones de donde salia la pieza, con una mediana de 1.556 caracteres. El esquema de la forja dice que el
campo es "que sostiene el procedimiento y por que funciona". Ademas, al menos un entregable llevaba pegada una nota de
correccion con rutas y ordenes de consola.

**Lo que la forja cambia.** Las notas de auditoria (unidad de origen, rutas, lineas, razonamiento del extractor,
correcciones declaradas, marcas de discutible) viven en su PROPIO campo interno, como en My-idea
(`notas_extraccion`, que nunca llega a la web ni a la IA). `resumen_teorico` solo lleva el resumen, de 400 a 600
caracteres, y la operacion de corregir nunca escribe en un campo de cara lo que no es contenido para el cliente.

**Condicion de cierre.** El gate de la forja rechaza un nodo cuyo resumen o cualquier otro campo de cara contenga una
ruta de archivo, un numero de linea o una marca de auditoria (la regla `marcasInternas` de My-idea), y un resumen fuera
de 400 a 600 caracteres.
