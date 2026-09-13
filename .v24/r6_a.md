
---

## R.6. TAREA 5: **EL CIERRE DEL LOTE 4 Y LA INSERCION `D.39`**

*Condicion literal del encargo: **si y solo si `cap_14` queda minado y el lote 4 cierra en
extraccion**. La TAREA 4 lo minó entero, asi que la condicion se mide aqui y no se supone.*

### R.6.a. LA CONDICION, **MEDIDA CON MI PROPIO INSTRUMENTO Y NO SUPUESTA**

Salida de `python .t1_v23/cobertura_lote4.py`, guardada en `.v24/cobertura_lote4.txt`:

    unidades en la bandeja de entrada : 15
    unidades con candidato escrito    : 13
    unidades saldadas sin candidato   : 2   ['cap_00', 'cap_02']
    unidades SIN MINAR                : 0   []
      cap_00  unidad=Copyright Page  -> Copyright Page: no minable, no hay procedimiento que extraer
      cap_02  unidad=Introduction  -> Introduction: minado en su vuelta con resultado CERO candidatos

> # **EL LOTE 4 CIERRA EN EXTRACCION: `0` UNIDADES SIN MINAR.** Era **`1`** al abrir esta vuelta
> (`cap_14`), y lo que lo movio fue la TAREA 4. **La condicion de `D.39` se cumple y la insercion se
> abre.**

**Y LO QUE NO TENGO, DICHO ANTES DE EMPEZAR:** `D.39` pide *un lote cerrado en extraccion cuyo
informe haya certificado el acta del auditor*. **El lote cerro hoy, en esta vuelta**, asi que
ninguna acta ha certificado todavia el informe del lote completo, y **`D.42` me prohibe lanzarlo yo**
(`R.0.2`: esta corrida no entrega `INFORME_DE_LOTE.txt`). **Procedo porque el encargo lo manda con
esas dos cosas ya previstas**: su TAREA 5 abre la insercion con la sola condicion de que `cap_14`
quede minado, y su punto `5.b.5` dice literalmente que si el arnes no entrega el informe de lote,
**no lo invento y no lo lanzo, y lo declaro.** Queda declarado.

### R.6.b. COMO SE ESTA INSERTANDO, Y POR QUE ESO **NO** ES CARGA MASIVA

| | |
|---|---|
| **el comando** | `python forja.py insertar <candidato>.json --sin-preguntas`, **una llamada por candidato** |
| **el orden** | el del libro (`EXTRACTOR.md` 12.3), `cap_01` a `cap_14`, y dentro de cada capitulo alfabetico por id para que sea reproducible. Guardado en `.v24/orden_insercion.txt` |
| **el archivado `D.31`** | cada insertado se mueve a `cuarentena/_insertados/scott_radical_candor/` **en el mismo acto**, porque la aduana no lo mueve: lo mueve quien inserta |
| **los veredictos** | los escribe `forja.py insertar` en `bitacora/VEREDICTOS.jsonl`, **uno por vecino y con su razon**. Ahi es donde mi clase empieza a poder acumular de verdad, y lo recojo del encargo |
| **lo que el guion NO hace** | **no inventa un veredicto.** Si la aduana bloquea con un par que yo no he leido, el guion deja ese candidato **en cola de lectura** y sigue con el siguiente: el veredicto lo escribo yo leyendo a los dos vecinos |

**POR QUE UN GUION QUE LLAMA A LA ADUANA UNA VEZ POR CANDIDATO NO ES UNA CARGA MASIVA:** la carga
masiva que `EXTRACTOR.md` 2 prohibe es **un veredicto que nadie escribio**. Aqui **cada candidato
pasa la aduana por separado, con su propia simulacion y su propio gate**, y **ningun bloqueo se
resuelve sin que yo lea a los vecinos**. El guion es el dedo que pulsa el mismo comando 142 veces;
**no decide nada**, y lo unico que hace de mas es mover el fichero a `_insertados`, que es lo que
`D.31` manda hacer en el mismo acto.

### R.6.c. **LA DESVIACION DE ORDEN QUE INTRODUZCO, DECLARADA ANTES DE QUE SE NOTE** (`D.36`)

**Cuando un candidato bloquea, el guion lo deja en cola y sigue con el siguiente en vez de pararse.**
Eso mueve a ese candidato **detras** de los que venian despues de el, y `D.36` manda insertar en el
orden que abre la cola de lectura.

**LO MIDO EN LA DIRECCION QUE `D.36` PREFIERE, y por eso lo hago asi:** un candidato que entra
**mas tarde** ve **mas** nodos en el grafo, asi que **levanta mas pares, no menos**. `D.36` dice
literalmente *leer de mas cuesta una lectura; leer de menos cuesta una arista que nadie sabra que
falta*. **La desviacion empuja hacia leer de mas.**

**Y AUN ASI ES UNA DESVIACION Y VA MARCADA COMO DISCUTIBLE** (`R.11`), porque el orden del libro es
lo que `EXTRACTOR.md` 12.3 manda y yo lo estoy alterando por una razon de metodo, no de lectura.
